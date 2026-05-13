---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-087-010-OPEN-ROTOR-BASELINE-AND-SCOPE"
register: ATLAS-1000
title: "Open Rotor Baseline and Scope"
ata: "ATLAS-087 (Open Rotor and Counter-Rotating)"
sns: "087-010-00"
subsection: "087"
subsubject_code: "010"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HORIZON, Q-HPC, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0087-010"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-087-010-OPEN-ROTOR-BASELINE-AND-SCOPE
     ATLAS-087 (Open Rotor and Counter-Rotating) · Open Rotor Baseline and Scope
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Open Rotor Baseline and Scope

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-087 Open Rotor](https://img.shields.io/badge/ATLAS--087-Open%20Rotor%20%26%20Counter--Rotating-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-teal)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

ATLAS subsubject 087-010 defines the technology baseline and mission scope for the Open Rotor and Counter-Rotating (ORCR) propulsor selected for the AMPEL360E eWTW. It records the trade study results that led to the contra-rotating unducted fan (CRUF) configuration selection, the Technology Readiness Level (TRL) status of each major subsystem, and the mission performance trade space.

---

## §2 Technology Baseline

| Technology Option | By-Pass Ratio | η_prop (M 0.78) | Noise vs. Ch14 | TRL (2026) | Decision |
|---|---|---|---|---|---|
| Geared turbofan (GTF) reference | 12–15 | 78 % | −1 to −2 dB | 9 (production) | Baseline reference |
| Single-rotation open rotor (SROR) | N/A (unducted) | 80 % | −0.5 dB | 6–7 | Rejected — swirl loss, noise margin |
| Contra-rotating unducted fan (CRUF) | N/A (unducted) | 83 % | −3 to −4 dB | 6 | **Selected — ORCR baseline** |
| Ultra-high BPR turbofan (BPR 20+) | 20–25 | 81 % | −2 dB | 7 | Rejected — diameter / weight penalty |
| Boundary-layer-ingesting fan (BLI) | N/A | 82 % | −2 dB | 5 | Addressed separately in ATLAS-086 |

**Rationale for CRUF selection:** The CRUF contra-rotating architecture recovers approximately 6–8 % additional propulsive efficiency compared to the SROR by eliminating exit swirl through the second rotor row. Combined with variable-pitch on both rotor rows, it achieves noise levels 3–4 dB below ICAO Chapter 14 through acoustic clocking (phasing the FR and AR blade passing events) and swept blade geometry. The integration weight penalty (DPGB, second rotor hub) is offset by the fuel burn reduction over a 2 000 NM design mission.

---

## §3 TRL Status

| Subsystem | TRL (2026) | Key Demonstration | Target TRL (PDR) | Target TRL (CDR) |
|---|---|---|---|---|
| FR/AR blade composite design | 6 | Sub-scale rig at M 0.5 (2024) | 7 | 8 |
| DPGB differential gearbox | 5 | Ground endurance test 200 h (2025) | 6 | 7 |
| ORSCU DAL B software | 4 | Algorithm simulation, iron-bird | 6 | 7 |
| EHPA (electro-hydraulic pitch) | 6 | Full-scale blade actuator test (2024) | 7 | 8 |
| BOCS containment shell | 5 | Ballistic fragment test (sub-scale, 2025) | 6 | 7 |
| Acoustic clocking control | 5 | Scale-model acoustic wind tunnel (2025) | 6 | 7 |

---

## §4 Mission Performance Trade Space

| Mission Parameter | Design Point | Low Case | High Case | Notes |
|---|---|---|---|---|
| Design mission range | 2 000 NM | 1 500 NM | 2 500 NM | ORCR fuel-burn advantage maximised at ≥ 1 800 NM |
| Cruise Mach | M 0.78 | M 0.72 | M 0.80 | Tip-speed constraint limits M > 0.80 without sweep redesign |
| Cruise altitude | FL 350 | FL 310 | FL 390 | Thrust lapse at FL 390 requires larger blade pitch angle |
| Payload | 180 pax / 18 000 kg | 150 pax | 220 pax (MEW increase) | Wing and fuselage stretch covered under separate ATLAS sections |
| Specific fuel consumption improvement vs. GTF reference | 15 % | 10 % | 18 % | Function of blade sweep schedule and noise clocking optimisation |
| Cumulative noise margin vs. ICAO Ch14 | −3.5 EPNdB | −2.5 EPNdB | −5.0 EPNdB | Dependent on acoustic clocking maturity |

---

## §5 In-Scope / Out-of-Scope Boundary

| In Scope (ATLAS-087) | Out of Scope |
|---|---|
| FR/AR blade design, materials, pitch mechanics | Core engine turbine design (covered by ATA 72) |
| DPGB differential gearbox and oil system | Main propeller shaft from LPT (covered by ATA 72) |
| ORSCU controls and EHPA pitch system | Aircraft fuel system (ATA 28) |
| BOCS containment structure | Airframe nacelle primary structure (ATA 54) |
| Aeroacoustics, noise budget, NVH | Cabin interior acoustic treatment (ATA 25) |
| Airframe integration clearance zones | Landing gear / runway interface loads (ATA 32) |
| Monitoring, diagnostics, AFDX interfaces | FADEC architecture (ATA 73) |

---

## §6 Governing Documents

| Document | Title | Rev |
|---|---|---|
| QATL-ATLAS-1000-ATLAS-080-089-08-087-000 | ORCR General | 0.1 |
| EASA CS-25 Amdt 27+ | Airworthiness Standards | — |
| EASA CS-P | Propeller Standards | — |
| ICAO Annex 16 Vol. I Ch. 14 | Noise Standards | — |
| DO-178C | Software Assurance | — |
| DO-254 | Hardware Assurance | — |

---

## §7 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-087-010-001 | Confirm M 0.80 stretch case requires blade re-sweep — involve Q-STRUCTURES | Q-GREENTECH | PDR |
| OI-087-010-002 | DPGB 200 h endurance test report — incorporate updated TRL assessment | Q-INDUSTRY | PDR |
| OI-087-010-003 | Noise clocking IP status — confirm patent coverage before CDR release | Q-HORIZON | CDR |
