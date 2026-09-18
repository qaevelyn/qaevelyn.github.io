---
layout: single
title: "RAG Knowledge Base Audit — Per Scholas AI Assistant (Azari)"
permalink: /case-studies/azari-audit/
author_profile: true
---

**Date:** September 10, 2026  
**System:** Per Scholas AI Assistant (Azari) — Praxis LXP  
**Role:** Independent Auditor

## Context

While preparing for the AWS CCP exam, I used the Per Scholas AI assistant (Azari) to look up program documentation. I noticed the assistant uses a RAG architecture with hybrid retrieval (graph, lexical, dense semantic) and Reciprocal Rank Fusion. As someone who has built five RAG pipelines, three of them agentic, I recognized the architecture and began testing its knowledge base coverage.

## Finding

The knowledge base contains gaps and quality issues that reduce the assistant's usefulness for learners:

| Finding | Priority |
|---------|----------|
| No JRA documentation (Week 6 / Week 10 requirements, early graduate criteria) | High |
| No survey availability documentation | High |
| No PD syllabus in the knowledge base | High |
| Learner-submitted personal content indexed in the institutional KB | Low |
| Blank or unextractable documents returning no content | Medium |

## Evidence

- Backend tool output showing `call_rag` with "Found no results" for JRA queries
- Hybrid retrieval output showing a learner profile banner image injected into the prompt
- OCR output showing a blank PDF page ingested as a knowledge base document

## Recommendation

Add official program documentation (JRA rubrics, survey windows, PD and technical syllabi, graduation checklist). Audit and remove learner-submitted content and blank documents from the institutional knowledge base.

## Outcome

Reported to the Per Scholas platform team via Jovani Padron (jpadron@perscholas.org) with a structured gap report drafted with Azari's assistance. Awaiting response.

## Skills Demonstrated

- RAG architecture recognition (hybrid retrieval, RRF)
- Systems audit methodology
- Evidence documentation
- Professional reporting and disclosure
- Peer collaboration

## Attachments

- [Full Gap Report (PDF)](/assets/pdfs/KB_Coverage_Feedback_Report_Evelyn_Caro.pdf)


---

© 2026 Evelyn Caro. All rights reserved.  
A Mirror of My Becoming — https://evelynacaro.github.io  
For licensing inquiries: evelyn.caro.cloud@gmail.com
