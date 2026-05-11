---
document_id: QATL-ATLAS-1000-STA-120-129-02-122-000-GENERAL
title: "STA 120-129 · 122-000 — General"
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
subsection: "122"
subsection_title: "Propulsión Nuclear Conceptual"
subsubject: "000"
subsubject_title: "General"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · 122-000 — General

## 1. Purpose

Overview entry-point for the *Propulsión Nuclear Conceptual* subsection within the `120-129` code range (Section `02` — *Propulsión Espacial Tradicional y Avanzada*) of the **STA** architecture band.

This subsubject (`000 Overview`) introduces the STA 120-129.122 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the conceptual nuclear propulsion framework governing controlled definitions, nuclear thermal and electric propulsion concepts, radioisotope boundaries, reactor power conversion, radiation shielding, mission class screening, safety/regulatory constraints, and non-deployment assurance governance. This subsection is designated **conceptual-only**.

## 2. Scope

- Covers the *Propulsión Nuclear Conceptual* slice of the parent code range `120-129`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- **Boundary**: This subsection covers conceptual-level study and taxonomy only. No design, manufacture, deployment, launch integration, fissile-material handling, reactor operation, or weaponizable technical detail is permitted without separate lawful authority and controlled safety governance.
- Concepts in scope across the subsection:
  - **Nuclear Propulsion Conceptual Definition** (`001`) — controlled scope, applicability, and non-deployment boundaries.
  - **Nuclear Thermal Propulsion Concepts** (`002`) — NTP working fluid heating, solid-core, liquid-core, gas-core concepts.
  - **Nuclear Electric Propulsion Concepts** (`003`) — NEP reactor-powered electric thruster arrays, power chain concepts.
  - **Radioisotope Power and Propulsion Boundaries** (`004`) — RTG/MMRTG power boundaries, RPS interface screening.
  - **Reactor Power Conversion and Thermal Interface Boundaries** (`005`) — Brayton/Stirling/thermoelectric conversion concepts, thermal rejection.
  - **Radiation Shielding and Separation Distance Concepts** (`006`) — shadow shield geometry, dose limits, separation distance estimation.
  - **Mission Classes and Use-Case Screening** (`007`) — deep space, NEP cargo, NTP crewed Mars screening.
  - **Safety, Security and Regulatory Constraints** (`008`) — launch safety policy, ITAR/EAR, NPT, Outer Space Treaty boundaries.
  - **ECSS, NASA, IAEA and Outer Space Treaty Mapping** (`009`) — regulatory standards mapping.
  - **Assurance Evidence and Non-Deployment Boundaries** (`010`) — evidence package, lifecycle assurance boundaries.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `120-129` |
| Section | `02` — Propulsión Espacial Tradicional y Avanzada |
| Subsection | `122` — Propulsión Nuclear Conceptual |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Safety boundary | conceptual-only |
| Folder path | `Q+ATLANTIDE/100-199_STA/120-129_Propulsion-Espacial-Tradicional-y-Avanzada/122_Propulsion-Nuclear-Conceptual/` |
| Document | `122-000-General.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

[^nasanss16761]: **NASA-NSS 1676.1 — Nuclear Safety Policy** — NASA nuclear safety policy for space nuclear power and propulsion systems.

[^iaeatecdoc1819]: **IAEA-TECDOC-1819 — Space Nuclear Power and Propulsion** — IAEA overview of space nuclear technologies.

### Applicable industry standards

- NASA-NSS 1676.1 — Nuclear Safety Policy[^nasanss16761]
- IAEA-TECDOC-1819 — Space Nuclear Power and Propulsion[^iaeatecdoc1819]
- Outer Space Treaty (1967) — Treaty on Principles Governing the Activities of States in the Exploration and Use of Outer Space
