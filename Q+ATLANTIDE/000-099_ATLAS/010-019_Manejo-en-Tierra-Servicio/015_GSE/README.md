---
document_id: QATL-ATLAS-1000-ATLAS-010-019-01-015-README
title: "ATLAS 010-019 · 01.015 — Ground Support Equipment (Subsection Index)"
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
subsection: "015"
subsection_title: "Ground Support Equipment"
primary_q_division: Q-GROUND
support_q_divisions: [Q-MECHANICS, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 010-019 · Section 01 · Subsection 015 — Ground Support Equipment

## 1. Purpose

Subsection-level index for *Ground Support Equipment* (`015`) within ATLAS `010-019` — *Manejo en Tierra & Servicio* — Ground support equipment catalogue and interfaces (was 060_).

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Covers the subsubject namespace `000`–`005` of subsection `015` *Ground Support Equipment*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Subsubjects `000`–`005` are populated in this baseline release:
  - `015-000-GSE-Overview.md` — subsection scope, boundary rules, position in ATLAS, content map
  - `015-001-GSE-Scope-and-Boundaries.md` — taxonomy boundary definitions; what is/is not GSE within ATLAS
  - `015-002-GSE-Catalog-and-Compatibility-Matrix.md` — authorised GSE list per AMPEL360 variant with compatibility ratings
  - `015-003-Powered-and-Non-Powered-GSE.md` — classification of GSE by power source; operational requirements per class
  - `015-004-GSE-Interfaces-Couplings-and-Aircraft-Side-Connections.md` — physical and electrical interfaces between GSE and aircraft
  - `015-005-GSE-Maintenance-Calibration-and-Records.md` — maintenance intervals, calibration schedules, and traceability records

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`015-000-GSE-Overview.md`](./015-000-GSE-Overview.md) | active |
| 001 | Scope and GSE Boundaries | [`015-001-GSE-Scope-and-Boundaries.md`](./015-001-GSE-Scope-and-Boundaries.md) | active |
| 002 | GSE Catalog and Compatibility Matrix | [`015-002-GSE-Catalog-and-Compatibility-Matrix.md`](./015-002-GSE-Catalog-and-Compatibility-Matrix.md) | active |
| 003 | Powered and Non-Powered GSE | [`015-003-Powered-and-Non-Powered-GSE.md`](./015-003-Powered-and-Non-Powered-GSE.md) | active |
| 004 | GSE Interfaces, Couplings and Aircraft-Side Connections | [`015-004-GSE-Interfaces-Couplings-and-Aircraft-Side-Connections.md`](./015-004-GSE-Interfaces-Couplings-and-Aircraft-Side-Connections.md) | active |
| 005 | GSE Maintenance, Calibration and Records | [`015-005-GSE-Maintenance-Calibration-and-Records.md`](./015-005-GSE-Maintenance-Calibration-and-Records.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `010-019` |
| Section | `01` — Manejo en Tierra & Servicio |
| Subsection | `015` — Ground Support Equipment |
| Subsubject namespace | `000`–`005` (active) |
| Primary Q-Division | Q-GROUND[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/010-019_Manejo-en-Tierra-Servicio/015_GSE/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-GROUND` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `000`–`099` shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
