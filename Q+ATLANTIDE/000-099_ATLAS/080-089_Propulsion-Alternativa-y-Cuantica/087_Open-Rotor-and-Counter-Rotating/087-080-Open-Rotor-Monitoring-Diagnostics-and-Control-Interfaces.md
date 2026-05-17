---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-087-080-OPEN-ROTOR-MONITORING-DIAGNOSTICS-AND-CONTROL-INTERFACES"
register: ATLAS-1000
title: "Open Rotor Monitoring, Diagnostics and Control Interfaces"
ata: "ATLAS-087 (Open Rotor and Counter-Rotating)"
sns: "087-080-00"
subsection: "087"
subsubject_code: "080"
primary_q_division: Q-HPC
support_q_divisions: [Q-GREENTECH, Q-INDUSTRY, Q-HORIZON]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0087-080"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-087-080-OPEN-ROTOR-MONITORING-DIAGNOSTICS-AND-CONTROL-INTERFACES
     ATLAS-087 (Open Rotor and Counter-Rotating) · Open Rotor Monitoring, Diagnostics and Control Interfaces
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Open Rotor Monitoring, Diagnostics and Control Interfaces

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-087 Open Rotor](https://img.shields.io/badge/ATLAS--087-Open%20Rotor%20%26%20Counter--Rotating-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-HPC](https://img.shields.io/badge/Q--Division-Q--HPC-blueviolet)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Open Rotor Monitoring, Diagnostics and Control Interfaces`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 ORSCU BITE Architecture

The ORSCU implements a two-tier BITE system:

| BITE Tier | Trigger | Scope | Output |
|---|---|---|---|
| Power-Up BITE (PUBT) | ORSCU power-on / engine start | Self-test of all hardware channels, ARINC 429 buses, pitch sensor loops | GO / NO-GO signal to FADEC |
| Continuous BITE (CBIT) | In-flight, every 100 ms | Monitor all sensor readings, channel crosscheck, AFDX heartbeats | BITE fault codes to AWMS |
| Maintenance BITE (MBIT) | Initiated by GSE or cockpit maintenance page | Extended ORSCU diagnostics; EHPA actuator stroke test; pitch sensor calibration check | Download to GSE via USB-C port |

---

## §3 Sensor Suite

### 3.1 Rotor-Speed Sensors

| Sensor | Location | Technology | Redundancy | Interface |
|---|---|---|---|---|
| FR speed (N_FR-1, N_FR-2) | FR shaft phonic wheel | Magneto-resistive, 60-tooth phonic wheel | Dual (2 per rotor) | ORSCU Ch A + Ch B |
| AR speed (N_AR-1, N_AR-2) | AR shaft phonic wheel | Magneto-resistive | Dual | ORSCU Ch A + Ch B |
| Over-speed shutdown (OSD-FR, OSD-AR) | FR and AR shaft | Independent Hall-effect (1 050 rpm FR / 1 135 AR threshold) | Separate from main speed sensors | Hardwired to FADEC fuel cut |

### 3.2 Blade-Pitch Position Sensors

| Sensor | Type | Qty | Accuracy | Notes |
|---|---|---|---|---|
| BPPS-FR (per blade) | RVDT (Rotary Variable Differential Transformer) | 12 (FR) | ±0.2° | Dual-redundant per blade; transferred via slip-ring |
| BPPS-AR (per blade) | RVDT | 10 (AR) | ±0.2° | As FR |
| Pitch-lock confirm switch | Mechanical microswitch | 22 total | Binary | Indicates pitch-lock pin engagement (ground ops) |

### 3.3 Structural Health Monitoring (SHM) — Blade FBG

| Parameter | Sensor | Sampling Rate | Processing |
|---|---|---|---|
| Blade root bending (flapwise) | FBG × 2 per blade | 2 kHz | ORSCU FBG conditioner; fast Fourier transform for modal ID |
| Blade torsional strain (25 % span) | FBG × 2 per blade | 2 kHz | As above |
| Blade torsional strain (75 % span) | FBG × 2 per blade | 2 kHz | As above |
| Blade tip strain | FBG × 2 per blade | 2 kHz | As above |
| Total FBG channels | 8 per blade × 22 blades | — | 176 channels total |

### 3.4 DPGB Health Sensors

| Sensor | Parameter | Location | Interface |
|---|---|---|---|
| P-OIL | Oil pressure | DPGB main gallery | ORSCU BITE |
| T-OIL-1 | Oil temperature — sump | DPGB sump | ORSCU BITE |
| T-OIL-2 | Oil temperature — cooler outlet | OHX outlet | ORSCU BITE |
| CHD-01 | Chip detector | DPGB magnetic chip plug | AWMS discrete |
| TRQ-FR | FR shaft torque | FR shaft magnetostrictive | ORSCU + FADEC |
| TRQ-AR | AR shaft torque | AR shaft magnetostrictive | ORSCU + FADEC |
| VIB-DPGB | Vibration accelerometer | DPGB housing (3-axis) | ORSCU vibration spectrum |

---

## §4 AFDX Network Topology

The ORSCU interfaces with aircraft avionics systems via AFDX ARINC 664 Part 7 Virtual Links (VLs):

| VL ID | Direction | Connected System | Bandwidth | Content |
|---|---|---|---|---|
| VL-087-01 | ORSCU → FADEC | FADEC — ATA 73 | 2 Mbit/s | Rotor speed reference, pitch demand, power available, mode status |
| VL-087-02 | ORSCU → AWMS | AWMS — ATA 31 | 1 Mbit/s | ORCR BITE faults, blade-off warning, over-speed alert, cautions |
| VL-087-03 | ORSCU → CMS | CMS — ATA 45 | 1 Mbit/s | LRU health data, DPGB trends, pitch-log download |
| VL-087-04 | ORSCU → FDR | FDR — ATA 31 | 0.5 Mbit/s | Selected 50 Hz parameters (N_FR, N_AR, pitch angles, torques) |
| VL-087-05 | ORSCU ↔ FADEC | FADEC — ATA 73 (return) | 1 Mbit/s | LPT shaft speed reference; throttle resolver angle; fuel flow advisory |
| VL-087-06 | ORSCU → EFIS/MFD | Display system — ATA 31 | 0.5 Mbit/s | ORCR synoptic data (rotor speeds, pitch angles, DPGB temps) |

---

## §5 Cockpit Synoptic — ORCR MFD Page

The ORCR propulsor status is displayed on a dedicated MFD synoptic page (ORCR SYNOPTIC), available on both PFDs and the ECAM/EICAS lower display:

| Display Item | Source | Update Rate | Normal / Caution / Warning |
|---|---|---|---|
| FR speed (N_FR) — numeric + analogue | N_FR-1 | 1 Hz | < 950: white; 950–1 049: amber; ≥ 1 050: red |
| AR speed (N_AR) — numeric + analogue | N_AR-1 | 1 Hz | < 1 030: white; 1 030–1 134: amber; ≥ 1 135: red |
| FR blade pitch (mean) | BPPS-FR mean | 2 Hz | Normal range: white |
| AR blade pitch (mean) | BPPS-AR mean | 2 Hz | Normal range: white |
| DPGB oil temp (T-OIL-1) | T-OIL-1 | 1 Hz | < 120: white; 120–129: amber; ≥ 130: red |
| DPGB oil press (P-OIL) | P-OIL | 1 Hz | > 2.0: white; 1.5–2.0: amber; < 1.5: red |
| ORSCU mode | ORSCU mode word | 2 Hz | TAKEOFF/CLIMB/CRUISE: white; DEGRADED: amber; FAIL: red |
| Chip detector status | CHD-01 discrete | 1 Hz | CLEAR: white; CHIP: amber |

---

## §6 Ground Support Interface

| GSE Tool | Interface | Functions |
|---|---|---|
| ORSCU Maintenance Terminal (ORSCU-GSE-1) | USB-C 3.2 Gen 2 (10 Gbit/s) + dedicated test break-out connector | ORSCU software load; MBIT execution; EHPA stroke calibration; BPPS sensor alignment; FBG data download |
| DPGB Diagnostic Kit (DPGB-DK-087) | OBD-style CAN bus adaptor via nacelle service port | Oil pressure/temperature log download; chip detector interrogation; torque sensor calibration verification |

---

## §7 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-087-080-001 | FBG data bandwidth (176 channels × 2 kHz × 16 bit = 5.6 Mbit/s) — confirm AFDX VL allocation and CMS storage capacity | Q-HPC | PDR |
| OI-087-080-002 | ORSCU BITE latency for blade-off detection (< 1 s requirement) — verify via hardware-in-the-loop (HIL) test | Q-HPC | CDR |
| OI-087-080-003 | Slip-ring reliability for BPPS RVDT signals (22 channels) — MTBUR target 8 000 FH | Q-INDUSTRY | CDR |
