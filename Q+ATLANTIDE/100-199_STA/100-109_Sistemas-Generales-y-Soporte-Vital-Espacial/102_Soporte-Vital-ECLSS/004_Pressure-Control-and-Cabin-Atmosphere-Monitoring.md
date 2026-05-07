---
document_id: QATL-ATLAS-1000-STA-100-109-00-102-004-PRESSURE-CONTROL-AND-CABIN-ATMOSPHERE-MONITORING
title: "STA 100-109 · 00.102.004 — Pressure Control and Cabin Atmosphere Monitoring"
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
subsubject: "004"
subsubject_title: "Pressure Control and Cabin Atmosphere Monitoring"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · Section 00 · Subsection 102 · Subsubject 004 — Pressure Control and Cabin Atmosphere Monitoring

## 1. Purpose

Defines the **pressure control architecture and cabin atmosphere monitoring network** for crewed space habitats, ensuring structural pressure integrity and real-time atmosphere quality awareness, per ECSS-E-ST-34C[^ecsse34].

## 2. Scope

- Covers the *Pressure Control and Cabin Atmosphere Monitoring* subsubject (`004`) of subsection `102`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Pressure control system** — pressure regulator valves, pressure equalisation ducts between modules, inter-hatch pressure equalisation, and vent/relief valve sizing.
  - **Leak detection** — cabin pressure decay monitoring (Δp/Δt ≤ 0.01 kPa/hr normal operations), small-leak detection algorithms, and acoustic/ultrasonic sensor integration.
  - **Atmosphere monitoring sensors** — O₂ partial-pressure sensors, CO₂ sensors (CDMS — Compound Specific Analyzer), total pressure gauges, humidity sensors, and temperature sensors; calibration cadence.
  - **Monitor network architecture** — distributed sensor nodes, redundant measurement paths, data bus interface (MIL-STD-1553 / SpaceWire), and connection to autonomy management system (`144`).
  - **Pressure event response** — rapid depressurisation detection (Δp > 0.34 kPa/min triggers emergency), crew shelter-in-place link to `101.007`, and ground-control notification via `100.005`.
  - **Calibration and verification** — on-orbit sensor calibration procedures and cross-check with reference gas standards.

## 3. Diagram — Pressure and Atmosphere Monitoring Network

```mermaid
flowchart LR
    SENSORS["Sensor Network<br/>(O₂ · CO₂ · P · T · RH)"]
    SENSORS --> DMON["Data Monitor Node<br/>(redundant)"]
    DMON --> AUTO["Autonomy Mgmt<br/>(144_Autonomia)"]
    DMON --> MCC["Mission Control<br/>(143_Control)"]

    SENSORS --> LEAK["Leak Detection<br/>(Δp/Δt algorithm)"]
    LEAK --> ALERT["Crew Alert<br/>(>0.34 kPa/min → emergency)"]
    ALERT --> SHELTER["Safe Haven<br/>(101.007)"]

    PREG["Pressure Regulators<br/>(+ relief valves)"] --> CABIN["Cabin P<br/>(50–103 kPa)"]
    CABIN --> SENSORS

    style CABIN fill:#2c82c9,color:#fff
    style ALERT fill:#e74c3c,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `102` — Soporte Vital ECLSS |
| Subsubject | `004` — Pressure Control and Cabin Atmosphere Monitoring |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/102_Soporte-Vital-ECLSS/` |
| Document | `004_Pressure-Control-and-Cabin-Atmosphere-Monitoring.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |
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
