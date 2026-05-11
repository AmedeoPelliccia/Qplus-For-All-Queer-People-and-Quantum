---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-050-INSPECTION-NDT-AND-DAMAGE-TOLERANCE-PRACTICES-OVERVIEW"
title: "ATLAS 050-059 · 05.051.050 — Inspection, NDT and Damage-Tolerance Practices — Overview"
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
subsubject: "050"
subsubject_title: "Inspection, NDT and Damage-Tolerance Practices"
parent_subsubject_doc: ./README.md
---

# ATLAS 050-059 · 05.051.050 — Inspection, NDT and Damage-Tolerance Practices — Overview

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Provides an overview of the inspection programme, non-destructive testing methods, and damage tolerance principles applied to Q+ATLANTIDE aircraft structures. The programme integrates MSG-3 maintenance task development with in-service NDT execution to maintain structural integrity throughout the aircraft operational life.

---

## 2. Scope

### 2.1 Context

Structural integrity is maintained through a combination of in-service inspection, NDT, and damage tolerance assessments. The inspection programme is derived from the damage tolerance and fatigue analysis conducted during certification and is reflected in the MPD and MSG-3 maintenance tasks. All inspections must be performed by appropriately qualified and authorised personnel.

The structural inspection programme addresses both fatigue cracking and accidental damage. Fatigue inspections are derived from damage tolerance analysis; accidental damage inspections are performed following any hard landing, birdstrike, or other significant event. Both categories require documented findings and dispositioning through the CAMO.

### 2.2 Scope Diagram

```mermaid
graph TD
    A[Structural Integrity Programme] --> B[Damage Tolerance Analysis — DTA]
    B --> C[MSG-3 Inspection Task Development]
    C --> D[MPD Task Issuance]
    D --> E[In-Service Inspection: Scheduled and Unscheduled]
    E --> F[NDT as Required by Task]
    F --> G{Damage Found?}
    G -->|Yes| H[Assess vs ADL]
    H --> I[Repair / Monitor / Accept]
    G -->|No| J[Record and Close Task]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Regulatory Basis | EASA CS-25.571 and CS-25.573 |
| Programme Methodology | MSG-3 Damage Tolerance Analysis |
| Inspection Intervals | Derived from DTA crack growth analysis |
| NDT Methods | UT, EC, RT, Visual, Active Thermography |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-050-INSPECTION-NDT-AND-DAMAGE-TOLERANCE-PRACTICES-OVERVIEW` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-050-Inspection-NDT-and-Damage-Tolerance-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| EASA CS-25.571 | Damage-Tolerant Design Requirements |
| MSG-3 Revision 2 | Maintenance Programme Development for Transport Category Aircraft |
| ATA MSG-3 | Maintenance Steering Group Task Logic Analysis |
| EASA AMC 20-20 | Continuing Structural Integrity Programme |
