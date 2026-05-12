---
document_id: QATL-ATLAS-1000-STA-100-109-00-105-020-CABIN-PRESSURE-REGULATION-AND-ALTITUDE-PROFILE
title: "STA 100-109 · 105-020 — Cabin Pressure Regulation and Altitude Profile"
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
subsubject: "020"
subsubject_title: "Cabin Pressure Regulation and Altitude Profile"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 105-020 — Cabin Pressure Regulation and Altitude Profile

## 1. Purpose

Defines the **cabin pressure regulation architecture** and equivalent altitude pressure profile for Q+ATLANTIDE crewed modules, specifying nominal pressure setpoints, pressurization and depressurization rates, and altitude equivalent limits per NASA-STD-3001[^nastd3001].

The nominal cabin total pressure is 101.3 kPa (sea level equivalent) for standard operations, with an alternative 70.3 kPa (approximately 3000 m altitude equivalent) for EVA preparation phases to reduce pre-breathe duration. Pressurization rate during ascent must not exceed 18 hPa/min to prevent crew barotrauma. Depressurization for EVA pre-breathe follows a staged 4-hour protocol (Stage 1: 101.3→70.3 kPa over 30 min; Stage 2: hold 70.3 kPa for 30 min; Stage 3: O₂ pre-breathe exercise protocol).

## 2. Scope

- Covers the *Cabin Pressure Regulation and Altitude Profile* subsubject (`020`) of subsection `105`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All design decisions traceable to source standards and CSDB evidence per subsection `109`.

## 3. Diagram — Cabin Pressure Regulation and Altitude Profile

```mermaid
flowchart LR
    LAUNCH["Launch 101.3 kPa<br/>(sea level)"] --> ORBIT["On-orbit Nominal<br/>101.3 kPa (760 mmHg)"]
    ORBIT --> EVA_PREP["EVA Prep<br/>70.3 kPa (10.2 psi)<br/>(staged depress 30 min)"]
    EVA_PREP --> EVA["EVA Suit<br/>29.6 kPa (4.3 psi)"]
    EVA --> REPRESS["Re-pressurisation<br/>70.3 → 101.3 kPa"]
    style EVA fill:#e74c3c,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `105` — Presurización y Atmósfera Interna |
| Subsubject | `020` — Cabin Pressure Regulation and Altitude Profile |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/105_Presurizacion-y-Atmosfera-Interna/` |
| Document | `105-020-Cabin-Pressure-Regulation-and-Altitude-Profile.md` (this file) |
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
