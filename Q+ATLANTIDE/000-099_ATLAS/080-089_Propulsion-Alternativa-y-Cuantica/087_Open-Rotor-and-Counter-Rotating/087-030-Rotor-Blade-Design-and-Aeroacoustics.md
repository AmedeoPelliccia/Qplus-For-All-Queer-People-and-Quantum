---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-087-030-ROTOR-BLADE-DESIGN-AND-AEROACOUSTICS"
register: ATLAS-1000
title: "Rotor Blade Design and Aeroacoustics"
ata: "ATLAS-087 (Open Rotor and Counter-Rotating)"
sns: "087-030-00"
subsection: "087"
subsubject_code: "030"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-HORIZON, Q-GREENTECH, Q-HPC]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0087-030"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-087-030-ROTOR-BLADE-DESIGN-AND-AEROACOUSTICS
     ATLAS-087 (Open Rotor and Counter-Rotating) · Rotor Blade Design and Aeroacoustics
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Rotor Blade Design and Aeroacoustics

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-087 Open Rotor](https://img.shields.io/badge/ATLAS--087-Open%20Rotor%20%26%20Counter--Rotating-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-STRUCTURES](https://img.shields.io/badge/Q--Division-Q--STRUCTURES-orange)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Rotor Blade Design and Aeroacoustics`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 Blade Geometry

### 2.1 Forward Rotor (FR) Blade

| Parameter | Value |
|---|---|
| Blade count | 12 |
| Span (hub to tip) | 1.58 m |
| Root chord | 0.48 m |
| Tip chord | 0.18 m |
| Taper ratio | 0.375 |
| Leading-edge sweep (at 75 % span) | 35° (aft sweep) |
| Twist distribution | +12° (root-to-tip washout) |
| Design section (at 75 % span) | NACA 65-series modified (t/c = 8 %) |
| Platform planform | Scimitar (swept and leaned) |

### 2.2 Aft Rotor (AR) Blade

| Parameter | Value |
|---|---|
| Blade count | 10 |
| Span (hub to tip) | 1.45 m |
| Root chord | 0.44 m |
| Tip chord | 0.16 m |
| Taper ratio | 0.364 |
| Leading-edge sweep (at 75 % span) | 28° (aft sweep) |
| Twist distribution | +10° (root-to-tip washout) |
| Design section (at 75 % span) | NACA 65-series modified (t/c = 7 %) |
| Platform planform | Scimitar (slightly reduced sweep vs. FR) |

---

## §3 Blade Materials and Structural Design

| Layer / Component | Material | Notes |
|---|---|---|
| Structural spar | Titanium alloy Ti-6Al-4V | Hollow-section D-spar; manufactured by SLM additive |
| Outer shell (blade body) | CFRP T800/M21 (8-ply ±45°/0° layup) | Co-cured with spar |
| Leading-edge erosion shield | Titanium foil, adhesively bonded | Replaceable; 0.4 mm Ti-6Al-4V |
| Trailing edge insert | GFRP trailing-edge strip | Vibration damping; replaceable |
| De-icing (AR blades only) | Electro-thermal mat (Ni-Cr foil) | 80 W/dm²; powered from aircraft 28 V DC |
| SHM sensors | Fibre Bragg Grating (FBG) array × 8 per blade | Embedded in spar layup; connected to ORSCU health monitor |
| Blade root attachment | Dovetail Ti-6Al-4V with CFRP transition | Tapered dovetail; FOD tolerance per CS-25.571(e) |

---

## §4 Aerodynamic Performance Data

| Parameter | FR (design point) | AR (design point) |
|---|---|---|
| Advance ratio J (cruise) | 3.2 | 3.5 |
| Blade loading coefficient | 0.042 | 0.038 |
| Efficiency η at cruise | 88 % | 93 % swirl-recovery efficiency |
| Combined η_prop (FR + AR) | 83 % | — |
| Stall margin (at 75 % span) | 12 % at TOGA | 14 % at TOGA |
| Estimated blade flutter margin | > 20 % above TOGA speed | > 20 % above TOGA speed |

---

## §5 Noise Budget and Acoustic Design

### 5.1 ICAO Chapter 14 Noise Budget Allocation

| Noise Source | Contribution (cumulative EPNdB) | Chapter 14 Limit (EPNdB) | Margin |
|---|---|---|---|
| FR blade-loading tone (BPF × 1) | −45 dB (below Chapter 14 reference) | — | Managed by sweep |
| FR–AR blade-passing interaction (BPI) | Dominant tone | — | Managed by clocking |
| Trailing-edge broadband noise | −50 dB | — | Managed by t/c and trailing-edge geometry |
| Cumulative (all sources) | Target: Ch14 − 3.5 EPNdB | Ch14 limit (aircraft class) | +3.5 EPNdB |

### 5.2 Acoustic Design Measures

| Measure | Applied To | Expected Benefit |
|---|---|---|
| Leading-edge sweep (35° / 28°) | FR / AR | Reduces leading-edge impingement tone by ~3 dB |
| Scimitar planform | FR + AR | Reduces tip-vortex interaction broadband by ~2 dB |
| Active acoustic clocking (ORSCU) | FR–AR phase | BPI tone reduction ≥ 3 dB |
| Axial spacing Δx = 0.65 m | FR–AR gap | BPI tone reduction (spacing effect) ~1 dB |
| Reduced tip loading (outer 15 % span) | FR + AR | Tip-vortex noise reduction ~1 dB |
| Blade count 12:10 (prime-like ratio) | FR–AR | Limits BPI tone order to 2nd harmonic (2×BPF) |

---

## §6 Structural Health Monitoring (SHM)

Each FR and AR blade is equipped with 8 Fibre Bragg Grating (FBG) sensors embedded in the structural spar layup. The FBG array monitors:

- Blade root bending moment (flapwise and edgewise)
- Torsional strain at 25 % and 75 % span stations
- Tip strain during pitch transients

The ORSCU FBG conditioning module samples all FBG channels at 2 kHz and streams blade-health data via AFDX VL-087-04 to the CMS for trend analysis and predictive maintenance scheduling.

---

## §7 Blade Maintenance Policy

| Inspection Type | Interval | Scope |
|---|---|---|
| Visual inspection | A-check (400 FH) | Leading-edge erosion shield, trailing-edge, surface cracks |
| Tip erosion measurement | 2 500 FH | Tip chord loss; replace shield if > 0.3 mm recess |
| SHM data download and trend review | C-check (6 000 FH) | FBG strain trends; update blade-specific fatigue usage file |
| Non-destructive inspection (NDI) — tap test + ultrasound | C-check | Delamination detection; co-cured spar bond integrity |
| Blade retirement | 20 000 FH or per SB fatigue limit | Safe-life retirement limit |

---

## §8 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-087-030-001 | Final blade t/c selection at tip (7 % vs. 6 %) — flutter vs. efficiency trade | Q-STRUCTURES | CDR |
| OI-087-030-002 | De-icing mat power sizing (80 W/dm²) — ice accretion rig test at −30 °C | Q-GREENTECH | PDR |
| OI-087-030-003 | FBG lead-wire routing through hollow Ti-spar — hermetic seal concept review | Q-STRUCTURES | CDR |
