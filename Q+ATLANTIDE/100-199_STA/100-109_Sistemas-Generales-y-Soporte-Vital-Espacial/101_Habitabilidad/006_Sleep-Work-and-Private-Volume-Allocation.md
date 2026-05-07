---
document_id: QATL-ATLAS-1000-STA-100-109-00-101-006-SLEEP-WORK-AND-PRIVATE-VOLUME-ALLOCATION
title: "STA 100-109 · 00.101.006 — Sleep Work and Private Volume Allocation"
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
subsubject: "006"
subsubject_title: "Sleep Work and Private Volume Allocation"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · Section 00 · Subsection 101 · Subsubject 006 — Sleep, Work and Private Volume Allocation

## 1. Purpose

Defines the **crew-volume partitioning rules, scheduling framework, and privacy provisions** for sleep, work, and personal time within crewed space habitats, per NASA-STD-3001 Vol.2[^nastd3001v2] and ICES-HB-11A[^icesseh].

## 2. Scope

- Covers the *Sleep, Work and Private Volume Allocation* subsubject (`006`) of subsection `101`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Sleep volume** — minimum individual crew-quarter volume (≥ 2.3 m³ for long-duration missions per NASA-STD-3001 Vol.2[^nastd3001v2]), acoustic isolation (≤ 62 dB-A), lighting control, and temperature-setpoint authority.
  - **Work volume** — primary and secondary workstation allocation, reach-envelope compliance, display/control layout, and multi-function area scheduling.
  - **Privacy provisions** — visual and acoustic separation between crew quarters, medical examination areas, and personal-hygiene facilities.
  - **Circadian scheduling** — 24-hour sleep/wake cycle management, light therapy provisions, and interface with the circadian lighting system (`003`).
  - **Exercise volume** — countermeasure exercise equipment footprint, scheduling windows, and acoustic isolation from sleep zones.
  - **Cultural and personal space** — provisions for personalisation, recreation, communication with family, and psychological support per ICES-HB-11A[^icesseh].

## 3. Diagram — Volume Partitioning and Scheduling

```mermaid
flowchart TB
    NHV["Net Habitable Volume (NHV)<br/>from 002"]
    NHV --> CQ["Crew Quarters<br/>(sleep · privacy · temp-ctrl)"]
    NHV --> WS["Work Volume<br/>(workstations · multi-function areas)"]
    NHV --> EXER["Exercise Volume<br/>(countermeasures)"]
    NHV --> PRIV["Privacy Areas<br/>(medical · hygiene)"]
    NHV --> REC["Recreation / Personal Space<br/>(communication · culture)"]

    CQ --> CIRC["Circadian Lighting<br/>(003 — Environmental Comfort)"]
    EXER -. "noise isolation" .-> CQ

    style NHV fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `101` — Habitabilidad |
| Subsubject | `006` — Sleep, Work and Private Volume Allocation |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/101_Habitabilidad/` |
| Document | `006_Sleep-Work-and-Private-Volume-Allocation.md` (this file) |
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
