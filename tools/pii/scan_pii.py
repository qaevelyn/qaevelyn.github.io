#!/usr/bin/env python3
# A Mirror of My Becoming™ — Ship 14: Quartermaster™
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Evelyn Caro — https://qaevelyn.github.io
# Commercial licensing without AGPL-3.0 obligations: see LICENSE-COMMERCIAL.md
"""
Quartermaster — deterministic PII/secret gate for the fleet's repositories.

The quartermaster inspects every crate before it goes aboard. Contract
(matches the lane philosophy): refusal is loud, explained, and final.
No ML, no confidence scores, no guessing. Every finding cites a rule id,
the exact file:line, and a fixed, human-written explanation of what the
rule matches and why it is dangerous in a public repository.

Usage:
  scan_pii.py --staged                 # pre-commit hook: scan staged changes
  scan_pii.py --git-diff SPEC          # scan files changed vs a git rev-spec
                                       #   e.g. "origin/master...HEAD"
  scan_pii.py PATH [PATH ...]          # scan explicit files/dirs
  scan_pii.py --all                    # baseline: scan every text file in repo
  scan_pii.py --private                # private-repo mode: suppress identity
                                       #   WARNs (credentials still BLOCK)

Exit codes: 0 = clean (or allowlisted), 1 = BLOCK findings, 2 = config/usage error.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------- rules ----
# Each rule: id, severity, regex, "why" (fixed explanation), "fix" (fixed
# remediation). The why/fix text is the no-guessing contract: the same rule
# always produces the same explanation, every time, in every repo.

RULES = [
    {
        "id": "AWS_ACCESS_KEY_ID",
        "severity": "BLOCK",
        "pattern": r"\b(?:AKIA|ASIA|ABIA|ACCA)[0-9A-Z]{16}\b",
        "why": ("AWS access key IDs are exactly 20-character uppercase "
                "identifiers beginning AKIA/ASIA/ABIA/ACCA. Paired with its "
                "secret, this identifier grants programmatic AWS access to "
                "everything its IAM principal can reach."),
        "fix": ("Rotate the key in AWS IAM immediately, remove it from the "
                "file, and if it was ever pushed, purge the history "
                "(git filter-repo) — rotation alone is not enough if the "
                "secret rode with it."),
    },
    {
        "id": "AWS_SECRET_KEY",
        "severity": "BLOCK",
        "pattern": r"(?i)aws[\w\-]{0,24}secret[\w\-]{0,24}[:=]\s*[\"']?[A-Za-z0-9/+=]{40}",
        "why": ("A field whose name contains aws…secret is assigned a "
                "40-character base-64-style value — the exact shape of an AWS "
                "secret access key. That value is the credential itself."),
        "fix": ("Rotate the AWS key pair in IAM, remove the value, and purge "
                "history if it was ever pushed."),
    },
    {
        "id": "GITHUB_TOKEN",
        "severity": "BLOCK",
        "pattern": r"\b(?:gh[pousr]_[A-Za-z0-9]{20,255}|github_pat_[A-Za-z0-9_]{22,255})\b",
        "why": ("GitHub personal access tokens begin ghp_/gho_/ghu_/ghs_/ghr_ "
                "or github_pat_. A leaked token grants repository or account "
                "access to whoever holds it until it is revoked."),
        "fix": ("Revoke the token at github.com/settings/tokens, issue a new "
                "one, store it in a secret or keychain — never in the tree."),
    },
    {
        "id": "SERVICE_API_KEY",
        "severity": "BLOCK",
        "pattern": r"\bsk-[A-Za-z0-9_\-]{20,}\b",
        "why": ("A bearer credential beginning sk- (OpenAI/Anthropic-style "
                "API key shape). Anyone holding it spends the account's "
                "quota and reads what the key can read."),
        "fix": ("Revoke/rotate the key at the provider's dashboard and store "
                "the replacement in an environment variable or secret store."),
    },
    {
        "id": "GOOGLE_API_KEY",
        "severity": "BLOCK",
        "pattern": r"\bAIza[0-9A-Za-z_\-]{35}\b",
        "why": ("Google API keys are 39 characters beginning AIza. A leaked "
                "key bills to your project until disabled."),
        "fix": ("Delete or regenerate the key in Google Cloud Console → "
                "APIs & Services → Credentials."),
    },
    {
        "id": "SLACK_TOKEN",
        "severity": "BLOCK",
        "pattern": r"\bxox[baprs]-[0-9A-Za-z\-]{10,}\b",
        "why": ("Slack tokens begin xoxb/xoxa/xoxp/xoxr/xoxs. A leaked token "
                "can read and post in the workspace it belongs to."),
        "fix": ("Revoke at api.slack.com/apps → OAuth & Permissions and "
                "re-issue."),
    },
    {
        "id": "JWT",
        "severity": "BLOCK",
        "pattern": r"\beyJ[A-Za-z0-9_\-]{15,}\.[A-Za-z0-9_\-]{15,}\.[A-Za-z0-9_\-]{8,}\b",
        "why": ("A JSON Web Token: three base64url segments beginning eyJ "
                "(an encoded '{\"'). It is a signed credential — unexpired, "
                "it grants every claim encoded inside it."),
        "fix": ("Remove the token; if it was real, let it expire or rotate "
                "the signing secret, and never commit re-issued tokens."),
    },
    {
        "id": "PRIVATE_KEY",
        "severity": "BLOCK",
        "pattern": r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY( BLOCK)?-----",
        "why": ("The header of a private key block (RSA/EC/DSA/OpenSSH/PGP). "
                "This is the credential material itself, not a reference to "
                "it. A public repo with a private key is an incident."),
        "fix": ("Treat the key as compromised the moment it is staged: "
                "generate a new keypair, update every place the old public "
                "key is registered, purge history if pushed."),
    },
    {
        "id": "SSN",
        "severity": "BLOCK",
        "pattern": r"\b(?!000|666|9\d{2})\d{3}[- ](?!00)\d{2}[- ](?!0000)\d{4}\b",
        "why": ("Matches the strict US Social Security number shape "
                "(3-2-4 digits, invalid-area exclusions applied). SSNs are "
                "the single highest-value identity-theft target."),
        "fix": ("Remove the number. If genuine SSN data ever reached a "
                "public repo, treat it as a breach: notify, and purge "
                "history."),
    },
    {
        "id": "CREDIT_CARD",
        "severity": "BLOCK",
        "why": ("A 13–19 digit sequence that passes the Luhn checksum — the "
                "defining property of a payment card number. Random digit "
                "strings fail Luhn; card numbers do not."),
        "fix": ("Remove the number. If it is a real card, cancel and reissue "
                "it — publication of the number alone is enough."),
    },
    {
        "id": "KEY_VALUE_CREDENTIAL",
        "severity": "BLOCK",
        "pattern": r"(?i)\b(?:api[_-]?key|secret|password|passwd|token)\b\s*[:=]\s*[\"'][A-Za-z0-9+/=_\-]{16,}[\"']",
        "why": ("A field literally named api key/secret/password/token is "
                "assigned a 16+ character opaque value. The name says what "
                "it is; the shape says it is not prose."),
        "fix": ("Move the value to an environment variable, secret store, "
                "or the allowlist if it is a documented placeholder."),
    },
    {
        "id": "EMAIL",
        "severity": "WARN",
        "pattern": r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}",
        "why": ("An email address. If this is your intentional public "
                "contact address, allowlist it with a reason. If it is a "
                "personal, employer, or third-party address, remove it — "
                "published emails harvest into spam and phishing lists."),
        "fix": ("Remove it, or add it to .pii-allowlist.json with a reason "
                "so the decision is recorded."),
    },
    {
        "id": "PHONE_US",
        "severity": "WARN",
        "pattern": r"(?:\+?1[-. ]?)?\(?\d{3}\)?[-. ]\d{3}[-. ]\d{4}\b",
        "why": ("Matches the North-American phone number shape. Phone "
                "numbers in public text feed SMS-phishing and number "
                "enumeration."),
        "fix": ("Remove it, or allowlist it with a reason if it is an "
                "intentional public contact number."),
    },
    {
        "id": "DOB",
        "severity": "WARN",
        "pattern": r"(?i)\b(?:dob|date[ -]of[ -]birth|born[ -]on)\b\s*[:\-]?\s*\d{1,4}[/.-]\d{1,2}[/.-]\d{2,4}",
        "why": ("A labeled date of birth. DOB is a core identity-verification "
                "answer used by banks and credit bureaus."),
        "fix": ("Remove it. There is no intentional-public case for a DOB in "
                "a repository."),
    },
    {
        "id": "STREET_ADDRESS",
        "severity": "WARN",
        "pattern": r"\b\d{1,5}\s+[A-Za-z0-9.\- ]{3,40}\s(?:Street|St|Avenue|Ave|Boulevard|Blvd|Road|Rd|Lane|Ln|Drive|Dr|Court|Ct|Way)\b\.?",
        "why": ("Looks like a street address (house number + name + street "
                "type). Home addresses in public repos are a physical-safety "
                "leak."),
        "fix": ("Remove it, or allowlist with a reason if it is a business "
                "address you intend to publish."),
    },
    {
        "id": "IP_ADDRESS",
        "severity": "WARN",
        "pattern": r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)\b",
        "why": ("An IPv4 address. Internal addresses leak network topology; "
                "external ones invite scanning of whatever runs there."),
        "fix": ("Replace with documentation addresses (192.0.2.x, "
                "198.51.100.x, 203.0.113.x are reserved for docs) or "
                "allowlist with a reason."),
    },
    {
        "id": "BEARER_TOKEN",
        "severity": "WARN",
        "pattern": r"(?i)\bbearer\s+[A-Za-z0-9._\-]{20,}",
        "why": ("A Bearer authorization value. Tutorial prose often uses "
                "fake ones; if this one is real it is a live credential."),
        "fix": ("Replace with a placeholder like Bearer <token>, or "
                "allowlist with a reason if it is documented as fake."),
    },
]

# rules that carry identity information — suppressed by --private
IDENTITY_RULES = {"EMAIL", "PHONE_US", "DOB", "STREET_ADDRESS", "IP_ADDRESS"}

# files/dirs never scanned
SKIP_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".zip", ".gz",
    ".tgz", ".bz2", ".xz", ".7z", ".rar", ".mp3", ".mp4", ".mov", ".wav",
    ".woff", ".woff2", ".ttf", ".otf", ".eot", ".jar", ".pyc", ".class",
    ".so", ".dylib", ".dll", ".exe", ".bin", ".sqlite", ".db",
}
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__"}
# the gate never flags itself (both current and legacy doc names)
SKIP_NAMES = {"scan_pii.py", "QUARTERMASTER.md", "PII-GATE.md"}
MAX_BYTES = 5 * 1024 * 1024

CANDIDATE_CARD = re.compile(r"\b\d(?:[ -]?\d){12,18}\b")
COMPILED = {r["id"]: re.compile(r["pattern"]) for r in RULES if r.get("pattern")}


def luhn_ok(digits: str) -> bool:
    total = 0
    for i, ch in enumerate(reversed(digits)):
        d = int(ch)
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def redact(text: str) -> str:
    """Deterministic redaction for BLOCK findings: never reprint a secret."""
    return f"{text[:4]}…({len(text)} chars)"


def load_allowlist(path: Path) -> list:
    """Every allowlist entry REQUIRES a reason. A malformed file is exit 2 —
    a silent or guessed allowance would break the no-guessing contract."""
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        print(f"QUARTERMASTER CONFIG ERROR: cannot parse {path}: {e}",
              file=sys.stderr)
        sys.exit(2)
    entries = data.get("entries", []) if isinstance(data, dict) else data
    if not isinstance(entries, list):
        print(f"QUARTERMASTER CONFIG ERROR: {path} must contain a list or "
              '{"entries": [...]}.', file=sys.stderr)
        sys.exit(2)
    for i, e in enumerate(entries):
        if not isinstance(e, dict) or not e.get("value"):
            print(f"QUARTERMASTER CONFIG ERROR: allowlist entry #{i + 1} in "
                  f"{path} has no 'value'.", file=sys.stderr)
            sys.exit(2)
        if not str(e.get("reason", "")).strip():
            print(f"QUARTERMASTER CONFIG ERROR: allowlist entry for "
                  f"'{e.get('value')}' in {path} has no 'reason'. "
                  "Every allowance must be explained — no guessing.",
                  file=sys.stderr)
            sys.exit(2)
    return entries


def is_allowlisted(entries: list, rule_id: str, value: str):
    for i, e in enumerate(entries):
        if e["value"] != value:
            continue
        if "rule" in e and e["rule"] != rule_id:
            continue
        return i, e["reason"]
    return None


def git_files(spec_args: list) -> list:
    try:
        out = subprocess.run(
            ["git"] + spec_args, capture_output=True, text=True, check=True
        ).stdout
    except subprocess.CalledProcessError as e:
        print(f"QUARTERMASTER ERROR: git failed ({' '.join(spec_args)}): "
              f"{e.stderr.strip()}", file=sys.stderr)
        sys.exit(2)
    return [f for f in out.split("\0") if f]


def walk_files(root: Path) -> list:
    files = []
    for p in sorted(root.rglob("*")):
        if p.is_dir():
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        files.append(str(p))
    return files


def should_skip(path: Path):
    if path.name in SKIP_NAMES:
        return "gate documentation"
    if path.name == ".pii-allowlist.json":
        return "allowlist itself"
    if path.suffix.lower() in SKIP_EXTENSIONS:
        return "binary/media extension"
    try:
        head = path.open("rb").read(8192)
    except OSError:
        return "unreadable"
    if b"\x00" in head:
        return "binary content"
    return None


def scan_line(line: str, rules: list, entries: list):
    """Return (findings, allowlisted) for one line."""
    findings, allowed = [], []
    for rule in rules:
        rid = rule["id"]
        if rid == "CREDIT_CARD":
            for m in CANDIDATE_CARD.finditer(line):
                digits = re.sub(r"\D", "", m.group())
                if 13 <= len(digits) <= 19 and luhn_ok(digits):
                    _record(rule, rid, m.group(), entries, findings, allowed)
            continue
        for m in COMPILED[rid].finditer(line):
            _record(rule, rid, m.group(), entries, findings, allowed)
    return findings, allowed


def _record(rule, rid, value, entries, findings, allowed):
    hit = is_allowlisted(entries, rid, value)
    if hit is not None:
        allowed.append((rid, value, hit))
        return
    findings.append((rule, value))


def scan_file(path: Path, rules: list, entries: list):
    findings, allowed = [], []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        print(f"QUARTERMASTER WARNING: cannot read {path}: {e}")
        return findings, allowed
    for n, line in enumerate(text.splitlines(), 1):
        f, a = scan_line(line, rules, entries)
        for rule, value in f:
            findings.append((path, n, rule, value))
        for rid, value, hit in a:
            allowed.append((path, n, rid, value, hit))
    return findings, allowed


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Quartermaster — deterministic PII/secret gate.")
    ap.add_argument("--staged", action="store_true",
                    help="scan files staged for commit (pre-commit)")
    ap.add_argument("--git-diff", metavar="SPEC",
                    help="scan files changed vs a git rev-spec")
    ap.add_argument("--all", action="store_true",
                    help="scan every text file in the repo (baseline)")
    ap.add_argument("--private", action="store_true",
                    help="private-repo mode: suppress identity WARNs")
    ap.add_argument("--allowlist", default=".pii-allowlist.json")
    ap.add_argument("paths", nargs="*", help="explicit files/dirs to scan")
    args = ap.parse_args()

    entries = load_allowlist(Path(args.allowlist))
    rules = [r for r in RULES
             if not (args.private and r["id"] in IDENTITY_RULES)]

    if args.staged:
        files = git_files(["diff", "--cached", "--name-only",
                           "--diff-filter=ACMR", "-z"])
    elif args.git_diff:
        files = git_files(["diff", "--name-only", "--diff-filter=ACMR",
                           "-z", "--", args.git_diff])
    elif args.all:
        files = walk_files(Path("."))
    elif args.paths:
        files = []
        for p in args.paths:
            pp = Path(p)
            if pp.is_dir():
                files += walk_files(pp)
            else:
                files.append(str(pp))
    else:
        ap.error("nothing to scan: use --staged, --git-diff, --all, or paths")

    findings, allowed, skipped = [], [], []
    for f in files:
        p = Path(f)
        if not p.exists() or not p.is_file():
            continue
        skip = should_skip(p)
        if skip:
            skipped.append((f, skip))
            continue
        if p.stat().st_size > MAX_BYTES:
            skipped.append((f, "size > 5MB"))
            continue
        fnd, alw = scan_file(p, rules, entries)
        findings += fnd
        allowed += alw

    for f, why in skipped:
        print(f"skip  {f}  ({why})")

    for path, n, rid, value, (idx, reason) in allowed:
        print(f"allow {path}:{n}  {rid}  {value}")
        print(f"      allowlist entry #{idx + 1}: {reason}")

    for path, n, rule, value in findings:
        sev = rule["severity"]
        shown = value if sev == "WARN" else redact(value)
        print(f"[{sev}] rule={rule['id']}  {path}:{n}")
        print(f"  match: {shown}")
        print(f"  why : {rule['why']}")
        print(f"  fix : {rule['fix']}")
        print()

    blocks = sum(1 for _, _, r, _ in findings if r["severity"] == "BLOCK")
    warns = sum(1 for _, _, r, _ in findings if r["severity"] == "WARN")

    if blocks:
        print(f"QUARTERMASTER: REFUSED — {blocks} blocking finding(s), "
              f"{warns} warning(s). Nothing rides until it is explained.")
        return 1
    print(f"QUARTERMASTER: PASSED — {blocks} blocking, {warns} warning(s), "
          f"{len(allowed)} allowlisted, {len(skipped)} skipped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
