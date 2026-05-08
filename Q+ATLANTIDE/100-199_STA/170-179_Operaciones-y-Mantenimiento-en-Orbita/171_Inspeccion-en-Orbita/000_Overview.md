---
document_id: QATL-ATLAS-1000-STA-170-179-07-171-000-OVERVIEW
title: "STA 170-179 · 07.171.000 — Overview"
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
subsection: "171"
subsection_title: "Inspección en Órbita"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-STRUCTURES, Q-INDUSTRY]
orb_function_support: [ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 170-179 · Section 07 · Subsection 171 — Inspección en Órbita

## 1. Purpose

Overview entry-point for the *Inspección en Órbita* subsection within the `170-179` code range (Section `07` — *Operaciones y Mantenimiento en Órbita*) of the **STA** architecture band.

This subsubject (`000 Overview`) introduces the STA 170-179.171 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the on-orbit inspection framework covering controlled definitions, inspection mission classes and objectives, visual/optical/multispectral inspection, radar/lidar/proximity sensing inspection, structural health monitoring and damage assessment, thermal/radiation/surface degradation inspection, autonomous and robotic inspection modes, inspection safety zones and proximity operations, standards mapping, and lifecycle governance. This subsection is designated **on-orbit inspection critical**.

## 2. Scope

- Covers the *Inspección en Órbita* slice of the parent code range `170-179`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope across the subsection:
  - **On-Orbit Inspection Controlled Definition** (`001`) — normative boundary of on-orbit inspection within STA; taxonomy, controlled vocabulary, safety classification, and applicability limits.
  - **Inspection Mission Classes and Objectives** (`002`) — taxonomy of inspection mission classes (routine, contingency, pre-/post-servicing, monitoring); objectives per class; mission planning constraints and success criteria.
  - **Visual, Optical and Multispectral Inspection** (`003`) — visible-spectrum camera systems, optical inspection techniques, multispectral imaging for surface degradation detection; resolution requirements; illumination constraints.
  - **Radar, Lidar and Proximity Sensing Inspection** (`004`) — radar reflectometry for structural assessment; lidar-based 3D mapping; proximity sensor fusion for inspection data quality; range and resolution requirements.
  - **Structural Health Monitoring and Damage Assessment** (`005`) — in-situ structural health monitoring sensors; damage detection algorithms; impact detection and characterization; damage assessment decision logic linked to repair trigger criteria.
  - **Thermal, Radiation and Surface Degradation Inspection** (`006`) — infrared thermal imaging; radiation dose mapping; micrometeorite and debris impact detection; surface coating degradation assessment.
  - **Autonomous Inspection and Robotic Inspection Modes** (`007`) — autonomous inspection trajectory planning; robotic inspection platform integration; human-in-the-loop boundaries; inspection coverage verification.
  - **Inspection Safety Zones and Proximity Operations** (`008`) — inspection approach corridors; safety zones during fly-around and close proximity inspection; abort triggers and collision avoidance.
  - **ECSS-NASA-CCSDS On-Orbit Inspection Standards Mapping** (`009`) — standards hierarchy and applicability matrix.
  - **Traceability, Evidence and Lifecycle Governance** (`010`) — inspection requirements traceability; evidence gates; data quality evidence; lifecycle configuration control.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `170-179` |
| Section | `07` — Operaciones y Mantenimiento en Órbita |
| Subsection | `171` — Inspección en Órbita |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-LEG |
| Governance class | `baseline`[^gov] |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.
