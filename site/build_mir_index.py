#!/usr/bin/env python3
"""
Build the Mir search index from the portfolio's public content files.
Run this after adding or editing any public content file.
Output: site/mir-index.json
"""

import os
import re
import json
from pathlib import Path

REPO = Path(os.path.expanduser("~/Repos/qaevelyn.github.io"))
OUT = REPO / "site" / "mir-index.json"

# The corpus — every file Mir reads. Explicitly listed so nothing is missed.
CORPUS = [
    # White papers
    "white-papers/White_Paper_AI_Collaboration_Case_Study.md",
    "white-papers/White_Paper_AI_Platform_Comparison.md",
    "white-papers/aisha-case-study.md",
    "white-papers/aws-case-study.md",
    "white-papers/chatgpt-case-study.md",
    "white-papers/comparative.md",
    "white-papers/deepseek-case-study.md",
    "white-papers/google-case-study.md",
    "white-papers/manus-case-study.md",
    "white-papers/methodology.md",
    "white-papers/samaritan-is-here.md",
    "white-papers/sovereign-ai-vs-silicon-valley.md",
    "white-papers/sovereign-recursive-improvement.md",
    "white-papers/the-ai-cartel-and-the-sovereign-response.md",
    "white-papers/white-paper-methodology.md",
    "white-papers/who-tests-the-testers.md",
    # Case studies
    "case-studies/azari-audit.md",
    "case-studies/evidenceflow-verification-ship5.md",
    # Services and assessment
    "services.md",
    "assessments/ai-readiness-assessment.md",
    # Words
    "site/words.md",
]

def strip_frontmatter(text):
    """Remove Jekyll YAML frontmatter (--- ... ---) from the top of a file."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip()
    return text

def clean_text(text):
    """Strip HTML tags, markdown syntax, and collapse whitespace."""
    import re
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Remove markdown code fences
    text = re.sub(r'```[^`]*```', ' ', text, flags=re.DOTALL)
    # Remove markdown headers (## )
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Remove markdown link syntax [text](url) -> text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove markdown bold/italic markers
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    text = re.sub(r'_([^_]+)_', r'\1', text)
    # Remove markdown tables pipes
    text = re.sub(r'^\|.*\|$', lambda m: m.group(0).replace('|', ' '), text, flags=re.MULTILINE)
    # Remove horizontal rules
    text = re.sub(r'^[-=]{3,}$', '', text, flags=re.MULTILINE)
    # Preserve paragraph breaks; collapse other whitespace
    # First, normalize all newlines
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    # Collapse 3+ newlines to exactly 2 (paragraph break)
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Collapse runs of spaces/tabs within lines
    text = re.sub(r'[ \t]+', ' ', text)
    # Trim each line
    text = '\n'.join(line.strip() for line in text.split('\n'))
    # Trim
    return text.strip()


def chunk(text, max_chars=800):
    """Split text into chunks of roughly max_chars, preserving paragraphs."""
    paragraphs = re.split(r"\n\s*\n", text)
    chunks = []
    buf = ""
    for p in paragraphs:
        if len(buf) + len(p) + 2 <= max_chars:
            buf = (buf + "\n\n" + p).strip() if buf else p
        else:
            if buf:
                chunks.append(buf)
            buf = p
    if buf:
        chunks.append(buf)
    return chunks

def extract_title(text, filename):
    """Find the first # heading, or fall back to the filename."""
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return filename.replace(".md", "").replace("-", " ").replace("_", " ")

def extract_lookbook_content():
    """Pull ship narratives and other book content from lookbook.html."""
    import re
    path = REPO / "lookbook.html"
    if not path.exists():
        return []
    html = path.read_text(encoding="utf-8", errors="replace")
    chunks_out = []

    # Ship narratives
    for m in re.finditer(r'<div class="ship-narrative">(.*?)</div>', html, re.DOTALL):
        text = clean_text(m.group(1))
        if text:
            chunks_out.append(("lookbook.html#ships", "Ships — Narrative", text))

    # Ship descriptions — badge + description on the right page
    for m in re.finditer(r'<div class="badge[^"]*">([^<]+)</div>\s*<p[^>]*>(.*?)</p>', html, re.DOTALL):
        badge = m.group(1).strip()
        body = clean_text(m.group(2))
        if body and len(body) > 20:
            chunks_out.append(("lookbook.html#ships", "Ship — " + badge, body))

    # Service spreads — grab headings and body
    for m in re.finditer(r'<h3>(\d{2} — [^<]+)</h3>\s*<p[^>]*>(.*?)</p>', html, re.DOTALL):
        title = m.group(1).strip()
        body = clean_text(m.group(2))
        if body and len(body) > 20:
            chunks_out.append(("lookbook.html#services", title, body))

    # Intro story
    for m in re.finditer(r'<h2>Intro / Story</h2>(.*?)</div>\s*</div>', html, re.DOTALL):
        text = clean_text(m.group(1))
        if text:
            chunks_out.append(("lookbook.html#intro", "Intro / Story", text))

    return chunks_out


def main():
    index = {
        "meta": {
            "purpose": "Mir search index — every public content file, chunked for retrieval",
            "source_files": len(CORPUS),
            "generated_by": "site/build_mir_index.py",
        },
        "entries": [],
    }

    missing = []
    for rel in CORPUS:
        path = REPO / rel
        if not path.exists():
            missing.append(rel)
            continue

        raw = path.read_text(encoding="utf-8", errors="replace")
        text = strip_frontmatter(raw)
        title = extract_title(text, path.name)
        text = clean_text(text)

        for i, chunk_text in enumerate(chunk(text, max_chars=800)):
            index["entries"].append({
                "id": rel.replace("/", "__").replace(".md", "") + "__" + str(i),
                "source": rel,
                "title": title,
                "chunk_index": i,
                "text": chunk_text,
                "live_url": "https://qaevelyn.github.io/" + rel.replace(".md", "/"),
            })

    # Add lookbook content
    lookbook_chunks = extract_lookbook_content()
    for src_marker, title, text in lookbook_chunks:
        for i, chunk_text in enumerate(chunk(text, max_chars=800)):
            index["entries"].append({
                "id": "lookbook__" + str(len(index["entries"])),
                "source": src_marker,
                "title": title,
                "chunk_index": i,
                "text": chunk_text,
                "live_url": "https://qaevelyn.github.io/lookbook.html",
            })
    print("Lookbook chunks added: " + str(len(lookbook_chunks)))

    index["meta"]["chunks"] = len(index["entries"])

    with open(OUT, "w") as f:
        json.dump(index, f, indent=2)

    print("Wrote " + str(OUT))
    print("Source files indexed: " + str(len(CORPUS) - len(missing)))
    print("Total chunks: " + str(len(index["entries"])))
    if missing:
        print("")
        print("MISSING FILES (skipped):")
        for m in missing:
            print("  " + m)

if __name__ == "__main__":
    main()
