---
document_id: QATL-ATLAS-1000-STA-130-139-03-133-000-OVERVIEW
title: "STA 130-139 · 03.133.000 — Overview"
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
subsection: "133"
subsection_title: "Distribución Eléctrica"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-DATAGOV, Q-HPC, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · Section 03 · Subsection 133 — Distribución Eléctrica

## 1. Purpose

Overview entry-point for *Distribución Eléctrica* (`133`) within STA `130-139`. This subsubject introduces the electrical distribution framework covering controlled definitions, power bus topology, power conditioning/regulation, harness/cable design, switching/protection, load management, EMC/grounding, redundancy/safe-modes, testing/qualification, and lifecycle governance. Designated **mission-power critical**.

## 2. Scope

- **Electrical Distribution Controlled Definition** (`001`) — normative scope, applicability boundary vs. `130`, `131`, `132`.
- **Power Architecture and Bus Topology** (`002`) — regulated vs. unregulated bus, single vs. dual bus, voltage standards.
- **Power Conditioning, Regulation and Conversion** (`003`) — DC/DC converters, linear regulators, ripple/noise limits.
- **Distribution Harnesses, Cables and Connectors** (`004`) — wire gauge, routing, shielding, connector selection.
- **Switching, Protection and Fault Isolation** (`005`) — remote power controllers (RPCs), fuses, circuit breakers, latching current limiters.
- **Load Management and Priority Shedding** (`006`) — load priority tiers, automatic load shedding in safe-mode.
- **EMC, Grounding, Bonding and Isolation** (`007`) — single-point ground, chassis bond, conducted emission limits.
- **Redundancy, Cross-Strapping and Safe Modes** (`008`) — bus cross-strapping, redundant power paths, safe-mode minimum load set.
- **Testing, Qualification and Assurance Boundaries** (`009`) — EPS test matrix, EMC testing, acceptance test.
- **Traceability, Evidence and Lifecycle Governance** (`010`) — design evidence gates, ICD freeze, CI lifecycle records.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `133` — Distribución Eléctrica |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `133-000-General.md` (this file) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.
[^ecssest20]: **ECSS-E-ST-20C — Electrical and Electronic**.

### Applicable industry standards
- ECSS-E-ST-20C — Electrical and Electronic[^ecssest20]
- MIL-STD-461G — Requirements for the Control of Electromagnetic Interference
