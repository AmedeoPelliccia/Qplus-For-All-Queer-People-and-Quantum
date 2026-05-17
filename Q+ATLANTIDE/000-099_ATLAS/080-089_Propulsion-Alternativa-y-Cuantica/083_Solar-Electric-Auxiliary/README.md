---
document_id: QATL-ATLAS-1000-ATLAS-080-089-08-083-README
title: "ATLAS 080-089 · 08.083 — Solar-Electric Auxiliary (Subsection Index)"
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
subsection: "083"
subsection_title: "Solar-Electric Auxiliary"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HORIZON, Q-HPC, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
standard_scope: agnostic
programme_specific: false
---

# ATLAS 080-089 · Section 08 · Subsection 083 — Solar-Electric Auxiliary

## 1. Purpose

Subsection-level index for *Solar-Electric Auxiliary* (`083`) within ATLAS `080-089` — *Propulsión Alternativa & Cuántica* — UAM / long-endurance.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Populates the subsubject namespace `00`–`99` of subsection `083` *Solar-Electric Auxiliary*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- All ten subsubjects (`00`–`90`) are active DRAFT documents covering the programme-defined aircraft type Solar-Electric Auxiliary (SEA) system: 24 m² GaAs triple-junction PV arrays (120 kW peak), dual-tier energy storage (100 kJ SCAP + 50 kWh <BATTERY-CHEMISTRY> Li-Ion), SEACU dual-channel DAL C controller, 2–4 BLI auxiliary propulsor nodes (15–40 kW each), AFDX ARINC 664 P7, S1000D 30 DMs, BREX-083-v1.

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 000 | Solar-Electric Auxiliary — General | [083-000-Solar-Electric-Auxiliary-General.md](083-000-Solar-Electric-Auxiliary-General.md) | active |
| 010 | Solar-Electric Auxiliary Baseline and Scope | [083-010-Solar-Electric-Auxiliary-Baseline-and-Scope.md](083-010-Solar-Electric-Auxiliary-Baseline-and-Scope.md) | active |
| 020 | Solar Array Integration for Auxiliary Propulsion | [083-020-Solar-Array-Integration-for-Auxiliary-Propulsion.md](083-020-Solar-Array-Integration-for-Auxiliary-Propulsion.md) | active |
| 030 | Energy Storage and Buffering for Auxiliary Use | [083-030-Energy-Storage-and-Buffering-for-Auxiliary-Use.md](083-030-Energy-Storage-and-Buffering-for-Auxiliary-Use.md) | active |
| 040 | Power Conditioning and Distribution Interfaces | [083-040-Power-Conditioning-and-Distribution-Interfaces.md](083-040-Power-Conditioning-and-Distribution-Interfaces.md) | active |
| 050 | Auxiliary Electric Propulsor Concepts | [083-050-Auxiliary-Electric-Propulsor-Concepts.md](083-050-Auxiliary-Electric-Propulsor-Concepts.md) | active |
| 060 | Emergency and Degraded Mode Auxiliary Power | [083-060-Emergency-and-Degraded-Mode-Auxiliary-Power.md](083-060-Emergency-and-Degraded-Mode-Auxiliary-Power.md) | active |
| 070 | Airframe Integration, Thermal and Structural Constraints | [083-070-Airframe-Integration-Thermal-and-Structural-Constraints.md](083-070-Airframe-Integration-Thermal-and-Structural-Constraints.md) | active |
| 080 | Solar-Electric Auxiliary — Monitoring, Diagnostics and Control Interfaces | [083-080-Solar-Electric-Auxiliary-Monitoring-Diagnostics-and-Control-Interfaces.md](083-080-Solar-Electric-Auxiliary-Monitoring-Diagnostics-and-Control-Interfaces.md) | active |
| 090 | S1000D / CSDB Mapping and Traceability | [083-090-S1000D-CSDB-Mapping-and-Traceability.md](083-090-S1000D-CSDB-Mapping-and-Traceability.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `080-089` |
| Section | `08` — Propulsión Alternativa & Cuántica |
| Subsection | `083` — Solar-Electric Auxiliary |
| Subsubject namespace | `00`–`99` (active) |
| Primary Q-Division | Q-GREENTECH[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-HPC, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-LEG, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/080-089_Propulsion-Alternativa-y-Cuantica/083_Solar-Electric-Auxiliary/` |
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
