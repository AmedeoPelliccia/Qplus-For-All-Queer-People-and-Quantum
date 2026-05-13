---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-086-030-FAN-PROPULSOR-AND-DISTORTION-TOLERANCE"
register: ATLAS-1000
title: "Fan-Propulsor and Distortion Tolerance"
ata: "ATLAS-086 (Boundary Layer Ingestion Propulsion)"
sns: "086-030-00"
subsection: "086"
subsubject_code: "030"
primary_q_division: Q-HORIZON
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-HPC]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0086-030"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-086-030-FAN-PROPULSOR-AND-DISTORTION-TOLERANCE
     ATLAS-086 (Boundary Layer Ingestion Propulsion) · Fan-Propulsor and Distortion Tolerance
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Fan-Propulsor and Distortion Tolerance

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-086 BLI Propulsion](https://img.shields.io/badge/ATLAS--086-BLI%20Propulsion-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-HORIZON](https://img.shields.io/badge/Q--Division-Q--HORIZON-blue)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

ATLAS subsubject 086-030 defines the aerodynamic design, distortion tolerance specification, speed range, and mechanical architecture of the BLI fan-propulsor stage. It also covers the distortion tolerance assessment methodology and qualification test plan for the fan operating in degraded inlet conditions.

---

## §2 Fan Stage Overview

| Parameter | Value |
|---|---|
| Fan diameter | 1.15 m |
| Fan pressure ratio (FPR) design point | 1.35 at M 0.78 |
| Fan rotor speed range | 3 000–6 500 RPM |
| Drive arrangement | Gearless direct-drive PMSM |
| Fan mass flow (design point) | 85 kg/s per propulsor |
| Fan efficiency (adiabatic, design point) | ≥ 90 % |
| Blade count — rotor | 18 (wide-chord swept) |
| Blade count — OGV (outlet guide vane) | 28 |
| Blade material | Ti-6Al-4V + CFRP leading-edge insert |
| Containment casing material | Ti-6Al-4V ring + CFRP overwrap |

---

## §3 Distortion Tolerance Design

### 3.1 DC60 Tolerance Requirement

The BLI fan stage is designed to maintain stall-free operation at inlet total pressure distortion indices (DC60) up to **0.35** across the full operating envelope. The design strategy employs three parallel mechanisms:

1. **Wide-chord swept blades:** Blade chord-to-span ratio 0.35 (wide-chord) and leading-edge sweep of 28° forward suppresses propagation of inlet distortion into rotating stall cells.
2. **Variable-frequency drive (VFD) speed modulation:** The MCU-086 VFD adjusts fan speed within ±10 % of the scheduling setpoint at ≤ 20 ms response, trimming the operating line away from the stall limit when elevated DC60 is detected by the TPR rake.
3. **Passive OGV clocking optimisation:** OGV angular position is fixed at the manufacturing stage to provide maximum stall margin at the cruise design point; re-clocking may be applied at major maintenance intervals per SB.

### 3.2 Stall Margin Map vs. DC60

| DC60 | Fan Speed (RPM) | Stall Margin (%) | Action |
|---|---|---|---|
| 0.00–0.20 | 5 500–6 200 | 18–22 | Normal BLI operation |
| 0.21–0.28 | 5 200–5 500 | 16–18 | BLICU speed trim active |
| 0.29–0.35 | 4 500–5 200 | 15–16 | BLICU caution; speed trim max |
| > 0.35 | Reduction to idle | — | BLICU activates bypass door; BLI off |

---

## §4 PMSM and Drive Architecture

| Parameter | Value |
|---|---|
| Motor type | Permanent-Magnet Synchronous Motor (PMSM) |
| Rated power | 120 kW continuous; 135 kW peak (30 s) |
| Supply voltage | HVDC 270 V from MCU-086 |
| Motor efficiency (120 kW) | ≥ 96.5 % |
| Control law | Field-Oriented Control (FOC) with active torque ripple suppression |
| Motor speed | Direct-coupled to fan; 3 000–6 500 RPM |
| Winding insulation class | Class H (180 °C max) |
| Cooling | Forced air cooling — fan rotor back-flow provides cooling airflow through stator slots |
| Encoder | Redundant resolver (2× per motor); 12-bit |
| IP rating | IP65 |

### 4.1 Torque Ripple Suppression

The MCU-086 FOC algorithm implements a **6th and 12th harmonic current injection** scheme to suppress the dominant torque harmonics. Target torque ripple peak-to-peak < 1.5 % at rated speed. This limits structural excitation of the aft fuselage frame to levels below the duct modal damping threshold (see ATLAS-086-060).

---

## §5 Fan Map and Operating Line

```mermaid
flowchart LR
    SURGE[Surge Line\n(Stall boundary)] --- SM[Stall Margin ≥ 15 %]
    SM --- OL[Operating Line\n(Design points)]
    OL --- CHOKE[Choke Line]
    OL --> DP_TO[TO point\n3000 RPM / FPR 1.08]
    OL --> DP_CL[Climb point\n5000 RPM / FPR 1.25]
    OL --> DP_CR[Cruise point\n6000 RPM / FPR 1.35]
```

---

## §6 Fan Mechanical Design Details

### 6.1 Blade Root Attachment

- Dovetail root slot machined in Ti-6Al-4V fan disk.
- Blade fir-tree not used (1.15 m fan insufficient disc rim space).
- Blade retention via single radial retaining pin + anti-rotation lug.
- Blade root inspection access at B-check (visual + dye penetrant).

### 6.2 Tip Clearance

| Operating Condition | Tip Clearance (mm) | Notes |
|---|---|---|
| Cold assembly | 1.80 | Nominal assembly clearance |
| Hot running (cruise) | 1.10 | Thermal growth closes ~0.70 mm |
| Minimum permissible | 0.70 | Hard limit — replace casing if worn below |

### 6.3 Containment

Fan casing containment certified to **CS-25.904 IBR-2** (uncontained blade release, one blade). The Ti-6Al-4V ring + CFRP overwrap design absorbs kinetic energy of a 1.15 m-diameter, Ti-6Al-4V blade fragment without penetration of the fuselage pressure vessel. Blast panel provided on outer casing for decompression venting.

---

## §7 Fan Stage Qualification Tests

| Test | Standard | Test Rig | Pass Criteria |
|---|---|---|---|
| Distortion tolerance rig test (DC60 sweep) | AC 20-128A; in-house spec | BLI-FAN-RIG-01 (full-scale rig) | Stall-free at DC60 ≤ 0.35 across all speed lines |
| Aerodynamic performance map | AIR 1419B | BLI-FAN-RIG-01 | FPR ≥ 1.35 at η ≥ 90 % at design point |
| Blade-off containment | CS-25.904 | Containment test cell | No fragment exits Ti ring + CFRP overwrap |
| Bird ingestion (1.8 kg) | AC 33.76; CS-25.775 | Bird ingestion test cell | No uncontained failure; continued rotation post-event |
| Vibration and resonance | DO-160G Cat F | Vibration table + spin rig | No resonance below 130 % of max speed (Campbell) |
| Fatigue (HCF) | ASTM E466 | Component test | 10⁷ cycles at maximum alternating load |

---

## §8 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-086-030-001 | Full-scale fan rig test facility booking — BLI-FAN-RIG-01 availability | Q-HORIZON | PDR |
| OI-086-030-002 | Blade CFRP leading-edge insert bond qualification — environmental (icing, hail) | Q-STRUCTURES | CDR |
| OI-086-030-003 | OGV clocking optimisation — adjoint sensitivity study scope | Q-HORIZON | PDR |
| OI-086-030-004 | Containment casing material down-select: Ti-6Al-4V ring vs. CFRP monolithic | Q-STRUCTURES | Phase 2 |
