---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-023-030-PASSENGER-ADDRESS-AND-CABIN-COMMUNICATIONS
title: "ATLAS 020-029 · 02.023 · Section 023-030 — Passenger Address and Cabin Communications"
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
local_section_code: "023-030"
ata_sns: "23-30-00"
title_short: "Passenger Address and Cabin Communications"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-AIR, Q-HPC, Q-GROUND, Q-MECHANICS, Q-SPACE]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.023 · 023-030 — Passenger Address and Cabin Communications

## 1. Purpose

Define the architecture boundary for *Passenger Address and Cabin Communications* (ATA 23-30-00) within ATLAS subsection `023`. This section covers the Passenger Address and Entertainment (PA) amplifier system, cabin zone loudspeaker distribution, pre-recorded announcement management, and interfaces to the Cabin Management System (CMS).

## 2. Scope

- Aligned to ATA SNS `23-30-00 Passenger Address and Cabin Communications`.
- Covers PA amplifier units, zone amplifiers, cabin loudspeaker networks, pre-recorded announcement system, boarding music, attendant handset PA activation, and CMS integration.
- Interfaces: Cabin interphone (`023-040`), audio integration system (`023-050`), cabin monitoring (`023-070`), flight deck crew alerting (CAP), and electrical power (`024`).
- Does not cover in-flight entertainment (IFE) content distribution or individual passenger seat units.

## 3. System Architecture

```mermaid
graph TD
    A023_030["023-030 Passenger Address\nand Cabin Communications\n(ATA 23-30-00)"]

    A023_030 --> PAAmplifier["PA Amplifier Unit"]
    A023_030 --> ZoneAmplifiers["Zone Amplifiers\n(Forward / Mid / Aft)"]
    A023_030 --> Loudspeakers["Cabin Loudspeaker\nNetwork"]
    A023_030 --> Prerecorded["Pre-recorded\nAnnouncement System"]

    A023_030 -->|crew control| A023_040["023-040 Interphone / Crew Comms"]
    A023_030 -->|audio bus| A023_050["023-050 Audio Integrating System"]
    A023_030 -->|cabin monitoring| A023_070["023-070 Audio-Video / Cabin Monitoring"]
    A023_030 -->|power supply| A024["024 Electrical Power"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `023` — Communications |
| Local section code | `023-030` |
| ATA SNS | `23-30-00` |
| Primary Q-Division | Q-DATAGOV |
| Support Q-Divisions | Q-AIR, Q-HPC, Q-GROUND, Q-MECHANICS, Q-SPACE |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/023_Communications/` |
| Document | `023-030-Passenger-Address-and-Cabin-Communications.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 23-30, Passenger Address and Cabin Communications
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `023-040` Interphone and Crew Communications [`./023-040-Interphone-and-Crew-Communications.md`](./023-040-Interphone-and-Crew-Communications.md)
- `023-050` Audio Integrating System [`./023-050-Audio-Integrating-System.md`](./023-050-Audio-Integrating-System.md)
- `023-070` Audio-Video and Cabin Monitoring [`./023-070-Audio-Video-and-Cabin-Monitoring-Interfaces.md`](./023-070-Audio-Video-and-Cabin-Monitoring-Interfaces.md)
