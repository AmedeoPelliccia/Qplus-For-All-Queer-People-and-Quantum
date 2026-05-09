---
document_id: QATL-ATLAS-1000-ATLAS-030-039-03-032-README
title: "ATLAS 030-039 · 03.032 — Landing Gear (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "030-039"
section: "03"
section_title: "Protección & Sistemas Mecánicos"
subsection: "032"
subsection_title: "Landing Gear"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-AIR, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 030-039 · Section 03 · Subsection 032 — Landing Gear

## 1. Purpose

Subsection-level index for *Landing Gear* (`032`) within ATLAS `030-039` — *Protección & Sistemas Mecánicos* — ATA 32.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Reserves the subsubject namespace `00`–`99` of subsection `032` *Landing Gear*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- The Overview and detailed subsubjects (`00`–`99`) will be populated in subsequent baseline releases per the parent section's authorisation.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| `000` | Landing Gear General | [`032-000-Landing-Gear-General.md`](./032-000-Landing-Gear-General.md) | active |
| `010` | Main Landing Gear | [`032-010-Main-Landing-Gear.md`](./032-010-Main-Landing-Gear.md) | active |
| `020` | Nose Landing Gear | [`032-020-Nose-Landing-Gear.md`](./032-020-Nose-Landing-Gear.md) | active |
| `030` | Extension and Retraction | [`032-030-Extension-and-Retraction.md`](./032-030-Extension-and-Retraction.md) | active |
| `040` | Wheels, Tires and Brakes | [`032-040-Wheels-Tires-and-Brakes.md`](./032-040-Wheels-Tires-and-Brakes.md) | active |
| `050` | Steering | [`032-050-Steering.md`](./032-050-Steering.md) | active |
| `060` | Position Indication and Warning | [`032-060-Position-Indication-and-Warning.md`](./032-060-Position-Indication-and-Warning.md) | active |
| `070` | Shock Absorption and Structural Interfaces | [`032-070-Shock-Absorption-and-Structural-Interfaces.md`](./032-070-Shock-Absorption-and-Structural-Interfaces.md) | active |
| `080` | Landing Gear Monitoring, Diagnostics and Control Interfaces | [`032-080-Landing-Gear-Monitoring-Diagnostics-and-Control-Interfaces.md`](./032-080-Landing-Gear-Monitoring-Diagnostics-and-Control-Interfaces.md) | active |
| `090` | S1000D CSDB Mapping and Traceability | [`032-090-S1000D-CSDB-Mapping-and-Traceability.md`](./032-090-S1000D-CSDB-Mapping-and-Traceability.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `030-039` |
| Section | `03` — Protección & Sistemas Mecánicos |
| Subsection | `032` — Landing Gear |
| Subsubject namespace | `00`–`99` (reserved) |
| Primary Q-Division | Q-MECHANICS[^qdiv] |
| Support Q-Divisions | Q-AIR, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/032_Landing-Gear/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-MECHANICS` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `00`–`99` shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
