---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-020-030-TOOLS-CONSUMABLES-AND-GSE-INTERFACES
title: "ATLAS 020-029 · 02.020 · Section 020-030 — Tools, Consumables and GSE Interfaces"
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
local_section_code: "020-030"
ata_sns: "20-30-00"
title_short: "Tools, Consumables and GSE Interfaces"
primary_q_division: Q-GROUND
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-AIR, Q-INDUSTRY, Q-MECHANICS]
governance_class: baseline
version: 1.0.0
status: deprecated
node_class: legacy-deprecated-compatibility-node
language: en
---

# ATLAS 020-029 · 02.020 · 020-030 — Tools, Consumables and GSE Interfaces

> **⚠ DEPRECATED / LEGACY COMPATIBILITY NODE** — See [`README.md`](./README.md) for migration guidance.

## 1. Purpose

Define the approved tool lists, consumables specifications, and ground support equipment (GSE) interface requirements within ATLAS subsection `020`, aligned to ATA SNS `20-30-00`. Establishes the standard tooling control framework for all airframe maintenance activities.

## 2. Scope

- Defines special tooling, standard tooling, and measurement equipment approved for airframe maintenance.
- Covers consumables classification (sealants, adhesives, lubricants, cleaning agents, thread-locking compounds) with shelf-life and storage controls.
- Establishes GSE interface requirements including jacking points, towing attachment, trestles, and maintenance platforms.
- Applies to all Q-GROUND and Q-MECHANICS maintenance activities; does not replace aircraft maintenance manual (AMM) tooling and consumables tables.

## 3. System Architecture

```mermaid
graph TD
    A020_030["020-030 Tools, Consumables\nand GSE Interfaces\n(ATA 20-30-00)"] --> T1["Approved Special\nTooling Register"]
    A020_030 --> T2["Standard Tooling\nand Measurement Equipment"]
    A020_030 --> T3["Consumables Classification\nand Shelf-life Control"]
    A020_030 --> T4["GSE Interface\nRequirements"]
    A020_030 --> T5["Tooling Calibration\nand Control Traceability"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Code range | `020-029` |
| Subsection | `020` — Standard Practices Airframe |
| Local section code | `020-030` |
| ATA SNS | `20-30-00` |
| Primary Q-Division | Q-GROUND |
| Governance class | `baseline` |
| Status | `deprecated` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/020_Standard-Practices-Airframe/` |
| Document | `020-030-Tools-Consumables-and-GSE-Interfaces.md` |

## 5. References

- ATA iSpec 2200 — Chapter 20-30, Standard Practices Airframe — Tooling and Consumables
- Subsection index [`./README.md`](./README.md)
- General [`./020-000-General.md`](./020-000-General.md)
