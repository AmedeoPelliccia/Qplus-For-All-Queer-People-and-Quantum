---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-029-050-PUMPS-ACCUMULATORS-AND-PRESSURE-CONTROL
title: "ATLAS 020-029 · 02.029 · Section 029-050 — Pumps, Accumulators and Pressure Control"
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
local_section_code: "029-050"
ata_sns: "29-50-00"
title_short: "Pumps, Accumulators and Pressure Control"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: programme-controlled-pumps-extension
status_note: >
  Section 029-050 is a programme-controlled pumps and pressure control
  extension covering detailed pump technology selection, accumulator design,
  pressure regulation architecture, and electrohydrostatic actuator (EHA)
  pump interfaces beyond the baseline ATA 29-10/20 generation scope.
  Activation requires programme authority and is controlled by Q-AIR
  in coordination with Q-MECHANICS.
language: en
---

# ATLAS 020-029 · 02.029 · 029-050 — Pumps, Accumulators and Pressure Control

## 1. Purpose

Define the architecture boundary for *Pumps, Accumulators and Pressure Control* (ATA 29-50-00) within ATLAS subsection `029`. This section covers hydraulic pump technology selection (fixed vs. variable displacement), accumulator design and pre-charge pressure, pressure relief and safety valves, unloading valves, system pressure switch settings, electrohydrostatic actuator (EHA) integrated pump interfaces, and advanced pressure control logic.

> **Programme-controlled pumps extension.** This section covers detailed pump technology, accumulator design parameters, and EHA pump interfaces requiring programme-level authority for definition. Architecture boundary and Q-Division assignments require formal programme review before population of detailed design data modules.

## 2. Scope

- Aligned to ATA SNS `29-50-00 Pumps, Accumulators and Pressure Control` (programme-controlled pumps extension of baseline ATA 29 scope).
- Covers fixed-displacement and variable-displacement pump design parameters, accumulator sizing and nitrogen pre-charge, system pressure relief valves, pressure compensators, thermal relief valves, bypass check valves, EHA pump integration interfaces, and pressure control logic for multi-system hydraulic architectures.
- Does not cover main and auxiliary pump installation boundary (see `029-010`, `029-020`), distribution line routing (see `029-040`), or pump health monitoring (see `029-080`).

## 3. System Architecture

```mermaid
graph TD
    A029_050["029-050 Pumps, Accumulators\nand Pressure Control\n(ATA 29-50-00 — PCE-pumps)"]

    A029_050 --> VarDispPump["Variable-displacement\nPump Architecture"]
    A029_050 --> Accumulator["Hydraulic Accumulators\n(N₂ Pre-charge)"]
    A029_050 --> PressRelief["Pressure Relief\n& Safety Valves"]
    A029_050 --> PressComp["Pressure Compensators\n& Unloading Valves"]
    A029_050 --> EHA_Pump["EHA Integrated\nPump Interfaces"]

    A029_010["029-010 Main Power"] -->|EDP type definition| A029_050
    A029_020["029-020 Aux Power"] -->|EMP type definition| A029_050
    A029_050 -->|accumulator supply| A029_040["029-040 Distribution"]
    A027["027 Flight Controls"] -->|EHA demand| EHA_Pump
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `029` — Hydraulic Power |
| Local section code | `029-050` |
| ATA SNS | `29-50-00` |
| Status | `programme-controlled-pumps-extension` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/029_Hydraulic-Power/` |
| Document | `029-050-Pumps-Accumulators-and-Pressure-Control.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 29-50, Pumps and Accumulators
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `029-000` General [`./029-000-General.md`](./029-000-General.md)
- `029-010` Main Hydraulic Power [`./029-010-Main-Hydraulic-Power.md`](./029-010-Main-Hydraulic-Power.md)
- `029-080` Hydraulic Power Monitoring, Diagnostics and Control Interfaces [`./029-080-Hydraulic-Power-Monitoring-Diagnostics-and-Control-Interfaces.md`](./029-080-Hydraulic-Power-Monitoring-Diagnostics-and-Control-Interfaces.md)
