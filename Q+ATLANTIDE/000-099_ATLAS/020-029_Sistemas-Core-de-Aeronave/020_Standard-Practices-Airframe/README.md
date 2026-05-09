---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-020-README
title: "ATLAS 020-029 · 02.020 — Standard Practices Airframe (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "020-029"
section: "02"
section_title: "Sistemas Core de Aeronave"
subsection: "020"
subsection_title: "Standard Practices Airframe"
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

Subsection-level index for *Standard Practices Airframe* (`020`) within ATLAS `020-029` — *Sistemas Core de Aeronave* — ATA 20.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Populates the subsubject namespace `00`–`10` of subsection `020` *Standard Practices Airframe* — the common airframe maintenance and standard-practice rules used across aircraft systems and structures.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- This is an umbrella practice node and does not replace detailed ATA/SNS ownership for structural repairs, landing gear, systems, propulsion, avionics or certified task-specific data modules.
- Standard practices defined here are safety-relevant; any maintenance task derived from this subsection requires approved procedure data, correct effectivity, tooling/GSE control, warnings and cautions before hazardous steps, inspection criteria, sign-off evidence and lifecycle traceability.

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 00 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 01 | Standard Practices Airframe — Controlled Definition | [`001_Standard-Practices-Airframe-Controlled-Definition.md`](./001_Standard-Practices-Airframe-Controlled-Definition.md) | active |
| 02 | Airframe General Maintenance Practices | [`002_Airframe-General-Maintenance-Practices.md`](./002_Airframe-General-Maintenance-Practices.md) | active |
| 03 | Airframe Zones, Access and Work Area Control | [`003_Airframe-Zones-Access-and-Work-Area-Control.md`](./003_Airframe-Zones-Access-and-Work-Area-Control.md) | active |
| 04 | Tools, Consumables and GSE Interfaces | [`004_Tools-Consumables-and-GSE-Interfaces.md`](./004_Tools-Consumables-and-GSE-Interfaces.md) | active |
| 05 | Fasteners, Torque, Locking and Retention Practices | [`005_Fasteners-Torque-Locking-and-Retention-Practices.md`](./005_Fasteners-Torque-Locking-and-Retention-Practices.md) | active |
| 06 | Sealing, Bonding, Grounding and Continuity Practices | [`006_Sealing-Bonding-Grounding-and-Continuity-Practices.md`](./006_Sealing-Bonding-Grounding-and-Continuity-Practices.md) | active |
| 07 | Cleaning, Protection and Surface Condition Control | [`007_Cleaning-Protection-and-Surface-Condition-Control.md`](./007_Cleaning-Protection-and-Surface-Condition-Control.md) | active |
| 08 | Inspection, NDT and Damage Reporting Interfaces | [`008_Inspection-NDT-and-Damage-Reporting-Interfaces.md`](./008_Inspection-NDT-and-Damage-Reporting-Interfaces.md) | active |
| 09 | Safety, Warnings, Cautions and Human Factors | [`009_Safety-Warnings-Cautions-and-Human-Factors.md`](./009_Safety-Warnings-Cautions-and-Human-Factors.md) | active |
| 10 | Traceability, Evidence and Lifecycle Governance | [`010_Traceability-Evidence-and-Lifecycle-Governance.md`](./010_Traceability-Evidence-and-Lifecycle-Governance.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `020` — Standard Practices Airframe |
| Subsubject namespace | `00`–`10` (11 subsubjects: 00–10 active) |
| Primary Q-Division | Q-GROUND[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-AIR, Q-INDUSTRY, Q-MECHANICS |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/020_Standard-Practices-Airframe/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-GROUND` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `00`–`10` shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
