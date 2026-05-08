---
document_id: QATL-ATLAS-1000-STA-180-189-08-182-000-OVERVIEW
title: "STA 180-189 · 08.182.000 — Overview"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "180-189"
section: "08"
section_title: "Infraestructura y Logística Espacial"
subsection: "182"
subsection_title: "Transporte Espacial"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
safety_boundary: "space-transport critical; requires explicit trajectory assurance, propulsion/power/thermal constraints, docking and transfer-interface validation, cargo/crew boundary control, rendezvous governance, traffic coordination and lifecycle traceability"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 180-189 · Section 08 · Subsection 182 — Transporte Espacial

## 1. Purpose

Entry-point overview for *Transporte Espacial* (subsection `182`) within STA `180-189` — *Infraestructura y Logística Espacial*. This document establishes the space transport framework spanning controlled definitions, transport classes and mission roles, launch-to-orbit interfaces, orbital transfer and in-space transport, cargo/crew/service transport boundaries, docking/berthing/transfer interfaces, propulsion/power/thermal constraints, trajectory operations and traffic control, standards mapping, and lifecycle traceability.

This subsection is designated **space-transport critical** under the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline]. All subsubjects (`001`–`010`) inherit the `safety_boundary` declaration and require explicit trajectory assurance, propulsion/power/thermal constraints, docking and transfer-interface validation, cargo/crew boundary control, rendezvous governance, traffic coordination, and lifecycle traceability.

## 2. Scope

- **Controlled definitions** (`001`): space transport system, launch vehicle (LV), orbital transfer vehicle (OTV), crew transport vehicle (CTV), cargo resupply spacecraft (CRS), reusable launch vehicle (RLV), transfer stage, payload interface.
- **Transport classes and mission roles** (`002`): expendable launch vehicle, reusable launch vehicle, in-space transfer tug, crewed transport capsule, autonomous cargo freighter; mission roles covering crew rotation, cargo resupply, propellant ferry, science payload delivery, infrastructure emplacement, and emergency return.
- **Launch-to-orbit interfaces** (`003`): payload fairing interfaces, launch vehicle adapter (LVA) design, separation event timing, MECO/SECO conditions, orbit insertion accuracy (Δa, Δe, Δi tolerances), upper-stage/kick-stage separation, umbilical connector standards.
- **Orbital transfer and in-space transport** (`004`): OTV delta-V budgets, propellant margin standards, multi-burn trajectories, cis-lunar transport corridor definitions, NRHO/LLO/DRO insertion manoeuvres.
- **Cargo, crew and service transport boundaries** (`005`): pressurised vs unpressurised cargo, hazardous materials handling and containment, crew-rated launch vehicle criteria (NASA-STD-8729.1), crew escape system authority, ORU delivery protocols, EVA support manifests.
- **Docking, berthing and transfer interfaces** (`006`): IDSS, CBM, APAS-89/95 legacy, androgynous peripheral docking system, approach ellipsoid and keep-out zone (KOZ) dimensions, hatch opening and pressurisation equalisation sequences.
- **Propulsion, power and thermal transport constraints** (`007`): minimum Isp requirements per mission class, propellant loading accuracy (±0.5 %), engine-out redundancy criteria, on-orbit power budget during transit, TPS design drivers (re-entry peak heat flux), on-orbit thermal cycling limits.
- **Trajectory operations, rendezvous and traffic control** (`008`): nominal ascent trajectory management, far-field approach (R-bar, V-bar), final approach corridor (20 m hold point, 10 m capture zone), abort authority hierarchy, launch window management, range safety requirements, Space Situational Awareness (SSA) hand-off, conjunction assessment data standard (CDM per CCSDS 508.0-B-1).
- **ECSS / NASA / CCSDS standards mapping** (`009`): ECSS-E-ST-60C, ECSS-E-ST-35C, ECSS-E-ST-32C, NASA-STD-8729.1, NASA-STD-5019, CCSDS 910.11-B-1, CCSDS 508.0-B-1, FAA 14 CFR Part 415, ISO 24113:2019, ECSS-Q-ST-40C.
- **Traceability, evidence and lifecycle governance** (`010`): requirements-to-vehicle RTM structure, evidence types (trajectory analysis, propulsion test, structural analysis, ICD verification, human-rating review), ECSS-M-ST-10C Phase 0–F gate criteria (CDR, Qualification Review, FRR, Launch Commit Criteria, Post-Flight Review), transport critical item list (TCIL), configuration control board (CCB).
- **No-AAA rule**: the identifier "AAA" must not be used for any safety-critical element across all subsubjects of this subsection.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `180-189` |
| Section | `08` — Infraestructura y Logística Espacial |
| Subsection | `182` — Transporte Espacial |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

| Standard | Body | Scope |
|---|---|---|
| ECSS-E-ST-60C | ESA/ECSS | GNC / rendezvous trajectory design |
| ECSS-E-ST-35C | ESA/ECSS | Propulsion systems |
| CCSDS 910.11-B-1 | CCSDS | Proximity operations / rendezvous protocols |
| FAA 14 CFR Part 415 | FAA AST | Commercial launch licensing |
| NASA-STD-8729.1 | NASA | Human-rating criteria for CTV |

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `180-189` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.
