---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-026-040-ENGINE-APU-AND-NACELLE-FIRE-PROTECTION
title: "ATLAS 020-029 · 02.026 · Section 026-040 — Engine, APU and Nacelle Fire Protection"
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
local_section_code: "026-040"
ata_sns: "26-40-00"
title_short: "Engine, APU and Nacelle Fire Protection"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: programme-controlled-extension
status_note: >
  Section 026-040 is a programme-controlled extension covering engine bay, APU bay
  and nacelle fire protection architecture including fire handle logic, zone definitions,
  and agent distribution. Activation requires programme authority and is controlled
  by Q-AIR in coordination with Q-MECHANICS.
language: en
---

# ATLAS 020-029 · 02.026 · 026-040 — Engine, APU and Nacelle Fire Protection

## 1. Purpose

Define the architecture boundary for *Engine, APU and Nacelle Fire Protection* (ATA 26-40-00) within ATLAS subsection `026`. This section covers fire zone definitions for engine bays and nacelles, APU fire protection, fire handle actuation logic, drain mast fire protection, and pylon fire protection interfaces.

> **Programme-controlled extension.** This section covers engine/APU zone fire architecture and fire handle integration activated under programme authority. Architecture boundary and Q-Division assignments require formal programme review before population of detailed design data modules.

## 2. Scope

- Aligned to ATA SNS `26-40-00 Engine/APU/Nacelle Fire Protection` (programme-controlled extension of baseline ATA 26 scope).
- Covers engine bay fire zone definitions (A-zone/B-zone), overheat detection loop routing, fire handle interlocks (engine shutdown, fuel shutoff, hydraulic shutoff, extinguisher discharge), APU fire protection (detection, extinguishing, APU shutdown interlock), nacelle fire protection architecture, drain mast fire protection, and pylon zone isolation.
- Does not cover core detection loop hardware (see `026-010`), extinguishing bottles (see `026-020`), or hydrogen/electric propulsion specifics (see `026-070`).

**Safety boundary:** Engine and APU fire protection are safety-critical. Fire handle authority, zone isolation logic, agent discharge sequencing, and APU shutdown interlocks require certified design data modules and full maintenance evidence.

## 3. System Architecture

```mermaid
graph TD
    A026_040["026-040 Engine, APU and Nacelle\nFire Protection\n(ATA 26-40-00 — PCE)"]

    A026_040 --> EngineZone["Engine Bay Fire\nZone A / Zone B"]
    A026_040 --> FireHandle["Fire Handle\nActuation Logic"]
    A026_040 --> APU_FP["APU Fire Protection\n(Detection + Extinguishing + Shutdown)"]
    A026_040 --> NacelleZone["Nacelle Fire\nZone Architecture"]
    A026_040 --> PylonIso["Pylon Zone\nIsolation Interface"]

    A026_010["026-010 Fire Detection"] -->|loop routing| A026_040
    A026_020["026-020 Fire Extinguishing"] -->|HRD agent distribution| A026_040
    A026_040 -->|interlock signals| Propulsion["ATA 70 Propulsion\n(Engine Shutdown / Fuel Shutoff)"]
    A026_040 -->|health data| A026_080["026-080 Monitoring and Diagnostics"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `026` — Fire Protection |
| Local section code | `026-040` |
| ATA SNS | `26-40-00` |
| Status | `programme-controlled-extension` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/026_Fire-Protection/` |
| Document | `026-040-Engine-APU-and-Nacelle-Fire-Protection.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 26-40, Engine / APU Fire Protection
- CS/FAR 25 — Engine Fire Protection Requirements
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `026-010` Fire and Smoke Detection [`./026-010-Fire-and-Smoke-Detection.md`](./026-010-Fire-and-Smoke-Detection.md)
- `026-020` Fire Extinguishing [`./026-020-Fire-Extinguishing.md`](./026-020-Fire-Extinguishing.md)
- `026-070` Hydrogen and Electric Propulsion Fire Safety Interfaces [`./026-070-Hydrogen-and-Electric-Propulsion-Fire-Safety-Interfaces.md`](./026-070-Hydrogen-and-Electric-Propulsion-Fire-Safety-Interfaces.md)
