---
document_id: QATL-ATLAS-1000-STA-120-129-02-121-000-OVERVIEW
title: "STA 120-129 · 02.121.000 — Overview"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "120-129"
section: "02"
section_title: "Propulsión Espacial Tradicional y Avanzada"
subsection: "121"
subsection_title: "Propulsión Eléctrica"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-HPC, Q-DATAGOV, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · Section 02 · Subsection 121 — Propulsión Eléctrica

## 1. Purpose

Overview entry-point for the *Propulsión Eléctrica* subsection within the `120-129` code range (Section `02` — *Propulsión Espacial Tradicional y Avanzada*) of the **STA** architecture band.

This subsubject (`000 Overview`) introduces the STA 120-129.121 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the electric propulsion framework governing controlled definitions, propulsion family taxonomy, electrothermal/electrostatic/electromagnetic system architectures, power processing units, propellant feed systems, performance metrics, thermal/EMC/plume interaction boundaries, and qualification/assurance governance. This subsection is designated **propulsion-critical**.

## 2. Scope

- Covers the *Propulsión Eléctrica* slice of the parent code range `120-129`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope across the subsection:
  - **Electric Propulsion Controlled Definition** (`001`) — normative definition, scope, and applicability per ECSS-E-ST-35C[^ecssest35].
  - **Electric Propulsion Families and Selection Criteria** (`002`) — taxonomy of electrothermal, electrostatic, and electromagnetic systems.
  - **Electrothermal Propulsion** (`003`) — resistojets, arcjets, and microwave electrothermal systems.
  - **Electrostatic Propulsion: Ion and Hall Effect** (`004`) — gridded ion thrusters and Hall-effect thrusters (HET/SPT).
  - **Electromagnetic Propulsion: MPDT and Pulsed Plasma** (`005`) — magnetoplasmadynamic thrusters and pulsed plasma thrusters.
  - **Power Processing Units and Electrical Interfaces** (`006`) — PPU design, PCDU interface, bus voltage, EMC constraints.
  - **Propellant Feed, Storage and Compatibility** (`007`) — xenon/krypton/iodine feed systems, propellant compatibility, storage.
  - **Thrust, Isp, Efficiency and Duty-Cycle Metrics** (`008`) — thrust levels, specific impulse, total impulse, power-to-thrust ratio, duty cycle.
  - **Thermal, EMC and Plume Interaction Boundaries** (`009`) — thruster thermal zones, EMC limits, plume impingement analysis.
  - **Testing, Qualification and Assurance Boundaries** (`010`) — acceptance/qualification test campaign, vacuum facility requirements.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `120-129` |
| Section | `02` — Propulsión Espacial Tradicional y Avanzada |
| Subsection | `121` — Propulsión Eléctrica |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-GREENTECH, Q-HPC, Q-DATAGOV, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/120-129_Propulsion-Espacial-Tradicional-y-Avanzada/121_Propulsion-Electrica/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

[^ecssest35]: **ECSS-E-ST-35C — Propulsion General Requirements** — European standard for space propulsion systems design, test, and operation.

[^nasatm103642]: **NASA-TM-103642 — Electric Propulsion Development** — NASA technical memorandum on electric propulsion system development.

### Applicable industry standards

- ECSS-E-ST-35C — Propulsion General Requirements[^ecssest35]
- NASA-TM-103642 — Electric Propulsion Development[^nasatm103642]
