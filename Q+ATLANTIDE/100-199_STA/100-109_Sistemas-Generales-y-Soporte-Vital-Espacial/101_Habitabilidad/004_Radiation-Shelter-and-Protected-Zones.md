---
document_id: QATL-ATLAS-1000-STA-100-109-00-101-004-RADIATION-SHELTER-AND-PROTECTED-ZONES
title: "STA 100-109 · 00.101.004 — Radiation Shelter and Protected Zones"
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
subsubject: "004"
subsubject_title: "Radiation Shelter and Protected Zones"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · Section 00 · Subsection 101 · Subsubject 004 — Radiation Shelter and Protected Zones

## 1. Purpose

Defines the **radiation shielding requirements, shelter-in-place design, and protected-zone architecture** for crewed space missions subject to solar particle events (SPE) and galactic cosmic radiation (GCR), per NASA-STD-3001 Vol.1[^nastd3001] and ECSS-E-ST-10-02C.

## 2. Scope

- Covers the *Radiation Shelter and Protected Zones* subsubject (`004`) of subsection `101`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Radiation environment** — SPE and GCR dose models per ECSS-E-ST-10-02C for each orbital regime (LEO within/beyond ISS shielding, cis-lunar, interplanetary).
  - **Career dose limits** — REID (Risk of Exposure-Induced Death) limits per NASA-STD-3001 Vol.1[^nastd3001] and ALARA principles.
  - **Shielding mass allocation** — polyethylene, water, and structural-material shielding mass budget per habitat module.
  - **Protected zone design** — central storm shelter location, minimum shielding thickness (≥10 g/cm² areal density for SPE), and crew-stowage layout to maximise passive shielding.
  - **Radiation monitor network** — on-board dosimetry sensor placement and alert thresholds linking to GNC and autonomy systems (`140`, `144`).
  - **Crew exposure tracking** — personal dosimetry, mission cumulative dose recording, and medical review interfaces.

## 3. Diagram — Radiation Shelter Architecture

```mermaid
flowchart TB
    ENV["Space Radiation Environment<br/>(SPE · GCR — ECSS-E-ST-10-02C)"]
    ENV --> DOSE["Dose Assessment<br/>(REID limit per NASA-STD-3001)"]
    DOSE --> SHIELD["Shielding Design<br/>(polyethylene · water · structure)"]
    SHIELD --> ZONE["Protected Zone<br/>(storm shelter ≥10 g/cm²)"]
    SHIELD --> MASS["Shielding Mass Budget<br/>(per module allocation)"]
    ZONE --> MONITOR["Radiation Monitor Network<br/>(dosimetry · alert thresholds)"]
    MONITOR --> GNC["GNC / Autonomy<br/>(140 · 144)"]
    DOSE --> TRACK["Crew Exposure Tracking<br/>(personal dosimetry)"]

    style ENV fill:#e74c3c,color:#fff
    style ZONE fill:#2c82c9,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `101` — Habitabilidad |
| Subsubject | `004` — Radiation Shelter and Protected Zones |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/101_Habitabilidad/` |
| Document | `004_Radiation-Shelter-and-Protected-Zones.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |
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
