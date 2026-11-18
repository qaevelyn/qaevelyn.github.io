#!/usr/bin/env python3
"""Stamp the minted DOIs into the papers and rebuild their PDFs.

Owner flow (after batch_zenodo_papers.py writes zenodo-dois.tsv):
  1. run this script from the repo root: python3 stamp_dois_and_pdfs.py zenodo-dois.tsv
  2. it inserts a styled DOI band under each paper's byline (only if the paper
     does not already carry it), re-renders that paper's PDF from its own
     index.html, and replaces the PDF at white-papers/<slug>/<slug>.pdf - the
     file the Download button serves.
  3. commit + push; the Download buttons then serve the DOI-stamped PDFs and
     every paper page carries its DOI. Optionally, later, upload the stamped
     PDF to its Zenodo deposit as a new version - the DOI itself never changes.

Renderer: uses Google Chrome (or Edge/Chromium) headless in print-to-pdf mode,
so it works on the owner's Mac with nothing installed. If no browser is found,
the HTML is still stamped and the message says so plainly.
"""
import os
import re
import shutil
import subprocess
import sys

if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
    sys.exit("usage: python3 stamp_dois_and_pdfs.py zenodo-dois.tsv")

rows = {}
with open(sys.argv[1]) as f:
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) >= 2 and parts[1]:
            rows[parts[0]] = parts[1]

BROWSERS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/Microsoft Edge",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    shutil.which("google-chrome"), shutil.which("chromium"), shutil.which("chrome"),
]


def find_browser():
    for b in BROWSERS:
        if b and os.path.exists(b):
            return b
    return None


def render_pdf(browser, src_html, out_pdf):
    url = "file://" + os.path.abspath(src_html)
    cmd = [browser, "--headless=new", "--disable-gpu",
           "--no-pdf-header-footer",
           f"--print-to-pdf={os.path.abspath(out_pdf)}", url]
    env = dict(os.environ, HOME=os.environ.get("HOME", "/tmp"))
    subprocess.run(cmd, check=True, env=env,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


browser = find_browser()
if browser:
    print("renderer:", browser)
else:
    print("NOTE no Chrome/Edge/Chromium found - the HTML pages will be stamped "
          "but the PDFs cannot be rebuilt on this machine; the unstamped PDFs "
          "stay in place (you can rebuild them later; nothing else breaks).")

for slug, doi in rows.items():
    idx = os.path.join("white-papers", slug, "index.html")
    pdf = os.path.join("white-papers", slug, slug + ".pdf")
    if not os.path.isfile(idx):
        print(f"SKIP  {slug}: no index.html")
        continue
    with open(idx, encoding="utf-8") as f:
        t = f.read()
    if doi in t:
        print(f"SKIP  {slug}: DOI already stamped")
        continue
    band = (f'<p style="text-align:center; margin:1.2rem 0 0;"><a href="https://doi.org/{doi}" '
            f'style="display:inline-block; background:#8b6f3d; color:#f5e6d3; padding:.25rem .8rem; '
            f'border-radius:4px; font-size:.85rem; text-decoration:none; letter-spacing:.5px;">'
            f'DOI: {doi}</a></p>')
    if re.search(r'class="byline', t):
        m = re.search(r'(<p class="byline.*?</p>)', t, re.S)
        t = t[:m.end()] + "\n" + band + t[m.end():]
    else:
        t = re.sub(r"(<body[^>]*>)", r"\1\n" + band, t, count=1)
    with open(idx, "w", encoding="utf-8") as f:
        f.write(t)
    if browser and os.path.isfile(pdf):
        try:
            render_pdf(browser, idx, pdf)
            print(f"OK  {slug}: DOI {doi} stamped, PDF rebuilt ({os.path.getsize(pdf)} bytes)")
            continue
        except Exception as e:
            print(f"OK  {slug}: DOI {doi} stamped (PDF rebuild failed: {e})")
            continue
    print(f"OK  {slug}: DOI {doi} stamped")
print("\nDONE - commit and push from the repo root when you are happy with the result.")
