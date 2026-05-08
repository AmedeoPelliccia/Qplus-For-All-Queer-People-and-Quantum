---
document_id: QATL-ATLAS-1000-STA-160-169-06-161-000-OVERVIEW
title: "STA 160-169 · 06.161.000 — Overview"
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
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-MKTG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 160-169 · Section 06 · Subsection 161 — Instrumentación

## 1. Purpose

Overview entry-point for the Instrumentación subsection within `160-169`. Introduces the instrumentation framework: controlled definitions, instrument classes, detector/transducer chains, calibration/metrology, signal conditioning, environmental constraints, interfaces, commissioning/health monitoring, standards mapping, and lifecycle governance. Designated mission-instrumentation critical.

## 2. Scope

- Covers the Instrumentation slice of parent code range `160-169`, establishing what constitutes spacecraft instrumentation in Q+ATLANTIDE STA-band platforms; distinguishes instrument from payload (→`160`) and scientific sensor (→`162`) scopes.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table).
- **Instrumentation Controlled Definition** (`001`) — normative boundary; instrument as a measurement device providing quantified physical observables, per ECSS-E-ST-10-03C testing and metrology conventions.
- **Instrument Classes and Mission Functions** (`002`) — taxonomy: in-situ/remote-sensing, passive/active, imaging/non-imaging; alignment to mission function.
- **Detectors, Transducers and Sensing Chains** (`003`) — detector technologies (photodetectors, bolometers, particle detectors, magnetometers), front-end electronics, analog/digital conversion.
- **Calibration Reference and Metrology Baselines** (`004`) — calibration hierarchy, reference standards, uncertainty budget per BIPM JCGM 100:2008 (GUM).
- **Signal Conditioning, Data Acquisition and Timing** (`005`) — amplifiers, filters, ADC specifications, timing synchronization, data latency.
- **Environmental Constraints: Thermal, Radiation and Vacuum** (`006`) — thermal operating range, total ionizing dose, SEU susceptibility, outgassing, vacuum qualification per NASA-HDBK-4002A and ECSS-E-ST-10-04C.
- **Instrument Interfaces: Power, Data, Thermal and Mechanical** (`007`) — SpaceWire, MIL-STD-1553, power rail specifications, alignment requirements.
- **Commissioning, Operations and Health Monitoring** (`008`) — switch-on sequence, functional verification, in-orbit calibration update, health telemetry.
- **ECSS-NASA-CCSDS Instrumentation Standards Mapping** (`009`) — standards hierarchy for instrumentation design and verification.
- **Traceability, Evidence and Lifecycle Governance** (`010`) — requirements traceability, evidence gates, lifecycle records.

## 3. Diagram — Instrumentation Subsection Map

```mermaid
flowchart TD
    A["161 — Instrumentación\n(STA 160-169 · §06)"]:::entry
    A --> B["001\nControlled Definition"]
    A --> C["002\nInstrument Classes &\nMission Functions"]
    A --> D["003\nDetectors, Transducers\n& Sensing Chains"]
    A --> E["004\nCalibration & Metrology\nBaselines"]
    A --> F["005\nSignal Conditioning,\nData Acquisition & Timing"]
    A --> G["006\nEnvironmental Constraints\n(Thermal / Radiation / Vacuum)"]
    A --> H["007\nInstrument Interfaces\n(Power / Data / Thermal / Mechanical)"]
    A --> I["008\nCommissioning, Operations\n& Health Monitoring"]
    A --> J["009\nECSS-NASA-CCSDS\nStandards Mapping"]
    A --> K["010\nTraceability, Evidence\n& Lifecycle Governance"]:::exit

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
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| ORB support | ORB-PMO, ORB-MKTG |
| Governance class | `baseline`[^gov] |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

| Standard | Title | Applicability |
|---|---|---|
| ECSS-E-ST-10-03C | Space Engineering: Testing | Instrument-level testing and thermal-vacuum qualification |
| ECSS-E-ST-10-04C | Space Engineering: Space Environment | Environmental specifications for instrumentation design |
| BIPM JCGM 100:2008 | GUM — Guide to the Expression of Uncertainty in Measurement | Calibration uncertainty budgets |
| ISO/IEC 17025 | General requirements for the competence of testing and calibration laboratories | Accredited calibration laboratory requirements |
| NASA-HDBK-4002A | Mitigating In-Space Charging Effects — A Guideline | Radiation and charging environment for detectors |
