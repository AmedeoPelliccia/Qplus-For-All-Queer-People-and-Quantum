---
document_id: QATL-ATLAS-1000-ATLAS-010-019-01-014-README
title: "ATLAS 010-019 · 01.014 — Parking (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "010-019"
section: "01"
section_title: "Manejo en Tierra & Servicio"
subsection: "014"
subsection_title: "Parking"
primary_q_division: Q-GROUND
support_q_divisions: [Q-MECHANICS, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.1.0
status: active
language: en
---

# ATLAS 010-019 · Section 01 · Subsection 014 — Parking

## 1. Purpose

Subsection-level index for *Parking* (`014`) within ATLAS `010-019` — *Manejo en Tierra & Servicio* — Parking, mooring and storage (was 050_).

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Populates subsubjects `000`–`005` of subsection `014` *Parking*; reserves `006`–`099` for future extension.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Each subsubject provides **Level 2 — Procedure** content; introductory orientation (Level 1) for parking and mooring is in [`../../000-009_Informacion-General-y-Servicio/003_Operaciones-Basicas/`](../../000-009_Informacion-General-y-Servicio/003_Operaciones-Basicas/).

## 3. Subsubject Index

| 00N | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`014-000-Parking-Overview.md`](./014-000-Parking-Overview.md) | active |
| 001 | Scope and Parking Boundaries | [`014-001-Parking-Scope-and-Boundaries.md`](./014-001-Parking-Scope-and-Boundaries.md) | active |
| 002 | Parking Configurations and Stand Types | [`014-002-Parking-Configurations-and-Stand-Types.md`](./014-002-Parking-Configurations-and-Stand-Types.md) | active |
| 003 | Mooring, Tie-Down and Wind Protection | [`014-003-Mooring-Tie-Down-and-Wind-Protection.md`](./014-003-Mooring-Tie-Down-and-Wind-Protection.md) | active |
| 004 | Short-Term Parking and Turnaround Configurations | [`014-004-Short-Term-Parking-and-Turnaround-Configurations.md`](./014-004-Short-Term-Parking-and-Turnaround-Configurations.md) | active |
| 005 | Parking Records, Inspections and Return to Service | [`014-005-Parking-Records-Inspections-and-Return-to-Service.md`](./014-005-Parking-Records-Inspections-and-Return-to-Service.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `010-019` |
| Section | `01` — Manejo en Tierra & Servicio |
| Subsection | `014` — Parking |
| Subsubject namespace | `000`–`005` populated; `006`–`099` reserved |
| Primary Q-Division | Q-GROUND[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/010-019_Manejo-en-Tierra-Servicio/014_Parking/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-GROUND` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `006`–`099` shall preserve those header fields and reuse the footnote set declared here.

## Change Log

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0.0 | 2026-05-07 | Q+ Team/Amedeo Pelliccia + AI | Initial reserve — subsection index only, all subsubjects `to be populated`. |
| 1.1.0 | 2026-05-07 | Q+ Team/Amedeo Pelliccia + AI | Baseline release — `014-000-Parking-Overview.md` + subsubjects `001`–`005` populated; subsubject index updated; namespace updated to reflect populated range. |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
