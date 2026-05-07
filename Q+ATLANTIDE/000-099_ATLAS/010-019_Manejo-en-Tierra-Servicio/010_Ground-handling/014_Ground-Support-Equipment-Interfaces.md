---
document_id: QATL-ATLAS-1000-ATLAS-010-019-01-010-014-GROUND-SUPPORT-EQUIPMENT-INTERFACES
title: "ATLAS 010-019 · 01.010.014 — Ground Support Equipment Interfaces"
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
subsection: "010"
subsection_title: "Ground handling"
subsubject: "014"
subsubject_title: "Ground Support Equipment Interfaces"
primary_q_division: Q-GROUND
support_q_divisions: [Q-MECHANICS, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# ATLAS 010-019 · Section 01 · Subsection 010 · Subsubject 014 — Ground Support Equipment Interfaces

## 1. Purpose

Defines the **aircraft-side interfaces** that GSE attaches to during ground handling under ATLAS `010-019.010` *Ground handling*: the named connection points (electrical ground-power, pre-conditioned air, low/high-pressure pneumatic, hydraulic ground-rig, fuel coupling, potable water/lavatory, towing fitting, chock points, jacking pads) together with their **physical envelope**, **clearance approach path** and **handshake protocol** with the aircraft's on-board systems. Interface records are anchored to the configuration baseline of subsection `020 configuración`, surfaced as S1000D applicability conditions on the ATA iSpec 2200 / Spec 100 information set[^ata2200][^ataspec100][^s1000d], in conformance with the controlled Q+ATLANTIDE baseline[^baseline] and quality-controlled per AS9100D[^as9100d].

## 2. Scope

- Covers the *Ground Support Equipment Interfaces* subsubject (`014`) of subsection `010` *Ground handling* within section `01` *Manejo en Tierra & Servicio*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable]; Q-GROUND owns the interface catalogue, with Q-MECHANICS consulted on structural attachment and Q-INDUSTRY consulted on GSE supply-side certification.
- Interface classes in scope: **electrical** (28 V DC ground-power, 115/200 V AC ground-power), **pneumatic** (low-pressure air-start, high-pressure air), **environmental** (pre-conditioned air, potable water, lavatory service), **fluid** (fuel coupling, hydraulic ground-rig, oil/oxygen replenishment), **mechanical** (towing fitting, chock points, jacking pads, mooring rings).
- Artefact classes in scope: **Interface Control Document (ICD) per coupling**, **GSE compatibility matrix** (aircraft variant × GSE type), **clearance approach diagram**, **handshake protocol record** (connect → energise → in-service → de-energise → disconnect), **interface-state log**.
- Out of scope: detailed servicing fluids and consumables specifications (subsection `020 servicing`) and GSE catalogue itself (subsection `060 GSE`); cross-references only.

## 3. Diagram

The diagram below shows how a **GSE unit** approaches an aircraft-side **interface coupling** along a controlled **clearance path**, executes the **handshake protocol** and writes an **interface-state log** entry that feeds the documentation chain in subsubject `015`.

```mermaid
flowchart LR
    GSE[GSE Unit] --> CP[Clearance Approach Path]
    CP --> IC[Interface Coupling\nelectrical · pneumatic · fluid · mechanical]
    IC --> HS{{Handshake Protocol\nconnect → energise → in-service → disconnect}}
    HS --> AC[Aircraft On-board System]
    HS --> ISL[Interface-State Log]
    ICD[(Interface Control Document)] --> IC
    CMX[GSE Compatibility Matrix] --> GSE
    ISL --> N05[05 Documentation & Traceability]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top-Level Architecture System |
| Master range | `000–099` |
| Code range | `010-019` |
| Section | `01` — Manejo en Tierra & Servicio |
| Subject | `00` — General Information |
| Subsection | `010` — Ground handling |
| Subsubject | `014` — Ground Support Equipment Interfaces |
| Primary Q-Division | Q-GROUND[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/010-019_Manejo-en-Tierra-Servicio/010_Ground-handling/` |
| Document | `014_Ground-Support-Equipment-Interfaces.md` (this file) |
| Parent subsection | [`010_Overview.md`](./010_Overview.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **ATLAS §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `010-019` row (Section `01` — Manejo en Tierra & Servicio, Primary Q-Division Q-GROUND).

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
