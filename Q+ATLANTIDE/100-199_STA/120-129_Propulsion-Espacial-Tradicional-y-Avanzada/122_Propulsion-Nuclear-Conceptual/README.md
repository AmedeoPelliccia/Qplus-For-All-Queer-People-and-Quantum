---
document_id: QATL-ATLAS-1000-STA-120-129-02-122-README
title: "STA 120-129 · 02.122 — Propulsión Nuclear Conceptual (Subsection Index)"
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
subsection: "122"
subsection_title: "Propulsión Nuclear Conceptual"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG]
orb_function_support: [ORB-PMO, ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "103_Seguridad-de-Mision"
  - "112_Proteccion-Termica-y-Radiacion"
  - "120_Propulsion-Quimica"
  - "121_Propulsion-Electrica"
  - "123_Propulsion-Avanzada"
  - "132_Energia-Nuclear-Espacial-Conceptual"
safety_boundary: "conceptual-only; no design, manufacture, deployment, launch integration, fissile-material handling, reactor operation, or weaponizable technical detail without separate lawful authority and controlled safety governance"
governance_class: baseline
version: 1.0.0
status: active
language: en
no_aaa_rule: true
---

# STA 120-129 · Section 02 · Subsection 122 — Propulsión Nuclear Conceptual

## 1. Purpose

Subsection-level index for *Propulsión Nuclear Conceptual* (`122`) within STA `120-129` — *Propulsión Espacial Tradicional y Avanzada*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **conceptual-only**: no design, manufacture, deployment, launch integration, fissile-material handling, reactor operation, or weaponizable technical detail is permitted without separate lawful authority and controlled safety governance.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `122` *Conceptual Nuclear Propulsion*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `103_Seguridad-de-Mision`, `112_Proteccion-Termica-y-Radiacion`, `120_Propulsion-Quimica`, `121_Propulsion-Electrica`, `123_Propulsion-Avanzada`, `132_Energia-Nuclear-Espacial-Conceptual`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](000_Overview.md) | active |
| 001 | Nuclear Propulsion Conceptual Definition | [`001_Nuclear-Propulsion-Conceptual-Definition.md`](001_Nuclear-Propulsion-Conceptual-Definition.md) | active |
| 002 | Nuclear Thermal Propulsion Concepts | [`002_Nuclear-Thermal-Propulsion-Concepts.md`](002_Nuclear-Thermal-Propulsion-Concepts.md) | active |
| 003 | Nuclear Electric Propulsion Concepts | [`003_Nuclear-Electric-Propulsion-Concepts.md`](003_Nuclear-Electric-Propulsion-Concepts.md) | active |
| 004 | Radioisotope Power and Propulsion Boundaries | [`004_Radioisotope-Power-and-Propulsion-Boundaries.md`](004_Radioisotope-Power-and-Propulsion-Boundaries.md) | active |
| 005 | Reactor Power Conversion and Thermal Interface Boundaries | [`005_Reactor-Power-Conversion-and-Thermal-Interface-Boundaries.md`](005_Reactor-Power-Conversion-and-Thermal-Interface-Boundaries.md) | active |
| 006 | Radiation Shielding and Separation Distance Concepts | [`006_Radiation-Shielding-and-Separation-Distance-Concepts.md`](006_Radiation-Shielding-and-Separation-Distance-Concepts.md) | active |
| 007 | Mission Classes and Use-Case Screening | [`007_Mission-Classes-and-Use-Case-Screening.md`](007_Mission-Classes-and-Use-Case-Screening.md) | active |
| 008 | Safety, Security and Regulatory Constraints | [`008_Safety-Security-and-Regulatory-Constraints.md`](008_Safety-Security-and-Regulatory-Constraints.md) | active |
| 009 | ECSS, NASA, IAEA and Outer Space Treaty Mapping | [`009_ECSS-NASA-IAEA-Outer-Space-Treaty-Mapping.md`](009_ECSS-NASA-IAEA-Outer-Space-Treaty-Mapping.md) | active |
| 010 | Assurance Evidence and Non-Deployment Boundaries | [`010_Assurance-Evidence-and-Non-Deployment-Boundaries.md`](010_Assurance-Evidence-and-Non-Deployment-Boundaries.md) | active |
| 011–099 | *(reserved)* | — | reserved |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `120-129` |
| Section | `02` — Propulsión Espacial Tradicional y Avanzada |
| Subsection | `122` — Propulsión Nuclear Conceptual |
| Subsubject namespace | `000`–`010` active / `011`–`099` reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Safety boundary | conceptual-only |
| Folder path | `Q+ATLANTIDE/100-199_STA/120-129_Propulsion-Espacial-Tradicional-y-Avanzada/122_Propulsion-Nuclear-Conceptual/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE`, `support_q_divisions = [Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG]`, and `governance_class = baseline` from the parent STA section. Extensions added under `011`–`099` shall preserve those header fields, declare the `safety_boundary`, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
