---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-060-REPAIR-DECISION-LOGIC-AND-ESCALATION-RULES"
title: "ATLAS 050-059 · 05.050.060 — Repair Decision Logic and Escalation Rules"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../../README.md
parent_section_doc: ../../README.md
parent_subsection_doc: ../README.md
parent_subsubject_doc: ./README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "050-059"
section: "05"
section_title: "Estructuras"
subsection: "050"
subsection_title: "General"
subsubject: "060"
subsubject_title: "Repair Decision Logic and Escalation Rules"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
standard_scope: agnostic
programme_specific: false
---

# ATLAS 050-059 · 05.050.060 — Repair Decision Logic and Escalation Rules

## 1. Purpose

Defines the **repair decision logic and escalation rules** for [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT] structural damage findings: the decision path from damage discovery through allowable-damage assessment, SRM pre-approved repair selection, and escalation to a Manufacturer Repair Approval (MRA) or engineering disposition when SRM coverage is exceeded.

## 2. Scope

### 2.1 Context

When a structural discrepancy is found during inspection, the maintenance technician must follow a defined decision process to determine the appropriate disposition: the damage may be within the allowable damage limits (ADL) and require no action; it may fall within the SRM pre-approved repair envelope; or it may exceed SRM limits and require escalation to the manufacturer's structural engineering team. Timely escalation is critical: operating an aircraft with damage beyond ADL without a valid engineering disposition is an airworthiness violation.

Escalation paths for CFRP primary structure involve the Structures Damage Tolerance Group (SDTG) and require submission of a completed damage report (including fibre-optic or thermographic imagery) before an MRA is issued. Metallic structure damage beyond SRM limits is escalated via the Structural Engineering Disposition (SED) process.

### 2.2 Repair Decision Flowchart

```mermaid
flowchart TD
    A[Damage Found During Inspection] --> B[Measure and characterise damage]
    B --> C{Within ADL?}
    C -->|Yes| D[No repair needed. Log entry and continue service]
    C -->|No| E{Within SRM pre-approved repair envelope?}
    E -->|Yes| F[Apply SRM repair per AMM/SRM procedure]
    E -->|No| G{Safety flight risk?}
    G -->|Yes, aircraft AOG| H[Raise immediate MRA — aircraft grounded until disposition]
    G -->|No, can defer| I[Raise SED or MRA with planned repair timeline]
    F --> J[Return to service after inspection and sign-off]
    H --> J
    I --> J
```

### 2.3 Escalation Path Summary

| Damage Category | Disposition Path | Response Time |
|---|---|---|
| Within ADL | No action; log book entry | Immediate (no delay) |
| SRM pre-approved | SRM repair procedure | Check period turnaround |
| Beyond SRM — non-critical | SED / MRA requested | Typically 5–10 working days |
| Beyond SRM — safety-critical | Immediate MRA; AOG | < 24 hours response target |
| Novel damage type (no precedent) | SDTG escalation + special inspection | As agreed with EASA |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-060-REPAIR-DECISION-LOGIC-AND-ESCALATION-RULES` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/050_General/050-060-Maintenance-Concept-General/` |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| CS-25.571 | Structural residual strength requirements |
| SRM-[PROGRAMME-AIRCRAFT]-050 | Structural Repair Manual — Chapter 050 |
| EASA Part-145 | Approved Maintenance Organisation — release to service |
| SED-PROC-[PROGRAMME-AIRCRAFT]-001 | Structural Engineering Disposition Procedure |
| [`./README.md`](./README.md) | Subsubject 060 index |
| [`../README.md`](../README.md) | 050_General subsection index |
