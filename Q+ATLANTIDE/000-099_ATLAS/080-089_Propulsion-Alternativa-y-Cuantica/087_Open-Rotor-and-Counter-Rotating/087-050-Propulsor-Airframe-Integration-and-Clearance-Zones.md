---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-087-050-PROPULSOR-AIRFRAME-INTEGRATION-AND-CLEARANCE-ZONES"
register: ATLAS-1000
title: "Propulsor Airframe Integration and Clearance Zones"
ata: "ATLAS-087 (Open Rotor and Counter-Rotating)"
sns: "087-050-00"
subsection: "087"
subsubject_code: "050"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-GREENTECH, Q-HORIZON, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0087-050"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-087-050-PROPULSOR-AIRFRAME-INTEGRATION-AND-CLEARANCE-ZONES
     ATLAS-087 (Open Rotor and Counter-Rotating) · Propulsor Airframe Integration and Clearance Zones
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Propulsor Airframe Integration and Clearance Zones

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

ATLAS subsubject 087-050 defines the airframe integration architecture for the ORCR propulsor at the aft fuselage pylon stations, including the pylon structural interface, ground clearance envelopes, FOD (Foreign Object Damage) exclusion zones, blade-tip sweep zones, and integration loads transmitted to the fuselage.

---

## §2 Pylon Station Definition

The ORCR pusher propulsors are installed at two symmetrical aft fuselage pylon stations:

| Station | Designation | Fuselage Frame Station | Height above fuselage CL | Lateral offset |
|---|---|---|---|---|
| Port | P-AFT-PORT | FS 2185 | +0.60 m above CL | −3.20 m (port) |
| Starboard | P-AFT-STBD | FS 2185 | +0.60 m above CL | +3.20 m (stbd) |

**Pylon Configuration:** Swept aft pylon (30° aft sweep from vertical), titanium primary structure, composite fairing. Pylon length (nacelle face to fuselage attach): 1.85 m.

---

## §3 Ground Clearance Envelope

| Configuration | FR Tip Clearance to Ground | AR Tip Clearance to Ground | Requirement |
|---|---|---|---|
| Maximum Ramp Weight (MRW), nominal tyre | 1.35 m | 1.22 m | ≥ 1.2 m (CS-25.939) |
| MRW, worn tyre (−50 mm) | 1.30 m | 1.17 m | ≥ 1.2 m |
| MRW, flat tyre (−100 mm) | 1.25 m | 1.12 m | FOD zone expanded; taxi speed limit 5 kt |
| Operating Empty Weight (OEW) | 1.60 m | 1.47 m | Nominal |

**Note:** The AR blade tips define the critical minimum clearance due to the shorter tip radius (1.85 m) combined with the lower pylon attach height. The flat-tyre case drives a taxi-speed restriction and is addressed in the MEL (Minimum Equipment List) under ORCR-MEL-087-TC.

---

## §4 Blade-Tip Sweep Zone

The rotating blade planes define exclusion zones that must be free of all personnel, GSE, and airfield infrastructure during engine operation.

| Zone | Radius | Axial Extent | Restriction |
|---|---|---|---|
| FR blade-tip sweep zone | 2.1 m (tip + 100 mm) | FR hub plane ± 0.4 m | No personnel; no GSE within zone during engine run |
| AR blade-tip sweep zone | 1.95 m (tip + 100 mm) | AR hub plane ± 0.4 m | As FR |
| Combined ORCR exclusion zone | 2.1 m radius | Entire FR–AR axial extent (1.4 m) | ORCR EXCLUSION ZONE: demarcated on ramp by red painted arc |

---

## §5 FOD Exclusion Zone

The open rotor configuration is inherently sensitive to Foreign Object Ingestion (FOI) or Foreign Object Damage (FOD) due to the absence of an inlet duct. The ORCR FOD management strategy establishes:

- **Runway / taxiway FOD sweep:** Pre-departure runway inspection within 5 m of aircraft centre-line for ORCR-equipped aircraft
- **Ramp sweep zone:** 15 m radius from AR tip — mandatory FOD check before engine start
- **Pylon fairing protection:** Titanium leading-edge strips on pylon fairing inboard face; replaceable
- **FOD sensor:** Millimetre-wave radar FOD detector (FODR-087) mounted on forward pylon strut; feeds AWMS discrete alert in case of debris detected within 10 m of AR plane

---

## §6 Integration Loads

The ORCR transmits the following primary loads to the pylon/fuselage structure:

| Load Type | Description | Design Value | Notes |
|---|---|---|---|
| Steady thrust | FR + AR combined axial thrust | 310 kN (TOGA) | Aft-acting; transmitted through pylon thrust lug |
| Gyroscopic yaw/pitch | Yaw and pitch moments from spinning rotors | ±45 kN·m (yaw), ±30 kN·m (pitch) | At maximum yaw/pitch rate; transmitted through pylon attach |
| Blade-off transient load | Unbalance force at blade-off event | 200 kN (FR) / 160 kN (AR) — 1-per-rev | Design load per CS-25.571(e); pylon fuse fitting shears at 220 kN |
| DPGB torque reaction | Torque arm to nacelle/pylon | 120 000 N·m | Transferred through torque strut |
| Pylon drag | Aerodynamic drag of pylon + nacelle fairing | 1.8 kN (cruise) | Longitudinal; minimal |

---

## §7 Proximity to Other Systems (ATLAS-085 and ATLAS-086)

| Nearby System | Proximity | Interface Risk | Mitigation |
|---|---|---|---|
| ATLAS-085 DEP fans (aft fuselage) | DEP intake 0.9 m forward of FR plane | FR wake ingested by DEP inlets | DEP inlet screens installed; ingestion tested by CFD |
| ATLAS-086 BLI ducts (aft S-ducts) | BLI S-duct outlet 1.2 m below ORCR pylon | ORCR rotor wake interacts with BLI outflow | Aerodynamic fairing installed on nacelle underside |
| APU exhaust (tail cone) | APU exhaust port 3.5 m forward of AR plane | Hot-gas ingestion risk at idle | Confirmed outside ingestion envelope by CFD; APU shutdown before ORCR start |

---

## §8 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-087-050-001 | AR tip clearance with worn+flat tyre — confirm 1.12 m meets CS-25.939 with regulatory credit for taxi-speed restriction | Q-STRUCTURES | PDR |
| OI-087-050-002 | ORCR–DEP-085 wake interaction CFD — confirm screen sizing for DEP inlet protection | Q-HORIZON | CDR |
| OI-087-050-003 | Pylon fuse fitting load (220 kN shear) — FEA and coupon test validation | Q-STRUCTURES | CDR |
