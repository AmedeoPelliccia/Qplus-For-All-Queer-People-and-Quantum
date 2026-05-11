---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-027-060-SPOILERS-SPEEDBRAKES-AND-GROUND-SPOILERS
title: "ATLAS 020-029 · 02.027 · Section 027-060 — Spoilers, Speedbrakes and Ground Spoilers"
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
local_section_code: "027-060"
ata_sns: "27-60-00"
title_short: "Spoilers, Speedbrakes and Ground Spoilers"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.027 · 027-060 — Spoilers, Speedbrakes and Ground Spoilers

## 1. Purpose

Define the architecture boundary for *Spoilers, Speedbrakes and Ground Spoilers* (ATA 27-60-00) within ATLAS subsection `027`. This section covers spoiler panel architecture, speedbrake actuation and control, roll spoiler scheduling, ground spoiler automatic deployment logic, and spoiler position indication.

## 2. Scope

- Aligned to ATA SNS `27-60-00 Drag Devices`.
- Covers flight spoiler panels (roll assistance and speedbrake), ground spoiler panels (lift dump), spoiler actuators (electrohydraulic servo actuators), speedbrake lever and control logic, roll spoiler mixing (aileron demand integration), ground spoiler automatic deployment (TOGA protection, main gear weight-on-wheels WoW), speedbrake limiting (with flap position interlock), and spoiler panel position feedback.
- Includes BITE for spoiler actuator and speedbrake lever switch integrity.
- Does not cover trailing edge flaps (see `027-050`) or aileron primary roll control (see `027-010`).

**Safety boundary:** Spoiler and speedbrake systems are safety-critical. Ground spoiler arming and automatic deployment logic, speedbrake flap interlocks, actuator serviceability, fly-by-wire certification evidence, and maintenance sign-off must be preserved with full lifecycle evidence.

## 3. System Architecture

```mermaid
graph TD
    A027_060["027-060 Spoilers, Speedbrakes\nand Ground Spoilers\n(ATA 27-60-00)"]

    A027_060 --> FlightSpoilers["Flight Spoiler Panels\n(Roll / Speedbrake)"]
    A027_060 --> GroundSpoilers["Ground Spoiler Panels\n(Lift Dump)"]
    A027_060 --> SpoilerActuators["Spoiler Actuators\n(EHA / Electrohydraulic)"]
    A027_060 --> SpeedbrakeLever["Speedbrake Lever\n& Control Logic"]
    A027_060 --> RollMixing["Roll Spoiler Mixing\n(Aileron Integration)"]
    A027_060 --> GSAutoLogic["Ground Spoiler Auto\nDeployment (WoW / TOGA)"]

    A027_010["027-010 Aileron / Roll Control"] -->|roll demand| A027_060
    A027_050["027-050 Flaps / High Lift"] -->|flap position interlock| A027_060
    A027_060 -->|health data| A027_080["027-080 Monitoring and Diagnostics"]
    A024["024 Electrical Power"] -->|actuator power| A027_060
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `027` — Flight Controls |
| Local section code | `027-060` |
| ATA SNS | `27-60-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/027_Flight-Controls/` |
| Document | `027-060-Spoilers-Speedbrakes-and-Ground-Spoilers.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 27-60, Drag Devices
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `027-000` General [`./027-000-General.md`](./027-000-General.md)
- `027-010` Aileron, Elevon and Roll Control [`./027-010-Aileron-Elevon-and-Roll-Control.md`](./027-010-Aileron-Elevon-and-Roll-Control.md)
- `027-050` Flaps, High Lift and Lift Augmentation [`./027-050-Flaps-High-Lift-and-Lift-Augmentation.md`](./027-050-Flaps-High-Lift-and-Lift-Augmentation.md)
- `027-080` Fly-by-Wire Monitoring, Diagnostics and Control Interfaces [`./027-080-Fly-by-Wire-Monitoring-Diagnostics-and-Control-Interfaces.md`](./027-080-Fly-by-Wire-Monitoring-Diagnostics-and-Control-Interfaces.md)
