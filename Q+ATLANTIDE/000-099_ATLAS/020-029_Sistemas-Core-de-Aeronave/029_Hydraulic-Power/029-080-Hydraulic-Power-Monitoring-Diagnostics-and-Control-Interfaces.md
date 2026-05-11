---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-029-080-HYDRAULIC-POWER-MONITORING-DIAGNOSTICS-AND-CONTROL-INTERFACES
title: "ATLAS 020-029 · 02.029 · Section 029-080 — Hydraulic Power Monitoring, Diagnostics and Control Interfaces"
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
local_section_code: "029-080"
ata_sns: "29-80-00"
title_short: "Hydraulic Power Monitoring, Diagnostics and Control Interfaces"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: programme-controlled-diagnostics-extension
status_note: >
  Section 029-080 is a programme-controlled diagnostics extension covering
  hydraulic system health monitoring, BITE diagnostics for pumps, valves,
  accumulators, and filters, plus CMS control interfaces beyond the baseline
  ATA 29 scope. Activation requires programme authority and is controlled
  by Q-AIR in coordination with Q-MECHANICS and Q-DATAGOV.
language: en
---

# ATLAS 020-029 · 02.029 · 029-080 — Hydraulic Power Monitoring, Diagnostics and Control Interfaces

## 1. Purpose

Define the architecture boundary for *Hydraulic Power Monitoring, Diagnostics and Control Interfaces* (ATA 29-80-00) within ATLAS subsection `029`. This section covers hydraulic system health monitoring, BITE for pumps, valves, and accumulators, contamination monitoring BITE, centralised fault isolation logic, ARINC data bus interfaces for hydraulic system status, and the Central Maintenance System (CMS) health data output.

> **Programme-controlled diagnostics extension.** This section covers monitoring, health management, and advanced diagnostics interfaces activated under programme authority. Architecture boundary and Q-Division assignments require formal programme review before population of detailed design data modules.

## 2. Scope

- Aligned to ATA SNS `29-80-00 Hydraulic Power Monitoring and Diagnostics` (programme-controlled diagnostics extension of baseline ATA 29 scope).
- Covers EDP and EMP pump BITE, hydraulic valve position feedback and fault isolation, pressure switch and transducer calibration monitoring, accumulator pre-charge integrity BITE, fluid contamination sensor monitoring, filter bypass status monitoring, ARINC 429/664 hydraulic system status bus, fault isolation logic, CMS health data interface, and maintenance control panel hydraulic status.
- Does not cover core pump installation (see `029-010`/`029-020`), distribution hardware (see `029-040`), or isolation valve hardware (see `029-070`).

## 3. System Architecture

```mermaid
graph TD
    A029_080["029-080 Hydraulic Power Monitoring,\nDiagnostics and Control Interfaces\n(ATA 29-80-00 — PCDE)"]

    A029_080 --> PumpBITE["EDP / EMP BITE\n(Run / Pressure Status)"]
    A029_080 --> ValveBITE["Valve Position\nBITE & Fault Isolation"]
    A029_080 --> AccumBITE["Accumulator Pre-charge\nIntegrity BITE"]
    A029_080 --> ContamBITE["Fluid Contamination\nSensor BITE"]
    A029_080 --> StatusBus["Hydraulic Status Bus\n(ARINC 429 / 664)"]

    A029_010["029-010 Main Power"] -->|pump status| A029_080
    A029_020["029-020 Aux Power"] -->|EMP status| A029_080
    A029_030["029-030 Indicating"] -->|pressure/qty data| A029_080
    A029_050["029-050 Pumps & Accum"] -->|accumulator data| A029_080
    A029_060["029-060 Filters"] -->|contamination data| A029_080
    A029_070["029-070 Isolation / Leak"] -->|isolation status| A029_080
    A029_080 -->|health data| CMS["041 Central Maintenance System"]
    A029_080 -->|maintenance data| MaintPanel["Maintenance\nControl Panel"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `029` — Hydraulic Power |
| Local section code | `029-080` |
| ATA SNS | `29-80-00` |
| Status | `programme-controlled-diagnostics-extension` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/029_Hydraulic-Power/` |
| Document | `029-080-Hydraulic-Power-Monitoring-Diagnostics-and-Control-Interfaces.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 29-80, Hydraulic Monitoring
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `029-010` Main Hydraulic Power [`./029-010-Main-Hydraulic-Power.md`](./029-010-Main-Hydraulic-Power.md)
- `029-050` Pumps, Accumulators and Pressure Control [`./029-050-Pumps-Accumulators-and-Pressure-Control.md`](./029-050-Pumps-Accumulators-and-Pressure-Control.md)
- `029-070` Isolation, Leak Detection and Safety Interfaces [`./029-070-Isolation-Leak-Detection-and-Safety-Interfaces.md`](./029-070-Isolation-Leak-Detection-and-Safety-Interfaces.md)
- ATA 41 — Central Maintenance System (CMS)
