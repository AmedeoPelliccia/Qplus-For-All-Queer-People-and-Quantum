---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-030-ALLOWABLE-DAMAGE-LIMITS-AND-REPAIR-CRITERIA"
title: "ATLAS 050-059 · 05.051.030 — Allowable Damage Limits and Repair Criteria"
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

# ATLAS 050-059 · 05.051.030 — Allowable Damage Limits and Repair Criteria

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Defines the allowable damage limits (ADL) for primary and secondary structure and establishes the criteria for when repair is mandatory. ADL tables provide zone-specific thresholds that balance operational flexibility with structural safety margins required under CS-25.571.

---

## 2. Scope

### 2.1 Context

Allowable damage limits are zone-specific thresholds defined in the SRM for each structural component. Damage within ADL does not require structural repair but may require cosmetic treatment or monitoring. The ADL accounts for residual strength requirements per CS-25.571, ensuring that structure with damage at or below the limit retains sufficient residual strength throughout the inspection interval.

ADL tables are specific to each structural zone classification. Primary structure (Zone 1) has more restrictive ADL values than secondary structure (Zone 2), reflecting the higher consequence of failure. Damage in close proximity to fastener holes, cutouts, or existing repairs may be subject to additional restrictions beyond the standard ADL tables.

### 2.2 Scope Diagram

```mermaid
graph TD
    A[Structure Zone Identified] --> B[Retrieve SRM ADL Table]
    B --> C[Measure Damage: Depth, Area, Length]
    C --> D{Damage ≤ ADL?}
    D -->|Yes| E[No Structural Repair Required]
    E --> F[Monitor or Apply Cosmetic Treatment]
    D -->|No| G[Initiate Repair Action]
    G --> H[Repair Scheme or Engineering Order]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| ADL Basis | Residual Strength, Fatigue Life, Stiffness |
| Zone Categories | Z1 Primary, Z2 Secondary, Z3 Tertiary |
| Measurement Precision | ±0.1 mm depth, ±1 mm length |
| SRM Revision Currency | At time of damage assessment |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-030-ALLOWABLE-DAMAGE-LIMITS-AND-REPAIR-CRITERIA` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-030-Structural-Repair-General-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| SRM 51-00 | Allowable Damage Tables by Zone and Structural Component |
| EASA CS-25.571(b) | Residual Strength Requirements for Damage-Tolerant Structure |
| EASA CS-25.573 | Damage Tolerance and Fatigue Evaluation of Structure |
| FAA AC 120-104 | Establishing and Implementing Limit of Validity (LOV) of the Engineering Data |
