---
document_id: QATL-ATLAS-1000-STA-170-179-07-173-000-GENERAL
title: "STA 170-179 · 173-000 — General"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "170-179"
section: "07"
section_title: "Operaciones y Mantenimiento en Órbita"
subsection: "173"
subsection_title: "Ensamblaje en Órbita"
subsubject: "000"
subsubject_title: "General"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-STRUCTURES, Q-INDUSTRY, Q-GREENTECH]
orb_function_support: [ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 170-179 · 173-000 — General

## 1. Purpose

Overview entry-point for the *Ensamblaje en Órbita* subsection within the `170-179` code range (Section `07` — *Operaciones y Mantenimiento en Órbita*) of the **STA** architecture band.

This subsubject (`000 Overview`) introduces the STA 170-179.173 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the on-orbit assembly framework covering controlled definitions, assembly mission classes and objectives, modular architecture and assembly units, rendezvous/docking/berthing/positioning interfaces, robotic assembly and manipulation functions, structural joining/latching/lockdown mechanisms, power/data/thermal/fluid interface integration, assembly safety zones and fault containment/abort modes, standards mapping, and lifecycle governance. This subsection is designated **on-orbit assembly critical**.

## 2. Scope

- Covers the *Ensamblaje en Órbita* slice of the parent code range `170-179`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope across the subsection:
  - **On-Orbit Assembly Controlled Definition** (`001`) — normative boundary of on-orbit assembly within STA; taxonomy, controlled vocabulary, safety classification, and applicability limits.
  - **Assembly Mission Classes and Objectives** (`002`) — taxonomy of assembly mission classes (incremental modular assembly, large structure assembly, infrastructure deployment); objectives per class; mission planning constraints and success criteria.
  - **Modular Architecture and Assembly Units** (`003`) — modular system decomposition; assembly unit design requirements; interface standardization; assembly sequence planning; compatibility matrix.
  - **Rendezvous, Docking, Berthing and Positioning Interfaces** (`004`) — approach corridors for assembly elements; docking/berthing interface standards for assembly; positioning and alignment requirements; interface control documents.
  - **Robotic Assembly and Manipulation Functions** (`005`) — robotic assembly system architecture; manipulator configuration for assembly tasks; end-effector taxonomy; teleoperated and supervised autonomous mode boundaries.
  - **Structural Joining, Latching and Lockdown Mechanisms** (`006`) — joining mechanism taxonomy; latch design requirements; lockdown verification; structural margin after joining; load transfer verification.
  - **Power, Data, Thermal and Fluid Interface Integration** (`007`) — multi-domain interface activation sequence post-joining; power interface connection and verification; data network integration; thermal interface connection; fluid circuit integration.
  - **Assembly Safety Zones, Fault Containment and Abort Modes** (`008`) — operational safety zones; collision avoidance during assembly; fault containment requirements; abort modes per assembly phase.
  - **ECSS-NASA-CCSDS On-Orbit Assembly Standards Mapping** (`009`) — standards hierarchy and applicability matrix.
  - **Traceability, Evidence and Lifecycle Governance** (`010`) — assembly requirements traceability; evidence gates; in-orbit monitoring; lifecycle configuration control.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `170-179` |
| Section | `07` — Operaciones y Mantenimiento en Órbita |
| Subsection | `173` — Ensamblaje en Órbita |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| ORB support | ORB-LEG |
| Governance class | `baseline`[^gov] |
| Document | `173-000-General.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.
