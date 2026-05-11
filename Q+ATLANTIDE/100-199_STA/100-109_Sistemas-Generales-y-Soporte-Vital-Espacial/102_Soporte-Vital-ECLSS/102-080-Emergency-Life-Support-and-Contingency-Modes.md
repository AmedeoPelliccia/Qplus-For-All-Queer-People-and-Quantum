---
document_id: QATL-ATLAS-1000-STA-100-109-00-102-080-EMERGENCY-LIFE-SUPPORT-AND-CONTINGENCY-MODES
title: "STA 100-109 · 102-080 — Emergency Life Support and Contingency Modes"
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
subsubject: "080"
subsubject_title: "Emergency Life Support and Contingency Modes"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · 102-080 — Emergency Life Support and Contingency Modes

## 1. Purpose

Defines the **emergency life support configuration and contingency operational modes** for ECLSS, ensuring crew survivability for a minimum of 24 hours without primary system operation or ground contact, in support of the safe-haven requirements declared in `101.007`.

## 2. Scope

- Covers the *Emergency Life Support and Contingency Modes* subsubject (`008`) of subsection `102`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Emergency O₂ supply** — SFOG canister inventory sized for ≥ 24 h crew O₂ demand in safe-haven shelter; activation procedure (manual + autonomous).
  - **Emergency CO₂ removal** — LiOH canister inventory sized for ≥ 24 h CO₂ scrubbing; activation procedure; interface with `101.007` storm shelter volume.
  - **Emergency water reserve** — potable water reserve sized for ≥ 72 h crew demand, stored in WRS distribution system or dedicated bladder.
  - **Contingency atmosphere modes** — five-mode ECLSS operational states: Normal, Reduced Power, Emergency Unmanned, Emergency Crewed, and Emergency Safe-Haven.
  - **Failure cascade prevention** — single-point failure elimination at life-support critical interfaces; cross-strapping between primary and backup subsystems.
  - **Crew interface** — emergency mode annunciation, manual override capability, and crew procedure references for contingency ECLSS operation.
  - **Mission control interface** — ground-commanded mode switching, telemetry health data, and ECLSS status reporting to `100.005`.

## 3. Diagram — Emergency Life Support Mode Hierarchy

```mermaid
stateDiagram-v2
    [*] --> Normal
    Normal --> ReducedPower : power emergency
    Normal --> EmergencyCrewedMode : ECLSS fault
    Normal --> EmergencySafeHaven : SPE / depress / fire
    EmergencyCrewedMode --> EmergencySafeHaven : escalation
    ReducedPower --> Normal : power restored
    EmergencyCrewedMode --> Normal : fault cleared
    EmergencySafeHaven --> EmergencyCrewedMode : shelter cleared

    Normal : Normal
(full ECLSS)
    ReducedPower : Reduced Power
(non-critical ECLSS off)
    EmergencyCrewedMode : Emergency Crewed
(SFOG + LiOH active)
    EmergencySafeHaven : Emergency Safe Haven
(24 h autonomy)
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `102` — Soporte Vital ECLSS |
| Subsubject | `008` — Emergency Life Support and Contingency Modes |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/102_Soporte-Vital-ECLSS/` |
| Document | `102-080-Emergency-Life-Support-and-Contingency-Modes.md` (this file) |
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
