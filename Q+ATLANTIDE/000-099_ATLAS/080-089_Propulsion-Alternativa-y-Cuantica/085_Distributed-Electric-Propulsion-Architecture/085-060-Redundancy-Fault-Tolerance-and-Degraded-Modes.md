---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-085-060-REDUNDANCY-FAULT-TOLERANCE-AND-DEGRADED-MODES"
register: ATLAS-1000
title: "Redundancy Fault Tolerance and Degraded Modes"
ata: "ATLAS-085 (Distributed Electric Propulsion Architecture)"
sns: "085-060-00"
subsection: "085"
subsubject_code: "060"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HORIZON, Q-STRUCTURES, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0085-060"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-085-060-REDUNDANCY-FAULT-TOLERANCE-AND-DEGRADED-MODES
     ATLAS-085 (Distributed Electric Propulsion Architecture) · Redundancy Fault Tolerance and Degraded Modes
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Redundancy Fault Tolerance and Degraded Modes

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

This document defines the agnostic ATLAS standard-level architecture context for `Redundancy Fault Tolerance and Degraded Modes`.

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
## §3 Degraded Mode Definitions

| Mode | Trigger Condition | Propulsors Lost | DEPCU Response | Pilot Actions | Thrust Available |
|---|---|---|---|---|---|
| DM-1 | Single propulsor loss (any P1–P4) | 1 × 500 kW | BTB open; asymmetric compensator activates; remaining 3 propulsors redistribute thrust | Monitor DEP synoptic; continue flight; dispatch per MEL | 75 % (3 × 500 kW) |
| DM-2 | Loss of one symmetric pair (P1+P2 or P3+P4) | 2 × 500 kW (same half-plane) | Both BTBs open; remaining pair at max; FMS notified for trim | Reduce cruise speed by M 0.04 if required; dispatch per MEL | 50 % (1 pair × 2 × 500 kW) |
| DM-3 | Loss of both aft propulsors (P3+P4) | 2 × 500 kW (aft) | P3+P4 BTBs open; P1+P2 at max; BLI gain lost; pitch trim change | Monitor pitch trim advisory; potential cruise altitude reduction | 50 % (P1+P2); no BLI gain |
| DM-4 | Loss of three propulsors | 3 × 500 kW | Single remaining propulsor; DEPCU asymmetric max; BGSCU notified; crew MAYDAY advisory | Declare MAYDAY; divert immediately; 30 min max endurance | 25 % (1 × 500 kW); yaw limit speed VML |
| DM-5 | DEPCU Lane A fault | DEPCU lane (not propulsor) | Lane B promoted to active within 5 ms; CAN buses transferred; propulsors maintained | No crew action required; monitor DEPCU LANE B status on MFD | 100 % (sub-optimal allocation) |

---

## §4 Reconfiguration Logic

**Automatic reconfiguration (DEPCU authority):**
The DEPCU automatically opens the BTB of a faulted propulsor station within 50 ms of fault detection (MDU fault flag or SSPC overcurrent trip). The mode state machine transitions to M4 (Degraded) and the asymmetric thrust compensator recomputes torque setpoints for remaining propulsors within one 10 ms control cycle. BGSCU is notified via AFDX VL-085-06 of the new DEP power demand profile.

**Manual reconfiguration:**
If the DEPCU commands a spurious BTB open, the crew can override via the DEP OVERRIDE panel (guarded amber cover) with discrete switches to command BTB re-close and SSPC re-arm. Manual override is logged and requires maintenance action before next flight.

**DEPCU authority limits in degraded modes:**
- DM-1: Full asymmetric compensation authority; yaw bounded by rudder authority margin.
- DM-2: Remaining pair at max; no cross-coupling to lost pair bus.
- DM-3: Pitch trim advisory only; no autonomous pitch re-trim.
- DM-4: Single-propulsor torque limited to prevent airframe yaw exceeding VML; speed restriction.
- DM-5: Lane B dispatch is sub-optimal (no aero-propulsive coupling table — uses simplified equal-split); 3 % efficiency penalty accepted.

---

## §5 Redundancy Architecture

| Component | Redundancy Method | Switchover Time | DEPA Mode Affected |
|---|---|---|---|
| DEPCU | Dual-lane hot standby (Lane A + Lane B) | < 5 ms | DM-5 |
| P1 propulsor | No redundancy (single unit); partial compensation by P2+P3+P4 | BTB open in 5 ms | DM-1 |
| P2 propulsor | As P1 (mirror; symmetric) | BTB open in 5 ms | DM-1 |
| P3 propulsor | No redundancy; highest consequence loss | BTB open in 5 ms | DM-1, DM-3 |
| P4 propulsor | As P3 (mirror) | BTB open in 5 ms | DM-1, DM-3 |
| CAN Bus A | Redundant Bus B (per propulsor) | Automatic switchover 1 ms | No propulsor loss |
| BTB (each) | Single unit; mechanical failsafe open-on-de-energise | N/A | Propulsor isolation |
| DEP-TML Pump | 2 redundant EGW pumps | Auto switchover 5 s | No propulsor loss |

---

## §6 FMEA Summary — Top 10 Failure Modes

| # | Failure Mode | Failure Effect | Severity | Detection | Mitigation |
|---|---|---|---|---|---|
| 1 | MDU-3 IGBT shoot-through | Loss of P3; potential bus spike | Hazardous | SSPC-P3 overcurrent; MDU CAN fault | BTB-P3 open < 5 ms; DM-1 entry |
| 2 | PMSM-3 winding insulation failure | Loss of P3; potential short to nacelle | Hazardous | IMU resistance drop; MDU phase current asymmetry | BTB-P3 open; DEP-IMU alert |
| 3 | DEPCU Lane A processor fault | MPC sub-optimal; allocation non-optimal | Major | Watchdog timeout; cross-lane compare | Lane B takeover in 5 ms; DM-5 |
| 4 | BTB-P1 spurious open | Loss of P1; DM-1 | Major | DEPCU detects MDU-1 power loss in 10 ms | DM-1 asymmetric compensation; crew advisory |
| 5 | CAN Bus A failure (single propulsor) | CAN Bus B takes over | Minor | DEPCU CAN A/B error counter | Bus B active; no propulsor loss |
| 6 | MDU-1 DC link capacitor failure | Loss of P1; potential bus voltage spike | Major | MDU CAN fault; bus voltage transient | SSPC-P1 trip; BTB-P1 open; DM-1 |
| 7 | DEP-TML pump A failure | Coolant flow reduction; MDU thermal derate | Minor | Flow sensor drop; MDU temp rise | Pump B auto-start; 5 s switchover; MDU derated temporarily |
| 8 | PMSM-3 fan blade fatigue crack | Eventual FBO if undetected | Catastrophic (if missed) | Vibration signature (MDU speed noise floor) | Vibration monitoring; 6 000 h inspection mandatory |
| 9 | HVDC cable P3 insulation ground fault | Bus-800 leakage; potential arc in fuselage | Major | DEP-IMU < 100 kΩ | BTB-P3 open; IMU fault location |
| 10 | SSPC-P4 overcurrent spurious trip | Loss of P4; DM-1 | Major | DEPCU detects MDU-4 power loss | DM-1; crew advisory; dispatch per MEL |

---

## §7 MEL Cross-Reference

| MEL Item | Component | Max Dispatch Condition | Required Op Procedure |
|---|---|---|---|
| MEL-085-P1 | P1 (over-wing port) inoperative | 10 days; DM-1 rules | DEPCU DM-1 selected pre-flight; BTB-P1 verified open; yaw limit speed VML in QRH |
| MEL-085-P2 | P2 (over-wing stbd) inoperative | 10 days; DM-1 rules | As MEL-085-P1 (mirror) |
| MEL-085-P3 | P3 (aft-fuse port) inoperative | 10 days; DM-1 rules; no STOL ops | DEPCU DM-1; BLI gain advisory; no operations from runways < 1 500 m |
| MEL-085-P4 | P4 (aft-fuse stbd) inoperative | 10 days; DM-1 rules; no STOL ops | As MEL-085-P3 (mirror) |
| MEL-085-P12 | P1 + P2 both inoperative | 5 days; DM-2 rules | DEPCU DM-2; reduced cruise speed −M 0.04; no STOL |
| MEL-085-P34 | P3 + P4 both inoperative | 5 days; DM-3; no STOL; reduced range | DEPCU DM-3; no BLI gain; fuel uplift required |
| MEL-085-DEPCU-LB | DEPCU Lane B inoperative | 3 days; no redundancy on Lane A | Lane A only; monitoring only; no DM-5 auto-switch |

---

## §8 Interfaces

| Interface | Connected System | Protocol | Data |
|---|---|---|---|
| Fault flags → DEPCU | MDU-1…4; SSPC-P1…4; BTBs | CAN ISO 11898 | Fault codes; overcurrent; temp alarms |
| BTB commands | BTB-P1…P4 | Hardwired discrete | Open/close; position feedback |
| DM status → CMS | CMS — ATA 45 | AFDX VL-085-02 | Active DM ID; thrust available %; maintenance code |
| DM status → cockpit | ECAM / MFD (DEP synoptic) | AFDX (via DEPCU) | Amber/red propulsor bars; DM ID; advisory messages |
| DM status → BGSCU | BGSCU — ATLAS-084 | AFDX VL-085-06 | DEPA power capability for BGSCU MPC re-plan |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-085-060-001 | DM-4 yaw limit speed VML — flight test characterisation plan | Q-GREENTECH | Phase 2 |
| OI-085-060-002 | FMEA item 8 (fan blade fatigue) — vibration threshold setting methodology | Q-STRUCTURES | CDR |
| OI-085-060-003 | MEL-085-P34 fuel penalty calculation — updated range with P3+P4 inoperative | Q-GREENTECH | PDR |
| OI-085-060-004 | CS-25.147 asymmetric thrust — DM-1 compliance margin demonstration via iron-bird test | Q-GREENTECH | CDR |
