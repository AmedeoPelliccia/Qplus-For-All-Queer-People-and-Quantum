---
document_id: QATL-ATLAS-1000-STA-100-109-00-101-070-EMERGENCY-HABITABILITY-AND-SAFE-HAVEN
title: "STA 100-109 · 101-070 — Emergency Habitability and Safe Haven"
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
subsection: "101"
subsection_title: "Habitabilidad"
subsubject: "070"
subsubject_title: "Emergency Habitability and Safe Haven"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · 101-070 — Emergency Habitability and Safe Haven

## 1. Purpose

Defines the **emergency habitability requirements and safe-haven design criteria** for crewed space missions — providing the crew with a protected refuge during contingency events (solar particle event, fire, rapid depressurisation, toxic atmosphere) — per NASA-STD-3001 Vol.1[^nastd3001] and the Q+ATLANTIDE STA safety framework.

## 2. Scope

- Covers the *Emergency Habitability and Safe Haven* subsubject (`007`) of subsection `101`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Safe-haven volume** — minimum pressurised volume for the full crew complement during contingency (≥ 0.6 m³/crewmember in pressure suits), integrated with the radiation storm shelter (`004`).
  - **Safe-haven duration** — minimum autonomous survivability duration (≥ 24 hours) without ground contact, including consumables (O₂, CO₂ scrubbing, water) from ECLSS emergency reserves (`102`).
  - **Emergency access and egress** — time-from-alarm-to-shelter requirement (≤ 3 minutes for SPE shelter-in-place), hatch accessibility, and crew-suit donning time.
  - **Pressure-suit stowage** — provision and accessibility of emergency pressure suits/EVA suits adjacent to crew work areas.
  - **Fire and toxic-atmosphere shelter** — smoke and contamination isolation, independent breathing-gas supply, and interface with fire-detection systems.
  - **Integrated emergency response** — linkage to mission control (`143`), autonomy systems (`144`), and crew medical response.

## 3. Diagram — Emergency Habitability Decision Tree

```mermaid
flowchart TD
    ALARM["Emergency Event<br/>(SPE · fire · depress · toxic)"]
    ALARM --> ASSESS["Crew Assessment<br/>(≤3 min response)"]
    ASSESS --> SHELTER["Safe Haven<br/>(radiation · pressure · fire)"]
    SHELTER --> O2["ECLSS Emergency Reserves<br/>(O₂ · CO₂ scrub · water — 102)"]
    SHELTER --> SUITS["Pressure Suits<br/>(stowage accessible)"]
    SHELTER --> COMMS["Ground Contact<br/>(143 Mission Control)"]
    SHELTER --> AUTO["On-board Autonomy<br/>(144 — if ground link lost)"]
    SHELTER --> DUR["24-hour Autonomous<br/>Survivability"]

    style ALARM fill:#e74c3c,color:#fff
    style SHELTER fill:#2c82c9,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `101` — Habitabilidad |
| Subsubject | `007` — Emergency Habitability and Safe Haven |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/101_Habitabilidad/` |
| Document | `101-070-Emergency-Habitability-and-Safe-Haven.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`101-000-General.md`](./101-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `100-109` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^nastd3001]: **NASA-STD-3001 Vol.1 — Space Human Factors Engineering** — Governs crew habitable volume, environmental parameters, human-factors requirements, and physiological constraints for crewed space missions.

[^nastd3001v2]: **NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health** — Detailed habitability design requirements covering comfort, sleep, hygiene, food, and emergency safe-haven provisions.

[^ecsse34]: **ECSS-E-ST-34C — Space Engineering: Environmental Control and Life Support** — European standard for ECLSS design, interface requirements, and subsystem test criteria.

[^iso11399]: **ISO 11399 — Ergonomics of the Thermal Environment** — Provides principles and application of relevant International Standards for ergonomic assessment of the thermal environment in enclosed spaces.

[^icesseh]: **ICES-HB-11A — ECSS Handbook: Spacecraft Crew Compartment Design** — Guidance document on crew-compartment layout, human-machine interface, and habitability assessment methods.

### Applicable industry standards

- NASA-STD-3001 Vol.1 — Space Human Factors Engineering[^nastd3001]
- NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health[^nastd3001v2]
- ECSS-E-ST-34C — Space Engineering: Environmental Control and Life Support[^ecsse34]
- ISO 11399 — Ergonomics of the Thermal Environment[^iso11399]
- ICES-HB-11A — Spacecraft Crew Compartment Design[^icesseh]
