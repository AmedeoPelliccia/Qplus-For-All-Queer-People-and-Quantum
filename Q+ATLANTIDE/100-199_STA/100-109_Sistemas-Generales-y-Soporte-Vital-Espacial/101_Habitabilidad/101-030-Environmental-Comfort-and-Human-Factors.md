---
document_id: QATL-ATLAS-1000-STA-100-109-00-101-030-ENVIRONMENTAL-COMFORT-AND-HUMAN-FACTORS
title: "STA 100-109 · 101-030 — Environmental Comfort and Human Factors"
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
subsubject: "030"
subsubject_title: "Environmental Comfort and Human Factors"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · 101-030 — Environmental Comfort and Human Factors

## 1. Purpose

Establishes the **environmental quality and human-factors design requirements** for crewed space habitats — covering thermal comfort, acoustic environment, lighting, vibration, and ergonomics — per NASA-STD-3001 Vol.2[^nastd3001v2] and ISO 11399[^iso11399].

## 2. Scope

- Covers the *Environmental Comfort and Human Factors* subsubject (`003`) of subsection `101`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Thermal comfort** — cabin temperature range (18–27 °C), relative humidity (25–75%), and air velocity limits; demands placed on ECLSS (`102`) per ISO 11399[^iso11399].
  - **Acoustic environment** — continuous noise level limits (≤72 dB-A in work areas, ≤62 dB-A in sleep areas), speech intelligibility requirements, and acoustic panel design.
  - **Lighting** — task lighting, circadian lighting cycles, and emergency lighting levels per NASA-STD-3001 Vol.2[^nastd3001v2].
  - **Vibration and loads** — crew-equipment interface vibration isolation and maximum sustained g-load limits for operations and contingency phases.
  - **Ergonomics and HMI** — reach envelope, display legibility, control layout, and anthropometric range coverage (5th–95th percentile crew per NASA-STD-3001 Vol.1[^nastd3001]).
  - **Psychological comfort** — window provision, colour schemes, personalisation allowances, and privacy provisions.

## 3. Diagram — Environmental Parameter Hierarchy

```mermaid
flowchart LR
    HF["Human Factors Requirements<br/>(NASA-STD-3001 Vol.1/2)"]
    HF --> THERM["Thermal Comfort<br/>18–27 °C · 25–75% RH"]
    HF --> ACOU["Acoustics<br/>≤72 dB-A work · ≤62 dB-A sleep"]
    HF --> LIGHT["Lighting<br/>task · circadian · emergency"]
    HF --> VIB["Vibration/Loads<br/>isolation · g-limits"]
    HF --> ERGO["Ergonomics & HMI<br/>reach · display · anthropometry"]
    HF --> PSYCH["Psychological Comfort<br/>windows · privacy · colour"]

    THERM --> ECLSS["ECLSS Interfaces<br/>(102 Soporte Vital)"]
    ACOU --> ECLSS
    style HF fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `101` — Habitabilidad |
| Subsubject | `003` — Environmental Comfort and Human Factors |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/101_Habitabilidad/` |
| Document | `101-030-Environmental-Comfort-and-Human-Factors.md` (this file) |
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
