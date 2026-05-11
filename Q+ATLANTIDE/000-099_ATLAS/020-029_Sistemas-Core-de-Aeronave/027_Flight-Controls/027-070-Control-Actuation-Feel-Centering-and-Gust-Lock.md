---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-027-070-CONTROL-ACTUATION-FEEL-CENTERING-AND-GUST-LOCK
title: "ATLAS 020-029 · 02.027 · Section 027-070 — Control Actuation, Feel, Centering and Gust Lock"
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
local_section_code: "027-070"
ata_sns: "27-70-00"
title_short: "Control Actuation, Feel, Centering and Gust Lock"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.027 · 027-070 — Control Actuation, Feel, Centering and Gust Lock

## 1. Purpose

Define the architecture boundary for *Control Actuation, Feel, Centering and Gust Lock* (ATA 27-70-00) within ATLAS subsection `027`. This section covers the primary flight control actuation architecture, artificial feel systems, centering mechanisms for sidestick or yoke, gust lock system, and the servo-actuation power supply envelope applicable to all primary flight control surfaces.

## 2. Scope

- Aligned to ATA SNS `27-70-00 Gust Lock and Damper System`.
- Covers primary flight control actuation (Electro-Hydraulic Actuators EHA, conventional hydraulic servo actuators CSA, electromechanical actuators EMA), artificial feel units for all axes, sidestick controller or control column centering and coupling, gust lock mechanical and electrical interlocks, actuator power supply interface (hydraulic and electrical), and actuator position transducers across all primary surfaces.
- Includes BITE for actuator engagement, hydraulic supply, and gust lock arming status.
- Does not cover secondary surface actuation (flaps, spoilers) which are addressed in `027-050` and `027-060`.

**Safety boundary:** Primary control actuation is safety-critical. Gust lock release interlocks, actuator authority limits, power supply integrity, fly-by-wire certification evidence, and maintenance sign-off must be preserved with full lifecycle evidence.

## 3. System Architecture

```mermaid
graph TD
    A027_070["027-070 Control Actuation, Feel,\nCentering and Gust Lock\n(ATA 27-70-00)"]

    A027_070 --> PrimaryActuators["Primary Actuators\n(EHA / CSA / EMA)"]
    A027_070 --> ArtificialFeel["Artificial Feel Units\n(All Axes)"]
    A027_070 --> CenteringMech["Sidestick / Yoke\nCentering Mechanism"]
    A027_070 --> GustLock["Gust Lock System\n(Mechanical & Electrical Interlock)"]
    A027_070 --> ActPowerIF["Actuator Power Supply Interface\n(Hydraulic & Electrical)"]
    A027_070 --> ActuatorBITE["Actuator BITE\n(Engagement / Supply / Lock)"]

    A027_010["027-010 Aileron / Roll"] -->|surface demand| A027_070
    A027_020["027-020 Rudder / Yaw"] -->|surface demand| A027_070
    A027_030["027-030 Elevator / Pitch"] -->|surface demand| A027_070
    A027_070 -->|health data| A027_080["027-080 Monitoring and Diagnostics"]
    A024["024 Electrical Power"] -->|EHA/EMA power| A027_070
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `027` — Flight Controls |
| Local section code | `027-070` |
| ATA SNS | `27-70-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/027_Flight-Controls/` |
| Document | `027-070-Control-Actuation-Feel-Centering-and-Gust-Lock.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 27-70, Gust Lock and Damper System
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `027-000` General [`./027-000-General.md`](./027-000-General.md)
- `027-010` Aileron, Elevon and Roll Control [`./027-010-Aileron-Elevon-and-Roll-Control.md`](./027-010-Aileron-Elevon-and-Roll-Control.md)
- `027-020` Rudder, Yaw Control and Directional Control [`./027-020-Rudder-Yaw-Control-and-Directional-Control.md`](./027-020-Rudder-Yaw-Control-and-Directional-Control.md)
- `027-030` Elevator, Pitch Control and Trim [`./027-030-Elevator-Pitch-Control-and-Trim.md`](./027-030-Elevator-Pitch-Control-and-Trim.md)
- `027-080` Fly-by-Wire Monitoring, Diagnostics and Control Interfaces [`./027-080-Fly-by-Wire-Monitoring-Diagnostics-and-Control-Interfaces.md`](./027-080-Fly-by-Wire-Monitoring-Diagnostics-and-Control-Interfaces.md)
