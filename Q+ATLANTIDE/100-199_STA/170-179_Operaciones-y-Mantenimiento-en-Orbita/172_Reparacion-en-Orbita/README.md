---
document_id: QATL-ATLAS-1000-STA-170-179-07-172-README
title: "STA 170-179 · 07.172 — Reparación en Órbita (Subsection Index)"
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
subsection: "172"
subsection_title: "Reparación en Órbita"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-STRUCTURES, Q-INDUSTRY, Q-GREENTECH]
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
  - "171_Inspeccion-en-Orbita"
  - "173_Ensamblaje-en-Orbita"
safety_boundary: "on-orbit repair critical; requires explicit repair admissibility criteria, damage-assessment evidence, robotics safety boundaries, modular-replacement control, abort modes, post-repair verification and lifecycle traceability"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 170-179 · Section 07 · Subsection 172 — Reparación en Órbita

## 1. Purpose

Subsection-level index for *Reparación en Órbita* (`172`) within STA `170-179` — *Operaciones y Mantenimiento en Órbita*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **on-orbit repair critical**: all subsubjects require explicit repair admissibility criteria, damage-assessment evidence, robotics safety boundaries, modular-replacement control, abort modes, post-repair verification, and lifecycle traceability.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `172` *On-Orbit Repair*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `103_Seguridad-de-Mision`, `110_Estructuras-Orbitales`, `111_Materiales-Espaciales`, `112_Proteccion-Termica-y-Radiacion`, `140_GNC-Guiado-Navegacion-y-Control`, `141_Avionica-Espacial`, `142_Software-de-Vuelo`, `143_Control-de-Mision`, `144_Autonomia`, `170_Servicing-Orbital`, `171_Inspeccion-en-Orbita`, `173_Ensamblaje-en-Orbita`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`172-000-General.md`](./172-000-General.md) | active |
| 010 | On Orbit Repair Controlled Definition | [`172-010-On-Orbit-Repair-Controlled-Definition.md`](./172-010-On-Orbit-Repair-Controlled-Definition.md) | active |
| 020 | Repair Mission Classes and Objectives | [`172-020-Repair-Mission-Classes-and-Objectives.md`](./172-020-Repair-Mission-Classes-and-Objectives.md) | active |
| 030 | Damage Assessment and Repair Admissibility | [`172-030-Damage-Assessment-and-Repair-Admissibility.md`](./172-030-Damage-Assessment-and-Repair-Admissibility.md) | active |
| 040 | Robotic Repair and Manipulation Functions | [`172-040-Robotic-Repair-and-Manipulation-Functions.md`](./172-040-Robotic-Repair-and-Manipulation-Functions.md) | active |
| 050 | Modular Replacement and Orbital LRU Exchange | [`172-050-Modular-Replacement-and-Orbital-LRU-Exchange.md`](./172-050-Modular-Replacement-and-Orbital-LRU-Exchange.md) | active |
| 060 | Structural Patch Bonding and Sealing Concepts | [`172-060-Structural-Patch-Bonding-and-Sealing-Concepts.md`](./172-060-Structural-Patch-Bonding-and-Sealing-Concepts.md) | active |
| 070 | Electrical Avionics and Payload Repair Interfaces | [`172-070-Electrical-Avionics-and-Payload-Repair-Interfaces.md`](./172-070-Electrical-Avionics-and-Payload-Repair-Interfaces.md) | active |
| 080 | Repair Safety Zones Fault Containment and Abort Modes | [`172-080-Repair-Safety-Zones-Fault-Containment-and-Abort-Modes.md`](./172-080-Repair-Safety-Zones-Fault-Containment-and-Abort-Modes.md) | active |
| 090 | Traceability Evidence and Lifecycle Governance | [`172-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./172-090-Traceability-Evidence-and-Lifecycle-Governance.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `170-179` |
| Section | `07` — Operaciones y Mantenimiento en Órbita |
| Subsection | `172` — Reparación en Órbita |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-STRUCTURES, Q-INDUSTRY, Q-GREENTECH |
| ORB support | ORB-LEG |
| Governance class | `baseline`[^gov] |
| Safety boundary | on-orbit repair critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/170-179_Operaciones-y-Mantenimiento-en-Orbita/172_Reparacion-en-Orbita/` |
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
