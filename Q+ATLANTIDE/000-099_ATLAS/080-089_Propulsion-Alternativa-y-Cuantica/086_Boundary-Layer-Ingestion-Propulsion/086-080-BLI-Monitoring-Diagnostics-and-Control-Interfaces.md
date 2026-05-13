---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-086-080-BLI-MONITORING-DIAGNOSTICS-AND-CONTROL-INTERFACES"
register: ATLAS-1000
title: "BLI Monitoring, Diagnostics and Control Interfaces"
ata: "ATLAS-086 (Boundary Layer Ingestion Propulsion)"
sns: "086-080-00"
subsection: "086"
subsubject_code: "080"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HPC, Q-INDUSTRY, Q-HORIZON]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0086-080"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-086-080-BLI-MONITORING-DIAGNOSTICS-AND-CONTROL-INTERFACES
     ATLAS-086 (Boundary Layer Ingestion Propulsion) · BLI Monitoring, Diagnostics and Control Interfaces
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# BLI Monitoring, Diagnostics and Control Interfaces

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-086 BLI Propulsion](https://img.shields.io/badge/ATLAS--086-BLI%20Propulsion-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-teal)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

ATLAS subsubject 086-080 defines the BLI system monitoring sensor suite, the BLICU Built-In Test Equipment (BITE) architecture, the cockpit and MFD synoptic interface, the AFDX data bus configuration, and the GSE maintenance interface for the AMPEL360E eWTW BLI Propulsion system.

---

## §2 Sensor Suite

### 2.1 Primary Monitoring Sensors

| Sensor ID | Type | Location | Range | Sample Rate | Interface |
|---|---|---|---|---|---|
| TPR-086-1A…1P | Total pressure probes (16 × per fan) | BLI-PA-1 fan face | 30–120 kPa | 100 Hz | BLICU ADC (differential, 12-bit) |
| TPR-086-2A…2P | Total pressure probes (16 × per fan) | BLI-PA-2 fan face | 30–120 kPa | 100 Hz | BLICU ADC |
| TT-086-101/102 | Thermocouple (K-type) | PMSM stator winding (2 per motor) | −55 to +200 °C | 10 Hz | BLICU via PT100 bridge |
| TT-086-201/202 | PT100 RTD | MCU-086 IGBT heatsink | −40 to +100 °C | 10 Hz | MCU-086 internal ADC |
| SP-086-101/102 | Tachometer (resolver) | Fan shaft (redundant pair per motor) | 0–7 000 RPM | 1 kHz | MCU-086 resolver interface |
| VI-086-101/102 | Current transducer (HVDC 270 V feed) | MCU-086 input rail | 0–600 A DC | 10 kHz | MCU-086 FOC loop |
| VV-086-101/102 | Voltage sensor | MCU-086 DC link | 0–300 V DC | 10 kHz | MCU-086 FOC loop |
| AC-086-F1/F2 | MEMS accelerometer (3-axis) | BLI-PA fan casing | ±50 g | 1 kHz | BLICU via ARINC 429 |
| FL-086-T1/T2 | Coolant flow sensor | BLITM coolant inlet | 0–15 L/min | 1 Hz | BLICU via ARINC 429 |
| PS-086-I1/I2 | Static pressure tap | S-duct mid-section | 30–120 kPa | 50 Hz | BLICU ADC |

---

## §3 BITE Architecture

### 3.1 BLICU BITE Functions

The BLICU BITE system provides:

| BITE Function | Level | Trigger | Output |
|---|---|---|---|
| Power-On Self-Test (POST) | L1 | BLICU power-on | GO/NO-GO within 5 s; prevents operation if fail |
| Continuous Monitoring (CM) | L1 | All modes except STANDBY | Real-time fault detection; < 50 ms detection latency |
| Maintenance BITE (MAINT) | L2 | GSE command via BLICU-GSE-1 | Full sensor sweep; LRU status; fault history |
| Extended BITE (EBIT) | L3 | GSE command — ground only | Actuates bypass doors; spins fans to 1 000 RPM; verifies all I/O channels |

### 3.2 Fault Classification

| Class | Code Range | Description | Crew Action |
|---|---|---|---|
| CAS Warning (red) | F-086-001–020 | Immediate airworthiness threat (stall, motor overheat, MCU fail) | Immediate BLI shutdown per QRH |
| CAS Caution (amber) | F-086-021–060 | Degraded performance; monitor | Monitor; land at next opportunity |
| Maintenance Message | F-086-061–120 | Non-airworthiness fault; maintenance action required | Log; address at next check |
| Advisory | F-086-121–200 | Information only; trend data | No action required |

### 3.3 Top-10 FMEA Failure Modes

| ID | Failure Mode | Effect | Detection | Mitigation |
|---|---|---|---|---|
| FM-086-001 | PMSM winding short circuit | Sudden torque loss; BLI-PA shutdown | Differential current protection; CM | MCU-086 hardware latch; bypass open |
| FM-086-002 | MCU-086 IGBT failure (open) | Loss of phase; torque ripple spike | CM phase current monitor | Graceful shutdown; Channel B |
| FM-086-003 | TPR rake probe blockage | DC60 underestimation | Probe differential vs. reference | Probe heater; flagged in BITE |
| FM-086-004 | BLICU Channel A fault | Control degradation | BLICU watchdog crosslink | Switchover to Channel B in < 50 ms |
| FM-086-005 | Fan blade tip rub | Vibration spike; efficiency loss | AC-086 accelerometer 3σ | Speed reduce; maintenance inspect |
| FM-086-006 | S-duct bypass door stuck closed | Fan stall risk on BLICU fail | BITE door position switch | Spring-loaded fail-safe; door opens |
| FM-086-007 | BLITM pump failure (both) | PMSM overtemperature | TT-086 alarms T2 level | Speed reduce; TT T3 → shutdown |
| FM-086-008 | AFDX VL-086-01 loss (FADEC link) | No AoA correction table update | BLICU AFDX watchdog | Use last valid AoA; caution alert |
| FM-086-009 | Fan resolver failure (one) | Speed control degradation | MCU resolver plausibility | Second resolver active; maintenance |
| FM-086-010 | MCU-086 DC link overvoltage | MCU trip; BLI shutdown | VV-086 overvoltage comparator | MCU hardware protection; BLI off |

---

## §4 Cockpit and MFD Interface

### 4.1 Crew Alerting System (CAS) Messages

| CAS Message | Level | Condition | Crew Action |
|---|---|---|---|
| `BLI CAUTION` | Amber | DC60 > 0.25 or any F-021–060 fault | Monitor; check ENG page |
| `BLI DISTORT HIGH` | Amber | DC60 > 0.30 for > 5 s | Speed trim active; monitor BLI status |
| `BLI STALL RISK` | Red | DC60 > 0.34 | QRH BLI STALL RISK procedure |
| `BLI FAIL` | Red | FM-001, 002, 006, or T3 overheat | QRH BLI FAIL procedure; bypass open |
| `BLI DEGRADED` | Amber | BLICU channel switchover | Advise maintenance; continue flight |
| `BLI THERMAL WARN` | Amber | PMSM T2 > 140 °C | Monitor temp; land at next opportunity |
| `BLI FAIL HOT` | Red | PMSM T3 > 150 °C | QRH BLI FAIL HOT procedure |
| `BLI FAIL MCU HOT` | Red | MCU T3 > 65 °C | QRH BLI FAIL MCU HOT procedure |

### 4.2 MFD Synoptic Page — BLI Status

The BLI synoptic page on the AMPEL360E MFD (ENG page) displays:

| Parameter | Format | Update Rate |
|---|---|---|
| BLI-PA-1 / PA-2 fan speed | Digital RPM + analogue arc | 1 Hz |
| BLI-PA-1 / PA-2 fan power | kW bar graph | 1 Hz |
| DC60 distortion index (per propulsor) | Analogue gauge 0–0.40 | 2 Hz |
| PMSM temperature (per motor) | °C digital | 0.5 Hz |
| BLICU mode (text) | Mode text (e.g., CRUISE_BLI) | 1 Hz |
| Bypass door status | OPEN / CLOSED indicator | 1 Hz |

---

## §5 AFDX Interface Configuration

| Virtual Link | From | To | Bandwidth | Data |
|---|---|---|---|---|
| VL-086-01 | BLICU | FADEC (ATA 73) | 10 Kbps | BLI power demand; AoA request; mode status |
| VL-086-02 | BLICU | EMS (ATLAS-079) | 20 Kbps | Power allocation request; speed setpoint |
| VL-086-03 | BLICU | CMS (ATA 45) | 50 Kbps | BITE faults; LRU health; fault history |
| VL-086-04 | BLICU | EPMS (research) | 200 Kbps | Full 50 Hz telemetry; TPR rake data; DC60 |
| VL-086-05 | BLICU | TMS (ATLAS-074) | 10 Kbps | PMSM/MCU temperatures; coolant flow |

---

## §6 GSE Interface

| GSE Function | Tool / Equipment | Interface | Notes |
|---|---|---|---|
| BLICU software load | BLICU-GSE-1 | USB-C 3.2 (10 Gbit) | Requires aircraft power; BLI in STANDBY |
| BITE MAINT download | BLICU-GSE-1 | USB-C 3.2 | Fault history; sensor logs |
| Extended BITE (EBIT) | BLICU-GSE-1 | USB-C 3.2 + AFDX tap | Ground only; bypass actuated; fans at 1 000 RPM |
| MCU-086 calibration | MCU-GSE-086 | CAN 2.0B (dedicated port) | FOC gain calibration; resolver offset check |
| TPR probe calibration | CAL-086-001 kit | Direct pneumatic | Reference pressure: 101.325 kPa ±0.01 % |
| BLITM coolant fill | TL-074-003 | EGW quick-disconnect | 50/50 EGW; fill to MAX mark; bleed air |

---

## §7 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-086-080-001 | MFD BLI synoptic page HMI review — pilot usability assessment | Q-GREENTECH | CDR |
| OI-086-080-002 | AFDX VL bandwidth allocation — confirm with network management plan | Q-HPC | PDR |
| OI-086-080-003 | EBIT procedure — bypass actuated at 1 000 RPM safety review | Q-INDUSTRY | CDR |
| OI-086-080-004 | CAS message wording review — align with AMPEL360E CAS style guide | Q-GREENTECH | PDR |
