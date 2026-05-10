---
document_id: QATL-ATLAS-1000-STA-140-149-04-144-000-GENERAL
title: "STA 140-149 · 144-000 — General"
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
subsection: "144"
subsection_title: "Autonomía"
subsubject: "000"
subsubject_title: "General"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 140-149 · 144-000 — General

## 1. Purpose

Overview entry-point for the *Autonomía* subsection within the `140-149` code range (Section `04` — *Aviónica y Control de Misión Espacial*) of the **STA** architecture band.

This subsubject (`000 Overview`) introduces the STA 140-149.144 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the autonomy framework covering controlled definitions, autonomous mode and authority boundaries, onboard decision logic and supervision, FDIR autonomy and contingency response, AI/ML autonomy admission and assurance, human-in-the-loop and ground override interfaces, safe-mode transition and recovery logic, verification/validation/simulation/HIL, standards mapping, and lifecycle governance. This subsection is designated **mission-autonomy critical**.

## 2. Scope

- Covers the *Autonomy* slice of the parent code range `140-149`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope across the subsection:
  - **Autonomy Controlled Definition** (`001`) — normative boundary of autonomy within STA; distinction from flight software (142), GNC algorithms (140), and mission control operations (143).
  - **Autonomous Modes and Authority Boundaries** (`002`) — taxonomy of onboard autonomous modes; authority levels and permissions per mode; transitions between autonomous and ground-controlled modes.
  - **Onboard Decision Logic and Supervision** (`003`) — onboard event-based decision logic; supervision architecture; onboard execution management; state machine design principles.
  - **FDIR Autonomy and Contingency Response** (`004`) — autonomy functions within the FDIR architecture; onboard fault detection, isolation, and autonomous recovery execution; interaction with FSW FDIR (→ `142`).
  - **AI/ML Autonomy Admission and Assurance Boundaries** (`005`) — admission criteria for AI/ML algorithms in autonomous functions; assurance requirements; explainability and determinism constraints; claim discipline.
  - **Human-in-the-Loop and Ground Override Interfaces** (`006`) — human-in-the-loop supervision modes; ground command override authority; real-time inhibit and authority delegation interfaces.
  - **Safe-Mode Transition and Recovery Logic** (`007`) — autonomous safe-mode entry logic; recovery sequences; interaction with flight software safe-mode (→ `142`) and mission control (→ `143`).
  - **Verification, Validation, Simulation and HIL Testing** (`008`) — V&V strategy for autonomous functions: unit testing, integration testing, SIL, HIL, Monte Carlo simulation, edge case testing.
  - **ECSS-NASA Autonomy Standards Mapping** (`009`) — standards hierarchy and applicability mapping.
  - **Traceability, Evidence and Lifecycle Governance** (`010`) — autonomy requirements traceability; evidence gates; AI/ML admission evidence; lifecycle configuration control.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `140-149` |
| Section | `04` — Aviónica y Control de Misión Espacial |
| Subsection | `144` — Autonomía |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/140-149_Avionica-y-Control-de-Mision-Espacial/144_Autonomia/` |
| Document | `144-000-General.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

[^ecssest40c]: **ECSS-E-ST-40C — Software Engineering** — FSW autonomy software development lifecycle and criticality classification standard.

[^nasastd87398]: **NASA-STD-8739.8 — Software Assurance Standard** — NASA software assurance requirements applicable to autonomous functions.

### Applicable industry standards

- ECSS-E-ST-40C — Software Engineering[^ecssest40c]
- NASA-STD-8739.8 — Software Assurance Standard[^nasastd87398]
