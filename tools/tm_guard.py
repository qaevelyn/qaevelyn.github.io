#!/usr/bin/env python3
"""tm_guard — TM Guard for the provenance repo.

Path agnostic: finds the git root and runs from there.
Checks for bare marks and duplicate blocks.
No version string by owner ruling: the file name is the name.
"""
import os, re, subprocess, sys

MARKS = [
    "A Mirror of My Becoming",
    "A Mirror of My Becoming Tools",
    "A Mirror of My Becoming Suite: Ingestion Tools",
    "TriviaGate",
    "Caro Command Deck",
    "SGC COMMAND DECK",
    "Radiology Companion",
    "Evelyn Books Travel",
    "Neuroplasticize",
    "encode by day, consolidate by night",
    "Sleep Is Studying Too",
]
TM = "\u2122"
TEXT_EXTS = (".html", ".md", ".txt", ".json", ".js")

def get_git_root():
    """Find the absolute path to the git root."""
    try:
        root = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
        if root:
            os.chdir(root)
            return root
    except Exception:
        pass
    return os.getcwd()

def find_registry():
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]
        for f in files:
            if f.startswith("A_Mirror_of_My_Becoming_Registry-of-Marks_Table-of-Terms."):
                return os.path.join(root, f)
    return None

def load_allowlist():
    pats = []
    if os.path.isfile(".tm-allowlist"):
        for line in open(".tm-allowlist", encoding="utf-8"):
            line = line.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            pats.append(line)
    return pats

def is_identifier(line):
    if re.search(r"`[^`]*`", line): return True
    if re.search(r"https?://", line) or re.search(r"/[\w./-]+", line): return True
    if re.search(r"\.(?:py|js|json|md|html|sh|svg|pdf|zip)\b", line): return True
    if re.search(r"sgc-deck-v\d|TriviaGate_transcript", line): return True
    return False

def staged_text_files():
    out = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z"],
        capture_output=True, text=True
    ).stdout
    files = [f for f in out.split("\0") if f]
    return [f for f in files if f.endswith(TEXT_EXTS)]

def check_duplicates(text):
    blocks = re.split(r'\n\s*---\s*\n', text)
    for i in range(1, len(blocks)):
        if blocks[i].strip() == blocks[i-1].strip() and len(blocks[i].strip()) > 5:
            return "Duplicate block detected (identical to previous block)"
    return None

def scan(files, allow):
    hits = []
    for path in files:
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        
        dup_err = check_duplicates(text)
        if dup_err:
            hits.append((path, 0, "DUPLICATE_BLOCK", dup_err))
            continue
            
        for i, line in enumerate(text.splitlines(), 1):
            if not any(m in line for m in MARKS):
                continue
            for m in MARKS:
                idx = line.find(m)
                while idx != -1:
                    tail = line[idx + len(m): idx + len(m) + 2]
                    if TM in tail:
                        idx = line.find(m, idx + len(m))
                        continue
                    if is_identifier(line):
                        idx = line.find(m, idx + len(m))
                        continue
                    if any(re.search(p, line) for p in allow):
                        idx = line.find(m, idx + len(m))
                        continue
                    hits.append((path, i, m, line.strip()[:100]))
                    idx = line.find(m, idx + len(m))
    return hits

def main():
    get_git_root()
    reg = find_registry()
    if not reg:
        print("TM GUARD — commit BLOCKED. Registry of Marks not found (stem search, repo root).")
        print("canon stem: A_Mirror_of_My_Becoming_Registry-of-Marks_Table-of-Terms")
        return 1
    
    files = staged_text_files()
    hits = scan(files, load_allowlist())
    if hits:
        print("TM GUARD — commit BLOCKED. Bare marks in staged text (full list, no cap):")
        for path, ln, mark, ctx in hits:
            print(f"{path}:{ln} :: [{mark}] :: {ctx}")
        print(f"registry: {reg}")
        print("to exempt a verbatim identifier, add its line pattern to .tm-allowlist with a reason; otherwise add \u2122 per registry \u00a71.1.")
        print("override only with: git commit --no-verify")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
