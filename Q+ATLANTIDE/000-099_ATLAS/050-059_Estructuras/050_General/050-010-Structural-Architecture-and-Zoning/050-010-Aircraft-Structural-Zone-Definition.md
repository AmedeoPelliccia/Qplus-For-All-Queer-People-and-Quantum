---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-010-AIRCRAFT-STRUCTURAL-ZONE-DEFINITION"
title: "ATLAS 050-059 · 05.050.010 — Aircraft Structural Zone Definition"
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
subsubject_title: "Aircraft Structural Zone Definition"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.050.010 — Aircraft Structural Zone Definition

## 1. Purpose

Defines the **structural zone taxonomy** for the AMPEL360 eWTW, establishing top-level zone identifiers, their geometric extents, structural classification, and the mapping to ATA/S1000D zone codes.

## 2. Scope

### 2.1 Zone Numbering Convention

Structural zones use a three-digit identifier in the range `Z100`–`Z900`. The first digit denotes the primary structural region:

| Range | Region |
|---|---|
| Z100–Z199 | Forward fuselage |
| Z200–Z299 | Centre forward fuselage |
| Z300–Z399 | Centre wing box and cabin crossing |
| Z400–Z499 | Rear cabin and rear fuselage |
| Z500–Z599 | Tail cone and empennage |
| Z600–Z699 | Wing inboard |
| Z700–Z799 | Wing outboard |
| Z800–Z899 | Nacelles and pylons |
| Z900–Z999 | Doors and access panels |

### 2.2 Zone Spatial Extents (Top-Level)

| Zone | FS start | FS end | WS / BL limits | WL limits |
|---|---|---|---|---|
| Z100 | 0 | 2,500 | ±BL 2,000 | WL 1,000–4,500 |
| Z300 | 7,000 | 11,000 | ±WS 16,000 (with wing) | WL 800–5,000 |
| Z600 | — | — | WS 0–4,500 | per wing contour |
| Z700 | — | — | WS 4,500–16,000 | per wing contour |

(Full zone table in Design Basis Document DBD-AMPEL360-STRUCT-001 §3.)

### 2.3 Zone Classification Attributes

Each zone carries the following classification attributes:

| Attribute | Options |
|---|---|
| Structural tier | Primary / Secondary / Tertiary |
| Pressurisation | Pressurised / Unpressurised |
| Access type | Routine (every C-check) / Periodic (every D-check) / Special |
| DT basis | Damage-tolerant / Safe-life / On-condition |
| CPCP zone | Zone A (severe) / Zone B (average) / Zone C (benign) |

### 2.4 Zone Definition Flowchart

```mermaid
flowchart LR
    A[Aircraft Geometry Model CAD] --> B[FS/WS/WL/BL Boundaries]
    B --> C[Zone Identifier Zxxx]
    C --> D[Structural Tier P/S/T]
    C --> E[Pressurisation Status]
    C --> F[CPCP Zone A/B/C]
    D --> G[MSG-3 / DT Analysis]
```

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-010-AIRCRAFT-STRUCTURAL-ZONE-DEFINITION` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| CS-25.571 | Damage-tolerance and fatigue evaluation |
| AMC 25.571 | CPCP zone classification |
| [`./README.md`](./README.md) | Subsubject index |
