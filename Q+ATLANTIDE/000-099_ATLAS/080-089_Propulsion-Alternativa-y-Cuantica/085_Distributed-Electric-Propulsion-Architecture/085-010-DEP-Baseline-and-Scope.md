---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-085-010-DEP-BASELINE-AND-SCOPE"
register: ATLAS-1000
title: "DEP Baseline and Scope"
ata: "ATLAS-085 (Distributed Electric Propulsion Architecture)"
sns: "085-010-00"
subsection: "085"
subsubject_code: "010"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0085-010"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-085-010-DEP-BASELINE-AND-SCOPE
     ATLAS-085 (Distributed Electric Propulsion Architecture) · DEP Baseline and Scope
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# DEP Baseline and Scope

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

This document defines the agnostic ATLAS standard-level architecture context for `DEP Baseline and Scope`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 Applicability

| Applicability Level | Rule |
|---|---|
| Standard taxonomy | Applies to the ATLAS node `085` |
| Programme implementation | Conditional; determined by programme architecture, trade studies, certification basis, and applicability model |
| Product configuration | Defined in the programme-specific configuration baseline |
| Effectivity | Defined in the programme CSDB / applicability layer |
| Non-applicability | Must be explicitly stated in the programme impact-study branch when excluded |
## §3 Architecture Comparison

The following table summarises how the DEPA compares to the centralized propulsion architectures used in earlier programme-defined aircraft type configurations.

| Attribute | Conventional Twin-Engine (Ref.) | Gen-2 Hybrid (ATLAS 070–079) | DEPA (ATLAS 085) |
|---|---|---|---|
| Propulsor count | 2 (podded turbofans) | 2 turbofan + 2 BLI fans | 4 BLI fans (no turbofan pods) |
| Total fan propulsive power | 2 × 6 000 kW shaft (thrust) | 2 × 200 kW electric fans | 4 × 500 kW electric fans |
| BLI integration | None | Partial (aft fans only) | Full (over-wing + aft-fuselage) |
| Motor drive topology | N/A | Centralised MDU, 270 V HVDC | Distributed co-located MDUs, <NOMINAL-VOLTAGE> HVDC |
| Control unit | FADEC only (ATA 73) | EMCU + FADEC | DEPCU DAL B + FADEC |
| Asymmetric thrust control | Engine-out yaw via rudder | Partial differential | Full per-propulsor differential torque |
| Aero-propulsive gain | None | ~4 % cruise drag reduction | ~12 % cruise drag reduction (P3+P4) |
| Regenerative capability | None | None | Yes — descent regen 80 kW |
| Noise footprint | High (high bypass podded) | Moderate | Low (distributed, BLI noise masking) |

---

## §4 Technology Readiness Summary

| Technology | Current TRL | Target TRL (Phase 2 / CDR) | Limiting Factor |
|---|---|---|---|
| 500 kW co-located PMSM (per propulsor) | TRL 5 (ground prototype) | TRL 7 (flight demo) | Motor-nacelle thermal management; weight target < 120 kg/unit |
| 500 kW co-located MDU (HVDC <NOMINAL-VOLTAGE> inverter) | TRL 5 (lab bench) | TRL 7 (flight demo) | IGBT switching losses; EMC DO-160G at HVDC <NOMINAL-VOLTAGE> |
| BLI duct integration (over-wing root) | TRL 4 (CFD + small-scale wind tunnel) | TRL 6 (large-scale WT or flight test) | Boundary-layer distortion at fan face; fan acoustic response |
| BLI duct integration (aft fuselage) | TRL 5 (heritage from ATLAS-086) | TRL 7 (flight demo) | Fuselage structural cut-outs; aero-structural coupling |
| DEPCU dual-lane DAL B | TRL 5 (FPGA proto) | TRL 7 (aircraft integration) | Asymmetric compensator algorithm verification |
| Per-propulsor regenerative inverter | TRL 4 (commercial motor heritage) | TRL 6 (ground qualification) | Four-quadrant MDU certification; bus back-feed protection |
| Differential thrust yaw control | TRL 4 (simulation) | TRL 6 (iron-bird ground test) | CS-25.147 compliance test plan |

---

## §5 Mission Trade Space

The DEPA programme targets six mission roles for the programme-defined aircraft type research platform:

**Role A — Full-DEP Takeoff (STOL variant):** All four propulsors at 500 kW, fed from BGHA all-source peak dispatch. Total DEP power 2 000 kW. Supports reduced-field operations from runway ≥ 1 200 m. Noise footprint reduction estimated at 3 EPNdB vs. conventional at equivalent thrust.

**Role B — BLI-Optimised Cruise:** P3 + P4 at cruise-optimal torque (~300 kW each); P1 + P2 at partial power (~150 kW each). BLI drag reduction ~12 % at FL 350 / M 0.78 steady. Net fuel (or H₂) saving vs. ATLAS-070 Gen-2 estimate: 10–15 %.

**Role C — Zero-Emission Taxi:** P3 + P4 at low torque (taxi thrust ~30 kN) from BGHA SSBP only. P1 + P2 idle. Eliminates all airport combustion emissions. Battery range for taxi: ≥ 45 min.

**Role D — Descent Regen:** All four propulsors windmilling in generator mode at descent idle. Estimated regenerative recovery: 80 kW total → ~50 kWh per typical descent. Absorbed by BGHA SSBP.

**Role E — Asymmetric DEP Research:** One propulsor deliberately throttled or isolated. DEPCU asymmetric compensator activates differential torque on remaining three units to demonstrate yaw authority without rudder input. Used to characterise CS-25.147 compliance margins.

**Role F — Noise-Optimised Approach:** P1 + P2 throttled back; P3 + P4 carry approach thrust. BLI shielding of aft-fan noise by fuselage. Estimated approach noise reduction: 2 EPNdB vs. Role A.

---

## §6 Performance Baseline

| Parameter | Floor (Design Minimum) | Target | Stretch Goal |
|---|---|---|---|
| Total DEP installed power | 1 800 kW | 2 000 kW | 2 400 kW |
| Per-propulsor power | 450 kW | 500 kW | 600 kW |
| BLI drag reduction (P3+P4 at cruise) | 8 % | 12 % | 16 % |
| BLI drag reduction (P1+P2 at cruise) | 2 % | 4 % | 6 % |
| DEPCU torque command cycle | ≤ 10 ms | 10 ms | 5 ms |
| Asymmetric thrust yaw correction | ≤ 100 ms | 50 ms | 20 ms |
| Regenerative recovery (descent) | 50 kW | 80 kW | 120 kW |
| PMSM specific power | ≥ 3.5 kW/kg | 4.0 kW/kg | 5.0 kW/kg |
| MDU specific power | ≥ 5.0 kW/kg | 6.0 kW/kg | 8.0 kW/kg |
| Noise reduction vs. podded turbofan | ≥ 2 EPNdB | 3 EPNdB | 5 EPNdB |
| CO₂ / fuel burn reduction vs. Gen-2 | 10 % | 15 % | 20 % |

---

## §7 Power Budget

| Source / Consumer | Nominal (kW) | Peak (kW) | Notes |
|---|---|---|---|
| BGHA HVDC <NOMINAL-VOLTAGE> bus supply | 2 000 | 2 200 | Provided by ATLAS-084 BGSCU dispatch |
| P1 PMSM (over-wing port) | 300 | 500 | Cruise / max takeoff |
| P2 PMSM (over-wing stbd) | 300 | 500 | Cruise / max takeoff |
| P3 PMSM (aft-fuselage port) | 350 | 500 | Higher cruise power for BLI gain |
| P4 PMSM (aft-fuselage stbd) | 350 | 500 | Higher cruise power for BLI gain |
| DEPCU + MDU control loads | 8 | 12 | Avionics; CAN buses |
| DEP-TML cooling pumps | 6 | 10 | EGW coolant loop |
| **Total DEP bus load (cruise)** | **1 314** | — | P3+P4 dominant |
| **Total DEP bus load (takeoff)** | **2 000** | **2 222** | All four propulsors max |

---

## §8 Interfaces

| Interface | Connected System | Protocol | Data |
|---|---|---|---|
| Power — all MDUs | BGHA HVDC <NOMINAL-VOLTAGE> bus (ATLAS-084) | HVDC <NOMINAL-VOLTAGE> cable | Source dispatch per BGSCU MPC setpoints |
| Thrust demand | FADEC — ATA 73 | AFDX VL-085-01 | Total DEP thrust demand; phase |
| Yaw coordination | FMS — ATA 22 | AFDX VL-085-03 | Differential thrust advisory |
| Research data | EPMS | AFDX VL-085-04 | 100 Hz per-propulsor power; BLI pressure maps |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-085-010-001 | BLI duct distortion acoustic penalty — wind tunnel test plan | Q-HORIZON | PDR |
| OI-085-010-002 | PMSM weight target (≤ 120 kg per unit) — supplier RFI | Q-INDUSTRY | PDR |
| OI-085-010-003 | Differential thrust yaw authority — simulation validation vs. CS-25.147 requirement | Q-GREENTECH | CDR |
| OI-085-010-004 | BLI drag reduction model fidelity (CFD vs. flight test plan) | Q-HORIZON | Phase 2 |
| OI-085-010-005 | Regenerative inverter (four-quadrant MDU) bus back-feed protection study | Q-INDUSTRY | PDR |
