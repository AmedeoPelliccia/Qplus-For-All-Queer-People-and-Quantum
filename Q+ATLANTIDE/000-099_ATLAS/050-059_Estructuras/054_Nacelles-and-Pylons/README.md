---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-054-README"
title: "ATLAS 050-059 · 05.054 — Nacelles and Pylons (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "050-059"
section: "05"
section_title: "Estructuras"
subsection: "054"
subsection_title: "Nacelles and Pylons"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · Section 05 · Subsection 054 — Nacelles and Pylons

## 1. Purpose

Subsection-level index for *Nacelles and Pylons* (`054`) within ATLAS `050-059` — *Estructuras* — ATA 54.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Reserves the subsubject namespace `00`–`99` of subsection `054` *Nacelles and Pylons*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- The Overview and detailed subsubjects (`00`–`99`) will be populated in subsequent baseline releases per the parent section's authorisation.

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 000 | Nacelles and Pylons — General | [054-000-Nacelles-and-Pylons-General/README.md](./054-000-Nacelles-and-Pylons-General/README.md) | DRAFT |
| 010 | Nacelle Structure | [054-010-Nacelle-Structure/README.md](./054-010-Nacelle-Structure/README.md) | DRAFT |
| 020 | Pylon Primary Structure | [054-020-Pylon-Primary-Structure/README.md](./054-020-Pylon-Primary-Structure/README.md) | DRAFT |
| 030 | Pylon-to-Wing Interfaces | [054-030-Pylon-to-Wing-Interfaces/README.md](./054-030-Pylon-to-Wing-Interfaces/README.md) | DRAFT |
| 040 | Propulsion Mounting Interfaces | [054-040-Propulsion-Mounting-Interfaces/README.md](./054-040-Propulsion-Mounting-Interfaces/README.md) | DRAFT |
| 050 | Fire Zone Structural Boundaries | [054-050-Fire-Zone-Structural-Boundaries/README.md](./054-050-Fire-Zone-Structural-Boundaries/README.md) | DRAFT |
| 060 | Fairings, Panels and Access Doors | [054-060-Fairings-Panels-and-Access-Doors/README.md](./054-060-Fairings-Panels-and-Access-Doors/README.md) | DRAFT |
| 070 | Nacelle and Pylon Repairs and NDT | [054-070-Nacelle-and-Pylon-Repairs-and-NDT/README.md](./054-070-Nacelle-and-Pylon-Repairs-and-NDT/README.md) | DRAFT |
| 080 | Nacelles and Pylons Monitoring, Diagnostics and Control Interfaces | [054-080-Nacelles-Pylons-Monitoring-Diagnostics-and-Control-Interfaces/README.md](./054-080-Nacelles-Pylons-Monitoring-Diagnostics-and-Control-Interfaces/README.md) | DRAFT |
| 090 | S1000D CSDB Mapping and Traceability | [054-090-S1000D-CSDB-Mapping-and-Traceability/README.md](./054-090-S1000D-CSDB-Mapping-and-Traceability/README.md) | DRAFT |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `050-059` |
| Section | `05` — Estructuras |
| Subsection | `054` — Nacelles and Pylons |
| Subsubject namespace | `00`–`99` (reserved) |
| Primary Q-Division | Q-STRUCTURES[^qdiv] |
| Support Q-Divisions | Q-AIR, Q-INDUSTRY, Q-HPC |
| ORB support | ORB-PMO, ORB-FIN, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/054_Nacelles-and-Pylons/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-STRUCTURES` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `00`–`99` shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
