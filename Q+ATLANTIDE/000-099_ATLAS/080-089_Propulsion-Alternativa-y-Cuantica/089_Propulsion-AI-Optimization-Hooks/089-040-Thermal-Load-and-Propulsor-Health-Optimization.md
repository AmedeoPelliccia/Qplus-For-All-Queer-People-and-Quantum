---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-089-040-THERMAL-LOAD-AND-PROPULSOR-HEALTH-OPTIMIZATION"
register: ATLAS-1000
title: "Thermal Load and Propulsor Health Optimization"
ata: "ATLAS-089 (Propulsion AI Optimization Hooks)"
sns: "089-040-00"
subsection: "089"
subsubject_code: "040"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-HPC, Q-GREENTECH, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0089-040"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-089-040-THERMAL-LOAD-AND-PROPULSOR-HEALTH-OPTIMIZATION
     ATLAS-089 (Propulsion AI Optimization Hooks) · Thermal Load and Propulsor Health Optimization
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Thermal Load and Propulsor Health Optimization

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-089 AI Optimization](https://img.shields.io/badge/ATLAS--089-Propulsion%20AI%20Optimization%20Hooks-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-STRUCTURES](https://img.shields.io/badge/Q--Division-Q--STRUCTURES-orange)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

ATLAS subsubject 089-040 defines the Thermal Load Balancer (TLB) and the Propulsor Health Optimization (PHO) algorithms embedded in the AIOCU. It covers the AI thermal model architecture, the sensor integration from the ATLAS-080 quantum sensing network, the load redistribution strategy for preventing thermal exceedances across the DEP/BLI motor set, and the health-state estimation models for predictive propulsor maintenance optimization.

---

## §2 Thermal Sensor Integration

The TLB ingests thermal data from the ATLAS-080 quantum sensing network (46 nodes) and supplementary conventional thermometry:

| Sensor Group | Sensor Type | Qty | Location | Interface | Update Rate |
|---|---|---|---|---|---|
| DEP motor winding (P1–P4) | NV-center diamond magnetothermometry | 4 | Per DEP motor stator | ATLAS-080 QSPU → AIOCU | 10 Hz |
| BLI motor winding (port, stbd) | NV-center sensors | 2 | BLI motor stators | ATLAS-080 QSPU | 10 Hz |
| DEP power electronics (P1–P4) | Josephson junction thermometer (JJT) | 4 | IGBT heat sinks | ATLAS-080 QSPU | 10 Hz |
| ORCR DPGB oil | RTD (Pt100) | 2 | DPGB sump + OHX outlet | ORSCU → AIOCU AFDX | 1 Hz |
| PEMFC stack temperature | Thermocouple K-type | 8 | Per PEMFC stack (4 stacks × 2) | FCCU → EMS → AIOCU | 2 Hz |
| Battery module temperature | NTC thermistor (BMS) | 16 | Battery module array | EMS EMCU → AIOCU | 5 Hz |
| Ambient OAT | TAT probe | 1 | Nose fuselage | ADC → AIOCU | 1 Hz |

---

## §3 Thermal Load Balancer (TLB) Architecture

### 3.1 DNN Thermal Model

The TLB uses a **Deep Neural Network (DNN) thermal surrogate model** trained on physics-based finite-element thermal models of the DEP motors and power electronics, calibrated with test rig data:

| Attribute | Value |
|---|---|
| Architecture | 3-layer FC network (20 input → 128 → 64 → 6 output) |
| Inputs | 20 thermal states + ambient OAT + power levels |
| Outputs | 6 predicted thermal margins (4 × DEP, 2 × BLI) in °C above limit |
| Quantization | INT8 FPGA deployment |
| Inference latency | < 1 ms |

### 3.2 Load Redistribution Algorithm

When the TLB predicts any motor thermal margin < 20 °C (pre-warning threshold), it initiates load redistribution:

```mermaid
flowchart TD
    TEMP[Thermal State\n& Margin Prediction] --> CHK{Any margin\n< 20 °C?}
    CHK -- No --> NOM[Nominal dispatch\nno change]
    CHK -- Yes --> ID[Identify\nhottest propulsor]
    ID --> SHED[Compute load shed\nΔP to restore 25 °C margin]
    SHED --> COMP[Compensate on\ncoolest propulsor(s)]
    COMP --> SBM[Verify vs.\nSBM thrust floor]
    SBM --> CMD[Issue adjusted\npower commands]
```

Thermal limits enforced by the TLB (all hard limits also enforced independently by SBM):

| Component | Warning Threshold | Hard Limit (SBM) |
|---|---|---|
| DEP motor winding | T_winding ≥ 155 °C | T_winding ≥ 180 °C |
| DEP IGBT junction | T_junction ≥ 145 °C | T_junction ≥ 175 °C |
| BLI motor winding | T_winding ≥ 145 °C | T_winding ≥ 170 °C |
| PEMFC stack | T_stack ≥ 75 °C | T_stack ≥ 85 °C |
| Battery module | T_module ≥ 45 °C | T_module ≥ 55 °C |
| DPGB oil (ORCR) | T_oil ≥ 120 °C | T_oil ≥ 130 °C |

---

## §4 Propulsor Health Optimization (PHO)

### 4.1 Health State Estimation

The PHO module estimates the **State of Health (SoH)** of each propulsor unit using a recursive Bayesian filter fusing multiple degradation indicators:

| Indicator | Source | Model | Update Rate |
|---|---|---|---|
| DEP motor insulation resistance trend | BMS → EMS EMCU | Exponential degradation fit | Per flight cycle |
| DEP motor vibration signature | ATLAS-080 SQUID magnetometers | FFT modal tracking | 40 Hz |
| BLI fan bearing vibration | ATLAS-080 optomechanical sensors | Envelope analysis | 40 Hz |
| ORCR blade pitch actuator position error | ORSCU RVDT | Kalman filter drift estimate | 10 Hz |
| PEMFC stack impedance | FCCU EIS measurement | RC equivalent circuit fit | Per flight cycle |
| Battery cell impedance growth | BMS EIS | Calendar aging model | Per flight cycle |

### 4.2 Remaining Useful Life (RUL) Estimation

The PHO module maintains a RUL estimate for each propulsor LRU, updated after each flight:

| LRU | Degradation Model | RUL Metric | Maintenance Alert Threshold |
|---|---|---|---|
| DEP P1–P4 motors | Arrhenius thermal aging + vibration fatigue | Flight hours to winding failure | RUL < 500 FH |
| BLI fans (port, stbd) | Bearing fatigue + erosion model | Flight hours to bearing replacement | RUL < 300 FH |
| PEMFC stacks | Voltage degradation (µV/h) | Hours to end-of-life voltage | RUL < 200 h |
| Battery modules | Capacity fade + impedance rise | Charge cycles to 80 % capacity | RUL < 100 cycles |

### 4.3 Maintenance Optimization

The PHO module interfaces with the CMS (ATA 45) to recommend optimized maintenance scheduling that minimizes ground time while respecting airworthiness limits:

- **Condition-Based Maintenance (CBM) recommendations:** Generated when any LRU RUL drops below alert threshold; communicated to CMS via AFDX VL-089-04.
- **Thermal aging credit:** If historical thermal data shows a propulsor has operated below nominal temperatures for ≥ 500 FH, the PHO may recommend an extended inspection interval (subject to approved CBM programme).

---

## §5 Performance Budgets

| Parameter | Requirement | Target Value | Status |
|---|---|---|---|
| TLB thermal limit exceedance prevention | 0 exceedances per mission | 0 (by design) | TBD |
| TLB load redistribution time | ≤ 500 ms from prediction to command | < 100 ms | TBD |
| PHO RUL estimation accuracy (DEP motors) | ±15 % of true RUL | ±10 % (target) | TBD |
| PHO false maintenance alert rate | ≤ 0.5 alerts per 1 000 FH | < 0.2 per 1 000 FH | TBD |

---

## §6 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-089-040-001 | DEP motor winding NV-center sensor installation — vibration isolation qualification for flight environment | Q-STRUCTURES | CDR |
| OI-089-040-002 | TLB DNN retraining cadence — agree on-ground update interval with Q-DATAGOV per CBM programme | Q-STRUCTURES | PDR |
| OI-089-040-003 | PHO RUL battery model — calibration with ATLAS-072 BMS aging data from test cells | Q-GREENTECH | CDR |
| OI-089-040-004 | PHO maintenance optimization interface to CMS — agree message format with ATA 45 team | Q-INDUSTRY | PDR |
