---
document_id: QATL-ATLAS-1000-STA-120-129-02-120-000-GENERAL
title: "STA 120-129 · 120-000 — General"
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
subsection: "120"
subsection_title: "Propulsión Química"
subsubject: "000"
subsubject_title: "General"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · 120-000 — General

## 1. Purpose

Overview entry-point for the *Propulsión Química* subsection within the `120-129` code range (Section `02` — *Propulsión Espacial Tradicional y Avanzada*) of the **STA** architecture band.

This subsubject (`000 Overview`) introduces the STA 120-129.120 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the chemical propulsion framework governing controlled definitions, propellant family taxonomy, liquid/solid/hybrid systems, combustion hardware, feed systems, ignition boundaries, performance metrics, and hazard/safety governance. This subsection is designated **propulsion-critical**.

## 2. Scope

- Covers the *Propulsión Química* slice of the parent code range `120-129`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope across the subsection:
  - **Chemical Propulsion Controlled Definition** (`001`) — normative definition, scope, and applicability per ECSS-E-ST-35C[^ecssest35].
  - **Propellant Families and Selection Criteria** (`002`) — taxonomy of bipropellant, monopropellant, solid, hybrid propellant families.
  - **Liquid Propulsion Systems** (`003`) — pressure-fed and pump-fed architectures, main engine and RCS.
  - **Solid Propulsion Systems** (`004`) — solid rocket motor design, grain geometry, burn rate.
  - **Hybrid Propulsion Systems** (`005`) — hybrid oxidiser/fuel configurations, throttleability.
  - **Combustion Chambers, Nozzles and Thrust Generation** (`006`) — chamber design, nozzle expansion, c*, C_F.
  - **Feed Systems, Tanks, Valves and Pressurization** (`007`) — pressurant bottles, propellant tanks, isolation valves, fill/drain.
  - **Ignition, Start-Stop and Throttle Boundaries** (`008`) — ignition systems, restart envelope, minimum impulse bit.
  - **Performance Metrics: Isp, Thrust and Mass Fraction** (`009`) — specific impulse, thrust-to-weight, propellant mass fraction.
  - **Safety, Hazards, Testing and Assurance Boundaries** (`010`) — propellant hazard classes, proof pressure test, acceptance/qualification testing.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `120-129` |
| Section | `02` — Propulsión Espacial Tradicional y Avanzada |
| Subsection | `120` — Propulsión Química |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/120-129_Propulsion-Espacial-Tradicional-y-Avanzada/120_Propulsion-Quimica/` |
| Document | `120-000-General.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

[^ecssest35]: **ECSS-E-ST-35C — Propulsion General Requirements** — European standard for space propulsion systems design, test, and operation.

[^nasastd5012]: **NASA-STD-5012 — Structural Test Requirements for Liquid Propulsion Systems** — NASA standard for structural qualification and proof testing.

[^nasastd871915]: **NASA-STD-8719.15 — Safety Standard for Explosives, Propellants and Pyrotechnics** — NASA safety standard for propellant handling and pyrotechnic systems.

### Applicable industry standards

- ECSS-E-ST-35C — Propulsion General Requirements[^ecssest35]
- NASA-STD-5012 — Structural Test Requirements for Liquid Propulsion Systems[^nasastd5012]
- NASA-STD-8719.15 — Safety Standard for Explosives, Propellants and Pyrotechnics[^nasastd871915]
