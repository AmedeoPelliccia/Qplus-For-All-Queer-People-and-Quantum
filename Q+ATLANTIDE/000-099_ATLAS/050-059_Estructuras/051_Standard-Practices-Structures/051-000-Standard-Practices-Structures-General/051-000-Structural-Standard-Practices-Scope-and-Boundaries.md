---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-000-STRUCTURAL-STANDARD-PRACTICES-SCOPE-AND-BOUNDARIES"
title: "ATLAS 050-059 · 05.051.000 — Structural Standard Practices — Scope and Boundaries"
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
subsection: "051"
subsection_title: "Standard Practices — Structures"
subsubject: "000"
subsubject_title: "Standard Practices Structures General"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.051.000 — Structural Standard Practices — Scope and Boundaries

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Defines the exact scope boundary of ATLAS Section 051 Standard Practices Structures, distinguishing it from adjacent ATA chapters (052–059) and identifying which tasks are governed by this section.

---

## 2. Scope

### 2.1 Context

This document clarifies where Section 051 Standard Practices authority begins and ends relative to Chapter 05 Structures sub-chapters. It identifies structural disciplines, zones, and process types that fall within scope versus those delegated to specialised sub-chapters.

The boundaries follow ATA iSpec 2200 chapter demarcation and are mapped to the Q+ATLANTIDE ATLAS-1000 register. Out-of-scope items are listed with cross-references to the applicable governing document.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[Scope Boundary 051] --> B[In Scope: General Practices]
        A --> C[Out of Scope]
        B --> D[Workmanship Rules]
        B --> E[Tooling & GSE]
        B --> F[Documentation]
        C --> G[052 Doors]
        C --> H[053 Fuselage]
        C --> I[055 Stabilizers]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| In-Scope Zone | All structural disciplines, all zones |
| Out-of-Scope | Chapter-specific repair details |
| Interface Chapters | 052, 053, 054, 055, 057 |
| Governing Standard | ATA iSpec 2200 / S1000D |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-000-STRUCTURAL-STANDARD-PRACTICES-SCOPE-AND-BOUNDARIES` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-000-Standard-Practices-Structures-General/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| AMM 51-00-00 | Structures — General Practices |
| ATA iSpec 2200 | Chapter Demarcation Rules |
| ATLAS README | Q+ATLANTIDE ATLAS-1000 Register |
| EASA CS-25 | Airworthiness Standards: Large Aeroplanes |
