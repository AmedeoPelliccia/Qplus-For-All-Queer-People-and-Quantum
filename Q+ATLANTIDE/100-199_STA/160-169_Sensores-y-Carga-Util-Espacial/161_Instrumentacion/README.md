---
document_id: QATL-ATLAS-1000-STA-160-169-06-161-README
title: "STA 160-169 · 06.161 — Instrumentación (Subsection Index)"
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
subsection: "161"
subsection_title: "Instrumentación"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-MKTG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "103_Seguridad-de-Mision"
  - "141_Avionica-Espacial"
  - "142_Software-de-Vuelo"
  - "143_Control-de-Mision"
  - "160_Cargas-Utiles"
  - "162_Sensores-Cientificos"
  - "163_Observacion"
safety_boundary: "mission-instrumentation critical; requires explicit calibration baseline, metrology traceability, detector/signal-chain validation, timing assurance, environmental qualification, interface control and lifecycle evidence"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 160-169 · Section 06 · Subsection 161 — Instrumentación

## 1. Purpose

Subsection-level index for *Instrumentación* (`161`) within STA `160-169` — *Sensores y Carga Útil Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **mission-instrumentation critical**: all subsubjects require explicit calibration baseline, metrology traceability, detector/signal-chain validation, timing assurance, environmental qualification, interface control, and lifecycle evidence.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `161` *Instrumentación / Instrumentation*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `103_Seguridad-de-Mision`, `141_Avionica-Espacial`, `142_Software-de-Vuelo`, `143_Control-de-Mision`, `160_Cargas-Utiles`, `162_Sensores-Cientificos`, `163_Observacion`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`161-000-General.md`](./161-000-General.md) | active |
| 010 | Instrumentation Controlled Definition | [`161-010-Instrumentation-Controlled-Definition.md`](./161-010-Instrumentation-Controlled-Definition.md) | active |
| 020 | Instrument Classes and Mission Functions | [`161-020-Instrument-Classes-and-Mission-Functions.md`](./161-020-Instrument-Classes-and-Mission-Functions.md) | active |
| 030 | Detectors Transducers and Sensing Chains | [`161-030-Detectors-Transducers-and-Sensing-Chains.md`](./161-030-Detectors-Transducers-and-Sensing-Chains.md) | active |
| 040 | Calibration Reference and Metrology Baselines | [`161-040-Calibration-Reference-and-Metrology-Baselines.md`](./161-040-Calibration-Reference-and-Metrology-Baselines.md) | active |
| 050 | Signal Conditioning Data Acquisition and Timing | [`161-050-Signal-Conditioning-Data-Acquisition-and-Timing.md`](./161-050-Signal-Conditioning-Data-Acquisition-and-Timing.md) | active |
| 060 | Environmental Constraints Thermal Radiation and Vacuum | [`161-060-Environmental-Constraints-Thermal-Radiation-and-Vacuum.md`](./161-060-Environmental-Constraints-Thermal-Radiation-and-Vacuum.md) | active |
| 070 | Instrument Interfaces Power Data Thermal and Mechanical | [`161-070-Instrument-Interfaces-Power-Data-Thermal-and-Mechanical.md`](./161-070-Instrument-Interfaces-Power-Data-Thermal-and-Mechanical.md) | active |
| 080 | Commissioning Operations and Health Monitoring | [`161-080-Commissioning-Operations-and-Health-Monitoring.md`](./161-080-Commissioning-Operations-and-Health-Monitoring.md) | active |
| 090 | Traceability Evidence and Lifecycle Governance | [`161-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./161-090-Traceability-Evidence-and-Lifecycle-Governance.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `160-169` |
| Section | `06` — Sensores y Carga Útil Espacial |
| Subsection | `161` — Instrumentación |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-MKTG |
| Governance class | `baseline`[^gov] |
| Safety boundary | mission-instrumentation critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/160-169_Sensores-y-Carga-Util-Espacial/161_Instrumentacion/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE`, and `governance_class = baseline` from the parent STA section. The `support_q_divisions` value for this subsection is declared in this document as `support_q_divisions = [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]`; extensions added under `011`–`099` shall preserve that header field, declare the `safety_boundary`, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
