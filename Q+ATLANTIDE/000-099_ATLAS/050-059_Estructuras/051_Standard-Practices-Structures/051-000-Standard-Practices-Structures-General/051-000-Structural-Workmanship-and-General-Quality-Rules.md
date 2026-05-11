---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-000-STRUCTURAL-WORKMANSHIP-AND-GENERAL-QUALITY-RULES"
title: "ATLAS 050-059 · 05.051.000 — Structural Workmanship and General Quality Rules"
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

# ATLAS 050-059 · 05.051.000 — Structural Workmanship and General Quality Rules

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Establishes minimum workmanship standards and quality rules applicable to all structural work, ensuring consistency, repeatability, and traceability across maintenance and manufacturing operations.

---

## 2. Scope

### 2.1 Context

Workmanship rules define the acceptable quality thresholds for structural assembly, repair, and modification tasks. They set the baseline criteria against which all completed structural work is inspected and accepted.

These rules are aligned with EASA Part-145, EASA Part-21, and company maintenance organisation exposition (MOE) requirements, and feed directly into inspection hold points and first-article inspection criteria.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[Workmanship Standards] --> B[Assembly Quality]
        A --> C[Repair Quality]
        A --> D[Modification Quality]
        B --> E[Inspection Hold Points]
        C --> E
        D --> E
        E --> F[Accept / Reject Decision]
        F --> G[Sign-Off & Record]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Quality Framework | EASA Part-145 / MOE |
| Inspection Hold Points | Per task card series |
| Acceptance Authority | Licensed Aircraft Engineer |
| Non-Conformance | NCR process per QMS |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-000-STRUCTURAL-WORKMANSHIP-AND-GENERAL-QUALITY-RULES` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-000-Standard-Practices-Structures-General/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| EASA Part-145 | Maintenance Organisation Requirements |
| AMM 51-11-00 | Workmanship — General |
| AS9100 Rev D | Quality Management — Aerospace |
| ASTM E1444 | Standard Practice for Magnetic Particle Testing |
