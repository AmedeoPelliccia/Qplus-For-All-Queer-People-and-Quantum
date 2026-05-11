---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-010-MATERIAL-SELECTION-AND-ALLOWABLES"
title: "ATLAS 050-059 · 05.051.010 — Material Selection and Allowables"
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
subsubject: "010"
subsubject_title: "Structural Materials and Processes"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.051.010 — Material Selection and Allowables

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Provides guidance on material selection criteria for new structural designs and repairs, and documents the process for establishing and applying structural material allowables within the Q+ATLANTIDE design framework.

---

## 2. Scope

### 2.1 Context

Material selection is driven by load case requirements, environmental exposure, weight targets, and maintainability. Allowables are established at B-basis (90th percentile, 95% confidence) for primary structure and A-basis for fracture-critical applications.

Design allowables are stored in the ATLAS Materials Allowables Database (MAD) and are updated whenever new test data or revised standards become available, with change notifications issued to all affected design teams.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[Design Requirement] --> B[Load Case Analysis]
        B --> C[Material Candidate Selection]
        C --> D[Retrieve Allowables from MAD]
        D --> E{A-Basis or B-Basis?}
        E -- Fracture Critical --> F[A-Basis]
        E -- Primary Structure --> G[B-Basis]
        F & G --> H[Apply to Analysis]
        H --> I[Document in Stress Report]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| A-Basis | 99th percentile, 95% confidence |
| B-Basis | 90th percentile, 95% confidence |
| MAD Source | MMPDS-12 / CMR / test data |
| Update Authority | Q-STRUCTURES Chief Engineer |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-010-MATERIAL-SELECTION-AND-ALLOWABLES` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-010-Structural-Materials-and-Processes/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| MMPDS-12 | Metallic Materials Properties |
| CMH-17 Vol.1 | Composite Materials Handbook |
| EASA CS-25.613 | Material Strength Properties |
| SAE ARP1796 | Material Allowables Process |
