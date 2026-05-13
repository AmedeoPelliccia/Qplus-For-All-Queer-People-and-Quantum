---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-087-040-GEARBOX-DRIVE-AND-TORQUE-TRANSFER-INTERFACES"
register: ATLAS-1000
title: "Gearbox Drive and Torque-Transfer Interfaces"
ata: "ATLAS-087 (Open Rotor and Counter-Rotating)"
sns: "087-040-00"
subsection: "087"
subsubject_code: "040"
primary_q_division: Q-INDUSTRY
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-HORIZON]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0087-040"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-087-040-GEARBOX-DRIVE-AND-TORQUE-TRANSFER-INTERFACES
     ATLAS-087 (Open Rotor and Counter-Rotating) · Gearbox Drive and Torque-Transfer Interfaces
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Gearbox Drive and Torque-Transfer Interfaces

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-087 Open Rotor](https://img.shields.io/badge/ATLAS--087-Open%20Rotor%20%26%20Counter--Rotating-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-INDUSTRY](https://img.shields.io/badge/Q--Division-Q--INDUSTRY-red)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

ATLAS subsubject 087-040 documents the Differential Planetary Gearbox (DPGB) detailed design, oil system architecture, shaft-coupling interfaces, and torque-measurement instrumentation for the AMPEL360E eWTW ORCR propulsor. It defines the mechanical interfaces between the LPT shaft, the DPGB, the FR and AR shafts, and the engine nacelle structure.

---

## §2 DPGB Detailed Design

### 2.1 Gear Train Architecture

The DPGB uses a two-stage compound epicyclic arrangement:

| Stage | Type | Function | Reduction |
|---|---|---|---|
| Stage 1 (Input) | Simple planetary — fixed ring | Reduces LPT 4 800 rpm to intermediate 760 rpm | 6.3:1 |
| Stage 2 (Output — Differential) | Differential epicyclic | Splits power to FR (carrier) and AR (ring, reversed) | FR 1.62:1; AR 1.50:1 |
| **Overall** | — | LPT to FR | **10.2:1** |

**Stage 2 Differential Detail:**
- Planet carrier → FR shaft (clockwise fwd view)
- Ring gear → AR shaft via reversal pinion (counter-clockwise fwd view)
- Sun gear → reacts torque through nacelle mount (torque arm)

### 2.2 DPGB Key Parameters

| Parameter | Value |
|---|---|
| Max continuous input torque | 100 000 N·m |
| Max transient torque (5 s) | 125 000 N·m |
| Design overload torque (structural limit) | 150 000 N·m (× 1.5 MoS) |
| DPGB housing material | Ti-6Al-4V precision cast |
| Gear material | Case-hardened M50 NiL steel (case depth 1.5 mm HRC 60) |
| Number of planets (Stage 1) | 5 |
| Number of planets (Stage 2) | 4 |
| DPGB total mass (dry) | 680 kg |

---

## §3 Lubrication and Oil System

| Parameter | Value |
|---|---|
| Oil specification | MIL-PRF-23699 Type IV (synthetic ester base) |
| Oil system pressure | 3.5 bar (nominal supply to main galleries) |
| Oil flow rate (TOGA) | 45 L/min |
| Oil temperature (normal) | 60–115 °C |
| Oil temperature (transient 5 min) | Up to 130 °C |
| Low-oil-pressure warning threshold | < 2.0 bar → ORSCU BITE fault + AWMS caution |
| High-temperature warning threshold | > 120 °C → AWMS caution; > 130 °C → automatic power de-rate |
| Oil cooler type | Air-oil heat exchanger (DPGB-OHX) mounted in nacelle inlet strut |
| Oil cooler capacity | 30 kW rejection |
| Oil filter | 25 µm absolute, magnetic chip detector integral |
| Oil pump — main (qty) | 2 × engine gear-driven pumps (FR-shaft and AR-shaft driven) |
| Oil pump — standby | 1 × electric pump (28 V DC; 8 L/min; activated on P < 2.0 bar) |
| Oil quantity (total system) | 22 L |
| Drain/service point | Quick-disconnect drain fitting, nacelle lower panel |

---

## §4 Shaft-Coupling Interfaces

| Interface | Type | Torque Capacity | Notes |
|---|---|---|---|
| LPT shaft → DPGB input | Splined curvic coupling | 125 000 N·m | Axial retention by Hirth lock ring |
| DPGB output → FR shaft | Conical splined flange | 110 000 N·m | Blade-off fuse feature (fuse washer, shears at 1.3× limit) |
| DPGB output → AR shaft | Conical splined flange | 100 000 N·m | As FR shaft |
| Elastomeric torsional damper | LPT-DPGB input shaft | N/A (damping element) | Frequency range 10–200 Hz; replaceable |
| Torque arm (DPGB to nacelle) | Rigid spigot mount | 150 000 N·m reaction | Load path to nacelle pylon; fatigue tested |

---

## §5 Torque Measurement and Instrumentation

Accurate torque measurement is required by the ORSCU for:
- Torque-balance control (maintaining FR/AR torque split within 5 % of design)
- Engine thrust indication cross-check
- Gearbox health monitoring and BITE

| Sensor | Type | Location | Accuracy | Interface |
|---|---|---|---|---|
| FR shaft torque (TRQ-FR) | Magnetostrictive torque sensor (non-contact) | FR shaft between DPGB and FR hub | ±0.5 % FS | ORSCU via ARINC 429 |
| AR shaft torque (TRQ-AR) | Magnetostrictive torque sensor (non-contact) | AR shaft between DPGB and AR hub | ±0.5 % FS | ORSCU via ARINC 429 |
| Input shaft torque (TRQ-IN) | Strain gauge telemetry (rotating) | LPT-DPGB coupling shaft | ±1 % FS | FADEC via ARINC 429 |
| DPGB chip detector (CHD-01) | Magnetic chip detector | DPGB sump | Qualitative (chip/no chip) | AWMS discrete |
| Oil pressure (P-OIL) | Piezo-resistive transducer | DPGB main gallery | ±0.1 bar | ORSCU BITE |
| Oil temperature (T-OIL-1,2) | PT-100 RTD | DPGB sump + cooler outlet | ±1 °C | ORSCU BITE |

---

## §6 Maintenance Procedures Summary

| Task | Interval | Duration | Access |
|---|---|---|---|
| Oil level check and top-up | A-check (400 FH) | 0.5 h | Lower nacelle cowl removed |
| Oil filter replacement | 2 000 FH or oil analysis indication | 1 h | Filter housing, lower nacelle |
| Chip detector inspection | 2 000 FH | 0.5 h | Sump drain plug |
| DPGB oil cooler (OHX) cleaning | 4 000 FH | 2 h | Nacelle inlet strut access |
| Torque sensor calibration check | 6 000 FH (C-check) | 3 h | Requires test-club (no blade removal) |
| Full DPGB overhaul | 8 000 FC | Off-wing 120 h | Depot; DPGB removed as assembly |

---

## §7 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-087-040-001 | DPGB 8 000 FC TBO — confirm by endurance test; interim TBO 4 000 FC pending | Q-INDUSTRY | Phase 2 |
| OI-087-040-002 | Fuse-washer shear load calibration (1.3× limit) — requires blade-off simulation FEA | Q-STRUCTURES | CDR |
| OI-087-040-003 | Magnetostrictive torque sensor EMI compatibility with ORSCU at DO-160G Cat M | Q-INDUSTRY | PDR |
