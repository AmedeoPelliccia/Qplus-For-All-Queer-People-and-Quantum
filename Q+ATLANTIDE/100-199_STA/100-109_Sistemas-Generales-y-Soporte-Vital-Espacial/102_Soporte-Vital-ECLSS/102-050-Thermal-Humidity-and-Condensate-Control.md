---
document_id: QATL-ATLAS-1000-STA-100-109-00-102-050-THERMAL-HUMIDITY-AND-CONDENSATE-CONTROL
title: "STA 100-109 · 102-050 — Thermal Humidity and Condensate Control"
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
subsubject: "050"
subsubject_title: "Thermal Humidity and Condensate Control"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · 102-050 — Thermal Humidity and Condensate Control

## 1. Purpose

Defines the **ECLSS atmospheric thermal and humidity control architecture**, ensuring cabin temperature and relative humidity remain within crew comfort and mould-prevention bounds, and managing condensate collection for return to the water recovery system, per ECSS-E-ST-34C[^ecsse34] and NASA-STD-3001 Vol.2[^nastd3001v2].

## 2. Scope

- Covers the *Thermal, Humidity and Condensate Control* subsubject (`005`) of subsection `102`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Atmosphere Temperature and Humidity Control System (ATCS)** — forced air circulation, inter-module ventilation, heat exchanger design, and cabin temperature control range (18–27 °C per NASA-STD-3001 Vol.2[^nastd3001v2]).
  - **Humidity control** — relative humidity target range 25–75%; condensing heat exchanger (CHX) for humidity removal; dew-point monitoring.
  - **Condensate management** — CHX condensate collection rate (≈ 0.5–1.5 kg/crew-day), gravity-independent collection hardware, and routing to WRS water supply.
  - **Mould and microbial prevention** — surface temperature management to prevent condensation on structural surfaces; swab monitoring cadence.
  - **Ventilation architecture** — inter-rack air distribution, dead-zone elimination, minimum airflow velocity (0.08–0.2 m/s at crew breathing zone).
  - **Interface with habitability** — thermal demands from subsubject `101.003` supply design constraints for ATCS.

## 3. Diagram — Thermal and Humidity Control Loop

```mermaid
flowchart LR
    CABIN["Cabin Air<br/>(T · RH)"]
    CABIN --> FAN["Circulation Fan<br/>(forced air)"]
    FAN --> CHX["Condensing HX<br/>(CHX — humidity removal)"]
    CHX --> COND["Condensate<br/>(→ WRS)"]
    CHX --> HX2["Heating/Cooling HX<br/>(ATCS)"]
    HX2 --> CABIN

    CABIN --> SENSOR["T · RH Sensors<br/>(monitoring)"]
    SENSOR --> AUTO["Autonomy / Control<br/>(144)"]

    style CABIN fill:#2c82c9,color:#fff
    style COND fill:#3498db,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `102` — Soporte Vital ECLSS |
| Subsubject | `005` — Thermal Humidity and Condensate Control |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/102_Soporte-Vital-ECLSS/` |
| Document | `102-050-Thermal-Humidity-and-Condensate-Control.md` (this file) |
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
