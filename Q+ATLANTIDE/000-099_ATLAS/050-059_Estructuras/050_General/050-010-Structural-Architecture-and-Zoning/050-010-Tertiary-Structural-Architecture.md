---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-010-TERTIARY-STRUCTURAL-ARCHITECTURE"
title: "ATLAS 050-059 · 05.050.010 — Tertiary Structural Architecture"
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
subsubject_title: "Tertiary Structural Architecture"
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

# ATLAS 050-059 · 05.050.010 — Tertiary Structural Architecture

## 1. Purpose

Describes the **tertiary structural architecture** of the [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT]: TSE inventory, on-condition maintenance basis, and the architectural boundary between secondary and tertiary structure.

## 2. Scope

### 2.1 TSE Definition

Tertiary structural elements (TSEs) are non-safety-critical structural items whose failure has no direct effect on airworthiness. They include:

| TSE type | Examples |
|---|---|
| Aerodynamic fairings | Belly fairing outer skins, APU/ECS fairing, wing-body fillet |
| Access panels and covers | Inspection panel skins, service panel doors |
| Non-structural brackets | Wire harness clips, pipe support brackets (non-CS-25 Subpart C) |
| Antenna mounting structures | Satcom antenna base plate, VHF antenna mounting |
| Cabin trim attachments | Overhead bin rails, monument seat rails (non-floor-beam) |

### 2.2 TSE Maintenance Basis

TSEs are maintained on an **on-condition** basis:
- Inspected during routine line maintenance (visual at A-check).
- Replaced when damage or corrosion is found.
- No programmed replacement or inspection interval required.
- Material: primarily GFRP/CFRP fairing panels; aluminium brackets.

### 2.3 TSE / SSE Boundary Rule

The boundary between SSE and TSE is determined by failure-effect analysis:
- If failure of the element could cause consequential damage to a PSE or SSE within one flight: → SSE
- If failure of the element causes no airworthiness consequence within one flight: → TSE

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-010-TERTIARY-STRUCTURAL-ARCHITECTURE` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| MSG-3 Rev 3 | On-condition basis for TSE |
| [`./README.md`](./README.md) | Subsubject index |
