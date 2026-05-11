---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-024-020-AC-GENERATION
title: "ATLAS 020-029 · 02.024 · Section 024-020 — AC Generation"
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
subsection: "024"
subsection_title: "Electrical Power"
local_section_code: "024-020"
ata_sns: "24-20-00"
title_short: "AC Generation"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.024 · 024-020 — AC Generation

## 1. Purpose

Define the architecture boundary for *AC Generation* (ATA 24-20-00) within ATLAS subsection `024`. This section covers aircraft AC power generation, including main generator output, APU generator, frequency regulation, voltage regulation, and generator control units (GCU).

## 2. Scope

- Aligned to ATA SNS `24-20-00 AC Generation`.
- Covers main AC generators (engine-driven), APU generator, Generator Control Units (GCU), Bus Tie Contactors (BTC), and Solid State Power Controllers (SSPC) for AC channels.
- Includes generator voltage and frequency regulation, parallel operation logic, and load sharing between channels.
- Interfaces: generator drive (`024-010`), AC distribution busses (`024-050`), and aircraft/APU electrical bus control.
- Does not cover DC generation or battery systems (see `024-030`), or external power interface (see `024-040`).

## 3. System Architecture

```mermaid
graph TD
    A024_020["024-020 AC Generation\n(ATA 24-20-00)"]

    A024_020 --> GEN1["Main Generator\nChannel 1 (Engine 1)"]
    A024_020 --> GEN2["Main Generator\nChannel 2 (Engine 2)"]
    A024_020 --> APUGEN["APU Generator"]
    A024_020 --> GCU["Generator Control\nUnits (GCU)"]
    A024_020 --> BTC["Bus Tie\nContactors (BTC)"]

    A024_010["024-010 Generator Drive"] -->|mechanical drive| A024_020
    A024_020 -->|AC power| A024_050["024-050 AC Load Distribution"]
    A024_020 -->|control signals| A024_080["024-080 Monitoring/Diagnostics"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `024` — Electrical Power |
| Local section code | `024-020` |
| ATA SNS | `24-20-00` |
| Primary Q-Division | Q-MECHANICS |
| Support Q-Divisions | Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/024_Electrical-Power/` |
| Document | `024-020-AC-Generation.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 24-20, AC Generation
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `024-010` Generator Drive [`./024-010-Generator-Drive.md`](./024-010-Generator-Drive.md)
- `024-050` AC Electrical Load Distribution [`./024-050-AC-Electrical-Load-Distribution.md`](./024-050-AC-Electrical-Load-Distribution.md)
