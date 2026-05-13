---
document_id: QATL-ATLAS-1000-ATLAS-010-019-01-016-README
title: "ATLAS 010-019 · 01.016 — Lifting, Shoring and Jacking Procedures (Subsection Index)"
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
subsection: "016"
subsection_title: "Lifting, Shoring and Jacking Procedures"
primary_q_division: Q-GROUND
support_q_divisions: [Q-MECHANICS, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.1.0
status: active
language: en
---

# ATLAS 010-019 · Section 01 · Subsection 016 — Lifting, Shoring and Jacking Procedures

## 1. Purpose

Subsection-level index for *Lifting, Shoring and Jacking Procedures* (`016`) within ATLAS `010-019` — *Manejo en Tierra & Servicio* — Detailed procedures for aircraft jacking, shoring, leveling and structural support operations for AMPEL360 variants.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

> **Orientation layer:** The introductory concepts for this Subject — jack points, jacking sequence, load distribution, leveling references — are in [`../../000-009_Informacion-General-y-Servicio/003_Operaciones-Basicas/005_Lifting-Shoring-and-Jacking-Basics.md`](../../000-009_Informacion-General-y-Servicio/003_Operaciones-Basicas/005_Lifting-Shoring-and-Jacking-Basics.md). This subsection (`016_`) provides the **operational procedure** (Level 2); see the three-level rule in `003_Operaciones-Basicas/000_Overview.md` §2.3.
>
> **Conventional ATA reference:** ATA chapter 7 (Lifting and Shoring) / ATA chapter 8 (Leveling and Weighing). The ATLAS `016_` slot is the programmatic equivalent of those chapters within the `010-019` Code range.

## 2. Scope

- Populates subsubjects `000`–`006` of subsection `016` *Lifting, Shoring and Jacking Procedures*; reserves `007`–`099` for future extension.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Subsubjects populated in this baseline release:
  - `016-000-Lifting-Shoring-Jacking-Procedures-Overview.md` — procedures overview, jack-point map summary, safety prerequisites
  - `016-001-Lifting-Shoring-Jacking-Scope-and-Boundaries.md` — applicability, variant sensitivities, boundary rules
  - `016-002-Jack-Points-Load-Limits-and-Aircraft-Side-Interfaces.md` — approved jack points by variant, structural fittings, load limits
  - `016-003-Jacking-Procedures-and-Sequencing.md` — step-level jacking sequence, safety-collar usage, emergency lower
  - `016-004-Shoring-and-Structural-Support-Procedures.md` — shoring rigs, placement, load-path analysis
  - `016-005-Leveling-Weighing-and-Reference-Datum-Procedures.md` — datum, leveling procedure, weighing procedure, CG calculation
  - `016-006-Lifting-Shoring-Jacking-Records-and-Traceability.md` — sign-off forms, ATLASREC entries, audit trail requirements

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`016-000-Lifting-Shoring-Jacking-Procedures-Overview.md`](./016-000-Lifting-Shoring-Jacking-Procedures-Overview.md) | active |
| 001 | Scope and Lifting, Shoring & Jacking Boundaries | [`016-001-Lifting-Shoring-Jacking-Scope-and-Boundaries.md`](./016-001-Lifting-Shoring-Jacking-Scope-and-Boundaries.md) | active |
| 002 | Jack Points, Load Limits and Aircraft-Side Interfaces | [`016-002-Jack-Points-Load-Limits-and-Aircraft-Side-Interfaces.md`](./016-002-Jack-Points-Load-Limits-and-Aircraft-Side-Interfaces.md) | active |
| 003 | Jacking Procedures and Sequencing | [`016-003-Jacking-Procedures-and-Sequencing.md`](./016-003-Jacking-Procedures-and-Sequencing.md) | active |
| 004 | Shoring and Structural Support Procedures | [`016-004-Shoring-and-Structural-Support-Procedures.md`](./016-004-Shoring-and-Structural-Support-Procedures.md) | active |
| 005 | Leveling, Weighing and Reference Datum Procedures | [`016-005-Leveling-Weighing-and-Reference-Datum-Procedures.md`](./016-005-Leveling-Weighing-and-Reference-Datum-Procedures.md) | active |
| 006 | Lifting, Shoring and Jacking Records and Traceability | [`016-006-Lifting-Shoring-Jacking-Records-and-Traceability.md`](./016-006-Lifting-Shoring-Jacking-Records-and-Traceability.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `010-019` |
| Section | `01` — Manejo en Tierra & Servicio |
| Subsection | `016` — Lifting, Shoring and Jacking Procedures |
| Subsubject namespace | `000`–`006` populated; `007`–`099` reserved |
| Conventional ATA ref | ATA chapters 7 (Lifting and Shoring), 8 (Leveling and Weighing) |
| Primary Q-Division | Q-GROUND[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/010-019_Manejo-en-Tierra-Servicio/016_Lifting-Shoring-Jacking-Procedures/` |
| Document | `README.md` (this file) |
| Orientation layer | [`../../000-009_Informacion-General-y-Servicio/003_Operaciones-Basicas/005_Lifting-Shoring-and-Jacking-Basics.md`](../../000-009_Informacion-General-y-Servicio/003_Operaciones-Basicas/005_Lifting-Shoring-and-Jacking-Basics.md) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-GROUND` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `007`–`099` shall preserve those header fields and reuse the footnote set declared here.

## 6. Change Log

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0.0 | 2026-05-07 | Q+ Team/Amedeo Pelliccia + AI | Initial reserve — subsection index only; all subsubjects `to be populated`. |
| 1.1.0 | 2026-05-07 | Q+ Team/Amedeo Pelliccia + AI | Baseline release — `016-000-Lifting-Shoring-Jacking-Procedures-Overview.md` + subsubjects `001`–`006` populated; subsubject index updated; Scope section revised to reflect populated content. |

## 7. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table). Source of authority for primary/support Q-Divisions and ORB support of this section.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^ata2200]: **ATA iSpec 2200** — Information standards for aviation maintenance documentation. ATA chapter 7 (Lifting and Shoring) and chapter 8 (Leveling and Weighing) are the conventional chapter references for this subsection's scope.

[^ataspec100]: **ATA Spec 100** — Manufacturers' Technical Data standard.

[^s1000d]: **S1000D Issue 6.0** — International specification for technical publications.

[^as9100d]: **AS9100D** — Quality Management Systems — Aviation, Space and Defense Organizations.

### Applicable industry standards

- ATA iSpec 2200 — Information standards for aviation maintenance (ATA chapters 7, 8)[^ata2200]
- ATA Spec 100 — Manufacturers' Technical Data[^ataspec100]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
