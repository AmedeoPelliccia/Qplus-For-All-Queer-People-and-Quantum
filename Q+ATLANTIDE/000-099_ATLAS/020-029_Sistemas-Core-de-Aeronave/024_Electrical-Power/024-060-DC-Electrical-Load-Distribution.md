---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-024-060-DC-ELECTRICAL-LOAD-DISTRIBUTION
title: "ATLAS 020-029 · 02.024 · Section 024-060 — DC Electrical Load Distribution"
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
local_section_code: "024-060"
ata_sns: "24-60-00"
title_short: "DC Electrical Load Distribution"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.024 · 024-060 — DC Electrical Load Distribution

## 1. Purpose

Define the architecture boundary for *DC Electrical Load Distribution* (ATA 24-60-00) within ATLAS subsection `024`. This section covers the DC bus architecture, including main DC busses, DC essential bus, hot battery bus, Solid State Power Controllers (SSPC) for DC loads, and the DC load management and protection logic.

## 2. Scope

- Aligned to ATA SNS `24-60-00 DC Electrical Load Distribution`.
- Covers main DC busses (DC BUS 1, DC BUS 2), DC Essential Bus, Hot Battery Bus, SSPC for DC panels, and current sensing/protection devices.
- Includes DC load shedding, cross-tie bus functionality, and distribution panel topology.
- Interfaces: DC generation/TRU (`024-030`), batteries (`024-030`), emergency power (`024-070`), and all DC-powered systems (avionics, instruments, lighting).
- Does not cover AC distribution (see `024-050`) or individual equipment connected to DC busses.

## 3. System Architecture

```mermaid
graph TD
    A024_060["024-060 DC Electrical Load Distribution\n(ATA 24-60-00)"]

    A024_060 --> DCBUS1["DC Bus 1\n(TRU 1)"]
    A024_060 --> DCBUS2["DC Bus 2\n(TRU 2)"]
    A024_060 --> DCESSBUS["DC Essential Bus"]
    A024_060 --> HotBattBus["Hot Battery Bus"]
    A024_060 --> SSPC_DC["Solid State Power\nControllers (SSPC — DC)"]

    A024_030["024-030 DC Generation"] -->|28 VDC| A024_060
    A024_060 -->|feeds| Avionics["Avionics,\nInstruments, Lighting"]
    A024_060 -->|essential loads| A024_070["024-070 Emergency/Standby Power"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `024` — Electrical Power |
| Local section code | `024-060` |
| ATA SNS | `24-60-00` |
| Primary Q-Division | Q-MECHANICS |
| Support Q-Divisions | Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/024_Electrical-Power/` |
| Document | `024-060-DC-Electrical-Load-Distribution.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 24-60, DC Electrical Load Distribution
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `024-030` DC Generation [`./024-030-DC-Generation.md`](./024-030-DC-Generation.md)
- `024-050` AC Electrical Load Distribution [`./024-050-AC-Electrical-Load-Distribution.md`](./024-050-AC-Electrical-Load-Distribution.md)
- `024-070` Emergency, Standby and Essential Power [`./024-070-Emergency-Standby-and-Essential-Power.md`](./024-070-Emergency-Standby-and-Essential-Power.md)
