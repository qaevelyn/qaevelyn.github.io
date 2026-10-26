#!/usr/bin/env python3
"""
drift_check.py — the Overseer™ for the record system. Compares what the book says
against what the manifests and tracker say, plus contact-email drift, and writes
site/DRIFT_REPORT.md. Exits 1 if drift exists (so CI and humans both see it).

Checked drifts:
  1. Ships in lookbook.html missing from ships/manifest.json
  2. Papers in white-papers/manifest.json missing from white-paper-tracker.md tables
  3. Contact emails off the standard address (owner-ruled standard:
     evelyn.caro.cloud@gmail.com) anywhere in md/html site sources

Usage:  python3 tools/records/drift_check.py [--root REPO_ROOT]
"""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

STANDARD_EMAIL = "evelyn.caro.cloud@gmail.com"
OFF_EMAIL_PATTERNS = [r"qaevelyn@pm\.me"]
SKIP_DIRS = {".git", ".github", "node_modules", "site", "_sass", "assets"}
SCAN_SUFFIXES = (".md", ".html")

SPREAD_RE = re.compile(r'<div\s+id="ship(\d+)"\s+class="spread"', re.S)
PAPER_LINK_RE = re.compile(r"/white-papers/([^/#\s)]+?)/")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    findings = []

    # 1. ships: book vs manifest
    html = (root / "lookbook.html").read_text(encoding="utf-8")
    book_ships = sorted({int(n) for n in SPREAD_RE.findall(html)})
    ships_manifest = json.loads((root / "ships" / "manifest.json").read_text(encoding="utf-8"))
    known = {s.get("number") for s in ships_manifest.get("ships", [])}
    known |= {int(re.sub(r"\D", "", k)) for k in ships_manifest.get("suite", {})
              if re.sub(r"\D", "", k).isdigit()}
    missing_ships = [n for n in book_ships if n not in known]
    if missing_ships:
        findings.append(f"SHIPS: lookbook has ship(s) {missing_ships} absent from ships/manifest.json")
    elif book_ships != sorted(known):
        findings.append(f"SHIPS: manifest lists {sorted(known)} but book carries {book_ships} "
                        f"(extra manifest rows without book spreads — report, do not delete)")

    # 2. papers: manifest vs tracker
    papers = json.loads((root / "white-papers" / "manifest.json").read_text(encoding="utf-8"))["white_papers"]
    manifest_ids = {p["id"] for p in papers}
    tracker = (root / "white-papers" / "white-paper-tracker.md").read_text(encoding="utf-8")
    tracker_ids = set(PAPER_LINK_RE.findall(tracker))
    # infra rows that live outside the published tables by design: redirect + changelog + tracker self-link
    INFRA_UNTRACKED = {"White_Paper_AI_Collaboration_Case_Study", "record-changelog"}
    untracked = manifest_ids - tracker_ids - INFRA_UNTRACKED
    if untracked:
        findings.append("PAPERS: in manifest but not in tracker -> "
                        + ", ".join(sorted(untracked)))
    stale_tracker_only = tracker_ids - manifest_ids - {"white-paper-tracker"}
    if stale_tracker_only:
        findings.append("PAPERS: in tracker but not in manifest -> "
                        + ", ".join(sorted(stale_tracker_only)))

    # 3. contact email drift
    for path in sorted(root.rglob("*")):
        if not path.suffix.lower() in SCAN_SUFFIXES:
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue
        for pat in OFF_EMAIL_PATTERNS:
            for m in re.finditer(pat, text):
                line_no = text[: m.start()].count("\n") + 1
                findings.append(f"EMAIL: {path.relative_to(root)}:{line_no} uses off-standard address")

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    report = [
        "# DRIFT REPORT",
        f"Generated: {stamp} by tools/records/drift_check.py",
        "",
        "Standard contact email: " + STANDARD_EMAIL,
        "",
    ]
    if findings:
        report += [f"- {f}" for f in findings]
        report += ["", f"**{len(findings)} drift finding(s). Fix or rule; the check reruns on next push.**"]
    else:
        report.append("**No drift. Book, manifests, tracker, and contact email agree.**")

    out = root / "site" / "DRIFT_REPORT.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(report) + "\n", encoding="utf-8")

    print(f"drift_check: {len(findings)} finding(s) — report at {out.relative_to(root)}")
    for f in findings:
        print("  - " + f)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
