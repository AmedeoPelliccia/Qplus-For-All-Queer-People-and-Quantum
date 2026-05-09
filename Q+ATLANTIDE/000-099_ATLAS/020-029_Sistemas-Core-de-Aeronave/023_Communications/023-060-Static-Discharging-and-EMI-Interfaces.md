---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-023-060-STATIC-DISCHARGING-AND-EMI-INTERFACES
title: "ATLAS 020-029 · 02.023 · Section 023-060 — Static Discharging and EMI Interfaces"
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
subsection: "023"
subsection_title: "Communications"
local_section_code: "023-060"
ata_sns: "23-60-00"
title_short: "Static Discharging and EMI Interfaces"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-AIR, Q-HPC, Q-GROUND, Q-MECHANICS, Q-SPACE]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.023 · 023-060 — Static Discharging and EMI Interfaces

## 1. Purpose

Define the architecture boundary for *Static Discharging and EMI Interfaces* (ATA 23-60-00) within ATLAS subsection `023`. This section covers static discharger systems, electromagnetic interference (EMI) filtering, shielding requirements for communications cabling, and EMC compliance boundaries relevant to communications architecture.

## 2. Scope

- Aligned to ATA SNS `23-60-00 Static Discharging`.
- Covers static wick dischargers, bonding strap network relevant to communications cabling, EMI filters on radio line inputs/outputs, antenna coaxial grounding, and shielding integrity requirements.
- Interfaces: Airframe bonding and grounding practices (`020`), antenna systems for speech (`023-010`) and datalink (`023-080`), and structural bonding (`050`).
- Does not define lightning protection zone (LPZ) analysis, high-intensity radiated fields (HIRF) certification data, or EWIS bundle routing specifications.

## 3. System Architecture

```mermaid
graph TD
    A023_060["023-060 Static Discharging\nand EMI Interfaces\n(ATA 23-60-00)"]

    A023_060 --> Dischargers["Static Wick\nDischargers"]
    A023_060 --> Bonding["Bonding Straps\n(Comms Cabling)"]
    A023_060 --> EMIFilters["EMI Filters\n(Radio Lines)"]
    A023_060 --> CoaxGnd["Antenna Coaxial\nGrounding"]
    A023_060 --> Shielding["Cable Shielding\nIntegrity"]

    A023_060 -->|airframe bonding| A020["020 Standard Practices Airframe"]
    A023_060 -->|antenna interfaces| A023_010["023-010 Speech Communications"]
    A023_060 -->|datalink antenna| A023_080["023-080 SATCOM/Datalink"]
    A023_060 -->|structural bonding| A050["050 Standard Practices Structures"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `023` — Communications |
| Local section code | `023-060` |
| ATA SNS | `23-60-00` |
| Primary Q-Division | Q-DATAGOV |
| Support Q-Divisions | Q-AIR, Q-HPC, Q-GROUND, Q-MECHANICS, Q-SPACE |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/023_Communications/` |
| Document | `023-060-Static-Discharging-and-EMI-Interfaces.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 23-60, Static Discharging
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `020` Standard Practices Airframe [`../020_Standard-Practices-Airframe/README.md`](../020_Standard-Practices-Airframe/README.md)
- `023-010` Speech Communications [`./023-010-Speech-Communications.md`](./023-010-Speech-Communications.md)
- `023-080` SATCOM/ACARS/CPDLC/Datalink [`./023-080-SATCOM-ACARS-CPDLC-and-Datalink-Interfaces.md`](./023-080-SATCOM-ACARS-CPDLC-and-Datalink-Interfaces.md)
