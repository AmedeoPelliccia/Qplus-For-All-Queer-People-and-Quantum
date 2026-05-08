---
document_id: QATL-ATLAS-1000-STA-160-169-06-162-002-SENSOR-CLASSES-AND-SCIENTIFIC-MEASUREMENT-OBJECTIVES
title: "STA 160-169 · 06.162.002 — Sensor Classes and Scientific Measurement Objectives"
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
subsection: "162"
subsection_title: "Sensores Científicos"
subsubject: "002"
subsubject_title: "Sensor Classes and Scientific Measurement Objectives"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-MKTG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 160-169 · Section 06 · Subsection 162 · Subsubject 002 — Sensor Classes and Scientific Measurement Objectives

## 1. Purpose

Establishes the taxonomy of scientific sensor classes and maps them to science measurement objectives within Q+ATLANTIDE STA-band spacecraft[^baseline][^n001].

## 2. Scope

- **Primary classification axis** — Electromagnetic (EM) sensors (measuring interaction of EM radiation with target) vs. in-situ sensors (measuring physical properties at sensor location); further sub-classified by spectral band (UV, optical, IR, microwave, radio) or physical quantity (magnetic field, electric field, particle flux, plasma density).
- **Science domain alignment** — Earth science (atmosphere, land, ocean, cryosphere); heliophysics (solar wind, magnetosphere, ionosphere); planetary science (surface composition, geology, atmosphere); astrophysics (stellar/galactic/extragalactic sources); technology demonstration sensors.
- **Measurement objective specification** — each sensor class assigned: primary measurand, measurement spectral/energy range, spatial resolution requirement, temporal resolution requirement, measurement accuracy and uncertainty requirement, and applicable calibration standard.
- **Active vs. passive sensors** — active sensors (radar, lidar, sounder) require transmitter sizing, frequency coordination, and specific interference analyses; passive sensors have simpler RF/optical budget but require strict stray-light and out-of-band rejection control.
- **Single vs. multi-sensor synergy** — multi-sensor measurement strategies (e.g., polarimetric SAR + optical + thermal) for improved geophysical retrieval; sensor synergy requirements imposed as cross-calibration constraints.
- **Heritage vs. novel technologies** — TRL requirements per ECSS-E-HB-10-12A; novel detector technologies (e.g., superconducting sensors, quantum sensors) require additional qualification margins.

## 3. Diagram — Sensor Class Map

```mermaid
flowchart TD
    A["Scientific Sensor\n(001 Controlled Definition)"]:::start
    B["EM Sensors\n(remote sensing)"]
    C["In-Situ Sensors\n(at platform location)"]
    D["Optical / IR / UV\n(→003)"]
    E["Radar / RF / Microwave\n(→004)"]
    F["Particle Sensors\n(→005)"]
    G["Field & Plasma Sensors\n(→005)"]
    H["Spectrometers / Imagers\n/ Radiometers (→006)"]
    I["Earth Science\natmosphere · ocean · land · cryo"]
    J["Heliophysics\nsolar wind · magnetosphere"]
    K["Planetary Science\nsurface · atmosphere"]
    L["Measurement Objectives\n& Calibration Standards"]:::end_node

    A --> B
    A --> C
    B --> D
    B --> E
    B --> H
    C --> F
    C --> G
    D --> I
    E --> I
    H --> I
    F --> J
    G --> J
    D --> K
    I --> L
    J --> L
    K --> L

    classDef start fill:#1f3a93,color:#fff
    classDef end_node fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `160-169` |
| Section | `06` — Sensores y Carga Útil Espacial |
| Subsection | `162` — Sensores Científicos |
| Subsubject | `002` — Sensor Classes and Scientific Measurement Objectives |
| Primary Q-Division | Q-SPACE[^qdiv] |
| ORB support | ORB-PMO, ORB-MKTG |
| Governance class | `baseline`[^gov] |
| Document | `002_Sensor-Classes-and-Scientific-Measurement-Objectives.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

[^n001]: **Note N-001** — Q+ATLANTIDE is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

### Applicable industry standards

- ECSS-E-ST-10C — Space engineering — System engineering general requirements
- ECSS-E-ST-10-03C — Testing
- ECSS-E-HB-10-12A — Radiation Effects Handbook
- CEOS Cal/Val — Committee on Earth Observation Satellites Calibration and Validation protocols
