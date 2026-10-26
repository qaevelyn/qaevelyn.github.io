#!/usr/bin/env python3
"""
build_ships_manifest.py — lookbook.html is the book; the manifest must never lag it.

Regenerates ships/manifest.json from the book (ground truth for WHICH ships exist,
their titles, narratives, spread anchors) while preserving all rich metadata already
in the manifest (notebooks, videos, tags, licenses, receipts).

Rules honored:
- Append-only: existing entries are never deleted; missing ships are added as stubs.
- Titles in the manifest are owner-curated: drift vs. the book is REPORTED, not overwritten.
- Statuses are owner-set via STATUS_OVERRIDES; automation never invents status.

Usage:  python3 tools/records/build_ships_manifest.py [--root REPO_ROOT]
Exit 0 always (it heals). Print a change summary.
"""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

SHIP_SECTION = {n: ("ships" if n <= 5 else "suite") for n in range(1, 20)}
STATUS_OVERRIDES = {
    8: "concept; public flip pending",
    9: "sealed — architecture sealed",
    11: "published 2026-10-17 — template edition, prepared for a fellow student",
}

SPREAD_RE = re.compile(
    r'<div\s+id="(ship\d+)"\s+class="spread"([^>]*)>(.*?)(?=<div\s+id="|\Z)',
    re.S,
)
H3_RE = re.compile(r"<h3>(.*?)</h3>", re.S)
NARRATIVE_RE = re.compile(
    r'<div class="ship-narrative">(.*?)</div>', re.S
)
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')


def strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    return re.sub(r"\s+", " ", s).strip()


def parse_book(root: Path) -> dict:
    html = (root / "lookbook.html").read_text(encoding="utf-8")
    ships = {}
    for m in SPREAD_RE.finditer(html):
        ship_id, attrs_html, body = m.group(1), m.group(2), m.group(3)
        num = int(re.sub(r"\D", "", ship_id))
        attrs = dict(ATTR_RE.findall(attrs_html))
        h3 = H3_RE.search(body)
        narr = NARRATIVE_RE.search(body)
        ships[num] = {
            "id": ship_id,
            "book_title": strip_tags(h3.group(1)) if h3 else "",
            "toc_parent": attrs.get("data-toc-parent", ""),
            "toc_child": attrs.get("data-toc-child", ""),
            "narrative": strip_tags(narr.group(1)) if narr else "",
            "anchor": f"lookbook.html#{ship_id}",
        }
    return ships


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    mpath = root / "ships" / "manifest.json"
    manifest = json.loads(mpath.read_text(encoding="utf-8"))
    book = parse_book(root)

    by_number = {}
    for i, s in enumerate(manifest.get("ships", [])):
        if isinstance(s.get("number"), int):
            by_number[s["number"]] = i

    suite = manifest.setdefault("suite", {})
    added, lookbook_blocks, drift = [], [], []

    for num, b in sorted(book.items()):
        lb = {
            "lookbook": {
                "h3_title": b["book_title"],
                "toc_parent": b["toc_parent"],
                "toc_child": b["toc_child"],
                "narrative": b["narrative"],
                "spread_anchor": b["anchor"],
                "synced": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            }
        }
        if num in by_number:
            entry = manifest["ships"][by_number[num]]
            if entry.get("title") and b["book_title"] and \
               entry["title"].split("—")[0].strip() != b["book_title"].split("—")[0].strip():
                drift.append(f"Ship {num}: manifest title '{entry['title']}' vs book '{b['book_title']}'")
            entry.update(lb)
            lookbook_blocks.append(num)
        elif f"ship{num}" in suite:
            suite[f"ship{num}"].update(lb)
            lookbook_blocks.append(num)
        else:
            stub = {
                "id": b["id"],
                "number": num,
                "title": b["book_title"] or f"Ship {num}",
                "status": STATUS_OVERRIDES.get(num, ""),
                "portfolio": {"spread_anchor": b["anchor"]},
            }
            stub.update(lb)
            if SHIP_SECTION.get(num) == "ships":
                manifest["ships"].append(stub)
                by_number[num] = len(manifest["ships"]) - 1
            else:
                suite[f"ship{num}"] = stub
            added.append(num)
            lookbook_blocks.append(num)

    for num, ov in STATUS_OVERRIDES.items():
        holder = (
            manifest["ships"][by_number[num]] if num in by_number
            else suite.get(f"ship{num}")
        )
        if holder is not None and not holder.get("status"):
            holder["status"] = ov

    info = manifest.setdefault("manifest_info", {})
    info["purpose"] = "Single source of truth for all ships in the book (auto-synced from lookbook.html)"
    info["update_workflow"] = (
        "AUTOMATED: ships/manifest.json regenerates from lookbook.html via "
        "tools/records/build_ships_manifest.py (GitHub Action records-sync). "
        "Owner edits rich metadata (videos, tags, licenses) freely; the book decides the roster."
    )

    mpath.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"lookbook ships found : {sorted(book)}")
    print(f"lookbook blocks added: {sorted(lookbook_blocks)}")
    print(f"NEW stub entries     : {added if added else 'none'}")
    for d in drift:
        print(f"TITLE DRIFT (reported, not changed): {d}")
    print(f"ships/manifest.json written — {len(manifest.get('ships', []))} array ships, "
          f"{len(suite)} suite ships")
    return 0


if __name__ == "__main__":
    sys.exit(main())
