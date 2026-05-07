---
document_id: QATL-ATLAS-1000-STA-130-139-03-132-000-OVERVIEW
title: "STA 130-139 · 03.132.000 — Overview"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "130-139"
section: "03"
section_title: "Sistemas de Energía Espacial"
subsection: "132"
subsection_title: "Energía Nuclear Espacial Conceptual"
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
# STA 130-139 · Section 03 · Subsection 132 — Energía Nuclear Espacial Conceptual

## 1. Purpose

Overview entry-point for *Energía Nuclear Espacial Conceptual* (`132`) within STA `130-139`. This subsection is designated **conceptual-only**: no design, manufacture, deployment, fissile-material handling, reactor operation, or operational nuclear-system implementation is permitted without separate lawful authority and controlled safety/regulatory governance.

## 2. Scope

- **Space Nuclear Energy Conceptual Definition** (`001`) — normative scope and conceptual-only boundary.
- **Radioisotope Power System Concepts** (`002`) — RTG and MMRTG survey; Pu-238 heat source concepts; published mission data.
- **Fission Power System Concepts** (`003`) — kilopower/fission surface power; reactor concepts at conceptual level only.
- **Nuclear Electric Power Architecture Boundaries** (`004`) — power conversion chains, thermal rejection, and electrical interface concepts.
- **Power Conversion, Thermal Rejection and Shielding** (`005`) — Stirling, Brayton, thermoelectric conversion; shadow-shield geometry.
- **Mission Class and Use-Case Screening** (`006`) — deep-space (>5 AU), lunar/Mars surface, NEP propulsion use cases.
- **Safety, Security and Regulatory Constraints** (`007`) — IAEA Safety Series, NSS-11, ESA/NASA launch approval frameworks.
- **Launch, Reentry and Disposal Risk Boundaries** (`008`) — INSRP/ODEC process; reentry dispersal boundaries.
- **IAEA, NASA, ECSS and Outer Space Treaty Mapping** (`009`) — regulatory hierarchy mapping.
- **Assurance, Evidence and Non-Deployment Boundaries** (`010`) — conceptual evidence package requirements; non-deployment boundary declaration.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `132` — Energía Nuclear Espacial Conceptual |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Safety boundary | **conceptual-only** |
| Document | `000_Overview.md` (this file) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards
- IAEA Safety Series No. 6 — Principles Relevant to the Use of Nuclear Power Sources in Outer Space
- NSS-11 — IAEA Nuclear Security Series
- NASA-STD-8719.14B — Process for Limiting Orbital Debris
