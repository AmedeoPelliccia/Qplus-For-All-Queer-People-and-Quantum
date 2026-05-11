---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-023-050-AUDIO-INTEGRATING-SYSTEM
title: "ATLAS 020-029 · 02.023 · Section 023-050 — Audio Integrating System"
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
local_section_code: "023-050"
ata_sns: "23-50-00"
title_short: "Audio Integrating System"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-AIR, Q-HPC, Q-GROUND, Q-MECHANICS, Q-SPACE]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.023 · 023-050 — Audio Integrating System

## 1. Purpose

Define the architecture boundary for the *Audio Integrating System* (ATA 23-50-00) within ATLAS subsection `023`. This section covers the Audio Management Unit (AMU), crew audio control panels (ACP), headset and boom-microphone interfaces, and the centralized audio bus that integrates speech radio, navigation audio, warning tones, and interphone signals.

## 2. Scope

- Aligned to ATA SNS `23-50-00 Audio Integrating System`.
- Covers Audio Management Unit (AMU), Audio Control Panels (ACP) for flight deck stations, boom-microphone / headset interfaces, hot-microphone circuits, navigation audio (VOR/ILS/ADF ident), warning/advisory tone mixing, and passenger address audio feed.
- Interfaces: Speech radios (`023-010`), interphone (`023-040`), PA system (`023-030`), navigation (`034`), and electrical power (`024`).
- Does not cover signal processing algorithms, software certification, or passive attenuator design data (see certified S1000D AMM/CMM data modules).

## 3. System Architecture

```mermaid
graph TD
    A023_050["023-050 Audio Integrating System\n(ATA 23-50-00)"]

    A023_050 --> AMU["Audio Management Unit (AMU)"]
    A023_050 --> ACP["Audio Control Panels\n(Captain / F/O / Observer)"]
    A023_050 --> Headsets["Headset / Boom-Mic\nInterfaces"]
    A023_050 --> NavAudio["Navigation Audio\n(VOR / ILS / ADF ident)"]
    A023_050 --> WarnTones["Warning / Advisory\nTone Mixing"]

    A023_050 -->|radio audio| A023_010["023-010 Speech Communications"]
    A023_050 -->|interphone audio| A023_040["023-040 Interphone / Crew Comms"]
    A023_050 -->|PA audio| A023_030["023-030 Passenger Address"]
    A023_050 -->|nav ident| A034["034 Navigation"]
    A023_050 -->|power supply| A024["024 Electrical Power"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `023` — Communications |
| Local section code | `023-050` |
| ATA SNS | `23-50-00` |
| Primary Q-Division | Q-DATAGOV |
| Support Q-Divisions | Q-AIR, Q-HPC, Q-GROUND, Q-MECHANICS, Q-SPACE |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/023_Communications/` |
| Document | `023-050-Audio-Integrating-System.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 23-50, Audio Integrating System
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `023-010` Speech Communications [`./023-010-Speech-Communications.md`](./023-010-Speech-Communications.md)
- `023-040` Interphone and Crew Communications [`./023-040-Interphone-and-Crew-Communications.md`](./023-040-Interphone-and-Crew-Communications.md)
- `034` Navigation [`../034_Navigation/README.md`](../034_Navigation/README.md)
