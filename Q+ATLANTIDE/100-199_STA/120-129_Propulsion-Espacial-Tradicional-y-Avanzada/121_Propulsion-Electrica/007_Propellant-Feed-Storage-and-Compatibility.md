---
document_id: QATL-ATLAS-1000-STA-120-129-02-121-007-PROPELLANT-FEED-STORAGE-AND-COMPATIBILITY
title: "STA 120-129 · 02.121.007 — Propellant Feed, Storage and Compatibility"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "120-129"
section: "02"
subsection: "121"
subsubject: "007"
subsubject_title: "Propellant Feed, Storage and Compatibility"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-HPC, Q-DATAGOV, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · Section 02 · Subsection 121 · Subsubject 007 — Propellant Feed, Storage and Compatibility

## 1. Purpose

Defines **propellant feed system, storage, and compatibility requirements** for electric propulsion on Q+ATLANTIDE STA-band platforms.

## 2. Scope

- **Propellant types** — Xenon (Xe): primary heritage EP propellant, boiling point −108 °C, stored as high-pressure gas (180–300 bar) or supercritical liquid (> 5.84 MPa, > −112 °C); Krypton (Kr): lower cost, comparable performance, higher storage pressure; Iodine (I₂): solid at ambient, sublimated for CubeSat EP; Bismuth (Bi): FEEP thruster propellant.
- **Storage tank** — Composite overwrapped pressure vessel (COPV) or metallic; compatibility with propellant (Xe/SS316L/Al); leak rate < 10⁻⁶ scc/s He-equivalent; burst factor ≥ 2.0 (ECSS-E-ST-35C[^ecssest35]).
- **Flow control** — Flow control valve (latching or proportional); xenon flow controller (XFC) accuracy ±1%; latch valve for isolation; filter (< 5 µm) upstream of thruster.
- **Compatibility** — All wetted materials shall be qualified for propellant contact; elastomers (PTFE, PEEK); seals torque-down specification; propellant contamination limit < 10 ppm for GIT grids.
- **Pressurisation** — Self-pressurising from tank vapour pressure; no separate pressurant needed for xenon; iodine requires dedicated heater system for sublimation.

## 3. Diagram — EP Propellant Feed System

```mermaid
flowchart LR
    A["Xe/Kr COPV Tank<br/>(180-300 bar)"] --> B["Latch Valve<br/>(isolation)"]
    B --> C["XFC<br/>(flow control · ±1%)"]
    C --> D["Filter<br/>(<5µm)"]
    D --> E["Thruster<br/>(GIT/HET/Arcjet)"]
    F["Temp/Press Sensor<br/>(TM)"] --> A
    style A fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `121` — Propulsión Eléctrica |
| Subsubject | `007` — Propellant Feed, Storage and Compatibility |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `007_Propellant-Feed-Storage-and-Compatibility.md` (this file) |

## 5. References & Citations

[^ecssest35]: **ECSS-E-ST-35C — Propulsion General Requirements**.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-35C — Propulsion General Requirements[^ecssest35]
- ECSS-E-ST-35-06C — Liquid and Electric Propulsion for Spacecraft Subsystems
