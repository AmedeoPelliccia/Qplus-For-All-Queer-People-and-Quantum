---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-027-040-STABILIZER-AND-PITCH-TRIM
title: "ATLAS 020-029 · 02.027 · Section 027-040 — Stabilizer and Pitch Trim"
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
local_section_code: "027-040"
ata_sns: "27-40-00"
title_short: "Stabilizer and Pitch Trim"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.027 · 027-040 — Stabilizer and Pitch Trim

## 1. Purpose

Define the architecture boundary for *Stabilizer and Pitch Trim* (ATA 27-40-00) within ATLAS subsection `027`. This section covers horizontal stabilizer structure and actuation, trimmable horizontal stabilizer (THS) drive mechanism, stabilizer position indication, pitch trim control interfaces, runaway protection, and stabilizer cut-out systems.

## 2. Scope

- Aligned to ATA SNS `27-40-00 Horizontal Stabilizer`.
- Covers the trimmable horizontal stabilizer (THS) assembly, THS actuator (ballscrew and jackscrew drive), stabilizer drive motor (electric or hydraulic), THS position indication and LVDT, pitch trim wheel and control column switch logic, autotrim interface from flight control system, stabilizer runaway protection and cut-out switch, and stabilizer structural attachment fittings.
- Includes BITE for THS actuator integrity and runaway detection logic.
- Does not cover elevator surface actuation (see `027-030`) or autopilot pitch authority (see `022 Auto Flight`).

**Safety boundary:** Horizontal stabilizer and pitch trim systems are safety-critical. Stabilizer runaway protection, trim authority limits, actuator serviceability, fly-by-wire certification evidence, and maintenance sign-off must be preserved with full lifecycle evidence.

## 3. System Architecture

```mermaid
graph TD
    A027_040["027-040 Stabilizer\nand Pitch Trim\n(ATA 27-40-00)"]

    A027_040 --> THSActuator["THS Actuator\n(Ballscrew/Jackscrew Drive)"]
    A027_040 --> THSDriveMotor["THS Drive Motor\n(Electric/Hydraulic)"]
    A027_040 --> THSPosition["Stabilizer Position\nIndication (LVDT)"]
    A027_040 --> PitchTrimWheel["Pitch Trim Wheel\n& Column Switch Logic"]
    A027_040 --> RunawayProtect["Stabilizer Runaway\nProtection & Cut-Out"]
    A027_040 --> AutotrimIF["Autotrim Interface\n(FCS)"]

    A027_030["027-030 Elevator / Pitch Control"] -->|pitch trim demand| A027_040
    A027_040 -->|health data| A027_080["027-080 Monitoring and Diagnostics"]
    A024["024 Electrical Power"] -->|drive motor power| A027_040
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `027` — Flight Controls |
| Local section code | `027-040` |
| ATA SNS | `27-40-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/027_Flight-Controls/` |
| Document | `027-040-Stabilizer-and-Pitch-Trim.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 27-40, Horizontal Stabilizer
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `027-000` General [`./027-000-General.md`](./027-000-General.md)
- `027-030` Elevator, Pitch Control and Trim [`./027-030-Elevator-Pitch-Control-and-Trim.md`](./027-030-Elevator-Pitch-Control-and-Trim.md)
- `027-080` Fly-by-Wire Monitoring, Diagnostics and Control Interfaces [`./027-080-Fly-by-Wire-Monitoring-Diagnostics-and-Control-Interfaces.md`](./027-080-Fly-by-Wire-Monitoring-Diagnostics-and-Control-Interfaces.md)
