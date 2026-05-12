---
document_id: QATL-ATLAS-1000-STA-100-109-00-105-030-ATMOSPHERIC-COMPOSITION-AND-PARTIAL-PRESSURES
title: "STA 100-109 · 105-030 — Atmospheric Composition and Partial Pressures"
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
subsubject: "030"
subsubject_title: "Atmospheric Composition and Partial Pressures"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 105-030 — Atmospheric Composition and Partial Pressures

## 1. Purpose

Defines the **atmospheric composition requirements** for Q+ATLANTIDE crewed module cabins, specifying oxygen and nitrogen partial pressures, CO₂ limits, trace gas concentrations, and spacecraft maximum allowable concentrations (SMACs) per NASA-STD-3001[^nastd3001] and ECSS-E-ST-34C[^ecsse34].

The nominal cabin atmosphere is a nitrogen-oxygen mix: ppO₂ = 21.4 kPa (160 mmHg), ppN₂ = 79.9 kPa; total pressure 101.3 kPa. Oxygen partial pressure must remain between 19.5 kPa (hypoxia floor) and 23.1 kPa (flammability ceiling). CO₂ partial pressure must remain < 0.70 kPa (7 mmHg) for continuous crew operations and < 1.01 kPa for emergency operations. The atmosphere composition is actively controlled by the ECLSS oxygen generation assembly (OGA) and CO₂ removal assembly (CDRA).

## 2. Scope

- Covers the *Atmospheric Composition and Partial Pressures* subsubject (`030`) of subsection `105`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All design decisions traceable to source standards and CSDB evidence per subsection `109`.

## 3. Diagram — Atmospheric Composition and Partial Pressures

```mermaid
flowchart TB
    OGA["O₂ Generation Assembly<br/>(OGA — ECLSS 102)"] --> CABIN["Cabin Atmosphere<br/>ppO₂ 19.5–23.1 kPa<br/>ppCO₂ < 0.70 kPa"]
    CDRA["CO₂ Removal Assembly<br/>(CDRA — ECLSS 102)"] --> CABIN
    N2["N₂ Supply<br/>(makeup gas)"] --> CABIN
    CABIN --> SMAC["SMAC Monitor<br/>(trace contaminants)"]
    CABIN --> ALARM["C&W if ppO₂ or ppCO₂<br/>out of limits"]
    style CABIN fill:#eaf3fb,stroke:#2c82c9
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
| Subsubject | `030` — Atmospheric Composition and Partial Pressures |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/105_Presurizacion-y-Atmosfera-Interna/` |
| Document | `105-030-Atmospheric-Composition-and-Partial-Pressures.md` (this file) |
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
