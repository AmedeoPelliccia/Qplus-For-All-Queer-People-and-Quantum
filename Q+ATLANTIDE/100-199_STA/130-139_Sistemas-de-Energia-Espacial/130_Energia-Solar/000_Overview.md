---
document_id: QATL-ATLAS-1000-STA-130-139-03-130-000-OVERVIEW
title: "STA 130-139 · 03.130.000 — Overview"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "130-139"
section: "03"
section_title: "Sistemas de Energía Espacial"
subsection: "130"
subsection_title: "Energía Solar"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · Section 03 · Subsection 130 — Energía Solar

## 1. Purpose

Overview entry-point for the *Energía Solar* subsection within the `130-139` code range (Section `03` — *Sistemas de Energía Espacial*) of the **STA** architecture band.

This subsubject (`000 Overview`) introduces the STA 130-139.130 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the solar energy framework covering controlled definitions, photovoltaic array architectures, solar cell technologies, deployable panel structural interfaces, sun-pointing constraints, power conversion and MPPT, degradation effects, eclipse operations, and standards mapping. This subsection is designated **mission-energy critical**.

## 2. Scope

- Covers the *Energía Solar* slice of the parent code range `130-139`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope across the subsection:
  - **Solar Energy Controlled Definition** (`001`) — normative definition, scope, and applicability per ECSS-E-ST-20C[^ecssest20].
  - **Photovoltaic Array Architectures** (`002`) — panel layouts, fixed vs. deployable, body-mounted vs. wing.
  - **Solar Cell Technologies and Efficiency Classes** (`003`) — Si, GaAs, multi-junction III-V, perovskite tandem.
  - **Deployable Panels, Wings and Structural Interfaces** (`004`) — hinge mechanisms, deployment sequences, structural loads.
  - **Sun-Pointing, Tracking and Attitude Constraints** (`005`) — SADM requirements, slew rates, eclipse-transition margins.
  - **Power Conversion, Regulation and MPPT** (`006`) — MPPT algorithms, bus voltage regulation, shunt/linear/switching regulators.
  - **Degradation, Radiation and Thermal Cycling Effects** (`007`) — BOL/EOL power, AM0 flux, proton/electron fluence, thermal cycling.
  - **Eclipse Operations and Energy Budgeting** (`008`) — eclipse duration, power budget methodology, minimum bus voltage.
  - **ECSS-NASA Solar Power Standards Mapping** (`009`) — ECSS-E-ST-20C, ECSS-E-ST-20-08C, NASA-HDBK-4002B.
  - **Traceability, Evidence and Lifecycle Governance** (`010`) — IVV evidence, design review gates, FMEA, lifecycle records.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `130-139` |
| Section | `03` — Sistemas de Energía Espacial |
| Subsection | `130` — Energía Solar |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/130-139_Sistemas-de-Energia-Espacial/130_Energia-Solar/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

[^ecssest20]: **ECSS-E-ST-20C — Electrical and Electronic** — European standard for spacecraft electrical power subsystems design and test.

[^nasahdbk4002b]: **NASA-HDBK-4002B — Mitigating In-Space Charging Effects** — NASA handbook for spacecraft charging and solar array design.

### Applicable industry standards

- ECSS-E-ST-20C — Electrical and Electronic[^ecssest20]
- ECSS-E-ST-20-08C — Space Engineering: Photovoltaic Assemblies and Components
- NASA-HDBK-4002B — Mitigating In-Space Charging Effects[^nasahdbk4002b]
