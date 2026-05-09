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
status: deprecated
node_class: legacy-deprecated-compatibility-node
deprecation_reason: >
  Under the corrected ATLAS 020-029 baseline, code 020 is assigned to
  Air-Conditioning-and-Pressurization. This node is preserved as a historical
  alias and migration reference only. New controlled content shall not be
  authored under this path.
replacement_paths:
  corrected_020_node: "Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/021_Air-Conditioning-and-Pressurization/"
  standard_practices_structures: "Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras-Primarias-e-Interfaces-de-Programa-Q-Division/050_Standard-Practices-Structures/"
migration_policy: >
  Preserve this breakdown only as a historical alias, compatibility bridge,
  and migration reference. New controlled content shall be authored under
  050_Standard-Practices-Structures/. Cross-references in the 020-029
  range pointing to this node shall be redirected to 021_Air-Conditioning-and-Pressurization/.
language: en
---

# ATLAS 020-029 · Section 02 · Subsection 020 — Standard Practices Airframe *(Deprecated — Legacy Compatibility Node)*

## ⚠ Deprecation Notice

> **This subsection is a legacy / deprecated compatibility node.**
>
> Under the corrected ATLAS 020-029 baseline, the local code `020` is assigned to **Air-Conditioning-and-Pressurization** (ATA 21). *Standard Practices Airframe* (ATA 20) shall not remain the active `020` node inside *Sistemas Core de Aeronave*.
>
> **Migration targets:**
> - Active Air Conditioning content → [`021_Air-Conditioning-and-Pressurization/`](../021_Air-Conditioning-and-Pressurization/README.md)
> - Standard Practices Structures (canonical) → `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras-Primarias-e-Interfaces-de-Programa-Q-Division/050_Standard-Practices-Structures/`
>
> This breakdown is preserved as a historical alias and compatibility bridge. New controlled content shall not be authored here.

## 1. Purpose

Subsection-level index for *Standard Practices Airframe* (`020`) within ATLAS `020-029` — *Sistemas Core de Aeronave* — ATA 20. This node is preserved as a **legacy compatibility bridge** only.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- ~~Populates the subsubject namespace `00`–`10` of subsection `020` *Standard Practices Airframe*~~ — preserved as a historical alias and migration reference.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- This is an umbrella practice node and does not replace detailed ATA/SNS ownership for structural repairs, landing gear, systems, propulsion, avionics or certified task-specific data modules.
- Standard practices defined here are safety-relevant; any maintenance task derived from this subsection requires approved procedure data, correct effectivity, tooling/GSE control, warnings and cautions before hazardous steps, inspection criteria, sign-off evidence and lifecycle traceability.

## 3. Section Index (ATA-SNS-Aligned — Legacy Compatibility Breakdown)

| Local Section Code | ATA SNS | Title | Document | Status |
|---|---|---|---|---|
| 020-000 | 20-00-00 | General | [`020-000-General.md`](./020-000-General.md) | deprecated |
| 020-010 | 20-10-00 | Airframe General Maintenance Practices | [`020-010-Airframe-General-Maintenance-Practices.md`](./020-010-Airframe-General-Maintenance-Practices.md) | deprecated |
| 020-020 | 20-20-00 | Airframe Zones, Access and Work Area Control | [`020-020-Airframe-Zones-Access-and-Work-Area-Control.md`](./020-020-Airframe-Zones-Access-and-Work-Area-Control.md) | deprecated |
| 020-030 | 20-30-00 | Tools, Consumables and GSE Interfaces | [`020-030-Tools-Consumables-and-GSE-Interfaces.md`](./020-030-Tools-Consumables-and-GSE-Interfaces.md) | deprecated |
| 020-040 | 20-40-00 | Fasteners, Torque, Locking and Retention Practices | [`020-040-Fasteners-Torque-Locking-and-Retention-Practices.md`](./020-040-Fasteners-Torque-Locking-and-Retention-Practices.md) | deprecated |
| 020-050 | 20-50-00 | Sealing, Bonding, Grounding and Continuity Practices | [`020-050-Sealing-Bonding-Grounding-and-Continuity-Practices.md`](./020-050-Sealing-Bonding-Grounding-and-Continuity-Practices.md) | deprecated |
| 020-060 | 20-60-00 | Cleaning, Protection and Surface Condition Control | [`020-060-Cleaning-Protection-and-Surface-Condition-Control.md`](./020-060-Cleaning-Protection-and-Surface-Condition-Control.md) | deprecated |
| 020-070 | 20-70-00 | Inspection, NDT and Damage Reporting Interfaces | [`020-070-Inspection-NDT-and-Damage-Reporting-Interfaces.md`](./020-070-Inspection-NDT-and-Damage-Reporting-Interfaces.md) | deprecated |
| 020-080 | 20-80-00 | Safety, Warnings, Cautions and Human Factors | [`020-080-Safety-Warnings-Cautions-and-Human-Factors.md`](./020-080-Safety-Warnings-Cautions-and-Human-Factors.md) | deprecated |
| 020-090 | 20-90-00 | S1000D CSDB Mapping and Traceability | [`020-090-S1000D-CSDB-Mapping-and-Traceability.md`](./020-090-S1000D-CSDB-Mapping-and-Traceability.md) | deprecated |

### Legacy Subsubject Files (Preserved for Migration Reference)

| NN | Title | Document |
|---:|---|---|
| 00 | Overview | [`000_Overview.md`](./000_Overview.md) |
| 01 | Standard Practices Airframe — Controlled Definition | [`001_Standard-Practices-Airframe-Controlled-Definition.md`](./001_Standard-Practices-Airframe-Controlled-Definition.md) |
| 02 | Airframe General Maintenance Practices | [`002_Airframe-General-Maintenance-Practices.md`](./002_Airframe-General-Maintenance-Practices.md) |
| 03 | Airframe Zones, Access and Work Area Control | [`003_Airframe-Zones-Access-and-Work-Area-Control.md`](./003_Airframe-Zones-Access-and-Work-Area-Control.md) |
| 04 | Tools, Consumables and GSE Interfaces | [`004_Tools-Consumables-and-GSE-Interfaces.md`](./004_Tools-Consumables-and-GSE-Interfaces.md) |
| 05 | Fasteners, Torque, Locking and Retention Practices | [`005_Fasteners-Torque-Locking-and-Retention-Practices.md`](./005_Fasteners-Torque-Locking-and-Retention-Practices.md) |
| 06 | Sealing, Bonding, Grounding and Continuity Practices | [`006_Sealing-Bonding-Grounding-and-Continuity-Practices.md`](./006_Sealing-Bonding-Grounding-and-Continuity-Practices.md) |
| 07 | Cleaning, Protection and Surface Condition Control | [`007_Cleaning-Protection-and-Surface-Condition-Control.md`](./007_Cleaning-Protection-and-Surface-Condition-Control.md) |
| 08 | Inspection, NDT and Damage Reporting Interfaces | [`008_Inspection-NDT-and-Damage-Reporting-Interfaces.md`](./008_Inspection-NDT-and-Damage-Reporting-Interfaces.md) |
| 09 | Safety, Warnings, Cautions and Human Factors | [`009_Safety-Warnings-Cautions-and-Human-Factors.md`](./009_Safety-Warnings-Cautions-and-Human-Factors.md) |
| 10 | Traceability, Evidence and Lifecycle Governance | [`010_Traceability-Evidence-and-Lifecycle-Governance.md`](./010_Traceability-Evidence-and-Lifecycle-Governance.md) |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `020` — Standard Practices Airframe |
| Section file namespace | `020-000` – `020-090` (ATA-SNS-aligned, 10 section files) |
| Legacy subsubject namespace | `00`–`10` (11 legacy subsubjects preserved for migration reference) |
| Primary Q-Division | Q-GROUND[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-AIR, Q-INDUSTRY, Q-MECHANICS |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Node class | `legacy-deprecated-compatibility-node` |
| Status | `deprecated` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/020_Standard-Practices-Airframe/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. This subsection is a **deprecated / legacy compatibility node**. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-GROUND` and `governance_class = baseline` from the parent ATLAS section. Extensions added under this node shall preserve those header fields but shall include `status: deprecated` and `node_class: legacy-deprecated-compatibility-node`. New controlled content shall be authored under the migration targets stated in the deprecation notice above.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
