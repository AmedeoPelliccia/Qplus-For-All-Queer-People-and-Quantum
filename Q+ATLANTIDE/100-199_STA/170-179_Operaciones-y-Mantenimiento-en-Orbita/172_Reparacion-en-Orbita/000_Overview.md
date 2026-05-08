---
document_id: QATL-ATLAS-1000-STA-170-179-07-172-000-OVERVIEW
title: "STA 170-179 · 07.172.000 — Overview"
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
subsection: "172"
subsection_title: "Reparación en Órbita"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-STRUCTURES, Q-INDUSTRY, Q-GREENTECH]
orb_function_support: [ORB-LEG]
safety_boundary: "on-orbit repair critical; requires explicit repair admissibility criteria, damage-assessment evidence, robotics safety boundaries, modular-replacement control, abort modes, post-repair verification and lifecycle traceability"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 170-179 · Section 07 · Subsection 172 — Reparación en Órbita

## 1. Purpose

This document is the overview entry-point for the *Reparación en Órbita* (`172`) subsection within STA `170-179` — *Operaciones y Mantenimiento en Órbita*. It introduces the on-orbit repair framework established across subsubjects `001`–`010` and provides a consolidated navigation guide for all controlled repair topics within this subsection.

This subsection is designated **on-orbit repair critical**[^baseline][^n001]: all repair operations require explicit repair admissibility criteria, damage-assessment evidence, robotics safety boundaries, modular-replacement control, defined abort modes, post-repair verification, and end-to-end lifecycle traceability. All documents within this subsection are part of the **ATLAS-1000** register under the controlled **Q+ATLANTIDE** baseline.

## 2. Scope

The following bullets summarise the content covered by each active subsubject in subsection `172`:

- **001 — On-Orbit Repair Controlled Definition**: Establishes the normative definition and controlled taxonomy of on-orbit repair. Defines the applicability boundary (repair vs. inspection `171`, new assembly `173`, preventive servicing `170`), the repair-type taxonomy (structural, thermal protection, avionics/electrical, pressurized system, payload), controlled vocabulary (Damage Assessment Record, Repair Admissibility Decision, Repair Evidence Package, Repair Procedure, Post-Repair Verification Report), and the safety classification basis per ECSS-E-ST-32C and NASA-STD-5009.

- **002 — Repair Mission Classes and Objectives**: Defines five on-orbit repair mission classes — Class R1 (Emergency Structural Repair), Class R2 (Thermal Protection Repair), Class R3 (Avionics/Electrical Repair), Class R4 (Pressurized System Repair), and Class R5 (Payload Repair) — together with their objectives, planning constraints (orbital mechanics, time budget, consumables), success criteria, abort criteria, and mission authorization requirements.

- **003 — Damage Assessment and Repair Admissibility**: Defines the damage assessment methodology using inspection data from `171`, damage classification (Minor / Moderate / Severe / Critical), residual strength and fracture mechanics analysis per ECSS-E-ST-32-01C and NASA-STD-5009, repair admissibility criteria and explicit non-admissibility conditions, procedure selection, and the formal admissibility decision authority hierarchy.

- **004 — Robotic Repair and Manipulation Functions**: Specifies the robotic repair architecture including 7-DOF manipulator configuration, force/torque-controlled manipulation requirements, end-effector taxonomy for repair operations, teleoperation versus supervised-autonomy mode boundaries, repair workspace management using 3D models updated from inspection data, and mid-repair fault management.

- **005 — Modular Replacement and Orbital LRU Exchange**: Establishes requirements for line-replaceable orbital unit (LROU) exchange as the primary repair strategy for avionics, payload, and subsystem units triggered by functional failure. Covers failure diagnosis, replacement authorization, interface damage assessment, compatibility and configuration control, stowage and waste management for replaced units, and post-replacement verification.

- **006 — Structural Patch, Bonding and Sealing Concepts**: Defines structural patch repair concepts (rigid, flexible, pressure boundary), bonding agent requirements for the space environment (thermal cycling, vacuum outgassing, radiation, cure process), sealing concepts for pressure boundaries including proof-test requirements, surface preparation, cure process control, and post-repair non-destructive inspection and structural verification.

- **007 — Electrical, Avionics and Payload Repair Interfaces**: Defines repair interface requirements for electrical systems, avionics units, and payload instruments. Covers power isolation and safing procedures, connector and harness repair concepts, avionics LRU exchange interfaces, payload instrument repair and calibration, ESD control requirements adapted for EVA/robotic operations, and post-repair electrical functional verification.

- **008 — Repair Safety Zones, Fault Containment and Abort Modes**: Defines repair operational safety zones (Repair Work Zone, Adjacent Structure Exclusion Zone, Free-Flyer Inspection Zone, Safety Cordon), hazardous material containment for bonding agents and solvents, single-fault tolerance requirements for robotic repair systems, three-tier abort mode architecture (R1 Pause-Hold / R2 Safe-Partial-Repair / R3 Abandon-Repair), post-repair residual risk, and safety evidence documentation.

- **009 — ECSS-NASA-CCSDS On-Orbit Repair Standards Mapping**: Maps all applicable ECSS (ECSS-E-ST-32C, ECSS-E-ST-32-01C, ECSS-Q-ST-70C, ECSS-E-ST-10-04C, ECSS-E-ST-10-03C), NASA (NASA-STD-5009, NASA-STD-3000, NASA-HDBK-1001, NASA-STD-6016), and CCSDS standards to the functional repair areas within subsection `172`. Provides a standards applicability matrix and standards evolution monitoring process.

- **010 — Traceability, Evidence and Lifecycle Governance**: Establishes bidirectional requirements traceability from mission/system/safety/structural requirements through repair functions to evidence artefacts, evidence gates at lifecycle milestones (SRR through ORR and pre-repair), in-orbit repair event logging and post-repair SHM monitoring, and lifecycle configuration control for repair procedures, Damage Assessment Records, Repair Authorization Records, and Repair Evidence Packages.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `170-179` |
| Section | `07` — Operaciones y Mantenimiento en Órbita |
| Subsection | `172` — Reparación en Órbita |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-STRUCTURES, Q-INDUSTRY, Q-GREENTECH |
| ORB support | ORB-LEG |
| Governance class | `baseline`[^gov] |
| Safety boundary | on-orbit repair critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/170-179_Operaciones-y-Mantenimiento-en-Orbita/172_Reparacion-en-Orbita/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
