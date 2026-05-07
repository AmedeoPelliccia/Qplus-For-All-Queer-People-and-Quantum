---
document_id: QATL-ATLAS-1000-STA-130-139-03-132-README
title: "STA 130-139 · 03.132 — Energía Nuclear Espacial Conceptual (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "130-139"
section: "03"
section_title: "Sistemas de Energía Espacial"
subsection: "132"
subsection_title: "Energía Nuclear Espacial Conceptual"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG]
orb_function_support: [ORB-PMO, ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "103_Seguridad-de-Mision"
  - "112_Proteccion-Termica-y-Radiacion"
  - "122_Propulsion-Nuclear-Conceptual"
  - "130_Energia-Solar"
  - "131_Baterias-y-Almacenamiento"
  - "133_Distribucion-Electrica"
safety_boundary: "conceptual-only; no design, manufacture, deployment, launch integration, fissile-material handling, reactor operation, or operational nuclear-system implementation without separate lawful authority and controlled safety/regulatory governance"
claim_discipline: "all nuclear energy claims must be grounded in published mission-class RPS or fission power studies; no speculative power levels, fuel masses, or reactor designs without cited authority"
governance_class: baseline
version: 1.0.0
status: active
language: en
no_aaa_rule: true
---

# STA 130-139 · Section 03 · Subsection 132 — Energía Nuclear Espacial Conceptual

## 1. Purpose

Subsection-level index for *Energía Nuclear Espacial Conceptual* (`132`) within STA `130-139` — *Sistemas de Energía Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **conceptual-only**: no design, manufacture, deployment, launch integration, fissile-material handling, reactor operation, or operational nuclear-system implementation is permitted without separate lawful authority and controlled safety/regulatory governance.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `132` *Conceptual Space Nuclear Energy*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `103_Seguridad-de-Mision`, `112_Proteccion-Termica-y-Radiacion`, `122_Propulsion-Nuclear-Conceptual`, `130_Energia-Solar`, `131_Baterias-y-Almacenamiento`, `133_Distribucion-Electrica`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](000_Overview.md) | active |
| 001 | Space Nuclear Energy Conceptual Definition | [`001_Space-Nuclear-Energy-Conceptual-Definition.md`](001_Space-Nuclear-Energy-Conceptual-Definition.md) | active |
| 002 | Radioisotope Power System Concepts | [`002_Radioisotope-Power-System-Concepts.md`](002_Radioisotope-Power-System-Concepts.md) | active |
| 003 | Fission Power System Concepts | [`003_Fission-Power-System-Concepts.md`](003_Fission-Power-System-Concepts.md) | active |
| 004 | Nuclear Electric Power Architecture Boundaries | [`004_Nuclear-Electric-Power-Architecture-Boundaries.md`](004_Nuclear-Electric-Power-Architecture-Boundaries.md) | active |
| 005 | Power Conversion, Thermal Rejection and Shielding | [`005_Power-Conversion-Thermal-Rejection-and-Shielding.md`](005_Power-Conversion-Thermal-Rejection-and-Shielding.md) | active |
| 006 | Mission Class and Use-Case Screening | [`006_Mission-Class-and-Use-Case-Screening.md`](006_Mission-Class-and-Use-Case-Screening.md) | active |
| 007 | Safety, Security and Regulatory Constraints | [`007_Safety-Security-and-Regulatory-Constraints.md`](007_Safety-Security-and-Regulatory-Constraints.md) | active |
| 008 | Launch, Reentry and Disposal Risk Boundaries | [`008_Launch-Reentry-and-Disposal-Risk-Boundaries.md`](008_Launch-Reentry-and-Disposal-Risk-Boundaries.md) | active |
| 009 | IAEA, NASA, ECSS and Outer Space Treaty Mapping | [`009_IAEA-NASA-ECSS-and-Outer-Space-Treaty-Mapping.md`](009_IAEA-NASA-ECSS-and-Outer-Space-Treaty-Mapping.md) | active |
| 010 | Assurance, Evidence and Non-Deployment Boundaries | [`010_Assurance-Evidence-and-Non-Deployment-Boundaries.md`](010_Assurance-Evidence-and-Non-Deployment-Boundaries.md) | active |
| 011–099 | *(reserved)* | — | reserved |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `130-139` |
| Section | `03` — Sistemas de Energía Espacial |
| Subsection | `132` — Energía Nuclear Espacial Conceptual |
| Subsubject namespace | `000`–`010` active / `011`–`099` reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Safety boundary | conceptual-only |
| Folder path | `Q+ATLANTIDE/100-199_STA/130-139_Sistemas-de-Energia-Espacial/132_Energia-Nuclear-Espacial-Conceptual/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE`, `support_q_divisions = [Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG]`, and `governance_class = baseline` from the parent STA section. The `safety_boundary` (conceptual-only) and `claim_discipline` apply to all subsubjects in this namespace. Extensions added under `011`–`099` shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

# STA 130-139 · Section 03 · Subsection 132 — Energía Nuclear Espacial Conceptual

## 1. Purpose

Subsection-level index for *Energía Nuclear Espacial Conceptual* (`132`) within STA `130-139` — *Sistemas de Energía Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Reserves the subsubject namespace `00`–`99` of subsection `132` *Space Nuclear Energy (Conceptual)*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Subsubjects `00`–`99` are reserved for future baseline extensions per the parent section's authorisation.

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 00 | Overview | `000_Overview.md` | reserved |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `130-139` |
| Section | `03` — Sistemas de Energía Espacial |
| Subsection | `132` — Energía Nuclear Espacial Conceptual |
| Subsubject namespace | `00`–`99` (reserved) |
| Primary Q-Division | Q-GREENTECH[^qdiv] |
| Support Q-Divisions | Q-SPACE, Q-HPC |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/130-139_Sistemas-de-Energia-Espacial/132_Energia-Nuclear-Espacial-Conceptual/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-GREENTECH` and `governance_class = baseline` from the parent STA section. Extensions added under `00`–`99` shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
