---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-026-010-FIRE-AND-SMOKE-DETECTION
title: "ATLAS 020-029 · 02.026 · Section 026-010 — Fire and Smoke Detection"
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
subsection: "026"
subsection_title: "Fire Protection"
local_section_code: "026-010"
ata_sns: "26-10-00"
title_short: "Fire and Smoke Detection"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.026 · 026-010 — Fire and Smoke Detection

## 1. Purpose

Define the architecture boundary for *Fire and Smoke Detection* (ATA 26-10-00) within ATLAS subsection `026`. This section covers fire detection loops, smoke detectors, overheat detection, fire warning systems, and detector monitoring across all aircraft fire zones.

## 2. Scope

- Aligned to ATA SNS `26-10-00 Fire Detection`.
- Covers continuous-loop fire detection systems (engine bays, APU bay, nacelles), photoelectric and ionisation smoke detectors (cargo, cabin, lavatories, equipment bays), overheat sensing elements, fire warning annunciation, detector serviceable status indication, and fire zone monitoring architecture.
- Includes BITE for detection loop continuity and detector integrity monitoring.
- Does not cover extinguishing systems (see `026-020`), cabin/lavatory specifics (see `026-060`), or engine-zone specialised protection (see `026-040`).

**Safety boundary:** Detection systems are safety-critical. Detector continuity, zone definitions, alarm thresholds, and maintenance serviceability checks must be preserved with full lifecycle evidence.

## 3. System Architecture

```mermaid
graph TD
    A026_010["026-010 Fire and\nSmoke Detection\n(ATA 26-10-00)"]

    A026_010 --> ContinuousLoop["Continuous-Loop\nFire Detection\n(Engine/APU/Nacelle)"]
    A026_010 --> SmokeDetectors["Smoke Detectors\n(Cargo/Cabin/Lavatory/Equip Bay)"]
    A026_010 --> OverheatSensing["Overheat Sensing\nElements"]
    A026_010 --> FireWarning["Fire Warning\nAnnunciation System"]
    A026_010 --> DetectorBITE["Detection Loop\nBITE / Integrity Monitor"]

    A026_010 -->|alarm signal| A026_020["026-020 Fire Extinguishing"]
    A026_010 -->|health data| A026_080["026-080 Monitoring and Diagnostics"]
    A024["024 Electrical Power"] -->|loop power supply| A026_010
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `026` — Fire Protection |
| Local section code | `026-010` |
| ATA SNS | `26-10-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/026_Fire-Protection/` |
| Document | `026-010-Fire-and-Smoke-Detection.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 26-10, Fire Detection
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `026-000` General [`./026-000-General.md`](./026-000-General.md)
- `026-020` Fire Extinguishing [`./026-020-Fire-Extinguishing.md`](./026-020-Fire-Extinguishing.md)
- `026-080` Fire Protection Monitoring, Diagnostics and Control Interfaces [`./026-080-Fire-Protection-Monitoring-Diagnostics-and-Control-Interfaces.md`](./026-080-Fire-Protection-Monitoring-Diagnostics-and-Control-Interfaces.md)
