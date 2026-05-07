---
document_id: QATL-ATLAS-1000-STA-110-119-01-110-README
title: "STA 110-119 · 01.110 — Estructuras Orbitales (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "110-119"
section: "01"
section_title: "Estructuras y Materiales Espaciales"
subsection: "110"
subsection_title: "Estructuras Orbitales"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "111_Materiales-Espaciales"
  - "112_Proteccion-Termica-y-Radiacion"
safety_boundary: "structural-mission critical; requires explicit load-path definition, launch-load verification, orbital-load assumptions, inspection logic, damage-tolerance evidence and lifecycle traceability"
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 110-119 · Section 01 · Subsection 110 — Estructuras Orbitales

## 1. Purpose

Subsection-level index for *Estructuras Orbitales* (`110`) within STA `110-119` — *Estructuras y Materiales Espaciales*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **structural-mission critical**: all subsubjects require explicit load-path definition, launch-load verification, orbital-load assumptions, inspection logic, damage-tolerance evidence, and lifecycle traceability.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `110` *Orbital Structures*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `111_Materiales-Espaciales`, `112_Proteccion-Termica-y-Radiacion`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](000_Overview.md) | active |
| 001 | Orbital Structures Controlled Definition | [`001_Orbital-Structures-Controlled-Definition.md`](001_Orbital-Structures-Controlled-Definition.md) | active |
| 002 | Primary and Secondary Structural Elements | [`002_Primary-and-Secondary-Structural-Elements.md`](002_Primary-and-Secondary-Structural-Elements.md) | active |
| 003 | Truss, Frames, Shells and Deployable Structures | [`003_Truss-Frames-Shells-and-Deployable-Structures.md`](003_Truss-Frames-Shells-and-Deployable-Structures.md) | active |
| 004 | Load Paths, Launch Loads and Orbital Loads | [`004_Load-Paths-Launch-Loads-and-Orbital-Loads.md`](004_Load-Paths-Launch-Loads-and-Orbital-Loads.md) | active |
| 005 | Docking, Berthing and Structural Interfaces | [`005_Docking-Berthing-and-Structural-Interfaces.md`](005_Docking-Berthing-and-Structural-Interfaces.md) | active |
| 006 | Modular Assembly and On-Orbit Construction | [`006_Modular-Assembly-and-On-Orbit-Construction.md`](006_Modular-Assembly-and-On-Orbit-Construction.md) | active |
| 007 | Thermal Distortion, Fatigue and Damage Tolerance | [`007_Thermal-Distortion-Fatigue-and-Damage-Tolerance.md`](007_Thermal-Distortion-Fatigue-and-Damage-Tolerance.md) | active |
| 008 | Inspection, Monitoring and Structural Health Management | [`008_Inspection-Monitoring-and-Structural-Health-Management.md`](008_Inspection-Monitoring-and-Structural-Health-Management.md) | active |
| 009 | ECSS / NASA Structural Standards Mapping | [`009_ECSS-NASA-Structural-Standards-Mapping.md`](009_ECSS-NASA-Structural-Standards-Mapping.md) | active |
| 010 | Traceability, Evidence and Lifecycle Governance | [`010_Traceability-Evidence-and-Lifecycle-Governance.md`](010_Traceability-Evidence-and-Lifecycle-Governance.md) | active |
| 011–099 | *(reserved)* | — | reserved |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `110` — Estructuras Orbitales |
| Subsubject namespace | `000`–`010` active / `011`–`099` reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Safety boundary | structural-mission critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/110_Estructuras-Orbitales/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE`, `support_q_divisions = [Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]`, and `governance_class = baseline` from the parent STA section. Extensions added under `011`–`099` shall preserve those header fields, declare the `safety_boundary`, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
