
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
