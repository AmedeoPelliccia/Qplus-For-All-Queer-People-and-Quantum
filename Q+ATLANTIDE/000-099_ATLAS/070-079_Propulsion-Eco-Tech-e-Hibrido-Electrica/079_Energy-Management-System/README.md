---
document_id: QATL-ATLAS-1000-ATLAS-070-079-07-079-README
title: "ATLAS 070-079 · 07.079 — Energy Management System (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "070-079"
section: "07"
section_title: "Propulsión Eco-Tech e Híbrido-Eléctrica"
subsection: "079"
subsection_title: "Energy Management System"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HPC, Q-MECHANICS, Q-AIR, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-CSR]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 070-079 · Section 07 · Subsection 079 — Energy Management System

## 1. Purpose

Subsection-level index for *Energy Management System* (`079`) within ATLAS `070-079` — *Propulsión Eco-Tech e Híbrido-Eléctrica*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Reserves the subsubject namespace `00`–`99` of subsection `079` *Energy Management System*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- The Overview and detailed subsubjects (`00`–`99`) will be populated in subsequent baseline releases per the parent section's authorisation.

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 00 | Energy Management System General | [079-000-Energy-Management-System-General.md](./079-000-Energy-Management-System-General.md) | active |
| 10 | Energy Management Architecture | [079-010-Energy-Management-Architecture.md](./079-010-Energy-Management-Architecture.md) | active |
| 20 | Power Demand Prediction and Allocation | [079-020-Power-Demand-Prediction-and-Allocation.md](./079-020-Power-Demand-Prediction-and-Allocation.md) | active |
| 30 | Energy Source Prioritization and Load Shedding | [079-030-Energy-Source-Prioritization-and-Load-Shedding.md](./079-030-Energy-Source-Prioritization-and-Load-Shedding.md) | active |
| 40 | Propulsion and ECS Energy Coordination | [079-040-Propulsion-and-ECS-Energy-Coordination.md](./079-040-Propulsion-and-ECS-Energy-Coordination.md) | active |
| 50 | Energy Degraded Modes and Reconfiguration | [079-050-Energy-Degraded-Modes-and-Reconfiguration.md](./079-050-Energy-Degraded-Modes-and-Reconfiguration.md) | active |
| 60 | Energy Management Software and Configuration | [079-060-Energy-Management-Software-and-Configuration.md](./079-060-Energy-Management-Software-and-Configuration.md) | active |
| 70 | Energy Management Test and Maintenance | [079-070-Energy-Management-Test-and-Maintenance.md](./079-070-Energy-Management-Test-and-Maintenance.md) | active |
| 80 | Energy Management Monitoring, Diagnostics and Control Interfaces | [079-080-Energy-Management-Monitoring-Diagnostics-and-Control-Interfaces.md](./079-080-Energy-Management-Monitoring-Diagnostics-and-Control-Interfaces.md) | active |
| 90 | S1000D CSDB Mapping and Traceability | [079-090-S1000D-CSDB-Mapping-and-Traceability.md](./079-090-S1000D-CSDB-Mapping-and-Traceability.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `070-079` |
| Section | `07` — Propulsión Eco-Tech e Híbrido-Eléctrica |
| Subsection | `079` — Energy Management System |
| Subsubject namespace | `00`–`90` (active) |
| Primary Q-Division | Q-GREENTECH[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-MECHANICS, Q-AIR, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN, ORB-CSR |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/070-079_Propulsion-Eco-Tech-e-Hibrido-Electrica/079_Energy-Management-System/` |
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
