---
document_id: QATL-ATLAS-1000-STA-120-129-02-123-000-OVERVIEW
title: "STA 120-129 · 02.123.000 — Overview"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "120-129"
section: "02"
section_title: "Propulsión Espacial Tradicional y Avanzada"
subsection: "123"
subsection_title: "Propulsión Avanzada"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · Section 02 · Subsection 123 — Propulsión Avanzada

## 1. Purpose

Overview entry-point for the *Propulsión Avanzada* subsection within the `120-129` code range (Section `02` — *Propulsión Espacial Tradicional y Avanzada*) of the **STA** architecture band.

This subsubject (`000 Overview`) introduces the STA 120-129.123 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the advanced propulsion framework covering controlled definitions, high-Isp concepts, solar/light sails, electric/plasma sails, beam-driven systems, fusion concepts, exotic propulsion claim discipline, mission use-case screening, and non-operational assurance boundaries. This subsection is designated **research and concept-screening only**.

## 2. Scope

- Covers the *Propulsión Avanzada* slice of the parent code range `120-129`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- **Boundary**: Content is limited to research and concept-screening activities. Concepts below TRL 3 must not claim proven performance. All extraordinary propulsion claims shall include an engineering model, independent verification, and explicit TRL statement.
- Concepts in scope across the subsection:
  - **Advanced Propulsion Controlled Definition** (`001`) — controlled scope, applicability, and non-operational boundaries.
  - **High-Isp Propulsion Concepts** (`002`) — survey of propulsion concepts with Isp > 5 000 s.
  - **Solar Sail and Light-Sail Propulsion** (`003`) — radiation pressure mechanics, sail materials, deployment architectures.
  - **Electric Sail and Plasma Sail Concepts** (`004`) — E-sail solar wind interaction, plasma brake concepts.
  - **Beam-Driven Propulsion Concepts** (`005`) — laser/microwave beaming, photon pressure, directed energy screening.
  - **Fusion Propulsion Conceptual Boundaries** (`006`) — D-T/D-3He/p-B fusion propulsion screening, TRL boundaries.
  - **Field-Effect and Exotic Propulsion Claim Discipline** (`007`) — claim verification protocol, EM Drive exclusion rationale.
  - **Mission Use-Cases and Technology Readiness Screening** (`008`) — TRL 1–3 screening matrix, mission class matching.
  - **Energy, Thermal and Structural Interface Boundaries** (`009`) — power source interfaces, heat rejection, structural loads.
  - **Assurance Evidence and Non-Operational Boundaries** (`010`) — evidence package, lifecycle assurance, non-operational status.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `120-129` |
| Section | `02` — Propulsión Espacial Tradicional y Avanzada |
| Subsection | `123` — Propulsión Avanzada |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Safety boundary | research and concept-screening only |
| Folder path | `Q+ATLANTIDE/100-199_STA/120-129_Propulsion-Espacial-Tradicional-y-Avanzada/123_Propulsion-Avanzada/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

[^nasatrl]: **NASA Technology Readiness Level (TRL) Definitions** — NASA standard scale TRL 1–9 for technology maturation.

[^ecssest10c]: **ECSS-E-ST-10C — System Engineering General Requirements** — European standard for space system engineering and TRL assessment.

### Applicable industry standards

- NASA TRL Definitions — Technology Readiness Level scale[^nasatrl]
- ECSS-E-ST-10C — System Engineering General Requirements[^ecssest10c]
