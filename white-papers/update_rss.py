#!/usr/bin/env python3
"""RSS feed generator: builds feed.xml from manifest.json. Newest first. Runs with the manifest sync."""
import json, os, html
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "white-papers", "manifest.json")
FEED = os.path.join(ROOT, "papers-feed.xml")
SITE = "https://qaevelyn.github.io"

with open(MANIFEST) as f:
    manifest = json.load(f)

papers = [p for p in manifest["white_papers"]
          if p.get("status") == "published" and p.get("permalink")]
papers.sort(key=lambda p: p.get("date", ""), reverse=True)

def rfc822(d):
    try:
        dt = datetime.strptime(d, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        return dt.strftime("%a, %d %b %Y %H:%M:%S GMT")
    except Exception:
        return ""

items = []
for p in papers[:20]:
    title = html.escape(p.get("title", "Untitled"))
    link = SITE + p["permalink"]
    desc = html.escape(p.get("subtitle", ""))
    items.append(
        "    <item>\n"
        f"      <title>{title}</title>\n"
        f"      <link>{link}</link>\n"
        f"      <guid isPermaLink=\"true\">{link}</guid>\n"
        f"      <pubDate>{rfc822(p.get('date',''))}</pubDate>\n"
        f"      <description>{desc}</description>\n"
        "    </item>")

last_build = rfc822(papers[0]["date"]) if papers else datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")

feed = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    "<rss version=\"2.0\">\n"
    "  <channel>\n"
    "    <title>Evelyn - Published Works</title>\n"
    f"    <link>{SITE}</link>\n"
    "    <description>The corpus of Evelyn: sovereign AI builder, independent journalist. Every claim sourced, every gap flagged, no invented precision.</description>\n"
    "    <language>en-us</language>\n"
    f"    <lastBuildDate>{last_build}</lastBuildDate>\n"
    + "\n".join(items) + "\n"
    "  </channel>\n"
    "</rss>\n")

with open(FEED, "w") as f:
    f.write(feed)
print(f"feed.xml written: {len(papers)} papers, newest {papers[0]['date'] if papers else 'n/a'}")
