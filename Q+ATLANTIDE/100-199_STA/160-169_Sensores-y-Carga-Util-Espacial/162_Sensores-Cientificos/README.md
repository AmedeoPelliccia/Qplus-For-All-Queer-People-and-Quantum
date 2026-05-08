---
document_id: QATL-ATLAS-1000-STA-160-169-06-162-README
title: "STA 160-169 · 06.162 — Sensores Científicos (Subsection Index)"
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
subsection: "162"
subsection_title: "Sensores Científicos"
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
  - "161_Instrumentacion"
  - "163_Observacion"
safety_boundary: "mission-science critical; requires explicit measurement objectives, calibration baseline, metrology traceability, uncertainty quantification, data-quality validation, environmental qualification and lifecycle evidence"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 160-169 · Section 06 · Subsection 162 — Sensores Científicos

## 1. Purpose

Subsection-level index for *Sensores Científicos* (`162`) within STA `160-169` — *Sensores y Carga Útil Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **mission-science critical**: all subsubjects require explicit measurement objectives, calibration baseline, metrology traceability, uncertainty quantification, data-quality validation, environmental qualification, and lifecycle evidence.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `162` *Sensores Científicos / Scientific Sensors*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `103_Seguridad-de-Mision`, `141_Avionica-Espacial`, `142_Software-de-Vuelo`, `143_Control-de-Mision`, `160_Cargas-Utiles`, `161_Instrumentacion`, `163_Observacion`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](000_Overview.md) | active |
| 001 | Scientific Sensors Controlled Definition | [`001_Scientific-Sensors-Controlled-Definition.md`](001_Scientific-Sensors-Controlled-Definition.md) | active |
| 002 | Sensor Classes and Scientific Measurement Objectives | [`002_Sensor-Classes-and-Scientific-Measurement-Objectives.md`](002_Sensor-Classes-and-Scientific-Measurement-Objectives.md) | active |
| 003 | Optical, Infrared and Ultraviolet Sensors | [`003_Optical-Infrared-and-Ultraviolet-Sensors.md`](003_Optical-Infrared-and-Ultraviolet-Sensors.md) | active |
| 004 | Radar, Radiofrequency and Microwave Sensors | [`004_Radar-Radiofrequency-and-Microwave-Sensors.md`](004_Radar-Radiofrequency-and-Microwave-Sensors.md) | active |
| 005 | Particle, Field and Plasma Sensors | [`005_Particle-Field-and-Plasma-Sensors.md`](005_Particle-Field-and-Plasma-Sensors.md) | active |
| 006 | Spectrometers, Imagers and Radiometers | [`006_Spectrometers-Imagers-and-Radiometers.md`](006_Spectrometers-Imagers-and-Radiometers.md) | active |
| 007 | Calibration, Metrology and Reference Standards | [`007_Calibration-Metrology-and-Reference-Standards.md`](007_Calibration-Metrology-and-Reference-Standards.md) | active |
| 008 | Data Quality, Uncertainty and Validation | [`008_Data-Quality-Uncertainty-and-Validation.md`](008_Data-Quality-Uncertainty-and-Validation.md) | active |
| 009 | ECSS-NASA-CCSDS Scientific Sensor Standards Mapping | [`009_ECSS-NASA-CCSDS-Scientific-Sensor-Standards-Mapping.md`](009_ECSS-NASA-CCSDS-Scientific-Sensor-Standards-Mapping.md) | active |
| 010 | Traceability, Evidence and Lifecycle Governance | [`010_Traceability-Evidence-and-Lifecycle-Governance.md`](010_Traceability-Evidence-and-Lifecycle-Governance.md) | active |
| 011–099 | *(reserved)* | — | reserved |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `160-169` |
| Section | `06` — Sensores y Carga Útil Espacial |
| Subsection | `162` — Sensores Científicos |
| Subsubject namespace | `000`–`010` active / `011`–`099` reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-MKTG |
| Governance class | `baseline`[^gov] |
| Safety boundary | mission-science critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/160-169_Sensores-y-Carga-Util-Espacial/162_Sensores-Cientificos/` |
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
