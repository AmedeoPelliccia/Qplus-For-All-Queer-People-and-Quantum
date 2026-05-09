---
document_id: QATL-ATLAS-1000-STA-160-169-06-161-020-INSTRUMENT-CLASSES-AND-MISSION-FUNCTIONS
title: "STA 160-169 · 161-020 — Instrument Classes and Mission Functions"
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
subsubject: "020"
subsubject_title: "Instrument Classes and Mission Functions"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-MKTG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 160-169 · 161-020 — Instrument Classes and Mission Functions

## 1. Purpose

Establishes the taxonomy of spacecraft instrument classes and their associated mission functions within Q+ATLANTIDE STA-band spacecraft. Provides the classification framework used across all downstream instrumentation design and verification activities.

## 2. Scope

- **Classification axes** — instruments classified by measurement principle (in-situ vs. remote-sensing), by actuation (passive vs. active), by output type (imaging vs. spectrometric vs. radiometric vs. in-situ particle/field), and by science domain (heliophysics, planetary, astrophysics, Earth observation, technology demonstration).
- **In-situ instruments** — magnetometers, plasma analyzers, particle detectors, mass spectrometers; measure physical quantities at spacecraft location; interface directly with local environment.
- **Remote-sensing instruments** — optical cameras, spectrometers, SAR, radiometers, lidar; measure physical quantities at a distance; require precise pointing knowledge from GNC (→`140`) and stable platform.
- **Active vs. passive distinction** — active instruments (radar, lidar, active sounder) transmit a signal and receive the return; require dedicated transmitter power budgets, frequency coordination, and EMC analysis; passive instruments rely solely on received natural radiation.
- **Mission function mapping** — each instrument class mapped to mission objective category (science return, navigation support, technology readiness, Earth observation) with primary interface node identification (`160`, `162`, `163`).
- **Accommodation constraints** — field-of-view requirements, pointing stability allocations, thermal stability windows, mass and power budgets per instrument class.

## 3. Diagram — Instrument Class Taxonomy

```mermaid
flowchart TD
    A["Spacecraft Instrumentation\nSTA 161"]:::entry
    A --> B["Measurement Principle"]
    A --> C["Actuation Type"]
    A --> D["Output Type"]
    A --> E["Science Domain"]
    B --> B1["In-Situ\n(magnetometer, plasma, particle,\nmass spectrometer)"]
    B --> B2["Remote-Sensing\n(camera, spectrometer, SAR,\nradiometer, lidar)"]
    C --> C1["Passive\n(receives natural radiation)"]
    C --> C2["Active\n(transmits signal, receives return;\npower/EMC budget required)"]
    D --> D1["Imaging · Spectrometric\nRadiometric · Particle/Field"]
    E --> E1["Heliophysics · Planetary\nAstrophysics · Earth Obs\nTech Demo"]
    B1 & B2 & C1 & C2 & D1 & E1 --> F["Mission Function Mapping\n→ 160 Payloads · 162 Scientific Sensors\n163 Observation"]:::exit

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
| Subsubject | `002` — Instrument Classes and Mission Functions |
| Primary Q-Division | Q-SPACE[^qdiv] |
| ORB support | ORB-PMO, ORB-MKTG |
| Governance class | `baseline`[^gov] |
| Document | `161-020-Instrument-Classes-and-Mission-Functions.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`161-000-General.md`](./161-000-General.md) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

| Standard | Title | Applicability |
|---|---|---|
| ECSS-E-ST-10C | Space Engineering: System Engineering General Requirements | System-level instrument taxonomy and mission function classification |
| ECSS-E-ST-10-03C | Space Engineering: Testing | Testing requirements by instrument class |
