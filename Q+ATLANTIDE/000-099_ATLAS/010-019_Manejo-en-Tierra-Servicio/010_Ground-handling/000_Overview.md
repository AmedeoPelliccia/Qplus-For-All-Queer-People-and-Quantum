---
document_id: QATL-ATLAS-1000-ATLAS-010-019-01-010-000-OVERVIEW
title: "ATLAS 010-019 · 01.010.000 — Ground Handling"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "010-019"
section: "01"
section_title: "Manejo en Tierra & Servicio"
subsection: "010"
subsection_title: "Ground Handling"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-GROUND
support_q_divisions: [Q-MECHANICS, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# ATLAS 010-019 · Section 01 · Subsection 010 — Ground Handling

## 1. Purpose

Overview entry-point for the *Ground Handling* subsection within the `010-019` code range (Section `01` — *Manejo en Tierra & Servicio*) of the **ATLAS** architecture band (*Aircraft Top Level Architecture Schema/System*, master range `000–099`).

This subsubject (`000 Overview`) introduces the ATLAS 010-019.010.000 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4. It establishes the controlled vocabulary and procedural framework — scope and definitions, roles and authorisations, safety zones, GSE interfaces, and documentation traceability — that governs all ground-handling activities within the Q+ATLANTIDE programme.

## 2. Scope

- Covers the *Ground Handling* slice of the parent code range `010-019`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`001`–`005`) under this subsection extend this Overview with detailed data modules per S1000D[^s1000d]; the populated set in this baseline is `001`–`005`, indexed in [`README.md`](./README.md).
- Concepts in scope across the subsection:
  - **Scope and Definitions** (`001`) — normative terminology, applicability limits, and regulatory references per ATA iSpec 2200[^ata2200].
  - **Roles, Authorizations and Responsibilities** (`002`) — ground-crew roles, authorisation matrix, and competency requirements per AS9100D[^as9100d].
  - **Safety Zones, Hazards and Exclusion Areas** (`003`) — demarcation of exclusion zones, hazard identification, and emergency egress routes per ICAO Doc 9137[^icaodoc9137].
  - **Ground Support Equipment Interfaces** (`004`) — mechanical, electrical, and pneumatic interface specifications between the aircraft and GSE per ATA Spec 100[^ataspec100].
  - **Documentation, Logs and Traceability** (`005`) — record-keeping obligations, log formats, and digital traceability links per S1000D[^s1000d] and ISO 15459[^iso15459].

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `010-019` |
| Section | `01` — Manejo en Tierra & Servicio |
| Subsection | `010` — Ground Handling |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-GROUND[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/010-019_Manejo-en-Tierra-Servicio/010_Ground-handling/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **ATLAS §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `010-019` row (Section `01` — Manejo en Tierra & Servicio, Primary Q-Division Q-GROUND).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ata2200]: **ATA iSpec 2200 — Information Standards for Aviation Maintenance** — Governs ground-handling document structure, data-module scope, and procedure format for all ATLAS maintenance artefacts.

[^ataspec100]: **ATA Spec 100 — Manufacturers Technical Data** — Baseline standard for GSE interface specification and manufacturer code conventions.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used for all Q+ATLANTIDE artefacts.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for roles, authorisations, and competency management in ground handling.

[^icaodoc9137]: **ICAO Doc 9137 — Airport Services Manual** — Authoritative reference for ground-handling safety zones, exclusion areas, and hazard classification at aerodrome.

[^iso15459]: **ISO 15459 — Unique Identification of Transport Units and Unit Loads** — UID standard applied to ground-handling records and log traceability.

### Applicable industry standards

The following standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- ATA iSpec 2200 — Information Standards for Aviation Maintenance[^ata2200]
- ATA Spec 100 — Manufacturers Technical Data[^ataspec100]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
- ICAO Doc 9137 — Airport Services Manual[^icaodoc9137]
- ISO 15459 — Unique Identification of Transport Units and Unit Loads[^iso15459]
