---
document_id: "QATL-ATLAS-1000-ATLAS-060-069-068-030-ENGINE-SENSORS-AND-TRANSDUCERS"
register: ATLAS-1000
title: "Engine Sensors and Transducers"
ata: "ATA 68"
sns: "068-030-00"
subsection: "068"
subsubject_code: "030"
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
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0068-030"
standard_scope: agnostic
programme_specific: false
---

# Engine Sensors and Transducers

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![ATA: ATA 68](https://img.shields.io/badge/ATA-68-green)
![Q-Division: Q-MECHANICS](https://img.shields.io/badge/Q--Division-Q--MECHANICS-orange)

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Engine Sensors and Transducers`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 Applicability

| Applicability Level | Rule |
|---|---|
| Standard taxonomy | Applies to the ATLAS node `068` |
| Programme implementation | Conditional; determined by programme architecture, trade studies, certification basis, and applicability model |
| Product configuration | Defined in the programme-specific configuration baseline |
| Effectivity | Defined in the programme CSDB / applicability layer |
| Non-applicability | Must be explicitly stated in the programme impact-study branch when excluded |
## §3 Sensor Inventory ![DRAFT]

| Sensor Type | Symbol | Qty/Engine | Location | Output Signal | DO-160G Cat |
|---|---|---|---|---|---|
| Low-Pressure Speed Sensor | N1 | 1 | Fan frame — phonic wheel | Frequency (pulse) | F (vibration) |
| High-Pressure Speed Sensor | N2 | 1 | HPC case — phonic wheel | Frequency (pulse) | F |
| EGT Thermocouple (K-type) | EGT | 4 | LPT exhaust frame — harness | mV (differential) | U (temperature) |
| Fuel Flow Transducer | FF | 1 | HPC fuel supply line | Frequency turbine flow | B (humidity) |
| Oil Pressure Transducer | OP | 1 | Main oil gallery — scavenge outlet | 4–20 mA | C (temperature) |
| Oil Temperature RTD | OT | 1 | Oil tank return port | Resistance (Pt100) | C |
| Oil Quantity Sensor | OQ | 1 | Oil tank | Capacitive / ultrasonic | B |
| Fan Frame Vibration Accelerometer | VIB-N1 | 2 | Fan frame 12 o'clock & 6 o'clock | Charge (pC) | F |
| LPT Frame Vibration Accelerometer | VIB-N2 | 2 | LPT frame 12 o'clock & 6 o'clock | Charge (pC) | F |
| Fuel Temperature Thermocouple | FT | 1 | Fuel/oil heat exchanger outlet | mV (differential) | B |

---

## §4 Sensor Routing

All sensor harnesses are routed via the engine firewall bulkhead connectors to the Engine Data Concentrator (EDC) mounted on the pylon forward zone. DO-160G-qualified shielded twisted-pair cables are used throughout. Harness separation from hydraulic lines is maintained per AMM.

---

## §5 Sensor Redundancy

- EGT: 4 thermocouples per engine; FADEC averages all four; single TC failure triggers ECAM advisory.
- VIB: Dual accelerometers per axis (fan / LPT); FADEC selects higher reading as protection parameter.
- N1/N2: Single primary sensor per spool; FADEC monitors for stale or out-of-range data.

---

## §6 Interfaces

| Interface | Connected System | Data |
|---|---|---|
| EDC (ATA 68-040) | Data concentrator | All analog/frequency signals |
| FADEC (ATA 73) | Engine controller | Processed digital values |
| AMM Chapter 68 | Maintenance | Sensor replacement procedures |

---

## §7 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-068-030-001 | Confirm N1 phonic wheel tooth count with OEM | Q-MECHANICS | 2026-Q4 |

---

## §8 Change Log

| Rev | Date | Author | Description |
|---|---|---|---|
| 0.1 | 2026-05-11 | @copilot | Initial DRAFT — programme-defined aircraft type contextualization |
