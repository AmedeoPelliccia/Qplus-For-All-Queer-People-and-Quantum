---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-028-070-VENTING-PURGE-LEAK-DETECTION-AND-ISOLATION
title: "ATLAS 020-029 · 02.028 · Section 028-070 — Venting, Purge, Leak Detection and Isolation"
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
local_section_code: "028-070"
ata_sns: "28-70-00"
title_short: "Venting, Purge, Leak Detection and Isolation"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.028 · 028-070 — Venting, Purge, Leak Detection and Isolation

## 1. Purpose

Define the architecture boundary for *Venting, Purge, Leak Detection and Isolation* (ATA 28-70-00) within ATLAS subsection `028`. This section covers conventional fuel tank venting, vent float valves, NACA vent scoops, fuel vapour inerting (OBIGGS interface), and for H₂-extended architectures: gaseous hydrogen leak detection, H₂ concentration sensors, purge system for fuel cell anode and cryogenic lines, and isolation valve actuation on leak detection.

## 2. Scope

- Aligned to ATA SNS `28-70-00 Venting` (baseline, extended for H₂ leak detection where applicable).
- Covers wing tank vent float valves and vent lines, NACA inlet vent scoops, NACA surge tank and overboard vent, OBIGGS (On-Board Inert Gas Generation System) vent interface, gaseous H₂ concentration sensors (cabin, fuel cell bay, equipment zones), H₂ purge flow valves and inert gas purge supply, H₂ leak isolation valves, and leak detection alarm logic.
- Includes BITE for H₂ sensor calibration status and isolation valve position.
- Does not cover LH₂ tank vessel design (see `028-050`) or fuel distribution valves (see `028-020`).

**Safety boundary:** Fuel venting, H₂ purge, and leak detection are safety-critical functions with fire and explosion hazard implications. Sensor calibration, isolation valve function, H₂ concentration alarm thresholds, maintenance sign-off, and lifecycle traceability must be preserved with full certification evidence.

## 3. System Architecture

```mermaid
graph TD
    A028_070["028-070 Venting, Purge, Leak\nDetection and Isolation\n(ATA 28-70-00)"]

    A028_070 --> VentFloat["Wing Tank Vent\nFloat Valves & Vent Lines"]
    A028_070 --> NACAScoops["NACA Vent Scoops\n& Surge Tank"]
    A028_070 --> OBIGGS["OBIGGS Vent\nInterface"]
    A028_070 --> H2Sensors["H₂ Concentration\nSensors (Bay / Cabin)"]
    A028_070 --> PurgeValves["H₂ Purge Flow Valves\n& Inert Gas Supply"]
    A028_070 --> IsolationValves["H₂ Leak Isolation\nValves & Alarm Logic"]

    A028_010["028-010 Storage"] -->|vent interface| A028_070
    A028_050["028-050 LH₂ Cryogenic"] -->|boil-off vent| A028_070
    A028_060["028-060 Fuel Cell Feed"] -->|purge return| A028_070
    A028_070 -->|health data| A028_080["028-080 Monitoring and Diagnostics"]
    A026["026 Fire Protection"] -->|H₂ zone detection| A028_070
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `028` — Fuel and Energy Storage |
| Local section code | `028-070` |
| ATA SNS | `28-70-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/028_Fuel-and-Energy-Storage/` |
| Document | `028-070-Venting-Purge-Leak-Detection-and-Isolation.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 28-70, Venting
- EASA CS-25 Special Conditions — Hydrogen Fuel Systems (vent and purge provisions)
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `028-000` General [`./028-000-General.md`](./028-000-General.md)
- `028-010` Storage [`./028-010-Storage.md`](./028-010-Storage.md)
- `028-050` LH₂ Cryogenic Storage and Containment [`./028-050-LH2-Cryogenic-Storage-and-Containment.md`](./028-050-LH2-Cryogenic-Storage-and-Containment.md)
- `028-080` Fuel and Energy Storage Monitoring, Diagnostics and Control Interfaces [`./028-080-Fuel-and-Energy-Storage-Monitoring-Diagnostics-and-Control-Interfaces.md`](./028-080-Fuel-and-Energy-Storage-Monitoring-Diagnostics-and-Control-Interfaces.md)
- `026` Fire Protection — H₂ fire zone interface [`../026_Fire-Protection/026-000-General.md`](../026_Fire-Protection/026-000-General.md)
