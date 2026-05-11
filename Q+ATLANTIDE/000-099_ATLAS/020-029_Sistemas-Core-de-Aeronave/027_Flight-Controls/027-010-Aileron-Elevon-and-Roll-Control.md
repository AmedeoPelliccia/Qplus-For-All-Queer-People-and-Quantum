---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-027-010-AILERON-ELEVON-AND-ROLL-CONTROL
title: "ATLAS 020-029 · 02.027 · Section 027-010 — Aileron, Elevon and Roll Control"
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
local_section_code: "027-010"
ata_sns: "27-10-00"
title_short: "Aileron, Elevon and Roll Control"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.027 · 027-010 — Aileron, Elevon and Roll Control

## 1. Purpose

Define the architecture boundary for *Aileron, Elevon and Roll Control* (ATA 27-10-00) within ATLAS subsection `027`. This section covers aileron and elevon surface architecture, roll control actuation, differential spoiler coordination, roll control law interfaces, and surface rigging and limit definitions for both conventional and blended-wing configurations.

## 2. Scope

- Aligned to ATA SNS `27-10-00 Aileron and Roll Control`.
- Covers inboard and outboard ailerons, elevon surfaces (blended-wing body configurations), roll control actuation systems (hydraulic, electro-hydraulic, electromechanical), aileron droop scheduling, roll-spoiler interconnect logic, roll control law (RCL) interface to the fly-by-wire flight control computer (FCPC), and surface position feedback transducers.
- Includes BITE for aileron actuator integrity and surface position monitoring.
- Does not cover lateral directional coupling (see `027-020`), high-lift roll assistance (see `027-050`), or roll spoiler actuation (see `027-060`).

**Safety boundary:** Aileron and roll control systems are safety-critical. Actuator serviceability, surface travel limits, rigging tolerances, fly-by-wire certification evidence, and maintenance sign-off must be preserved with full lifecycle evidence.

## 3. System Architecture

```mermaid
graph TD
    A027_010["027-010 Aileron, Elevon\nand Roll Control\n(ATA 27-10-00)"]

    A027_010 --> OutboardAileron["Outboard Aileron\nSurface & Actuation"]
    A027_010 --> InboardAileron["Inboard Aileron\nSurface & Actuation"]
    A027_010 --> Elevon["Elevon Surface\n(BWB configuration)"]
    A027_010 --> RollSpoilerLink["Roll-Spoiler\nInterconnect Logic"]
    A027_010 --> RCL["Roll Control Law (RCL)\nInterface to FCPC"]
    A027_010 --> SurfaceFeedback["Surface Position\nFeedback Transducers"]

    A027_010 -->|roll demand| A027_060["027-060 Spoilers / Speedbrakes"]
    A027_010 -->|health data| A027_080["027-080 Monitoring and Diagnostics"]
    A024["024 Electrical Power"] -->|actuator power| A027_010
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `027` — Flight Controls |
| Local section code | `027-010` |
| ATA SNS | `27-10-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/027_Flight-Controls/` |
| Document | `027-010-Aileron-Elevon-and-Roll-Control.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 27-10, Aileron and Roll Control
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `027-000` General [`./027-000-General.md`](./027-000-General.md)
- `027-060` Spoilers, Speedbrakes and Ground Spoilers [`./027-060-Spoilers-Speedbrakes-and-Ground-Spoilers.md`](./027-060-Spoilers-Speedbrakes-and-Ground-Spoilers.md)
- `027-080` Fly-by-Wire Monitoring, Diagnostics and Control Interfaces [`./027-080-Fly-by-Wire-Monitoring-Diagnostics-and-Control-Interfaces.md`](./027-080-Fly-by-Wire-Monitoring-Diagnostics-and-Control-Interfaces.md)
