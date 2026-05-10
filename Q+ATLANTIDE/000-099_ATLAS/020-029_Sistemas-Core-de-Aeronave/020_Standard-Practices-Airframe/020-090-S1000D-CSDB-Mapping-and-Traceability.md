---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-020-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY
title: "ATLAS 020-029 · 02.020 · Section 020-090 — S1000D CSDB Mapping and Traceability"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "020-029"
section: "02"
section_title: "Sistemas Core de Aeronave"
subsection: "020"
subsection_title: "Standard Practices Airframe"
local_section_code: "020-090"
ata_sns: "20-90-00"
title_short: "S1000D CSDB Mapping and Traceability"
primary_q_division: Q-GROUND
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-AIR, Q-INDUSTRY, Q-MECHANICS]
governance_class: baseline
version: 1.0.0
status: deprecated
node_class: legacy-deprecated-compatibility-node
status_note: programme-controlled-publication-and-traceability-extension
language: en
---

# ATLAS 020-029 · 02.020 · 020-090 — S1000D CSDB Mapping and Traceability

> **⚠ DEPRECATED / LEGACY COMPATIBILITY NODE** — See [`README.md`](./README.md) for migration guidance.

## 1. Purpose

Provide the S1000D Common Source Database (CSDB) data module code (DMC) mapping, Q+ATLANTIDE URN scheme, and publication traceability index for ATLAS subsection `020` — *Standard Practices Airframe*, aligned to ATA SNS `20-90-00`. Establishes the canonical reference linking each local section code to its S1000D DMC and Q+ATLANTIDE URN.

## 2. Scope

- Maps each `020-XXX` local section code to an S1000D DMC in the form `DMC-QATL-A-20-XX-00-00A-040A-A`.
- Defines the Q+ATLANTIDE URN scheme: `urn:qatl:atlas:020-029:020:{section-code}`.
- Establishes traceability from ATLAS section nodes to S1000D data module types (description, procedure, fault isolation, illustrated parts data).
- This is a `programme-controlled-publication-and-traceability-extension`; the DMC mapping table is the authoritative publication cross-reference for this subsection.
- Does not replace the programme CSDB or S1000D business rules document.

## 3. DMC Mapping Table

| Local Section Code | ATA SNS | Title | S1000D DMC (illustrative) | Q+ATLANTIDE URN |
|---|---|---|---|---|
| 020-000 | 20-00-00 | General | `DMC-QATL-A-20-00-00-00A-040A-A` | `urn:qatl:atlas:020-029:020:000` |
| 020-010 | 20-10-00 | Airframe General Maintenance Practices | `DMC-QATL-A-20-10-00-00A-040A-A` | `urn:qatl:atlas:020-029:020:010` |
| 020-020 | 20-20-00 | Airframe Zones, Access and Work Area Control | `DMC-QATL-A-20-20-00-00A-040A-A` | `urn:qatl:atlas:020-029:020:020` |
| 020-030 | 20-30-00 | Tools, Consumables and GSE Interfaces | `DMC-QATL-A-20-30-00-00A-040A-A` | `urn:qatl:atlas:020-029:020:030` |
| 020-040 | 20-40-00 | Fasteners, Torque, Locking and Retention Practices | `DMC-QATL-A-20-40-00-00A-040A-A` | `urn:qatl:atlas:020-029:020:040` |
| 020-050 | 20-50-00 | Sealing, Bonding, Grounding and Continuity Practices | `DMC-QATL-A-20-50-00-00A-040A-A` | `urn:qatl:atlas:020-029:020:050` |
| 020-060 | 20-60-00 | Cleaning, Protection and Surface Condition Control | `DMC-QATL-A-20-60-00-00A-040A-A` | `urn:qatl:atlas:020-029:020:060` |
| 020-070 | 20-70-00 | Inspection, NDT and Damage Reporting Interfaces | `DMC-QATL-A-20-70-00-00A-040A-A` | `urn:qatl:atlas:020-029:020:070` |
| 020-080 | 20-80-00 | Safety, Warnings, Cautions and Human Factors | `DMC-QATL-A-20-80-00-00A-040A-A` | `urn:qatl:atlas:020-029:020:080` |
| 020-090 | 20-90-00 | S1000D CSDB Mapping and Traceability | `DMC-QATL-A-20-90-00-00A-040A-A` | `urn:qatl:atlas:020-029:020:090` |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Code range | `020-029` |
| Subsection | `020` — Standard Practices Airframe |
| Local section code | `020-090` |
| ATA SNS | `20-90-00` |
| Primary Q-Division | Q-GROUND |
| Governance class | `baseline` |
| Status note | `programme-controlled-publication-and-traceability-extension` |
| Status | `deprecated` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/020_Standard-Practices-Airframe/` |
| Document | `020-090-S1000D-CSDB-Mapping-and-Traceability.md` |

## 5. References

- S1000D Issue 5.0 — Data Module Code (DMC) construction rules
- ATA iSpec 2200 — Chapter 20, Standard Practices — Airframe
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- General [`./020-000-General.md`](./020-000-General.md)
