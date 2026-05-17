---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-000-STRUCTURAL-SCOPE-AND-BOUNDARIES"
title: "ATLAS 050-059 · 05.050.000 — Structural Scope and Boundaries"
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
subsubject: "000"
subsubject_title: "Structural Scope and Boundaries"
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

# ATLAS 050-059 · 05.050.000 — Structural Scope and Boundaries

## 1. Purpose

Defines the **precise taxonomic scope** of the ATLAS `050-059` *Estructuras* section and establishes the **boundary rules** that distinguish structural subjects from adjacent ATLAS sections (systems, propulsion, electrical).

## 2. Scope

### 2.1 What is "Structure" within ATLAS 050-059

For the purposes of this section, **structure** is defined as:

> *Any primary, secondary, or tertiary load-bearing element of the [PROGRAMME-AIRCRAFT] airframe whose integrity is required for continued safe flight and landing, ground operations, or structural fire containment.*

This encompasses:

- **Fuselage** — pressure vessel, frames, stringers, skin panels, floor structure, crown and keel beams.
- **Wings** — wing box (spars, ribs, skins), leading/trailing edge structure, winglet structure.
- **Empennage** — HTP and VTP primary structure, attach fittings.
- **Nacelles and pylons** — engine pylon primary fittings, nacelle load-bearing structure.
- **Doors** — structural door frames, hinges, latch fittings, pressure stops.
- **Windows** — window frames and retention structure.

### 2.2 Items explicitly out of scope

| Item | Governed by |
|---|---|
| EMA actuator units (non-structural) | ATLAS 027 / ATLAS 029 (flight controls) |
| Fuel system plumbing | ATLAS 028 |
| Electrical harnesses and connectors | ATLAS 024 |
| Pressurisation seals (non-load-bearing) | ATLAS 021 |
| Interior furnishing structure (non-CS-25 Subpart C) | ATLAS 025 |

### 2.3 Boundary Rule S-B01 — Structural vs. System Interface

Where a system component attaches to airframe structure, the **attachment fitting, insert, or pad-up** belongs in `050-059`. The **system component itself** belongs in the relevant systems ATLAS section.

### 2.4 Cross-references

| Subject | ATLAS ref |
|---|---|
| Standard Practices (repair, NDT, materials) | `051_Standard-Practices-Structures` |
| Doors detailed structure | `052_Doors` |
| Fuselage detailed structure | `053_Fuselage` |
| Nacelles and pylons | `054_Nacelles-and-Pylons` |
| Stabilizers | `055_Stabilizers` |
| Windows | `056_Windows` |
| Wings | `057_Wings` |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-000-STRUCTURAL-SCOPE-AND-BOUNDARIES` |
| Architecture | `ATLAS` |
| Code range | `050-059` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/050_General/050-000-Structures-General/` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| CS-25.301 | Loads — General |
| CS-25.571 | Damage-tolerance and fatigue evaluation of structure |
| [`./README.md`](./README.md) | Subsubject index |
| [`../README.md`](../README.md) | 050_General subsection index |
