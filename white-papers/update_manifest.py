#!/usr/bin/env python3
"""Manifest self-inventory: scans white-papers/*.md front matter, syncs manifest.json. Newest first."""
import json, re, glob, os

ROOT = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(ROOT, "manifest.json")

def parse_fm(path):
    with open(path) as f:
        text = f.read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m: return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm

EXCLUDE = {"white-paper-tracker"}  # tools, not papers

entries = []
for path in glob.glob(os.path.join(ROOT, "*.md")):
    fm = parse_fm(path)
    if os.path.basename(path).replace(".md", "") in EXCLUDE: continue
    if not fm or "permalink" not in fm or "title" not in fm: continue
    permalink = fm.get("permalink", "")
    live_url = "https://qaevelyn.github.io" + permalink if permalink else ""
    entries.append({
        "id": os.path.basename(path).replace(".md", ""),
        "title": fm.get("title", ""),
        "subtitle": fm.get("subtitle", ""),
        "author": fm.get("author", "Evelyn Caro"),
        "date": fm.get("date", ""),
        "type": fm.get("type", "white-paper"),
        "permalink": permalink,
        "live_url": live_url,
        "file": "white-papers/" + os.path.basename(path),
        "status": "published"
    })

entries.sort(key=lambda e: e["date"], reverse=True)

with open(MANIFEST) as f: manifest = json.load(f)
manifest["white_papers"] = entries
with open(MANIFEST, "w") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"manifest synced: {len(entries)} papers, newest: {entries[0]['date']} - {entries[0]['title'][:60]}")
