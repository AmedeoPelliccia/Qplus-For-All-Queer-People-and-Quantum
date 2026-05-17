---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-083-010-SOLAR-ELECTRIC-AUXILIARY-BASELINE-AND-SCOPE"
register: ATLAS-1000
title: "Solar-Electric Auxiliary Baseline and Scope"
ata: "ATLAS-083 (Solar-Electric Auxiliary)"
sns: "083-010-00"
subsection: "083"
subsubject_code: "010"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HORIZON, Q-HPC, Q-STRUCTURES]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0083-010"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-083-010-SOLAR-ELECTRIC-AUXILIARY-BASELINE-AND-SCOPE
     ATLAS-083 (Solar-Electric Auxiliary) · Baseline and Scope
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Solar-Electric Auxiliary Baseline and Scope

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

This document defines the agnostic ATLAS standard-level architecture context for `Solar-Electric Auxiliary Baseline and Scope`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 Applicability

| Applicability Level | Rule |
|---|---|
| Standard taxonomy | Applies to the ATLAS node `083` |
| Programme implementation | Conditional; determined by programme architecture, trade studies, certification basis, and applicability model |
| Product configuration | Defined in the programme-specific configuration baseline |
| Effectivity | Defined in the programme CSDB / applicability layer |
| Non-applicability | Must be explicitly stated in the programme impact-study branch when excluded |
## §3 Mission Trade Space

The SEA programme targets three operational roles for the programme-defined aircraft type research platform:

**Role A — Solar-Augmented Cruise (SAC):** PV harvest supplements the HVDC 270 V bus at cruise altitude (FL350, M 0.78), offloading generator demand by up to 120 kW and driving BLI propulsor nodes. Net benefit: estimated 3–5 % block-fuel reduction on 3 000 NM long-range mission.

**Role B — Emergency Backup Power (EBP):** In the event of main generator failure, the 50 kWh Li-Ion battery subset and residual solar harvest sustain essential loads (avionics, lighting, FCS) and limited auxiliary propulsion for up to 30 min, providing sufficient time to divert to an alternate.

**Role C — Research Characterisation (RC):** Dedicated flight test segments characterise PV array in-flight harvest versus irradiance model predictions, MPPT algorithm performance under partial shading, BLI fan propulsive efficiency, and SCAP charge/discharge cycling behaviour for Phase 2 programme decisions.

### 3.1 Technology Selection Summary

| Technology | Role | Power Range | Key Advantage | Key Risk |
|---|---|---|---|---|
| GaAs Triple-Junction PV | A, B, C | 0–120 kW harvest | η = 31 %, radiation-hard, low mass | High cell cost; CTE mismatch with CFRP |
| CIGS Thin-Film PV | A, C | 0–80 kW harvest | Lower cost; flexible laminate | η = 18 %; lower harvest at altitude |
| Monocrystalline Si PV | A | 0–90 kW harvest | Mature supply chain | η = 24 %; heavier; temperature coefficient worse |
| Maxwell-type Supercapacitor | A, B, C | ±200 kW / 0.5 s | Unlimited cycle life; high power density | Low energy density (100 kJ vs. MJ for battery) |
| <BATTERY-CHEMISTRY> Li-Ion Battery | B, C | 50 kWh sustained | High energy density; proven technology | Thermal runaway risk; cycle life limited |

**Selected technologies:** GaAs TJ PV cells + Maxwell-type SCAP (transient buffer) + <BATTERY-CHEMISTRY> Li-Ion subset (sustained backup).

---

## §4 Performance Baseline

| Parameter | Minimum (Design Floor) | Target | Stretch Goal |
|---|---|---|---|
| PV array active area | 18 m² | 24 m² | 32 m² |
| Peak solar harvest (FL350, clear sky) | 80 kW | 120 kW | 160 kW |
| MPPT efficiency | 96 % | 98 % | 99 % |
| SCAP energy buffer | 60 kJ | 100 kJ | 150 kJ |
| Li-Ion battery backup capacity | 30 kWh | 50 kWh | 80 kWh |
| HVDC 270 V bus tie power | ±40 kW | ±80 kW | ±120 kW |
| BLI propulsor total power | 40 kW | 80 kW (2×40 kW) | 160 kW (4×40 kW) |
| BLI propulsive efficiency improvement | 4 % | 8 % | 12 % |
| Block-fuel reduction (Role A, 3 000 NM) | 2 % | 4 % | 6 % |
| Emergency backup duration (Role B) | 20 min at 20 kW | 30 min at 40 kW | 45 min at 60 kW |

---

## §5 Solar Harvest Model

| Altitude | Irradiance (W/m²) | Array Harvest (kW) | MPPT Loss (%) | Net Electrical (kW) |
|---|---|---|---|---|
| SL (AMO ground) | 1 000 | 74.4 | 2 | 72.9 |
| FL100 | 1 200 | 89.3 | 2 | 87.5 |
| FL250 | 1 320 | 98.2 | 2 | 96.2 |
| FL350 (design point) | 1 350 | 100.5 | 2 | 98.5 |
| FL350 (optimal angle) | 1 350 × cos(5°) | 120 kW (corrected for cell temp −0.3 %/°C below STC at altitude) | 2 | **117.6** |

> **Note:** Cell temperature at FL350 in cruise is approximately 20 °C below STC (25 °C), increasing efficiency by 0.3 %/°C × 5 °C = +1.5 %, partially offsetting incidence angle loss.

---

## §6 Power Budget

| Consumer | Nominal (kW) | Peak (kW) | Source |
|---|---|---|---|
| 2× BLI Propulsor Nodes (Role A cruise) | 60 | 80 | PV + SCAP |
| SEACU internal losses (η = 0.97) | 2 | 3 | — |
| HVDC 270 V bus export (surplus solar) | 50 | 80 | PV → HVDC bus |
| Emergency avionics loads (Role B) | 20 | 30 | Battery |
| **Total peak SEACU input from PV** | **112** | **120** | PV arrays |

> All roles are **not operated simultaneously at maximum**. Peak simultaneous draw is Role A (BLI) + HVDC export = 112 kW, within the 120 kW harvest ceiling.

---

## §7 Technology Readiness Levels (TRL)

| Technology | Current TRL | Target TRL (Phase 2) | Limiting Factor |
|---|---|---|---|
| GaAs TJ PV on CFRP aircraft skin (conformal laminate) | TRL 4 (sub-scale ground demo) | TRL 6 (aircraft ground test) | CTE mismatch; aerodynamic step; DO-160G lightning |
| 6-channel MPPT airborne system | TRL 5 (commercial derived) | TRL 7 (flight qualified) | Altitude EMC qualification; partial shading algorithm |
| SCAP bank (700 V, 100 kJ, airborne) | TRL 4 (ground lab prototype) | TRL 6 | DO-160G vibration qualification; weight budget |
| BLI PMSM propulsor (airborne, 40 kW) | TRL 5 (ground rig) | TRL 7 (flight test) | BLI duct bird-strike CS-25.631; noise certification |
| SEACU dual-channel DAL C | TRL 4 (concept design) | TRL 6 (CDR) | DAL C verification artefacts; AFDX interface qualification |

---

## §8 Interfaces

| Interface | Connected System | Protocol | Data |
|---|---|---|---|
| PV harvest input | 6× MPPT → SEACU DC link | MPPT boost converter, 700 V DC | Up to 120 kW solar energy |
| Main bus tie | HVDC 270 V — ATLAS 073 | HVDC bidirectional cable | ±80 kW export/import |
| Energy dispatch | EMS — ATLAS 079 | AFDX VL-083-02 | Power demand / state forecast |
| Propulsion advisory | FADEC — ATA 73 | AFDX VL-083-03 | SEA auxiliary thrust advisory |
| Battery interface | Li-Ion subset — ATLAS 072 BMS | CAN bus (internal) | SoC, SoH, temperature, charge/discharge |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-083-010-001 | Block-fuel reduction model validation against AEAC mission analysis tool | Q-GREENTECH | PDR |
| OI-083-010-002 | PV array area optimisation vs. aerodynamic drag penalty (step height study) | Q-STRUCTURES | PDR |
| OI-083-010-003 | SCAP vs. second Li-Ion battery trade for transient buffer — weight/cost/cycle-life analysis | Q-GREENTECH | CDR |
