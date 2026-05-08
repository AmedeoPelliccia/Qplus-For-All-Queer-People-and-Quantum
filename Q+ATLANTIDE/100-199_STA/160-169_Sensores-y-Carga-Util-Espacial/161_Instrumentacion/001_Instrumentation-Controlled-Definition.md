---
document_id: QATL-ATLAS-1000-STA-160-169-06-161-001-INSTRUMENTATION-CONTROLLED-DEFINITION
title: "STA 160-169 · 06.161.001 — Instrumentation Controlled Definition"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "160-169"
section: "06"
section_title: "Sensores y Carga Útil Espacial"
subsection: "161"
subsection_title: "Instrumentación"
subsubject: "001"
subsubject_title: "Instrumentation Controlled Definition"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-MKTG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 160-169 · Section 06 · Subsection 161 · Subsubject 001 — Instrumentation Controlled Definition

## 1. Purpose

Establishes the normative definition and controlled scope of spacecraft instrumentation within the Q+ATLANTIDE STA band, per ECSS-E-ST-10-03C testing and metrology framework. Provides the authoritative vocabulary and applicability boundaries for all downstream subsubjects.

## 2. Scope

- **Controlled definition** — Instrumentation encompasses all sensors, detectors, transducers, and associated electronics that generate quantified physical observables from the spacecraft environment or target, including readout chains, calibration sources, and data formatting functions.
- **Applicability boundary** — STA `161` covers the instrumentation subsystem on Q+ATLANTIDE STA-band platforms; excludes payload accommodation functions (→`160`), on-board software execution environment (→`142`), scientific data analysis (→`162`), and observation mission design (→`163`).
- **Controlled vocabulary** — *instrument*: measurement device with traceable calibration; *detector*: physical element converting signal to electrical output; *transducer*: device converting one physical quantity to another; *sensing chain*: detector through ADC; *noise equivalent power (NEP)*; *noise equivalent temperature difference (NEDT)*; *dynamic range*; *linearity*.
- **Safety classification** — mission-instrumentation critical; instrument malfunction may result in science data loss, false measurements leading to incorrect science conclusions, or collateral damage to spacecraft systems.
- **Interface boundaries** — Instrumentation interfaces with: payloads (160) as hosted instrument suite; avionics (141) for housekeeping; flight software (142) for instrument commanding; scientific sensors (162) for sensor-level characterization; observation (163) for data product definition.

## 3. Diagram — Instrumentation Definition Framework

```mermaid
flowchart TD
    A["Regulatory Anchors\nECSS-E-ST-10-03C · BIPM JCGM 100:2008\nISO/IEC 17025"]:::entry
    A --> B["Controlled Definition\nInstrument = measurement device\nwith traceable calibration"]
    B --> C["Applicability Boundary\nSTA 161 scope vs. 160/142/162/163"]
    B --> D["Controlled Vocabulary\ndetector · transducer · sensing chain\nNEP · NEDT · dynamic range · linearity"]
    B --> E["Safety Classification\nmission-instrumentation critical"]
    C --> F["Subsubjects 002–010\nInstrument Classes · Detectors ·\nCalibration · Signal Conditioning ·\nEnvironment · Interfaces ·\nCommissioning · Standards · Governance"]:::exit
    D --> F
    E --> F

    classDef entry fill:#1f3a93,color:#fff
    classDef exit fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `160-169` |
| Section | `06` — Sensores y Carga Útil Espacial |
| Subsection | `161` — Instrumentación |
| Subsubject | `001` — Instrumentation Controlled Definition |
| Primary Q-Division | Q-SPACE[^qdiv] |
| ORB support | ORB-PMO, ORB-MKTG |
| Governance class | `baseline`[^gov] |
| Document | `001_Instrumentation-Controlled-Definition.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

| Standard | Title | Applicability |
|---|---|---|
| ECSS-E-ST-10-03C | Space Engineering: Testing | Normative testing and metrology framework for instrumentation |
| BIPM JCGM 100:2008 | GUM — Guide to the Expression of Uncertainty in Measurement | Traceable calibration and uncertainty vocabulary |
| ISO/IEC 17025 | General requirements for the competence of testing and calibration laboratories | Calibration laboratory accreditation baseline |
