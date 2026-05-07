---
document_id: QATL-ATLAS-1000-ATLAS-000-009-00-003-README
title: "ATLAS 000-009 · 00.003 — Operaciones Básicas (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "000-009"
section: "00"
section_title: "Información General y Servicio"
subsection: "003"
subsection_title: "Operaciones Básicas"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-GROUND, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.1.0
status: active
language: en
---

# ATLAS 000-009 · Section 00 · Subsection 003 — Operaciones Básicas

## 1. Purpose

Subsection-level index for *Operaciones Básicas* (`003`) within ATLAS `000-009` — *Información General y Servicio* — the fourth and final subsection of the first Code range of the ATLAS master range. Covers the **introductory-orientation layer** for ground handling, towing, taxiing, parking, mooring, storage, fluids/gases servicing, and lifting/shoring/jacking as they apply to AMPEL360 aircraft variants.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

> **Doctrinal rule — three-level separation of concerns:**
> `003_Operaciones-Basicas/` is **introductory orientation** at the level of the *first* Code range (Información General, `000-009`).
> `010-019_Manejo-en-Tierra-Servicio/` is **detailed operational procedure** at the level of the *second* Code range.
> Published manuals (AMM, GMM, etc.) are the **materialisation** of both layers.
> Three levels, three roles — see `000_Overview.md` §2 for the canonical boundary declaration.

## 2. Scope

- Aggregates the subsubject namespace `000`–`005` of subsection `003` *Operaciones Básicas*, plus reserves `006`–`099` for future extension.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Each subsubject is **introductory only**; the corresponding procedural detail lives in `010-019_Manejo-en-Tierra-Servicio/` (see §5 cross-references).

## 3. Subsubject Index

| 00N | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 001 | Ground Handling Basics | [`001_Ground-Handling-Basics.md`](./001_Ground-Handling-Basics.md) | active |
| 002 | Towing, Taxiing and Parking | [`002_Towing-Taxiing-and-Parking.md`](./002_Towing-Taxiing-and-Parking.md) | active |
| 003 | Mooring, Storage and Return to Service | [`003_Mooring-Storage-and-Return-to-Service.md`](./003_Mooring-Storage-and-Return-to-Service.md) | active |
| 004 | Servicing: Fluids and Gases | [`004_Servicing-Fluids-and-Gases.md`](./004_Servicing-Fluids-and-Gases.md) | active |
| 005 | Lifting, Shoring and Jacking Basics | [`005_Lifting-Shoring-and-Jacking-Basics.md`](./005_Lifting-Shoring-and-Jacking-Basics.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `000-009` |
| Section | `00` — Información General y Servicio |
| Subsection | `003` — Operaciones Básicas |
| Subsubject namespace | `000`–`005` populated; `006`–`099` reserved |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-GROUND, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/000-009_Informacion-General-y-Servicio/003_Operaciones-Basicas/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. Sibling-Subject and Cross-Section Pointers

| Pointer | Target | Relationship |
|---|---|---|
| Preceding sibling | [`../002_Documentacion-General/`](../002_Documentacion-General/) | Documentation General — third Subject in `000-009` |
| Preceding siblings | [`../000_Identificacion/`](../000_Identificacion/), [`../001_Configuracion/`](../001_Configuracion/) | Identification and Configuration — first and second Subjects |
| Procedural detail — ground handling | [`../../010-019_Manejo-en-Tierra-Servicio/010_Ground-handling/`](../../010-019_Manejo-en-Tierra-Servicio/010_Ground-handling/) | `001_` introductory orientation → `010_` operational procedure |
| Procedural detail — servicing | [`../../010-019_Manejo-en-Tierra-Servicio/011_Servicing/`](../../010-019_Manejo-en-Tierra-Servicio/011_Servicing/) | `004_` introductory orientation → `011_` operational procedure |
| Procedural detail — towing | [`../../010-019_Manejo-en-Tierra-Servicio/013_Remolque/`](../../010-019_Manejo-en-Tierra-Servicio/013_Remolque/) | `002_` introductory orientation → `013_` operational procedure |
| Procedural detail — parking/mooring | [`../../010-019_Manejo-en-Tierra-Servicio/014_Parking/`](../../010-019_Manejo-en-Tierra-Servicio/014_Parking/) | `002_`/`003_` introductory orientation → `014_` operational procedure |
| Procedural detail — lifting/shoring/jacking | [`../../010-019_Manejo-en-Tierra-Servicio/016_Lifting-Shoring-Jacking-Procedures/`](../../010-019_Manejo-en-Tierra-Servicio/016_Lifting-Shoring-Jacking-Procedures/) | `005_` introductory orientation → `016_` operational procedure |
| LH₂ servicing detail | `Q+ATLANTIDE/400-499_EPTA/460-469_Propulsion-de-Hidrogeno-y-Celdas-de-Combustible/` | `004_` aircraft-side only; couplings, boil-off in EPTA `460-469_` |
| Variant catalog | [`../001_Configuracion/`](../001_Configuracion/) | `004_` fluid list is variant-dependent; resolve against Configuration Baseline |

## 6. Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-DATAGOV` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `006`–`099` shall preserve those header fields, follow the canonical `00N_*.md` naming scheme, and reuse the footnote set declared here.

## 7. Change Log

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0.0 | 2026-05-07 | Q-DATAGOV | Initial reserve — subsection index only, all subsubjects `to be populated`. |
| 1.1.0 | 2026-05-07 | Q-DATAGOV | Baseline release — `000_Overview.md` + subsubjects `001`–`005` populated; sibling-Subject pointers and doctrinal three-level boundary rule added; `016_Lifting-Shoring-Jacking-Procedures/` registered as cross-ref target in `010-019_`. |

## 8. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table). Source of authority for primary/support Q-Divisions and ORB support of this section.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

### Applicable industry standards

- ATA iSpec 2200 — Information Standards for Aviation Maintenance[^ata2200]
- ATA Spec 100 — Manufacturers' Technical Data[^ataspec100]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]

[^ata2200]: **ATA iSpec 2200** — Information standards for aviation maintenance documentation. Governs data-module structure, ATA chapter mapping, and technical-publication interchange for ATLAS artefacts.

[^ataspec100]: **ATA Spec 100** — Manufacturers' Technical Data standard. Legacy reference for ATA chapter/subject numbering conventions reflected in the ATLAS `000-099` band.

[^s1000d]: **S1000D Issue 6.0** — International specification for technical publications. Common Source DataBase (CSDB) and Data Module Code (DMC) specification used for all Q+ATLANTIDE artefacts.

[^as9100d]: **AS9100D** — Quality Management Systems — Aviation, Space and Defense Organizations. Quality-management baseline for all Q+ATLANTIDE deliverables.
