# PORTFOLIO MAP — every layer, what sits where, change-propagation guide
Created Oct 1, 2026. Consult this map BEFORE any structural change; update it AFTER any structural change.

## LAYER 1 — ENTRY POINTS
- index.html — homepage, 3D book cover, site-wide footer (line ~442)
- lookbook.html — THE BOOK: spreads with data-toc-parent/child; TOC auto-built by buildTOC() JS (~line 1295); ship-narrative class (day #2c1810 / night #f5f1e8); footer inside
- tools.md — Ship 6/7 tools page (/tools/)

## LAYER 2 — SHIPS & SERVICES (spreads inside lookbook.html + _pages mirrors)
- Ships 1–5 spreads: lookbook lines ~770–860; _pages/ship1–5.md mirrors
- Services spreads: lookbook ~906–1070 (six service types)
- Certifications spreads: lookbook ~1131–1230 (Google AI / AWS+CompTIA / IBM)
- Portfolio mirrors: _pages/portfolio.md, _portfolio/portfolio-1.md, portfolio-2.html
- services.md line 322 — Proof-of-Work blurb (names the suite)

## LAYER 3 — EVIDENCE CHAIN (site/)
- evidence.json — the ledger; artifact counts; add new artifacts HERE + manifest
- manifest.json, mir-index.json, words.json/words.md, exhibits/, build_mir_index.py — derived index (run build script after evidence changes)

## LAYER 4 — PUBLISHED WORKS
- white-papers/ — 20 papers + manifest.json + white-paper-tracker.md + update_manifest.py (run after adding papers; tracker is the queue)
- case-studies/ — azari-audit, evidenceflow-verification-ship5 + manifest.json
- CHANGE RULE: new paper = md here + manifest update via update_manifest.py + tracker line

## LAYER 5 — CONFIG & THEME
- _config.yml — identity, theme (academicpages), description
- _includes/_layouts/_sass — theme machinery (don't edit casually)
- LICENSE (site), CNAME, Dockerfile/docker-compose — infrastructure

## LAYER 6 — LOOSE EVIDENCE (root — candidates for site/evidence/ someday)
- exhibit 1–7 PNGs, FTC confirmation PDF, AWS cert PDFs, Coursera PDFs, screen recording .mov, ICP/LEAD-GEN md files

## EXTERNAL (not in this repo)
- Suite repo: a-mirror-of-my-becoming-suite-ingestion-tools (Ship 6+7, AGPL)
- Ships 1–5 repos: qaevelyn/ship1–5 (license conversion pending)
- Mirror-Project (private): PER_SCHOLAS trio, MIRROR trio, handovers, SESSION_DOING.yaml, evidence folders
- ~/Mirror-Food/: Store 1 (CANONICAL), stores pending retirement, ingest scripts, aws-dispute-evidence/

## CHANGE-PROPAGATION RULES
1. Ship name/content change → lookbook spread + _pages mirror + ships/manifest.json + PORTFOLIO_MAP + services.md blurb + tools.md
2. New artifact → evidence.json + manifest + this map
3. New paper → white-papers/ + update_manifest.py + tracker
4. Store path change → ingest scripts + quel1_search + student_anchors + plists + this map
5. Brand text → ™ after "Becoming"; "mirror" = project only
