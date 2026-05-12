---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-083-080-SOLAR-ELECTRIC-AUXILIARY-MONITORING-DIAGNOSTICS-AND-CONTROL-INTERFACES"
register: ATLAS-1000
title: "Solar-Electric Auxiliary — Monitoring, Diagnostics and Control Interfaces"
ata: "ATLAS-083 (Solar-Electric Auxiliary)"
sns: "083-080-00"
subsection: "083"
subsubject_code: "080"
primary_q_division: Q-HPC
support_q_divisions: [Q-GREENTECH, Q-INDUSTRY, Q-HORIZON]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0083-080"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-083-080-SOLAR-ELECTRIC-AUXILIARY-MONITORING-DIAGNOSTICS-AND-CONTROL-INTERFACES
     ATLAS-083 (Solar-Electric Auxiliary) · Monitoring, Diagnostics and Control
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Solar-Electric Auxiliary — Monitoring, Diagnostics and Control Interfaces

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-083 Solar-Electric](https://img.shields.io/badge/ATLAS--083-Solar--Electric%20Auxiliary-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-HPC](https://img.shields.io/badge/Q--Division-Q--HPC-navy)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

ATLAS subsubject 083-080 defines the SEACU BITE architecture, monitored parameters, AFDX virtual link allocation, CMS fault code table, EPMS research telemetry, FDR parameter list, control loop overview (MPPT P&O algorithm, SCAP charge control, motor FOC), and maintenance ground support interface for the Solar-Electric Auxiliary system.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA reference | ATLAS-083 — 083-080 Monitoring, Diagnostics and Control Interfaces |
| Certification basis | EASA CS-25 Amdt 27+; DO-178C DAL C; ARINC 664 P7; ARINC 429 (advisory outputs) |
| S1000D SNS | 083-080-00 |

---

## §3 SEACU BITE Architecture

### 3.1 BITE Modes

| BITE Mode | Trigger | Coverage | Duration |
|---|---|---|---|
| Power-On BIT (POBIT) | HVDC 270 V applied to SEACU | All LRU self-test; MPPT open-loop check; SCAP voltage read; battery BMS comms check | 45 s |
| Continuous BIT (CBIT) | All in-flight operational modes | Ongoing monitoring (1 Hz); comparison to alarm thresholds | Continuous |
| Initiated BIT (IBIT) | Maintenance command via GSE or CMS | Full system functional test; MPPT load sweep; SCAP discharge/recharge partial cycle; propulsor no-load spin test | 8 min; aircraft on ground only |
| Post-Flight BITE Report | At power-down | Consolidation of all in-flight fault records; write to NVM; available via GSE port | Automatic |

### 3.2 Monitored Parameters (CBIT, 1 Hz)

| Parameter | Sensor | Alarm L1 | Alarm L2 | Alarm L3 |
|---|---|---|---|---|
| PV string current (6 channels × 4 strings = 24 measurements) | Hall-effect clamp sensor | < 0 A (reverse) | > 115 % rated | > 130 % rated |
| PV string open-circuit voltage (6 channels) | Voltage divider | > 130 V (over-voltage) | > 140 V | > 150 V → isolate |
| MPPT output power (6 channels) | Computed from V × I | < 50 % expected from irradiance model | < 10 % expected | Fault → channel shut down |
| SCAP voltage (bank total) | Resistive divider | > 720 V or < 340 V | > 730 V or < 330 V | > 740 V → crowbar |
| SCAP cell voltage (280 cells, 1 Hz average by module) | Module BMS | Δ > 50 mV between modules | Δ > 100 mV | Module disconnect |
| Battery SoC (%) | BMS EKF | < 30 % or > 88 % | < 22 % or > 90 % | < 20 % → propulsor off |
| Battery cell temperature (max cell Tj) | NTC thermistor per module | > 45 °C | > 55 °C | > 65 °C → BMS relay open |
| Propulsor motor speed (4 nodes) | Resolver (encoder integral to iPMSM) | ±5 % from demanded | ±10 % from demanded | Stall → SSPC trip |
| Propulsor motor winding temperature (4 nodes) | PT100 embedded in winding | > 140 °C | > 160 °C | > 175 °C → SSPC trip |
| SiC inverter junction temperature (8 modules) | NTC on SiC baseplate | > 110 °C | > 120 °C | > 130 °C → derate |
| DC link voltage (700 V) | Voltage divider | < 650 V or > 720 V | < 630 V or > 730 V | < 600 V → SCAP boost |
| HVDC 270 V bus tie current | Hall-effect sensor | > 95 % rated (±80 kW) | > 100 % rated | > 110 % → SSPC trip |
| Insulation resistance (DC link to airframe) | IMD (Bender ISOMETER) | < 500 kΩ·kW | < 200 kΩ·kW | < 100 kΩ·kW → fault |

---

## §4 AFDX Virtual Link Allocation

| VL ID | Direction | Bandwidth (MB/s) | Period (ms) | Destination | Content |
|---|---|---|---|---|---|
| VL-083-01 | SEACU → CMS (ATA 45) | 0.5 | 100 | CMS fault processor | BITE fault codes; SEACU health status; SCAP SoE; battery SoC |
| VL-083-02 | SEACU → EMS (ATLAS 079) | 1.0 | 50 | EMS energy dispatcher | SEA power state vector; available export to HVDC; propulsor demand |
| VL-083-03 | SEACU → FADEC (ATA 73) | 0.2 | 100 | FADEC advisory channel | SEA net thrust (N); operational mode (advisory, no command authority) |
| VL-083-04 | SEACU → EPMS | 5.0 | 10 | Research EPMS | Full 10 Hz telemetry: all 24 PV strings; all MPPT; SCAP; battery; all propulsors; irradiance model |
| VL-083-05 | SEACU → TMS (ATLAS 074) | 0.2 | 200 | TMS thermal controller | SEACU cold plate temp; inverter Tj; battery thermal demand |
| VL-083-06 | EMS → SEACU | 0.5 | 50 | SEACU power arbitrator | Power dispatch command (kW); mode command (solar/battery/emergency) |

---

## §5 CMS Fault Code Table (Key Fault Codes)

| Fault Code | Description | Severity | SEA Response | Maintenance Action |
|---|---|---|---|---|
| SEA-001 | MPPT CH-1 failure (harvest < 10 % expected) | Advisory | Continue; CH-1 isolated | Check PV string CH-1; replace MPPT module if MPPT IBIT fails |
| SEA-002 | MPPT CH-2 failure | Advisory | Continue; CH-2 isolated | Check PV string CH-2 |
| SEA-003 | MPPT CH-3 failure | Advisory | Continue; CH-3 isolated | Check PV string CH-3 |
| SEA-004 | MPPT CH-4 failure | Advisory | Continue; CH-4 isolated | Check PV string CH-4 |
| SEA-005 | MPPT CH-5 failure | Advisory | Continue; CH-5 isolated | Check PV string CH-5 |
| SEA-006 | MPPT CH-6 (winglet) failure | Advisory | Continue; CH-6 isolated | Check winglet PV panel |
| SEA-010 | SCAP over-voltage (> 730 V) | Caution | Crowbar activated; SCAP isolated | Inspect SCAP bank; check bleed resistor |
| SEA-011 | SCAP under-voltage (< 330 V) | Caution | DM-1 buffering reduced | Check SCAP SoE; inspect contactor |
| SEA-012 | SCAP cell imbalance (Δ > 100 mV) | Advisory | Continue; advisory | C-check SCAP balancing board |
| SEA-020 | Battery SoC < 22 % | Caution | DM-2: propulsors at 20 % throttle | Normal; charge on ground |
| SEA-021 | Battery over-temperature (Tj > 65 °C) | Warning | BMS relay open; battery isolated | Inspect battery thermal circuit; check EGW flow |
| SEA-022 | Battery Novec 1230 discharge | Emergency | Battery isolated; all SEA isolated | Ground; Novec bottle replacement; battery inspection |
| SEA-030 | SEACU CHA failure | Caution | DM-3: CHB active | Replace or reset SEACU CHA at next maintenance |
| SEA-031 | SEACU CHB failure | Caution | CHA remains active; dual-channel lost | Treat as SEA single-channel — ground at next opportunity |
| SEA-032 | SEACU dual-channel failure | Warning | DM-5: total SEA shutdown | Ground immediately; replace SEACU |
| SEA-040 | Propulsor L motor over-temp | Advisory | Propulsor L throttle limited | Inspect motor; check winding PT100; replace if failed |
| SEA-041 | Propulsor R motor over-temp | Advisory | Propulsor R throttle limited | Inspect motor; check winding PT100 |
| SEA-050 | Propulsor L stall (speed error > 10 %) | Caution | DM-4: Propulsor L SSPC trip | Inspect fan for FOD; check motor resolver |
| SEA-051 | Propulsor R stall | Caution | DM-4: Propulsor R SSPC trip | Inspect fan for FOD |
| SEA-060 | Insulation resistance low (< 100 kΩ·kW) | Warning | SEACU fault; DM-5 initiated | Ground immediately; HiPot test all cables; replace damaged cable |

---

## §6 EPMS Research Telemetry (10 Hz)

| Parameter Group | Parameters | Rate |
|---|---|---|
| PV harvest | 24 string currents; 6 channel voltages; 6 MPPT output powers; irradiance model prediction; actual vs. predicted ratio | 10 Hz |
| SCAP | Bank voltage; bank current; SoE %; cell voltage (280, averaged per module) | 10 Hz |
| Battery | SoC %; cell temperature (max/min/avg); charge/discharge current; remaining capacity | 10 Hz |
| DC link | Voltage; total SEACU input power; export to HVDC 270 V bus | 10 Hz |
| Propulsors (4 nodes) | Speed (RPM); torque (Nm); power (kW); motor temperature; regenerative power; propulsive efficiency (computed) | 10 Hz |
| SEACU internals | Channel A/B active flag; degraded mode code; MPPT algorithm convergence flag; power arbitration state | 10 Hz |

---

## §7 FDR / QAR Parameters

Per ICAO Annex 6 extended research parameter list for AMPEL360E eWTW flight test:

| Parameter | Resolution | Range |
|---|---|---|
| SEA total electrical power (kW) | 1 kW | 0–150 kW |
| Battery SoC (%) | 1 % | 0–100 % |
| SCAP SoE (%) | 1 % | 0–100 % |
| Propulsor L and R speed (RPM) | 100 RPM | 0–16 000 RPM |
| Propulsor L and R thrust (N, estimated) | 10 N | 0–1 000 N |
| SEACU degraded mode code | — | 0–5 (integer) |
| Solar irradiance (estimated, W/m²) | 10 W/m² | 0–1 500 W/m² |

---

## §8 Control Loop Overview

### 8.1 MPPT Perturb-and-Observe (P&O) Algorithm

1. At each 10 ms cycle, SEACU increments MPPT duty cycle by Δd (variable step, 0.2–2 %)
2. Measure Pout = V × I after settling (1 ms)
3. If Pout increased → continue same direction; if Pout decreased → reverse direction
4. Step size Δd adapted: larger step during rapid irradiance change (dG/dt > 50 W/m²/s from EPMS weather model); smaller step at steady irradiance for tight tracking
5. Independent P&O per channel (6 instances); cross-channel irradiance feed used to initialise duty cycle after occlusion recovery

### 8.2 SCAP Charge Control

- SEACU monitors SCAP SoE; if SoE < 70 %, SCAP DC/DC converter is commanded to absorb power from DC link (charge mode) at up to 50 kW continuous
- If SoE > 90 % and propulsors at full demand, SCAP DC/DC switches to idle (no charging; DC link supplied by MPPT only)
- During propulsor transient (speed change command): SCAP DC/DC commanded to discharge at current setpoint proportional to demanded torque rate; MPPT commanded to maintain DC link voltage via voltage-mode control

### 8.3 Propulsor Motor FOC

- Field-Oriented Control (FOC) implemented per propulsor inverter
- d-axis current (id) set to 0 for IPMSM below rated speed; MTPA above rated speed switches to flux weakening (negative id)
- Speed outer loop: PI controller (Kp = 0.8, Ki = 12 s⁻¹; bandwidth 50 Hz)
- Torque inner loop: PI controller (Kp = 0.05, Ki = 200 s⁻¹; bandwidth 1 000 Hz)
- Anti-windup on all integrators; torque limit = ±200 Nm per motor

---

## §9 Ground Support Interface

| Interface | Connector | Protocol | Functions |
|---|---|---|---|
| SEACU GSE port (primary) | USB-C 3.2 Gen 2 (10 Gbps) | Proprietary SEACU GSE protocol over USB | POBIT / IBIT command; fault log download; MPPT calibration; software upload (DO-178C change control) |
| SEACU Ethernet GSE | RJ-45 (1000BASE-T) | TFTP / secure shell | SEACU firmware upload; AFDX network diagnostic; EPMS data burst download |
| SEACU front panel indicators | LED panel | Visual | PWR ON (green); CHA ACTIVE (blue); CHB ACTIVE (amber); FAULT (red); SOLAR ARRAY ISOLATED (white); SCAP DISCHARGED (white) |
| BLI FAN ZONE CLEAR | GSE software command | SEACU GSE USB-C | Enables propulsor inverter gate signals during ground run-up; confirms operator zone clearance |

---

## §10 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-083-080-001 | MPPT P&O step size tuning under simulated cloud shadow profile — HIL test | Q-HPC | PDR |
| OI-083-080-002 | AFDX VL-083-04 (10 Hz EPMS) bandwidth allocation review — conflict with ATLAS 084 EPMS VLs | Q-HPC | CDR |
| OI-083-080-003 | CMS fault code integration with AMPEL360E ECAM display layout — crew advisory format approval | Q-HORIZON | CDR |
| OI-083-080-004 | FDR parameter recording format and ICAO Annex 6 research extension documentation | Q-HORIZON | Phase 2 |
