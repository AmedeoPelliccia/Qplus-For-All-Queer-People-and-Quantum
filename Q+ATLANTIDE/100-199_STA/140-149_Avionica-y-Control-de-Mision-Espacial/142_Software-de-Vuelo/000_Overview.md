---
document_id: QATL-ATLAS-1000-STA-140-149-04-142-000-OVERVIEW
title: "STA 140-149 · 04.142.000 — Overview"
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
subsection: "142"
subsection_title: "Software de Vuelo"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 140-149 · Section 04 · Subsection 142 — Software de Vuelo

## 1. Purpose

Overview entry-point for the *Software de Vuelo* subsection within the `140-149` code range (Section `04` — *Aviónica y Control de Misión Espacial*) of the **STA** architecture band.

This subsubject (`000 Overview`) introduces the STA 140-149.142 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the flight software framework covering controlled definitions, onboard software architecture, command/telemetry/data handling software, GNC software interfaces, FDIR, safe-mode and contingency recovery, real-time scheduling and determinism, verification/validation/simulation/HIL, standards mapping, and lifecycle governance. This subsection is designated **mission-software critical**.

## 2. Scope

- Covers the *Flight Software* slice of the parent code range `140-149`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope across the subsection:
  - **Flight Software Controlled Definition** (`001`) — normative boundary of FSW within STA; distinction from hardware avionics (141), GNC algorithms (140), and mission control (143).
  - **Onboard Software Architecture** (`002`) — FSW architecture layers (BSP, RTOS, middleware, application); component-based design; software configuration management; partitioning.
  - **Command, Telemetry and Data Handling Software** (`003`) — TC/TM packet processing (CCSDS PUS layer); telecommand authentication; housekeeping telemetry generation; mass memory management.
  - **GNC Software Interfaces and Control Loops** (`004`) — interface boundary between FSW and GNC algorithms (140); sensor driver software; actuator command generation; control-loop execution timing.
  - **FDIR: Fault Detection, Isolation and Recovery Logic** (`005`) — FDIR architecture in software: fault detection algorithms, anomaly thresholds, isolation actions, recovery sequences, interaction with hardware watchdogs.
  - **Safe-Mode, Contingency and Autonomous Recovery Software** (`006`) — safe-mode transition sequences; autonomous onboard emergency management; contingency mode logic; ground-command-free recovery procedures.
  - **Real-Time Scheduling, Timing and Determinism** (`007`) — RTOS selection and configuration; task priority scheme; WCET analysis; jitter budget; timing verification.
  - **Verification, Validation, Simulation and HIL Testing** (`008`) — FSW V&V strategy: unit testing, integration testing, SIL, HIL, final functional testing on FM.
  - **ECSS-NASA-CCSDS Software Standards Mapping** (`009`) — standards hierarchy and applicability mapping.
  - **Traceability, Evidence and Lifecycle Governance** (`010`) — FSW requirements traceability; evidence gates; in-orbit anomaly monitoring; lifecycle configuration control.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `140-149` |
| Section | `04` — Aviónica y Control de Misión Espacial |
| Subsection | `142` — Software de Vuelo |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/140-149_Avionica-y-Control-de-Mision-Espacial/142_Software-de-Vuelo/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

[^ecssest40c]: **ECSS-E-ST-40C — Software Engineering** — European standard for spacecraft software development lifecycle and requirements.

[^ecssqst80c]: **ECSS-Q-ST-80C — Software Product Assurance** — Software product assurance requirements for space projects.

[^nasastd87398]: **NASA-STD-8739.8 — Software Assurance Standard** — NASA software assurance requirements.

[^do178c]: **DO-178C — Software Considerations in Airborne Systems and Equipment Certification** — Aviation software standard adapted as reference for space FSW.

### Applicable industry standards

- ECSS-E-ST-40C — Software Engineering[^ecssest40c]
- ECSS-Q-ST-80C — Software Product Assurance[^ecssqst80c]
- DO-178C — Software Considerations in Airborne Systems (adapted)[^do178c]
- NASA-STD-8739.8 — Software Assurance Standard[^nasastd87398]
