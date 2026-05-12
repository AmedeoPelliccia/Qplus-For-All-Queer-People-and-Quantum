---
document_id: QATL-ATLAS-1000-STA-100-109-00-106-030-RADIATION-EXPOSURE-AND-DOSIMETRY
title: "STA 100-109 · 106-030 — Radiation-Exposure-and-Dosimetry"
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
subsection: "106"
subsection_title: "Salud Tripulación y Factores Humanos"
subsubject: "030"
subsubject_title: "Radiation-Exposure-and-Dosimetry"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 106-030 — Radiation-Exposure-and-Dosimetry

## 1. Purpose

Defines the **radiation monitoring, dosimetry, and protection architecture** for Q+ATLANTIDE crewed missions, specifying dose limits, shield design requirements, solar particle event (SPE) response, and ALARA implementation per NCRP-132[^ncrp132] and NASA-STD-3001[^nastd3001].

Space radiation sources include: galactic cosmic rays (GCR, 0.1–1 Sv/year in free space), solar particle events (SPE, up to 1–10 Sv in hours during major events), and trapped Van Allen belt radiation. The NASA career limit is 3 % Risk of Exposure-Induced Death (REID), corresponding to approximately 0.5–1.0 Sv effective dose depending on age and sex. ALARA requires optimization of: mission duration, orbital trajectory (inclination, altitude), structural shielding (polyethylene, water walls), and SPE shelter design (minimum 5 g/cm² shielding for shelter). Active dosimetry: personal dosimeters (thermoluminescent, TLD) + charged particle directional spectrometer (CPDS) for area monitoring.

## 2. Scope

- Covers the *Radiation-Exposure-and-Dosimetry* subsubject (`030`) of subsection `106`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All design decisions and monitoring thresholds traceable to NASA-STD-3001[^nastd3001] and CSDB evidence per subsection `109`.

## 3. Diagram — Radiation-Exposure-and-Dosimetry

```mermaid
flowchart TB
    GCR["Galactic Cosmic Rays<br/>(0.1–1 Sv/yr)"]
    SPE["Solar Particle Events<br/>(1–10 Sv acute risk)"]
    TRAPPED["Van Allen Belt<br/>(LEO passage)"]

    GCR & SPE & TRAPPED --> SHIELD["Structural Shielding<br/>(polyethylene · water walls<br/>> 5 g/cm² shelter)"]
    SHIELD --> DOSE["Residual Dose<br/>(monitor vs. REID limit)"]

    DOSE --> TLD["Personal Dosimeter<br/>(TLD per crew)"]
    DOSE --> CPDS["Area Monitor<br/>(CPDS spectrometer)"]
    TLD & CPDS --> DOSE_DB["Dosimetry Database<br/>(cumulative REID tracking)"]

    SPE_WARN["SPE Warning System<br/>(NOAA / ESA space weather)"] --> SHELTER["SPE Shelter Protocol<br/>(crew to shelter < 15 min)"]
    style SPE fill:#e74c3c,color:#fff
    style SHELTER fill:#e74c3c,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `106` — Salud Tripulación y Factores Humanos |
| Subsubject | `030` — Radiation-Exposure-and-Dosimetry |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/106_Salud-Tripulacion-y-Factores-Humanos/` |
| Document | `106-030-Radiation-Exposure-and-Dosimetry.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`106-000-General.md`](./106-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management.

[^nastd3001]: **NASA-STD-3001 Vol.1 & Vol.2 — Human Integration Design Handbook / Human Factors, Habitability, and Environmental Health** — Primary standard for crew health, physical performance, and medical monitoring requirements.

[^nasahf]: **NASA/SP-2010-3407 — Human Integration Design Handbook (HIDH)** — Comprehensive human factors guidance for crewed spacecraft design.

[^ecsse10]: **ECSS-E-HB-10-12A — Methods for the Calculation of Reliability** — Reliability and human factors engineering methodology applicable to crew health monitoring systems.

[^iso9241]: **ISO 9241-11:2018 — Ergonomics of Human-System Interaction** — Usability and ergonomics standards applicable to crew health monitoring interfaces.

### Applicable industry standards

- NASA-STD-3001 Vol.1 & Vol.2 — Human Integration Design Handbook[^nastd3001]
- NASA/SP-2010-3407 — Human Integration Design Handbook[^nasahf]
- ECSS-E-HB-10-12A — Methods for the Calculation of Reliability[^ecsse10]
- ISO 9241-11:2018 — Ergonomics of Human-System Interaction[^iso9241]

[^ncrp132]: **NCRP Report No. 132 — Radiation Protection Guidance for Activities in Low-Earth Orbit** — Career dose limits and SPE protection requirements for crewed space missions.

[^milstd1472]: **MIL-STD-1472G — Human Engineering** — Anthropometric, display, control, and cognitive load requirements applicable to crewed spacecraft.
