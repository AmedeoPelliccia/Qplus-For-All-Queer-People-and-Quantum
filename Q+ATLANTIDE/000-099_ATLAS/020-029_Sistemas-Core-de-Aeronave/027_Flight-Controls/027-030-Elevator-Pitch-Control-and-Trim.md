---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-027-030-ELEVATOR-PITCH-CONTROL-AND-TRIM
title: "ATLAS 020-029 · 02.027 · Section 027-030 — Elevator, Pitch Control and Trim"
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
subsection: "027"
subsection_title: "Flight Controls"
local_section_code: "027-030"
ata_sns: "27-30-00"
title_short: "Elevator, Pitch Control and Trim"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.027 · 027-030 — Elevator, Pitch Control and Trim

## 1. Purpose

Define the architecture boundary for *Elevator, Pitch Control and Trim* (ATA 27-30-00) within ATLAS subsection `027`. This section covers elevator surface architecture, pitch control actuation, elevator feel systems, pitch trim actuation, pitch control law interfaces, and surface position feedback for both conventional tail and canard configurations.

## 2. Scope

- Aligned to ATA SNS `27-30-00 Elevator`.
- Covers left and right elevator panels, elevator actuation (hydraulic and electromechanical), pitch feel unit and adjustable feel spring system, manual elevator trim (MET) wheel mechanism, autotrim function interface, pitch control law (PCL) interface to the fly-by-wire flight control primary computer (FCPC), elevator droop scheduling, and surface position feedback transducers.
- Includes BITE for elevator actuator integrity and trim runaway detection.
- Does not cover horizontal stabilizer trim (see `027-040`), canard pitch control where configured as an independent axis, or high-lift pitch effect (see `027-050`).

**Safety boundary:** Elevator and pitch control systems are safety-critical. Actuator serviceability, trim authority limits, runaway protection, fly-by-wire certification evidence, and maintenance sign-off must be preserved with full lifecycle evidence.

## 3. System Architecture

```mermaid
graph TD
    A027_030["027-030 Elevator, Pitch Control\nand Trim\n(ATA 27-30-00)"]

    A027_030 --> ElevatorL["Left Elevator\nSurface & Actuation"]
    A027_030 --> ElevatorR["Right Elevator\nSurface & Actuation"]
    A027_030 --> PitchFeel["Pitch Feel Unit\n& Adjustable Spring"]
    A027_030 --> METTrim["Manual Elevator Trim\n(MET) Mechanism"]
    A027_030 --> PCL["Pitch Control Law (PCL)\nInterface to FCPC"]
    A027_030 --> ElevFeedback["Elevator Position\nFeedback Transducers"]

    A027_030 -->|pitch demand| A027_040["027-040 Stabilizer and Pitch Trim"]
    A027_030 -->|health data| A027_080["027-080 Monitoring and Diagnostics"]
    A024["024 Electrical Power"] -->|actuator power| A027_030
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `027` — Flight Controls |
| Local section code | `027-030` |
| ATA SNS | `27-30-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/027_Flight-Controls/` |
| Document | `027-030-Elevator-Pitch-Control-and-Trim.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 27-30, Elevator
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `027-000` General [`./027-000-General.md`](./027-000-General.md)
- `027-040` Stabilizer and Pitch Trim [`./027-040-Stabilizer-and-Pitch-Trim.md`](./027-040-Stabilizer-and-Pitch-Trim.md)
- `027-080` Fly-by-Wire Monitoring, Diagnostics and Control Interfaces [`./027-080-Fly-by-Wire-Monitoring-Diagnostics-and-Control-Interfaces.md`](./027-080-Fly-by-Wire-Monitoring-Diagnostics-and-Control-Interfaces.md)
