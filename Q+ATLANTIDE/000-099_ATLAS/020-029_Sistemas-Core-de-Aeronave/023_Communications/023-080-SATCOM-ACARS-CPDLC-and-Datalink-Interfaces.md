---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-023-080-SATCOM-ACARS-CPDLC-AND-DATALINK-INTERFACES
title: "ATLAS 020-029 · 02.023 · Section 023-080 — SATCOM, ACARS, CPDLC and Datalink Interfaces"
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
local_section_code: "023-080"
ata_sns: "23-80-00"
title_short: "SATCOM, ACARS, CPDLC and Datalink Interfaces"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-AIR, Q-HPC, Q-GROUND, Q-MECHANICS, Q-SPACE]
governance_class: baseline
version: 1.0.0
status: programme-controlled-datalink-extension
status_note: >
  Section 023-080 is a programme-controlled datalink extension covering
  SATCOM, ACARS, CPDLC and advanced datalink interfaces. Activation requires
  programme authority and cybersecurity review by Q-DATAGOV.
language: en
---

# ATLAS 020-029 · 02.023 · 023-080 — SATCOM, ACARS, CPDLC and Datalink Interfaces

## 1. Purpose

Define the architecture boundary for *SATCOM, ACARS, CPDLC and Datalink Interfaces* (ATA 23-80-00) within ATLAS subsection `023`. This section covers satellite communications (SATCOM), ACARS routing via SATCOM/HF/VDL, Controller–Pilot Data Link Communications (CPDLC), ADS-C position reporting, and integration with the ATSU/DMU (`023-020`).

> **Programme-controlled datalink extension.** Advanced datalink functions covered here require programme authority, cybersecurity review, and ATC-link authority boundary confirmation before population of detailed architecture data modules.

## 2. Scope

- Aligned to ATA SNS `23-80-00` (programme-controlled datalink extension).
- Covers SATCOM High-Power Amplifier (HPA), Low-Noise Amplifier (LNA), SATCOM system unit (SDU/HSDL), ACARS routing via SATCOM/HF/VHF, CPDLC via FANS-1/A and ATN B1, ADS-C, and integration with ATSU (`023-020`).
- Interfaces: Speech communications (`023-010`), data communications/ACARS (`023-020`), navigation/FMS (`034`), CMC (`041`), cybersecurity domains (`800-899_CYB`), and STA space communications (`150_SATCOM`, `152_Redes-Espaciales`).
- Does not define SATCOM service provider agreements, ATC data-link procedure specifications, or cybersecurity countermeasure data (see CYB band).

## 3. System Architecture

```mermaid
graph TD
    A023_080["023-080 SATCOM / ACARS /\nCPDLC / Datalink\n(ATA 23-80-00 — PCDE)"]

    A023_080 --> SDU["SATCOM System Data Unit\n(SDU / HSDL)"]
    A023_080 --> HPA["High-Power Amplifier (HPA)"]
    A023_080 --> CPDLC["CPDLC\n(FANS-1/A / ATN B1)"]
    A023_080 --> ADSC["ADS-C Position\nReporting"]
    A023_080 --> ACARSRouting["ACARS Routing\n(SATCOM / HF / VDL)"]

    A023_080 -->|ACARS/DMU link| A023_020["023-020 Data Comms / ACARS"]
    A023_080 -->|radio interfaces| A023_010["023-010 Speech Communications"]
    A023_080 -->|FMS position| A034["034 Navigation / FMS"]
    A023_080 -->|fault reporting| A041["041 Central Maintenance System"]
    A023_080 -->|cybersecurity| CYB["800-899 CYB"]
    A023_080 -->|space-comms link| STA150["150 SATCOM (STA)"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `023` — Communications |
| Local section code | `023-080` |
| ATA SNS | `23-80-00` |
| Status | `programme-controlled-datalink-extension` |
| Primary Q-Division | Q-DATAGOV |
| Support Q-Divisions | Q-AIR, Q-HPC, Q-GROUND, Q-MECHANICS, Q-SPACE |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/023_Communications/` |
| Document | `023-080-SATCOM-ACARS-CPDLC-and-Datalink-Interfaces.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 23, Communications (datalink functions)
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `023-020` Data Communications [`./023-020-Data-Communications-and-Automatic-Calling.md`](./023-020-Data-Communications-and-Automatic-Calling.md)
- `034` Navigation / FMS [`../034_Navigation/README.md`](../034_Navigation/README.md)
- STA `150_SATCOM` [`../../../../100-199_STA/150-159_Comunicaciones-Espaciales/150_SATCOM/README.md`](../../../../100-199_STA/150-159_Comunicaciones-Espaciales/150_SATCOM/README.md)
- CYB band `800-899` [`../../../../800-899_CYB/README.md`](../../../../800-899_CYB/README.md)
