---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-024-000-GENERAL
title: "ATLAS 020-029 · 02.024 · Section 024-000 — General"
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
subsection: "024"
subsection_title: "Electrical Power"
local_section_code: "024-000"
ata_sns: "24-00-00"
title_short: "General"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.024 · 024-000 — General

## 1. Purpose

Provide the general architectural definition for *Electrical Power* (ATA 24) within ATLAS subsection `024`. This section establishes the scope boundary, system family, Q-Division authority, and top-level structural context for all electrical power sections `024-010` through `024-090`.

## 2. Scope

- Defines the electrical power system family within the ATLAS-1000 register, aligned to ATA SNS `24-00-00 General`.
- Covers the architectural authority of `primary_q_division: Q-MECHANICS` with support from Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, and Q-INDUSTRY.
- Applies to all aircraft-level electrical power functions including generator drive, AC/DC generation, external power, electrical load distribution, emergency and standby power, monitoring and diagnostics interfaces.
- Does not replace certified ATA/S1000D task-specific maintenance, troubleshooting, operational, or software assurance data modules.

**Scope boundary:** This node covers aircraft electrical power architecture, generator drive, AC/DC generation, external power, load distribution, emergency and essential power, monitoring and diagnostics, and publication traceability. It does not replace certified ATA/S1000D task-specific maintenance, troubleshooting, operational, or avionics software data modules.

**Safety boundary:** Electrical power is safety-critical. Any artefact derived from this node requires correct aircraft effectivity, load shed logic, bus-tie authority boundaries, failure detection, essential bus switching, maintenance sign-off evidence and lifecycle traceability.

## 3. System Architecture

```mermaid
graph TD
    A024["024 Electrical Power\n(ATA 24)"] --> A024_010["024-010 Generator Drive"]
    A024 --> A024_020["024-020 AC Generation"]
    A024 --> A024_030["024-030 DC Generation"]
    A024 --> A024_040["024-040 External Power"]
    A024 --> A024_050["024-050 AC Electrical\nLoad Distribution"]
    A024 --> A024_060["024-060 DC Electrical\nLoad Distribution"]
    A024 --> A024_070["024-070 Emergency, Standby\nand Essential Power"]
    A024 --> A024_080["024-080 Electrical Power\nMonitoring and Diagnostics"]
    A024 --> A024_090["024-090 S1000D CSDB\nMapping and Traceability"]

    A023["023 Communications"] -->|power supply| A024
    A025["025 Equipment/Furnishings"] -->|power consumers| A024
    A041["041 CMS"] -->|health monitoring| A024
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `024` — Electrical Power |
| Local section code | `024-000` |
| ATA SNS | `24-00-00` |
| Primary Q-Division | Q-MECHANICS |
| Support Q-Divisions | Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/024_Electrical-Power/` |
| Document | `024-000-General.md` |
| Parent subsection | [`README.md`](./README.md) |
| Parent section | [`../README.md`](../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References

- ATA iSpec 2200 — Chapter 24, Electrical Power
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- ATLAS section index [`../README.md`](../README.md)
- Subsection index [`./README.md`](./README.md)
- Section `023-000` General — Communications [`../023_Communications/023-000-General.md`](../023_Communications/023-000-General.md)
- Section `025` — Equipment/Furnishings [`../025_Equipment-Furnishings/README.md`](../025_Equipment-Furnishings/README.md)
