---
document_id: QATL-ATLAS-1000-STA-100-109-00-105-050-LEAK-DETECTION-AND-SEAL-INTEGRITY
title: "STA 100-109 · 105-050 — Leak Detection and Seal Integrity"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "100-109"
section: "00"
section_title: "Sistemas Generales y Soporte Vital Espacial"
subsection: "105"
subsection_title: "Presurización y Atmósfera Interna"
subsubject: "050"
subsubject_title: "Leak Detection and Seal Integrity"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 105-050 — Leak Detection and Seal Integrity

## 1. Purpose

Defines the **leak detection and seal integrity** architecture for Q+ATLANTIDE crewed modules, specifying leak rate requirements, detection methods, seal inspection protocols, and micro-meteoroid impact response per ECSS-E-ST-34C[^ecsse34] and NASA-STD-5019[^nasastd5019].

The cabin structure must maintain a leak rate < 0.05 % of pressurised volume per day (equivalent to < 0.05 kg/day for a 100 m³ module at 101.3 kPa). Leak detection uses: (1) pressure decay monitoring — continuous trend analysis of cabin pressure at ≤ 1 min intervals; (2) trace gas detection — mass spectrometer or helium tracer for pinhole leak localisation; (3) ultrasonic acoustic leak detectors; (4) visual seal inspection procedures. Seal materials: silicone or fluorosilicone O-rings (Class S per MIL-PRF-83461) for hatch seals; metallic C-seals for crew equipment interfaces. All primary seals are backed by a secondary seal with a seal inspection port.

## 2. Scope

- Covers the *Leak Detection and Seal Integrity* subsubject (`050`) of subsection `105`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All design decisions traceable to source standards and CSDB evidence per subsection `109`.

## 3. Diagram — Leak Detection and Seal Integrity

```mermaid
flowchart TB
    CABIN["Pressurised Volume<br/>(pressure trend monitoring)"]
    CABIN --> PRESS_TREND["Pressure Decay Monitor<br/>(ΔP/Δt < threshold)"]
    CABIN --> TRACE["Trace Gas Detector<br/>(mass spectrometer / He tracer)"]
    CABIN --> ULTRASONIC["Ultrasonic Acoustic Detector<br/>(pinhole localisation)"]
    PRESS_TREND & TRACE & ULTRASONIC --> ALARM["Leak Alarm<br/>(C&W — localise and isolate)"]
    ALARM --> ISOLATE["Module Isolation<br/>(hatch closure · MMOD response)"]
    style ALARM fill:#e74c3c,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `105` — Presurización y Atmósfera Interna |
| Subsubject | `050` — Leak Detection and Seal Integrity |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/105_Presurizacion-y-Atmosfera-Interna/` |
| Document | `105-050-Leak-Detection-and-Seal-Integrity.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`105-000-General.md`](./105-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management.

[^ecsse34]: **ECSS-E-ST-34C Rev.1 — Space Engineering: Environmental Control and Life Support** — Primary standard for pressurization design, cabin atmosphere, and leak detection requirements.

[^nastd3001]: **NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health** — Cabin pressure and atmospheric composition requirements for crew health.

[^nasajsc]: **NASA/JSC-65591 — ECLSS Design and Performance Requirements** — Pressurization system design reference for ISS-class crewed modules.

[^iso20521]: **ISO 20521 — Space Systems: Human Spaceflight** — Crew habitability and pressurization requirements for crewed spacecraft.

### Applicable industry standards

- ECSS-E-ST-34C Rev.1 — Space Engineering: Environmental Control and Life Support[^ecsse34]
- NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health[^nastd3001]
- NASA/JSC-65591 — ECLSS Design and Performance Requirements[^nasajsc]
- ISO 20521 — Space Systems: Human Spaceflight[^iso20521]
