---
document_id: QATL-ATLAS-1000-STA-170-179-07-170-000-GENERAL
title: "STA 170-179 · 170-000 — General"
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
subsection: "170"
subsection_title: "Servicing Orbital"
subsubject: "000"
subsubject_title: "General"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-STRUCTURES, Q-INDUSTRY]
orb_function_support: [ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 170-179 · 170-000 — General

## 1. Purpose

Overview entry-point for the *Servicing Orbital* subsection within the `170-179` code range (Section `07` — *Operaciones y Mantenimiento en Órbita*) of the **STA** architecture band.

This subsubject (`000 Overview`) introduces the STA 170-179.170 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the on-orbit servicing framework covering controlled definitions, servicing mission classes and objectives, rendezvous/proximity/servicing boundaries, docking/berthing/capture interfaces, robotic servicing and manipulation functions, refueling/recharging/consumables replenishment, modular replacement and line-replaceable orbital units, servicing safety zones and fault containment, standards mapping, and lifecycle governance. This subsection is designated **on-orbit servicing critical**.

## 2. Scope

- Covers the *Servicing Orbital* slice of the parent code range `170-179`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope across the subsection:
  - **On-Orbit Servicing Controlled Definition** (`001`) — normative boundary of on-orbit servicing within STA; taxonomy, controlled vocabulary, safety classification, and applicability limits.
  - **Servicing Mission Classes and Objectives** (`002`) — taxonomy of servicing mission classes (scheduled, contingency, life-extension, upgrade); objectives per class; mission planning constraints and success criteria.
  - **Rendezvous, Proximity and Servicing Boundaries** (`003`) — rendezvous approach corridor design; proximity operations zones (far approach, intermediate, close approach, berthing envelope); keep-out zones and servicing boundary definitions.
  - **Docking, Berthing and Capture Interfaces** (`004`) — docking interface standards (IDSS, CBM); berthing mechanism requirements; capture tool interfaces; interface control documents; alignment tolerances and force/torque envelopes.
  - **Robotic Servicing and Manipulation Functions** (`005`) — robotic servicing architecture; end-effector taxonomy; manipulator kinematics and workspace; autonomous and teleoperated mode boundaries; payload handling constraints.
  - **Refueling, Recharging and Consumables Replenishment** (`006`) — propellant transfer architectures; fluid coupling interface standards; electrical recharging interfaces; consumables (pressurant, fluids, gases) replenishment; leak detection and safing.
  - **Modular Replacement and Line-Replaceable Orbital Units** (`007`) — LROU taxonomy and design requirements; modular interface standards; replacement sequence control; post-replacement verification requirements.
  - **Servicing Safety Zones and Fault Containment** (`008`) — operational safety zones; collision avoidance volumes; fault containment requirements; abort authority and abort modes; residual risk management.
  - **ECSS-NASA-CCSDS On-Orbit Servicing Standards Mapping** (`009`) — standards hierarchy and applicability matrix for servicing operations.
  - **Traceability, Evidence and Lifecycle Governance** (`010`) — servicing requirements traceability; evidence gates (SRR/PDR/CDR/TRR/ORR); in-orbit monitoring; lifecycle configuration control.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `170-179` |
| Section | `07` — Operaciones y Mantenimiento en Órbita |
| Subsection | `170` — Servicing Orbital |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| ORB support | ORB-LEG |
| Governance class | `baseline`[^gov] |
| Document | `170-000-General.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.
