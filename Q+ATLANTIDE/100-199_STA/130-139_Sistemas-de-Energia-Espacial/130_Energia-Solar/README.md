---
document_id: QATL-ATLAS-1000-STA-130-139-03-130-README
title: "STA 130-139 · 03.130 — Energía Solar (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "130-139"
section: "03"
section_title: "Sistemas de Energía Espacial"
subsection: "130"
subsection_title: "Energía Solar"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "103_Seguridad-de-Mision"
  - "112_Proteccion-Termica-y-Radiacion"
  - "121_Propulsion-Electrica"
  - "131_Baterias-y-Almacenamiento"
  - "133_Distribucion-Electrica"
safety_boundary: "mission-energy critical; requires explicit power-budget analysis, eclipse-case verification, solar-array degradation modelling, deployment assurance, thermal/radiation evidence and lifecycle traceability"
governance_class: baseline
version: 1.0.0
status: active
language: en
no_aaa_rule: true
---

# STA 130-139 · Section 03 · Subsection 130 — Energía Solar

## 1. Purpose

Subsection-level index for *Energía Solar* (`130`) within STA `130-139` — *Sistemas de Energía Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **mission-energy critical**: all subsubjects require explicit power-budget analysis, eclipse-case verification, solar-array degradation modelling, deployment assurance, thermal/radiation evidence, and lifecycle traceability.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `130` *Solar Energy*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `103_Seguridad-de-Mision`, `112_Proteccion-Termica-y-Radiacion`, `121_Propulsion-Electrica`, `131_Baterias-y-Almacenamiento`, `133_Distribucion-Electrica`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`130-000-General.md`](./130-000-General.md) | active |
| 010 | Solar Energy Controlled Definition | [`130-010-Solar-Energy-Controlled-Definition.md`](./130-010-Solar-Energy-Controlled-Definition.md) | active |
| 020 | Photovoltaic Array Architectures | [`130-020-Photovoltaic-Array-Architectures.md`](./130-020-Photovoltaic-Array-Architectures.md) | active |
| 030 | Solar Cell Technologies and Efficiency Classes | [`130-030-Solar-Cell-Technologies-and-Efficiency-Classes.md`](./130-030-Solar-Cell-Technologies-and-Efficiency-Classes.md) | active |
| 040 | Deployable Panels Wings and Structural Interfaces | [`130-040-Deployable-Panels-Wings-and-Structural-Interfaces.md`](./130-040-Deployable-Panels-Wings-and-Structural-Interfaces.md) | active |
| 050 | Sun Pointing Tracking and Attitude Constraints | [`130-050-Sun-Pointing-Tracking-and-Attitude-Constraints.md`](./130-050-Sun-Pointing-Tracking-and-Attitude-Constraints.md) | active |
| 060 | Power Conversion Regulation and MPPT | [`130-060-Power-Conversion-Regulation-and-MPPT.md`](./130-060-Power-Conversion-Regulation-and-MPPT.md) | active |
| 070 | Degradation Radiation and Thermal Cycling Effects | [`130-070-Degradation-Radiation-and-Thermal-Cycling-Effects.md`](./130-070-Degradation-Radiation-and-Thermal-Cycling-Effects.md) | active |
| 080 | Eclipse Operations and Energy Budgeting | [`130-080-Eclipse-Operations-and-Energy-Budgeting.md`](./130-080-Eclipse-Operations-and-Energy-Budgeting.md) | active |
| 090 | Traceability Evidence and Lifecycle Governance | [`130-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./130-090-Traceability-Evidence-and-Lifecycle-Governance.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `130-139` |
| Section | `03` — Sistemas de Energía Espacial |
| Subsection | `130` — Energía Solar |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Safety boundary | mission-energy critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/130-139_Sistemas-de-Energia-Espacial/130_Energia-Solar/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE`, `support_q_divisions = [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]`, and `governance_class = baseline` from the parent STA section. Extensions added under `011`–`099` shall preserve those header fields, declare the `safety_boundary`, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
