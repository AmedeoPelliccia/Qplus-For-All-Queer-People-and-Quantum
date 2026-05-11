---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-028-040-INDICATING
title: "ATLAS 020-029 · 02.028 · Section 028-040 — Indicating"
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
subsection: "028"
subsection_title: "Fuel and Energy Storage"
local_section_code: "028-040"
ata_sns: "28-40-00"
title_short: "Indicating"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.028 · 028-040 — Indicating

## 1. Purpose

Define the architecture boundary for *Fuel Indicating* (ATA 28-40-00) within ATLAS subsection `028`. This section covers fuel quantity measurement and indication, fuel flow measurement, fuel temperature sensors, CG fuel balance indication, and fuel management computer display interfaces for conventional Jet-A fuel systems.

## 2. Scope

- Aligned to ATA SNS `28-40-00 Indicating`.
- Covers capacitance fuel quantity sensors (FQMS), fuel quantity management computer (FQMC/FQIS), fuel flow meters, fuel temperature sensors, low-level warning sensors, cockpit ECAM/EICAS fuel page displays, refuelling panel quantity indication, CG fuel balance display and alerting, BITE for sensor and FQMS integrity, and ground refuelling quantity pre-selection.
- Does not cover fuel distribution valves and pumps (see `028-020`), transfer logic (see `028-030`), or LH₂ quantity measurement (see `028-050`).

**Safety boundary:** Fuel quantity measurement is safety-critical. Sensor calibration, FQMS integrity, low-level warnings, maintenance sign-off, and lifecycle traceability must be preserved with full certification evidence.

## 3. System Architecture

```mermaid
graph TD
    A028_040["028-040 Indicating\n(ATA 28-40-00)"]

    A028_040 --> FQSensors["Capacitance FQ Sensors\n(FQMS)"]
    A028_040 --> FQMC["Fuel Quantity Management\nComputer (FQMC/FQIS)"]
    A028_040 --> FlowMeters["Fuel Flow Meters"]
    A028_040 --> TempSensors["Fuel Temperature\nSensors"]
    A028_040 --> LowLevel["Low-Level Warning\nSensors"]
    A028_040 --> Displays["ECAM/EICAS Fuel Page\n& Refuelling Panel Display"]

    A028_010["028-010 Storage"] -->|tank quantity| A028_040
    A028_030["028-030 Transfer/Jettison"] -->|CG balance| A028_040
    A028_040 -->|health data| A028_080["028-080 Monitoring and Diagnostics"]
    A024["024 Electrical Power"] -->|sensor/computer power| A028_040
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `028` — Fuel and Energy Storage |
| Local section code | `028-040` |
| ATA SNS | `28-40-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/028_Fuel-and-Energy-Storage/` |
| Document | `028-040-Indicating.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 28-40, Indicating
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `028-000` General [`./028-000-General.md`](./028-000-General.md)
- `028-010` Storage [`./028-010-Storage.md`](./028-010-Storage.md)
- `028-080` Fuel and Energy Storage Monitoring, Diagnostics and Control Interfaces [`./028-080-Fuel-and-Energy-Storage-Monitoring-Diagnostics-and-Control-Interfaces.md`](./028-080-Fuel-and-Energy-Storage-Monitoring-Diagnostics-and-Control-Interfaces.md)
