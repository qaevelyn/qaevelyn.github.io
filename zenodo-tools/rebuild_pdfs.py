import os, shutil, subprocess
BROWSERS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/Microsoft Edge",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    shutil.which("google-chrome"), shutil.which("chromium"),
    shutil.which("chrome"),
]
b = next((x for x in BROWSERS if x and os.path.exists(x)), None)
if not b:
    raise SystemExit("No Chrome/Edge/Chromium found - install one, re-run.")
print("renderer:", b)
done = 0
for d in sorted(os.listdir("white-papers")):
    idx = os.path.join("white-papers", d, "index.html")
    pdf = os.path.join("white-papers", d, d + ".pdf")
    if not (os.path.isfile(idx) and os.path.isfile(pdf)):
        continue
    t = open(idx, encoding="utf-8", errors="ignore").read()
    if "doi.org/10." not in t:
        continue
    url = "file://" + os.path.abspath(idx)
    cmd = [b, "--headless=new", "--disable-gpu",
           "--no-pdf-header-footer",
           "--print-to-pdf=" + os.path.abspath(pdf), url]
    r = subprocess.run(cmd, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
    tag = "OK " if r.returncode == 0 else "FAIL"
    print(tag, d, os.path.getsize(pdf), "bytes")
    done += r.returncode == 0
print("rebuilt", done, "stamped PDFs in place")
