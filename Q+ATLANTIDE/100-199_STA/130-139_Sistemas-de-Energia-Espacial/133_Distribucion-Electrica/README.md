---
document_id: QATL-ATLAS-1000-STA-130-139-03-133-README
title: "STA 130-139 · 03.133 — Distribución Eléctrica (Subsection Index)"
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
subsection: "133"
subsection_title: "Distribución Eléctrica"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-DATAGOV, Q-HPC, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-FIN]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "103_Seguridad-de-Mision"
  - "121_Propulsion-Electrica"
  - "130_Energia-Solar"
  - "131_Baterias-y-Almacenamiento"
  - "132_Energia-Nuclear-Espacial-Conceptual"
safety_boundary: "mission-power critical; requires explicit bus topology, load priority logic, fault isolation, redundancy, EMC control, safe-mode behavior, qualification evidence and lifecycle traceability"
governance_class: baseline
version: 1.0.0
status: active
language: en
no_aaa_rule: true
---

# STA 130-139 · Section 03 · Subsection 133 — Distribución Eléctrica

## 1. Purpose

Subsection-level index for *Distribución Eléctrica* (`133`) within STA `130-139` — *Sistemas de Energía Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **mission-power critical**: all subsubjects require explicit bus topology, load priority logic, fault isolation, redundancy, EMC control, safe-mode behaviour, qualification evidence, and lifecycle traceability.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `133` *Electrical Distribution*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `103_Seguridad-de-Mision`, `121_Propulsion-Electrica`, `130_Energia-Solar`, `131_Baterias-y-Almacenamiento`, `132_Energia-Nuclear-Espacial-Conceptual`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](000_Overview.md) | active |
| 001 | Electrical Distribution Controlled Definition | [`001_Electrical-Distribution-Controlled-Definition.md`](001_Electrical-Distribution-Controlled-Definition.md) | active |
| 002 | Power Architecture and Bus Topology | [`002_Power-Architecture-and-Bus-Topology.md`](002_Power-Architecture-and-Bus-Topology.md) | active |
| 003 | Power Conditioning, Regulation and Conversion | [`003_Power-Conditioning-Regulation-and-Conversion.md`](003_Power-Conditioning-Regulation-and-Conversion.md) | active |
| 004 | Distribution Harnesses, Cables and Connectors | [`004_Distribution-Harnesses-Cables-and-Connectors.md`](004_Distribution-Harnesses-Cables-and-Connectors.md) | active |
| 005 | Switching, Protection and Fault Isolation | [`005_Switching-Protection-and-Fault-Isolation.md`](005_Switching-Protection-and-Fault-Isolation.md) | active |
| 006 | Load Management and Priority Shedding | [`006_Load-Management-and-Priority-Shedding.md`](006_Load-Management-and-Priority-Shedding.md) | active |
| 007 | EMC, Grounding, Bonding and Isolation | [`007_EMC-Grounding-Bonding-and-Isolation.md`](007_EMC-Grounding-Bonding-and-Isolation.md) | active |
| 008 | Redundancy, Cross-Strapping and Safe Modes | [`008_Redundancy-Cross-Strapping-and-Safe-Modes.md`](008_Redundancy-Cross-Strapping-and-Safe-Modes.md) | active |
| 009 | Testing, Qualification and Assurance Boundaries | [`009_Testing-Qualification-and-Assurance-Boundaries.md`](009_Testing-Qualification-and-Assurance-Boundaries.md) | active |
| 010 | Traceability, Evidence and Lifecycle Governance | [`010_Traceability-Evidence-and-Lifecycle-Governance.md`](010_Traceability-Evidence-and-Lifecycle-Governance.md) | active |
| 011–099 | *(reserved)* | — | reserved |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `130-139` |
| Section | `03` — Sistemas de Energía Espacial |
| Subsection | `133` — Distribución Eléctrica |
| Subsubject namespace | `000`–`010` active / `011`–`099` reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-GREENTECH, Q-DATAGOV, Q-HPC, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Safety boundary | mission-power critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/130-139_Sistemas-de-Energia-Espacial/133_Distribucion-Electrica/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE`, `support_q_divisions = [Q-GREENTECH, Q-DATAGOV, Q-HPC, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]`, and `governance_class = baseline` from the parent STA section. Extensions added under `011`–`099` shall preserve those header fields, declare the `safety_boundary`, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

# STA 130-139 · Section 03 · Subsection 133 — Distribución Eléctrica

## 1. Purpose

Subsection-level index for *Distribución Eléctrica* (`133`) within STA `130-139` — *Sistemas de Energía Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Reserves the subsubject namespace `00`–`99` of subsection `133` *Electrical Distribution*.
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
| Subsection | `133` — Distribución Eléctrica |
| Subsubject namespace | `00`–`99` (reserved) |
| Primary Q-Division | Q-GREENTECH[^qdiv] |
| Support Q-Divisions | Q-SPACE, Q-HPC |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/130-139_Sistemas-de-Energia-Espacial/133_Distribucion-Electrica/` |
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
