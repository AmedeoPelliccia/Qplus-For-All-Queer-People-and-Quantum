---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-023-040-INTERPHONE-AND-CREW-COMMUNICATIONS
title: "ATLAS 020-029 · 02.023 · Section 023-040 — Interphone and Crew Communications"
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
local_section_code: "023-040"
ata_sns: "23-40-00"
title_short: "Interphone and Crew Communications"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-AIR, Q-HPC, Q-GROUND, Q-MECHANICS, Q-SPACE]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.023 · 023-040 — Interphone and Crew Communications

## 1. Purpose

Define the architecture boundary for *Interphone and Crew Communications* (ATA 23-40-00) within ATLAS subsection `023`. This section covers flight-deck-to-cabin crew interphone, service interphone, ground crew interphone jacks, and associated handset and call-light systems.

## 2. Scope

- Aligned to ATA SNS `23-40-00 Interphone and Crew Communications`.
- Covers the Passenger Service/Cabin Interphone System (CIDS interface), flight-deck interphone, service interphone panels, ground crew interphone jacks, call lights (attendant call and lavatory call), and hand-microphone/handset interfaces.
- Interfaces: PA system (`023-030`), audio integrating system (`023-050`), electrical power (`024`), and cabin management system.
- Does not cover public address content, IFE systems, or satellite-based crew communications.

## 3. System Architecture

```mermaid
graph TD
    A023_040["023-040 Interphone\nand Crew Communications\n(ATA 23-40-00)"]

    A023_040 --> FlightDeckIP["Flight Deck\nInterphone Unit"]
    A023_040 --> CabinIP["Cabin Interphone\n(CIDS Interface)"]
    A023_040 --> ServiceIP["Service Interphone\nPanels"]
    A023_040 --> GroundIP["Ground Crew\nInterphone Jacks"]
    A023_040 --> CallLights["Call Lights\n(Attendant / Lavatory)"]

    A023_040 -->|PA activation| A023_030["023-030 Passenger Address"]
    A023_040 -->|audio bus| A023_050["023-050 Audio Integrating System"]
    A023_040 -->|power supply| A024["024 Electrical Power"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `023` — Communications |
| Local section code | `023-040` |
| ATA SNS | `23-40-00` |
| Primary Q-Division | Q-DATAGOV |
| Support Q-Divisions | Q-AIR, Q-HPC, Q-GROUND, Q-MECHANICS, Q-SPACE |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/023_Communications/` |
| Document | `023-040-Interphone-and-Crew-Communications.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 23-40, Interphone and Crew Communications
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `023-030` Passenger Address [`./023-030-Passenger-Address-and-Cabin-Communications.md`](./023-030-Passenger-Address-and-Cabin-Communications.md)
- `023-050` Audio Integrating System [`./023-050-Audio-Integrating-System.md`](./023-050-Audio-Integrating-System.md)
