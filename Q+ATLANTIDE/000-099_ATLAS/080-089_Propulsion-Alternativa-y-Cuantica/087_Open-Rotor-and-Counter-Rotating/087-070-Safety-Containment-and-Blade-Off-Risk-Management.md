---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-087-070-SAFETY-CONTAINMENT-AND-BLADE-OFF-RISK-MANAGEMENT"
register: ATLAS-1000
title: "Safety, Containment and Blade-Off Risk Management"
ata: "ATLAS-087 (Open Rotor and Counter-Rotating)"
sns: "087-070-00"
subsection: "087"
subsubject_code: "070"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-STRUCTURES, Q-HORIZON, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0087-070"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-087-070-SAFETY-CONTAINMENT-AND-BLADE-OFF-RISK-MANAGEMENT
     ATLAS-087 (Open Rotor and Counter-Rotating) · Safety, Containment and Blade-Off Risk Management
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Safety, Containment and Blade-Off Risk Management

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

ATLAS subsubject 087-070 documents the safety design philosophy, containment architecture, blade-off event risk assessment, and emergency response protocols for the AMPEL360E eWTW ORCR propulsor. It addresses the principal hazard unique to the open-rotor configuration: uncontained blade liberation and fragment trajectory analysis.

---

## §2 Safety Design Philosophy

The ORCR safety philosophy applies the following hierarchy:

1. **Prevention:** Blade fatigue management (safe-life limits), SHM-based early detection, FOD protection, bird-strike testing
2. **Mitigation:** Blade-Off Containment Shell (BOCS) to arrest or deflect fragments away from the pressure hull
3. **Consequence limitation:** Feather and rotor de-spin within 10 s; ORSCU auto-shutdown on blade-off detection; emergency procedures in FCOM
4. **Zoning:** Critical structure (pressure hull, fuel tanks, flight controls) placed outside blade-off trajectory risk corridors

---

## §3 Blade-Off Containment Shell (BOCS)

The BOCS is a structural partial-arc containment assembly mounted on the engine nacelle between 60° and 300° of arc relative to the fuselage datum (i.e., the arc facing the fuselage and passenger cabin). It does not form a complete 360° ring (which would negate the open-rotor configuration) but covers the critical sector where fragment trajectories could endanger the pressure hull.

| BOCS Parameter | Value |
|---|---|
| Arc coverage | 60° to 300° (240° arc) |
| Material | Aramid woven fabric (Kevlar-49) + UHMWPE (Dyneema) hybrid layup — 28 plies |
| Mass per unit (one side, port or stbd) | 95 kg |
| Design fragment | Single FR blade (mass 8.5 kg at tip radius) at rotor burst speed (1 275 rpm — 1.5× design TOGA) |
| Performance criterion | Fragment must not perforate BOCS outer face; max residual deformation < 50 mm | 
| Test method | Ballistic fragment test (full-scale blade segment, gas gun) per CS-25.571(e) programme |
| BOCS inspection interval | Visual at each A-check; NDT (thermography) at 6 000 FH (C-check) |

---

## §4 Blade-Off Event Analysis

### 4.1 Fault Tree Summary

| Top Event | Probability Target | Dominant Contributor | Status |
|---|---|---|---|
| FR blade liberation (any blade) | < 1 × 10⁻⁹ per FH (Catastrophic) | Fatigue at root dovetail | TBD (safe-life programme in progress) |
| AR blade liberation (any blade) | < 1 × 10⁻⁹ per FH | As FR | TBD |
| Fragment penetrates pressure hull | < 1 × 10⁻⁹ per FH | BOCS defeat (low probability given 240° coverage) | TBD |

### 4.2 Trajectory Risk Zones

| Fragment Source | Deflection Arc (after BOCS) | Risk Zone | Mitigation |
|---|---|---|---|
| FR blade (BOCS-defeated fragment) | 0°–60° and 300°–360° (above/below — uncovered arc) | Nacelle upper/lower area; empennage | Structural reinforcement of empennage below ORCR pylon; fuel tank isolation |
| AR blade | As FR (AR slightly inboard) | As FR | As FR |
| DPGB shaft fragment | Nacelle containment zone (360°) | Nacelle cowl only | Nacelle structural housing provides full containment |

---

## §5 Bird-Strike and Ice-Throw Protection

| Hazard | Requirement | Test | Status |
|---|---|---|---|
| Large bird (4 lb / 1.8 kg) | CS-25.631; CS-P: blade structural integrity maintained; continued safe flight after single-blade impact | Blade ballistic impact test (gas gun 1.8 kg at 200 m/s impact velocity) | TBD (planned Phase 1) |
| Medium bird strike (0.37 kg × 2) | CS-25.631 | Wind-tunnel bird ingestion (sub-scale model) | TBD |
| Ice throw from FR leading edge | CS-25.1093(b) ice throw trajectory analysis | Ice accretion analysis + rig test | TBD |
| Ice throw impact on AR | BOCS geometry check | CFD trajectory | TBD |

---

## §6 ORSCU Emergency Protocols

| Trigger | ORSCU Response | Time Limit | Crew Alert |
|---|---|---|---|
| Rotor over-speed (N > 1 050 rpm FR or 1 135 rpm AR) | Automatic feather command; FADEC power cut | < 500 ms | MASTER WARNING: ORCR OVERSPEED |
| Blade-off unbalance detected (vibration spike > 5 g) | Automatic feather + FADEC fuel cut | < 1 s | MASTER WARNING: ORCR BLADE-OFF |
| ORSCU channel failure (single) | Switch to standby channel; pitch hold | 50 ms switchover | CAUTION: ORSCU CH FAIL |
| ORSCU dual-channel failure | Pitch hydraulic fail-safe (fine pitch); feather command via FADEC backup | Hydraulic bleed-down to fine pitch | MASTER WARNING: ORCR FAIL — DECLARE EMERGENCY |
| DPGB oil pressure loss | CAUTION + power de-rate; feather within 5 min | 5 min to feather | CAUTION: ORCR OIL PRESS LOW |

---

## §7 LOTO (Lock-Out / Tag-Out) Requirements

All ground maintenance activities on the ORCR that require access within the blade-tip sweep zone must comply with ORCR LOTO Procedure ORCR-LOTO-087:

1. Engine shut down and N1 < 100 rpm confirmed
2. FR and AR blade-pitch lock pins (mechanical) inserted per MEI 087-LOCK-001
3. ORSCU de-energised via ground power switch; GSE hydraulic supply disconnected
4. Hydraulic lines depressurised; blade-pitch accumulator discharged (< 50 psi)
5. Red LOTO tags on ORSCU circuit breakers (2 tags — Ch A and Ch B)
6. Ground inspection of BOCS for cracks/delamination before maintenance access

---

## §8 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-087-070-001 | BOCS full-scale ballistic fragment test programme — test article procurement and schedule | Q-STRUCTURES | Phase 1 |
| OI-087-070-002 | FR blade safe-life limit calculation (20 000 FH target) — fatigue analysis report | Q-STRUCTURES | CDR |
| OI-087-070-003 | Blade-off fault tree (< 1 × 10⁻⁹/FH) — verify independence of BOCS and safe-life barriers | Q-GREENTECH | CDR |
| OI-087-070-004 | Empennage reinforcement mass budget vs. structural penalty — confirm with MBD (mass budget document) | Q-STRUCTURES | PDR |
