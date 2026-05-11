---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-030-TEMPORARY-PERMANENT-AND-DEFERRED-REPAIRS"
title: "ATLAS 050-059 · 05.051.030 — Temporary, Permanent and Deferred Repairs"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../../README.md
parent_section_doc: ../../README.md
parent_subsection_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "050-059"
section: "05"
section_title: "Estructuras"
subsection: "051"
subsection_title: "Standard Practices — Structures"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
subsubject: "030"
subsubject_title: "Structural Repair General Practices"
parent_subsubject_doc: ./README.md
---

# ATLAS 050-059 · 05.051.030 — Temporary, Permanent and Deferred Repairs

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Defines the categories of structural repair disposition — temporary, permanent, and deferred — and specifies the conditions, limitations, and documentation requirements for each. Correct categorisation ensures that operational safety is maintained while minimising unscheduled aircraft ground time.

---

## 2. Scope

### 2.1 Context

A temporary repair restores airworthiness for a defined period or number of flight cycles pending a permanent repair. It must be accompanied by specific operational limitations and an approved time limit. Deferred repairs are permitted only within approved deferral schemes, such as those referenced in the MEL/CDL or engineering deferral orders approved under EASA Part-M.

Permanent repairs restore the structure to its original or equivalent structural capability with no time limitation. All repair categories require a completed maintenance record and a Certifying Staff release to service. The repair category must be explicitly stated in the repair record and cross-referenced to the approval basis.

### 2.2 Scope Diagram

```mermaid
graph TD
    A[Damage Assessed] --> B{Repair Urgency?}
    B -->|Permanent| C[Permanent Repair — Full Structural Restoration]
    B -->|Deferred| D[Deferral Scheme Approval — Engineering/EASA]
    B -->|Temporary| E[Temp Repair with Operational Limitation Placard]
    C --> F[Document Repair Order]
    D --> F
    E --> F
    F --> G[MEL/CDL/Repair Order Tracking to Closure]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Temp Repair Validity | Defined flight cycles or calendar days per approval |
| Deferral Authority | Engineering order / EASA-approved deferral |
| Permanent Repair Restoration | Full structural and damage tolerance life |
| Documentation | Repair Sticker, Technical Log Entry, Repair Order |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-030-TEMPORARY-PERMANENT-AND-DEFERRED-REPAIRS` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-030-Structural-Repair-General-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| AMM 51-70-00 | Structural Repair Procedures and Disposition |
| MEL/CDL Framework | Minimum Equipment / Configuration Deviation List |
| EASA Part-M / Part-CAMO | Continuing Airworthiness Management Requirements |
| SRM Chapter 51 | Disposition Tables for Temporary and Deferred Repairs |
