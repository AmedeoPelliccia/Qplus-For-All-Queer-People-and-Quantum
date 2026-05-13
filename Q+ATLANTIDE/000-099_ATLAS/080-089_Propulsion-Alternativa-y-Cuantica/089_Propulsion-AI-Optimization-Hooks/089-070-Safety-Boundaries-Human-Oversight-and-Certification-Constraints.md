---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-089-070-SAFETY-BOUNDARIES-HUMAN-OVERSIGHT-AND-CERTIFICATION-CONSTRAINTS"
register: ATLAS-1000
title: "Safety Boundaries, Human Oversight and Certification Constraints"
ata: "ATLAS-089 (Propulsion AI Optimization Hooks)"
sns: "089-070-00"
subsection: "089"
subsubject_code: "070"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HPC, Q-DATAGOV, Q-HORIZON]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0089-070"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-089-070-SAFETY-BOUNDARIES-HUMAN-OVERSIGHT-AND-CERTIFICATION-CONSTRAINTS
     ATLAS-089 (Propulsion AI Optimization Hooks) · Safety Boundaries, Human Oversight and Certification Constraints
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Safety Boundaries, Human Oversight and Certification Constraints

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-089 AI Optimization](https://img.shields.io/badge/ATLAS--089-Propulsion%20AI%20Optimization%20Hooks-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-teal)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

ATLAS subsubject 089-070 defines the Safety Boundary Monitor (SBM) architecture, the hard constraint catalogue, the human oversight mechanisms, and the full certification constraint set applicable to the PAIO AI optimization system. It establishes the boundary between the AI optimization domain (AIOCU DAL B) and the safety enforcement domain (SBM DAL A), and documents the crew interfaces for AI control and override.

---

## §2 Safety Boundary Monitor (SBM) Architecture

The SBM is a **non-AI, deterministic, DO-178C DAL A** safety enforcement module architecturally isolated from the AIOCU AI optimization partition. It intercepts all AIOCU output commands before relay to actuator controllers and enforces the following principles:

- **Clamp:** All AI commands are bounded by hard physical limits (§3). Any command outside bounds is clamped to the nearest limit without notification delay.
- **Override:** If an AI command trend would cross a safety limit within 500 ms, the SBM pre-emptively overrides and freezes the relevant command.
- **Veto:** If any propulsor subsystem reports a safety-critical fault via discrete wire (independent of AFDX), the SBM vetoes all AIOCU commands to that subsystem and activates the fixed-schedule fallback LUT for that channel.

### 2.1 SBM Hardware Partition

| Attribute | Value |
|---|---|
| SBM processor | Separate redundant microcontroller (not shared with AIOCU) |
| Software certification | DO-178C DAL A |
| Hardware certification | DO-254 DAL A |
| Communication to AIOCU | ARINC 653 IPC channel (read AIOCU output, write override flag) |
| Discrete veto lines | Direct hardwired discretes to DEPCU, BLICU, ORSCU (bypass AFDX) |
| SBM response time | ≤ 5 ms from limit detection to command clamp |

---

## §3 Hard Safety Constraint Catalogue

All limits listed below are enforced by the SBM and cannot be overridden by the AIOCU under any condition:

### 3.1 Thrust Limits

| Parameter | Lower Limit | Upper Limit | Notes |
|---|---|---|---|
| DEP individual fan thrust (Pi) | 0 kN (shutdown) | P_max_Pi (function of Mach, altitude) | Per fan envelope; lookup from certified table |
| DEP total thrust | T_min_flight (go-around floor) | T_max_total (structural limit) | CS-25.119 go-around floor enforced |
| BLI combined power | 0 kW | 240 kW | TLB thermal limit + electrical rating |
| Lateral thrust asymmetry (P1–P4) | −35 kN | +35 kN | Wing root structural limit |
| ORCR advisory offset | −5 % demand | +5 % demand | Advisory only; ORSCU retains full authority |

### 3.2 Energy Limits

| Parameter | Lower Limit | Upper Limit | Notes |
|---|---|---|---|
| Battery SoC | 0.15 (15 %) | 0.95 (95 %) | Hard dispatch limits |
| Battery discharge rate | 0 kW | 500 kW | Peak discharge rating |
| Fuel-cell power | 0 kW | 400 kW | FCCU rated maximum |
| Battery charge rate (regen) | 0 kW | 150 kW | Regenerative charge limit |

### 3.3 Thermal Limits

| Parameter | Hard Limit | Source |
|---|---|---|
| DEP motor winding temperature | 180 °C | Motor insulation class H |
| DEP IGBT junction temperature | 175 °C | Power electronics datasheet |
| BLI motor winding temperature | 170 °C | Motor insulation class H |
| Battery module temperature | 55 °C | Cell safety requirement |
| PEMFC stack temperature | 85 °C | MEA degradation limit |

### 3.4 Structural and Aerodynamic Limits

| Parameter | Hard Limit | Notes |
|---|---|---|
| Wing root bending moment (from APCO differential thrust) | ≤ Design limit load × 1.0 | CS-25.305; no exceedance allowed |
| BLI DC60 distortion contribution | DC60 ≤ 0.35 | Fan stability limit (ATLAS-086) |

---

## §4 Human Oversight Mechanisms

### 4.1 AI-OPT-OFF Guarded Switch

The cockpit contains a guarded two-position switch **AI-OPT-OFF** (located on the overhead panel, OHP-089-1):

| Switch Position | PAIO State | AIOCU State | Reversion Time |
|---|---|---|---|
| AI-OPT-ON (normal) | Full AI optimization active | PPOE + EMOM + TLB + APCO + QAOA | — |
| AI-OPT-OFF (guarded) | AI inhibited (DM-7) | Fixed LUT fallback | ≤ 1 s to complete reversion |

**Procedure for AI-OPT-OFF activation:** Crew lifts guard and places switch to OFF. AIOCU transitions to DM-7 within 1 s; AWMS generates STATUS message "AI OPT OFF"; CMS logs timestamp, flight phase, and reason code.

### 4.2 Pilot-Selectable Optimization Objective

When AI optimization is active, the flight crew may select among three optimization objectives via the MCDU/FMS interface:

| Objective Code | Name | PPOE Weight | EMOM Priority | Notes |
|---|---|---|---|---|
| OBJ-1 (default) | Balanced (fuel + efficiency) | w₁=0.40, w₂=0.35 | Standard SoC trajectory | Default cruise objective |
| OBJ-2 | Maximum efficiency | w₁=0.55, w₂=0.25 | Aggressive battery use | Used for range maximization |
| OBJ-3 | Minimum noise | w₁=0.20, w₂=0.30, w₃_noise=0.30 | Conservative BLI/DEP | Required for noise-sensitive airports |

### 4.3 Explainability Display (EXP page)

An optional MCDU page (EXP-089) shows the current AIOCU decision rationale:

| Field | Content |
|---|---|
| Active objective | OBJ-1/2/3 |
| Dominant optimization driver | e.g., "SoC recovery", "DEP fan P3 thermal limit", "BLI drag reduction" |
| SBM status | NOMINAL / ACTIVE CLAMP / OVERRIDE |
| Last override event | Timestamp and parameter clamped |
| QAOA macro plan | Current mission segment strategy |

---

## §5 Certification Constraint Summary

| Constraint | Standard | Description |
|---|---|---|
| AI/ML Learning Assurance | EUROCAE ED-324 | PPOE and TLB: LAL 1B; APCO and QAOA: LAL 2; no online learning in flight |
| Software DAL | DO-178C | AIOCU optimization engines: DAL B; SBM: DAL A; EEPROM LUTs: DAL B |
| Hardware DAL | DO-254 | AIOCU FPGA and processor: DAL B; SBM MCU: DAL A |
| Partition independence | ARINC 653 | SBM partition must demonstrate time and space partitioning from AIOCU partition |
| Human override | CS-25.1329 adapted | AI-OPT-OFF reversion ≤ 1 s; single crew action |
| Configuration control | DO-178C §12; CM-SWCEH-001 | NN weights and QAOA circuit are configuration-controlled artefacts; field update via SB only |
| Fail-safe behaviour | CS-25.1309 | Failure of AIOCU (including both channels) must not prevent continued safe flight; SBM must maintain fixed LUT operation |
| Explainability and audit | EASA AI Roadmap §4.3 | All AIOCU decisions logged at ≥ 1 Hz; downloadable post-flight; retained for ≥ 2 000 FH |

---

## §6 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-089-070-001 | EASA MOC for AI-OPT-OFF reversion time ≤ 1 s — confirm acceptable means of compliance with CS-25.1329 | Q-GREENTECH | PDR |
| OI-089-070-002 | SBM DAL A partition independence verification plan — tool qualification for ARINC 653 RTOS separation test | Q-HPC | PDR |
| OI-089-070-003 | EUROCAE ED-324 LAL 1B compliance plan for PPOE RL — confirm EASA acceptance of inference-only deployment model | Q-DATAGOV | PDR |
| OI-089-070-004 | OBJ-3 (minimum noise) objective validation — confirm DEP asymmetry reduction achieves ≥ 1.5 EPNdB cumulative noise reduction at Heathrow Category C | Q-HORIZON | CDR |
