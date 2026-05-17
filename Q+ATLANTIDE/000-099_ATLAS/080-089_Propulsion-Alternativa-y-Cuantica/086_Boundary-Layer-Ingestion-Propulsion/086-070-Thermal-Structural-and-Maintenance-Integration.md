---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-086-070-THERMAL-STRUCTURAL-AND-MAINTENANCE-INTEGRATION"
register: ATLAS-1000
title: "Thermal, Structural and Maintenance Integration"
ata: "ATLAS-086 (Boundary Layer Ingestion Propulsion)"
sns: "086-070-00"
subsection: "086"
subsubject_code: "070"
primary_q_division: Q-INDUSTRY
support_q_divisions: [Q-STRUCTURES, Q-GREENTECH, Q-HORIZON]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0086-070"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-086-070-THERMAL-STRUCTURAL-AND-MAINTENANCE-INTEGRATION
     ATLAS-086 (Boundary Layer Ingestion Propulsion) · Thermal, Structural and Maintenance Integration
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Thermal, Structural and Maintenance Integration

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-086 BLI Propulsion](https://img.shields.io/badge/ATLAS--086-BLI%20Propulsion-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-INDUSTRY](https://img.shields.io/badge/Q--Division-Q--INDUSTRY-purple)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Thermal, Structural and Maintenance Integration`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 Thermal Management

### 2.1 PMSM Cooling Architecture

Each 120 kW PMSM dissipates approximately **4.8 kW** of waste heat at peak continuous load (96.5 % efficiency at 135 kW peak → 4.7 kW; nominal at 120 kW → ~4.2 kW). The cooling strategy uses:

1. **Internal air cooling:** Rotor back-flow through stator slots; natural convention of fan flow. Provides primary stator cooling at all fan speeds ≥ 1 500 RPM.
2. **Supplementary liquid jacket:** An ethylene–glycol–water (EGW) liquid jacket surrounding the stator housing provides supplementary cooling at low fan speed (ground taxi) or high ambient temperature. The jacket feeds from the ATLAS-074 Thermal Management loop (BLI branch, BLITM-1 and BLITM-2 circuits).

### 2.2 BLI Thermal Management Loop (BLITM)

| Parameter | BLITM-1 (BLI-PA-1) | BLITM-2 (BLI-PA-2) |
|---|---|---|
| Coolant | EGW 50/50 | EGW 50/50 |
| Flow rate | 6 L/min | 6 L/min |
| Inlet temperature | ≤ 45 °C | ≤ 45 °C |
| Max PMSM winding temperature | ≤ 150 °C (alarm 140 °C) | ≤ 150 °C (alarm 140 °C) |
| MCU-086 coolant jacket temp | ≤ 55 °C (alarm 50 °C) | ≤ 55 °C (alarm 50 °C) |
| Pump type | Brushless centrifugal (redundant pair) | Brushless centrifugal (redundant pair) |
| Heat exchanger | ATLAS-074 RAHX secondary circuit | ATLAS-074 RAHX secondary circuit |

### 2.3 Thermal Alarms and BLICU Actions

| Alarm | Threshold | BLICU Response |
|---|---|---|
| PMSM winding T1 caution | > 130 °C | Log; increase coolant pump speed |
| PMSM winding T2 warning | > 140 °C | Reduce fan speed by 15 %; alert crew `BLI THERMAL WARN` |
| PMSM winding T3 critical | > 150 °C | Shut down BLI-PA; bypass open; `BLI FAIL HOT` |
| MCU-086 T1 caution | > 50 °C | Log; activate supplementary cooling |
| MCU-086 T2 warning | > 55 °C | Reduce fan speed by 20 %; alert crew |
| MCU-086 T3 critical | > 65 °C | Shut down MCU; `BLI FAIL MCU HOT` |

---

## §3 Structural Integration

### 3.1 Aft Fuselage Interface

The BLI propulsor assemblies attach to the aft fuselage at the **FS 43.5 m rear pressure bulkhead** via four hardpoints (HP-086-A through HP-086-D, defined in 086-040 §3). The structural interface incorporates:

- **Vibration isolation mounts:** Visco-elastic damper isolators at each hardpoint, rated for the load cases in 086-040 §3.2. Isolator natural frequency 22 Hz (well below fan BPF at 1 800 Hz).
- **Electrical bonding straps:** Dedicated 4 AWG copper bonding straps at each HP; resistance ≤ 1 mΩ per CS-25.899.
- **Thermal growth accommodation:** Sliding/floating fastener in HP-086-C (lateral axis) accommodates PMSM housing thermal expansion ±1.2 mm.

### 3.2 S-Duct Structural Integration

The S-duct inlet assembly bonds to the fuselage upper skin at FS 40.0–43.2 m:

- Adhesive bond + mechanical fasteners (M6 countersunk, 100 mm pitch, CFRP compatible).
- Sealed with PR-1422 polysulfide sealant (fuel-resistant, −65 °C to +130 °C).
- External surface flushness: ≤ 0.5 mm step/gap (aerodynamic requirement).

---

## §4 Maintenance Access

### 4.1 Access Provisions

| LRU | Access Panel | Panel Type | Special Tooling |
|---|---|---|---|
| BLI-PA Fan Stage | Panel 86L/86R (aft fuselage upper) | Quick-release quarter-turn fasteners | None (hand tools) |
| PMSM Stator | Requires fan stage removal | — | Fan puller tool TL-086-001 |
| MCU-086 | Panel 86M (aft avionics bay) | Dzus fasteners | None |
| BLICU | Panel 86A (aft avionics bay) | Dzus fasteners | BLICU-GSE-1 unit |
| TPR Rake Assembly | Access via fan face (fan stage removed) | — | Probe calibration kit CAL-086-001 |
| BLITM Coolant Coupling | Panel 86C (aft service bay) | Quick-disconnect fittings | EGW drain kit TL-074-003 |

### 4.2 Maintenance Intervals

| Component | Check Level | Interval | Task |
|---|---|---|---|
| Fan blade visual inspection | A-check | 500 h or 200 cycles | Visual; leading edge erosion assessment |
| Fan balance check | B-check | 2 000 h or 800 cycles | Ground spin balance rig; re-balance if > 25 g·mm |
| Fan-face TPR rake probe calibration | B-check | 2 000 h | Bench calibration vs. reference pressure source |
| PMSM winding resistance check | C-check | 6 000 h | Megger test; record trend |
| PMSM bearing replacement | C-check | 6 000 h | Mandatory replace; LRU exchange |
| MCU-086 BITE download and inspection | B-check | 2 000 h | GSE download; inspect IGBT thermal data |
| BLICU software update | Per SB | Per SB | BLICU-GSE-1 upload procedure |
| S-duct NDT inspection | C-check | 6 000 h | UT/bond inspection of adhesive bond |
| BLITM coolant sample and refill | C-check | 6 000 h | EGW acidity / inhibitor check; top-off |
| Vibration isolation mount inspection | C-check | 6 000 h | Compression set measurement; replace if > 20 % |

---

## §5 Safety and LOTO Requirements

| Hazard | LOTO Requirement | PPE |
|---|---|---|
| HVDC 270 V (MCU-086) | MCU-086 HV isolator OFF; lock tag; wait 60 s; verify < 50 V | Class 2 HV gloves; face shield |
| Rotating fan (residual spin) | Confirm BLICU in STANDBY; verify RPM = 0 on MCU display; install fan lock pin TL-086-002 | Safety glasses |
| EGW coolant (hot) | Allow 30 min cool-down after BLI OFF; pressure-relief coupler before opening | Chemical gloves; eye protection |
| Inlet duct confined space | Ventilate duct before entry; O₂ monitor; 2-person rule | None additional |

---

## §6 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-086-070-001 | BLITM pump sizing confirmation at ground idle in ISA+35 °C — thermal analysis | Q-STRUCTURES | PDR |
| OI-086-070-002 | Vibration isolator qualification — DO-160G vibe + shock test at IBR-2 impulse load | Q-INDUSTRY | Phase 2 |
| OI-086-070-003 | Fan blade erosion rate model — sand/rain erosion test at cruise speeds | Q-HORIZON | CDR |
| OI-086-070-004 | S-duct bond durability — 120 000-cycle fatigue test per ASTM D3762 | Q-STRUCTURES | Phase 2 |
