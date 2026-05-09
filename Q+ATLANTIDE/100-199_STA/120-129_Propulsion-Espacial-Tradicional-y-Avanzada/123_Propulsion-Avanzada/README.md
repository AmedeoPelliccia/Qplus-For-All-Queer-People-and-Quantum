---
document_id: QATL-ATLAS-1000-STA-120-129-02-123-README
title: "STA 120-129 · 02.123 — Propulsión Avanzada (Subsection Index)"
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
subsection: "123"
subsection_title: "Propulsión Avanzada"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG]
orb_function_support: [ORB-PMO, ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "103_Seguridad-de-Mision"
  - "112_Proteccion-Termica-y-Radiacion"
  - "120_Propulsion-Quimica"
  - "121_Propulsion-Electrica"
  - "122_Propulsion-Nuclear-Conceptual"
  - "130_Energia-Solar"
  - "133_Distribucion-Electrica"
safety_boundary: "research and concept-screening only unless separately matured, verified, lawfully authorized, and governed through explicit mission-safety, energy, thermal, structural and regulatory assurance gates"
claim_discipline: "extraordinary propulsion claims shall include engineering model, independent verification, and explicit TRL statement; no claims of proven performance for concepts below TRL 3"
governance_class: baseline
version: 1.0.0
status: active
language: en
no_aaa_rule: true
---

# STA 120-129 · Section 02 · Subsection 123 — Propulsión Avanzada

## 1. Purpose

Subsection-level index for *Propulsión Avanzada* (`123`) within STA `120-129` — *Propulsión Espacial Tradicional y Avanzada*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **research and concept-screening only**: content here is limited to matured, verified, and lawfully authorized concepts governed through explicit mission-safety, energy, thermal, structural, and regulatory assurance gates.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `123` *Advanced Propulsion*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `103_Seguridad-de-Mision`, `112_Proteccion-Termica-y-Radiacion`, `120_Propulsion-Quimica`, `121_Propulsion-Electrica`, `122_Propulsion-Nuclear-Conceptual`, `130_Energia-Solar`, `133_Distribucion-Electrica`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`123-000-General.md`](./123-000-General.md) | active |
| 010 | Advanced Propulsion Controlled Definition | [`123-010-Advanced-Propulsion-Controlled-Definition.md`](./123-010-Advanced-Propulsion-Controlled-Definition.md) | active |
| 020 | High Isp Propulsion Concepts | [`123-020-High-Isp-Propulsion-Concepts.md`](./123-020-High-Isp-Propulsion-Concepts.md) | active |
| 030 | Solar Sail and Light Sail Propulsion | [`123-030-Solar-Sail-and-Light-Sail-Propulsion.md`](./123-030-Solar-Sail-and-Light-Sail-Propulsion.md) | active |
| 040 | Electric Sail and Plasma Sail Concepts | [`123-040-Electric-Sail-and-Plasma-Sail-Concepts.md`](./123-040-Electric-Sail-and-Plasma-Sail-Concepts.md) | active |
| 050 | Beam Driven Propulsion Concepts | [`123-050-Beam-Driven-Propulsion-Concepts.md`](./123-050-Beam-Driven-Propulsion-Concepts.md) | active |
| 060 | Fusion Propulsion Conceptual Boundaries | [`123-060-Fusion-Propulsion-Conceptual-Boundaries.md`](./123-060-Fusion-Propulsion-Conceptual-Boundaries.md) | active |
| 070 | Field Effect and Exotic Propulsion Claim Discipline | [`123-070-Field-Effect-and-Exotic-Propulsion-Claim-Discipline.md`](./123-070-Field-Effect-and-Exotic-Propulsion-Claim-Discipline.md) | active |
| 080 | Mission Use Cases and Technology Readiness Screening | [`123-080-Mission-Use-Cases-and-Technology-Readiness-Screening.md`](./123-080-Mission-Use-Cases-and-Technology-Readiness-Screening.md) | active |
| 090 | Assurance Evidence and Non Operational Boundaries | [`123-090-Assurance-Evidence-and-Non-Operational-Boundaries.md`](./123-090-Assurance-Evidence-and-Non-Operational-Boundaries.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `120-129` |
| Section | `02` — Propulsión Espacial Tradicional y Avanzada |
| Subsection | `123` — Propulsión Avanzada |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Safety boundary | research and concept-screening only |
| Folder path | `Q+ATLANTIDE/100-199_STA/120-129_Propulsion-Espacial-Tradicional-y-Avanzada/123_Propulsion-Avanzada/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE`, `support_q_divisions = [Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG]`, and `governance_class = baseline` from the parent STA section. Extensions added under `011`–`099` shall preserve those header fields, declare the `safety_boundary` and `claim_discipline`, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
