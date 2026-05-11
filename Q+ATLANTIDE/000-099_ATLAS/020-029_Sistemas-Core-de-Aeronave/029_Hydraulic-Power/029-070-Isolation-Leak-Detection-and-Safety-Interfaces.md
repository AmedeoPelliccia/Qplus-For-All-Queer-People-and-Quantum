---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-029-070-ISOLATION-LEAK-DETECTION-AND-SAFETY-INTERFACES
title: "ATLAS 020-029 · 02.029 · Section 029-070 — Isolation, Leak Detection and Safety Interfaces"
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
local_section_code: "029-070"
ata_sns: "29-70-00"
title_short: "Isolation, Leak Detection and Safety Interfaces"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.029 · 029-070 — Isolation, Leak Detection and Safety Interfaces

## 1. Purpose

Define the architecture boundary for *Hydraulic Power Isolation, Leak Detection and Safety Interfaces* (ATA 29-70-00) within ATLAS subsection `029`. This section covers hydraulic system isolation valves, fire zone shutoff valve logic, hydraulic leak detection sensors, low-fluid-level warnings, cross-feed and isolation logic, and safety interfaces to fire protection and emergency power systems.

## 2. Scope

- Aligned to ATA SNS `29-70-00 Isolation, Leak Detection and Safety Interfaces`.
- Covers system isolation shutoff valves, fire zone hydraulic isolation valve control, hydraulic fluid leak detection (pressure drop monitoring, visual inspection access panels), low-level fluid warnings, cross-feed isolation logic between hydraulic systems, ground isolation valve for maintenance, and interfaces to fire protection (ATA 26) and emergency electrical power (ATA 24).
- Does not cover main line routing (see `029-040`), pump monitoring (see `029-080`), or fire extinguishing hardware (see `026-020`).

## 3. System Architecture

```mermaid
graph TD
    A029_070["029-070 Isolation, Leak Detection\nand Safety Interfaces\n(ATA 29-70-00)"]

    A029_070 --> IsolationValves["System Isolation\nShutoff Valves"]
    A029_070 --> FireZoneISO["Fire Zone Hydraulic\nIsolation Valve Control"]
    A029_070 --> LeakDetect["Leak Detection\n(Pressure Drop / Visual)"]
    A029_070 --> LowFluidWarn["Low-level Fluid\nWarning"]
    A029_070 --> CrossFeed["Cross-feed &\nIsolation Logic"]

    A026["026 Fire Protection"] -->|fire signal| FireZoneISO
    A029_040["029-040 Distribution"] -->|pressure monitoring| LeakDetect
    A029_030["029-030 Indicating"] -->|low fluid status| LowFluidWarn
    A029_070 -->|isolation command| IsolationValves
    A029_070 -->|safety status| A029_080["029-080 Monitoring\n& Diagnostics"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `029` — Hydraulic Power |
| Local section code | `029-070` |
| ATA SNS | `29-70-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/029_Hydraulic-Power/` |
| Document | `029-070-Isolation-Leak-Detection-and-Safety-Interfaces.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 29-70, Hydraulic Isolation and Leak Detection
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `029-000` General [`./029-000-General.md`](./029-000-General.md)
- `029-040` Hydraulic Distribution, Reservoirs and Lines [`./029-040-Hydraulic-Distribution-Reservoirs-and-Lines.md`](./029-040-Hydraulic-Distribution-Reservoirs-and-Lines.md)
- Section `026-010` Fire and Smoke Detection [`../026_Fire-Protection/026-010-Fire-and-Smoke-Detection.md`](../026_Fire-Protection/026-010-Fire-and-Smoke-Detection.md)
