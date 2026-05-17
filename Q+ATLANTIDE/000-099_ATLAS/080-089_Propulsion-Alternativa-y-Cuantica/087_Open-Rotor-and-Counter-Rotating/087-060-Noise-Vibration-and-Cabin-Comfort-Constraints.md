---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-087-060-NOISE-VIBRATION-AND-CABIN-COMFORT-CONSTRAINTS"
register: ATLAS-1000
title: "Noise, Vibration and Cabin Comfort Constraints"
ata: "ATLAS-087 (Open Rotor and Counter-Rotating)"
sns: "087-060-00"
subsection: "087"
subsubject_code: "060"
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
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0087-060"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-087-060-NOISE-VIBRATION-AND-CABIN-COMFORT-CONSTRAINTS
     ATLAS-087 (Open Rotor and Counter-Rotating) · Noise, Vibration and Cabin Comfort Constraints
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Noise, Vibration and Cabin Comfort Constraints

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-087 Open Rotor](https://img.shields.io/badge/ATLAS--087-Open%20Rotor%20%26%20Counter--Rotating-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-HORIZON](https://img.shields.io/badge/Q--Division-Q--HORIZON-purple)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Noise, Vibration and Cabin Comfort Constraints`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 Far-Field Noise Certification Targets

| Measurement Point | ICAO Ch14 Limit (EPNdB) | [PROGRAMME-AIRCRAFT] Design Target | Margin |
|---|---|---|---|
| Take-off (TOGA, 6 500 m downtrack) | 88.0 | 84.5 | −3.5 EPNdB |
| Sideline (450 m offset, max-noise point) | 98.0 | 94.5 | −3.5 EPNdB |
| Approach (2 000 m from threshold) | 105.0 | 101.5 | −3.5 EPNdB |
| Cumulative (all three points) | ≤ ICAO sum | −10.5 EPNdB cumulative | +10.5 EPNdB |

---

## §3 Dominant Noise Sources and Budget

| Source | Mechanism | Primary Frequency | EPNdB Contribution | Mitigation |
|---|---|---|---|---|
| FR–AR blade-passing interaction (BPI) tone | Potential field interaction + wake impingement | 2 × BPF (≈ 283 Hz at cruise) | Largest contributor | Active clocking, axial spacing, blade count ratio |
| FR blade-loading broadband | Turbulence ingestion + boundary layer | Broadband 200–3 000 Hz | Secondary | Sweep, t/c, inlet turbulence screen |
| FR tip-vortex noise | Tip-vortex / AR leading-edge interaction | Broadband 500–5 000 Hz | Moderate | Reduced tip loading (outer 15 % span) |
| DPGB gear-mesh tones | Mechanical radiation through nacelle | Stage 1 mesh: ~5 040 Hz; Stage 2: ~3 800 Hz | Minor | Gearbox isolation mounts + nacelle attenuation panels |
| Tail-cone turbulence | Aft-fuselage boundary-layer ingestion by FR | Broadband low-frequency | Minor | Pylon fairing, BL trip |

---

## §4 Interior Cabin NVH Constraints

The aft position of the ORCR propulsors means that the primary noise coupling path is through the fuselage aft bulkhead and aft-section sidewalls. The design targets are:

| Zone | Interior SPL Target (A-weighted) | Primary Frequency Concern | Design Measure |
|---|---|---|---|
| Aft cabin (rows 30–40) | ≤ 78 dB(A) in cruise | BPI tone + DPGB mesh tones | Damped rib frames, constrained-layer damping (CLD) on aft skins |
| Mid cabin (rows 15–29) | ≤ 75 dB(A) in cruise | Structural-borne BPI | Active noise control (ANC) panels — 24 speaker ANC array |
| Forward cabin (rows 1–14) | ≤ 73 dB(A) in cruise | Residual broadband | Standard acoustic blankets |
| Cockpit | ≤ 70 dB(A) in cruise | Engine/airframe mix | Standard isolation + headset |

### Active Noise Control (ANC) System

The mid-cabin ANC system uses 24 loudspeaker actuators embedded in the overhead panels and 32 microphone error sensors in the seat-back arrays. The ANC controller (ANC-CTRL) is an FPGA-based digital signal processor running a filtered-x LMS algorithm with 50 ms update rate, targeting cancellation of the BPI tone and first two harmonics (283, 566, 849 Hz) in the mid-cabin volume.

| ANC Parameter | Value |
|---|---|
| Number of actuators | 24 |
| Number of error microphones | 32 |
| Target tones | BPI × 1, 2, 3 (283, 566, 849 Hz) |
| Expected BPI tone attenuation | ≥ 12 dB (primary tone) |
| ANC controller qualification | DAL D (passenger comfort system) |

---

## §5 Structural Vibration Transmission and NVH Design Measures

| Measure | Application | Expected Benefit |
|---|---|---|
| DPGB soft-mount isolators (elastomeric) | DPGB to nacelle hard mount | Isolates gear-mesh frequencies above 100 Hz; ≥ 25 dB insertion loss |
| Constrained-Layer Damping (CLD) panels | Aft fuselage skins FS 2100–2250 | 5–8 dB reduction in structural-borne BPI radiation |
| Tuned Vibration Absorbers (TVAs) | Aft bulkhead ribs at BPI frequency (283 Hz) | 6–10 dB reduction at BPI tone |
| Acoustic blankets (mass-spring-mass) | Aft cabin sidewalls and ceiling | 20 dB TL improvement at 200–2 000 Hz |
| Pylon vibration isolation mounts | Pylon-to-fuselage attachment fittings | Limit transmission of BPI and gear tones into fuselage spine |

---

## §6 Vibration Levels and Limits

| Location | Vibration Level (cruise, 1/3 octave RMS) | Limit | Standard |
|---|---|---|---|
| DPGB housing (gear-mesh) | ≤ 2 g peak at gear-mesh frequency | 5 g peak | DPGB design spec |
| Engine nacelle external | ≤ 0.5 g RMS (10–200 Hz) | 1.0 g RMS | CS-25.251 |
| Aft fuselage structure | ≤ 0.1 g RMS at BPI frequency | 0.15 g RMS | Cabin comfort spec |
| Cabin floor (aft zone) | ≤ 0.05 g RMS | 0.08 g RMS | ISO 2631-1 |
| Cockpit floor | ≤ 0.02 g RMS | 0.05 g RMS | CS-25.251 |

---

## §7 Noise Monitoring and Reporting

The ORSCU includes a real-time noise-state estimator that uses the blade-pitch angle, rotor speed, and atmospheric data to compute an estimated BPI tone level at the ICAO certification measurement points. This estimated noise state is:

- Displayed on the EFIS/MFD noise page (advisory only)
- Logged to the FDR for noise compliance reporting
- Used by the active acoustic clocking algorithm to trim FR–AR phase for minimum noise

---

## §8 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-087-060-001 | ANC system integration test in fuselage section — validate 12 dB BPI tone attenuation | Q-HORIZON | CDR |
| OI-087-060-002 | CLD mass budget allocation (aft fuselage CLD ≈ 85 kg) — confirm payload impact acceptance | Q-STRUCTURES | PDR |
| OI-087-060-003 | DPGB isolation mount stiffness optimisation — trade-off noise isolation vs. rotor dynamic stability | Q-INDUSTRY | CDR |
| OI-087-060-004 | EC 598/2014 airport noise charging — confirm ORCR APD (Aircraft Performance Data) submission format | Q-GREENTECH | PDR |
