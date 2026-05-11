---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-030-REPAIR-CLASSIFICATION-AND-DAMAGE-ASSESSMENT"
title: "ATLAS 050-059 · 05.051.030 — Repair Classification and Damage Assessment"
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

# ATLAS 050-059 · 05.051.030 — Repair Classification and Damage Assessment

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Establishes the methodology for classifying structural damage and assigning the appropriate repair category (minor/major) in accordance with regulatory and OEM requirements. The classification process ensures that the correct level of engineering authority, documentation, and inspection is applied to each repair.

---

## 2. Scope

### 2.1 Context

Damage assessment begins with a visual inspection to characterise the extent, type, and location of damage. Measurements are recorded and compared against SRM allowable damage limits. Damage exceeding allowable limits requires an engineering disposition. Classification as minor or major determines the approval authority required for the repair scheme.

Major repairs require an EASA-approved engineering order or are performed under an approved SRM chapter. Minor repairs are performed directly in accordance with the SRM without additional engineering involvement. In all cases, the repair record must reference the approval basis, and the certifying staff must verify compliance before release.

### 2.2 Scope Diagram

```mermaid
graph TD
    A[Damage Found] --> B[Visual Survey]
    B --> C[Measure Damage Extent]
    C --> D[Compare to SRM ADL]
    D --> E{Within Limits?}
    E -->|Yes| F[Allowable Damage — Monitor/Accept]
    E -->|No| G[Classify Minor or Major Repair]
    G --> H[Engineering Disposition]
    H --> I[Repair Scheme Approval]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Damage Categories | Dent, Scratch, Gouge, Crack, Delamination |
| Classification Authority | SRM ADL / Major Repair SB |
| Measurement Tools | Depth Gauge, Borescope, Ultrasonic |
| Disposition Paths | Fly-as-is, Monitor, Repair, Replace |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-030-REPAIR-CLASSIFICATION-AND-DAMAGE-ASSESSMENT` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-030-Structural-Repair-General-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| SRM Chapter 51-00 | Allowable Damage Limit Tables |
| FAA AC 43.13-1B | Acceptable Methods, Techniques and Practices — Aircraft Inspection and Repair |
| EASA CS-25.571 | Damage Tolerance and Fatigue Evaluation |
| ASTM E2533 | Standard Guide for NDE of Polymer Matrix Composites |
