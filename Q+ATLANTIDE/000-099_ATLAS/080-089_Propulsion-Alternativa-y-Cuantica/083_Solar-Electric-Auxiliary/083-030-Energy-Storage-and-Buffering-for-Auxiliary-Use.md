---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-083-030-ENERGY-STORAGE-AND-BUFFERING-FOR-AUXILIARY-USE"
register: ATLAS-1000
title: "Energy Storage and Buffering for Auxiliary Use"
ata: "ATLAS-083 (Solar-Electric Auxiliary)"
sns: "083-030-00"
subsection: "083"
subsubject_code: "030"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-INDUSTRY, Q-HPC, Q-STRUCTURES]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0083-030"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-083-030-ENERGY-STORAGE-AND-BUFFERING-FOR-AUXILIARY-USE
     ATLAS-083 (Solar-Electric Auxiliary) · Energy Storage and Buffering
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Energy Storage and Buffering for Auxiliary Use

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-083 Solar-Electric](https://img.shields.io/badge/ATLAS--083-Solar--Electric%20Auxiliary-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-teal)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

ATLAS subsubject 083-030 defines the dual-tier energy storage subsystem of the Solar-Electric Auxiliary (SEA) system: a supercapacitor (SCAP) bank for fast transient power buffering, and a Li-Ion battery auxiliary subset for sustained energy backup. It covers design parameters, energy management strategy, state-of-energy (SoE) tracking, charging/discharging arbitration, thermal management, safety constraints, and maintenance requirements.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA reference | ATLAS-083 — 083-030 Energy Storage and Buffering |
| Certification basis | EASA CS-25 Amdt 27+ (research ref.); IEC 62619 (Li-Ion safety); DO-160G Section 16 (power input/output) |
| S1000D SNS | 083-030-00 |

---

## §3 Tier 1 — Supercapacitor Bank (SCAP)

### 3.1 Design Parameters

| Parameter | Value | Notes |
|---|---|---|
| Total energy | 100 kJ | At 700 V, usable between 350–700 V (75 % energy range) |
| Capacitance | 400 F | At 700 V nominal |
| Operating voltage | 350–700 V DC | Usable range |
| Peak discharge power | 200 kW | For ≤ 0.5 s transient |
| Peak charge power | 200 kW | Regenerative capture from propulsors in motoring mode |
| Cycle life | > 1 000 000 cycles | No significant degradation; Maxwell SHB-1500 cell stack (or equivalent) |
| Operating temperature range | −40 °C to +65 °C | Within SEACU bay thermal envelope |
| Mass | 28 kg (estimated) | Including bus bar, housing, bleeder resistor |
| Volume | 18 L | Under-floor centre equipment bay |
| ESR (equivalent series resistance) | < 0.5 mΩ | At 1 kHz; check interval 2 500 h |

### 3.2 SCAP Cell Stack Configuration

- **Cell count:** 280 cells in series (2.5 V/cell × 280 = 700 V)
- **Cell capacitance:** 3 000 F per cell (Maxwell BCAP3000 P270 or equivalent)
- **Module arrangement:** 4 modules × 70 cells; each module has a balancing circuit (passive bleed resistor per cell, Δ < 50 mV between cells)
- **Safety features:** Manual service disconnect (MSD) rated 700 V / 500 A; electronic contactor (normally open); bleeder resistor (700 V → < 50 V in ≤ 60 s via 10 Ω bleed resistor); cell voltage monitoring (1 Hz, all 280 cells, SEACU BMS channel)
- **Housing:** Aluminium alloy box, IP55, vibration-isolated on 4× elastomeric mounts per DO-160G Section 8

### 3.3 SCAP Energy Management

The SCAP is the **primary fast transient buffer** for all SEA power events:

- **Propulsor start (inrush):** 50–200 kW for 0.2–0.5 s — discharged from SCAP; prevents voltage sag on HVDC 270 V bus
- **Propulsor speed transient:** ±30 kW for ≤ 1 s — SCAP absorbs/supplies; MPPT converters too slow to respond within 1 s
- **Regenerative capture (descent):** Propulsors generate up to 30 kW in motoring; SCAP absorbs first (if SoE < 90 %); excess to battery
- **SCAP target SoE:** Maintained at 70–90 % during cruise for maximum buffering headroom

---

## §4 Tier 2 — Li-Ion Auxiliary Battery Subset

### 4.1 Design Parameters

| Parameter | Value | Notes |
|---|---|---|
| Usable capacity | 50 kWh | NMC 811 chemistry; SoC 20–90 % operating window |
| Nominal voltage | 680 V DC | ~520 V at SoC 20 % min; ~740 V at SoC 90 % max |
| Continuous discharge power | 40 kW | Emergency backup (Role B) |
| Peak discharge power | 80 kW | Short burst ≤ 10 s (bus stabilisation) |
| Continuous charge power | 40 kW | From solar PV surplus |
| C-rate (continuous) | 0.8 C | NMC 811 optimum; extends cycle life |
| Cycle life | 2 000 cycles (80 % DoD) | 10-year programme life at 1 cycle/flight |
| Operating temperature | +10 °C to +45 °C (charging); −20 °C to +55 °C (discharge) | BMS enforces limits |
| Mass | 210 kg (estimated) | Including BMS electronics, housing, cooling plate |
| Volume | 140 L | Aft equipment bay |
| Thermal management | Liquid cooling — EGW loop from ATLAS 074 (battery dedicated loop) | Coolant flow 4 L/min |
| Fire suppression | Novec 1230 total flooding (1.5 kg discharge per zone) | Triggered by BMS over-temperature or smoke detector |

### 4.2 Battery Management System (BMS) — SEA Channel

The SEA 50 kWh subset uses a **dedicated BMS channel** within the ATLAS 072 main BMS (dual-lane EKF SoC estimator):

- **SoC estimation:** Extended Kalman Filter (EKF) at 1 Hz; cell voltage + current + temperature inputs; accuracy ±2 % SoC
- **SoH estimation:** Coulomb counting + incremental capacity analysis; updated every 10 cycles
- **Alarm thresholds:**
  - L1 Advisory: SoC < 30 % or SoC > 88 % or cell Tj > 45 °C
  - L2 Caution: SoC < 22 % or cell Tj > 55 °C
  - L3 Warning: cell Tj > 65 °C or cell voltage > 4.25 V or < 2.80 V → disconnect
  - L4 Emergency: smoke or Tj > 80 °C → BMS relay opens; Novec 1230 discharged

### 4.3 Charging Strategy

| Source | Condition | Max Charge Power | Priority |
|---|---|---|---|
| PV solar (surplus after BLI propulsor demand) | Daytime cruise, SCAP SoE > 90 % | 40 kW | 1st |
| HVDC 270 V main bus | SCAP SoE > 90 %; battery SoC < 85 % | 30 kW | 2nd |
| Ground charging (GSE) | Pre-flight; aircraft on ground | 50 kW (DC fast) | Ground only |

---

## §5 Energy Arbitration Strategy

The SEACU implements the following priority cascade for power dispatch:

1. **PV harvest → BLI propulsors** (direct conversion, highest efficiency, no storage losses)
2. **PV harvest → SCAP** (top up SCAP if SoE < 70 %)
3. **PV harvest → HVDC 270 V bus** (export surplus)
4. **SCAP → BLI propulsors** (transient support; MPPT cannot respond fast enough)
5. **Battery → BLI propulsors** (sustained supply during cloud/night; SoC > 22 %)
6. **Battery → HVDC 270 V bus** (emergency backup Role B; avionics priority)

---

## §6 State-of-Energy (SoE) Tracking

| Parameter | Update Rate | Accuracy | Output |
|---|---|---|---|
| SCAP voltage (all 280 cells) | 1 Hz | ±10 mV | SEACU BITE; CMS ATA 45 |
| SCAP SoE (%) | 1 Hz | ±1 % | AFDX VL-083-01 to CMS |
| Battery SoC (%) | 1 Hz | ±2 % | AFDX VL-083-01 to CMS; VL-083-02 to EMS |
| Battery SoH (%) | Every 10 cycles | ±3 % | Maintenance report |
| Remaining backup duration | Computed (1 Hz) | ±2 min | AFDX VL-083-02; ECAM advisory |

---

## §7 Safety Constraints

| Constraint | Requirement | Source |
|---|---|---|
| SCAP pre-access discharge | Voltage < 50 V confirmed (SEACU SCAP DISCHARGED indicator); ≥ 60 s after SEACU shutdown | BREX-083-v1 / IEC 62109-1 |
| Battery LOTO | BMS relay open + manual MSD engaged before any connector removal | BREX-083-v1 / CS-25.981 |
| Battery over-temperature isolation | Disconnect within 200 ms at Tj > 80 °C | IEC 62619 |
| SCAP over-voltage protection | Electronic crowbar at 730 V; passive bleeder continues to 700 V | IEC 62109-1 |
| Thermal runaway suppression | Novec 1230 auto-discharge on L4 trigger | CS-25 analogous / operator agreement |

---

## §8 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-083-030-001 | SCAP DO-160G Section 8 (vibration) qualification test — rig design and schedule | Q-INDUSTRY | PDR |
| OI-083-030-002 | Battery EKF SoC estimator accuracy at low temperature (−20 °C) validation | Q-HPC | CDR |
| OI-083-030-003 | SCAP bleeder resistor thermal dissipation management in confined equipment bay | Q-STRUCTURES | PDR |
| OI-083-030-004 | Novec 1230 regulatory path under EASA STC for under-floor battery zone | Q-GREENTECH | Phase 2 |
