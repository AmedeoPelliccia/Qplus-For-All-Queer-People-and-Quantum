---
document_id: QATL-ATLAS-1000-ATLAS-000-009-00-000-05-DIGITAL-IDENTIFIERS
title: "ATLAS 000-009 · 00.000.05 — Digital Identifiers"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top-Level Architecture System"
master_range: "000–099"
code_range: "000-009"
section: "00"
section_title: "Información General y Servicio"
subject: "00"
subject_title: "General Information"
subsection: "000"
subsection_title: "Identificación"
subsubject: "05"
subsubject_title: "Digital Identifiers"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-GROUND, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# ATLAS 000-009 · Section 00 · Subsection 000 · Subsubject 05 — Digital Identifiers

## 1. Purpose

Defines the **digital-identifier surface** that connects ATLAS hardware identifiers to their digital-thread representations: Digital Product Passport (DPP) hashes, Universal Trace and Data Service (UTDS) hashes, Decentralised Identifier (DID), the Data Module Code (DMC) root used for the airframe in the CSDB[^s1000d], and the S1000D enterprise code derived from the manufacturer designation (subsubject `02`). These identifiers complete the chain from the on-airframe markings of subsubject `04` to the controlled Q+ATLANTIDE baseline[^baseline].

## 2. Scope

- Covers the *Digital Identifiers* subsubject (`05`) of subsection `000` *Identificación* within section `00` *Información General y Servicio*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Identifier classes in scope: **DPP / UTDS hashes** (content-addressed integrity proofs), **DID** (W3C-style decentralised identifier for the airframe), **DMC root** (S1000D `<dmIdent>` `modelIdentCode` for this airframe family) and **S1000D enterprise code** instance.
- Cryptographic and quality-management governance flow from Q+ATLANTIDE and AS9100D[^as9100d]; transport and CSDB packaging follow S1000D Issue 6.0[^s1000d].
- **Co-equality of physical and digital identifiers (canonical declaration).** In Q+ATLANTIDE, the digital identifiers defined here and the physical identifiers defined in [`./004_Serialization-and-Marking.md`](./004_Serialization-and-Marking.md) are **co-equal**: neither is derivative of the other, both are required, and both are auditable.
- Both physical and digital identifier sets shall be kept in sync across the lifecycle (manufacture, entry into service, modification, retirement); a desynchronisation between the two sets is a controlled non-conformance under the Q+ATLANTIDE baseline[^baseline].
- This co-equality is the property that distinguishes Q+ATLANTIDE from a conventional ATA-100-style register — where identification stops at the dataplate — by ensuring every aircraft, configuration and lifecycle event has digital identifiers that anchor evidence chains, ledger entries and DPP traceability.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top-Level Architecture System |
| Master range | `000–099` |
| Code range | `000-009` |
| Section | `00` — Información General y Servicio |
| Subject | `00` — General Information |
| Subsection | `010` — Identificación |
| Subsubject | `05` — Digital Identifiers |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-GROUND, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/000-009_Informacion-General-y-Servicio/000_Identificacion/` |
| Document | `005_Digital-Identifiers.md` (this file) |
| Parent subsection | [`000_Overview.md`](./000_Overview.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **ATLAS §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `000-009` row (Section `00` — Información General y Servicio, Primary Q-Division Q-DATAGOV).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — Bands are classified as `baseline` or `restricted` per Q+ATLANTIDE §4 governance rules.

[^ata2200]: **ATA iSpec 2200 — Information Standards for Aviation Maintenance** — Industry standard for digital aircraft maintenance information; governs chapter / section / subject numbering inherited by ATLAS `000-099`.

[^ataspec100]: **ATA Spec 100 — Manufacturers' Technical Data** — Predecessor numbering scheme that established the 00–99 chapter map mirrored by ATLAS sub-ranges.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used across ATLAS technical publications.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

### Applicable industry standards

The following ATA-family and industry standards apply to this subsubject in addition to the cross-cutting Q+ATLANTIDE governance:

- ATA iSpec 2200 — Information Standards for Aviation Maintenance[^ata2200]
- ATA Spec 100 — Manufacturers' Technical Data[^ataspec100]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
