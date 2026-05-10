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
| 000 | General | [`122-000-General.md`](./122-000-General.md) | active |
| 010 | Nuclear Propulsion Conceptual Definition | [`122-010-Nuclear-Propulsion-Conceptual-Definition.md`](./122-010-Nuclear-Propulsion-Conceptual-Definition.md) | active |
| 020 | Nuclear Thermal Propulsion Concepts | [`122-020-Nuclear-Thermal-Propulsion-Concepts.md`](./122-020-Nuclear-Thermal-Propulsion-Concepts.md) | active |
| 030 | Nuclear Electric Propulsion Concepts | [`122-030-Nuclear-Electric-Propulsion-Concepts.md`](./122-030-Nuclear-Electric-Propulsion-Concepts.md) | active |
| 040 | Radioisotope Power and Propulsion Boundaries | [`122-040-Radioisotope-Power-and-Propulsion-Boundaries.md`](./122-040-Radioisotope-Power-and-Propulsion-Boundaries.md) | active |
| 050 | Reactor Power Conversion and Thermal Interface Boundaries | [`122-050-Reactor-Power-Conversion-and-Thermal-Interface-Boundaries.md`](./122-050-Reactor-Power-Conversion-and-Thermal-Interface-Boundaries.md) | active |
| 060 | Radiation Shielding and Separation Distance Concepts | [`122-060-Radiation-Shielding-and-Separation-Distance-Concepts.md`](./122-060-Radiation-Shielding-and-Separation-Distance-Concepts.md) | active |
| 070 | Mission Classes and Use Case Screening | [`122-070-Mission-Classes-and-Use-Case-Screening.md`](./122-070-Mission-Classes-and-Use-Case-Screening.md) | active |
| 080 | Safety Security and Regulatory Constraints | [`122-080-Safety-Security-and-Regulatory-Constraints.md`](./122-080-Safety-Security-and-Regulatory-Constraints.md) | active |
| 090 | Assurance Evidence and Non Deployment Boundaries | [`122-090-Assurance-Evidence-and-Non-Deployment-Boundaries.md`](./122-090-Assurance-Evidence-and-Non-Deployment-Boundaries.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `120-129` |
| Section | `02` — Propulsión Espacial Tradicional y Avanzada |
| Subsection | `122` — Propulsión Nuclear Conceptual |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
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
