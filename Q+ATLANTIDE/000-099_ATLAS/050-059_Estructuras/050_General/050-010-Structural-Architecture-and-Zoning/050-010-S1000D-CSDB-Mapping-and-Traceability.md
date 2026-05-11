---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-010-S1000D-CSDB-MAPPING-AND-TRACEABILITY"
title: "ATLAS 050-059 · 05.050.010 — S1000D CSDB Mapping and Traceability"
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
subsubject_title: "S1000D CSDB Mapping and Traceability"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.050.010 — S1000D CSDB Mapping and Traceability

## 1. Purpose

Defines the S1000D **Data Module Code (DMC) mapping** for structural architecture and zoning content, and establishes the traceability between zone-referenced ATLAS documents and CSDB data modules.

## 2. Scope

### 2.1 DMC Pattern for Zone Documentation

Zone architecture data modules use systemCode `050` (General) with subSystemCode `01` (Architecture and Zoning):

```
DMC-AMPEL360-A-050-01-{assyCode}-{disassyCode}{variant}-{infoCode}{variant}-A_EN-US
```

### 2.2 Zone DM Allocation

| Zone group | systemCode | subSystemCode | subSubSystemCode | Info code | DM purpose |
|---|---|---|---|---|---|
| Overall zone map | 050 | 01 | 00 | 040 | Zone architecture description |
| Fuselage zones | 050 | 01 | 10 | 040 | Fuselage zone detailed map |
| Wing zones | 050 | 01 | 20 | 040 | Wing zone detailed map |
| CLPZ register | 050 | 01 | 30 | 040 | Critical load path zone register |
| Zone coding rules | 050 | 01 | 40 | 040 | Zone coding and designator rules |

### 2.3 ATLAS-to-CSDB Traceability

| ATLAS document | CSDB DM |
|---|---|
| This file (S1000D mapping) | `DMC-AMPEL360-A-050-0100-00A-040A-A` |
| `050-010-Aircraft-Structural-Zone-Definition.md` | `DMC-AMPEL360-A-050-0100-00A-040A-A` |
| `050-010-Fuselage-Wing-and-Center-Body-Zoning.md` | `DMC-AMPEL360-A-050-0110-00A-040A-A` + `DMC-AMPEL360-A-050-0120-00A-040A-A` |
| `050-010-Structural-Zone-Coding-and-Designator-Rules.md` | `DMC-AMPEL360-A-050-0140-00A-040A-A` |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-010-S1000D-CSDB-MAPPING-AND-TRACEABILITY` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| S1000D Issue 5.0 | International specification for technical publications |
| [`./README.md`](./README.md) | Subsubject index |
| [`../../README.md`](../../README.md) | 050-059_Estructuras section index |
