---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-084-080-BEYOND-GEN-2-MONITORING-DIAGNOSTICS-AND-CONTROL-INTERFACES"
register: ATLAS-1000
title: "Beyond-Gen-2 Monitoring Diagnostics and Control Interfaces"
ata: "ATLAS-084 (Hybrid Architectures — Beyond Gen-2)"
sns: "084-080-00"
subsection: "084"
subsubject_code: "080"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HPC, Q-INDUSTRY, Q-HORIZON]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0084-080"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-084-080-BEYOND-GEN-2-MONITORING-DIAGNOSTICS-AND-CONTROL-INTERFACES
     ATLAS-084 (Hybrid Architectures — Beyond Gen-2) · Monitoring Diagnostics and Control Interfaces
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Beyond-Gen-2 Monitoring Diagnostics and Control Interfaces

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-084 Hybrid Beyond Gen-2](https://img.shields.io/badge/ATLAS--084-Hybrid%20Beyond%20Gen--2-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-teal)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

ATLAS subsubject 084-080 defines the BGSCU Built-In Test (BITE) architecture, the CMS (ATA 45) maintenance interface, the EPMS research monitoring interface, the cockpit BGHA synoptic display, and the ground support equipment (GSE) interface for the BGHA. It establishes all monitoring and diagnostic data products, their rates, formats, and routing.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA Reference | ATLAS-084 — 084-080 Beyond-Gen-2 Monitoring Diagnostics and Control Interfaces |
| Certification Basis | EASA CS-25 Amdt 27+; DO-178C DAL B (BGSCU BITE); ATA iSpec 2200 (CMS) |
| S1000D SNS | 084-080-00 |

---

## §3 BITE Architecture

The BGSCU BITE system operates in Partition P5 (DAL C) and performs continuous background monitoring of the following:

**Source health monitoring (per source, 100 ms cycle):**
- SSBP Pack A/B: Cell voltage min/max; pack temperature; BMS fault register; SoC; contactor state; BDCC status
- FCSS: Stack voltage; stack current; H₂ manifold pressure; stack outlet temperature; FCCU fault register; BDCC-C status
- VCGT-1/2: ATRU output voltage/current; VCGT FADEC health word; shaft speed; fuel flow actual
- SCEB: Terminal voltage; SoC; ESR estimate; BDCC-D status; temperature

**Bus-800 health monitoring (50 ms cycle):**
- Bus-800 voltage (per segment S1–S4)
- Total bus current (summed)
- Segment BTB position (open/closed)
- IMU insulation resistance (Bus-800 to ground)

**BGSCU internal BITE (10 ms cycle):**
- Lane A/B processor watchdog
- ARINC 653 partition health (timeout flags)
- QPU coherence error rate; QPU temperature; dilution refrigerator pressure
- AFDX VL health (frame counter; latency; CRC errors)
- CAN bus error counters (all nodes)

**BITE fault classification:**
| Level | Colour | Description | Response |
|---|---|---|---|
| Level 1 — Advisory | Blue | Non-critical monitoring alert | CMS log; crew info |
| Level 2 — Caution | Amber | Degraded performance; dispatch with MEL | CMS fault; BGHA MFD amber bar |
| Level 3 — Warning | Red | Imminent source isolation required | CMS fault + ECAM; BGSCU auto-reconfigures |
| Level 4 — Emergency | Red flashing | Safety-critical; immediate action required | ECAM BGHA EMERGENCY; DM entered; crew procedure |

---

## §4 CMS Interface (ATA 45)

The BGSCU publishes BITE data to the CMS (ATA 45) on AFDX VL-084-02 at 500 ms cycle. The CMS stores faults in the Aircraft Fault Memory (AFM) and provides maintenance staff with downloadable fault reports via ACARS or ground GSE.

**Fault code table (selected):**

| Fault Code | Description | Level | Component | Maintenance Action |
|---|---|---|---|---|
| FC-084-SSBP-A-01 | SSBP Pack A BMS over-temperature | 3 — Warning | SSBP Pack A | Inspect pack cooling; check BMS sensor calibration |
| FC-084-SSBP-B-01 | SSBP Pack B contactor open fail | 2 — Caution | SSBP Pack B | BDCC-B / contactor inspection; MEL-084-SSBP-B |
| FC-084-FCSS-01 | FCSS stack voltage drop > 10 % | 2 — Caution | FCSS | Stack polarisation curve check; MEL-084-FCSS |
| FC-084-FCSS-H2-01 | H₂ sensor ATEX zone alarm | 4 — Emergency | FCSS/H₂ manifold | H₂ emergency procedure; FCSS isolation; land ASAP |
| FC-084-VCGT1-01 | VCGT-1 ATRU over-temperature | 2 — Caution | ATRU-1 | ATRU inspection at next maintenance stop |
| FC-084-VCGT2-01 | VCGT-2 shaft speed sensor fail | 2 — Caution | VCGT-2 speed sensor | Speed sensor replacement |
| FC-084-SCEB-01 | SCEB ESR > 2× baseline | 2 — Caution | SCEB | SCEB capacitance check; MEL-084-SCEB |
| FC-084-QPU-01 | BGSCU QPU latency > 25 ms | 1 — Advisory | QPU module | Classical fallback active; QPU maintenance at base |
| FC-084-BUS-IMU-01 | Bus-800 insulation resistance < 100 kΩ | 3 — Warning | Bus-800 segment | Fault location via IMU; isolation before maintenance |
| FC-084-BGSCU-LB-01 | BGSCU Lane B health fault | 2 — Caution | BGSCU Lane B | Lane B replacement; 3-day MEL |

---

## §5 EPMS Research Interface

The Experimental Propulsion Monitoring System (EPMS) receives a full 50 Hz BGHA state vector on AFDX VL-084-03. This interface is not used for flight operations and is classified DAL D (research only).

**EPMS data stream (50 Hz, 2 kHz data internally, decimated to 50 Hz for AFDX):**
- SSBP A/B: All cell voltages (2 800 cells per pack); pack current; pack temperature histogram
- FCSS: Stack current/voltage (per stack, 8 stacks); H₂ flow actual; air stoichiometry; EIS spectrum (swept at 1 Hz)
- VCGT: Shaft power actual; ATRU output current/voltage; exhaust temperature; fuel flow
- SCEB: Terminal voltage; current; ESR estimate at 1 Hz
- Bus-800: All segment voltages/currents; BTB states; IMU resistance
- BGSCU: QPU dispatch vector (P_SSBP, P_FCSS, P_VCGT1, P_VCGT2, P_SCEB); MPC cost function value; QPU error rate; mode state
- BGHA-TML: Coolant inlet/outlet temperature; flow rate; RAHX effectiveness estimate

EPMS data is stored to the Aircraft Data Recording Unit (ADRU) in 10 min block files, downloaded post-flight to the Q+ATLANTIDE ground analysis platform.

---

## §6 Cockpit Displays

**BGHA Synoptic page (MFD page BG-1):**

The BGHA Synoptic is accessed via MFD System Page > BGHA. It displays:
- **Source bars (top row):** SSBP-A, SSBP-B (kWh remaining; SoC%), FCSS (kW actual / 400 kW max), VCGT-1, VCGT-2 (kW actual), SCEB (kWh remaining; SoC%). Bars are green (normal), amber (caution), red (warning/fault).
- **Bus-800 power flow diagram:** Animated flow from each active source to the bus and to PMSM fans. Source contribution shown as kW and percentage.
- **Mode indicator:** Active BGHA mode (M1–M7) displayed prominently with DM number if in M7.
- **QPU status:** "QAOA ACTIVE" (green) or "CLASSICAL FALLBACK" (amber).
- **Energy totals:** Cumulative energy from each source since last power-on (kWh); H₂ mass consumed (kg).

**Crew alerting (ECAM):**
- Level 3/4 faults generate ECAM master WARNING/CAUTION with BGHA fault title and associated crew procedure.
- Level 1/2 faults appear as STATUS messages only.

---

## §7 Ground Support Interface

The BGSCU-GSE-1 connector (USB-C 3.2 Gen 2 × 2, 20 Gbps) is located on the forward avionics bay E&E access panel. It provides:

| Function | Tool Required | Notes |
|---|---|---|
| BGSCU software load | BGSCU Loader v3.x (laptop + USB-C) | Requires BGSCU in maintenance mode; DO-178C DAL B controlled load |
| BITE fault report download | BGSCU Diagnostic Software (BDS) v2.x | Exports XML fault log; printable maintenance record |
| BDCC calibration | BDS with BDCC calibration plugin | Zero-current offset; gain cal; thermal model coefficient update |
| QPU calibration / reset | QPU Calibration Tool (QCT) | Requires QPU cryo warm-up; 45 min procedure; once per 1 000 h |
| SSBP conditioning | BDS SSBP Conditioning mode | Capacity test (C/5 rate); SoH update |
| SCEB capacitance test | BDS SCEB module | Full charge/discharge cycle; ESR measurement; SoC recalibration |
| Bus-800 HiPot test | External HiPot tester + GSE HV probe | 1 500 V DC; BGSCU must be in STANDBY; all BDCCs disconnected |

---

## §8 Interfaces

| Interface | Connected System | Protocol | Data |
|---|---|---|---|
| BITE output | CMS — ATA 45 | AFDX VL-084-02 | Fault codes; LRU health; 500 ms cycle |
| Research telemetry | EPMS | AFDX VL-084-03 | Full state vector; 50 Hz; 2 kHz decimated |
| Cockpit synoptic | MFD (BG-1 page) | AFDX (via DU) | Source bars; mode; QPU status; energy totals |
| ECAM alerts | ECAM processor | Discrete hardwired + AFDX | Level 3/4 fault alerts |
| GSE interface | BGSCU-GSE-1 | USB-C 3.2 | Software load; diagnostics; calibration |
| Data download | ADRU (ATA 31) | ARINC 717 derived | EPMS block file archival |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-084-080-001 | EPMS 50 Hz AFDX VL bandwidth — confirm 664 P7 VLAN allocation sufficient | Q-INDUSTRY | PDR |
| OI-084-080-002 | QPU calibration procedure (QCT) — 45 min outage impact on aircraft utilisation | Q-HPC | CDR |
| OI-084-080-003 | BGHA Synoptic MFD page layout — HMI review with EASA AMC 25.1322 | Q-GREENTECH | PDR |
| OI-084-080-004 | FC-084-FCSS-H2-01 emergency procedure crew workload assessment | Q-HORIZON | CDR |
| OI-084-080-005 | ADRU block file format — compatibility with Q+ATLANTIDE ground analysis platform | Q-HPC | PDR |
