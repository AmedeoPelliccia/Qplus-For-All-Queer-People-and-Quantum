---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-083-070-AIRFRAME-INTEGRATION-THERMAL-AND-STRUCTURAL-CONSTRAINTS"
register: ATLAS-1000
title: "Airframe Integration, Thermal and Structural Constraints"
ata: "ATLAS-083 (Solar-Electric Auxiliary)"
sns: "083-070-00"
subsection: "083"
subsubject_code: "070"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-GREENTECH, Q-INDUSTRY, Q-HPC]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0083-070"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-083-070-AIRFRAME-INTEGRATION-THERMAL-AND-STRUCTURAL-CONSTRAINTS
     ATLAS-083 (Solar-Electric Auxiliary) · Airframe Integration, Thermal and Structural
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Airframe Integration, Thermal and Structural Constraints

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-083 Solar-Electric](https://img.shields.io/badge/ATLAS--083-Solar--Electric%20Auxiliary-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-STRUCTURES](https://img.shields.io/badge/Q--Division-Q--STRUCTURES-orange)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

ATLAS subsubject 083-070 defines the airframe integration constraints, structural design requirements, and thermal management provisions for the Solar-Electric Auxiliary (SEA) system. It covers PV panel laminate structural ICD, BLI duct structural design, SEACU mounting, SiC inverter thermal budget, fuel system exclusion zones, lightning protection, structural weight allocation, and aerodynamic smoothness requirements.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA reference | ATLAS-083 — 083-070 Airframe Integration, Thermal and Structural |
| Certification basis | EASA CS-25 Amdt 27+; CS-25.631 (bird strike); CS-25.581 (lightning); DO-160G (environmental); ASTM D7762 (adhesive bond structural) |
| S1000D SNS | 083-070-00 |

---

## §3 PV Laminate Structural Integration

### 3.1 Bonded Panel ICD

Each PV panel (max 600 mm × 400 mm) is adhesively bonded to the outer CFRP skin using FM-300 epoxy film adhesive (0.12 mm nominal thickness, 150 °C cure compatible). The bond design must satisfy:

| Constraint | Limit | Analysis Method |
|---|---|---|
| Peel stress (panel edge, −55 °C) | < 0.5 MPa | Linear elastic FE + CTE mismatch; 3D shell model |
| Shear stress (bond line, 1 g + gust) | < 2.5 MPa | Classical laminate shear flow |
| Bond fatigue (thermal cycles) | No delamination at 5 000 cycles (−55 °C ↔ +85 °C) | Fatigue test coupon programme |
| Moisture uptake (bond line, 85 % RH, 70 °C, 1 000 h) | < 3 % mass gain | ASTM D5229; bond strength retention ≥ 80 % |

**CTE mismatch:** GaAs cell stack CTE = 5.7 ppm/°C; CFRP outer skin CTE = 1–3 ppm/°C (in-plane). Silicone encapsulant (CTE ≈ 250 ppm/°C, E ≈ 0.1 MPa) accommodates the differential strain by acting as a compliant buffer layer. Peel stress at panel edge is dominated by encapsulant deformation rather than CTE mismatch at panel substrate level.

### 3.2 Panel Removal and Replacement

Panels are removable at B-check or on-condition. Procedure:
1. Apply opaque cover blanket (SEACU SOLAR ARRAY ISOLATED confirmed per BREX-083-v1)
2. Heat bond line to 60 °C (heated blanket tool) to soften FM-300 below shear yield
3. Insert removal blade under panel edge; slide to debond
4. Clean skin surface; apply new FM-300 film; cure at 80 °C for 2 h (cold-cure compatible adhesive variant)

---

## §4 SEACU Mounting

| Parameter | Value |
|---|---|
| Location | Forward avionics bay, rack position 3A–3B (4-MCU size) |
| Mass | 32 kg (SEACU + MPPT modules + cooling) |
| Mounting | 4-point bolt pattern (M8 Ti fasteners); DO-160G Section 8 Category B vibration envelope |
| Vibration isolation | None (rack-mounted); rack has internal elastomeric anti-vibration dampers |
| Cooling | Forced air cooling 80 CFM (bay cooling fans); SEACU front panel exhaust grille |
| EMC gasket | Beryllium copper finger spring gasket on all panel seams; DO-160G Section 21 |
| Access | Front panel removable (2 quarter-turn fasteners) for MPPT module replacement |

---

## §5 BLI Fan Duct Structural Design

### 5.1 Duct Structure

| Component | Material | Thickness | Joins |
|---|---|---|---|
| Intake lip (external) | Ti-6Al-4V | 3 mm | Machined from billet; bolted to duct forward frame |
| Intake duct body | CFRP 8-ply quasi-isotropic | 2.5 mm | Co-cured with fuselage frame inserts |
| Fan case (containment ring) | Al 7075-T73 | 8 mm | Bolted to aft fuselage bulkhead Frame 72 |
| Exhaust duct | CFRP 6-ply | 2 mm | Bonded to fan case aft flange |
| Acoustic liner | Honeycomb foam core | 15 mm | Bonded to duct inner surface; 60–5 000 Hz absorption |

### 5.2 Bird Strike (CS-25.631)

Bird mass: 1.8 kg (medium bird); impact at Vd − 15 kn (design dive speed minus 15 kn); normal angle to intake plane.

- Titanium lip minimum gauge (3 mm Ti-6Al-4V) provides energy absorption per CS-25.631 without structural collapse
- Fan containment ring (8 mm Al 7075) sized for blade-off containment (max blade tip at 15 000 RPM, 40 kW PMSM torque)
- Post-bird-strike: duct may sustain permanent deformation; structural integrity (no separation) required per CS-25.631(b); fan may not continue to operate after strike

### 5.3 Fan Motor Mount

- 4-point mount to Frame 72 (primary aft fuselage bulkhead)
- Mount fitting: Ti-6Al-4V, fail-safe (any 3 of 4 mounts carry 150 % design limit load)
- Vibration isolation: elastomeric pads (SIA VibroMount or equivalent); attenuation −30 dB at 250 Hz (fundamental fan BPF)

---

## §6 SiC Inverter Thermal Management

### 6.1 Thermal Budget (per inverter at 50 kW)

| Parameter | Value |
|---|---|
| Power dissipation (η = 97 %) | 1.5 kW per inverter |
| SiC junction temperature target | Tj ≤ 125 °C (rated limit 175 °C; 50 °C margin) |
| Case-to-coolant thermal resistance (Rth_ca) | 0.02 °C/W (copper cold plate, EGW coolant) |
| Coolant temperature (ATLAS 074 EGW loop) | 50 °C max |
| Junction-to-case resistance (Rth_jc) | 0.03 °C/W (per switch) |
| Thermal paste | Shin-Etsu X-23 (0.1 mm, 6.5 W/m·K) |
| **Estimated Tj at 50 kW, 50 °C coolant** | **50 + (1 500 × 0.02) + (1 500 × 0.03) = 50 + 30 + 45 = 125 °C** |

> **Note:** Tj = 125 °C exactly meets design limit. If coolant temperature exceeds 50 °C (ATLAS 074 alarm threshold T2), SEACU reduces inverter output power to maintain Tj ≤ 125 °C.

### 6.2 Thermal Interface Design

- SiC module baseplate lapped to Ra < 0.4 µm
- Cold plate: aluminium with micro-channel etching; EGW coolant flow 3 L/min per inverter
- Coolant circuit: dedicated branch from ATLAS 074 MICL (Motor Inverter Cooling Loop); flow control via SEACU-commanded solenoid valve
- Overheat protection: SEACU derate inverter at Tj > 115 °C; trip inverter SSPC at Tj > 135 °C

---

## §7 Fuel System Exclusion Zones

Per AMPEL360E airframe ICD, no SEA electrical equipment (PV wiring, MPPT cables, SCAP bus bars, battery) may be routed within 150 mm of any fuel tank wall, fuel vent line, or fuel system component without approved fire-resistant conduit and FAR 25.953 / CS-25.953 separation.

| SEA Component | Nearest Fuel Element | Minimum Separation | Status |
|---|---|---|---|
| Wing upper skin PV wiring (rib 2–18) | Wing fuel tank upper cover | 300 mm (fuel tank inner flange to PV wiring outer) | Compliant (wing box sealed) |
| MPPT input cables (wing to fuselage) | Wing-to-fuselage fuel transfer line | 200 mm (separate conduit) | Compliant (dedicated SEA conduit) |
| SCAP bank (under-floor centre) | Centre fuel tank | 500 mm (SCAP in non-fuel zone) | Compliant |

---

## §8 Lightning Protection

| Zone | Lightning Attachment Probability | Protection Measure |
|---|---|---|
| Wing tip PV (winglet, CH-6) | Zone 1A (initial attachment) | Embedded copper mesh in panel laminate (36 g/m²); surge arrestor 10 kA on CH-6 MPPT input |
| Wing upper skin PV | Zone 2A (swept) | Copper mesh; arrester on each MPPT channel input |
| Fuselage crown PV | Zone 2B (swept/final) | Copper mesh; arrestors; panel frame bonded to longeron |
| BLI duct intake | Zone 1A potential (aft) | Titanium intake lip (conductive); electrically bonded to airframe; 50 Ω max bonding resistance |
| SEACU (forward bay) | Indirect effects only | DO-160G Section 22 Level 3 shielding (cabinet); all cable shields bonded at single point |

---

## §9 Structural Weight Allocation

| SEA Component | Mass (kg, estimated) |
|---|---|
| PV panels and laminates (44 panels, 24 m²) | 18 |
| PV wiring, junction boxes, conduits | 8 |
| MPPT converter modules (6×) | 12 |
| SEACU chassis and electronics | 20 |
| SCAP bank assembly | 28 |
| Li-Ion battery subset (50 kWh) | 210 |
| Bidirectional DC/DC converters (2×) | 10 |
| SiC inverter assemblies (4×) | 16 |
| BLI fan units (2× PMSM + fan + nacelle) | 80 |
| BLI duct structure (2× Ti lip + CFRP duct + mount) | 30 |
| Cables — propulsor feeds (2×, 2/0 AWG, 15 m each) | 14 |
| Cooling circuit additions (cold plates, fittings) | 6 |
| Miscellaneous brackets, fasteners, shielding | 8 |
| **Total SEA structural/installation mass** | **460 kg** |
| Less battery subset (accounted in ATLAS 072) | −210 |
| **Net SEA-specific mass addition** | **250 kg** |

> **Target:** 250 kg (original 180 kg target revised upward to 250 kg to accommodate SCAP bank — open issue OI-083-070-001).

---

## §10 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-083-070-001 | Weight reduction plan: SCAP bank aluminium housing → CFRP housing; target 250 kg → 200 kg | Q-STRUCTURES | PDR |
| OI-083-070-002 | PV panel bond fatigue test programme (5 000 thermal cycles) — coupon design and test schedule | Q-STRUCTURES | PDR |
| OI-083-070-003 | BLI duct aero-structural interaction (pressure load distribution at FL350 cruise + gust) — FE analysis | Q-STRUCTURES | CDR |
| OI-083-070-004 | Lightning qualification (DO-160G Section 22 Level 4) for SEACU — test lab scheduling | Q-INDUSTRY | CDR |
