---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-082-030-ELECTRIC-FIELD-AND-MAGNETIC-FIELD-ACCELERATION-MECHANISMS"
register: ATLAS-1000
title: "Electric Field and Magnetic Field Acceleration Mechanisms"
ata: "ATLAS-082 (Plasma and Ionic Propulsion Concepts)"
sns: "082-030-00"
subsection: "082"
subsubject_code: "030"
primary_q_division: Q-HPC
support_q_divisions: [Q-GREENTECH, Q-HORIZON, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0082-030"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-082-030-ELECTRIC-FIELD-AND-MAGNETIC-FIELD-ACCELERATION-MECHANISMS
     ATLAS-082 (Plasma and Ionic Propulsion Concepts) · E-Field and B-Field Acceleration Mechanisms
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Electric Field and Magnetic Field Acceleration Mechanisms

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-082 Plasma & Ionic](https://img.shields.io/badge/ATLAS--082-Plasma%20%26%20Ionic%20Propulsion-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-HPC](https://img.shields.io/badge/Q--Division-Q--HPC-purple)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Electric Field and Magnetic Field Acceleration Mechanisms`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 Applicability

| Applicability Level | Rule |
|---|---|
| Standard taxonomy | Applies to the ATLAS node `082` |
| Programme implementation | Conditional; determined by programme architecture, trade studies, certification basis, and applicability model |
| Product configuration | Defined in the programme-specific configuration baseline |
| Effectivity | Defined in the programme CSDB / applicability layer |
| Non-applicability | Must be explicitly stated in the programme impact-study branch when excluded |
## §3 Electrostatic Ion Acceleration (GIE)

### 3.1 Ion Optics Grid System

The GIE ion optics system consists of two or three metallic grids placed at the downstream end of the discharge chamber, aligned co-axially with the thruster axis:

| Grid | Voltage (typical) | Material | Function |
|---|---|---|---|
| Screen Grid | +1 000 to +2 000 V | Molybdenum (Mo), Carbon-Carbon (C/C) | Confines discharge plasma; allows ion extraction |
| Accelerator Grid | −150 to −300 V | Mo, C/C composite | Focuses and collimates ion beam; blocks backstreaming electrons |
| Decelerator Grid (optional) | ~0 V (ground) | Mo | Final beam collimation; reduces downstream ion energy spread |

**Grid geometry parameters (30 cm class GIE for programme-defined aircraft type):**

| Parameter | Value |
|---|---|
| Grid diameter | 300 mm |
| Aperture diameter (screen) | 1.91 mm |
| Aperture diameter (accel) | 1.14 mm |
| Grid gap (screen–accel) | 0.66 mm |
| Transparency (screen) | 67 % |
| Ion optics efficiency η_o | 0.95 |

### 3.2 Child-Langmuir Space Charge Limit

The maximum extractable ion current density J_max is governed by the Child-Langmuir law:

```
J_max = (4ε₀/9) × √(2e/m_i) × V_total^(3/2) / d²
```

where V_total = V_screen − V_accel (total accelerating potential) and d = screen–accel gap. At V_total = 1 400 V, d = 0.66 mm for Xe⁺:

```
J_max ≈ 6.8 mA/cm²
```

This sets the upper bound on ion beam current density and, combined with grid transparency, determines maximum beam current for a given grid area.

---

## §4 Hall-Channel ExB Drift Acceleration

### 4.1 Magnetic Circuit Design

The HET magnetic circuit produces a radially directed magnetic field B_r in the discharge channel exit region. The magnetic circuit comprises:

| Component | Material | Function |
|---|---|---|
| Inner magnetic pole piece | Silicon steel (Fe-Si) | Carries flux inward to channel |
| Outer magnetic pole piece | Silicon steel (Fe-Si) | Carries flux outward from channel |
| Electromagnetic coils | Copper windings, PTFE insulated | Excite magnetic flux; inner and outer coil sets |
| Permanent magnet (optional) | SmCo₅ (temperature stable) | Fixed baseline field; coils trim only |
| Magnetic screen | Soft iron | Shields discharge chamber from fringe flux |

**Target magnetic field parameters (500 mN class HET):**

| Parameter | Value |
|---|---|
| Peak B_r at channel exit | 15–25 mT |
| Radial field uniformity | ± 5 % across channel annulus |
| Axial B_r gradient at exit | ~200 T/m (sharp peak) |
| Coil power consumption | ≤ 40 W total |
| Operating temperature (coils) | ≤ 200 °C (PTFE limit) |

### 4.2 ExB Electron Azimuthal Drift

Electrons injected by the hollow cathode and entering the discharge channel are trapped in azimuthal ExB drift by the crossed electric field E_z (axial) and magnetic field B_r (radial):

```
v_drift = E_z / B_r    [azimuthal direction]
```

At E_z ≈ 15 V/mm and B_r = 20 mT:

```
v_drift ≈ 750 m/s    (much less than electron thermal velocity ~10⁶ m/s)
```

This closed-drift trapping concentrates electrons in the ionisation zone and sets the effective anode-to-cathode impedance. The Hall parameter Ω_e (= ω_ce / ν_en, where ω_ce is electron cyclotron frequency and ν_en is electron-neutral collision frequency) must satisfy Ω_e >> 1 for efficient electron confinement; typical Ω_e ≈ 50–200 in the peak ionisation zone.

---

## §5 Electromagnetic Lorentz Acceleration (MPD)

In an MPD thruster, the Lorentz body force density f is:

```
f = J × B    (N/m³)
```

For a self-field MPD with discharge current I_d, the total Lorentz thrust F_L is approximately:

```
F_L ≈ (μ₀ / 4π) × I_d² × [ln(r_a/r_c) + 3/4]
```

where r_a and r_c are the anode and cathode radii respectively. This squared dependence on I_d means MPD performance scales strongly with power, requiring I_d > 5 kA (power > 50 kW) for useful thrust, which is beyond the current HVDC 270 V research bus capacity. Applied-field MPD (AF-MPD) uses an external superconducting or electromagnet coil to provide B_z (axial) and can operate efficiently at lower current (I_d ~ 100–500 A) but adds magnet mass and cryogenic complexity.

---

## §6 DBD E-Field Plasma Actuation

For the dielectric barrier discharge (DBD) plasma actuators (Role A), the relevant E-field parameter is the reduced electric field E/N (V·cm²), where N is the air number density. Effective ionisation in atmospheric air requires:

```
E/N > 120 Td    (1 Td = 10⁻¹⁷ V·cm²)
```

At sea level (N = 2.69 × 10¹⁹ cm⁻³, standard conditions), this requires E > 3.2 × 10³ V/cm. For a 1 mm electrode gap, applied voltage V > 3.2 kV. In practice, sinusoidal voltages of 5–15 kV at 5–30 kHz are used to produce repetitive micro-discharge streamers that sustain the ionic wind.

---

## §7 Electrode and Grid Material Selection

| Material | Application | Advantages | Limitations |
|---|---|---|---|
| Molybdenum (Mo) | GIE screen/accel grids | High melting point (2 623 °C); low sputter yield vs. Xe⁺ | Brittle at room temp; machining difficulty |
| Carbon-Carbon (C/C) composite | GIE grids, HET channel erosion zones | Very low sputter yield (factor 3× vs. Mo); lighter | Higher resistivity; requires PyC coating for conductivity |
| TZM (Mo-Ti-Zr alloy) | HET anode, high-temp electrodes | Higher ductility than pure Mo; ~same sputter resistance | More expensive than Mo; limited availability |
| Boron Nitride (BN) / BN-SiO₂ | HET discharge channel ceramic | Low secondary electron emission; thermally stable to 900 °C | Erosion under sustained ion bombardment |
| Polyimide (Kapton) | DBD dielectric layer | Flexible; dielectric strength 3–5 kV/mm; lightweight | Degradation under UV and ozone from discharge |
| Alumina (Al₂O₃) ceramic | DBD rigid dielectric panels | High dielectric strength (10–15 kV/mm); erosion resistant | Brittle; not suitable for curved aerofoil installation |

---

## §8 Magnetic and Electric Field Safety Requirements

| Hazard | Requirement | Mitigation |
|---|---|---|
| HV electric field (GIE, HET) | No accessible HV surface; 500 V RMS > 50 V threshold per IEC 60479-1 | All HV rails enclosed in grounded metallic shrouds; interlocked panels |
| Stray magnetic field (HET magnet) | B < 1 mT at 300 mm from thruster body | Magnetic screen; fringe field analysis required |
| DBD ozone generation | < 0.1 ppm O₃ in occupied zone (OSHA) | DBD location aft-exterior only; no cabin air entrainment |
| RF emissions from PPPU switching | DO-160G Section 21 compliance | Shielded PPPU enclosure; common-mode filter on HV output |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-082-030-001 | HET magnetic circuit thermal expansion detuning at Tcoil > 150 °C — field uniformity analysis | Q-HPC | CDR |
| OI-082-030-002 | GIE C/C grid electrical resistivity vs. temperature: PyC coating spec needed | Q-STRUCTURES | PDR |
| OI-082-030-003 | DBD ozone budget at full cruise altitude (low density, reduced O₃ conversion) | Q-GREENTECH | Phase 2 |
