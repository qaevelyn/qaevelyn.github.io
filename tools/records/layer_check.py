#!/usr/bin/env python3
"""
layer_check.py — canonical-source enforcement between markdown records and their
rendered static pages. The owner ruled 2026-10-26: when the layers disagree in
both directions, both directions are reconciled and one layer is set canonical.
Canonical status that is not enforced is not canonical.

Checks per pair (md <-> index.html), both directions:
  - every md table row's meaningful cells render on the static page
  - every static table row's cells exist in the canonical md
  - every md heading (## and deeper) appears on the static page
  - every static h2/h3 heading exists in the canonical md

Report: site/LAYER_REPORT.md. Exit 1 on drift.
Usage:  python3 tools/records/layer_check.py [--root REPO_ROOT]
"""
import argparse
import io
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

MIN_CELL = 12
MAX_PER_FILE = 8

DEEP_PAIRS = [
    ("white-papers/record-changelog.md", "white-papers/record-changelog/index.html"),
    ("white-papers/white-paper-tracker.md", "white-papers/white-paper-tracker/index.html"),
]


def norm(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = (s.replace("&amp;", "&").replace("&lt;", "<")
          .replace("&gt;", ">").replace("&nbsp;", " "))
    return re.sub(r"\s+", " ", s).strip().lower()


def delink(s: str) -> str:
    return re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)


def md_rows(text: str):
    rows = []
    for ln in text.split("\n"):
        t = ln.strip()
        if t.startswith("|") and set(t) - {"|", "-", ":", " "}:
            cells = [c.strip() for c in t.strip("|").split("|")]
            if cells:
                rows.append(cells)
    return rows


def html_rows(html: str):
    rows = []
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S):
        cells = [norm(c) for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", tr, re.S)]
        if cells:
            rows.append(cells)
    return rows


def md_headings(text: str):
    return [norm(m.group(2)) for m in re.finditer(r"^(#{2,4})\s+(.+)$", text, re.M)
            if len(m.group(2).strip()) >= MIN_CELL]


def html_headings(html: str):
    return [norm(t) for t in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", html, re.S)
            if len(norm(t)) >= MIN_CELL]


def check_pair(root: Path, md_rel: str, html_rel: str, findings: list) -> None:
    mp, hp = root / md_rel, root / html_rel
    if not (mp.exists() and hp.exists()):
        return
    md = mp.read_text(encoding="utf-8")
    html = hp.read_text(encoding="utf-8")
    htext, mtext = norm(html), norm(delink(md))
    n = 0
    for i, cells in enumerate(md_rows(md), 1):
        for c in cells:
            cn = norm(delink(c))
            if len(cn) >= MIN_CELL and cn not in htext:
                findings.append(f"{md_rel} row {i}: canonical cell not rendered -> \"{cn[:70]}\"")
                n += 1
                break
        if n >= MAX_PER_FILE:
            findings.append(f"{md_rel}: ... further md->static findings suppressed")
            break
    n = 0
    for i, cells in enumerate(html_rows(html), 1):
        for c in cells:
            if len(c) >= MIN_CELL and c not in mtext:
                findings.append(f"{html_rel} row {i}: static row absent from canonical md -> \"{c[:70]}\"")
                n += 1
                break
        if n >= MAX_PER_FILE:
            findings.append(f"{html_rel}: ... further static->md findings suppressed")
            break
    for h in md_headings(md):
        if h not in htext:
            findings.append(f"{md_rel}: heading not rendered -> \"{h[:70]}\"")
    for h in html_headings(html):
        if h not in mtext:
            findings.append(f"{html_rel}: heading absent from canonical md -> \"{h[:70]}\"")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    findings = []
    for md_rel, html_rel in DEEP_PAIRS:
        check_pair(root, md_rel, html_rel, findings)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = ["# LAYER REPORT",
             f"Generated: {stamp} by tools/records/layer_check.py",
             "",
             "Owner ruling 2026-10-26: both directions reconcile into the canonical md; the static page renders it. Drift here means a layer moved without the other."]
    lines += [f"- {f}" for f in findings] if findings else ["", "**No drift. Canonical md and rendered static agree, both directions.**"]
    out = root / "site" / "LAYER_REPORT.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"layer_check: {len(findings)} finding(s) — report at {out.relative_to(root)}")
    for f in findings:
        print("  - " + f)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
