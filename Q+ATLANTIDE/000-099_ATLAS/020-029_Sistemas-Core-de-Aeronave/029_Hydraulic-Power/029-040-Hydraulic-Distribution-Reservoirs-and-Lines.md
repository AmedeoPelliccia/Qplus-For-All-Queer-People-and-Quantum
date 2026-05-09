---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-029-040-HYDRAULIC-DISTRIBUTION-RESERVOIRS-AND-LINES
title: "ATLAS 020-029 · 02.029 · Section 029-040 — Hydraulic Distribution, Reservoirs and Lines"
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
local_section_code: "029-040"
ata_sns: "29-40-00"
title_short: "Hydraulic Distribution, Reservoirs and Lines"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: programme-controlled-distribution-extension
status_note: >
  Section 029-040 is a programme-controlled distribution extension covering
  detailed hydraulic distribution routing, reservoir design specifications,
  return line and case drain architecture beyond the baseline ATA 29-10/20
  scope. Activation requires programme authority and is controlled by Q-AIR
  in coordination with Q-MECHANICS.
language: en
---

# ATLAS 020-029 · 02.029 · 029-040 — Hydraulic Distribution, Reservoirs and Lines

## 1. Purpose

Define the architecture boundary for *Hydraulic Distribution, Reservoirs and Lines* (ATA 29-40-00) within ATLAS subsection `029`. This section covers reservoir design, pressurisation interfaces, distribution line routing, check valves, priority valves, selector valves, return lines, case drain lines, and the structural routing interfaces for hydraulic supply to all consumer systems.

> **Programme-controlled distribution extension.** This section covers detailed hydraulic distribution architecture requiring programme-level authority for line routing design, structural integration, and fire zone penetration definition. Architecture boundary and Q-Division assignments require formal programme review before population of detailed design data modules.

## 2. Scope

- Aligned to ATA SNS `29-40-00 Hydraulic Distribution` (programme-controlled distribution extension of baseline ATA 29 scope).
- Covers main and auxiliary reservoirs, reservoir pressurisation by bleed air, hydraulic supply lines to actuators and services, return lines and manifolds, case drain lines, check valves, priority valves and selector valves, ground service panel connections, fire zone hydraulic line shutoff valves, and structural clamp and bracket interfaces.
- Does not cover pump hardware (see `029-010`, `029-020`), fluid servicing procedures (see `029-060`), or isolation and leak detection logic (see `029-070`).

## 3. System Architecture

```mermaid
graph TD
    A029_040["029-040 Hydraulic Distribution,\nReservoirs and Lines\n(ATA 29-40-00 — PCE-dist)"]

    A029_040 --> Reservoir["Main & Aux Reservoirs\n(Pressurised by bleed air)"]
    A029_040 --> SupplyLines["Supply Lines &\nManifolds"]
    A029_040 --> ReturnLines["Return Lines &\nCase Drains"]
    A029_040 --> CheckValves["Check Valves &\nPriority Valves"]
    A029_040 --> FireShutoff["Fire Zone\nShutoff Valves"]

    A029_010["029-010 Main Power"] -->|high-pressure supply| A029_040
    A029_020["029-020 Aux Power"] -->|auxiliary supply| A029_040
    A029_040 -->|actuator supply| A027["027 Flight Controls"]
    A029_040 -->|utility supply| LandingGear["Landing Gear Systems"]
    A029_040 -->|braking supply| Brakes["Brakes & Steering"]
    A026["026 Fire Protection"] -->|fire zone interface| FireShutoff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `029` — Hydraulic Power |
| Local section code | `029-040` |
| ATA SNS | `29-40-00` |
| Status | `programme-controlled-distribution-extension` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/029_Hydraulic-Power/` |
| Document | `029-040-Hydraulic-Distribution-Reservoirs-and-Lines.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 29-40, Hydraulic Distribution
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `029-000` General [`./029-000-General.md`](./029-000-General.md)
- `029-010` Main Hydraulic Power [`./029-010-Main-Hydraulic-Power.md`](./029-010-Main-Hydraulic-Power.md)
- `029-070` Isolation, Leak Detection and Safety Interfaces [`./029-070-Isolation-Leak-Detection-and-Safety-Interfaces.md`](./029-070-Isolation-Leak-Detection-and-Safety-Interfaces.md)
