---
document_id: QATL-ATLAS-1000-ATLAS-080-089-08-085-README
title: "ATLAS 080-089 · 08.085 — Distributed Electric Propulsion Architecture (Subsection Index)"
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
subsection: "085"
subsection_title: "Distributed Electric Propulsion Architecture"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HORIZON, Q-HPC, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 080-089 · Section 08 · Subsection 085 — Distributed Electric Propulsion Architecture

## 1. Purpose

Subsection-level index for *Distributed Electric Propulsion Architecture* (`085`) within ATLAS `080-089` — *Propulsión Alternativa & Cuántica*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Populates the subsubject namespace `00`–`09` of subsection `085` *Distributed Electric Propulsion Architecture* with ten active baseline documents.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- All ten subsubjects (085-000 through 085-090) are now at `active` / `DRAFT` status per BREX-085-v1; 30 Data Modules in DMRL.

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 00 | Distributed Electric Propulsion Architecture — General | [085-000-Distributed-Electric-Propulsion-Architecture-General.md](085-000-Distributed-Electric-Propulsion-Architecture-General.md) | active |
| 01 | DEP Baseline and Scope | [085-010-DEP-Baseline-and-Scope.md](085-010-DEP-Baseline-and-Scope.md) | active |
| 02 | Distributed Propulsor Layout and Topology | [085-020-Distributed-Propulsor-Layout-and-Topology.md](085-020-Distributed-Propulsor-Layout-and-Topology.md) | active |
| 03 | Electric Motor and Drive Allocation | [085-030-Electric-Motor-and-Drive-Allocation.md](085-030-Electric-Motor-and-Drive-Allocation.md) | active |
| 04 | Power Distribution and Energy Management Interfaces | [085-040-Power-Distribution-and-Energy-Management-Interfaces.md](085-040-Power-Distribution-and-Energy-Management-Interfaces.md) | active |
| 05 | Propulsor Airframe Integration and Aero-Propulsive Coupling | [085-050-Propulsor-Airframe-Integration-and-Aero-Propulsive-Coupling.md](085-050-Propulsor-Airframe-Integration-and-Aero-Propulsive-Coupling.md) | active |
| 06 | Redundancy Fault Tolerance and Degraded Modes | [085-060-Redundancy-Fault-Tolerance-and-Degraded-Modes.md](085-060-Redundancy-Fault-Tolerance-and-Degraded-Modes.md) | active |
| 07 | Thermal EMC and Structural Integration Constraints | [085-070-Thermal-EMC-and-Structural-Integration-Constraints.md](085-070-Thermal-EMC-and-Structural-Integration-Constraints.md) | active |
| 08 | DEP Monitoring Diagnostics and Control Interfaces | [085-080-DEP-Monitoring-Diagnostics-and-Control-Interfaces.md](085-080-DEP-Monitoring-Diagnostics-and-Control-Interfaces.md) | active |
| 09 | S1000D CSDB Mapping and Traceability | [085-090-S1000D-CSDB-Mapping-and-Traceability.md](085-090-S1000D-CSDB-Mapping-and-Traceability.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `080-089` |
| Section | `08` — Propulsión Alternativa & Cuántica |
| Subsection | `085` — Distributed Electric Propulsion Architecture |
| Subsubject namespace | `00`–`09` (active; 10 documents) |
| Primary Q-Division | Q-GREENTECH[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-HPC, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-LEG, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/080-089_Propulsion-Alternativa-y-Cuantica/085_Distributed-Electric-Propulsion-Architecture/` |
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
