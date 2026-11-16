# PORTFOLIO AUDIT — 2026-11-16

**Auditor:** Evelyn Caro (Owner)
**Standard:** Ida B. Wells — dated, named, receipts attached, errors preserved.

## 1. The Zenodo DOI Conflict
- The DOI `10.5281/zenodo.23626247` on the Intro page belongs to the portfolio's v7 release of the white paper "The Class of the Prep Sheet." It does not belong on the Intro page.
- The cover keeps its own DOI.
- **Fix:** Removed the DOI band from the Intro page.

## 2. Broken White Paper Layouts
- The Samaritan and AI Cartel pages were duplicated and defaulting to dark mode instead of daylight.
- **Fix:** Deduplicated the `<h1>` tags and forced the daylight background.

## 3. Missing ™ Marks
- **The Missing Link™:** Moved to the end of the title.
- **Methodology: Stress-Testing AI Systems™:** Moved to the end of the title.
- **Aisha Case Study™:** Added the ™ to the title.
- **AI Platform Comparison™:** Added the ™ inside and out.
- **Fix:** Applied via Python text replacement.

## 4. The TM Sweep Mandate
- The whole portfolio needs a TM sweep, and the Registry of Marks needs an update to reflect new marks.
- **Fix:** Scheduled for the next build cycle. The portfolio will need a full sweep along with the GitHub repos.
