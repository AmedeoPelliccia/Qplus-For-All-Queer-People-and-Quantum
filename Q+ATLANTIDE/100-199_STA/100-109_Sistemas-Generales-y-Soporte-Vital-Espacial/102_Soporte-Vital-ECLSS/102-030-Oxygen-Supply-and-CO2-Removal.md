---
document_id: QATL-ATLAS-1000-STA-100-109-00-102-030-OXYGEN-SUPPLY-AND-CO2-REMOVAL
title: "STA 100-109 · 102-030 — Oxygen Supply and CO2 Removal"
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
subsection: "102"
subsection_title: "Soporte Vital ECLSS"
subsubject: "030"
subsubject_title: "Oxygen Supply and CO2 Removal"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · 102-030 — Oxygen Supply and CO2 Removal

## 1. Purpose

Defines the **detailed design requirements and subsystem architecture** for oxygen supply and CO₂ removal — the two critical ECLSS subsystem pairs maintaining crew respiratory gas quality — per ECSS-E-ST-34C[^ecsse34] and NASA/JSC-65591[^nasajsc].

## 2. Scope

- Covers the *Oxygen Supply and CO₂ Removal* subsubject (`003`) of subsection `102`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **O₂ supply modes** — primary (OGA electrolysis), secondary (stored high-pressure O₂ tanks), and emergency (SFOG canisters) with automatic mode-switching logic.
  - **OGA performance** — O₂ generation rate (≥ 0.84 kg/crew-day), power consumption, and deionised water feed requirements.
  - **CDRA design** — two-bed/four-bed zeolite sorbent configuration, adsorption/desorption cycling, CO₂ partial-pressure control accuracy (± 0.02 kPa), and power budget.
  - **Sabatier CO₂ reduction** — catalytic Sabatier reaction (CO₂ + 4H₂ → CH₄ + 2H₂O), hydrogen supply from OGA, methane venting or storage policy, and water reclaim to WRS.
  - **LiOH backup** — lithium hydroxide canister sizing for emergency CO₂ removal (24-hour safe-haven), integration with `102.008` emergency modes.
  - **Redundancy and FDIR** — dual-string architecture, failure mode effects analysis (FMEA), and on-board autonomy interfaces (`144_Autonomia`).

## 3. Diagram — O₂/CO₂ Subsystem Architecture

```mermaid
flowchart TB
    O2MODES["O₂ Supply Modes"]
    O2MODES --> OGA["OGA (primary)<br/>electrolysis"]
    O2MODES --> TANK["High-P O₂ tanks<br/>(secondary)"]
    O2MODES --> SFOG["SFOG canisters<br/>(emergency)"]

    CO2MODES["CO₂ Removal Modes"]
    CO2MODES --> CDRA["CDRA (primary)<br/>zeolite 4-bed"]
    CO2MODES --> SAB["Sabatier<br/>(reduction)"]
    CO2MODES --> LIOH["LiOH canisters<br/>(backup 24 h)"]

    OGA --> CABIN["Cabin<br/>Atmosphere"]
    CABIN --> CDRA
    CDRA --> SAB
    SAB --> WRS["WRS<br/>(water reclaim)"]
    WRS --> OGA

    style CABIN fill:#2c82c9,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `102` — Soporte Vital ECLSS |
| Subsubject | `003` — Oxygen Supply and CO2 Removal |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/102_Soporte-Vital-ECLSS/` |
| Document | `102-030-Oxygen-Supply-and-CO2-Removal.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`102-000-General.md`](./102-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `100-109` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ecsse34]: **ECSS-E-ST-34C Rev.1 — Space Engineering: Environmental Control and Life Support** — European standard for ECLSS design, subsystem interfaces, and test criteria.

[^nasajsc]: **NASA/JSC-65591 — ECLSS Design and Performance Requirements** — NASA design specification for ISS-class ECLSS subsystems, used as the baseline engineering reference.

[^nastd3001v2]: **NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health** — Atmosphere and water quality requirements that ECLSS must satisfy.

[^iso14644]: **ISO 14644-1:2015 — Cleanrooms and Associated Controlled Environments** — Applied to atmosphere quality monitoring and contamination control requirements.

[^nasacp]: **NASA/CP-2008-214304 — ECLSS Development and Testing** — ECLSS hardware development and qualification test reference covering all subsystems.

### Applicable industry standards

- ECSS-E-ST-34C Rev.1 — Space Engineering: Environmental Control and Life Support[^ecsse34]
- NASA/JSC-65591 — ECLSS Design and Performance Requirements[^nasajsc]
- NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health[^nastd3001v2]
- ISO 14644-1:2015 — Cleanrooms and Associated Controlled Environments[^iso14644]
- NASA/CP-2008-214304 — ECLSS Development and Testing[^nasacp]
