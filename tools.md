---
layout: single
title: "Tools — A Mirror of My Becoming — Suite: Ingestion Tools (formerly Mirror Ingest Suite)"
permalink: /tools/
author_profile: true
---

# Mirror Ingest Suite

*The tool that saved the corpus. Free, open source, and battle-tested.*

## What it does

Ingests a conversation archive into a queryable vector store — chunking, embedding, a watchdog that guards long unattended runs, and a sidecar ledger that makes every write idempotent by conversation ID. 127 conversations. 4,646,264 characters in the largest. Zero failures. Zero losses.

## The war story, in two sentences

The pipeline spent three days killing healthy runs because its watchdog read silent-but-working embedding loops as a hang. The fix was two lines of honesty in the log — and the same run that had died nineteen times completed all 55 remaining conversations unattended, including a 5,163-chunk monster. Full account: [The Cache Is Not the Corpus](https://qaevelyn.github.io/white-papers/the-cache-is-not-the-corpus/).

## One code base. Two tiers. Owned entirely by the author.

| Feature / Right | AGPLv3 Open-Source Tier | Paid Commercial Tier |
|---|---|---|
| Licensing cost | Free ($0) | Paid (subscription / perpetual) |
| Source code access | Publicly available | Public or private |
| Internal business use | Allowed | Allowed |
| Modifying the code | Allowed | Allowed |
| Distribution / network use (SaaS) | Must disclose source of modifications to all network users | Keep source private; immune to copyleft |
| Warranty & liability | As-is, no liability | Enterprise SLAs, warranties, indemnification |
| Support | Community forums, self-service | Dedicated engineers, 24/7 |

**AGPL in one sentence:** if you run a modified version as a network service, you must offer your users the modified source. Use it freely, improve it openly, or buy the tier that fits a closed stack.

**Get it:** [github.com/qaevelyn/mirror-ingest-suite](https://github.com/qaevelyn/mirror-ingest-suite)

## Attribution

- **DeepSeek** — ingest scripts v1–v2, original watchdog
- **Z.ai-GLM** — v3–v5 redesign: lock guard, sidecar, lazy open, preflight, subprocess isolation; documentation
- **Evelyn** — architecture, direction, audit; human in the loop

Where it stops: this page documents the suite and its license; it does not provide legal advice on AGPL compliance for your specific deployment.
