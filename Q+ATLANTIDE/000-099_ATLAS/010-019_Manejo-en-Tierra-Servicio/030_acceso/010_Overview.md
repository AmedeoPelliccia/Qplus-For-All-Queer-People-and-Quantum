---
document_id: QATL-ATLAS-1000-ATLAS-010-019-01-030-010-OVERVIEW
title: "ATLAS 010-019 · 01.030.010 — acceso"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top-Level Architecture System"
master_range: "000–099"
code_range: "010-019"
section: "01"
section_title: "Manejo en Tierra & Servicio"
subject: "00"
subject_title: "General Information"
subsection: "030"
subsection_title: "acceso"
subsubject: "010"
subsubject_title: "Overview"
primary_q_division: Q-GROUND
support_q_divisions: [Q-MECHANICS, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# ATLAS 010-019 · Section 01 · Subsection 030 — acceso

## 1. Purpose

Overview entry-point for the *acceso* subsection within the `010-019` code range (Section `01` — *Manejo en Tierra & Servicio*) of the **ATLAS** architecture band (*Aircraft Top-Level Architecture System*, master range `000–099`).

This subsubject (`010 Overview`) introduces the ATLAS 010-019.030.010 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §5. *Access* is the precondition for both *ground handling* (subsection `010`) and *servicing* (subsection `020`): you cannot service or maintain what you cannot reach safely. This subsection therefore governs the **physical and procedural opening of the aircraft envelope** that makes presence inside or at compartments possible.

## 2. Scope

- Covers the *acceso* slice of the parent code range `010-019` — i.e. **doors, hatches, panels, access GSE, internal access paths and access-control records** that together constitute the access surface of the aircraft on the ramp, in the hangar and at maintenance bays.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Maps to the following ATA chapters as canonical scope references:
  - **ATA 06 — Dimensions and Areas**[^ata06] for the spatial geometry that defines what is reachable and from where.
  - **ATA 52 — Doors**[^ata52] for the door population (passenger, crew, service, cargo) and their opening sequences/interlocks treated under subsubject `012`.
  - **ATA 50 — Cargo and Accessory Compartments**[^ata50] for cargo-bay and accessory-compartment access treated under subsubjects `012` and `014`.
  - **ATA 25 — Equipment / Furnishings**[^ata25] for cabin access paths, monuments and seating clearance treated under subsubject `014`.
- **Boundary triangulation with sibling subsections `010` and `020`.** The three lead subsections of the `010-019` range form a clean partition of the ramp activity space and are stated symmetrically across all three Overviews:
  - **Ground handling** (`010`) = aircraft *positioning*, *safety perimeter*, GSE *physical placement*. See [`../010_Ground-handling/010_Overview.md`](../010_Ground-handling/010_Overview.md).
  - **Servicing** (`020`) = active *flow through coupling interfaces* (fluids, gases, energy). See [`../020_servicing/010_Overview.md`](../020_servicing/010_Overview.md).
  - **Access** (`030`, this) = *opening the aircraft envelope* to enable presence inside or at compartments.
  Worked examples of the partition: cabin-door opening for boarding belongs to *access*; fuel coupling engagement belongs to *servicing*; GSE positioning at the door belongs to *ground handling*.
- **AMPEL360 LH₂ / fuel-cell bay access is the high-stakes access surface.** Conventional aircraft access procedures do not transfer cleanly: LH₂ bay access has *purge requirements*, *oxygen-depletion risk* and *post-access leak verification* that are absent for kerosene aircraft. Subsubjects `012` and `014` cross-reference the upstream H₂-handling-and-permits baseline at `OPT-INS_FRAMEWORK/I-INFRASTRUCTURES/ATA_85-FUEL_CELL_SYSTEMS_INFRA/85-20-h2-handling-safety-permits-for-fcs/` and the LH₂-storage access procedure at the corresponding ATA 28-10 overlay; this subsection is a *downstream consumer* and shall not redefine those upstream procedures.
- Subsequent subsubjects (`011`–`019`) under this subsection extend this Overview with detailed data modules per S1000D[^s1000d].

## 3. Diagram

The diagram below shows how this subsection's `010 Overview` aggregates the populated subsubjects (`011`–`015`) into the *acceso* slice of ATLAS `010-019` and how each maps to its primary ATA reference.

```mermaid
flowchart LR
    OV[(00 Overview\nATLAS 010-019.01.030)]
    OV --> N01[01 — Scope & Access Boundaries]
    OV --> N02[02 — Doors, Hatches & Panels]
    OV --> N03[03 — Access Equipment, Stands & Ladders]
    OV --> N04[04 — Cabin, Cargo & Compartment Access]
    OV --> N05[05 — Access Control, Authorizations & Records]
    N02 -. ATA 52 / 50 .-> ATA[Access-related ATA overlays\n(ATA 06 / 25 / 50 / 52)]
    N04 -. ATA 25 / 50 .-> ATA
    N02 -. H₂ bay .-> H2[ATA 85-20 H₂ handling\nATA 28-10 LH₂ storage]
    N04 -. fuel-cell bay .-> H2
    N05 -. authorizations .-> SEC[Security domain\n(dual-use records)]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top-Level Architecture System |
| Master range | `000–099` |
| Code range | `010-019` |
| Section | `01` — Manejo en Tierra & Servicio |
| Subject | `00` — General Information |
| Subsection | `030` — acceso |
| Subsubject | `010` — Overview |
| Primary Q-Division | Q-GROUND[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/010-019_Manejo-en-Tierra-Servicio/030_acceso/` |
| Document | `010_Overview.md` (this file) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **ATLAS §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `010-019` row (Section `01` — Manejo en Tierra & Servicio, Primary Q-Division Q-GROUND).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — Bands are classified as `baseline` or `restricted` per Q+ATLANTIDE §4 governance rules.

[^ata06]: **ATA Chapter 06 — Dimensions and Areas** — Industry chapter establishing the spatial geometry of the aircraft (stations, water-lines, buttock-lines, zones); canonical reference for what is physically reachable and from where.

[^ata25]: **ATA Chapter 25 — Equipment / Furnishings** — Industry chapter covering cabin equipment, monuments and furnishings; reference for cabin access paths and clearance.

[^ata50]: **ATA Chapter 50 — Cargo and Accessory Compartments** — Industry chapter covering cargo and accessory-compartment construction and access.

[^ata52]: **ATA Chapter 52 — Doors** — Industry chapter covering passenger, crew, service, cargo and emergency doors, including opening sequences and safety interlocks.

[^ata2200]: **ATA iSpec 2200 — Information Standards for Aviation Maintenance** — Industry standard for digital aircraft maintenance information; governs chapter / section / subject numbering inherited by ATLAS `000-099`.

[^ataspec100]: **ATA Spec 100 — Manufacturers' Technical Data** — Predecessor numbering scheme that established the 00–99 chapter map mirrored by ATLAS sub-ranges.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used across ATLAS technical publications.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

### Applicable industry standards

The following ATA-family and industry standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- ATA Chapter 06 — Dimensions and Areas[^ata06]
- ATA Chapter 25 — Equipment / Furnishings[^ata25]
- ATA Chapter 50 — Cargo and Accessory Compartments[^ata50]
- ATA Chapter 52 — Doors[^ata52]
- ATA iSpec 2200 — Information Standards for Aviation Maintenance[^ata2200]
- ATA Spec 100 — Manufacturers' Technical Data[^ataspec100]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
