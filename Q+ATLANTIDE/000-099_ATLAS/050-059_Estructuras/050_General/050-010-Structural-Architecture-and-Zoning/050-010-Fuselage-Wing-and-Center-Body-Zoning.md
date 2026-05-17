---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-010-FUSELAGE-WING-AND-CENTER-BODY-ZONING"
title: "ATLAS 050-059 · 05.050.010 — Fuselage, Wing and Centre-Body Zoning"
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
subsubject_title: "Fuselage Wing and Centre Body Zoning"
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

# ATLAS 050-059 · 05.050.010 — Fuselage, Wing and Centre-Body Zoning

## 1. Purpose

Provides the **detailed zone map** for the [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT] fuselage, wing, and centre wing-body junction, including sub-zone identifiers, station-referenced geometric boundaries, and CPCP zone assignments.

## 2. Scope

### 2.1 Fuselage Sub-Zones

| Zone | Sub-zone | FS range | Description |
|---|---|---|---|
| Z100 | Z110 | 0–1,200 | Nose radome and pressure bulkhead |
| Z100 | Z120 | 1,200–2,500 | Forward fuselage (first pressure dome to fwd cabin) |
| Z200 | Z210 | 2,500–5,000 | Forward cabin barrel |
| Z200 | Z220 | 5,000–7,000 | Forward cabin to wing LE |
| Z300 | Z310 | 7,000–9,000 | Wing-box/cabin intersection (upper) |
| Z300 | Z320 | 7,000–9,000 | Wing-box/cabin intersection (lower/keel) |
| Z400 | Z410 | 9,000–13,000 | Rear cabin |
| Z400 | Z420 | 13,000–17,500 | Aft fuselage |
| Z500 | Z510 | 17,500–21,000 | Tail cone |

### 2.2 Wing Sub-Zones

| Zone | Sub-zone | WS range | Description |
|---|---|---|---|
| Z600 | Z610 | 0–1,500 | Centre section (within fuselage) |
| Z600 | Z620 | 1,500–4,500 | Inboard wing box |
| Z700 | Z710 | 4,500–10,000 | Mid-span wing box |
| Z700 | Z720 | 10,000–16,000 | Outboard wing box and winglet root |

### 2.3 Zone Diagram

```mermaid
graph LR
    Z110[Z110 Nose] --> Z120[Z120 Fwd Fus]
    Z120 --> Z210[Z210 Fwd Cabin]
    Z210 --> Z310[Z310 Wing-Body]
    Z310 --> Z410[Z410 Rear Cabin]
    Z410 --> Z510[Z510 Tail Cone]
    Z310 --> Z610[Z610 Centre Box]
    Z610 --> Z620[Z620 Inboard Wing]
    Z620 --> Z710[Z710 Mid Wing]
    Z710 --> Z720[Z720 Outboard Wing]
```

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-010-FUSELAGE-WING-AND-CENTER-BODY-ZONING` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| CS-25.571 | DT zone assignments |
| AMC 25.571 | CPCP zone map |
| [`./README.md`](./README.md) | Subsubject index |
