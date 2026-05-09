---
document_id: QATL-ATLAS-1000-STA-140-149-04-141-000-GENERAL
title: "STA 140-149 · 141-000 — General"
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
subsection: "141"
subsection_title: "Aviónica Espacial"
subsubject: "000"
subsubject_title: "General"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 140-149 · 141-000 — General

## 1. Purpose

Overview entry-point for the *Aviónica Espacial* subsection within the `140-149` code range (Section `04` — *Aviónica y Control de Misión Espacial*) of the **STA** architecture band.

This subsubject (`000 Overview`) introduces the STA 140-149.141 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the space avionics framework covering controlled definitions, onboard computer and data handling architecture, command/telemetry interfaces, sensor/actuator/payload avionics interfaces, time synchronization and data bus architecture, redundancy and fault tolerance, radiation hardening, EMC/thermal/power interfaces, standards mapping, and lifecycle governance. This subsection is designated **mission-avionics critical**.

## 2. Scope

- Covers the *Space Avionics* slice of the parent code range `140-149`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope across the subsection:
  - **Space Avionics Controlled Definition** (`001`) — normative boundary of space avionics within STA; distinction from GNC (140), flight software (142), and mission control (143).
  - **Onboard Computer and Data Handling Architecture** (`002`) — processor selection, memory hierarchy, EDAC; centralized vs distributed data handling; processor redundancy.
  - **Command and Telemetry Interfaces** (`003`) — TC/TM protocol stack (CCSDS PUS), uplink/downlink data rates, on-board parameter management, command authentication.
  - **Sensor, Actuator and Payload Avionics Interfaces** (`004`) — interface definition for sensors, actuators, and payload equipment; interface control documents (ICDs).
  - **Time Synchronization and Data Bus Architecture** (`005`) — OBCT, GPS-derived time, synchronization protocols, SpaceWire/MIL-STD-1553/CAN bus topologies, bandwidth budgets.
  - **Redundancy, Fault Tolerance and Safe-Mode Support** (`006`) — cold/warm/hot redundancy for OBC, voting logic, watchdog timers, autonomous safe-mode transition triggers.
  - **Radiation Hardening and Single Event Effects** (`007`) — TID budget, SEE mitigation techniques, radiation-hardened vs COTS-with-mitigation selection.
  - **EMC, Thermal and Power Interface Boundaries** (`008`) — EMC design rules, thermal dissipation boundaries, power consumption budget and interface with subsystem 133.
  - **ECSS-NASA-CCSDS Avionics Standards Mapping** (`009`) — standards hierarchy and applicability mapping.
  - **Traceability, Evidence and Lifecycle Governance** (`010`) — requirements traceability, evidence gates, in-orbit health monitoring, lifecycle records.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `140-149` |
| Section | `04` — Aviónica y Control de Misión Espacial |
| Subsection | `141` — Aviónica Espacial |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/140-149_Avionica-y-Control-de-Mision-Espacial/141_Avionica-Espacial/` |
| Document | `141-000-General.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

[^ecssest50c]: **ECSS-E-ST-50C — Communications** — European standard for spacecraft on-board data handling and communications.

[^milstd1553b]: **MIL-STD-1553B — Digital Time Division Command/Response Multiplex Data Bus** — Military standard for avionics data bus.

[^ccsds7320b3]: **CCSDS 732.0-B-3 — AOS Space Data Link Protocol** — CCSDS standard for advanced orbiting systems data link protocol.

### Applicable industry standards

- ECSS-E-ST-50C — Communications[^ecssest50c]
- ECSS-E-ST-50-12C — SpaceWire — Links, nodes, routers and networks
- MIL-STD-1553B — Digital Time Division Command/Response Multiplex Data Bus[^milstd1553b]
- CCSDS 732.0-B-3 — AOS Space Data Link Protocol[^ccsds7320b3]
