---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-029-020-AUXILIARY-HYDRAULIC-POWER
title: "ATLAS 020-029 · 02.029 · Section 029-020 — Auxiliary Hydraulic Power"
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
subsection: "029"
subsection_title: "Hydraulic Power"
local_section_code: "029-020"
ata_sns: "29-20-00"
title_short: "Auxiliary Hydraulic Power"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.029 · 029-020 — Auxiliary Hydraulic Power

## 1. Purpose

Define the architecture boundary for *Auxiliary Hydraulic Power* (ATA 29-20-00) within ATLAS subsection `029`. This section covers electric motor pumps (EMPs), ram air turbine (RAT) hydraulic power, APU-driven hydraulic generation, and power transfer units (PTUs) that supplement main hydraulic generation under degraded or emergency conditions.

## 2. Scope

- Aligned to ATA SNS `29-20-00 Auxiliary Hydraulic Power`.
- Covers electric motor-driven pumps (AC and DC), ram air turbine hydraulic output, APU-driven hydraulic pump, power transfer unit between hydraulic systems, ground hydraulic power connector, and priority valve logic for auxiliary supply sequencing.
- Does not cover main engine-driven pump systems (see `029-010`), distribution routing (see `029-040`), or extended EMP monitoring beyond auxiliary generation boundary (see `029-080`).

## 3. System Architecture

```mermaid
graph TD
    A029_020["029-020 Auxiliary Hydraulic Power\n(ATA 29-20-00)"]

    A029_020 --> EMP_AC["AC Electric Motor Pump\n(AC EMP)"]
    A029_020 --> EMP_DC["DC Electric Motor Pump\n(DC EMP — Emergency)"]
    A029_020 --> RAT["Ram Air Turbine\n(RAT Hydraulic)"]
    A029_020 --> PTU["Power Transfer Unit\n(PTU)"]
    A029_020 --> APU_Pump["APU-driven Hydraulic Pump"]
    A029_020 --> GndPower["Ground Hydraulic\nPower Connector"]

    A024["024 Electrical Power"] -->|AC/DC bus| EMP_AC
    A024 -->|DC essential bus| EMP_DC
    RAT -->|emergency flow| A029_040["029-040 Distribution"]
    A029_020 -->|auxiliary supply| A029_040
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `029` — Hydraulic Power |
| Local section code | `029-020` |
| ATA SNS | `29-20-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/029_Hydraulic-Power/` |
| Document | `029-020-Auxiliary-Hydraulic-Power.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 29-20, Auxiliary Hydraulic Power
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `029-000` General [`./029-000-General.md`](./029-000-General.md)
- `029-010` Main Hydraulic Power [`./029-010-Main-Hydraulic-Power.md`](./029-010-Main-Hydraulic-Power.md)
