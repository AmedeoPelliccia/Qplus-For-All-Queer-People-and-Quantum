---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-020-020-AIRFRAME-ZONES-ACCESS-AND-WORK-AREA-CONTROL
title: "ATLAS 020-029 · 02.020 · Section 020-020 — Airframe Zones, Access and Work Area Control"
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
local_section_code: "020-020"
ata_sns: "20-20-00"
title_short: "Airframe Zones, Access and Work Area Control"
primary_q_division: Q-GROUND
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-AIR, Q-INDUSTRY, Q-MECHANICS]
governance_class: baseline
version: 1.0.0
status: deprecated
node_class: legacy-deprecated-compatibility-node
language: en
---

# ATLAS 020-029 · 02.020 · 020-020 — Airframe Zones, Access and Work Area Control

> **⚠ DEPRECATED / LEGACY COMPATIBILITY NODE** — See [`README.md`](./README.md) for migration guidance.

## 1. Purpose

Define the airframe zone classification, access panel and door management, and work-area control procedures within ATLAS subsection `020`, aligned to ATA SNS `20-20-00`. Establishes the spatial and procedural framework for controlled access to all airframe work zones.

## 2. Scope

- Defines airframe zone taxonomy (nose, fuselage station bands, wing, empennage, belly fairing) aligned to Q+ATLANTIDE coordinate frames.
- Covers access panel identification, opening/closure procedures, required tooling, and access-door torque schedules.
- Establishes work-area barricading, foreign object debris (FOD) control, and handback verification procedures.
- Applies to all airframe maintenance zones; does not replace aircraft maintenance manual (AMM) access panel task cards.

## 3. System Architecture

```mermaid
graph TD
    A020_020["020-020 Airframe Zones,\nAccess and Work Area Control\n(ATA 20-20-00)"] --> Z1["Zone Taxonomy\nand Boundary Definition"]
    A020_020 --> Z2["Access Panel\nIdentification and Control"]
    A020_020 --> Z3["Work Area Barricading\nand FOD Control"]
    A020_020 --> Z4["Access-door Torque\nSchedule"]
    A020_020 --> Z5["Handback and\nClose-out Verification"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Code range | `020-029` |
| Subsection | `020` — Standard Practices Airframe |
| Local section code | `020-020` |
| ATA SNS | `20-20-00` |
| Primary Q-Division | Q-GROUND |
| Governance class | `baseline` |
| Status | `deprecated` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/020_Standard-Practices-Airframe/` |
| Document | `020-020-Airframe-Zones-Access-and-Work-Area-Control.md` |

## 5. References

- ATA iSpec 2200 — Chapter 20-20, Standard Practices Airframe — Zones and Access
- Subsection index [`./README.md`](./README.md)
- General [`./020-000-General.md`](./020-000-General.md)
