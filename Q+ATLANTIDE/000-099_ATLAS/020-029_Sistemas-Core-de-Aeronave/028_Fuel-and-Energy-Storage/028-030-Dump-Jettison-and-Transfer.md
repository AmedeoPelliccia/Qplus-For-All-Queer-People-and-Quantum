---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-028-030-DUMP-JETTISON-AND-TRANSFER
title: "ATLAS 020-029 · 02.028 · Section 028-030 — Dump, Jettison and Transfer"
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
local_section_code: "028-030"
ata_sns: "28-30-00"
title_short: "Dump, Jettison and Transfer"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.028 · 028-030 — Dump, Jettison and Transfer

## 1. Purpose

Define the architecture boundary for *Fuel Dump, Jettison and Transfer* (ATA 28-30-00) within ATLAS subsection `028`. This section covers fuel jettison system architecture, fuel transfer between tanks, tank-to-tank balancing logic, centre of gravity (CG) fuel management, and jettison control panel and valve interfaces.

## 2. Scope

- Aligned to ATA SNS `28-30-00 Dump`.
- Covers fuel jettison nozzles and jettison pump architecture, jettison flow control valves, jettison rate control and minimum fuel protection, inter-tank transfer pumps, trim tank transfer valves and CG management logic, cross-ship fuel balancing, jettison control panel (cockpit), FCMC transfer and jettison logic, and over-wing and under-wing gravity transfer provisions.
- Includes BITE for jettison valve position and transfer pump run status.
- Does not cover fuel distribution to engines (see `028-020`) or tank storage design (see `028-010`).

**Safety boundary:** Fuel jettison and transfer are safety-critical operations. Minimum fuel protection logic, jettison valve arming, transfer pump serviceability, CG limits, maintenance sign-off, and lifecycle traceability must be preserved with full certification evidence.

## 3. System Architecture

```mermaid
graph TD
    A028_030["028-030 Dump, Jettison\nand Transfer\n(ATA 28-30-00)"]

    A028_030 --> JettisonSystem["Jettison Nozzles\n& Pump System"]
    A028_030 --> JettisonValves["Jettison Flow\nControl Valves"]
    A028_030 --> TransferPumps["Inter-Tank Transfer\nPumps"]
    A028_030 --> TrimTransfer["Trim Tank Transfer\nValves & CG Logic"]
    A028_030 --> BalancingLogic["Cross-Ship Fuel\nBalancing"]
    A028_030 --> JettisonPanel["Jettison Control\nPanel (Cockpit)"]

    A028_010["028-010 Storage"] -->|fuel supply| A028_030
    A028_030 -->|CG data| A028_040["028-040 Indicating"]
    A028_030 -->|health data| A028_080["028-080 Monitoring and Diagnostics"]
    A024["024 Electrical Power"] -->|pump/valve power| A028_030
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `028` — Fuel and Energy Storage |
| Local section code | `028-030` |
| ATA SNS | `28-30-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/028_Fuel-and-Energy-Storage/` |
| Document | `028-030-Dump-Jettison-and-Transfer.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 28-30, Dump
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `028-000` General [`./028-000-General.md`](./028-000-General.md)
- `028-010` Storage [`./028-010-Storage.md`](./028-010-Storage.md)
- `028-040` Indicating [`./028-040-Indicating.md`](./028-040-Indicating.md)
- `028-080` Fuel and Energy Storage Monitoring, Diagnostics and Control Interfaces [`./028-080-Fuel-and-Energy-Storage-Monitoring-Diagnostics-and-Control-Interfaces.md`](./028-080-Fuel-and-Energy-Storage-Monitoring-Diagnostics-and-Control-Interfaces.md)
