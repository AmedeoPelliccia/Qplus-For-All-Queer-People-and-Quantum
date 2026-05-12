---
document_id: QATL-ATLAS-1000-ATLAS-080-089-08-082-README
title: "ATLAS 080-089 · 08.082 — Plasma and Ionic Propulsion Concepts (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "080-089"
section: "08"
section_title: "Propulsión Alternativa & Cuántica"
subsection: "082"
subsection_title: "Plasma and Ionic Propulsion Concepts"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HORIZON, Q-HPC, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 080-089 · Section 08 · Subsection 082 — Plasma and Ionic Propulsion Concepts

## 1. Purpose

Subsection-level index for *Plasma and Ionic Propulsion Concepts* (`082`) within ATLAS `080-089` — *Propulsión Alternativa & Cuántica* — Research horizon.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Populates the subsubject namespace `00`–`99` of subsection `082` *Plasma and Ionic Propulsion Concepts*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- All ten subsubjects (`00`–`90`) are active DRAFT documents covering the AMPEL360E eWTW Plasma and Ionic Propulsion Concepts system (PPPU dual-channel DAL C, 8 thruster nodes: 4 HET + 4 GIE, xenon propellant, DBD plasma actuators, Hall-effect and gridded ion engine physics, high-voltage interfaces, plume interaction and EMC constraints, AFDX ARINC 664 P7, S1000D 28 DMs, BREX-082-v1).

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 00 | Plasma and Ionic Propulsion Concepts — General | [082-000-Plasma-and-Ionic-Propulsion-Concepts-General.md](./082-000-Plasma-and-Ionic-Propulsion-Concepts-General.md) | active |
| 10 | Plasma Propulsion Baseline and Scope | [082-010-Plasma-Propulsion-Baseline-and-Scope.md](./082-010-Plasma-Propulsion-Baseline-and-Scope.md) | active |
| 20 | Ionic Propulsion Concepts and Operating Principles | [082-020-Ionic-Propulsion-Concepts-and-Operating-Principles.md](./082-020-Ionic-Propulsion-Concepts-and-Operating-Principles.md) | active |
| 30 | Electric Field and Magnetic Field Acceleration Mechanisms | [082-030-Electric-Field-and-Magnetic-Field-Acceleration-Mechanisms.md](./082-030-Electric-Field-and-Magnetic-Field-Acceleration-Mechanisms.md) | active |
| 40 | Propellant Ionization and Plasma Generation | [082-040-Propellant-Ionization-and-Plasma-Generation.md](./082-040-Propellant-Ionization-and-Plasma-Generation.md) | active |
| 50 | Thruster Chamber, Grid and Electrode Interfaces | [082-050-Thruster-Chamber-Grid-and-Electrode-Interfaces.md](./082-050-Thruster-Chamber-Grid-and-Electrode-Interfaces.md) | active |
| 60 | Power Processing and High-Voltage Interfaces | [082-060-Power-Processing-and-High-Voltage-Interfaces.md](./082-060-Power-Processing-and-High-Voltage-Interfaces.md) | active |
| 70 | Thermal, EMC and Plume Interaction Constraints | [082-070-Thermal-EMC-and-Plume-Interaction-Constraints.md](./082-070-Thermal-EMC-and-Plume-Interaction-Constraints.md) | active |
| 80 | Plasma/Ionic Monitoring, Diagnostics and Control Interfaces | [082-080-Plasma-Ionic-Monitoring-Diagnostics-and-Control-Interfaces.md](./082-080-Plasma-Ionic-Monitoring-Diagnostics-and-Control-Interfaces.md) | active |
| 90 | S1000D / CSDB Mapping and Traceability | [082-090-S1000D-CSDB-Mapping-and-Traceability.md](./082-090-S1000D-CSDB-Mapping-and-Traceability.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `080-089` |
| Section | `08` — Propulsión Alternativa & Cuántica |
| Subsection | `082` — Plasma and Ionic Propulsion Concepts |
| Subsubject namespace | `00`–`99` (active) |
| Primary Q-Division | Q-GREENTECH[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-HPC, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-LEG, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/080-089_Propulsion-Alternativa-y-Cuantica/082_Plasma-and-Ionic-Propulsion-Concepts/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-GREENTECH` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `00`–`99` shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
