---
document_id: QATL-ATLAS-1000-STA-170-179-07-173-README
title: "STA 170-179 · 07.173 — Ensamblaje en Órbita (Subsection Index)"
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
subsection: "173"
subsection_title: "Ensamblaje en Órbita"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-STRUCTURES, Q-INDUSTRY, Q-GREENTECH]
orb_function_support: [ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "103_Seguridad-de-Mision"
  - "110_Estructuras-Orbitales"
  - "111_Materiales-Espaciales"
  - "112_Proteccion-Termica-y-Radiacion"
  - "133_Distribucion-Electrica"
  - "140_GNC-Guiado-Navegacion-y-Control"
  - "141_Avionica-Espacial"
  - "142_Software-de-Vuelo"
  - "143_Control-de-Mision"
  - "144_Autonomia"
  - "170_Servicing-Orbital"
  - "171_Inspeccion-en-Orbita"
  - "172_Reparacion-en-Orbita"
safety_boundary: "on-orbit assembly critical; requires explicit modular-interface control, docking/berthing validation, robotic-manipulation boundaries, joining/locking verification, integrated power/data/thermal/fluid checks, abort modes and lifecycle traceability"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 170-179 · Section 07 · Subsection 173 — Ensamblaje en Órbita

## 1. Purpose

Subsection-level index for *Ensamblaje en Órbita* (`173`) within STA `170-179` — *Operaciones y Mantenimiento en Órbita*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **on-orbit assembly critical**: all subsubjects require explicit modular-interface control, docking/berthing validation, robotic-manipulation boundaries, joining/locking verification, integrated power/data/thermal/fluid checks, abort modes, and lifecycle traceability.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `173` *On-Orbit Assembly*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `103_Seguridad-de-Mision`, `110_Estructuras-Orbitales`, `111_Materiales-Espaciales`, `112_Proteccion-Termica-y-Radiacion`, `133_Distribucion-Electrica`, `140_GNC-Guiado-Navegacion-y-Control`, `141_Avionica-Espacial`, `142_Software-de-Vuelo`, `143_Control-de-Mision`, `144_Autonomia`, `170_Servicing-Orbital`, `171_Inspeccion-en-Orbita`, `172_Reparacion-en-Orbita`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](000_Overview.md) | active |
| 001 | On-Orbit Assembly Controlled Definition | [`001_On-Orbit-Assembly-Controlled-Definition.md`](001_On-Orbit-Assembly-Controlled-Definition.md) | active |
| 002 | Assembly Mission Classes and Objectives | [`002_Assembly-Mission-Classes-and-Objectives.md`](002_Assembly-Mission-Classes-and-Objectives.md) | active |
| 003 | Modular Architecture and Assembly Units | [`003_Modular-Architecture-and-Assembly-Units.md`](003_Modular-Architecture-and-Assembly-Units.md) | active |
| 004 | Rendezvous, Docking, Berthing and Positioning Interfaces | [`004_Rendezvous-Docking-Berthing-and-Positioning-Interfaces.md`](004_Rendezvous-Docking-Berthing-and-Positioning-Interfaces.md) | active |
| 005 | Robotic Assembly and Manipulation Functions | [`005_Robotic-Assembly-and-Manipulation-Functions.md`](005_Robotic-Assembly-and-Manipulation-Functions.md) | active |
| 006 | Structural Joining, Latching and Lockdown Mechanisms | [`006_Structural-Joining-Latching-and-Lockdown-Mechanisms.md`](006_Structural-Joining-Latching-and-Lockdown-Mechanisms.md) | active |
| 007 | Power, Data, Thermal and Fluid Interface Integration | [`007_Power-Data-Thermal-and-Fluid-Interface-Integration.md`](007_Power-Data-Thermal-and-Fluid-Interface-Integration.md) | active |
| 008 | Assembly Safety Zones, Fault Containment and Abort Modes | [`008_Assembly-Safety-Zones-Fault-Containment-and-Abort-Modes.md`](008_Assembly-Safety-Zones-Fault-Containment-and-Abort-Modes.md) | active |
| 009 | ECSS-NASA-CCSDS On-Orbit Assembly Standards Mapping | [`009_ECSS-NASA-CCSDS-On-Orbit-Assembly-Standards-Mapping.md`](009_ECSS-NASA-CCSDS-On-Orbit-Assembly-Standards-Mapping.md) | active |
| 010 | Traceability, Evidence and Lifecycle Governance | [`010_Traceability-Evidence-and-Lifecycle-Governance.md`](010_Traceability-Evidence-and-Lifecycle-Governance.md) | active |
| 011–099 | *(reserved)* | — | reserved |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `170-179` |
| Section | `07` — Operaciones y Mantenimiento en Órbita |
| Subsection | `173` — Ensamblaje en Órbita |
| Subsubject namespace | `000`–`010` active / `011`–`099` reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-STRUCTURES, Q-INDUSTRY, Q-GREENTECH |
| ORB support | ORB-LEG |
| Governance class | `baseline`[^gov] |
| Safety boundary | on-orbit assembly critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/170-179_Operaciones-y-Mantenimiento-en-Orbita/173_Ensamblaje-en-Orbita/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE`, `support_q_divisions = [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-STRUCTURES, Q-INDUSTRY, Q-GREENTECH]`, and `governance_class = baseline` from the parent STA section. Extensions added under `011`–`099` shall preserve those header fields, declare the `safety_boundary`, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
