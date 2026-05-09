---
document_id: QATL-ATLAS-1000-STA-120-129-02-121-README
title: "STA 120-129 · 02.121 — Propulsión Eléctrica (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "120-129"
section: "02"
section_title: "Propulsión Espacial Tradicional y Avanzada"
subsection: "121"
subsection_title: "Propulsión Eléctrica"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-HPC, Q-DATAGOV, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "112_Proteccion-Termica-y-Radiacion"
  - "120_Propulsion-Quimica"
  - "123_Propulsion-Avanzada"
  - "130_Energia-Solar"
  - "133_Distribucion-Electrica"
safety_boundary: "propulsion-critical; requires explicit power-interface assurance, PPU validation, plume interaction analysis, EMC control, thermal management, propellant compatibility, test evidence and lifecycle traceability"
governance_class: baseline
version: 1.0.0
status: active
language: en
no_aaa_rule: true
---

# STA 120-129 · Section 02 · Subsection 121 — Propulsión Eléctrica

## 1. Purpose

Subsection-level index for *Propulsión Eléctrica* (`121`) within STA `120-129` — *Propulsión Espacial Tradicional y Avanzada*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **propulsion-critical**: all subsubjects require explicit power-interface assurance, PPU validation, plume interaction analysis, EMC control, thermal management, propellant compatibility, test evidence, and lifecycle traceability.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `121` *Electric Propulsion*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `112_Proteccion-Termica-y-Radiacion`, `120_Propulsion-Quimica`, `123_Propulsion-Avanzada`, `130_Energia-Solar`, `133_Distribucion-Electrica`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`121-000-General.md`](./121-000-General.md) | active |
| 010 | Electric Propulsion Controlled Definition | [`121-010-Electric-Propulsion-Controlled-Definition.md`](./121-010-Electric-Propulsion-Controlled-Definition.md) | active |
| 020 | Electric Propulsion Families and Selection Criteria | [`121-020-Electric-Propulsion-Families-and-Selection-Criteria.md`](./121-020-Electric-Propulsion-Families-and-Selection-Criteria.md) | active |
| 030 | Electrothermal Propulsion | [`121-030-Electrothermal-Propulsion.md`](./121-030-Electrothermal-Propulsion.md) | active |
| 040 | Electrostatic Propulsion Ion and Hall Effect | [`121-040-Electrostatic-Propulsion-Ion-and-Hall-Effect.md`](./121-040-Electrostatic-Propulsion-Ion-and-Hall-Effect.md) | active |
| 050 | Electromagnetic Propulsion MPDT and Pulsed Plasma | [`121-050-Electromagnetic-Propulsion-MPDT-and-Pulsed-Plasma.md`](./121-050-Electromagnetic-Propulsion-MPDT-and-Pulsed-Plasma.md) | active |
| 060 | Power Processing Units and Electrical Interfaces | [`121-060-Power-Processing-Units-and-Electrical-Interfaces.md`](./121-060-Power-Processing-Units-and-Electrical-Interfaces.md) | active |
| 070 | Propellant Feed Storage and Compatibility | [`121-070-Propellant-Feed-Storage-and-Compatibility.md`](./121-070-Propellant-Feed-Storage-and-Compatibility.md) | active |
| 080 | Thrust Isp Efficiency and Duty Cycle Metrics | [`121-080-Thrust-Isp-Efficiency-and-Duty-Cycle-Metrics.md`](./121-080-Thrust-Isp-Efficiency-and-Duty-Cycle-Metrics.md) | active |
| 090 | Testing Qualification and Assurance Boundaries | [`121-090-Testing-Qualification-and-Assurance-Boundaries.md`](./121-090-Testing-Qualification-and-Assurance-Boundaries.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `120-129` |
| Section | `02` — Propulsión Espacial Tradicional y Avanzada |
| Subsection | `121` — Propulsión Eléctrica |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-GREENTECH, Q-HPC, Q-DATAGOV, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Safety boundary | propulsion-critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/120-129_Propulsion-Espacial-Tradicional-y-Avanzada/121_Propulsion-Electrica/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE`, `support_q_divisions = [Q-GREENTECH, Q-HPC, Q-DATAGOV, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]`, and `governance_class = baseline` from the parent STA section. Extensions added under `011`–`099` shall preserve those header fields, declare the `safety_boundary`, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
