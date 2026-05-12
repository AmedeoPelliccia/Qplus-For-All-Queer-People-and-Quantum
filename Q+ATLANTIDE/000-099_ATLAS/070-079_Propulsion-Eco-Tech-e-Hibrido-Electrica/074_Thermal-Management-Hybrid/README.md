---
document_id: QATL-ATLAS-1000-ATLAS-070-079-07-074-README
title: "ATLAS 070-079 · 07.074 — Thermal Management — Hybrid (Subsection Index)"
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
subsection: "074"
subsection_title: "Thermal Management — Hybrid"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HPC, Q-MECHANICS, Q-AIR, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-CSR]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 070-079 · Section 07 · Subsection 074 — Thermal Management — Hybrid

## 1. Purpose

Subsection-level index for *Thermal Management — Hybrid* (`074`) within ATLAS `070-079` — *Propulsión Eco-Tech e Híbrido-Eléctrica*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Populates the subsubject namespace `00`–`99` of subsection `074` *Thermal Management — Hybrid* with ten subsubject documents covering general overview, propulsion thermal architecture, liquid cooling loops and pumps, heat exchangers and cold plates, motor/inverter/battery cooling interfaces, thermal control valves and regulation, overtemperature and fire-zone thermal isolation, thermal system service and maintenance, monitoring/diagnostics/control interfaces, and S1000D / CSDB mapping.

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 00 | Thermal Management Hybrid General | [074-000-Thermal-Management-Hybrid-General.md](./074-000-Thermal-Management-Hybrid-General.md) | active |
| 10 | Propulsion Thermal Architecture | [074-010-Propulsion-Thermal-Architecture.md](./074-010-Propulsion-Thermal-Architecture.md) | active |
| 20 | Liquid Cooling Loops and Pumps | [074-020-Liquid-Cooling-Loops-and-Pumps.md](./074-020-Liquid-Cooling-Loops-and-Pumps.md) | active |
| 30 | Heat Exchangers Cold Plates and Radiators | [074-030-Heat-Exchangers-Cold-Plates-and-Radiators.md](./074-030-Heat-Exchangers-Cold-Plates-and-Radiators.md) | active |
| 40 | Motor Inverter and Battery Cooling Interfaces | [074-040-Motor-Inverter-and-Battery-Cooling-Interfaces.md](./074-040-Motor-Inverter-and-Battery-Cooling-Interfaces.md) | active |
| 50 | Thermal Control Valves and Regulation | [074-050-Thermal-Control-Valves-and-Regulation.md](./074-050-Thermal-Control-Valves-and-Regulation.md) | active |
| 60 | Overtemperature and Fire Zone Thermal Isolation | [074-060-Overtemperature-and-Fire-Zone-Thermal-Isolation.md](./074-060-Overtemperature-and-Fire-Zone-Thermal-Isolation.md) | active |
| 70 | Thermal System Service and Maintenance | [074-070-Thermal-System-Service-and-Maintenance.md](./074-070-Thermal-System-Service-and-Maintenance.md) | active |
| 80 | Thermal Management Monitoring Diagnostics and Control Interfaces | [074-080-Thermal-Management-Monitoring-Diagnostics-and-Control-Interfaces.md](./074-080-Thermal-Management-Monitoring-Diagnostics-and-Control-Interfaces.md) | active |
| 90 | S1000D / CSDB Mapping and Traceability | [074-090-S1000D-CSDB-Mapping-and-Traceability.md](./074-090-S1000D-CSDB-Mapping-and-Traceability.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `070-079` |
| Section | `07` — Propulsión Eco-Tech e Híbrido-Eléctrica |
| Subsection | `074` — Thermal Management — Hybrid |
| Subsubject namespace | `00`–`99` (active) |
| Primary Q-Division | Q-GREENTECH[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-MECHANICS, Q-AIR, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN, ORB-CSR |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/070-079_Propulsion-Eco-Tech-e-Hibrido-Electrica/074_Thermal-Management-Hybrid/` |
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
