---
document_id: QATL-ATLAS-1000-STA-170-179-07-171-README
title: "STA 170-179 · 07.171 — Inspección en Órbita (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "170-179"
section: "07"
section_title: "Operaciones y Mantenimiento en Órbita"
subsection: "171"
subsection_title: "Inspección en Órbita"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-STRUCTURES, Q-INDUSTRY]
orb_function_support: [ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "103_Seguridad-de-Mision"
  - "110_Estructuras-Orbitales"
  - "111_Materiales-Espaciales"
  - "112_Proteccion-Termica-y-Radiacion"
  - "140_GNC-Guiado-Navegacion-y-Control"
  - "141_Avionica-Espacial"
  - "142_Software-de-Vuelo"
  - "143_Control-de-Mision"
  - "144_Autonomia"
  - "170_Servicing-Orbital"
  - "172_Reparacion-en-Orbita"
  - "173_Ensamblaje-en-Orbita"
safety_boundary: "on-orbit inspection critical; requires explicit proximity-operations control, sensor calibration, inspection criteria, damage-assessment logic, autonomous-mode boundaries, data-quality evidence and lifecycle traceability"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 170-179 · Section 07 · Subsection 171 — Inspección en Órbita

## 1. Purpose

Subsection-level index for *Inspección en Órbita* (`171`) within STA `170-179` — *Operaciones y Mantenimiento en Órbita*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **on-orbit inspection critical**: all subsubjects require explicit proximity-operations control, sensor calibration, inspection criteria, damage-assessment logic, autonomous-mode boundaries, data-quality evidence, and lifecycle traceability.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `171` *On-Orbit Inspection*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `103_Seguridad-de-Mision`, `110_Estructuras-Orbitales`, `111_Materiales-Espaciales`, `112_Proteccion-Termica-y-Radiacion`, `140_GNC-Guiado-Navegacion-y-Control`, `141_Avionica-Espacial`, `142_Software-de-Vuelo`, `143_Control-de-Mision`, `144_Autonomia`, `170_Servicing-Orbital`, `172_Reparacion-en-Orbita`, `173_Ensamblaje-en-Orbita`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](000_Overview.md) | active |
| 001 | On-Orbit Inspection Controlled Definition | [`001_On-Orbit-Inspection-Controlled-Definition.md`](001_On-Orbit-Inspection-Controlled-Definition.md) | active |
| 002 | Inspection Mission Classes and Objectives | [`002_Inspection-Mission-Classes-and-Objectives.md`](002_Inspection-Mission-Classes-and-Objectives.md) | active |
| 003 | Visual, Optical and Multispectral Inspection | [`003_Visual-Optical-and-Multispectral-Inspection.md`](003_Visual-Optical-and-Multispectral-Inspection.md) | active |
| 004 | Radar, Lidar and Proximity Sensing Inspection | [`004_Radar-Lidar-and-Proximity-Sensing-Inspection.md`](004_Radar-Lidar-and-Proximity-Sensing-Inspection.md) | active |
| 005 | Structural Health Monitoring and Damage Assessment | [`005_Structural-Health-Monitoring-and-Damage-Assessment.md`](005_Structural-Health-Monitoring-and-Damage-Assessment.md) | active |
| 006 | Thermal, Radiation and Surface Degradation Inspection | [`006_Thermal-Radiation-and-Surface-Degradation-Inspection.md`](006_Thermal-Radiation-and-Surface-Degradation-Inspection.md) | active |
| 007 | Autonomous Inspection and Robotic Inspection Modes | [`007_Autonomous-Inspection-and-Robotic-Inspection-Modes.md`](007_Autonomous-Inspection-and-Robotic-Inspection-Modes.md) | active |
| 008 | Inspection Safety Zones and Proximity Operations | [`008_Inspection-Safety-Zones-and-Proximity-Operations.md`](008_Inspection-Safety-Zones-and-Proximity-Operations.md) | active |
| 009 | ECSS-NASA-CCSDS On-Orbit Inspection Standards Mapping | [`009_ECSS-NASA-CCSDS-On-Orbit-Inspection-Standards-Mapping.md`](009_ECSS-NASA-CCSDS-On-Orbit-Inspection-Standards-Mapping.md) | active |
| 010 | Traceability, Evidence and Lifecycle Governance | [`010_Traceability-Evidence-and-Lifecycle-Governance.md`](010_Traceability-Evidence-and-Lifecycle-Governance.md) | active |
| 011–099 | *(reserved)* | — | reserved |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `170-179` |
| Section | `07` — Operaciones y Mantenimiento en Órbita |
| Subsection | `171` — Inspección en Órbita |
| Subsubject namespace | `000`–`010` active / `011`–`099` reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-LEG |
| Governance class | `baseline`[^gov] |
| Safety boundary | on-orbit inspection critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/170-179_Operaciones-y-Mantenimiento-en-Orbita/171_Inspeccion-en-Orbita/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE`, `support_q_divisions = [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-STRUCTURES, Q-INDUSTRY]`, and `governance_class = baseline` from the parent STA section. Extensions added under `011`–`099` shall preserve those header fields, declare the `safety_boundary`, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
