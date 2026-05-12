---
document_id: QATL-ATLAS-1000-STA-100-109-00-105-010-PRESSURIZATION-CONTROLLED-DEFINITION
title: "STA 100-109 · 105-010 — Pressurization Controlled Definition"
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
subsubject: "010"
subsubject_title: "Pressurization Controlled Definition"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 105-010 — Pressurization Controlled Definition

## 1. Purpose

Establishes the **controlled normative definition** of the Pressurization and Internal Atmosphere Subsystem for all Q+ATLANTIDE crewed modules, fixing the controlled vocabulary, acronym registry, and scope boundaries per ECSS-E-ST-34C[^ecsse34].

The Pressurization Subsystem is defined as the ensemble of hardware, software, and procedures that maintain cabin total pressure, atmospheric composition, and gas supply within crew survivability and performance limits. Key terms: **PCS** (Pressure Control Subsystem), **ppO₂** (partial pressure of oxygen, 19.5–23.1 kPa), **ppCO₂** (partial pressure of CO₂, < 0.70 kPa operational), **TCPS** (Total Cabin Pressure Subsystem), **EVA** (Extravehicular Activity), **pre-breathe** (N₂ washout protocol), **total pressure** (70.3–104.1 kPa), **leak rate** (< 0.05 % cabin volume per day).

## 2. Scope

- Covers the *Pressurization Controlled Definition* subsubject (`010`) of subsection `105`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All design decisions traceable to source standards and CSDB evidence per subsection `109`.

## 3. Diagram — Pressurization Controlled Definition

```mermaid
flowchart LR
    subgraph PCS["Pressurization Control Subsystem"]
        REG["Pressure Regulator"]
        OFV["Outflow Valve"]
        PRV["Pressure Relief Valve"]
    end
    GAS["Gas Supply<br/>(O₂ / N₂)"] --> REG
    REG --> CABIN["Cabin Volume<br/>(70.3–104.1 kPa)"]
    CABIN --> OFV
    CABIN --> PRV
    style PCS fill:#eaf3fb,stroke:#2c82c9
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `105` — Presurización y Atmósfera Interna |
| Subsubject | `010` — Pressurization Controlled Definition |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/105_Presurizacion-y-Atmosfera-Interna/` |
| Document | `105-010-Pressurization-Controlled-Definition.md` (this file) |
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
