---
document_id: QATL-ATLAS-1000-STA-140-149-04-143-README
title: "STA 140-149 · 04.143 — Control de Misión (Subsection Index)"
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
subsection: "143"
subsection_title: "Control de Misión"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "103_Seguridad-de-Mision"
  - "140_GNC-Guiado-Navegacion-y-Control"
  - "141_Avionica-Espacial"
  - "142_Software-de-Vuelo"
  - "144_Autonomia"
  - "150_SATCOM"
  - "152_Redes-Espaciales"
safety_boundary: "mission-operations critical; requires explicit command authority, uplink validation, telemetry monitoring, anomaly escalation, flight-rule governance, simulation/rehearsal evidence, operational readiness gates and lifecycle traceability"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 140-149 · Section 04 · Subsection 143 — Control de Misión

## 1. Purpose

Subsection-level index for *Control de Misión* (`143`) within STA `140-149` — *Aviónica y Control de Misión Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **mission-operations critical**: all subsubjects require explicit command authority, uplink validation, telemetry monitoring, anomaly escalation, flight-rule governance, simulation/rehearsal evidence, operational readiness gates, and lifecycle traceability.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `143` *Mission Control*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `103_Seguridad-de-Mision`, `140_GNC-Guiado-Navegacion-y-Control`, `141_Avionica-Espacial`, `142_Software-de-Vuelo`, `144_Autonomia`, `150_SATCOM`, `152_Redes-Espaciales`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`143-000-General.md`](./143-000-General.md) | active |
| 010 | Mission Control Controlled Definition | [`143-010-Mission-Control-Controlled-Definition.md`](./143-010-Mission-Control-Controlled-Definition.md) | active |
| 020 | Ground Segment and Control Centre Architecture | [`143-020-Ground-Segment-and-Control-Centre-Architecture.md`](./143-020-Ground-Segment-and-Control-Centre-Architecture.md) | active |
| 030 | Command Planning Validation and Uplink Control | [`143-030-Command-Planning-Validation-and-Uplink-Control.md`](./143-030-Command-Planning-Validation-and-Uplink-Control.md) | active |
| 040 | Telemetry Reception Monitoring and Trending | [`143-040-Telemetry-Reception-Monitoring-and-Trending.md`](./143-040-Telemetry-Reception-Monitoring-and-Trending.md) | active |
| 050 | Operations Procedures Timelines and Flight Rules | [`143-050-Operations-Procedures-Timelines-and-Flight-Rules.md`](./143-050-Operations-Procedures-Timelines-and-Flight-Rules.md) | active |
| 060 | Anomaly Response Escalation and Contingency Control | [`143-060-Anomaly-Response-Escalation-and-Contingency-Control.md`](./143-060-Anomaly-Response-Escalation-and-Contingency-Control.md) | active |
| 070 | Mission Operations Roles Authority and Handover | [`143-070-Mission-Operations-Roles-Authority-and-Handover.md`](./143-070-Mission-Operations-Roles-Authority-and-Handover.md) | active |
| 080 | Simulation Rehearsal and Operational Readiness Testing | [`143-080-Simulation-Rehearsal-and-Operational-Readiness-Testing.md`](./143-080-Simulation-Rehearsal-and-Operational-Readiness-Testing.md) | active |
| 090 | Traceability Evidence and Lifecycle Governance | [`143-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./143-090-Traceability-Evidence-and-Lifecycle-Governance.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `140-149` |
| Section | `04` — Aviónica y Control de Misión Espacial |
| Subsection | `143` — Control de Misión |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Safety boundary | mission-operations critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/140-149_Avionica-y-Control-de-Mision-Espacial/143_Control-de-Mision/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE`, `support_q_divisions = [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR]`, and `governance_class = baseline` from the parent STA section. Extensions added under `011`–`099` shall preserve those header fields, declare the `safety_boundary`, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
