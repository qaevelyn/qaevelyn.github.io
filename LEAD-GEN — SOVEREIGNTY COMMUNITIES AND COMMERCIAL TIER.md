# ============================================================
# LEAD-GEN — SOVEREIGNTY COMMUNITIES AND COMMERCIAL TIER
# Status: DRAFT v1.0
# Created: 2026-09-25
# Author: Evelyn Caro
# Basis: ICP v2.0 — Built from Portfolio as Evidence of Capability
# Note: Operational document. Derives from ICP. Revise as ICP revises.
# ============================================================

leadgen_v1:

  principle: >
    Lead-gen is the operational bridge between the ICP and the first
    engagement. The ICP defines who qualifies. This document defines
    how to find them, reach them, and convert them.

  input: "ICP — BUILT FROM PORTFOLIO AS EVIDENCE OF CAPABILITY.md (v2.0)"
  status: "DRAFT v1.0"

  # ----------------------------------------------------------
  # SEGMENT 1 — GENEALOGY AND LINEAGE NONPROFITS
  # Priority: HIGHEST — already validated by meeting
  # ----------------------------------------------------------

  segment_1_genealogy:
    priority: "HIGHEST"
    rationale: "Cynthia Evans meeting held Aug 28 2026. Offer documented. No response yet."

    target_organizations:
      - name: "10 Million Names"
        status: "MEETING HELD — awaiting response"
        contact: "Cynthia Evans, Research Director"
        source: "~/Repos/Mirror-Project/meeting with cynthia/"
        next_action: "Follow up — meeting was Aug 28, email Aug 29, no response as of 09/25"
        offer: "Free RAG pipeline build for existing data. Path B volunteer documented."
        partners: "Harvard, American Ancestors, ABC News, Georgetown"

      - name: "American Ancestors"
        status: "Named as 10 Million Names partner — separate licensing conversation"
        source: "10M_Names_Response_Final_2026-08-24.md"
        next_action: "Hold until 10 Million Names responds — do not approach independently"

      - name: "Freedmen's Bureau Records Project"
        status: "NAMED in provenance — outreach queued"
        source: "MIRROR_PROVENANCE_v3.5_2026-07-04.md lines 63, 74, 83"
        next_action: "Begin outreach — named as next step in provenance"

      - name: "Community archives serving FBA and Freedmen"
        status: "Segment defined, specific orgs not yet named"
        next_action: "Identify by searching genealogy nonprofit directories"

    lead_sources:
      - "Genealogy nonprofit directories"
      - "National Genealogical Society member list"
      - "African American genealogy societies"
      - "Harvard / Georgetown / ABC News partner pages (per 10M Names partners)"
      - "Cynthia Evans referral network"

    contact_path:
      - "Research Director or Executive Director"
      - "Digital infrastructure lead if exists"
      - "Cynthia Evans as warm referral for others in her network"

    outreach_sequence:
      step_1: "Follow up with Cynthia Evans — check in, no pressure, restate offer"
      step_2: "If no response in 2 weeks, send a short nudge with a specific ask"
      step_3: "If still no response, approach Freedmen's Bureau Records Project independently"
      step_4: "Use any 10M Names progress as a credential for the next approach"

    qualification_questions:
      - "Do you have a database of fragmented records that need connecting?"
      - "Is data sovereignty a concern for your community?"
      - "Would you accept a free pipeline build with no obligation?"
      - "Would you grant a testimonial and reference if the build succeeds?"

    success_criteria:
      - "One deployment — RAG pipeline built for a genealogy nonprofit"
      - "Signed testimonial"
      - "Named reference"
      - "Case study written with permission"

  # ----------------------------------------------------------
  # SEGMENT 2 — LAW FIRMS
  # Priority: HIGH — Kott proposal, ABA + EY links
  # ----------------------------------------------------------

  segment_2_law_firms:
    priority: "HIGH"
    rationale: "Dr. Kott proposal 09/25/2026. ABA + EY links provided. Not yet owner-validated."

    target_profile:
      size: "20-150 attorneys"
      practice: "Litigation, regulatory, compliance, or IP"
      geography: "DMV first — DC, Northern Virginia, Maryland"
      trigger: "AI governance question from client, regulator, or insurer"

    lead_sources:
      - "DC Bar directory"
      - "Virginia State Bar directory"
      - "Maryland State Bar directory"
      - "Legal press — Law.com, National Law Journal, ABA Journal"
      - "LinkedIn — managing partners, GCs, practice chairs"
      - "Dr. Kott / SCORE DC network"

    contact_path:
      - "Managing partner"
      - "General counsel or outside counsel coordinator"
      - "Practice chair for litigation / regulatory / IP"
      - "IT or operations director if AI governance is their remit"

    outreach_sequence:
      step_1: "Identify 20 firms matching the profile in DMV"
      step_2: "Send short intro email referencing ABA + EY AI governance concerns"
      step_3: "Offer 30-minute readiness conversation — no pitch, no deck"
      step_4: "Bring the portfolio — the work is the proof"
      step_5: "Convert to a fixed-scope, fixed-fee readiness assessment"

    qualification_questions:
      - "Are attorneys at your firm using AI tools?"
      - "Is there a firm-level AI use policy?"
      - "Has a client or insurer asked about AI governance?"
      - "Would you grant a testimonial and reference if the work succeeds?"

    success_criteria:
      - "One pilot — AI governance readiness assessment"
      - "Signed testimonial"
      - "Named reference"
      - "Case study written with permission"

  # ----------------------------------------------------------
  # SEGMENT 3 — COMMUNITY ORGANIZATIONS SERVING FBA AND FREEDMEN
  # Priority: MEDIUM — mission-aligned, funding uncertain
  # ----------------------------------------------------------

  segment_3_community:
    priority: "MEDIUM"
    rationale: "Mission core. May not have budget. Offer volunteer or grant-funded builds."

    target_organizations:
      - "FBA community organizations"
      - "Freedmen descendant organizations"
      - "Indigenous data sovereignty organizations"
      - "Community archives and historical societies"

    lead_sources:
      - "Community organization directories"
      - "MIRROR_PROVENANCE named partners"
      - "Referrals from genealogy segment"

    contact_path:
      - "Executive Director"
      - "Program Director"
      - "Community archivist or historian"

    outreach_sequence:
      step_1: "Identify 10 organizations aligned with the mission"
      step_2: "Intro email — mission alignment, no pitch, offer to build free"
      step_3: "Offer to build a RAG pipeline for their existing records"
      step_4: "Position as free for the community, licensed for commercial use"

    qualification_questions:
      - "Do you hold records that need connecting?"
      - "Is data sovereignty central to your work?"
      - "Would you accept a free build with no obligation?"
      - "Would you grant a testimonial and reference if the build succeeds?"

    success_criteria:
      - "One free community deployment"
      - "Testimonial from the community, not the organization"
      - "Case study written with permission"

  # ----------------------------------------------------------
  # SEGMENT 4 — ORGANIZATIONS BURNED BY CLOUD AI OR DATA LOSS
  # Priority: MEDIUM — derived from portfolio evidence
  # ----------------------------------------------------------

  segment_4_cloud_burned:
    priority: "MEDIUM"
    rationale: "Portfolio AWS loss arc proves you have felt the loss. Empathy is the lead."

    target_profile:
      - "Organizations that lost data to a cloud provider"
      - "Organizations locked into a cloud AI vendor"
      - "Organizations that cannot send data to third-party AI"
      - "Organizations fearing vendor failure"

    lead_sources:
      - "Industry press covering cloud failures"
      - "Professional networks where loss has been shared"
      - "Referrals from law firms and compliance functions"

    outreach_sequence:
      step_1: "Identify organizations publicly affected by cloud failure or lock-in"
      step_2: "Intro email — reference the AWS loss arc as empathy, not as pitch"
      step_3: "Offer a sovereign AI readiness conversation"

  # ----------------------------------------------------------
  # TRACKING
  # ----------------------------------------------------------

  tracking:
    columns:
      - "Prospect name"
      - "Segment"
      - "Contact name"
      - "Contact role"
      - "Source"
      - "First contact date"
      - "Last contact date"
      - "Status"
      - "Next action"
      - "Notes"
    format: "Simple markdown table or CSV — start now, refine later"
    cadence: "Review weekly"

  # ----------------------------------------------------------
  # METRICS
  # ----------------------------------------------------------

  metrics:
    - "Qualified conversations per week"
    - "Proposals out per month"
    - "Pilots closed"
    - "Testimonials collected"
    - "References granted"
    - "Case studies written"

  # ----------------------------------------------------------
  # WHAT THIS DOCUMENT IS NOT
  # ----------------------------------------------------------

  not_claimed:
    - "No clients exist — none named anywhere"
    - "No ROI figures exist — none named anywhere"
    - "No testimonials exist — none named anywhere"
    - "Cynthia Evans has not responded — follow-up is the first action"
    - "Law firms are a Kott proposal, not yet owner-validated"
    - "This document is DRAFT v1.0 — derived from ICP v2.0"

  # ----------------------------------------------------------
  # IMMEDIATE NEXT ACTIONS
  # ----------------------------------------------------------

  immediate_next_actions:
    high:
      - "Follow up with Cynthia Evans — 4 weeks since meeting, no response"
      - "Draft follow-up email to Cynthia referencing the Aug 29 email"
      - "Identify first 10 genealogy nonprofits beyond 10 Million Names"
      - "Identify first 20 DMV law firms matching the ICP"
    medium:
      - "Build simple tracking table"
      - "Draft intro email templates for each segment"
    low:
      - "Review Kott's ABA and EY links for law-firm outreach language"

  sources:
    - "ICP — BUILT FROM PORTFOLIO AS EVIDENCE OF CAPABILITY.md (v2.0)"
    - "~/Repos/Mirror-Project/meeting with cynthia/"
    - "~/Repos/Mirror-Project/md files/community-outreach.md"
    - "~/Repos/Mirror-Project/md files/10M_Names_Response_Final_2026-08-24.md"
    - "~/Repos/Mirror-Project/md files/MIRROR_PROVENANCE_v3.5_2026-07-04.md"
    - "Dr. Kott email 09/25/2026"
    - "Handover YAML 09/25/2026"

# ============================================================
# Copyright © Evelyn Caro, September 25, 2026.
# All rights reserved.
# ============================================================
