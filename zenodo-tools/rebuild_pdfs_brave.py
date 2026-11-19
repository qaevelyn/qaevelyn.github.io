#!/usr/bin/env python3
"""Rebuild the white-paper PDFs in place from the DOI-stamped HTML using Brave headless.

Path-agnostic: repo root resolved from this file's own location (zenodo-tools/..).
Per ledger slug: find white-papers/<slug>/index.html (case-insensitive, hyphen/underscore
tolerant), render with Brave, overwrite the existing PDF (folder-level preferred, then
white-papers/<slug>*.pdf). If no PDF exists, write white-papers/<slug>/<slug>.pdf.
Uses a throwaway Brave profile so an open Brave window cannot interfere.
"""
import os, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSV, WP = ROOT / "zenodo-dois.tsv", ROOT / "white-papers"

candidates = [shutil.which("brave-browser"), shutil.which("brave"),
              "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
              os.path.expanduser("~/Applications/Brave Browser.app/Contents/MacOS/Brave Browser")]
brave = next((c for c in candidates if c and Path(c).exists()), None)
if not brave:
    sys.exit("No Brave found - install it from brave.com or reply with the exact app path.")

slugs = sorted({ln.split("\t")[0].strip() for ln in TSV.read_text().splitlines()
                if ln.strip() and not ln.startswith("#")})
print("ledger slugs: %d   brave: %s" % (len(slugs), brave))
if len(sys.argv) > 1:
    want = {x.lower() for x in sys.argv[1:]}
    slugs = [x for x in slugs if x.lower() in want]
    print("slug filter:", ", ".join(sys.argv[1:]))

def find_dir(slug):
    for cand in dict.fromkeys([slug, slug.replace("_", "-"), slug.replace("-", "_")]):
        for d in WP.iterdir():
            if d.is_dir() and d.name.lower() == cand.lower():
                return d
    return None

def pick_target(d, slug):
    pdfs = lambda base: sorted(p for p in base.iterdir()
                               if p.is_file() and p.suffix.lower() == ".pdf")
    exact  = [p for p in pdfs(d) if p.stem.lower() == slug.lower()]
    folder = pdfs(d)
    root   = [p for p in pdfs(WP) if p.stem.lower().startswith(slug.lower())]
    if exact:  return exact[0], "overwrite"
    if folder: return folder[0], "overwrite-first-of-%d" % len(folder)
    if root:   return root[0], "overwrite-first-of-%d" % len(root)
    return d / (slug + ".pdf"), "create"

profile = tempfile.mkdtemp(prefix="brave-pdf-")
done, failed = [], []
try:
    for slug in slugs:
        d = find_dir(slug)
        html = (d / "index.html") if d else None
        if not html or not html.exists():
            failed.append("%s: no white-papers/<slug>/index.html found" % slug)
            continue
        out, mode = pick_target(d, slug)
        cmd = [brave, "--headless", "--disable-gpu", "--no-first-run",
               "--user-data-dir=" + profile, "--no-pdf-header-footer", "--virtual-time-budget=20000",
               "--print-to-pdf=" + str(out.resolve()), "file://" + str(html.resolve())]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        except subprocess.TimeoutExpired:
            failed.append("%s: Brave timed out" % slug)
            continue
        if r.returncode == 0 and out.exists() and out.stat().st_size > 2000:
            done.append("%s -> %s  [%s, %d KB]" % (slug, out.relative_to(ROOT), mode,
                                                   out.stat().st_size // 1024))
        else:
            tail = ((r.stderr or "") + (r.stdout or "")).strip()[-200:]
            failed.append("%s: rc=%d %s" % (slug, r.returncode, tail))
finally:
    shutil.rmtree(profile, ignore_errors=True)

print("\nrebuilt %d / %d" % (len(done), len(slugs)))
for ln in done:   print("OK  ", ln)
for ln in failed: print("FAIL", ln)
sys.exit(1 if failed else 0)
