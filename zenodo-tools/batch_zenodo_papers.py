#!/usr/bin/env python3
"""Batch-create one Zenodo deposit per white-paper PDF and print the DOIs.

Owner flow (audit No. 5, item O2):
  1. export ZENODO_TOKEN=...   (zenodo.org -> Settings -> Applications ->
     Personal access tokens, scope "deposit:write"; SANDBOX=true for a dry run)
  2. run this script FROM THE REPO ROOT of qaevelyn.github.io
  3. it finds each paper's PDF at white-papers/<slug>/<slug>.pdf, refuses to
     run if any is missing (audit finding O1 - commit the PDFs first),
     reads each paper's real <title> and meta description from its index.html
     so nothing is invented, creates the deposit, uploads the PDF, and
     publishes; it writes zenodo-dois.tsv (slug -> DOI) when done.

Publishing is per-deposit and permanent; use SANDBOX=true first to see the
flow end to end without minting real DOIs. Nothing is uploaded for the ships
- they already carry DOIs (verified in audit No. 5).
"""
import html
import json
import os
import re
import sys
import urllib.request

API = "https://sandbox.zenodo.org/api" if os.environ.get("SANDBOX") == "true" else "https://zenodo.org/api"
TOKEN = os.environ.get("ZENODO_TOKEN")
if not TOKEN:
    sys.exit("Set ZENODO_TOKEN first (zenodo.org -> Settings -> Applications -> Personal access tokens, scope deposit:write). Add SANDBOX=true for a dry run.")

PAPERS = [
    "enhancement-not-replacement", "it-scaled-the-fence", "samaritan-is-here",
    "sovereign-recursive-improvement", "who-tests-the-testers",
    "the-ai-cartel-and-the-sovereign-response", "the-cache-is-not-the-corpus",
    "the-class-of-the-prep-sheet", "the-missing-link", "the-tester-is-the-target",
    "three-days-of-silence", "who-decides-when-the-model-lies", "tourist-to-student",
    "sovereign-ai-vs-silicon-valley", "white-paper-methodology", "methodology",
    "comparative",
    "White_Paper_AI_Platform_Comparison", "chatgpt-case-study", "aws-case-study",
    "aisha-case-study", "manus-case-study", "google-case-study", "deepseek-case-study",
]
# owner ruling 2026-11-18: record-changelog and white-paper-tracker are index
# pages, not papers - no PDF, no DOI deposit for them.


def api(url, data=None, files=None, method=None):
    req = urllib.request.Request(url)
    req.add_header("Authorization", "Bearer " + TOKEN)
    if files:
        # bucket upload: raw bytes
        body, ctype = files, "application/pdf"
        req.add_method(method or "PUT")
        req.add_header("Content-Type", ctype)
        req.data = body
    elif data is not None:
        req.add_method(method or "POST")
        req.add_header("Content-Type", "application/json")
        req.data = json.dumps(data).encode()
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())


def paper_meta(slug):
    p = os.path.join("white-papers", slug, "index.html")
    with open(p, encoding="utf-8", errors="ignore") as f:
        t = f.read()
    m = re.search(r"<title>(.*?)</title>", t, re.S)
    d = re.search(r'<meta name="description" content="(.*?)"', t, re.S)
    title = html.unescape(m.group(1)).strip() if m else slug
    desc = html.unescape(d.group(1)).strip()[:900] if d else title
    return title, desc


results = []
if os.path.exists("zenodo-dois.tsv"):
    os.rename("zenodo-dois.tsv", "zenodo-dois.tsv.bak")
    print("previous zenodo-dois.tsv moved to .bak")

missing = [s for s in PAPERS if not os.path.isfile(os.path.join("white-papers", s, s + ".pdf"))]
if missing:
    print("SKIPPED (no PDF in white-papers/<slug>/<slug>.pdf yet - these get no deposit):")
    print("  " + "\n  ".join(missing))
    print("If ALL papers are listed, the PDFs are not committed yet (audit No. 5, item O1).")
to_upload = [s for s in PAPERS if s not in missing]
if not to_upload:
    sys.exit("Nothing to upload - commit the paper PDFs first (audit No. 5, item O1).")

for slug in to_upload:
    pdf_path = os.path.join("white-papers", slug, slug + ".pdf")
    title, desc = paper_meta(slug)
    meta = {
        "title": f"{title} — Evelyn Caro",
        "upload_type": "publication",
        "publication_type": "report",
        "description": f"{desc}<p>Part of <i>A Mirror of My Becoming™</i>, the verification portfolio of Evelyn Caro (qaevelyn.github.io). Dual-licensed: AGPL-3.0 + commercial.</p>",
        "creators": [{"name": "Caro, Evelyn"}],
        "access_right": "open",
        "license": "AGPL-3.0",
        "notes": "A Mirror of My Becoming™ — the verification portfolio of Evelyn Caro. Dual-licensed: AGPL-3.0 + commercial.",
    }
    dep = api(f"{API}/deposit/depositions", data={"metadata": meta})
    bucket = dep["links"]["bucket"]
    with open(pdf_path, "rb") as f:
        api(bucket + "/" + os.path.basename(pdf_path), files=f.read())
    pub = api(dep["links"]["publish"], data={}, method="POST")
    doi = pub.get("doi") or pub.get("metadata", {}).get("prereserve_doi", {}).get("doi", "")
    rec = pub.get("links", {}).get("record_html", "")
    print(f"OK  {slug}\n    {doi}\n    {rec}")
    results.append(f"{slug}\t{doi}\t{rec}")

with open("zenodo-dois.tsv", "w") as f:
    f.write("\n".join(results) + "\n")
print("\nDONE - zenodo-dois.tsv written. Next: python3 stamp_dois_and_pdfs.py zenodo-dois.tsv")
