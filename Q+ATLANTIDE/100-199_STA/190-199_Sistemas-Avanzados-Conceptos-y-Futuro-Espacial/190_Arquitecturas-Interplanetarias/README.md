---
document_id: QATL-ATLAS-1000-STA-190-199-09-190-README
title: "STA 190-199 · 09.190 — Arquitecturas Interplanetarias (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "190-199"
section: "09"
section_title: "Sistemas Avanzados, Conceptos y Futuro Espacial"
subsection: "190"
subsection_title: "Arquitecturas Interplanetarias"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-DATAGOV, Q-HPC, Q-GREENTECH, Q-STRUCTURES, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 190-199 · Section 09 · Subsection 190 — Arquitecturas Interplanetarias

## 1. Purpose

Subsection-level index for *Arquitecturas Interplanetarias* (`190`) within STA `190-199` — *Sistemas Avanzados, Conceptos y Futuro Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Reserves the subsubject namespace `00`–`99` of subsection `190` *Interplanetary Architectures*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Subsubjects `00`–`10` are active baseline documents; `11`–`99` are reserved for future baseline extensions per the parent section's authorisation.

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 00 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 01 | Interplanetary Architecture Controlled Definition | [`001_Interplanetary-Architecture-Controlled-Definition.md`](./001_Interplanetary-Architecture-Controlled-Definition.md) | active |
| 02 | Mission Classes and Interplanetary Regimes | [`002_Mission-Classes-and-Interplanetary-Regimes.md`](./002_Mission-Classes-and-Interplanetary-Regimes.md) | active |
| 03 | Trajectory Architecture and Transfer Windows | [`003_Trajectory-Architecture-and-Transfer-Windows.md`](./003_Trajectory-Architecture-and-Transfer-Windows.md) | active |
| 04 | Deep-Space Transport and Propulsion Interfaces | [`004_Deep-Space-Transport-and-Propulsion-Interfaces.md`](./004_Deep-Space-Transport-and-Propulsion-Interfaces.md) | active |
| 05 | Communication, Navigation and Time-Reference Boundaries | [`005_Communication-Navigation-and-Time-Reference-Boundaries.md`](./005_Communication-Navigation-and-Time-Reference-Boundaries.md) | active |
| 06 | Surface, Orbital and Transit Infrastructure Interfaces | [`006_Surface-Orbital-and-Transit-Infrastructure-Interfaces.md`](./006_Surface-Orbital-and-Transit-Infrastructure-Interfaces.md) | active |
| 07 | Autonomy, Safe Modes and Long-Duration Operations | [`007_Autonomy-Safe-Modes-and-Long-Duration-Operations.md`](./007_Autonomy-Safe-Modes-and-Long-Duration-Operations.md) | active |
| 08 | Radiation, Life Support and Human Factors Boundaries | [`008_Radiation-Life-Support-and-Human-Factors-Boundaries.md`](./008_Radiation-Life-Support-and-Human-Factors-Boundaries.md) | active |
| 09 | ECSS, NASA, CCSDS Deep-Space Standards Mapping | [`009_ECSS-NASA-CCSDS-Deep-Space-Standards-Mapping.md`](./009_ECSS-NASA-CCSDS-Deep-Space-Standards-Mapping.md) | active |
| 10 | Traceability, Evidence and Lifecycle Governance | [`010_Traceability-Evidence-and-Lifecycle-Governance.md`](./010_Traceability-Evidence-and-Lifecycle-Governance.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `190-199` |
| Section | `09` — Sistemas Avanzados, Conceptos y Futuro Espacial |
| Subsection | `190` — Arquitecturas Interplanetarias |
| Subsubject namespace | `00`–`99` (active: `00`–`10`) |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-DATAGOV, Q-HPC, Q-GREENTECH, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/190-199_Sistemas-Avanzados-Conceptos-y-Futuro-Espacial/190_Arquitecturas-Interplanetarias/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE` and `governance_class = baseline` from the parent STA section. Extensions added under `00`–`99` shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — Q-SPACE is the primary authority for all interplanetary architecture standards within Q+ATLANTIDE; Q-HORIZON, Q-DATAGOV, Q-HPC, Q-GREENTECH, Q-STRUCTURES, and Q-INDUSTRY provide supporting governance.

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
