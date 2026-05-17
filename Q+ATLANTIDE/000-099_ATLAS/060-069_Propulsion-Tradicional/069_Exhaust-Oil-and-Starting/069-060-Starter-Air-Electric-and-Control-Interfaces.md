---
document_id: "QATL-ATLAS-1000-ATLAS-060-069-069-060-STARTER-ELECTRIC-AND-CONTROL-INTERFACES"
register: ATLAS-1000
title: "Starter — Electric and Control Interfaces"
ata: "ATA 69"
sns: "069-060-00"
subsection: "069"
subsubject_code: "060"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-MECHANICS, Q-AIR, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-11"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
parent_subsubject_doc: "./README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0069-060"
standard_scope: agnostic
programme_specific: false
---

# Starter — Electric and Control Interfaces

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![ATA: ATA 69](https://img.shields.io/badge/ATA-69-green)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-brightgreen)

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Starter — Electric and Control Interfaces`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 Applicability

| Applicability Level | Rule |
|---|---|
| Standard taxonomy | Applies to the ATLAS node `069` |
| Programme implementation | Conditional; determined by programme architecture, trade studies, certification basis, and applicability model |
| Product configuration | Defined in the programme-specific configuration baseline |
| Effectivity | Defined in the programme CSDB / applicability layer |
| Non-applicability | Must be explicitly stated in the programme impact-study branch when excluded |
## §3 SPEC Electrical Interfaces ![DRAFT]

| Interface | Bus / Medium | Function |
|---|---|---|
| HVDC 270 V input | HVDC cable — bus tie contactor controlled | Power supply for motor mode |
| 3-phase AC output to PMSG | Heavy-gauge shielded cable (nacelle routed) | Variable-frequency motor drive |
| AFDX data link (FADEC → SPEC) | AFDX VL (ATA 73) | Start enable, speed setpoint, abort |
| AFDX data link (SPEC → FADEC) | AFDX VL | SPEC status, motor current, fault flags |
| AFDX data link (SPEC → CMS) | AFDX VL | BITE, start event log |
| Discrete — start isolation relay | Hardwired discrete | FADEC hardware-controlled isolation on abort |

---

## §4 SPEC Control Modes

| Mode | Trigger | SPEC State |
|---|---|---|
| Motor mode (start) | FADEC start command + HVDC healthy | SPEC converts HVDC 270 V → variable AC; ramps N2 to target |
| Generator mode (flight) | N2 > 58 % self-sustaining + FADEC command | SPEC transitions to rectifier mode; PMSG → HVDC feed |
| Standby | Engine running, no start active | SPEC in low-power standby; ready for relight |
| Abort isolation | FADEC abort command | SPEC opens input contactor; HVDC disconnected within 50 ms |

---

## §5 Interface Block Diagram — Mermaid Diagram

```mermaid
flowchart LR
    HVDC[HVDC 270 V Bus ATA 24] -->|Bus tie contactor| SPEC_IN[SPEC Input Stage]
    SPEC_IN --> INV[3-phase Inverter]
    INV -->|Variable freq AC| PMSG[PMSG Motor/Generator]
    FADEC[FADEC EEC DAL A ATA 73] -->|AFDX Start Enable + Setpoint| SPEC_CPU[SPEC Controller DAL B]
    SPEC_CPU --> INV
    SPEC_CPU -->|AFDX Status + Current| FADEC
    SPEC_CPU -->|AFDX BITE| CMS[CMS ATA 45]
    SPEC_CPU -->|Discrete abort relay| ISOL_RELAY[Input Contactor Isolation]
```

---

## §6 SPEC Specifications ![TBD]

| Specification | Requirement | Value | Status |
|---|---|---|---|
| Input voltage range | 250–300 V DC | HVDC 270 V nominal | ![TBD] |
| Peak output power | ≤ 200 kW | 180 kW | ![TBD] |
| Efficiency (motor mode) | ≥ 96 % | ≥ 97 % target | ![TBD] |
| DO-178C level | DAL B | DAL B | Confirmed |
| Operating temperature | −55 °C to +70 °C | Per DO-160G Cat U | ![TBD] |

---

## §7 Interfaces

| Interface | Connected System | Data |
|---|---|---|
| HVDC 270 V (ATA 24) | Bus power | Start current draw |
| FADEC (ATA 73) | Controller | Start sequence command |
| CMS (ATA 45) | Maintenance | BITE, start event log |
| PMSG (ATA 69-050) | Machine | AC motor drive current |

---

## §8 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-069-060-001 | Confirm SPEC DO-178C DAL B SW development plan and supplier | Q-GREENTECH | 2027-Q1 |

---

## §9 Change Log

| Rev | Date | Author | Description |
|---|---|---|---|
| 0.1 | 2026-05-11 | @copilot | Initial DRAFT — programme-defined aircraft type contextualization |
