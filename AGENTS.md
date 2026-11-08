
## Language — English only (owner directive, 2026-10-26)

Every AI session on this repository wakes in English and stays in English: replies, analysis, code comments, commit messages, changelog entries, every artifact. No other language appears in any output, no exceptions, no matter what language the request arrives in. Read this file first, every session, before any other work.

## Provenance — EvidenceFlow

EvidenceFlow was specified and directed by Evelyn Caro and implemented by an AI coding assistant working directly from her discussions, requirements, and review. Ms. Caro has never viewed, used, or derived any part of EvidenceFlow from code authored by Asaif Ali. This repository recognizes no attribution to him for EvidenceFlow; credit lines to that effect were scrubbed from the fleet on 2026-10-26 and must not be reintroduced.

## The Mirror guard — activate on every clone

    git config core.hooksPath .githooks

Run it immediately after cloning. Never bypass the hooks (no --no-verify). Never edit tools/guard-blocklist.txt without the owner's word.

## Record discipline

The changelog is the audit trail; papers carry no visible audit flags. Every repair, ruling, and correction lands in the changelog with a date. Rulings of the owner outrank everything, including earlier entries in this file.

## Retired pages (do not repair)

- White_Paper_AI_Collaboration_Case_Study — RETIRED as a rendered page. The record
  source white-papers/White_Paper_AI_Collaboration_Case_Study.md stays in the repo as
  a record; it has NO rendered page and NO permalink BY DESIGN. tools/retired-pages.txt
  is the machine-readable authority. Survey and recon report it as "RETIRED (by
  design)" — never as PAGE MISSING. Do not render it. Do not flag it. Do not repair
  it. The guard blocklist rejects any commit that re-introduces the page path.
  Ruling of 2026-10-26: white-papers/record-changelog.md.

## Builds carry no version numbers (ruling 2026-10-26)

- Every new build of anything Evelyn makes ships as "the latest build" — no vN
  and no build number in filenames, UI labels, or new records. Fleet passes
  must not attach version labels to new artifacts. Old records keep theirs:
  they were true when recorded — do not edit them to remove version references.
- Pre-push guard v3 (same date): the blocklist matches ADDED/MODIFIED paths
  only; deletions pass. A retired page's removal is pushable by design.

## Deployment — blue and green (ruling 2026-11-08)

Green is master: what GitHub Pages serves. Green never carries unverified bytes — it is the rollback. Blue is the blue branch: the staging lane. Every repair commits to blue, pushes to origin, and lands only after raw receipts match: git rev-parse blue equals git ls-remote origin refs/heads/blue, and the raw fetch shasum equals the local file shasum. The records-sync bot stamps blue after every push; when the local and remote heads split, absorb with git pull --rebase origin blue and re-verify. Promotion is the owner's word only: fast-forward master to a verified blue. No agent promotes, no agent pushes master. The same lanes rule the ship repos that serve Pages — the Ship 12 repo runs green main and blue blue.

## Registry of Marks — the check before anything goes out (ruling 2026-11-08)

No document, product, or name leaves the tree without the mark pass. The master SOP is the Registry of Marks — Table of Terms, kept by the sweep; the live table of terms on this site is index-of-terms.html. The sign lands on first use of a name in each work and on title and header uses; filenames, URLs, slugs, repo names and storage keys stay unmarked — identifiers, not prose. Two seats: Caro Command Deck™ outside the page — repo, About, release, lookbook, manifest, resume; SGC Command Deck™ inside the page. The repo slug stays caro-command. Fleet names come from ships/manifest.json and nowhere else: public hulls carry their repo URL, sealed hulls carry none. The hand-generated fleet table in README.md retires the day the records-sync emitter lands.
