---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-027-020-RUDDER-YAW-CONTROL-AND-DIRECTIONAL-CONTROL
title: "ATLAS 020-029 · 02.027 · Section 027-020 — Rudder, Yaw Control and Directional Control"
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
local_section_code: "027-020"
ata_sns: "27-20-00"
title_short: "Rudder, Yaw Control and Directional Control"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.027 · 027-020 — Rudder, Yaw Control and Directional Control

## 1. Purpose

Define the architecture boundary for *Rudder, Yaw Control and Directional Control* (ATA 27-20-00) within ATLAS subsection `027`. This section covers rudder surface architecture, yaw control actuation, yaw damper systems, asymmetric thrust compensation, directional control law interfaces, and rudder travel limiting systems.

## 2. Scope

- Aligned to ATA SNS `27-20-00 Rudder`.
- Covers upper and lower rudder panels (where applicable), rudder actuation (hydraulic and electromechanical), yaw damper (YD) actuators and control law, rudder travel limiter (RTL) and pedal force feel units, asymmetric thrust yaw compensation logic, crosswind ground handling control, and rudder position feedback transducers.
- Includes BITE for rudder actuator and yaw damper integrity.
- Does not cover lateral roll coupling (see `027-010`), Dutch roll damping in the pitch axis (see `027-030`), or directional trim in the stabilizer (see `027-040`).

**Safety boundary:** Rudder and yaw control systems are safety-critical. Rudder travel limits, yaw damper authority, actuator serviceability, fly-by-wire certification evidence, and maintenance sign-off must be preserved with full lifecycle evidence.

## 3. System Architecture

```mermaid
graph TD
    A027_020["027-020 Rudder, Yaw Control\nand Directional Control\n(ATA 27-20-00)"]

    A027_020 --> RudderSurface["Rudder Surface\n& Actuation"]
    A027_020 --> YawDamper["Yaw Damper (YD)\nActuator & Control Law"]
    A027_020 --> RTL["Rudder Travel Limiter\n(RTL) System"]
    A027_020 --> PedalFeel["Pedal Force Feel\nUnit"]
    A027_020 --> AsymThrust["Asymmetric Thrust\nYaw Compensation Logic"]
    A027_020 --> RudderFeedback["Rudder Position\nFeedback Transducers"]

    A027_020 -->|health data| A027_080["027-080 Monitoring and Diagnostics"]
    A027_010["027-010 Aileron / Roll Control"] -->|lateral-directional coupling| A027_020
    A024["024 Electrical Power"] -->|actuator power| A027_020
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `027` — Flight Controls |
| Local section code | `027-020` |
| ATA SNS | `27-20-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/027_Flight-Controls/` |
| Document | `027-020-Rudder-Yaw-Control-and-Directional-Control.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 27-20, Rudder
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `027-000` General [`./027-000-General.md`](./027-000-General.md)
- `027-010` Aileron, Elevon and Roll Control [`./027-010-Aileron-Elevon-and-Roll-Control.md`](./027-010-Aileron-Elevon-and-Roll-Control.md)
- `027-080` Fly-by-Wire Monitoring, Diagnostics and Control Interfaces [`./027-080-Fly-by-Wire-Monitoring-Diagnostics-and-Control-Interfaces.md`](./027-080-Fly-by-Wire-Monitoring-Diagnostics-and-Control-Interfaces.md)
