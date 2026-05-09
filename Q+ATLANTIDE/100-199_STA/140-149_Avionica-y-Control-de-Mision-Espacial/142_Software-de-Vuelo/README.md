---
document_id: QATL-ATLAS-1000-STA-140-149-04-142-README
title: "STA 140-149 · 04.142 — Software de Vuelo (Subsection Index)"
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
subsection: "142"
subsection_title: "Software de Vuelo"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "103_Seguridad-de-Mision"
  - "133_Distribucion-Electrica"
  - "140_GNC-Guiado-Navegacion-y-Control"
  - "141_Avionica-Espacial"
  - "143_Control-de-Mision"
  - "144_Autonomia"
safety_boundary: "mission-software critical; requires explicit requirements traceability, deterministic execution, timing assurance, FDIR validation, safe-mode behavior, simulation/HIL test evidence, configuration control and lifecycle governance"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 140-149 · Section 04 · Subsection 142 — Software de Vuelo

## 1. Purpose

Subsection-level index for *Software de Vuelo* (`142`) within STA `140-149` — *Aviónica y Control de Misión Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **mission-software critical**: all subsubjects require explicit requirements traceability, deterministic execution, timing assurance, FDIR validation, safe-mode behavior, simulation/HIL test evidence, configuration control, and lifecycle governance.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `142` *Flight Software*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `103_Seguridad-de-Mision`, `133_Distribucion-Electrica`, `140_GNC-Guiado-Navegacion-y-Control`, `141_Avionica-Espacial`, `143_Control-de-Mision`, `144_Autonomia`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`142-000-General.md`](./142-000-General.md) | active |
| 010 | Flight Software Controlled Definition | [`142-010-Flight-Software-Controlled-Definition.md`](./142-010-Flight-Software-Controlled-Definition.md) | active |
| 020 | Onboard Software Architecture | [`142-020-Onboard-Software-Architecture.md`](./142-020-Onboard-Software-Architecture.md) | active |
| 030 | Command Telemetry and Data Handling Software | [`142-030-Command-Telemetry-and-Data-Handling-Software.md`](./142-030-Command-Telemetry-and-Data-Handling-Software.md) | active |
| 040 | GNC Software Interfaces and Control Loops | [`142-040-GNC-Software-Interfaces-and-Control-Loops.md`](./142-040-GNC-Software-Interfaces-and-Control-Loops.md) | active |
| 050 | FDIR Fault Detection Isolation and Recovery Logic | [`142-050-FDIR-Fault-Detection-Isolation-and-Recovery-Logic.md`](./142-050-FDIR-Fault-Detection-Isolation-and-Recovery-Logic.md) | active |
| 060 | Safe Mode Contingency and Autonomous Recovery Software | [`142-060-Safe-Mode-Contingency-and-Autonomous-Recovery-Software.md`](./142-060-Safe-Mode-Contingency-and-Autonomous-Recovery-Software.md) | active |
| 070 | Real Time Scheduling Timing and Determinism | [`142-070-Real-Time-Scheduling-Timing-and-Determinism.md`](./142-070-Real-Time-Scheduling-Timing-and-Determinism.md) | active |
| 080 | Verification Validation Simulation and HIL Testing | [`142-080-Verification-Validation-Simulation-and-HIL-Testing.md`](./142-080-Verification-Validation-Simulation-and-HIL-Testing.md) | active |
| 090 | Traceability Evidence and Lifecycle Governance | [`142-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./142-090-Traceability-Evidence-and-Lifecycle-Governance.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `140-149` |
| Section | `04` — Aviónica y Control de Misión Espacial |
| Subsection | `142` — Software de Vuelo |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Safety boundary | mission-software critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/140-149_Avionica-y-Control-de-Mision-Espacial/142_Software-de-Vuelo/` |
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
