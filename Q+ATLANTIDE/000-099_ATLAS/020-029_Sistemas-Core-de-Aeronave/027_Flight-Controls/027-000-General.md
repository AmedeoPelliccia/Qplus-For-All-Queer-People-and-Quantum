---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-027-000-GENERAL
title: "ATLAS 020-029 · 02.027 · Section 027-000 — General"
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
local_section_code: "027-000"
ata_sns: "27-00-00"
title_short: "General"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.027 · 027-000 — General

## 1. Purpose

Provide the general architectural definition for *Flight Controls* (ATA 27) within ATLAS subsection `027`. This section establishes the scope boundary, system family, Q-Division authority, and top-level structural context for all flight controls sections `027-010` through `027-090`.

## 2. Scope

- Defines the flight controls system family within the ATLAS-1000 register, aligned to ATA SNS `27-00-00 General`.
- Covers the architectural authority of `primary_q_division: Q-AIR` with support from Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, and Q-INDUSTRY.
- Applies to all aircraft-level flight control functions including aileron and roll control, rudder and yaw control, elevator and pitch control, stabilizer and pitch trim, flaps and high lift, spoilers and speedbrakes, control actuation and feel systems, fly-by-wire monitoring and diagnostics, and publication traceability.
- Does not replace certified ATA/S1000D task-specific maintenance, troubleshooting, operational, or software assurance data modules.

**Scope boundary:** This node covers aircraft flight control architecture across all primary and secondary control surfaces, fly-by-wire actuation, and control law interfaces. It does not replace certified ATA/S1000D task-specific maintenance, troubleshooting, or operational data modules.

**Safety boundary:** Flight controls are safety-critical. Any artefact derived from this node requires correct aircraft effectivity, fly-by-wire certification evidence, flight-control authority limits, actuator maintenance sign-off, control surface rigging data, and full lifecycle traceability.

## 3. System Architecture

```mermaid
graph TD
    A027["027 Flight Controls\n(ATA 27)"] --> A027_010["027-010 Aileron, Elevon\nand Roll Control"]
    A027 --> A027_020["027-020 Rudder, Yaw Control\nand Directional Control"]
    A027 --> A027_030["027-030 Elevator, Pitch Control\nand Trim"]
    A027 --> A027_040["027-040 Stabilizer\nand Pitch Trim"]
    A027 --> A027_050["027-050 Flaps, High Lift\nand Lift Augmentation"]
    A027 --> A027_060["027-060 Spoilers, Speedbrakes\nand Ground Spoilers"]
    A027 --> A027_070["027-070 Control Actuation, Feel,\nCentering and Gust Lock"]
    A027 --> A027_080["027-080 Fly-by-Wire Monitoring,\nDiagnostics and Control Interfaces"]
    A027 --> A027_090["027-090 S1000D CSDB\nMapping and Traceability"]

    A024["024 Electrical Power"] -->|power supply to actuators| A027
    A022["022 Auto Flight"] -->|control law commands| A027_080
    A041["041 CMS"] -->|health monitoring| A027_080
    A026["026 Fire Protection"] -->|flight control bay fire zone| A027
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `027` — Flight Controls |
| Local section code | `027-000` |
| ATA SNS | `27-00-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/027_Flight-Controls/` |
| Document | `027-000-General.md` |
| Parent subsection | [`README.md`](./README.md) |
| Parent section | [`../README.md`](../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References

- ATA iSpec 2200 — Chapter 27, Flight Controls
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- ATLAS section index [`../README.md`](../README.md)
- Subsection index [`./README.md`](./README.md)
- Section `026-000` General — Fire Protection [`../026_Fire-Protection/026-000-General.md`](../026_Fire-Protection/026-000-General.md)
- Section `028-000` General — Fuel and Energy Storage [`../028_Fuel-and-Energy-Storage/028-000-General.md`](../028_Fuel-and-Energy-Storage/028-000-General.md)
