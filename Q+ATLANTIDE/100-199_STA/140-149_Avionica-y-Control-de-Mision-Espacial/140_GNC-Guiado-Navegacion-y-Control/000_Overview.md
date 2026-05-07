---
document_id: QATL-ATLAS-1000-STA-140-149-04-140-000-OVERVIEW
title: "STA 140-149 · 04.140.000 — Overview"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "140-149"
section: "04"
section_title: "Aviónica y Control de Misión Espacial"
subsection: "140"
subsection_title: "GNC — Guiado, Navegación y Control"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HPC, Q-DATAGOV, Q-HORIZON, Q-AIR, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 140-149 · Section 04 · Subsection 140 — GNC — Guiado, Navegación y Control

## 1. Purpose

Overview entry-point for the *GNC — Guiado, Navegación y Control* subsection within the `140-149` code range (Section `04` — *Aviónica y Control de Misión Espacial*) of the **STA** architecture band.

This subsubject (`000 Overview`) introduces the STA 140-149.140 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the GNC framework covering controlled definitions, guidance architecture, navigation sensor suites, control laws, actuator interfaces, autonomous and safe modes, software interfaces, verification and validation, standards mapping, and lifecycle governance. This subsection is designated **mission-control critical**.

## 2. Scope

- Covers the *GNC — Guidance, Navigation and Control* slice of the parent code range `140-149`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope across the subsection:
  - **GNC Controlled Definition** (`001`) — normative boundary of GNC within STA, per ECSS-E-ST-60C[^ecssest60c], distinction from flight software (142), avionics (141), and mission control (143).
  - **Guidance Architecture and Mission Trajectory Logic** (`002`) — trajectory planning, maneuver execution, targeting logic, delta-v budget accountability.
  - **Navigation Sensors, State Estimation and Reference Frames** (`003`) — star trackers, gyros, GPS, LIDAR; Kalman filter, EKF, UKF; ECI, ECEF, body and orbit-relative frames.
  - **Control Laws, Attitude and Orbit Control** (`004`) — PD, PID, LQR, sliding-mode control; AOCS modes; orbit control maneuver logic.
  - **Actuators: Reaction Wheels, Thrusters and Magnetorquers** (`005`) — RW sizing and momentum management, thruster selection, magnetorquer authority, redundancy strategy.
  - **Autonomous Modes, Safe Modes and Contingency Control** (`006`) — Sun-acquisition, emergency spin-stabilization, safe attitude, autonomous maneuver inhibit/abort logic.
  - **GNC Software Interfaces and Timing Constraints** (`007`) — GNC-to-FSW interface boundary, sensor data rates, actuator command timing, deterministic execution, OBSW integration.
  - **Verification, Validation, Simulation and HIL Testing** (`008`) — functional simulation, 6-DOF simulator, HIL testing with actual sensors/actuators, test coverage requirements.
  - **ECSS-NASA GNC Standards Mapping** (`009`) — standards hierarchy: ECSS-E-ST-60C, ECSS-E-ST-60-10C, ECSS-E-ST-60-30C, NASA-STD-7009A, CCSDS 871.0-M-1.
  - **Traceability, Evidence and Lifecycle Governance** (`010`) — requirements traceability, evidence gates, in-orbit performance monitoring, lifecycle records.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `140-149` |
| Section | `04` — Aviónica y Control de Misión Espacial |
| Subsection | `140` — GNC — Guiado, Navegación y Control |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV, Q-HORIZON, Q-AIR, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/140-149_Avionica-y-Control-de-Mision-Espacial/140_GNC-Guiado-Navegacion-y-Control/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

[^ecssest60c]: **ECSS-E-ST-60C — Control Engineering** — European standard for spacecraft GNC system design and verification.

[^nasastd7009a]: **NASA-STD-7009A — Standard for Models and Simulations** — NASA standard for development and use of models and simulations.

[^ccsds8710m1]: **CCSDS 871.0-M-1 — Navigation Data — Definitions and Conventions** — CCSDS recommended standard for navigation data definitions.

### Applicable industry standards

- ECSS-E-ST-60C — Control Engineering[^ecssest60c]
- ECSS-E-ST-60-10C — Space Engineering: Control Performance
- NASA-STD-7009A — Standard for Models and Simulations[^nasastd7009a]
- CCSDS 871.0-M-1 — Navigation Data — Definitions and Conventions[^ccsds8710m1]
