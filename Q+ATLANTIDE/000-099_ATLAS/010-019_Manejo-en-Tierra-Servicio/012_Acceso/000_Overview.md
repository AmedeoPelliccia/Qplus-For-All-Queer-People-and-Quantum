---
document_id: QATL-ATLAS-1000-ATLAS-010-019-01-012-000-OVERVIEW
title: "ATLAS 010-019 · 01.012.000 — Acceso"
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
subsection: "012"
subsection_title: "Acceso"
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
# ATLAS 010-019 · Section 01 · Subsection 012 — Acceso

## 1. Purpose

Overview entry-point for the *Acceso* subsection within the `010-019` code range (Section `01` — *Manejo en Tierra & Servicio*) of the **ATLAS** architecture band (*Aircraft Top Level Architecture Schema/System*, master range `000–099`).

This subsubject (`000 Overview`) introduces the ATLAS 010-019.012 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4. It establishes the controlled access vocabulary — scope and boundaries, physical access doors/hatches/panels, access equipment (stands, platforms, ladders), cabin/cargo/compartment access, and access control authorisations and records — used by ground-handling, maintenance, and safety teams during all ground operations.

## 2. Scope

- Covers the *Acceso* slice of the parent code range `010-019`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`001`–`005`) under this subsection extend this Overview with detailed data modules per S1000D[^s1000d]; the populated set in this baseline is `001`–`005`, indexed in [`README.md`](./README.md).
- Concepts in scope across the subsection:
  - **Scope and Access Boundaries** (`001`) — defines the controlled zone perimeters, access categories (interior, exterior, underfloor, avionics bay), and applicable safety rules per ATA iSpec 2200[^ata2200].
  - **Access Doors, Hatches and Panels** (`002`) — location, dimensions, locking mechanisms, opening torque limits, and inspection criteria for all exterior and interior access openings.
  - **Access Equipment — Stands, Platforms and Ladders** (`003`) — approved stand and ladder types, load ratings, positioning procedures, and interface with ATA Spec 100[^ataspec100] GSE requirements.
  - **Cabin, Cargo and Compartment Access** (`004`) — passenger/crew door sequencing, cargo-hold access, avionics-bay entry, and underfloor compartment procedures; S1000D CSDB cross-references.
  - **Access Control, Authorizations and Records** (`005`) — authorisation levels, badge/key management, digital-access logs, and AS9100D[^as9100d] record-retention requirements.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `010-019` |
| Section | `01` — Manejo en Tierra & Servicio |
| Subsection | `012` — Acceso |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-GROUND[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/010-019_Manejo-en-Tierra-Servicio/012_Acceso/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **ATLAS §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `010-019` row (Section `01` — Manejo en Tierra & Servicio, Primary Q-Division Q-GROUND).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ata2200]: **ATA iSpec 2200 — Information Standards for Aviation Maintenance** — Governs aircraft access-zone definition, document structure, and data-module scope for all ATLAS maintenance artefacts.

[^ataspec100]: **ATA Spec 100 — Manufacturers Technical Data** — Baseline standard for aircraft access-point identification and GSE interface conventions.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used for all Q+ATLANTIDE artefacts.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline covering access-control records and documentation retention requirements.

### Applicable industry standards

The following standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- ATA iSpec 2200 — Information Standards for Aviation Maintenance[^ata2200]
- ATA Spec 100 — Manufacturers Technical Data[^ataspec100]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
