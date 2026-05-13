---
document_id: QATL-ATLAS-1000-ATLAS-010-019-01-013-README
title: "ATLAS 010-019 · 01.013 — Remolque (Subsection Index)"
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
subsection: "013"
subsection_title: "Remolque"
primary_q_division: Q-GROUND
support_q_divisions: [Q-MECHANICS, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.1.0
status: active
language: en
---

# ATLAS 010-019 · Section 01 · Subsection 013 — Remolque

## 1. Purpose

Subsection-level index for *Remolque* (`013`) within ATLAS `010-019` — *Manejo en Tierra & Servicio* — Towing and pushback operations for AMPEL360 aircraft variants on the apron and maintenance areas. This subsection provides the **operational procedure layer** (Level 2) for towing; the introductory orientation is at [`../../000-009_Informacion-General-y-Servicio/003_Operaciones-Basicas/002_Towing-Taxiing-and-Parking.md`](../../000-009_Informacion-General-y-Servicio/003_Operaciones-Basicas/002_Towing-Taxiing-and-Parking.md).

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

> **Conventional ATA reference:** ATA chapter 9 (Towing and Taxiing). The ATLAS `013_` slot is the programmatic equivalent within the `010-019` Code range.

## 2. Scope

- Aggregates the subsubject namespace `000`–`005` of subsection `013` *Remolque*, plus reserves `006`–`099` for future extension.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Anticipated subsubjects (all populated in this release):
  - `013-000-Towing-Overview.md` — subsection map, scope boundaries, Mermaid diagram
  - `013-001-Towing-Scope-and-Boundaries.md` — operation scope, aircraft applicability, exclusions
  - `013-002-Towing-Equipment-and-Tug-Compatibility.md` — towbar / TBL tug specs, bypass pin, GSE qualification
  - `013-003-Towing-Procedures-Pushback-and-Maneuvering.md` — step-level pushback and repositioning sequences
  - `013-004-Towing-Limits-Loads-and-Steering-Constraints.md` — speed, steering angle, load, and gradient limits
  - `013-005-Towing-Records-Incidents-and-Traceability.md` — logbook entries, incident categories, traceability

## 3. Subsubject Index

| 00N | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`013-000-Towing-Overview.md`](./013-000-Towing-Overview.md) | active |
| 001 | Scope and Towing Boundaries | [`013-001-Towing-Scope-and-Boundaries.md`](./013-001-Towing-Scope-and-Boundaries.md) | active |
| 002 | Towing Equipment and Tug Compatibility | [`013-002-Towing-Equipment-and-Tug-Compatibility.md`](./013-002-Towing-Equipment-and-Tug-Compatibility.md) | active |
| 003 | Towing Procedures — Pushback and Maneuvering | [`013-003-Towing-Procedures-Pushback-and-Maneuvering.md`](./013-003-Towing-Procedures-Pushback-and-Maneuvering.md) | active |
| 004 | Towing Limits, Loads and Steering Constraints | [`013-004-Towing-Limits-Loads-and-Steering-Constraints.md`](./013-004-Towing-Limits-Loads-and-Steering-Constraints.md) | active |
| 005 | Towing Records, Incidents and Traceability | [`013-005-Towing-Records-Incidents-and-Traceability.md`](./013-005-Towing-Records-Incidents-and-Traceability.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `010-019` |
| Section | `01` — Manejo en Tierra & Servicio |
| Subsection | `013` — Remolque |
| Subsubject namespace | `000`–`005` populated; `006`–`099` reserved |
| Conventional ATA ref | ATA chapter 9 (Towing and Taxiing) |
| Primary Q-Division | Q-GROUND[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/010-019_Manejo-en-Tierra-Servicio/013_Remolque/` |
| Document | `README.md` (this file) |
| Orientation layer | [`../../000-009_Informacion-General-y-Servicio/003_Operaciones-Basicas/002_Towing-Taxiing-and-Parking.md`](../../000-009_Informacion-General-y-Servicio/003_Operaciones-Basicas/002_Towing-Taxiing-and-Parking.md) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-GROUND` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `006`–`099` shall preserve those header fields, follow the canonical `00N_*.md` naming scheme, and reuse the footnote set declared here.

## 6. Change Log

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0.0 | 2026-05-07 | Q+ Team/Amedeo Pelliccia + AI | Initial reserve — subsection index only, all subsubjects `to be populated`. |
| 1.1.0 | 2026-05-07 | Q+ Team/Amedeo Pelliccia + AI | Baseline release — `013-000-Towing-Overview.md` + subsubjects `001`–`005` populated; ATA chapter 9 reference registered; orientation-layer pointer added. |

## 7. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table). Source of authority for primary/support Q-Divisions and ORB support of this section.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^ata2200]: **ATA iSpec 2200** — Information standards for aviation maintenance documentation. ATA chapter 9 (Towing and Taxiing) is the conventional chapter reference for this subsection's scope.

[^ataspec100]: **ATA Spec 100** — Manufacturers' Technical Data standard.

[^s1000d]: **S1000D Issue 6.0** — International specification for technical publications.

[^as9100d]: **AS9100D** — Quality Management Systems — Aviation, Space and Defense Organizations.

### Applicable industry standards

- ATA iSpec 2200 — Information standards for aviation maintenance (ATA chapter 9)[^ata2200]
- ATA Spec 100 — Manufacturers' Technical Data[^ataspec100]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
