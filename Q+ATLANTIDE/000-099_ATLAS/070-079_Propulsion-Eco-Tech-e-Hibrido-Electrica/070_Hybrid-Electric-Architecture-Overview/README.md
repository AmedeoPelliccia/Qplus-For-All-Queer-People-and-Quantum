---
document_id: QATL-ATLAS-1000-ATLAS-070-079-07-070-README
title: "ATLAS 070-079 · 07.070 — Hybrid-Electric Architecture Overview (Subsection Index)"
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
subsection: "070"
subsection_title: "Hybrid-Electric Architecture Overview"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HPC, Q-MECHANICS, Q-AIR, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-CSR]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 070-079 · Section 07 · Subsection 070 — Hybrid-Electric Architecture Overview

## 1. Purpose

Subsection-level index for *Hybrid-Electric Architecture Overview* (`070`) within ATLAS `070-079` — *Propulsión Eco-Tech e Híbrido-Eléctrica* — Programme-specific.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Reserves the subsubject namespace `00`–`99` of subsection `070` *Hybrid-Electric Architecture Overview*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- The Overview and detailed subsubjects (`00`–`99`) will be populated in subsequent baseline releases per the parent section's authorisation.

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 00 | Hybrid-Electric Architecture Overview — General | [070-000](./070-000-Hybrid-Electric-Architecture-Overview-General.md) | active |
| 10 | Propulsion System Topology | [070-010](./070-010-Propulsion-System-Topology.md) | active |
| 20 | Electric and Thermal Propulsion Allocation | [070-020](./070-020-Electric-and-Thermal-Propulsion-Allocation.md) | active |
| 30 | Hybrid-Electric Operating Modes | [070-030](./070-030-Hybrid-Electric-Operating-Modes.md) | active |
| 40 | Propulsion Redundancy and Degraded Modes | [070-040](./070-040-Propulsion-Redundancy-and-Degraded-Modes.md) | active |
| 50 | Propulsion Energy Flow Architecture | [070-050](./070-050-Propulsion-Energy-Flow-Architecture.md) | active |
| 60 | Propulsion Safety and Isolation Zones | [070-060](./070-060-Propulsion-Safety-and-Isolation-Zones.md) | active |
| 70 | Propulsion Integration and Airframe Interfaces | [070-070](./070-070-Propulsion-Integration-and-Airframe-Interfaces.md) | active |
| 80 | Hybrid-Electric Monitoring, Diagnostics and Control Interfaces | [070-080](./070-080-Hybrid-Electric-Monitoring-Diagnostics-and-Control-Interfaces.md) | active |
| 90 | S1000D / CSDB Mapping and Traceability | [070-090](./070-090-S1000D-CSDB-Mapping-and-Traceability.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `070-079` |
| Section | `07` — Propulsión Eco-Tech e Híbrido-Eléctrica |
| Subsection | `070` — Hybrid-Electric Architecture Overview |
| Subsubject namespace | `00`–`99` (10 subsubjects populated) |
| Primary Q-Division | Q-GREENTECH[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-MECHANICS, Q-AIR, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN, ORB-CSR |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/070-079_Propulsion-Eco-Tech-e-Hibrido-Electrica/070_Hybrid-Electric-Architecture-Overview/` |
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
