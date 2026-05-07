---
document_id: QATL-ATLAS-1000-ATLAS-000-009-00-000-000-OVERVIEW
title: "ATLAS 000-009 · 00.000.000 — Identificación"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "000-009"
section: "00"
section_title: "Información General y Servicio"
subsection: "000"
subsection_title: "Identificación"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-GROUND, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# ATLAS 000-009 · Section 00 · Subsection 000 — Identificación

## 1. Purpose

Overview entry-point for the *Identificación* subsection within the `000-009` code range (Section `00` — *Información General y Servicio*) of the **ATLAS** architecture band (*Aircraft Top Level Architecture Schema/System*, master range `000–099`).

This subsubject (`000 Overview`) introduces the ATLAS 000-009.000.000 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4. It establishes the controlled identity vocabulary — aircraft type designation, manufacturer codes, configuration identification, serialisation and marking, and digital identifiers — that every other ATLAS section depends on to trace data to a specific aircraft and configuration.

## 2. Scope

- Covers the *Identificación* slice of the parent code range `000-009`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`001`–`005`) under this subsection extend this Overview with detailed data modules per S1000D[^s1000d]; the populated set in this baseline is `001`–`005`, indexed in [`README.md`](./README.md).
- Concepts in scope across the subsection:
  - **Aircraft Identification** (`001`) — ICAO type designator, IATA code, FAA designator, and model designation as defined in ATA iSpec 2200[^ata2200].
  - **Manufacturer Designation** (`002`) — CAGE code, DUNS/LEI, and the Q+ATLANTIDE manufacturer registry entry.
  - **Configuration Identification** (`003`) — effectivity expressions, modification incorporation status, and variant labelling per ATA Spec 100[^ataspec100].
  - **Serialization and Marking** (`004`) — Manufacturer Serial Number (MSN), line number, physical marking requirements, and part marking per AS9100D[^as9100d].
  - **Digital Identifiers** (`005`) — S1000D Data Module Code (DMC), Unique Identifier (UID) per ISO 15459[^iso15459], and Q+ATLANTIDE-specific URNs used to cross-link all artefacts in the ATLAS-1000 register.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `000-009` |
| Section | `00` — Información General y Servicio |
| Subsection | `000` — Identificación |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-GROUND, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/000-009_Informacion-General-y-Servicio/000_Identificacion/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **ATLAS §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `000-009` row (Section `00` — Información General y Servicio, Primary Q-Division Q-DATAGOV).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ata2200]: **ATA iSpec 2200 — Information Standards for Aviation Maintenance** — Governs aircraft type designation, document structure, and data-module scope for all ATLAS maintenance artefacts.

[^ataspec100]: **ATA Spec 100 — Manufacturers Technical Data** — Baseline standard for aircraft type designation and manufacturer code conventions.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used for all Q+ATLANTIDE artefacts.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline covering serialisation and marking requirements.

[^iso15459]: **ISO 15459 — Unique Identification of Transport Units and Unit Loads** — Unique identifier (UID) standard applied to aircraft, parts, and assemblies.

### Applicable industry standards

The following standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- ATA iSpec 2200 — Information Standards for Aviation Maintenance[^ata2200]
- ATA Spec 100 — Manufacturers Technical Data[^ataspec100]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
- ISO 15459 — Unique Identification of Transport Units and Unit Loads[^iso15459]
