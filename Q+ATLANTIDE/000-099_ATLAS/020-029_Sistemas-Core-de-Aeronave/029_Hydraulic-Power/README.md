---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-029-README
title: "ATLAS 020-029 · 02.029 — Hydraulic Power (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "020-029"
section: "02"
section_title: "Sistemas Core de Aeronave"
subsection: "029"
subsection_title: "Hydraulic Power"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · Section 02 · Subsection 029 — Hydraulic Power

## 1. Purpose

Subsection-level index for *Hydraulic Power* (`029`) within ATLAS `020-029` — *Sistemas Core de Aeronave* — ATA 29.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Covers the subsubject namespace `000`–`090` of subsection `029` *Hydraulic Power*, aligned to ATA SNS `29-XX-00`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- `primary_q_division: Q-AIR` with support from Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, and Q-INDUSTRY.

## 3. Subsubject Index

| Section Code | ATA SNS | Title | File | Status |
|---|---|---|---|---|
| 029-000 | 29-00-00 | General | [`029-000-General.md`](./029-000-General.md) | baseline |
| 029-010 | 29-10-00 | Main Hydraulic Power | [`029-010-Main-Hydraulic-Power.md`](./029-010-Main-Hydraulic-Power.md) | baseline |
| 029-020 | 29-20-00 | Auxiliary Hydraulic Power | [`029-020-Auxiliary-Hydraulic-Power.md`](./029-020-Auxiliary-Hydraulic-Power.md) | baseline |
| 029-030 | 29-30-00 | Indicating | [`029-030-Indicating.md`](./029-030-Indicating.md) | baseline |
| 029-040 | 29-40-00 | Hydraulic Distribution, Reservoirs and Lines | [`029-040-Hydraulic-Distribution-Reservoirs-and-Lines.md`](./029-040-Hydraulic-Distribution-Reservoirs-and-Lines.md) | programme-controlled-distribution-extension |
| 029-050 | 29-50-00 | Pumps, Accumulators and Pressure Control | [`029-050-Pumps-Accumulators-and-Pressure-Control.md`](./029-050-Pumps-Accumulators-and-Pressure-Control.md) | programme-controlled-pumps-extension |
| 029-060 | 29-60-00 | Hydraulic Fluids, Filters and Servicing | [`029-060-Hydraulic-Fluids-Filters-and-Servicing.md`](./029-060-Hydraulic-Fluids-Filters-and-Servicing.md) | baseline |
| 029-070 | 29-70-00 | Isolation, Leak Detection and Safety Interfaces | [`029-070-Isolation-Leak-Detection-and-Safety-Interfaces.md`](./029-070-Isolation-Leak-Detection-and-Safety-Interfaces.md) | baseline |
| 029-080 | 29-80-00 | Hydraulic Power Monitoring, Diagnostics and Control Interfaces | [`029-080-Hydraulic-Power-Monitoring-Diagnostics-and-Control-Interfaces.md`](./029-080-Hydraulic-Power-Monitoring-Diagnostics-and-Control-Interfaces.md) | programme-controlled-diagnostics-extension |
| 029-090 | 29-90-00 | S1000D CSDB Mapping and Traceability | [`029-090-S1000D-CSDB-Mapping-and-Traceability.md`](./029-090-S1000D-CSDB-Mapping-and-Traceability.md) | programme-controlled-publication-and-traceability-extension |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `029` — Hydraulic Power |
| Subsubject namespace | `000`–`090` |
| Primary Q-Division | Q-AIR[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/029_Hydraulic-Power/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-AIR` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `000`–`090` shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
