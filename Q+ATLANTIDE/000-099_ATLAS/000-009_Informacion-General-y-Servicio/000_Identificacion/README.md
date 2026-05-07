---
document_id: QATL-ATLAS-1000-ATLAS-000-009-00-000-README
title: "ATLAS 000-009 · 00.000 — Identificación (Subsection Index)"
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
subsection: "000"
subsection_title: "Identificación"
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

Subsection-level index for *Identificación* (`000`) within ATLAS `000-009` — *Información General y Servicio*. Covers aircraft type designation, manufacturer codes, configuration identification, serialisation and physical marking, and the full suite of digital identifiers (URNs, DMC codes, UUIDs) used across the Q+ATLANTIDE documentation ecosystem.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Covers the full subsubject namespace `000`–`009` of subsection `000` *Identificación*; subsubjects `001`–`005` are populated in this baseline release, the remaining `006`–`009` slots remain available for future extension per the Overview's authorisation[^archtable].
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Governs the controlled identity vocabulary for the entire ATLAS `000–099` band: every other section and subsection that references an aircraft, serial number, or document identifier traces back to the definitions established here.

## 3. Subsubject Index

| 00N | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 001 | Aircraft Identification | [`001_Aircraft-Identification.md`](./001_Aircraft-Identification.md) | active |
| 002 | Manufacturer Designation | [`002_Manufacturer-Designation.md`](./002_Manufacturer-Designation.md) | active |
| 003 | Configuration Identification | [`003_Configuration-Identification.md`](./003_Configuration-Identification.md) | active |
| 004 | Serialization and Marking | [`004_Serialization-and-Marking.md`](./004_Serialization-and-Marking.md) | active |
| 005 | Digital Identifiers | [`005_Digital-Identifiers.md`](./005_Digital-Identifiers.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `000-009` |
| Section | `00` — Información General y Servicio |
| Subsection | `000` — Identificación |
| Subsubject namespace | `000`–`009` (`000` + `001`–`005` populated; canonical `00N_*.md` scheme) |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-GROUND, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/000-009_Informacion-General-y-Servicio/000_Identificacion/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-DATAGOV` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `006`–`009` shall preserve those header fields, follow the canonical `00N_*.md` naming scheme, and reuse the footnote set declared below.

## 6. Downstream and Cross-Subsection Dependencies

The identity vocabulary defined in this subsection is consumed by:

- **Within `000-009`** — `001_Configuracion/` (effectivity and mod status reference aircraft identification and MSN), `002_Documentacion-General/` (all document identifiers reference the digital-identifier scheme in `005_`), `003_Operaciones-Basicas/` (operational procedures reference type designation and configuration).
- **Across ATLAS `000–099`** — every subsequent section references the aircraft type designation, MSN, and DMC/URN scheme established here to trace maintenance data, illustrated parts, and wiring to a specific configuration and serial number.

## 7. Change Log

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0.0 | 2026-05-07 | Q-DATAGOV | Initial baseline: `000_Overview.md` plus subsubjects `001`–`005`, using the sequential `00N_*.md` scheme under the `000_Identificacion/` subsection. Subsection index established. |

## 8. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `000-009` row (Section `00` — Información General y Servicio, Primary Q-Division Q-DATAGOV).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^ata2200]: **ATA iSpec 2200 — Information Standards for Aviation Maintenance** — Governs document structure and data modules for all ATLAS maintenance artefacts.

[^ataspec100]: **ATA Spec 100 — Manufacturers Technical Data** — Baseline standard for aircraft type designation and manufacturer code conventions used in this subsection.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used for all Q+ATLANTIDE artefacts.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

### Applicable industry standards

The following standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- ATA iSpec 2200 — Information Standards for Aviation Maintenance[^ata2200]
- ATA Spec 100 — Manufacturers Technical Data[^ataspec100]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
