---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-010-ACCESS-MAINTENANCE-AND-INSPECTION-ZONES"
title: "ATLAS 050-059 · 05.050.010 — Access, Maintenance and Inspection Zones"
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
subsubject_title: "Access Maintenance and Inspection Zones"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.050.010 — Access, Maintenance and Inspection Zones

## 1. Purpose

Defines the **access, maintenance, and inspection (AMI) zone** layout for the AMPEL360 eWTW, mapping structural zones to their applicable inspection access method, access panel locations, and inspection check level.

## 2. Scope

### 2.1 Access Zone Classification

| Access class | Definition | Examples |
|---|---|---|
| Class A | Direct visual access — no panels required | Fuselage exterior, wing upper skin external |
| Class B | Panel removal required | Wing box through access panels, aft fuselage bilge |
| Class C | Structure disassembly required | WFIJ inner face, fuselage lap joint inner row |
| Class D | Heavy maintenance access | Centre wing box inner surfaces (D-check only) |

### 2.2 Inspection Access by Zone

| Zone | Access class | Nominal check level | Special equipment |
|---|---|---|---|
| Z110–Z120 | A (external) + B (internal) | A-check visual + 2C HFEC | Articulated arm for nose cone interior |
| Z210–Z220 | B | 2C HFEC row 1 | Access panels fwd cargo bay |
| Z310 | C | 4C PAUT + WFIJ UT | Belly cargo unload required |
| Z610–Z620 | B + C | 2C visual + 4C PAUT spar | Wing root access panel removal |
| Z710–Z720 | A + B | A-check visual + 2C HFEC LE | Scaffolding for leading edge |

### 2.3 SHM Integration with Access Zones

Zones with embedded FBG/PWAS sensor networks (Z310, Z610) benefit from continuous structural monitoring, potentially enabling extension of 2C inspection intervals subject to AMC 20-29A credit.

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-010-ACCESS-MAINTENANCE-AND-INSPECTION-ZONES` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| CS-25 AMC 20-29A | Onboard maintenance systems — SHM interval credit |
| MSG-3 Rev 3 | Maintenance programme development |
| [`./README.md`](./README.md) | Subsubject index |
