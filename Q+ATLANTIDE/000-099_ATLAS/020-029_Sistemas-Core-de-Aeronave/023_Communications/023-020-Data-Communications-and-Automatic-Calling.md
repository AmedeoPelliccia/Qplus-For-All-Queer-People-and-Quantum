---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-023-020-DATA-COMMUNICATIONS-AND-AUTOMATIC-CALLING
title: "ATLAS 020-029 · 02.023 · Section 023-020 — Data Communications and Automatic Calling"
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
local_section_code: "023-020"
ata_sns: "23-20-00"
title_short: "Data Communications and Automatic Calling"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-AIR, Q-HPC, Q-GROUND, Q-MECHANICS, Q-SPACE]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.023 · 023-020 — Data Communications and Automatic Calling

## 1. Purpose

Define the architecture boundary for *Data Communications and Automatic Calling* (ATA 23-20-00) within ATLAS subsection `023`. This section covers ACARS, VDL Mode 2, automatic aircraft identification, datalink management unit (DMU), and associated ARINC 429/664 bus interfaces.

## 2. Scope

- Aligned to ATA SNS `23-20-00 Data Communications and Automatic Calling`.
- Covers the Datalink Management Unit (DMU/ATSU), Aircraft Communications Addressing and Reporting System (ACARS), VHF Datalink (VDL Mode 2), and automatic calling functions.
- Interfaces: Flight Management System (FMS/ATA 34), CMC/CMS (`041`), SATCOM unit (`023-080`), avionics data busses (ARINC 429, AFDX), and electrical power (`024`).
- Does not define cybersecurity data modules, CPDLC-specific ATC procedures, or SATCOM datalink routing (see `023-080`).

## 3. System Architecture

```mermaid
graph TD
    A023_020["023-020 Data Communications\nand Automatic Calling\n(ATA 23-20-00)"]

    A023_020 --> DMU["Datalink Management Unit\n(DMU / ATSU)"]
    A023_020 --> ACARS["ACARS Functions"]
    A023_020 --> VDL2["VDL Mode 2 Transceiver"]
    A023_020 --> AutoCall["Automatic Calling\nFunctions"]

    A023_020 -->|FMS interfaces| A034["034 Navigation / FMS"]
    A023_020 -->|fault reporting| A041["041 Central Maintenance System"]
    A023_020 -->|SATCOM routing| A023_080["023-080 SATCOM/ACARS/CPDLC Datalink"]
    A023_020 -->|power supply| A024["024 Electrical Power"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `023` — Communications |
| Local section code | `023-020` |
| ATA SNS | `23-20-00` |
| Primary Q-Division | Q-DATAGOV |
| Support Q-Divisions | Q-AIR, Q-HPC, Q-GROUND, Q-MECHANICS, Q-SPACE |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/023_Communications/` |
| Document | `023-020-Data-Communications-and-Automatic-Calling.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 23-20, Data Communications and Automatic Calling
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `023-000` General [`./023-000-General.md`](./023-000-General.md)
- `023-080` SATCOM/ACARS/CPDLC/Datalink [`./023-080-SATCOM-ACARS-CPDLC-and-Datalink-Interfaces.md`](./023-080-SATCOM-ACARS-CPDLC-and-Datalink-Interfaces.md)
- `034` Navigation [`../034_Navigation/README.md`](../034_Navigation/README.md)
