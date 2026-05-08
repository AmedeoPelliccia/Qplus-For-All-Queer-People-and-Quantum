---
document_id: QATL-ATLAS-1000-STA-160-169-06-160-README
title: "STA 160-169 · 06.160 — Cargas Útiles (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "160-169"
section: "06"
section_title: "Sensores y Carga Útil Espacial"
subsection: "160"
subsection_title: "Cargas Útiles"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-MKTG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "103_Seguridad-de-Mision"
  - "141_Avionica-Espacial"
  - "143_Control-de-Mision"
  - "150_SATCOM"
  - "161_Instrumentacion"
  - "162_Sensores-Cientificos"
  - "163_Observacion"
safety_boundary: "mission-payload critical; requires explicit interface control, power/data/thermal/mechanical compatibility, calibration evidence, operational constraints, commissioning logic, safety classification and lifecycle traceability"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 160-169 · Section 06 · Subsection 160 — Cargas Útiles

## 1. Purpose

Subsection-level index for *Cargas Útiles* (`160`) within STA `160-169` — *Sensores y Carga Útil Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **mission-payload critical**: all subsubjects require explicit interface control, power/data/thermal/mechanical compatibility, calibration evidence, operational constraints, commissioning logic, safety classification, and lifecycle traceability.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `160` *Cargas Útiles / Payloads*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `103_Seguridad-de-Mision`, `141_Avionica-Espacial`, `143_Control-de-Mision`, `150_SATCOM`, `161_Instrumentacion`, `162_Sensores-Cientificos`, `163_Observacion`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](000_Overview.md) | active |
| 001 | Payloads Controlled Definition | [`001_Payloads-Controlled-Definition.md`](001_Payloads-Controlled-Definition.md) | active |
| 002 | Payload Classes and Mission Roles | [`002_Payload-Classes-and-Mission-Roles.md`](002_Payload-Classes-and-Mission-Roles.md) | active |
| 003 | Scientific Payloads and Instruments | [`003_Scientific-Payloads-and-Instruments.md`](003_Scientific-Payloads-and-Instruments.md) | active |
| 004 | Communication Payloads and Relay Functions | [`004_Communication-Payloads-and-Relay-Functions.md`](004_Communication-Payloads-and-Relay-Functions.md) | active |
| 005 | Earth Observation and Remote Sensing Payloads | [`005_Earth-Observation-and-Remote-Sensing-Payloads.md`](005_Earth-Observation-and-Remote-Sensing-Payloads.md) | active |
| 006 | Navigation, Timing and Positioning Payloads | [`006_Navigation-Timing-and-Positioning-Payloads.md`](006_Navigation-Timing-and-Positioning-Payloads.md) | active |
| 007 | Payload Interfaces: Power, Data, Thermal and Mechanical | [`007_Payload-Interfaces-Power-Data-Thermal-and-Mechanical.md`](007_Payload-Interfaces-Power-Data-Thermal-and-Mechanical.md) | active |
| 008 | Payload Operations, Calibration and Commissioning | [`008_Payload-Operations-Calibration-and-Commissioning.md`](008_Payload-Operations-Calibration-and-Commissioning.md) | active |
| 009 | ECSS-NASA-CCSDS Payload Standards Mapping | [`009_ECSS-NASA-CCSDS-Payload-Standards-Mapping.md`](009_ECSS-NASA-CCSDS-Payload-Standards-Mapping.md) | active |
| 010 | Traceability, Evidence and Lifecycle Governance | [`010_Traceability-Evidence-and-Lifecycle-Governance.md`](010_Traceability-Evidence-and-Lifecycle-Governance.md) | active |
| 011–099 | *(reserved)* | — | reserved |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `160-169` |
| Section | `06` — Sensores y Carga Útil Espacial |
| Subsection | `160` — Cargas Útiles |
| Subsubject namespace | `000`–`010` active / `011`–`099` reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-MKTG |
| Governance class | `baseline`[^gov] |
| Safety boundary | mission-payload critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/160-169_Sensores-y-Carga-Util-Espacial/160_Cargas-Utiles/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE`, and `governance_class = baseline` from the parent STA section, and shall use `support_q_divisions = [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]` as declared in this subsection header. Extensions added under `011`–`099` shall preserve those header fields, declare the `safety_boundary`, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
