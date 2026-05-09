---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-024-050-AC-ELECTRICAL-LOAD-DISTRIBUTION
title: "ATLAS 020-029 · 02.024 · Section 024-050 — AC Electrical Load Distribution"
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
local_section_code: "024-050"
ata_sns: "24-50-00"
title_short: "AC Electrical Load Distribution"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.024 · 024-050 — AC Electrical Load Distribution

## 1. Purpose

Define the architecture boundary for *AC Electrical Load Distribution* (ATA 24-50-00) within ATLAS subsection `024`. This section covers the AC bus architecture, including main AC busses, transfer busses, galley busses, and Solid State Power Controllers (SSPC) for AC load management.

## 2. Scope

- Aligned to ATA SNS `24-50-00 AC Electrical Load Distribution`.
- Covers main AC busses (AC BUS 1, AC BUS 2, AC ESS BUS), transfer busses, galley and IFE AC feed busses, Solid State Power Controllers (SSPC), and circuit breakers for AC distribution panels.
- Includes load shedding logic, bus transfer on generator loss, and AC bus tie control.
- Interfaces: AC generation (`024-020`), external power (`024-040`), DC generation (`024-030`), and all AC-powered systems.
- Does not cover DC bus distribution (see `024-060`) or the specific load equipment connected to AC busses.

## 3. System Architecture

```mermaid
graph TD
    A024_050["024-050 AC Electrical Load Distribution\n(ATA 24-50-00)"]

    A024_050 --> ACBUS1["AC Bus 1\n(Engine 1 Generator)"]
    A024_050 --> ACBUS2["AC Bus 2\n(Engine 2 Generator)"]
    A024_050 --> ACESSBUS["AC Essential Bus"]
    A024_050 --> GalleyBus["Galley / IFE\nAC Bus"]
    A024_050 --> SSPC_AC["Solid State Power\nControllers (SSPC — AC)"]
    A024_050 --> LoadShed["Load Shedding\nLogic"]

    A024_020["024-020 AC Generation"] -->|AC power| A024_050
    A024_040["024-040 External Power"] -->|GPU AC| A024_050
    A024_050 -->|feeds| AllSystems["Aircraft AC\nPowered Systems"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `024` — Electrical Power |
| Local section code | `024-050` |
| ATA SNS | `24-50-00` |
| Primary Q-Division | Q-MECHANICS |
| Support Q-Divisions | Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/024_Electrical-Power/` |
| Document | `024-050-AC-Electrical-Load-Distribution.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 24-50, AC Electrical Load Distribution
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `024-020` AC Generation [`./024-020-AC-Generation.md`](./024-020-AC-Generation.md)
- `024-060` DC Electrical Load Distribution [`./024-060-DC-Electrical-Load-Distribution.md`](./024-060-DC-Electrical-Load-Distribution.md)
- `024-070` Emergency, Standby and Essential Power [`./024-070-Emergency-Standby-and-Essential-Power.md`](./024-070-Emergency-Standby-and-Essential-Power.md)
