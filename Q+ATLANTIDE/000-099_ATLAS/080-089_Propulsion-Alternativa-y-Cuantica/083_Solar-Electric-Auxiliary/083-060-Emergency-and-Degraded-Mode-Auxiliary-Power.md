---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-083-060-EMERGENCY-AND-DEGRADED-MODE-AUXILIARY-POWER"
register: ATLAS-1000
title: "Emergency and Degraded Mode Auxiliary Power"
ata: "ATLAS-083 (Solar-Electric Auxiliary)"
sns: "083-060-00"
subsection: "083"
subsubject_code: "060"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HORIZON, Q-HPC, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0083-060"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-083-060-EMERGENCY-AND-DEGRADED-MODE-AUXILIARY-POWER
     ATLAS-083 (Solar-Electric Auxiliary) · Emergency and Degraded Modes
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Emergency and Degraded Mode Auxiliary Power

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

ATLAS subsubject 083-060 defines the five degraded and emergency operating modes of the Solar-Electric Auxiliary (SEA) system, including FMEA summary, SEACU channel failover, single propulsor failure response, and total SEA failure graceful shutdown. It provides the failure mode analysis baseline and CS-25.1309 compliance rationale for the SEA research system.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA reference | ATLAS-083 — 083-060 Emergency and Degraded Mode Auxiliary Power |
| Certification basis | EASA CS-25.1309 (equipment, systems and installations — research platform analogue); DO-178C DAL C; AMC 25.1309 |
| S1000D SNS | 083-060-00 |

---

## §3 Degraded Mode Summary

| Mode | Designation | Trigger | SEA System State |
|---|---|---|---|
| DM-1 | Solar-Only (no battery) | Battery BMS fault / relay open | PV + SCAP → propulsors at ≤ 40 % throttle |
| DM-2 | Battery-Only (no solar) | Cloud/night + MPPT harvest < 5 kW | Battery + SCAP → propulsors at ≤ 40 % throttle (30 min endurance) |
| DM-3 | SEACU Channel A Failure | SEACU CHA internal fault | Automatic changeover to CHB ≤ 100 ms; thrust −50 % for 2 s |
| DM-4 | Single Propulsor Failure | Propulsor motor fault / inverter fault | Power redistributed to remaining propulsors; FCS asymmetric trim advisory |
| DM-5 | Total SEA Failure | SEACU dual-channel fault or FIRE emergency | All propulsors shutdown; battery → HVDC 270 V bus for essential loads only |

---

## §4 Mode DM-1 — Solar-Only (No Battery)

**Trigger:** Battery BMS fault (L3 or L4) or battery manual isolation (LOTO).

**SEA behaviour:**
- SEACU disconnects battery via MSD / relay; battery BMS relay open
- MPPT continues harvesting from PV arrays
- SCAP provides transient buffering as normal
- Propulsor throttle limit set to 40 % (80 kW harvest − losses = 72 kW; 2× propulsors at 36 kW each)
- Surplus solar still exported to HVDC 270 V bus (up to 50 kW)
- SEACU publishes DM-1 status to CMS ATA 45 (fault advisory, not warning)
- Crew advisory: "SEA BATTERY INOP — SOLAR ONLY"

**Performance in DM-1:** Full solar-augmented cruise capability retained; emergency backup (Role B) capability lost.

---

## §5 Mode DM-2 — Battery-Only (No Solar)

**Trigger:** Irradiance < 200 W/m² (cloud cover, night); MPPT harvest < 5 kW on all 6 channels.

**SEA behaviour:**
- MPPT converters reduce duty cycle; output drops to zero
- Battery sustains propulsors at 40 % throttle (40 kW total = 20 kW per propulsor)
- SCAP continues buffering propulsor transients
- SEACU energy arbitrator computes remaining endurance from SoC; publishes to ECAM
- At SoC = 25 %: SEACU reduces propulsors to 20 % throttle (20 kW) — "SEA LOW BATTERY" advisory
- At SoC = 22 %: SEACU shuts down propulsors; battery reserved for HVDC 270 V bus emergency backup
- Crew advisory: "SEA BATTERY ONLY — X MIN REMAINING" (computed endurance)

**Endurance budget (DM-2):**
- 50 kWh usable × 0.68 (SoC 20–90 % window) × 0.96 (inverter η) = **31.9 kWh at propulsors**
- At 40 kW total: 31.9 kWh / 40 kW = **47 min** endurance
- Reserve (SoC 20–22 %): 1 kWh → available for essential bus (not propulsors)

---

## §6 Mode DM-3 — SEACU Channel A Failure

**Trigger:** SEACU CHA internal fault (watchdog timeout, power supply fault, BITE failure detected).

**Changeover sequence (automatic, ≤ 100 ms):**
1. CHA BITE detects fault → asserts CHB_TAKEOVER line (hardware, < 1 ms)
2. CHB transitions from hot-standby to active (power supply already on, software synchronised via crosslink)
3. CHB assumes all MPPT command, power arbitration, and inverter control functions
4. Thrust reduced to 50 % for 2 s during AFDX handover (VL-083-01 to VL-083-06 re-initialised)
5. Normal thrust restored after 2 s if no further fault
6. SEACU CHA fault logged; CMS ATA 45 BITE message generated
7. Crew advisory: "SEACU CHAN A FAULT — CHAN B ACTIVE"

**Post-changeover capability:** Full SEA capability on CHB; maintenance action required before next flight (CHA LRU replacement or reset).

---

## §7 Mode DM-4 — Single Propulsor Failure

**Trigger:** BLI propulsor motor fault (over-temperature, bearing failure, stall), or SiC inverter fault (SSPC trip), or propulsor BITE fault.

**SEA behaviour:**
- Affected propulsor SSPC trips; inverter gate signals inhibited within 2 µs
- SEACU reassigns available power to remaining operational propulsor(s)
- If 2 propulsors and 1 fails: remaining propulsor receives full 80 kW budget; net thrust asymmetry = 520 N on one side
- FCS receives asymmetric thrust advisory via AFDX VL-083-03; FCS applies rudder/aileron trim
- SEACU logs failed propulsor ID and fault code; publishes to CMS
- Crew advisory: "SEA PROPULSOR [L/R] FAULT — ASYMMETRIC THRUST"
- No structural hazard: BLI propulsor thrust level (520 N per unit) is low compared to primary turbofan (> 100 kN); asymmetric yaw moment is within FCS trim authority

---

## §8 Mode DM-5 — Total SEA Failure

**Trigger:** SEACU dual-channel fault (both CHA and CHB), or FIRE/ELEC emergency signal from CMS.

**SEA behaviour:**
1. All propulsor SSPCs trip (all SSPC-083-01 through -04); propulsors coastdown
2. MPPT converter outputs inhibited; PV arrays effectively open-circuited (MPPT gate signals off)
3. SCAP bleed resistor activated; SCAP voltage discharges to < 50 V in ≤ 60 s
4. Battery bidirectional DC/DC converter switches to emergency export mode: 20 kW to HVDC 270 V bus (essential loads)
5. SEACU FIRE logic: if FIRE signal received, battery relay also opens → full SEA isolation
6. HVDC 270 V bus maintained from main generator chain (ATLAS 073 / 072 / 075)
7. No degradation of primary propulsion (FADEC unaffected)
8. Crew advisory: "SEA TOTAL FAILURE — BATTERY ISOLATED" (if FIRE); or "SEA INOP" (if dual-channel fault)

---

## §9 FMEA Summary

| Failure Mode | Effect on SEA | Effect on Aircraft | Severity | Probability | Mitigation |
|---|---|---|---|---|---|
| Single MPPT converter failure | −20 kW harvest (1/6 channels) | Reduced solar contribution | Minor | Probable | 5 remaining channels; SEACU advisory |
| Single PV string short circuit | String bypass diode conducts; −180 W (1 panel) | Negligible | Negligible | Probable | Bypass diodes per sub-string |
| SCAP contactor failure (open) | No fast buffering | Propulsor transients on DC link; inverter voltage ripple | Major | Remote | Inverter DC link cap absorbs 200 ms; SEACU reduces throttle rate |
| Battery BMS relay failure (closed) | Battery cannot be isolated | DM-1 mode (solar only) | Hazardous | Extremely Remote | Battery MSD; Novec 1230 backup |
| SEACU CHA failure | Changeover to CHB (DM-3) | −50 % thrust for 2 s | Minor | Remote | Hot-standby CHB; 100 ms changeover |
| SEACU dual-channel failure | Total SEA failure (DM-5) | SEA INOP; no primary propulsion effect | Minor | Extremely Improbable | Dual-channel + independent power supply per channel |
| BLI propulsor motor over-temperature | Propulsor trip (DM-4) | Asymmetric thrust (520 N) | Minor | Remote | Thermal protection; FCS trim authority |

---

## §10 CS-25.1309 Compliance Rationale

The SEA system is a **research augmentation layer** at DAL C. Primary propulsion (FADEC, turbofans) is independent of SEA. Total SEA failure (DM-5) is classified as a **Minor** failure condition (no effect on primary propulsion, no effect on aircraft controllability). Per CS-25.1309 AMC Table 1, Minor failure conditions require a probability of ≤ 10⁻³ per flight hour — satisfied by the SEACU dual-channel architecture and independent power supply.

Emergency backup power (Role B) is classified as a **supplemental capability** — its loss is classified as Minor. The primary emergency power system (RAT, APU, ATLAS 072 battery) is unaffected by SEA failure.

---

## §11 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-083-060-001 | Quantitative FMEA (failure probability per flight hour) for SEACU dual-channel vs. CS-25.1309 targets | Q-HORIZON | PDR |
| OI-083-060-002 | FCS asymmetric thrust trim authority demonstration for DM-4 (1 propulsor at 520 N full power) | Q-HPC | CDR |
| OI-083-060-003 | Battery emergency export mode (DM-5, 20 kW to HVDC bus) qualification — interaction with ATLAS 073 SSPCs | Q-INDUSTRY | CDR |
