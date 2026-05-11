---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-000-STRUCTURAL-TOLERANCES-AND-ACCEPTANCE-PRINCIPLES"
title: "ATLAS 050-059 · 05.051.000 — Structural Tolerances and Acceptance Principles"
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

# ATLAS 050-059 · 05.051.000 — Structural Tolerances and Acceptance Principles

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Defines the dimensional tolerances, surface quality criteria, and acceptance principles used to evaluate the conformity of structural components, repairs, and assemblies.

---

## 2. Scope

### 2.1 Context

Tolerances specified in this document represent the allowable deviations from nominal design dimensions for structural elements. Acceptance is based on fitness-for-purpose criteria aligned with damage tolerance and fatigue life requirements.

Acceptance principles follow a hierarchical approach: drawing nominal → allowable deviation per AMM → engineering disposition for out-of-tolerance findings, with each level requiring appropriate authorisation.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[Measurement Result] --> B{Within Drawing Tolerance?}
        B -- Yes --> C[Accept — Record]
        B -- No --> D{Within AMM Limits?}
        D -- Yes --> E[Accept with Note]
        D -- No --> F[Engineering Disposition]
        F --> G{Repair / Scrap / Defer?}
        G --> H[Document Decision]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Nominal Tolerance | Per approved drawing |
| AMM Repair Limit | Per 51-xx-xx AMM task |
| Oversize Fastener Limit | Up to +2 drill sizes |
| Surface Finish | Ra per material spec |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-000-STRUCTURAL-TOLERANCES-AND-ACCEPTANCE-PRINCIPLES` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-000-Standard-Practices-Structures-General/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| AMM 51-40-00 | Allowable Damage and Repairs |
| EASA CS-25.305 | Strength and Deformation |
| MIL-HDBK-17 | Composite Materials Handbook |
| SAE ARP4761 | Safety Assessment Processes |
