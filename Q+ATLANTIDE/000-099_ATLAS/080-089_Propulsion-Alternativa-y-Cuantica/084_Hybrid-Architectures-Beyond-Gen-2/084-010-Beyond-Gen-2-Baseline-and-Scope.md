---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-084-010-BEYOND-GEN-2-BASELINE-AND-SCOPE"
register: ATLAS-1000
title: "Beyond-Gen-2 Baseline and Scope"
ata: "ATLAS-084 (Hybrid Architectures — Beyond Gen-2)"
sns: "084-010-00"
subsection: "084"
subsubject_code: "010"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0084-010"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-084-010-BEYOND-GEN-2-BASELINE-AND-SCOPE
     ATLAS-084 (Hybrid Architectures — Beyond Gen-2) · Baseline and Scope
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Beyond-Gen-2 Baseline and Scope

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

This document defines the agnostic ATLAS standard-level architecture context for `Beyond-Gen-2 Baseline and Scope`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 Applicability

| Applicability Level | Rule |
|---|---|
| Standard taxonomy | Applies to the ATLAS node `084` |
| Programme implementation | Conditional; determined by programme architecture, trade studies, certification basis, and applicability model |
| Product configuration | Defined in the programme-specific configuration baseline |
| Effectivity | Defined in the programme CSDB / applicability layer |
| Non-applicability | Must be explicitly stated in the programme impact-study branch when excluded |
## §3 Generation Comparison

The following table summarises how the BGHA compares to Gen-1 and Gen-2 hybrid-electric architectures previously defined for the programme-defined aircraft type programme.

| Attribute | Gen-1 (ATLAS 070 baseline) | Gen-2 (ATLAS 070–079 expanded) | Beyond-Gen-2 / BGHA (ATLAS 084) |
|---|---|---|---|
| Max installed propulsion power | 1 200 kW | 2 200 kW | 4 400 kW |
| Primary bus voltage | HVDC 270 V | HVDC 540 V | HVDC <NOMINAL-VOLTAGE> |
| Energy sources | Battery + turbine | Battery + PEMFC + turbine | SSBP + FCSS + VCGT + SCEB |
| Battery technology | <BATTERY-CHEMISTRY> liquid-cooled | <BATTERY-CHEMISTRY> liquid-cooled <ENERGY-CAPACITY> | NMC/SSE solid-state 800 kWh |
| Fuel cell power | — | 200 kW (4×50 kW PEMFC) | 400 kW (8×50 kW PEMFC) |
| Gas turbine type | Conventional turbofan | SAF-capable turbofan | Variable-cycle bi-fuel (SAF/LH₂) |
| Peak-power buffer | — | — | Supercapacitor 80 kWh / 2 MW |
| Energy management | Rule-based EMS (EMCU) | MPC 50 ms classical (EMCU DAL B) | QAOA quantum MPC 20 ms (BGSCU DAL B) |
| Zero-emission capability | None | Partial (PEMFC cruise segments) | ≥ 55 % of flight time |
| Control assurance | DAL C/B mixed | DAL B | DAL B throughout |

---

## §4 Technology Readiness Summary

| Technology | Current TRL | Target TRL (Phase 2 / CDR) | Limiting Factor |
|---|---|---|---|
| SSBP — NMC/SSE solid-state 800 kWh | TRL 4 (lab cell level) | TRL 6 (prototype pack, ground test) | Cell-level energy density vs. safety, CS-25.1353 fire cert |
| FCSS — 8×50 kW PEMFC (LH₂ feed) | TRL 6 (Gen-2 PEMFC heritage) | TRL 7 (flight demo) | LH₂ ATEX integration, stack lifetime 15 000 h |
| VCGT — SAF/LH₂ bi-fuel variable-cycle | TRL 4 (component tests) | TRL 6 (engine ground test) | Dual-fuel combustor certification, LH₂ fuel system |
| SCEB — 80 kWh supercapacitor 2 MW | TRL 5 (industrial prototype) | TRL 7 (airborne qualification) | DO-160G shock/vibe at 2 MW pulse; weight |
| QAOA quantum MPC (16-qubit) | TRL 3 (algorithm simulation) | TRL 5 (hardware-in-loop) | Airborne QPU coherence, EMI sensitivity |
| Distributed 500 kW PMSM fan sets (×4) | TRL 5 (Gen-2 motor heritage) | TRL 7 (ATLAS-085 flight demo) | Motor-airframe integration, thermal |
| HVDC <NOMINAL-VOLTAGE> bus | TRL 4 (ground rig) | TRL 6 (ground qualification) | EASA advisory material for > 540 V DC |

---

## §5 Mission Trade Space

The BGHA programme targets five mission roles for the programme-defined aircraft type research platform:

**Role A — ecoClimb:** VCGT primary power + SSBP partial, FCSS in warm standby. Optimised climb fuel burn via MPC-scheduled variable-cycle turbine throttle and SSBP peak-load shaving. Estimated fuel saving vs. Gen-2: 8–12 %.

**Role B — Turbine-Off Cruise (TOC):** FCSS primary + SSBP top-up; both VCGTs shut down. Zero direct combustion emissions during cruise segment. Available when H₂ supply ≥ 300 kg and OAT ≤ −40 °C (FCSS thermal limits). Estimated segment duration: 2–4 h.

**Role C — Zero-Emission Taxi:** SSBP only; VCGT and FCSS off. All four PMSM fans at low thrust for ground manoeuvring. Eliminates airport ground emissions.

**Role D — STOL Boost:** SCEB + SSBP + VCGT all-sources pulse for short-takeoff segment. Total 4 400 kW for ≤ 90 s. Required for operations from short (< 1 500 m) runway environments.

**Role E — Research / Quantum MPC Characterisation:** BGSCU QAOA QPU energy optimisation logging for all flight phases. Full 50 Hz telemetry to EPMS for algorithm performance characterisation vs. classical MPC baseline.

---

## §6 Performance Baseline

| Parameter | Floor (Design Minimum) | Target | Stretch Goal |
|---|---|---|---|
| Total propulsion power | 4 000 kW | 4 400 kW | 5 000 kW |
| Zero-emission flight fraction | 40 % | 55 % | 70 % |
| Cruise propulsion efficiency | 62 % (well-to-thrust) | 70 % | 75 % |
| SSBP energy (total) | 700 kWh | 800 kWh | 1 000 kWh |
| FCSS power (continuous) | 350 kW | 400 kW | 500 kW |
| VCGT bi-fuel electrical off-take | 2 000 kW | 2 400 kW | 2 800 kW |
| SCEB pulse power | 1.5 MW / 500 ms | 2 MW / 500 ms | 3 MW / 1 s |
| QAOA MPC cycle time | ≤ 30 ms | 20 ms | 10 ms |
| LH₂ consumption rate (TOC role) | ≤ 1.8 kg/min | 1.5 kg/min | 1.2 kg/min |
| CO₂ reduction vs. Gen-2 | 30 % | 45 % | 60 % |

---

## §7 Power Budget

| Source / Consumer | Nominal (kW) | Peak (kW) | Notes |
|---|---|---|---|
| SSBP discharge | 400 | 800 | 2 packs × 400 kWh; max 2C rate |
| FCSS output | 400 | 440 | 8 × 50 kW stacks; +10 % transient |
| VCGT electrical off-take | 2 400 | 2 600 | 2 × 1 200 kW nominal |
| SCEB pulse | 0 | 2 000 | ≤ 500 ms; not concurrent with full VCGT |
| 4 × PMSM fan loads | 2 000 | 2 200 | At cruise; 2 400 kW takeoff |
| BGSCU / avionics loads | 15 | 20 | Includes QPU cryo unit |
| BGHA-TML cooling pumps | 10 | 15 | EGW coolant loop |
| **Total bus load (cruise)** | **2 025** | — | FCSS + SSBP partial |
| **Total bus load (takeoff)** | **4 400** | **4 635** | All sources minus SCEB concurrent limit |

---

## §8 Interfaces

| Interface | Connected System | Protocol | Data |
|---|---|---|---|
| Power — all sources | HVDC <NOMINAL-VOLTAGE> bus | HVDC cable | Source dispatch per MPC setpoints |
| Turbine fuel | VCGT fuel system | Physical SAF/LH₂ feed | Fuel flow demand from BGSCU |
| H₂ supply to FCSS | ATLAS-077 | LH₂ feed line; CAN flow demand | H₂ mass flow; manifold pressure |
| Propulsion demand | FADEC — ATA 73 | AFDX VL-084-01 | BGHA thrust increment advisory |
| Research data | EPMS | AFDX VL-084-03 | QPU telemetry; energy flow at 50 Hz |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-084-010-001 | SSBP NMC/SSE cell supplier qualification under CS-25.1353 | Q-GREENTECH | PDR |
| OI-084-010-002 | VCGT LH₂ combustor TRL 4→6 roadmap and test article funding | Q-HORIZON | PDR |
| OI-084-010-003 | HVDC <NOMINAL-VOLTAGE> EASA advisory material identification (AMC 25.xxx) | Q-INDUSTRY | PDR |
| OI-084-010-004 | QAOA algorithm validation on hardware QPU (16-qubit superconducting) | Q-HPC | CDR |
| OI-084-010-005 | CO₂ reduction accounting methodology (well-to-wing vs. well-to-thrust) | Q-GREENTECH | PDR |
