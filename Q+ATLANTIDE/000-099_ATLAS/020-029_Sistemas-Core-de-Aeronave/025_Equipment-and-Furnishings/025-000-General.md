---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-025-000-GENERAL
title: "ATLAS 020-029 · 02.025 · Section 025-000 — General"
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
subsection: "025"
subsection_title: "Equipment and Furnishings"
local_section_code: "025-000"
ata_sns: "25-00-00"
title_short: "General"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.025 · 025-000 — General

## 1. Purpose

Provide the general architectural definition for *Equipment and Furnishings* (ATA 25) within ATLAS subsection `025`. This section establishes the scope boundary, system family, Q-Division authority, and top-level structural context for all equipment and furnishings sections `025-010` through `025-090`.

## 2. Scope

- Defines the equipment and furnishings system family within the ATLAS-1000 register, aligned to ATA SNS `25-00-00 General`.
- Covers the architectural authority of `primary_q_division: Q-AIR` with support from Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, and Q-INDUSTRY.
- Applies to all aircraft equipment and furnishings functions including flight compartment equipment, passenger cabin furnishings, galley and service equipment, lavatories, cargo compartment liners and fittings, emergency equipment, and accessory compartments.
- Does not replace certified ATA/S1000D task-specific maintenance, operational, or safety-of-flight data modules for cabin crew equipment or emergency systems.

**Scope boundary:** This node covers aircraft equipment and furnishings architecture, compartment definitions, cabin layouts, galley/lavatory systems, emergency equipment interfaces, cargo compartment fittings, monitoring and diagnostics, and publication traceability. It does not replace certified ATA/S1000D task-specific maintenance, operational, or emergency procedures data modules.

**Safety boundary:** Equipment and furnishings include flight-critical emergency equipment (life vests, oxygen, evacuation slides). Any artefact derived from this node affecting emergency equipment requires correct aircraft effectivity, regulatory compliance evidence (CS-25/FAR 25), maintenance sign-off evidence, and lifecycle traceability.

## 3. System Architecture

```mermaid
graph TD
    A025["025 Equipment and Furnishings\n(ATA 25)"] --> A025_010["025-010 Flight Compartment"]
    A025 --> A025_020["025-020 Passenger Compartment"]
    A025 --> A025_030["025-030 Buffet, Galley\nand Service Equipment"]
    A025 --> A025_040["025-040 Lavatories"]
    A025 --> A025_050["025-050 Cargo Compartments"]
    A025 --> A025_060["025-060 Emergency Equipment"]
    A025 --> A025_070["025-070 Accessory Compartments\nand Furnishing Interfaces"]
    A025 --> A025_080["025-080 Cabin Equipment\nMonitoring and Diagnostics"]
    A025 --> A025_090["025-090 S1000D CSDB\nMapping and Traceability"]

    A024["024 Electrical Power"] -->|power supply| A025
    A021["021 Air Conditioning"] -->|cabin env control| A025
    A026["026 Fire Protection"] -->|safety interface| A025
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `025` — Equipment and Furnishings |
| Local section code | `025-000` |
| ATA SNS | `25-00-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/025_Equipment-and-Furnishings/` |
| Document | `025-000-General.md` |
| Parent subsection | [`README.md`](./README.md) |
| Parent section | [`../README.md`](../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References

- ATA iSpec 2200 — Chapter 25, Equipment / Furnishings
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- ATLAS section index [`../README.md`](../README.md)
- Subsection index [`./README.md`](./README.md)
- Section `024-000` General — Electrical Power [`../024_Electrical-Power/024-000-General.md`](../024_Electrical-Power/024-000-General.md)
- Section `026` — Fire Protection [`../026_Fire-Protection/README.md`](../026_Fire-Protection/README.md)
