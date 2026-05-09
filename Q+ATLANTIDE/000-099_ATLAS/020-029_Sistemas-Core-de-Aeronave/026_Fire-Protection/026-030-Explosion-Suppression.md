---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-026-030-EXPLOSION-SUPPRESSION
title: "ATLAS 020-029 · 02.026 · Section 026-030 — Explosion Suppression"
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
local_section_code: "026-030"
ata_sns: "26-30-00"
title_short: "Explosion Suppression"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.026 · 026-030 — Explosion Suppression

## 1. Purpose

Define the architecture boundary for *Explosion Suppression* (ATA 26-30-00) within ATLAS subsection `026`. This section covers fuel tank inerting, centre-wing tank explosion prevention, nitrogen-enriched air (NEA) generation, and flammability reduction systems.

## 2. Scope

- Aligned to ATA SNS `26-30-00 Explosion Suppression`.
- Covers Fuel Tank Inerting System (FTIS), nitrogen-enriched air (NEA) generation via on-board inert gas generation system (OBIGGS), air separation module (ASM), NEA distribution to fuel tanks, oxygen ullage monitoring, and flammability reduction compliance per FAR/CS 25.981 and SFAR 88/EASA ALT.
- Includes fuel tank explosion prevention architecture for centre-wing, main wing, and auxiliary fuel tanks.
- Does not cover fire extinguishing agents (see `026-020`) or propulsion-specific flammability interfaces (see `026-070`).

**Safety boundary:** Fuel tank flammability and explosion suppression are safety-critical. OBIGGS/FTIS integrity, NEA concentration levels, ASM serviceability, and airworthiness evidence must be maintained with full lifecycle traceability.

## 3. System Architecture

```mermaid
graph TD
    A026_030["026-030 Explosion Suppression\n(ATA 26-30-00)"]

    A026_030 --> OBIGGS["OBIGGS — On-Board Inert\nGas Generation System"]
    A026_030 --> ASM["Air Separation\nModule (ASM)"]
    A026_030 --> NEA_Dist["NEA Distribution\nto Fuel Tanks"]
    A026_030 --> OxygenMonitor["Oxygen Ullage\nMonitor"]
    A026_030 --> FTIS["Fuel Tank\nInerting System (FTIS)"]

    A021["021 ECS"] -->|bleed/pressurised air supply| OBIGGS
    A026_030 -->|inerting status| A026_080["026-080 Monitoring and Diagnostics"]
    FuelSystem["ATA 28 Fuel System"] -->|tank geometry / fill state| A026_030
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `026` — Fire Protection |
| Local section code | `026-030` |
| ATA SNS | `26-30-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/026_Fire-Protection/` |
| Document | `026-030-Explosion-Suppression.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 26-30, Explosion Suppression
- FAR/CS 25.981 — Fuel Tank Flammability Reduction
- SFAR 88 / EASA ALT — Fuel Tank Safety
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `026-020` Fire Extinguishing [`./026-020-Fire-Extinguishing.md`](./026-020-Fire-Extinguishing.md)
- `026-070` Hydrogen and Electric Propulsion Fire Safety Interfaces [`./026-070-Hydrogen-and-Electric-Propulsion-Fire-Safety-Interfaces.md`](./026-070-Hydrogen-and-Electric-Propulsion-Fire-Safety-Interfaces.md)
