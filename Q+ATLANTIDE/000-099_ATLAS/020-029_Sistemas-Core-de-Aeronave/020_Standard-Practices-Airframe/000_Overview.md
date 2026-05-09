---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-020-000-OVERVIEW
title: "ATLAS 020-029 · 02.020.000 — Standard Practices Airframe"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "020-029"
section: "02"
section_title: "Sistemas Core de Aeronave"
subsection: "020"
subsection_title: "Standard Practices Airframe"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-GROUND
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-AIR, Q-INDUSTRY, Q-MECHANICS]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# ATLAS 020-029 · Section 02 · Subsection 020 — Standard Practices Airframe

## 1. Purpose

Overview entry-point for the *Standard Practices Airframe* subsection within the `020-029` code range (Section `02` — *Sistemas Core de Aeronave*) of the **ATLAS** architecture band (*Aircraft Top Level Architecture Schema/System*, master range `000–099`).

This subsubject (`000 Overview`) introduces the ATLAS 020-029.020.000 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the controlled vocabulary, procedural framework, and safety boundaries that govern all common airframe maintenance standard-practice activities within the Q+ATLANTIDE programme — spanning controlled definitions, general maintenance practices, zone and work-area control, tooling and consumables, fastener and torque practices, sealing/bonding/grounding, surface protection, inspection and NDT, safety and human factors, and lifecycle traceability.

This is an umbrella practice node. It does not replace detailed ATA/SNS ownership for structural repairs, landing gear, propulsion, avionics, or certified task-specific data modules; it provides the cross-cutting standard-practice layer that all those domains inherit.

## 2. Scope

- Covers the *Standard Practices Airframe* slice of the parent code range `020-029`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`001`–`010`) under this subsection extend this Overview with detailed data modules; the populated set in this baseline is `001`–`010`, indexed in [`README.md`](./README.md).
- Concepts in scope across the subsection:
  - **Controlled Definition** (`001`) — normative terminology, ATA 20 applicability, and regulatory references per ATA iSpec 2200[^ata2200] and EASA Part 145[^part145].
  - **General Maintenance Practices** (`002`) — universal airframe maintenance procedures, work-card discipline, and task sequencing per ATA iSpec 2200[^ata2200].
  - **Zones, Access and Work Area Control** (`003`) — aircraft zone numbering, access-panel management, and controlled work-area procedures per S1000D[^s1000d].
  - **Tools, Consumables and GSE Interfaces** (`004`) — approved tooling lists, consumable specifications, and GSE mechanical interface requirements per ATA Spec 100[^ataspec100].
  - **Fasteners, Torque, Locking and Retention** (`005`) — fastener standards, torque table conventions, and retention/locking methods per ASME B18[^asmeb18] and FAA AC 43.13[^ac4313].
  - **Sealing, Bonding, Grounding and Continuity** (`006`) — sealant application, electrical bonding paths, and grounding continuity checks per MIL-DTL-81706[^mildtl] and EASA Part 145[^part145].
  - **Cleaning, Protection and Surface Condition** (`007`) — approved cleaning agents, corrosion-inhibiting compounds, and surface-inspection criteria per AMS standards[^ams].
  - **Inspection, NDT and Damage Reporting** (`008`) — general visual inspection protocols, non-destructive testing interfaces, and damage-report linkage per NAS 410[^nas410].
  - **Safety, Warnings, Cautions and Human Factors** (`009`) — safety advisory hierarchy, human-factors controls, and hazardous-task pre-work requirements per EASA Part 145[^part145] and HF guidelines[^hf].
  - **Traceability, Evidence and Lifecycle Governance** (`010`) — sign-off evidence schema, lifecycle record linkage, and digital traceability chain per AS9100D[^as9100d] and S1000D[^s1000d].

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `020` — Standard Practices Airframe |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-GROUND[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-AIR, Q-INDUSTRY, Q-MECHANICS |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/020_Standard-Practices-Airframe/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **ATLAS §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `020-029` row (Section `02` — Sistemas Core de Aeronave, Primary Q-Division Q-GROUND).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ata2200]: **ATA iSpec 2200 — Information Standards for Aviation Maintenance** — Governs document structure, data-module scope, and procedure format for all ATLAS maintenance artefacts.

[^ataspec100]: **ATA Spec 100 — Manufacturers Technical Data** — Baseline standard for document numbering conventions, applicability expressions, and GSE interface specifications.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used for all Q+ATLANTIDE artefacts.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for roles, authorisations, record control, and lifecycle governance.

[^part145]: **EASA Part 145 — Approved Maintenance Organisations** — Regulatory framework for airframe maintenance practices, safety requirements, and personnel authorisation.

[^ac4313]: **FAA AC 43.13-1B/2B — Acceptable Methods, Techniques and Practices: Aircraft Inspection and Repair / Aircraft Alterations** — Advisory circular governing general airframe maintenance practices and fastener/torque standards.

[^asmeb18]: **ASME B18 — Fastener Standards** — Dimensional and material standards for aerospace fasteners referenced in torque and retention practice specifications.

[^mildtl]: **MIL-DTL-81706 — Chemical Conversion Materials for Coating Aluminum** — Specification for surface treatment and bonding preparation materials applied in sealing and grounding practices.

[^ams]: **AMS (SAE Aerospace Material Specifications)** — Material specifications for approved cleaning agents, corrosion-inhibiting compounds, and surface-protection treatments.

[^nas410]: **NAS 410 — Certification & Qualification of Nondestructive Test Personnel** — Standard governing NDT method qualification, inspection protocol classification, and damage-report formatting.

[^hf]: **EASA Human Factors Guidelines for Aircraft Maintenance** — Advisory material on human-factors controls, error management, and safety-advisory hierarchy in maintenance tasks.

### Applicable industry standards

The following standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- ATA iSpec 2200 — Information Standards for Aviation Maintenance[^ata2200]
- ATA Spec 100 — Manufacturers Technical Data[^ataspec100]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
- EASA Part 145 — Approved Maintenance Organisations[^part145]
- FAA AC 43.13-1B/2B — Acceptable Methods, Techniques and Practices[^ac4313]
- ASME B18 — Fastener Standards[^asmeb18]
- MIL-DTL-81706 — Chemical Conversion Materials for Coating Aluminum[^mildtl]
- NAS 410 — Certification & Qualification of NDT Personnel[^nas410]
