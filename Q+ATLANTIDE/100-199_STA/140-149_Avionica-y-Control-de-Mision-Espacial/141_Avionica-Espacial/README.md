---
document_id: QATL-ATLAS-1000-STA-140-149-04-141-README
title: "STA 140-149 · 04.141 — Aviónica Espacial (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "140-149"
section: "04"
section_title: "Aviónica y Control de Misión Espacial"
subsection: "141"
subsection_title: "Aviónica Espacial"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "103_Seguridad-de-Mision"
  - "133_Distribucion-Electrica"
  - "140_GNC-Guiado-Navegacion-y-Control"
  - "142_Software-de-Vuelo"
  - "143_Control-de-Mision"
  - "144_Autonomia"
safety_boundary: "mission-avionics critical; requires explicit redundancy architecture, fault-tolerance evidence, command/telemetry validation, radiation-effect analysis, timing assurance, EMC/power-interface control and lifecycle traceability"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 140-149 · Section 04 · Subsection 141 — Aviónica Espacial

## 1. Purpose

Subsection-level index for *Aviónica Espacial* (`141`) within STA `140-149` — *Aviónica y Control de Misión Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **mission-avionics critical**: all subsubjects require explicit redundancy architecture, fault-tolerance evidence, command/telemetry validation, radiation-effect analysis, timing assurance, EMC/power-interface control, and lifecycle traceability.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `141` *Space Avionics*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `103_Seguridad-de-Mision`, `133_Distribucion-Electrica`, `140_GNC-Guiado-Navegacion-y-Control`, `142_Software-de-Vuelo`, `143_Control-de-Mision`, `144_Autonomia`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](000_Overview.md) | active |
| 001 | Space Avionics Controlled Definition | [`001_Space-Avionics-Controlled-Definition.md`](001_Space-Avionics-Controlled-Definition.md) | active |
| 002 | Onboard Computer and Data Handling Architecture | [`002_Onboard-Computer-and-Data-Handling-Architecture.md`](002_Onboard-Computer-and-Data-Handling-Architecture.md) | active |
| 003 | Command and Telemetry Interfaces | [`003_Command-and-Telemetry-Interfaces.md`](003_Command-and-Telemetry-Interfaces.md) | active |
| 004 | Sensor, Actuator and Payload Avionics Interfaces | [`004_Sensor-Actuator-and-Payload-Avionics-Interfaces.md`](004_Sensor-Actuator-and-Payload-Avionics-Interfaces.md) | active |
| 005 | Time Synchronization and Data Bus Architecture | [`005_Time-Synchronization-and-Data-Bus-Architecture.md`](005_Time-Synchronization-and-Data-Bus-Architecture.md) | active |
| 006 | Redundancy, Fault Tolerance and Safe-Mode Support | [`006_Redundancy-Fault-Tolerance-and-Safe-Mode-Support.md`](006_Redundancy-Fault-Tolerance-and-Safe-Mode-Support.md) | active |
| 007 | Radiation Hardening and Single Event Effects | [`007_Radiation-Hardening-and-Single-Event-Effects.md`](007_Radiation-Hardening-and-Single-Event-Effects.md) | active |
| 008 | EMC, Thermal and Power Interface Boundaries | [`008_EMC-Thermal-and-Power-Interface-Boundaries.md`](008_EMC-Thermal-and-Power-Interface-Boundaries.md) | active |
| 009 | ECSS-NASA-CCSDS Avionics Standards Mapping | [`009_ECSS-NASA-CCSDS-Avionics-Standards-Mapping.md`](009_ECSS-NASA-CCSDS-Avionics-Standards-Mapping.md) | active |
| 010 | Traceability, Evidence and Lifecycle Governance | [`010_Traceability-Evidence-and-Lifecycle-Governance.md`](010_Traceability-Evidence-and-Lifecycle-Governance.md) | active |
| 011–099 | *(reserved)* | — | reserved |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `140-149` |
| Section | `04` — Aviónica y Control de Misión Espacial |
| Subsection | `141` — Aviónica Espacial |
| Subsubject namespace | `000`–`010` active / `011`–`099` reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Safety boundary | mission-avionics critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/140-149_Avionica-y-Control-de-Mision-Espacial/141_Avionica-Espacial/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE`, `support_q_divisions = [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]`, and `governance_class = baseline` from the parent STA section. Extensions added under `011`–`099` shall preserve those header fields, declare the `safety_boundary`, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
