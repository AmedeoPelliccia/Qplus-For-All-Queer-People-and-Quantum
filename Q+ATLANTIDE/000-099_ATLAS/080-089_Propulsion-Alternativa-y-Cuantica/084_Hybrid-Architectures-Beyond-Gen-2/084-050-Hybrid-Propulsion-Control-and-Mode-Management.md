---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-084-050-HYBRID-PROPULSION-CONTROL-AND-MODE-MANAGEMENT"
register: ATLAS-1000
title: "Hybrid Propulsion Control and Mode Management"
ata: "ATLAS-084 (Hybrid Architectures — Beyond Gen-2)"
sns: "084-050-00"
subsection: "084"
subsubject_code: "050"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HPC, Q-HORIZON, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0084-050"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-084-050-HYBRID-PROPULSION-CONTROL-AND-MODE-MANAGEMENT
     ATLAS-084 (Hybrid Architectures — Beyond Gen-2) · Hybrid Propulsion Control and Mode Management
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Hybrid Propulsion Control and Mode Management

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

ATLAS subsubject 084-050 defines the BGSCU control architecture, the Quantum Approximate Optimisation Algorithm (QAOA) Model Predictive Control (MPC) scheduler, the classical fallback control law, the 8-mode state machine, and the BGSCU-to-subsystem communication protocols. This is the authoritative control design baseline from which BGSCU software requirements and hardware interface specifications are derived.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA Reference | ATLAS-084 — 084-050 Hybrid Propulsion Control and Mode Management |
| Certification Basis | DO-178C DAL B (BGSCU software); DO-254 DAL B (BGSCU hardware); ARINC 653 |
| S1000D SNS | 084-050-00 |

---

## §3 BGSCU Architecture

The Beyond-Gen-2 Supervisory Control Unit (BGSCU) is a dual-lane, hot-standby controller qualified to DO-178C DAL B (software) and DO-254 DAL B (hardware). Each lane runs on an independent processor module (COTS COTS-P7 space-grade derivative, 2.4 GHz quad-core) with ARINC 653 OS partitioning to separate flight-critical control partitions from research/monitoring partitions.

**Lane A** is the active lane. **Lane B** is the hot standby lane. Both lanes receive identical sensor inputs. Lane B monitors Lane A output and takes over within 10 ms if a Lane A watchdog timeout or disagreement monitor trip occurs.

**Processing partitions (Lane A):**
| Partition | Function | Scheduling Period | DAL |
|---|---|---|---|
| P1 — MPC Execution | QAOA QPU interface; dispatch setpoint computation | 20 ms | DAL B |
| P2 — Mode State Machine | Mode transitions; BTB and contactor commands | 10 ms | DAL B |
| P3 — Source Controllers | BDCC setpoint broadcast; ATRU demand; BMS polling | 20 ms | DAL B |
| P4 — AFDX Communications | Publish/subscribe to FADEC, CMS, EPMS | 50 ms | DAL C |
| P5 — BITE / Monitoring | Self-test; source health aggregation | 100 ms | DAL C |

**QPU Module:** A 16-qubit superconducting transmon QPU module operates within BGSCU at 15 mK (local dilution refrigerator, 200 W input power). The QPU executes QAOA circuits of depth p = 4, approximating the MPC energy minimisation problem over a 300 s prediction horizon (15 × 20 ms steps discretised at 20 s intervals). QPU result is forwarded to P1 as a dispatch vector [P_SSBP, P_FCSS, P_VCGT1, P_VCGT2, P_SCEB] within 18 ms.

---

## §4 Mode State Machine

| Mode ID | Mode Name | Entry Condition | Exit Condition | Sources Active |
|---|---|---|---|---|
| M0 | Power-Off | Aircraft de-energised | Aircraft power-on | None |
| M1 | Standby (GND) | Aircraft power-on; all inhibits cleared | Pre-flight sequence initiated | SSBP trickle; BGSCU initialising |
| M2 | Ground Pre-Flight | Crew pre-flight; BGSCU BIT complete | Takeoff clearance + all sources ready | SSBP; FCSS warm-up; SCEB charge |
| M3 | Takeoff / STOL Boost | TOGA lever position OR STOL mode | Gear up + V₂ + 200 ft AGL | SSBP + VCGT + SCEB (peak) |
| M4 | Climb Eco | Gear up; FMS climb profile active | Level-off at cruise FL | VCGT primary; SSBP partial |
| M5 | Cruise Optimised | FL cruise; QAOA active | Descent initiation | FCSS primary; SSBP top-up (QAOA dispatch) |
| M6 | Descent Regen | FMS descent; thrust idle | Flare / 50 ft AGL | PMSM regen → SSBP / SCEB |
| M7 | Degraded | Any source isolation fault | Fault cleared + crew reset | Remaining sources per DM-1…DM-6 (084-060) |

**Mode transition guard conditions:** Transitions to M3, M4, M5 are permitted only when all of the following are true: BGSCU Lane A and B healthy; HVDC Bus-800 voltage within limits; at least 2 sources available at ≥ 50 % rated power; no active Level-1 fault.

---

## §5 QAOA MPC Description

**Objective function:** Minimise total primary energy cost over a 300 s prediction horizon:

```
J = Σ [w₁·SFC_VCGT·P_VCGT(k) + w₂·SoC_cost(P_SSBP(k)) + w₃·H2_cost(P_FCSS(k))] · Δt
```

where:
- `SFC_VCGT` = specific fuel consumption of VCGT (kg/kWh, function of shaft power)
- `SoC_cost` = quadratic penalty for SSBP SoC deviation from target trajectory
- `H2_cost` = LH₂ mass flow cost for FCSS (aligned with H₂ price/environmental weight)
- `w₁, w₂, w₃` = mission-phase weighting factors (tuned pre-flight by FMS)
- `Δt` = 20 s (discretisation step within 300 s horizon)

**State vector (per step):** [SoC_SSBP_A, SoC_SSBP_B, SoC_SCEB, P_demand, P_FCSS_avail, P_VCGT1_avail, P_VCGT2_avail, T_SSBP, T_FCSS]

**Constraint set:**
- Power balance: P_SSBP + P_FCSS + P_VCGT1 + P_VCGT2 + P_SCEB = P_demand(k) at each step
- Source limits: 0 ≤ P_source ≤ P_max_source (from real-time availability)
- SoC limits: SoC_min ≤ SoC_SSBP ≤ SoC_max (10–95 %)
- Ramp rate: |ΔP_VCGT| ≤ 120 kW/s (turbine response limit)

**QAOA encoding:** The optimisation is mapped to a Quadratic Unconstrained Binary Optimisation (QUBO) problem discretised into 4-bit source dispatch levels per step. With 5 sources × 4 bits × 15 steps = 300 binary variables; reduced to 16-qubit representation via variable aggregation and symmetry reduction. QAOA depth p = 4; output solution rounded to nearest feasible dispatch vector.

---

## §6 Classical Fallback Control

If the QPU reports latency > 25 ms, error rate > 0.05, or hardware fault, BGSCU P1 automatically switches to the classical rule-based dispatch law within one MPC cycle (20 ms). The classical fallback uses the priority table defined in 084-030 §5 with a proportional-integral (PI) power balance controller updating at 50 ms. Fallback engagement is logged as a BGSCU fault code (FC-084-QPU-01) and annunciated on the BGHA synoptic MFD page.

The fallback produces sub-optimal (vs. QAOA) but safe and certified dispatch. Fuel burn penalty in classical fallback is estimated at 3–7 % vs. full QAOA operation.

---

## §7 BGSCU-to-Subsystem Communication

| Interface | Remote System | Protocol | Virtual Link | Data | Period |
|---|---|---|---|---|---|
| Power demand advisory | FADEC — ATA 73 | AFDX ARINC 664 P7 | VL-084-01 | BGHA total power; mode; VCGT demand advisory | 100 ms |
| BITE / faults | CMS — ATA 45 | AFDX ARINC 664 P7 | VL-084-02 | Fault codes; LRU health; energy totals | 500 ms |
| Research telemetry | EPMS | AFDX ARINC 664 P7 | VL-084-03 | Full state vector; QPU dispatch; 50 Hz | 20 ms |
| Thermal data | TMS — ATLAS-074 | AFDX ARINC 664 P7 | VL-084-04 | BGHA-TML temps; BGSCU heat load | 100 ms |
| FCSS stack interface | FCCU | AFDX ARINC 664 P7 | VL-084-05 | H₂ demand; stack current limit; FCSS mode | 50 ms |
| BDCC / ATRU gate drives | All BDCCs; ATRUs | CAN ISO 11898 (internal) | N/A | Setpoints; fault flags; contactor commands | 20 ms |

---

## §8 Interfaces

| Interface | Connected System | Protocol | Data |
|---|---|---|---|
| Inceptor demand | Thrust Lever Assembly (TLA) | ARINC 429 (from FADEC relay) | Total thrust demand (N or kN) |
| FMS flight profile | FMS — ATA 22 | AFDX | Predicted flight phase; altitude; fuel remaining |
| Source availability | All BDCC controllers | CAN ISO 11898 | Real-time power available per source |
| BGSCU GSE | BGSCU-GSE-1 | USB-C 3.2 | Software load; diagnostic download; QPU calibration |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-084-050-001 | QAOA QUBO formulation validation vs. mixed-integer linear programming (MILP) benchmark | Q-HPC | CDR |
| OI-084-050-002 | BGSCU Lane A/B disagreement monitor threshold — acceptable divergence limit | Q-GREENTECH | PDR |
| OI-084-050-003 | QPU dilution refrigerator power (200 W) impact on aircraft electrical budget | Q-INDUSTRY | PDR |
| OI-084-050-004 | DO-178C DAL B compliance strategy for QAOA-derived dispatch output (non-deterministic element) | Q-GREENTECH | PDR |
| OI-084-050-005 | Classical fallback PI controller tuning — fuel burn penalty characterisation | Q-HPC | CDR |
