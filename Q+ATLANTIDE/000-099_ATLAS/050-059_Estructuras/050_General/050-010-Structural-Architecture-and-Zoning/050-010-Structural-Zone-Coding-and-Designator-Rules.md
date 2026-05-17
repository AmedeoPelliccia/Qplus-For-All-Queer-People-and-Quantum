---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-010-STRUCTURAL-ZONE-CODING-AND-DESIGNATOR-RULES"
title: "ATLAS 050-059 · 05.050.010 — Structural Zone Coding and Designator Rules"
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
subsubject: "010"
subsubject_title: "Structural Zone Coding and Designator Rules"
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

# ATLAS 050-059 · 05.050.010 — Structural Zone Coding and Designator Rules

## 1. Purpose

Establishes the **structural zone coding conventions and designator rules** for the [PROGRAMME-AIRCRAFT] programme, ensuring consistent zone identification across all structural data modules, drawings, stress reports, and maintenance documentation.

## 2. Scope

### 2.1 Zone Designator Format

```
Z{R}{S}{Q}[-{modifier}]
```

Where:
- `{R}` = Region digit (1–9, see §2.2)
- `{S}` = Sub-zone digit (0–9)
- `{Q}` = Qualifier digit (0–9); `0` = full zone, 1–9 = further subdivision
- `{modifier}` = optional letter suffix: `L` (LH), `R` (RH), `U` (upper), `L` (lower)

### 2.2 Region Digit Assignment

| Region digit | Structural region |
|---|---|
| 1 | Forward fuselage (Z1xx) |
| 2 | Forward cabin (Z2xx) |
| 3 | Wing-body junction (Z3xx) |
| 4 | Rear cabin and rear fuselage (Z4xx) |
| 5 | Tail cone and empennage (Z5xx) |
| 6 | Wing inboard (Z6xx) |
| 7 | Wing outboard (Z7xx) |
| 8 | Nacelles and pylons (Z8xx) |
| 9 | Doors, access panels, windows (Z9xx) |

### 2.3 Coding Rules

| Rule ID | Rule |
|---|---|
| ZCR-001 | Zone designators shall use the Z-prefix followed by exactly 3 digits. |
| ZCR-002 | Sub-zone digit shall be set to 0 for full-zone references; 1–9 for sub-zone references. |
| ZCR-003 | LH/RH symmetry designators shall be appended as suffix (e.g., Z620-L, Z620-R). |
| ZCR-004 | New zone codes require approval via Zone Code Registry change request (OCR form). |
| ZCR-005 | Zone codes are frozen at CDR; post-CDR changes require Configuration Control Board approval. |

### 2.4 Zone Code Registry

The master Zone Code Registry is maintained in the PLM system (Siemens Teamcenter) under document number `[PROGRAMME-AIRCRAFT]-STR-ZCR-001`. A read-only export is published to the Q+ATLANTIDE CSDB at each major lifecycle gate.

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-010-STRUCTURAL-ZONE-CODING-AND-DESIGNATOR-RULES` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| [PROGRAMME-AIRCRAFT]-STR-ZCR-001 | Zone Code Registry (PLM Teamcenter) |
| [`./README.md`](./README.md) | Subsubject index |
