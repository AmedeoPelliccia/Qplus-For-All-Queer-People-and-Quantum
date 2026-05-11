---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-024-070-EMERGENCY-STANDBY-AND-ESSENTIAL-POWER
title: "ATLAS 020-029 · 02.024 · Section 024-070 — Emergency, Standby and Essential Power"
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
local_section_code: "024-070"
ata_sns: "24-70-00"
title_short: "Emergency, Standby and Essential Power"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.024 · 024-070 — Emergency, Standby and Essential Power

## 1. Purpose

Define the architecture boundary for *Emergency, Standby and Essential Power* (ATA 24-70-00) within ATLAS subsection `024`. This section covers the aircraft's last-resort power architecture, including Ram Air Turbine (RAT), emergency bus, standby bus, essential bus topology under dual-generator failure, and the automatic or manual switching logic to sustain flight-critical and safety-critical systems.

## 2. Scope

- Aligned to ATA SNS `24-70-00 Emergency/Standby Power`.
- Covers Ram Air Turbine (RAT) deployment and electrical output, emergency AC and DC busses, standby bus, main battery as emergency source, essential bus load roster (flight controls, core avionics, critical lighting), and automatic bus transfer logic.
- Includes emergency power automatic actuation, manual override, cockpit annunciation, and the priority sequencing of load shedding to sustain minimum essential systems.
- Interfaces: DC generation/battery (`024-030`), DC distribution (`024-060`), flight controls (ATA 27), core avionics (ATA 31/34), and emergency lighting (ATA 33).
- Does not replace individual system emergency power certification data modules — those belong to the respective ATA chapter owners.

**Safety boundary:** Emergency and standby power is flight-safety critical. Any artefact derived from this section requires explicit system effectivity, load priority analysis, failure mode effects analysis (FMEA), RAT deployment certification, battery capacity substantiation, sign-off evidence and lifecycle traceability.

## 3. System Architecture

```mermaid
graph TD
    A024_070["024-070 Emergency, Standby\nand Essential Power\n(ATA 24-70-00)"]

    A024_070 --> RAT["Ram Air Turbine\n(RAT)"]
    A024_070 --> EmergACBus["Emergency AC Bus"]
    A024_070 --> EmergDCBus["Emergency DC Bus"]
    A024_070 --> StandbyBus["Standby Bus"]
    A024_070 --> LoadShedSeq["Priority Load\nShedding Sequence"]
    A024_070 --> AutoTransfer["Auto Bus Transfer\nLogic"]

    A024_030["024-030 DC Generation\n(Battery)"] -->|battery power| A024_070
    A024_070 -->|essential AC| FlightControls["Flight Controls\n(ATA 27)"]
    A024_070 -->|essential DC| CoreAvionics["Core Avionics\n(ATA 31/34)"]
    A024_070 -->|standby lighting| EmergLighting["Emergency Lighting\n(ATA 33)"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `024` — Electrical Power |
| Local section code | `024-070` |
| ATA SNS | `24-70-00` |
| Primary Q-Division | Q-MECHANICS |
| Support Q-Divisions | Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/024_Electrical-Power/` |
| Document | `024-070-Emergency-Standby-and-Essential-Power.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 24-70, Emergency/Standby Power
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `024-030` DC Generation [`./024-030-DC-Generation.md`](./024-030-DC-Generation.md)
- `024-060` DC Electrical Load Distribution [`./024-060-DC-Electrical-Load-Distribution.md`](./024-060-DC-Electrical-Load-Distribution.md)
- `024-080` Electrical Power Monitoring, Diagnostics and Control Interfaces [`./024-080-Electrical-Power-Monitoring-Diagnostics-and-Control-Interfaces.md`](./024-080-Electrical-Power-Monitoring-Diagnostics-and-Control-Interfaces.md)
