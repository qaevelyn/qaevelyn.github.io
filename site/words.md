# Portfolio Words — Human-Editable Source

This file is the human-readable companion to `site/words.json`. Edit the words here, then sync to the JSON. Do not edit both at once.

---

## Homepage (`index.html`)

### 3D Book Cover
- **Cover title:** A Mirror of My Becoming
- **Prompt:** Click to open

### Below the Book
- **Line 1:** Open the book to see the work
- **Name:** Evelyn Caro
- **Tagline:** Sovereign systems, local first. No cloud dependency.¹
- **Footnote:** ¹ Five RAG pipelines built locally. Three cloud attempts — AWS, IBM WatsonX, Google AI Studio. One lost project, rebuilt. The white papers document all.

---

## Lookbook (`lookbook.html`)

### TOC Left Page
- **Title:** LOOKBOOK
- **Subtitle:** Sovereign AI Portfolio — Evelyn Caro

### TOC Right Page — Intro / Story
- **Header:** Intro / Story
- **Subtitle:** Sovereign AI Builder · RAG Pipelines, Agentic AI & EvidenceFlow · AWS re/Start Graduate
- **Body:** I engineer sovereign AI systems that run locally, on my terms. Built 5 RAG pipelines. Tested them adversarially. Now in conversation with a national historical organization partnered with a major university — proof of concept pending.
- **Context:** This portfolio is a lookbook of my work — Ships first, then the credentials that built the foundation.
- **Blockquote:** Sovereign systems, local first. No cloud dependency.
- **Proof line:** Proof, not tenure: I hold certifications in AI, LangChain, and Agentic RAG from Google and IBM. I am an AWS re/Start graduate as of September 9, 2026.
- **Closer:** Count my proofs.

### Ship 1
- **Title:** Ship 1 — AWS SageMaker RAG
- **Description:** Retrieval-Augmented Generation on AWS SageMaker using vector databases and large language models. Built and deployed locally on an M1 MacBook Air.

### Ship 2
- **Title:** Ship 2 — AWS SageMaker Agentic RAG
- **Description:** Agentic RAG pipeline on AWS SageMaker — retrieval + action (API calls, decision-making). Demonstrates autonomous reasoning and tool use.

### Ship 3
- **Title:** Ship 3 — IBM Granite RAG
- **Description:** RAG pipeline on IBM Granite, demonstrating cross-platform AI/cloud capabilities. Built to show interoperability and model flexibility.

### Ship 4
- **Title:** Ship 4 — IBM Granite Agentic RAG
- **Description:** Agentic RAG pipeline on IBM Granite — retrieval + action. Cross-platform agentic architecture with autonomous reasoning and decision-making.

### Ship 5
- **Title:** Ship 5 — IBM Granite Agentic RAG with EvidenceFlow
- **Description:** A local, sovereign, evidence-verified RAG pipeline built on IBM Granite, running via Ollama on an M1 MacBook Air. Every claim is traceable to a source. Fail-closed behavior: if evidence is missing, it abstains.
- **Attribution:** Foundation: IBM SkillsBuild (Anna Gutowska). Inspiration: Asaif Ali's EvidenceFlow. Execution: Evelyn Caro.

---

## Update Workflow

1. Edit the words **here** (human-readable)
2. Copy the change into `site/words.json` (machine-readable)
3. `git add site/words.md site/words.json && git commit && git push`

---

**Companion file:** `site/words.json`
**Last updated:** September 12, 2026
