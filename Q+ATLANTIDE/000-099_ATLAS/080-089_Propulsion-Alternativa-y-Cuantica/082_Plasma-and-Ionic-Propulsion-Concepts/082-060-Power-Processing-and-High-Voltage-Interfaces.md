---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-082-060-POWER-PROCESSING-AND-HIGH-VOLTAGE-INTERFACES"
register: ATLAS-1000
title: "Power Processing and High-Voltage Interfaces"
ata: "ATLAS-082 (Plasma and Ionic Propulsion Concepts)"
sns: "082-060-00"
subsection: "082"
subsubject_code: "060"
primary_q_division: Q-INDUSTRY
support_q_divisions: [Q-GREENTECH, Q-HPC, Q-STRUCTURES]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0082-060"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-082-060-POWER-PROCESSING-AND-HIGH-VOLTAGE-INTERFACES
     ATLAS-082 (Plasma and Ionic Propulsion Concepts) · Power Processing and High-Voltage Interfaces
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Power Processing and High-Voltage Interfaces

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-082 Plasma & Ionic](https://img.shields.io/badge/ATLAS--082-Plasma%20%26%20Ionic%20Propulsion-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-INDUSTRY](https://img.shields.io/badge/Q--Division-Q--INDUSTRY-grey)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

ATLAS subsubject 082-060 defines the Plasma Propulsion Power Processing Unit (PPPU) architecture, its HVDC 270 V input interface, high-voltage output circuits (up to 2 000 V DC) for HET and GIE thrusters, EMC zoning and filtering, HV personnel safety provisions, and the electrical interfaces between the PPPU and the aircraft power distribution system (ATLAS 073).

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA reference | ATLAS-082 — 082-060 Power Processing and High-Voltage Interfaces |
| Certification basis | EASA CS-25 Amdt 27+; DO-160G Section 16 (power input); DO-160G Section 21 (RF emissions); IEC 60950-1 (HV safety) |
| S1000D SNS | 082-060-00 |

---

## §3 PPPU Architecture

### 3.1 Overview

The Plasma Propulsion Power Processing Unit (PPPU) is a dual-channel LRU (4-MCU form factor, 6.4 kg) housed in the aft avionics bay. It accepts HVDC 270 V input from the aircraft power distribution network (ATLAS 073) and produces the regulated high-voltage outputs required by each thruster type:

| Output Rail | Voltage | Current Range | Load |
|---|---|---|---|
| HET Discharge (×4) | 200–400 V DC regulated | 5–20 A per channel | HET anode (discharge) |
| HET Magnetic (×4) | 12–24 V DC | 1–3 A per channel | HET magnetic coils |
| HET Heater (×4) | 12 V DC | 2 A per channel | Hollow cathode heater |
| HET Keeper (×4) | 15–25 V DC | 0.5–1 A per channel | Hollow cathode keeper |
| GIE Screen (×4) | +800 to +2 000 V DC regulated | 0.5–3 A per channel | GIE screen grid |
| GIE Accel (×4) | −100 to −300 V DC regulated | 0.1–0.5 A per channel | GIE accel grid |
| GIE Heater (×4) | 12 V DC | 2 A per channel | GIE cathode heater |
| GIE Keeper (×4) | 15–25 V DC | 0.5 A per channel | GIE cathode keeper |
| DBD Actuator HV (×8 zones) | 2–15 kV AC (sinusoidal) | 100–500 mA per zone | DBD plasma actuators |

### 3.2 Power Conversion Topology

**Stage 1 — Input Filter and Pre-Boost:**
- EMC input filter (common-mode + differential-mode, 40 dB attenuation at 150 kHz)
- Inrush limiting NTC thermistor + bypass relay
- Active PFC-equivalent current shaping for HVDC 270 V load

**Stage 2 — Isolated DC-DC Conversion:**
- Resonant LLC converter (100 kHz switching frequency) for galvanic isolation
- Primary: HVDC 270 V; Transformer turns ratio selected per output rail
- Isolation voltage: 3 000 V DC (tested 60 s, per IEC 60950-1)
- Efficiency η ≥ 93 % at full load

**Stage 3 — Output Regulation:**
- Post-regulation buck/boost stage per HV output rail
- Digital control loop (PPPU FPGA + DSP): PI current-mode control for discharge current regulation
- Current ramp rate: 0 → full load in ≤ 2 s (soft-start)
- Over-current protection: hardware latch, ≤ 10 µs response, OC threshold 110 % of nominal

**Stage 4 — DBD High-Voltage AC Generator:**
- Resonant inverter (Class-E topology) producing sinusoidal HV AC at 5–30 kHz
- Output voltage: 2–15 kV (adjustable by frequency/duty modulation)
- Output impedance: ≤ 5 Ω at operating frequency (matched to DBD capacitive load)
- Per-zone current monitoring for fault isolation

---

## §4 HVDC 270 V Input Interface

| Parameter | Specification |
|---|---|
| Nominal input voltage | 270 V DC ± 10 % (243–297 V) |
| Maximum input current | 56 A (at 15 kW, η = 0.93) |
| Transient input voltage range | 200–350 V (per DO-160G Section 16 Category B) |
| Input SSPC rating | 60 A (ATLAS 073 PDCU channel) |
| Inrush current limit | ≤ 200 A peak for ≤ 10 ms |
| EMC filter input attenuation | ≥ 40 dB, 150 kHz–30 MHz (DO-160G Section 21) |
| Input circuit protection | PPPU internal 70 A HRC fuse + SSPC interlock |
| Ground bonding | 10 mm² Cu braid; bonding resistance ≤ 0.1 Ω |

---

## §5 HV Output Circuit Design

### 5.1 HV Cable and Connector Specification

| Parameter | Value |
|---|---|
| HV cable rating | 3 000 V DC, 200 °C silicone insulated |
| HV connector type | Lemo HV series or equivalent (2 500 V DC rated) |
| Minimum bend radius | 50 mm |
| Cable OD | 6 mm (screened; Al braid screen earthed at PPPU end only) |
| Screen termination | PPPU chassis ground; not connected at thruster end (single-point) |
| Conduit | PTFE-lined Al conduit; ≥ 50 mm separation from signal cables |
| HiPot test voltage (installed) | 2 500 V DC, 1 min; leakage ≤ 1 mA pass criterion |

### 5.2 HV Isolation Module (HVIM)

Each thruster is equipped with an HV Isolation Module (HVIM) located at the PPPU output terminal. The HVIM provides:

| Function | Specification |
|---|---|
| Galvanic isolation | 3 000 V DC; double insulation |
| Normally open / normally closed | Normally open (deenergised = HV disconnected) |
| Switching time | ≤ 5 ms open → close; ≤ 2 ms close → open (arc quench) |
| Arc quench mechanism | SF₆-free vacuum interrupter (halogen-free) |
| HVIM command | PPPU digital output (24 V logic); interlock from PPPU safety monitor |
| Leakage current (open state) | ≤ 100 µA at 2 000 V |

### 5.3 HV Personnel Safety Provisions

| Safety Feature | Implementation |
|---|---|
| HV indicator lamp | Amber LED at each HVIM panel; ON = HV active |
| HV dead-indicator | PPPU panel indicator PROP PLASMA HV OFF confirms HV rails discharged; bleed resistors discharge HV rails to < 50 V within 30 s of shutdown |
| Access interlock | Avionics bay door microswitch wired to PPPU HV inhibit input; HV inhibited when door open |
| LOTO provision | PPPU HV master switch with padlock provision; lockout state verified by BITE |
| Warning label | ISO 3864-2 Class B HV warning (triangle + lightning bolt) at every HV access point |

---

## §6 EMC Architecture

| EMC Requirement | Compliance Method |
|---|---|
| DO-160G Section 21 (Radiated RF emission) | PPPU metallic enclosure (6 dB attenuation; additional shield tiles where needed); HV cable screening |
| DO-160G Section 17 (Spike) | TVS diodes on all PPPU signal I/O; MOV on HVDC 270 V input |
| DO-160G Section 18 (Audio frequency conducted) | Input EMC filter (40 dB, 150 kHz) on HVDC 270 V rail |
| DO-160G Section 20 (RF susceptibility) | PPPU screened enclosure; FPGA firmware watchdog and self-recovery within 50 ms |
| DBD kV AC RF emissions | DBD HV AC cables screened, routed < 100 mm from airframe skin; HV AC frequency kept within ISM band (13.56 MHz or 27.12 MHz) |

---

## §7 PPPU Physical and Electrical Characteristics

| Parameter | Value |
|---|---|
| Form factor | 4-MCU (standard avionics rack) |
| Dimensions (H × W × D) | 197 mm × 482 mm × 380 mm |
| Mass | ≤ 6.4 kg |
| Cooling | Forced air (rack fan); PPPU heatsink to rack backplane: ≤ 150 W dissipation |
| Input connector | Amphenol MIL-DTL-38999 Series III, HVDC 270 V rail; 3 positions |
| Signal/data connector | Amphenol MIL-DTL-38999 AFDX + discrete I/O; 55 positions |
| BITE self-test coverage | ≥ 95 % of failure modes |
| Software | DO-178C DAL C (research phase) |
| FPGA | DO-254 DAL C (research phase) |

---

## §8 Interfaces

| Interface | Connected System | Protocol | Data |
|---|---|---|---|
| Primary power input | HVDC 270 V bus (ATLAS 073) | HVDC cable | Up to 15 kW |
| Thruster power output (HET×4) | HET discharge circuits | HV coaxial cable (3 kV) | Regulated discharge V, I per thruster |
| Thruster power output (GIE×4) | GIE screen/accel circuits | HV coaxial cable (3 kV) | Screen + accel V, beam current |
| DBD HV AC output (×8 zones) | DBD plasma actuators | HV AC cable (15 kV) | Sinusoidal HV AC, zone power |
| Propellant control | XMFC ×8 | CAN bus (12 V) | Flow demand, actuals |
| Maintenance / BITE | CMS — ATA 45 | AFDX VL-082-01 | PPPU faults, HV rail status, power telemetry |
| Research data | EPMS | AFDX VL-082-02 | Full PPPU electrical telemetry at 10 Hz |
| Thermal monitoring | TMS — ATLAS 074 | AFDX VL-082-04 | PPPU heatsink temperature |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-082-060-001 | PPPU cooling: forced-air fan qualification for vibration environment — check against DO-160G Section 8 (vibration) | Q-INDUSTRY | CDR |
| OI-082-060-002 | GIE screen HV supply stability vs. beam plasma instabilities (ionisation wave coupling) — model and test | Q-HPC | CDR |
| OI-082-060-003 | DBD HV AC cable routing plan vs. TCAS antenna proximity — EMC analysis | Q-INDUSTRY | PDR |
