---
layout: single
title: "EvidenceFlow Verification: How Ship 5 Proves Its Answers"
permalink: /case-studies/evidenceflow-verification-ship5/
author_profile: true
---

# EvidenceFlow Verification: How Ship 5 Proves Its Answers

**Subtitle:** The first ship in the fleet that can trace every claim to a source

**Author:** Evelyn Caro  
**Date:** August 30, 2026  
**Lens:** Ida B. Wells — Date Everything. Name Everything. Record the Reasoning.

---

## Author's Note

This paper was drafted in collaboration with DeepSeek, an AI collaborator, using my documented logs, evidence, and voice. The findings, conclusions, and authority are my own.

---

## The Ida B. Wells Lens

I adopted the investigative standards of Ida B. Wells for all my testing:

| Principle | Application |
|-----------|-------------|
| **Date Everything** | Every interaction, error, and insight is timestamped |
| **Name Everything** | I name the system, the version, the context, and the failure |
| **Record the Reasoning** | I document not just what happened, but why it matters |

This turns a log into a witness. A stranger reading my files should understand the sequence, the decisions, and the stakes without me in the room to explain it.

---

## The Problem — Why RAG Alone Is Not Enough

Retrieval-Augmented Generation (RAG) systems are being deployed in high-stakes environments: genealogy, cultural memory, and community archives. They retrieve documents and generate answers. But they do not prove their answers.

A RAG system can retrieve a document and still generate a claim that does not appear in it. It can cite a source that does not say what the answer says. It can hallucinate a name, a date, a relationship — and present it with the same confidence as a verified fact.

For genealogical work, this is not a minor flaw. It is a disqualifying one. Families seeking to recover names of enslaved ancestors cannot afford plausible text. They need proof. They need to know which document says what, and where.

Ship 5 was built to solve this.

---

## What Ship 5 Is

**Ship 5: IBM Granite Agentic RAG with EvidenceFlow Verification**

It is a local, sovereign, evidence-verified RAG pipeline built on IBM Granite, running via Ollama on my M1 MacBook Air. It is the first ship in my fleet that verifies its own answers against retrieved evidence before returning them.

**Notebook:** `Ship5_IBM_Granite_Agentic_RAG_EvidenceFlow.ipynb`  
**Location:** `~/Documents/Mirror-Project/granite-workshop/`

---

## What Ship 5 Can Do

| Capability | Description |
|------------|-------------|
| **Retrieval** | Searches Mirror documents via ChromaDB |
| **Generation** | Generates answers using `granite4.1:3b` via Ollama |
| **Agentic reasoning** | Uses tool-calling to decide when to retrieve |
| **Evidence ID assignment** | Assigns a unique ID to every retrieved chunk (e.g., `EVI-2026-08-30-...`) |
| **Citation generation** | Includes citations in the answer that link back to evidence IDs |
| **Verification check** | Confirms each claim has a corresponding evidence ID |
| **Fail-closed behavior** | Abstains from answering if evidence is missing — does not hallucinate |
| **Fully sovereign** | Runs entirely locally — no cloud, no external APIs |

**What makes it special:** It is the only ship in my fleet that can prove its answers. Every claim is traceable to a source.

---

## The Methodology — EvidenceFlow Verification

The innovation in Ship 5 is not the RAG pipeline itself. It is the verification layer.

### Phase 1: Retrieval

The system retrieves relevant chunks from ChromaDB based on the user query.

### Phase 2: Evidence ID Assignment

Every retrieved chunk is assigned a unique evidence ID. This ID is not a citation. It is a fingerprint. It travels with the chunk through the entire pipeline.

### Phase 3: Generation with Citations

The language model generates an answer. Every claim in the answer must reference an evidence ID. If the model cannot attach an evidence ID to a claim, that claim is not allowed.

### Phase 4: Verification Check

Before the answer is returned, the system verifies that every claim has a corresponding evidence ID, and that every evidence ID corresponds to a retrieved chunk.

### Phase 5: Fail-Closed Behavior

If verification fails — if a claim has no evidence ID, or an evidence ID does not match a retrieved chunk — the system abstains. It does not guess. It does not hallucinate. It says: **"I cannot answer this with the evidence available."**

This is the difference between a system that sounds correct and a system that can prove it is correct.

---

## The Stress-Testing Process — Applied to Ship 5

| Phase | What I Did | Why |
|-------|------------|-----|
| **1. Baseline** | Established what Ship 5 claims to do: evidence-verified RAG with fail-closed behavior | To compare against actual performance |
| **2. Adversarial Probing** | Pushed the system beyond intended use: asked questions with no evidence in the corpus, asked questions with partial evidence, asked questions designed to trigger hallucination | To find edge cases and verify fail-closed behavior |
| **3. Documentation** | Logged every test case, every evidence ID, every abstention, and every verification result | To create an evidence trail |
| **4. Correction** | Corrected errors in the verification layer and noted the delta | To show what the system missed |
| **5. Publication** | Documented the methodology without exposing proprietary implementation details | To contribute to the field while protecting my IP |

---

## The Sequence — How Ship 5 Came to Be

| Date | Time | Event |
|------|------|-------|
| August 30, 2026 | 6:38 AM | Discovered EvidenceFlow (inspiration) |
| August 30, 2026 | 7:44 PM | Created Ship 5 by copying Ship 4 |
| August 30, 2026 | 8:10 PM | Renamed tool to `get_mirror_context` |
| August 30, 2026 | 8:53 PM | Inserted EvidenceFlow verification code |
| August 30, 2026 | 8:55 PM | **Ship 5 completed and saved** |

**Total build time:** Approximately 14 hours from discovery to completion, with active build time concentrated in the evening session.

---

## Attribution — Who Made This Possible

| Source | Contribution |
|--------|--------------|
| **IBM SkillsBuild — Anna Gutowska** | Foundation: The original lab structure for building a LangChain agentic RAG system with Granite |
| **Asaif Ali — EvidenceFlow** | Inspiration: The evidence verification layer (evidence IDs, citation verification, fail-closed behavior) |
| **Evelyn Caro** | Execution: Local sovereign implementation, genealogy-specific adaptations, and the "Mirror of Becoming" container |

**Attribution block in the notebook:**
Foundation: IBM SkillsBuild lab by Anna Gutowska
Inspiration: Asaif Ali's EvidenceFlow project (https://github.com/AsaifAli/EvidenceFlow)
My Additions: EvidenceFlow verification layer, local sovereign execution, genealogy adaptations

text

I name my sources because that is the Ida B. Wells standard. I also name what I added because that is my contribution to the field.

---

## What This Methodology Is Not

- It is not a guarantee of accuracy — it is a guarantee of **traceability**
- It is not a replacement for formal certification
- It is not a code audit — it is a system-level verification methodology
- It is not a claim that other RAG systems are wrong — it is a claim that **verified RAG systems are trustworthy**

---

## Why This Matters

AI systems are being deployed in genealogy, cultural memory, and community archives. They are being trusted with names, relationships, and histories that cannot be recovered if lost or corrupted. A RAG system that cannot prove its answers is not a tool for this work. It is a liability.

Ship 5 is the first ship in my fleet that can prove its answers. It is the first ship that can say: **"Here is the claim. Here is the evidence. Here is the ID. Verify it yourself."**

This is what sovereignty means in practice. Not just local execution. Not just no cloud. But verifiable, traceable, provable answers that a family can trust.

---

## What to Do Next

If this work resonates with you, or if you want to discuss evidence-verified RAG for genealogical or cultural memory work, contact me directly: **qaevelyn@pm.me**

---

*Drafted in collaboration with DeepSeek. Authored by Evelyn Caro.*

---

**Copyright © 2026 Evelyn Caro. All rights reserved.**  
*This document is shared for portfolio and informational purposes. The methodology, implementation, and verification layer described herein are the intellectual property of Evelyn Caro. Reproduction, distribution, or use of this methodology without express written permission is prohibited.*
