---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-084-070-AIRFRAME-INTEGRATION-THERMAL-AND-SAFETY-CONSTRAINTS"
register: ATLAS-1000
title: "Airframe Integration Thermal and Safety Constraints"
ata: "ATLAS-084 (Hybrid Architectures — Beyond Gen-2)"
sns: "084-070-00"
subsection: "084"
subsubject_code: "070"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-GREENTECH, Q-INDUSTRY, Q-HORIZON]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0084-070"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-084-070-AIRFRAME-INTEGRATION-THERMAL-AND-SAFETY-CONSTRAINTS
     ATLAS-084 (Hybrid Architectures — Beyond Gen-2) · Airframe Integration Thermal and Safety Constraints
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Airframe Integration Thermal and Safety Constraints

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-084 Hybrid Beyond Gen-2](https://img.shields.io/badge/ATLAS--084-Hybrid%20Beyond%20Gen--2-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-STRUCTURES](https://img.shields.io/badge/Q--Division-Q--STRUCTURES-grey)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

ATLAS subsubject 084-070 defines the physical installation layout of all BGHA major components within the AMPEL360E eWTW airframe, the BGHA Thermal Management Loop (BGHA-TML) design, HVDC 800 V safety zone requirements, hydrogen ATEX zone boundaries, weight and balance impact of BGHA components, and structural interface requirements for BGHA component mounts and supports.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA Reference | ATLAS-084 — 084-070 Airframe Integration Thermal and Safety Constraints |
| Certification Basis | EASA CS-25 Amdt 27+; IEC 60479-1; ATEX 94/9/EC; DO-160G |
| S1000D SNS | 084-070-00 |

---

## §3 BGHA Installation Layout

| Component | Location | Structural Interface | Access Panel | ATEX Zone |
|---|---|---|---|---|
| SSBP Pack A | Forward cargo bay — port side | SSBP cradle frame, 4-point mounting; vibration isolators | LD-3 cargo door (port) | Non-ATEX (SSE sealed cells) |
| SSBP Pack B | Forward cargo bay — stbd side | SSBP cradle frame, 4-point mounting; vibration isolators | LD-3 cargo door (stbd) | Non-ATEX (SSE sealed cells) |
| FCSS Assembly | Aft bay centre (STA 1200–1450) | FCSS pallet frame; 8-point mounting with fire-resistant blanket | Aft fuselage lower access panel | ATEX Zone 2 (H₂ manifold zone) |
| VCGT-1 | Port under-wing pylon (STA 850) | Pylon-to-wing root interface; 4-lug mount; vibration-damped | Nacelle cowl access | Non-ATEX; bi-fuel hazard zone near fuel lines |
| VCGT-2 | Stbd under-wing pylon (STA 850) | As VCGT-1 mirror | As VCGT-1 mirror | Non-ATEX; bi-fuel hazard zone |
| SCEB Module | Mid-fuselage electronics rack (STA 900–1000) | 19-inch rack; 4-point vibration mount | Fuselage LH access door | Non-ATEX |
| BGSCU | Forward avionics bay (STA 200–280) | Standard 6-MCU ARINC 600 tray | E&E bay access door | Non-ATEX |
| BGHA-TML Pumps (×2) | Aft bay lower (STA 1100) | Pump bracket welded to airframe frame | Lower aft access panel | Non-ATEX |
| ATRUs (×2) | VCGT nacelle pylon (1 per pylon) | Pylon electronics bay | Pylon lower panel | Non-ATEX |
| BDCCs A, B, C, D | Power electronics bay (STA 950–1050) | 19-inch rack; cold-plate mounted | LH electronics bay door | Non-ATEX |

---

## §4 Thermal Management Loop (BGHA-TML)

The BGHA-TML is a dedicated EGW (40/60 ethylene-glycol/water) liquid cooling loop serving all BGHA power electronics and the FCSS stack. It operates in parallel with (but hydraulically independent of) the Gen-2 MICL and BCL loops defined in ATLAS-074.

**BGHA-TML primary circuit:**
- Coolant: EGW 40/60; operating temperature 20–65 °C inlet / 65–80 °C outlet
- Flow rate: 30 L/min total (15 L/min per pump; pumps in parallel)
- Pump A (primary): 15 L/min at 3 bar ΔP; BLDC motor 400 W
- Pump B (standby): Identical to Pump A; auto-start if Pump A flow drops > 20 %
- BGHA-RAHX: Ram-air heat exchanger in lower fuselage; rated 200 kW heat rejection at M 0.78 FL 350
- Cold plates: BDCC cold plates (1 per BDCC unit); BGSCU QPU cryo interface (secondary loop)
- FCSS stack coolant: BGHA-TML supplies FCSS stack coolant directly; FCSS EGW inlet 65 °C, outlet 80 °C; separate thermostat valve for stack temperature control

**Alarm thresholds:**
| Alarm | Threshold | Response |
|---|---|---|
| TML-T1 WARN | Coolant outlet > 82 °C | BGSCU advisory; reduce BDCC loads 10 % |
| TML-T2 WARN | Coolant outlet > 90 °C | BGSCU reduces all BGHA loads 25 %; crew advisory |
| TML-T3 CAUTION | Pump A flow < 10 L/min | Pump B start command; CMS fault logged |
| TML-T4 CRITICAL | Coolant outlet > 95 °C | BGSCU enters DM-2 emergency power reduction; crew advisory |

---

## §5 HVDC 800 V Safety Zones

All components, cables, and connectors carrying HVDC 800 V are designated **HV Zone 84** under the AMPEL360E eWTW electrical safety plan. The following rules apply to all work in or near HV Zone 84:

1. **LOTO procedure:** BGSCU must be commanded to STANDBY mode via GSE; Bus-800 must show < 50 V on HV Zone 84 indicator before any physical access.
2. **Discharge hold-off:** After BGSCU STANDBY command, a minimum of 60 s must elapse (Bus-800 capacitor bleed discharge via bleed resistors) before touching any Bus-800 cable or connector.
3. **HiPot test interval:** Every C-check, all HVDC 800 V cables must pass HiPot test at 1 500 V DC for 1 min (dielectric withstand); any failure requires cable replacement.
4. **PPE:** Certified Class 4 HV gloves (1 000 V AC / 1 500 V DC rated); face shield; non-conductive footwear.
5. **Warning labels:** ISO 3864-2 Class B HV warning labels on all BDCC panels, BTB enclosures, Bus-800 busbars, and HVDC cable conduits.

---

## §6 Hydrogen ATEX Zones

The FCSS installation and LH₂/GH₂ feed lines (from ATLAS-076/077) within the aft bay create an ATEX Zone 2 environment:

| Zone | Location | Extent | Requirements |
|---|---|---|---|
| ATEX-084-H2-01 | FCSS assembly bay (STA 1200–1450) | Full bay volume | O₂ sensor; forced ventilation before entry; Xe-classification tools; H₂ detector (4 sensors) |
| ATEX-084-H2-02 | LH₂ feed manifold trench (STA 1100–1450) | 300 mm radius from manifold | As above; no spark-generating tools |

Ventilation: Dedicated bay ventilation fan (600 m³/h) must be operational before entering either zone. Entry is prohibited if O₂ level < 19.5 % v/v (checked by personal O₂ monitor at bay entrance).

---

## §7 Weight and Balance Impact

| Component | Mass (kg) | CG Station (mm from datum) | CG Contribution (kg·m) |
|---|---|---|---|
| SSBP Pack A | 1 200 | 4 200 (forward cargo bay) | 5 040 |
| SSBP Pack B | 1 200 | 4 200 | 5 040 |
| FCSS Assembly | 480 | 12 500 (aft bay) | 6 000 |
| VCGT-1 (excl. pylon) | 620 | 8 500 (port wing) | 5 270 |
| VCGT-2 (excl. pylon) | 620 | 8 500 (stbd wing) | 5 270 |
| SCEB Module | 280 | 9 000 (mid-fuse rack) | 2 520 |
| BGSCU | 45 | 2 500 (fwd avionics bay) | 113 |
| BDCCs (A+B+C+D) | 160 | 9 500 | 1 520 |
| ATRUs (×2) | 120 | 8 500 (pylon) | 1 020 |
| BGHA-TML (fluid + exchanger + pipes) | 85 | 11 000 | 935 |
| **BGHA Total** | **4 810** | — | **32 728** |
| **BGHA System CG** | — | **6 803 mm** | — |

> **Note:** BGHA total mass of 4 810 kg replaces Gen-2 propulsion components of 3 200 kg; net mass increase ~1 610 kg to be absorbed within MTOW growth margin under BGHA STC.

---

## §8 Structural Interfaces

| Interface | Requirement | Standard | Verification |
|---|---|---|---|
| SSBP cradle | Withstand 9g forward, 4.5g sideward (CS-25.561 crash loads) | CS-25.561; MIL-HDBK-516C | Static load test + FEA |
| FCSS pallet | Fire-resistant blanket (FAR 25.855 class); 4g aft crash load | CS-25.855; CS-25.561 | Test + FEA |
| VCGT pylon | Meet VCGT OEM pylon interface load spectrum; fatigue life 60 000 FC | CS-25.571; VCGT OEM ICD | Fatigue analysis + ground test |
| SCEB rack | 9g forward; 19-inch rack per ARINC 404A | ARINC 404A; CS-25.561 | Static test |
| BGHA-TML pipe routing | Continuous support ≤ 600 mm span; P-clamp fire-resistant material | CS-25.1182 | Drawing review + assembly check |

---

## §9 Interfaces

| Interface | Connected System | Protocol | Data |
|---|---|---|---|
| BGHA-TML coolant to FCSS | FCSS stack coolant circuit | Physical EGW piping + CAN temp | Coolant flow and temperature |
| BGHA-TML to ATLAS-074 TMS | ATLAS-074 RAHX manifold | Physical EGW piping | Heat rejection to ram-air |
| HVDC cables to Bus-800 | All BDCCs; ATRUs | HVDC 800 V shielded cable | Power distribution |
| H₂ feed to FCSS | ATLAS-077 LH₂ distribution | LH₂ cryo feed line | LH₂ flow to FCSS manifold |

---

## §10 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-084-070-001 | SSBP cradle FEA — 9g crash load analysis with SSE cell pack mass | Q-STRUCTURES | PDR |
| OI-084-070-002 | BGHA-TML RAHX sizing — heat rejection at FL 350, M 0.78, ISA+15 | Q-GREENTECH | CDR |
| OI-084-070-003 | VCGT pylon fatigue spectrum — combined SAF/LH₂ vibration signature | Q-STRUCTURES | CDR |
| OI-084-070-004 | ATEX zone H₂ concentration threshold under single FCSS manifold leak | Q-GREENTECH | PDR |
| OI-084-070-005 | BGHA net mass increase (1 610 kg) — MTOW STC growth margin confirmation | Q-STRUCTURES | PDR |
