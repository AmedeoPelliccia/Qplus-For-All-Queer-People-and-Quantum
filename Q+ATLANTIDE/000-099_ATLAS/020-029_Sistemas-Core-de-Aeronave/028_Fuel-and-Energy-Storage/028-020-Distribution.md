---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-028-020-DISTRIBUTION
title: "ATLAS 020-029 · 02.028 · Section 028-020 — Distribution"
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
local_section_code: "028-020"
ata_sns: "28-20-00"
title_short: "Distribution"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.028 · 028-020 — Distribution

## 1. Purpose

Define the architecture boundary for *Fuel Distribution* (ATA 28-20-00) within ATLAS subsection `028`. This section covers fuel feed and distribution piping, boost pumps, crossfeed valves, engine feed valves, fuel manifold architecture, and the fuel control system logic governing fuel routing from tanks to engines under normal, abnormal and emergency conditions.

## 2. Scope

- Aligned to ATA SNS `28-20-00 Distribution`.
- Covers wing tank boost pumps (inboard and outboard), centre tank boost pumps, crossfeed manifold and crossfeed valve, engine fuel feed lines and shutoff valves (EFCV), fuel control and monitoring computer (FCMC) distribution logic, APU feed line and shutoff valve, fuel feed priority scheduling, and LP/HP fuel shutoff interfaces to engines.
- Includes BITE for pump run status, valve position feedback, and crossfeed valve integrity.
- Does not cover fuel quantity measurement (see `028-040`), transfer and jettison (see `028-030`), or fuel cell feed interfaces (see `028-060`).

**Safety boundary:** Fuel distribution is safety-critical. Engine feed valve positions, boost pump serviceability, crossfeed logic, fire shutoff valve function, maintenance sign-off, and lifecycle traceability must be preserved with full certification evidence.

## 3. System Architecture

```mermaid
graph TD
    A028_020["028-020 Distribution\n(ATA 28-20-00)"]

    A028_020 --> BoostPumps["Wing/Centre Tank\nBoost Pumps"]
    A028_020 --> CrossfeedValve["Crossfeed Manifold\n& Valve"]
    A028_020 --> EngineFeedValves["Engine Fuel Feed\nShutoff Valves (EFCV)"]
    A028_020 --> FCMC["Fuel Control & Monitoring\nComputer (FCMC)"]
    A028_020 --> APUFeed["APU Feed Line\n& Shutoff Valve"]
    A028_020 --> FeedPriority["Feed Priority\nScheduling Logic"]

    A028_010["028-010 Storage"] -->|fuel supply| A028_020
    A028_020 -->|engine feed| EngineIF["Engine HP/LP\nShutoff Interface"]
    A028_020 -->|health data| A028_080["028-080 Monitoring and Diagnostics"]
    A024["024 Electrical Power"] -->|pump/valve power| A028_020
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `028` — Fuel and Energy Storage |
| Local section code | `028-020` |
| ATA SNS | `28-20-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/028_Fuel-and-Energy-Storage/` |
| Document | `028-020-Distribution.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 28-20, Distribution
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `028-000` General [`./028-000-General.md`](./028-000-General.md)
- `028-010` Storage [`./028-010-Storage.md`](./028-010-Storage.md)
- `028-030` Dump, Jettison and Transfer [`./028-030-Dump-Jettison-and-Transfer.md`](./028-030-Dump-Jettison-and-Transfer.md)
- `028-080` Fuel and Energy Storage Monitoring, Diagnostics and Control Interfaces [`./028-080-Fuel-and-Energy-Storage-Monitoring-Diagnostics-and-Control-Interfaces.md`](./028-080-Fuel-and-Energy-Storage-Monitoring-Diagnostics-and-Control-Interfaces.md)
