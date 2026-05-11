---
document_id: QATL-ATLAS-1000-STA-140-149-04-143-000-GENERAL
title: "STA 140-149 · 143-000 — General"
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
subsection: "143"
subsection_title: "Control de Misión"
subsubject: "000"
subsubject_title: "General"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 140-149 · 143-000 — General

## 1. Purpose

Overview entry-point for the *Control de Misión* subsection within the `140-149` code range (Section `04` — *Aviónica y Control de Misión Espacial*) of the **STA** architecture band.

This subsubject (`000 Overview`) introduces the STA 140-149.143 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the mission control framework covering controlled definitions, ground segment and control centre architecture, command planning/validation/uplink, telemetry reception/monitoring/trending, operations procedures/timelines/flight rules, anomaly response/escalation/contingency, mission operations roles/authority/handover, simulation/rehearsal/operational readiness, standards mapping, and lifecycle governance. This subsection is designated **mission-operations critical**.

## 2. Scope

- Covers the *Mission Control* slice of the parent code range `140-149`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope across the subsection:
  - **Mission Control Controlled Definition** (`001`) — normative boundary of mission control within STA; distinction from flight software (142), GNC algorithms (140), and autonomy functions (144).
  - **Ground Segment and Control Centre Architecture** (`002`) — ground segment decomposition: Mission Control Centre (MCC), Ground Station Network (GSN), mission planning and scheduling systems, data archiving and distribution.
  - **Command Planning, Validation and Uplink Control** (`003`) — command planning workflow; command database management; uplink validation (authentication, authorisation, range safety); command stack management and execution monitoring.
  - **Telemetry Reception, Monitoring and Trending** (`004`) — telemetry reception pipeline; real-time monitoring displays; limit checking and alarm management; telemetry trending, archiving and analysis.
  - **Operations Procedures, Timelines and Flight Rules** (`005`) — operations procedure library; mission timeline development and validation; flight rules and constraints database; on-call and shift management.
  - **Anomaly Response, Escalation and Contingency Control** (`006`) — anomaly detection and classification; response escalation procedures; contingency mode activation; anomaly resolution lifecycle.
  - **Mission Operations Roles, Authority and Handover** (`007`) — roles and responsibilities: Flight Director, Spacecraft Controller, Mission Planner; authority delegation and handover protocols; shift handover procedures.
  - **Simulation, Rehearsal and Operational Readiness Testing** (`008`) — mission simulation environments; operational readiness reviews (ORR); simulation campaigns; lessons-learned integration.
  - **ECSS-NASA-CCSDS Mission Control Standards Mapping** (`009`) — standards hierarchy and applicability mapping.
  - **Traceability, Evidence and Lifecycle Governance** (`010`) — mission control requirements traceability; evidence gates; operations readiness gates; lifecycle configuration control.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `140-149` |
| Section | `04` — Aviónica y Control de Misión Espacial |
| Subsection | `143` — Control de Misión |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/140-149_Avionica-y-Control-de-Mision-Espacial/143_Control-de-Mision/` |
| Document | `143-000-General.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

[^ecssest70c]: **ECSS-E-ST-70C — Ground Systems and Operations** — European standard for spacecraft ground segment and mission control requirements.

[^ccsds505]: **CCSDS 505.0-B-1 — Mission Operations Reference Architecture** — CCSDS reference architecture for mission operations.

[^nasastd87198]: **NASA-STD-8719.8 — Mission Operations Safety** — NASA requirements for mission operations safety assurance.

### Applicable industry standards

- ECSS-E-ST-70C — Ground Systems and Operations[^ecssest70c]
- CCSDS 505.0-B-1 — Mission Operations Reference Architecture[^ccsds505]
- NASA-STD-8719.8 — Mission Operations Safety[^nasastd87198]
