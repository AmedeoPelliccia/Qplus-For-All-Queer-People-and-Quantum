---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-085-080-DEP-MONITORING-DIAGNOSTICS-AND-CONTROL-INTERFACES"
register: ATLAS-1000
title: "DEP Monitoring Diagnostics and Control Interfaces"
ata: "ATLAS-085 (Distributed Electric Propulsion Architecture)"
sns: "085-080-00"
subsection: "085"
subsubject_code: "080"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HPC, Q-INDUSTRY, Q-STRUCTURES]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0085-080"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-085-080-DEP-MONITORING-DIAGNOSTICS-AND-CONTROL-INTERFACES
     ATLAS-085 (Distributed Electric Propulsion Architecture) · DEP Monitoring Diagnostics and Control Interfaces
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# DEP Monitoring Diagnostics and Control Interfaces

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-085 DEP Architecture](https://img.shields.io/badge/ATLAS--085-DEP%20Architecture-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-teal)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

ATLAS subsubject 085-080 defines the DEPCU Built-In Test Equipment (BITE) architecture, the cockpit synoptic MFD page for the DEP system, all AFDX virtual-link (VL) definitions for DEPCU data outputs, the ground support equipment (GSE) interface, the research telemetry interface with the EPMS (Experimental Propulsion Monitoring System), and the maintenance diagnostic download procedures.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA Reference | ATLAS-085 — 085-080 DEP Monitoring Diagnostics and Control Interfaces |
| Certification Basis | DO-178C DAL B (DEPCU BITE); DO-160G; ATA MSG-3 (maintenance task selection) |
| S1000D SNS | 085-080-00 |

---

## §3 DEPCU BITE Architecture

The DEPCU implements two levels of BITE:

**Level 1 — Continuous Monitoring (in-flight):**
Executes on both DEPCU channels at every 10 ms control cycle. Monitors:
- Per-MDU: output voltage, phase current (3-phase), switching frequency, IGBT junction temperature, coolant temperature.
- Per-PMSM: shaft speed (encoder), winding temperature, bearing vibration (RMS).
- Per-BTB: position feedback (open/closed); coil current.
- DEPCU internal: RAM parity; CPU watchdog; CAN error counters; AFDX frame sequence.
- Bus: HVDC bus voltage (DPDP instrumented); DEP-IMU insulation resistance (each rail).

**Level 2 — Ground BITE (maintenance download):**
Initiated via DEPCU-GSE-1. Full fault memory download (FMEM): 1 000 most recent fault events with timestamp and channel. PMSM vibration spectrum (FFT) snapshot per propulsor. MDU gate-driver event log. DEP-TML flow and temperature history at 1 Hz.

---

## §4 BITE Fault Classification

| Class | Description | DEPCU Action | Crew Indication |
|---|---|---|---|
| Class A — Advisory | Non-critical parameter trend; no immediate action | Log; send to CMS at next 1 Hz cycle | White STATUS message on ECAM |
| Class B — Caution | Parameter approaching limit; potential degradation | Log; send to CMS; derate MDU if thermal | Amber CAUTION on ECAM; DEP MFD amber bar |
| Class C — Warning | Limit exceeded; degraded mode imminent | Log; initiate automatic reconfiguration | Red WARNING on ECAM; aural chime |
| Class D — Fault | Hard fault; BTB open command; degraded mode entered | Log; BTB open; degraded mode; crew advisory | Red FAULT on ECAM; DEP MFD propulsor bar extinguished |

---

## §5 BITE Fault Code Table (Selected)

| Fault Code | Description | Class | Auto Action |
|---|---|---|---|
| DEP-0001 | MDU-1 over-temperature (cold plate > 55 °C) | D | BTB-P1 open; DM-1 |
| DEP-0002 | MDU-2 over-temperature | D | BTB-P2 open; DM-1 |
| DEP-0003 | MDU-3 over-temperature | D | BTB-P3 open; DM-1 |
| DEP-0004 | MDU-4 over-temperature | D | BTB-P4 open; DM-1 |
| DEP-0010 | PMSM-1 winding temperature > 180 °C | D | BTB-P1 open |
| DEP-0011 | PMSM-2 winding temperature > 180 °C | D | BTB-P2 open |
| DEP-0012 | PMSM-3 winding temperature > 180 °C | D | BTB-P3 open |
| DEP-0013 | PMSM-4 winding temperature > 180 °C | D | BTB-P4 open |
| DEP-0020 | SSPC-P1 overcurrent trip | D | BTB-P1 open; DM-1 |
| DEP-0021 | SSPC-P2 overcurrent trip | D | BTB-P2 open; DM-1 |
| DEP-0022 | SSPC-P3 overcurrent trip | D | BTB-P3 open; DM-1 |
| DEP-0023 | SSPC-P4 overcurrent trip | D | BTB-P4 open; DM-1 |
| DEP-0030 | CAN Bus A error count > 10 (P1) | B | Switch to CAN Bus B P1 |
| DEP-0031 | CAN Bus A error count > 10 (P2) | B | Switch to CAN Bus B P2 |
| DEP-0032 | CAN Bus A error count > 10 (P3) | B | Switch to CAN Bus B P3 |
| DEP-0033 | CAN Bus A error count > 10 (P4) | B | Switch to CAN Bus B P4 |
| DEP-0040 | DEP-IMU insulation resistance < 100 kΩ | C | Advisory; fault location; crew alert |
| DEP-0041 | DEP-IMU insulation resistance < 50 kΩ | D | BTB open (segment); DM entry |
| DEP-0050 | DEPCU Lane A CPU watchdog timeout | D | Lane B takeover; DM-5 |
| DEP-0060 | DEP-TML pump A flow < 8 L/min | B | Pump B start; advisory |
| DEP-0061 | DEP-TML pump B flow < 8 L/min (pump B active) | C | Crew warning; no redundant pump |

---

## §6 Cockpit Synoptic MFD Page (DEP Synoptic)

The DEP synoptic page is displayed on the right-hand MFD in the ECAM stack. It shows:

- **Four propulsor status bars** (P1, P2, P3, P4): colour-coded by power level — green (>300 kW), amber (150–300 kW derated), red (fault/off); numeric kW readout per propulsor.
- **DEP Bus voltage** (DPDP): numeric readout in V DC; green 780–820 V; amber 760–840 V; red outside range.
- **Total DEP power** (kW): sum of P1–P4.
- **DEPCU lane status**: LANE A / LANE B — green (active), amber (standby/monitoring).
- **DEP-TML temperature**: coolant supply temperature in °C; green ≤ 50 °C; amber 50–55 °C; red > 55 °C.
- **Active mode indicator**: NORMAL / DM-1…DM-5 / REGEN.
- **Insulation status (DEP-IMU)**: OK / ADVISORY / FAULT.

---

## §7 AFDX Virtual-Link Definitions

| VL ID | Direction | From | To | Content | Rate |
|---|---|---|---|---|---|
| VL-085-01 | Input | FADEC (ATA 73) | DEPCU | Total DEP thrust demand; phase command | 10 Hz |
| VL-085-02 | Output | DEPCU | CMS (ATA 45) | BITE faults; MDU health; energy totals; fault memory summary | 1 Hz |
| VL-085-03 | Output | DEPCU | FMS (ATA 22) | Differential thrust advisory; yaw moment availability | 10 Hz |
| VL-085-04 | Output | DEPCU | EPMS | Full 100 Hz per-propulsor power; MDU telemetry; BLI pressure; vibration | 100 Hz |
| VL-085-05 | Output | DEPCU | TMS (ATLAS-074) | DEP-TML coolant temps; MDU heat load; pump status | 1 Hz |
| VL-085-06 | Bidirectional | DEPCU ↔ BGSCU (ATLAS-084) | Total DEP power demand; per-propulsor actuals; regen available; curtailment command | 10 Hz |
| VL-085-07 | Input | BGSCU (ATLAS-084) | DEPCU | Bus voltage; power curtailment; emergency load-shed discrete | 10 Hz |

---

## §8 Ground Support Equipment (GSE) Interface

| GSE Function | Interface | Equipment ID | Procedure |
|---|---|---|---|
| DEPCU parameter upload | USB-C 3.2 + DEPCU-GSE-1 port | DEPCU-GSE-1 | DEPCU software load (DO-178C SOI-4); aero-propulsive table update |
| BITE download | USB-C 3.2 | DEPCU-GSE-1 | Ground BITE Level 2 download; FMEM, vibration FFT, MDU event log |
| MDU FOC calibration | USB-C 3.2 + MDU service port (nacelle) | MDU-GSE-CAL | MDU encoder offset calibration; IGBT deadtime calibration |
| BTB functional test | Discrete test lead (DPDP BTB test port) | BTB-TEST-SET | Open/close cycle test; position feedback confirm |
| HiPot test (HVDC cables) | HV test port (DPDP) | HIPOT-800V | 1 500 V DC HiPot per C-check; per BTB feeder individually |

---

## §9 Research Telemetry (EPMS Interface)

The DEP subsystem provides the highest-bandwidth research telemetry output to the EPMS via AFDX VL-085-04 at 100 Hz. The following parameters are streamed:

| Parameter | Resolution | Rate | Notes |
|---|---|---|---|
| P1…P4 shaft torque command | 1 N·m | 100 Hz | DEPCU setpoint to MDU |
| P1…P4 shaft speed (encoder) | 1 RPM | 100 Hz | MDU encoder feedback |
| P1…P4 electrical power | 100 W | 100 Hz | MDU DC link power |
| P1…P4 MDU cold plate temp | 0.1 °C | 10 Hz | DEP-TML supply per branch |
| P1…P4 PMSM winding temp | 0.1 °C | 10 Hz | MDU-reported |
| DEP bus voltage (DPDP) | 0.1 V | 100 Hz | DPDP instrumented shunt |
| Asymmetric thrust compensator output | 0.1 % | 100 Hz | Differential torque fraction per propulsor |
| DEPCU mode state | Enum | 10 Hz | NORMAL / DM-1…5 / REGEN |
| BLI inlet total pressure (P3/P4) | 0.01 kPa | 100 Hz | Research Pitot array at fan face |

---

## §10 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-085-080-001 | DEP synoptic MFD page layout — ECAM designer review and HMI approval | Q-GREENTECH | PDR |
| OI-085-080-002 | VL-085-04 100 Hz AFDX bandwidth budget — EPMS network load study | Q-HPC | CDR |
| OI-085-080-003 | BITE Class D auto-BTB-open latency verification — 50 ms target iron-bird test | Q-GREENTECH | CDR |
| OI-085-080-004 | BLI inlet Pitot array (P3/P4 research) — fan face distortion probe sizing | Q-HORIZON | Phase 2 |
| OI-085-080-005 | DEPCU FMEM capacity — 1 000 fault events sufficient for 10-hour flight? Increase to 5 000 if log rate > 1 fault/min | Q-HPC | CDR |
