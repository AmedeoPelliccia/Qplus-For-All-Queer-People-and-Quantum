---
document_id: QATL-ATLAS-1000-ATLAS-080-089-08-084-README
title: "ATLAS 080-089 · 08.084 — Hybrid Architectures — Beyond Gen-2 (Subsection Index)"
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
subsection: "084"
subsection_title: "Hybrid Architectures — Beyond Gen-2"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HORIZON, Q-HPC, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 080-089 · Section 08 · Subsection 084 — Hybrid Architectures — Beyond Gen-2

## 1. Purpose

Subsection-level index for *Hybrid Architectures — Beyond Gen-2* (`084`) within ATLAS `080-089` — *Propulsión Alternativa & Cuántica* — Post-2040.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Reserves the subsubject namespace `00`–`99` of subsection `084` *Hybrid Architectures — Beyond Gen-2*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- The Overview and all detailed subsubjects (`00`–`90`) have been populated in the current baseline release.

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 00 | Hybrid Architectures Beyond Gen-2 — General | [084-000-Hybrid-Architectures-Beyond-Gen-2-General.md](084-000-Hybrid-Architectures-Beyond-Gen-2-General.md) | active |
| 10 | Beyond-Gen-2 Baseline and Scope | [084-010-Beyond-Gen-2-Baseline-and-Scope.md](084-010-Beyond-Gen-2-Baseline-and-Scope.md) | active |
| 20 | Advanced Hybrid Propulsion Topology | [084-020-Advanced-Hybrid-Propulsion-Topology.md](084-020-Advanced-Hybrid-Propulsion-Topology.md) | active |
| 30 | Multi-Source Energy Architecture | [084-030-Multi-Source-Energy-Architecture.md](084-030-Multi-Source-Energy-Architecture.md) | active |
| 40 | Fuel-Cell Battery Turbine and Advanced Source Coupling | [084-040-Fuel-Cell-Battery-Turbine-and-Advanced-Source-Coupling.md](084-040-Fuel-Cell-Battery-Turbine-and-Advanced-Source-Coupling.md) | active |
| 50 | Hybrid Propulsion Control and Mode Management | [084-050-Hybrid-Propulsion-Control-and-Mode-Management.md](084-050-Hybrid-Propulsion-Control-and-Mode-Management.md) | active |
| 60 | Degraded Modes Redundancy and Reconfiguration | [084-060-Degraded-Modes-Redundancy-and-Reconfiguration.md](084-060-Degraded-Modes-Redundancy-and-Reconfiguration.md) | active |
| 70 | Airframe Integration Thermal and Safety Constraints | [084-070-Airframe-Integration-Thermal-and-Safety-Constraints.md](084-070-Airframe-Integration-Thermal-and-Safety-Constraints.md) | active |
| 80 | Beyond-Gen-2 Monitoring Diagnostics and Control Interfaces | [084-080-Beyond-Gen-2-Monitoring-Diagnostics-and-Control-Interfaces.md](084-080-Beyond-Gen-2-Monitoring-Diagnostics-and-Control-Interfaces.md) | active |
| 90 | S1000D CSDB Mapping and Traceability | [084-090-S1000D-CSDB-Mapping-and-Traceability.md](084-090-S1000D-CSDB-Mapping-and-Traceability.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `080-089` |
| Section | `08` — Propulsión Alternativa & Cuántica |
| Subsection | `084` — Hybrid Architectures — Beyond Gen-2 |
| Subsubject namespace | `00`–`99` (reserved) |
| Primary Q-Division | Q-GREENTECH[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-HPC, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-LEG, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/080-089_Propulsion-Alternativa-y-Cuantica/084_Hybrid-Architectures-Beyond-Gen-2/` |
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
