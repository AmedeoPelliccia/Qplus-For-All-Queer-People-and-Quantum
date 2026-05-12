---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-084-060-DEGRADED-MODES-REDUNDANCY-AND-RECONFIGURATION"
register: ATLAS-1000
title: "Degraded Modes Redundancy and Reconfiguration"
ata: "ATLAS-084 (Hybrid Architectures — Beyond Gen-2)"
sns: "084-060-00"
subsection: "084"
subsubject_code: "060"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HORIZON, Q-STRUCTURES, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0084-060"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-084-060-DEGRADED-MODES-REDUNDANCY-AND-RECONFIGURATION
     ATLAS-084 (Hybrid Architectures — Beyond Gen-2) · Degraded Modes Redundancy and Reconfiguration
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Degraded Modes Redundancy and Reconfiguration

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

ATLAS subsubject 084-060 defines the six BGHA degraded operating modes (DM-1 through DM-6), the automatic and manual reconfiguration logic executed by the BGSCU, the redundancy architecture of each source and the BGSCU itself, a top-level FMEA summary for the BGHA, and the MEL (Minimum Equipment List) cross-reference for dispatch with inoperative BGHA components.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA Reference | ATLAS-084 — 084-060 Degraded Modes Redundancy and Reconfiguration |
| Certification Basis | EASA CS-25.1309; DO-178C DAL B; CS-25 AMC 25.1309 |
| S1000D SNS | 084-060-00 |

---

## §3 Degraded Mode Definitions

| Mode | Trigger Condition | Sources Lost | BGSCU Response | Pilot Actions | Thrust Available |
|---|---|---|---|---|---|
| DM-1 | Single SSBP pack fault (Pack A or B) | 1 × 400 kWh SSBP | Isolate faulty pack via BDCC and BTB; increase VCGT + FCSS share; SCEB activated as buffer | Monitor BGHA synoptic; continue flight; dispatch per MEL-084-SSBP-A/B | 80 % (VCGT + FCSS + remaining SSBP) |
| DM-2 | Both SSBP packs faulted | 2 × 400 kWh SSBP | SSBP fully isolated; VCGT + FCSS provide all bus power; SCEB available for pulse only | Declare PAN PAN; expedite landing; no further regen capability | 65 % |
| DM-3 | FCSS fault (stack failure or H₂ loss) | 400 kW FCSS | Isolate FCSS; VCGT primary; SSBP supplement | Monitor H₂; FCSS restart if H₂ available and temp permits; continue flight | 75 % |
| DM-4 | Single VCGT fault | 1 × 1 200 kW VCGT | Isolate faulted VCGT; remaining VCGT at max; SSBP + FCSS supplement | Reduce cruise speed if required; dispatch per MEL-084-VCGT | 70 % |
| DM-5 | Both VCGT faulted | 2 × 1 200 kW VCGT | Full electric mode; FCSS + SSBP + SCEB only | Declare MAYDAY; divert to nearest suitable airport; limit to 60 min max | 45 % (FCSS + SSBP limited) |
| DM-6 | BGSCU Lane A fault | 1 BGSCU lane | Lane B promoted to active within 10 ms; QPU offline (classical fallback) | No crew action required (auto); monitor BGHA MFD for Lane B status | 100 % (sub-optimal dispatch) |

---

## §4 Reconfiguration Logic

**Automatic reconfiguration (BGSCU authority):**
The BGSCU automatically isolates a faulted source by commanding the corresponding BTB open and BDCC shutdown within 50 ms of fault detection. The mode state machine transitions to M7 (Degraded) and the appropriate DM is entered. The BGSCU selects the new dispatch strategy from the degraded-mode dispatch table (pre-computed offline) within one MPC cycle (20 ms).

**Manual reconfiguration:**
If the BGSCU itself commands an incorrect isolation (spurious fault), the crew can override via the BGHA OVERRIDE panel (guarded, amber cover) using discrete switches to command BTB open/close and BDCC enable/disable. Manual override is logged and requires maintenance action before next flight.

**BGSCU authority limits in degraded modes:**
- DM-1 through DM-4: BGSCU retains full authority over remaining sources.
- DM-5 (both VCGT lost): BGSCU restricts total bus power to FCSS + SSBP rated capacity (800 kW); SCEB available for 500 ms pulses only.
- DM-6 (BGSCU lane fault): Classical fallback with 3 % higher fuel burn; QPU remains offline until maintenance reset.

---

## §5 Redundancy Architecture

| Component | Redundancy Method | Switchover Time | BGHA Mode Affected |
|---|---|---|---|
| BGSCU | Dual-lane hot standby (Lane A + Lane B) | < 10 ms | DM-6 |
| SSBP | 2 independent packs (A and B) | Immediate (BTB isolation) | DM-1, DM-2 |
| FCSS | 8 stacks; any 4 stacks sufficient for 200 kW | Stack-level isolation; 30 s reconfig | DM-3 |
| VCGT | 2 independent turbines with separate ATRUs | Immediate (BTB isolation) | DM-4, DM-5 |
| SCEB | Single unit; no internal redundancy | N/A (single unit) | Loss of pulse buffer |
| BGHA-TML pump | 2 redundant EGW pumps | Automatic switchover 5 s | No propulsion mode change |
| HVDC Bus-800 | 4 segments (S1–S4) with BTBs | BTB open in 5 ms | Segment loss; partial load shed |

---

## §6 FMEA Summary — Top 10 Failure Modes

| # | Failure Mode | Failure Effect | Severity | Detection | Mitigation |
|---|---|---|---|---|---|
| 1 | SSBP Pack A thermal runaway | Fire; bus isolation | Catastrophic | BMS cell temp > 80 °C; smoke detector | Novec 1230 suppression; BDCC-A isolation within 50 ms; DM-1 |
| 2 | VCGT-1 shaft failure | Loss of 1 200 kW | Hazardous | ATRU output drop; shaft speed sensor | DM-4; VCGT-2 takes load |
| 3 | FCSS H₂ line rupture | H₂ release; potential fire | Hazardous | H₂ sensor in FCSS bay; pressure drop | FCSS isolation; SOV close; DM-3; ventilation |
| 4 | BGSCU Lane A processor fault | Loss of MPC optimality | Major | Watchdog timeout; cross-lane compare | Lane B takeover in 10 ms; DM-6 |
| 5 | BDCC-C (FCSS boost) open-circuit | Loss of FCSS output | Major | Bus voltage drop; FCSS current to zero | DM-3; VCGT + SSBP compensate |
| 6 | QPU decoherence event | MPC sub-optimal or timeout | Minor | QPU error rate > 0.05 | Classical fallback within 20 ms |
| 7 | SCEB BDCC-D shoot-through | Bus-800 short spike | Major | IMU; BDCC-D overcurrent | BDCC-D self-protected crowbar; BTB isolates if bus fault persists |
| 8 | Bus-800 ground fault | Leakage current; potential for arc | Major | IMU insulation resistance < 100 kΩ | IMU alert; fault location; BTB segment isolation |
| 9 | ATRU-1 diode short | DC component on VCGT AC output | Major | ATR output harmonic monitor | ATRU-1 isolated; VCGT-1 off; DM-4 |
| 10 | BGHA-TML pump A failure | Coolant flow reduction | Minor | Flow sensor; temperature rise | Pump B auto-start; crew advisory |

---

## §7 MEL Cross-Reference

| MEL Item | Component | Max Dispatch Condition | Required Op Procedure |
|---|---|---|---|
| MEL-084-SSBP-A | SSBP Pack A inoperative | 10 days; DM-1 rules apply | BGSCU DM-1 selected pre-flight; SSBP-A BTB verified open; reduced range ops |
| MEL-084-SSBP-B | SSBP Pack B inoperative | 10 days; DM-1 rules apply | As MEL-084-SSBP-A (mirror) |
| MEL-084-SSBP-AB | Both SSBP packs inoperative | No dispatch (DM-2; 45 % thrust insufficient for takeoff) | Aircraft on ground; maintenance required |
| MEL-084-FCSS | FCSS inoperative | 10 days; DM-3 rules; H₂ system depressurised | FCSS isolated; H₂ SOV closed; reduced zero-emission capability |
| MEL-084-VCGT1 | VCGT-1 inoperative | 5 days; DM-4 rules | VCGT-1 fuel isolated; ATRU-1 BTB open; VCGT-2 at max continuous |
| MEL-084-VCGT12 | Both VCGTs inoperative | No dispatch (DM-5; range insufficient) | Aircraft on ground |
| MEL-084-SCEB | SCEB inoperative | 10 days; no STOL ops | STOL boost inhibited; normal takeoff only |
| MEL-084-BGSCU-LB | BGSCU Lane B inoperative | 3 days; no redundancy | BGSCU Lane A only; QPU offline; classical dispatch |

---

## §8 Interfaces

| Interface | Connected System | Protocol | Data |
|---|---|---|---|
| Fault flags → BGSCU | All BDCCs; ATRUs; BMS | CAN ISO 11898 | Fault codes; overcurrent; temperature alarms |
| BTB commands | BTB (×4 plus source BTBs) | Hardwired discrete | Open/close command; position feedback |
| DM status → CMS | CMS — ATA 45 | AFDX VL-084-02 | Active DM ID; thrust available %; maintenance code |
| DM status → cockpit | ECAM / MFD (BGHA synoptic) | AFDX (via BGSCU) | Amber/red source bars; DM ID; advisory messages |
| MEL data | Crew Electronic Flight Bag (EFB) | Offline document | Pre-flight dispatch check |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-084-060-001 | DM-2 (both SSBP lost) thrust level — flight test verification of 65 % figure | Q-GREENTECH | Phase 2 |
| OI-084-060-002 | FMEA items 1 and 3 (SSBP TR, FCSS H₂ rupture) — FHA classification review | Q-STRUCTURES | PDR |
| OI-084-060-003 | SCEB BDCC-D shoot-through energy — busbar arc flash energy calcs | Q-INDUSTRY | CDR |
| OI-084-060-004 | MEL-084-VCGT12 dispatch prohibition — confirm consistent with CS-25.1309 safety assessment | Q-GREENTECH | PDR |
