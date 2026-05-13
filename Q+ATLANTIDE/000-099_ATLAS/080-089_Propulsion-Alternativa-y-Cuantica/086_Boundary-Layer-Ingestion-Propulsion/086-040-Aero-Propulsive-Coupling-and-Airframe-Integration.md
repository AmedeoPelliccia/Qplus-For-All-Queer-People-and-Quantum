---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-086-040-AERO-PROPULSIVE-COUPLING-AND-AIRFRAME-INTEGRATION"
register: ATLAS-1000
title: "Aero-Propulsive Coupling and Airframe Integration"
ata: "ATLAS-086 (Boundary Layer Ingestion Propulsion)"
sns: "086-040-00"
subsection: "086"
subsubject_code: "040"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-HORIZON, Q-GREENTECH, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0086-040"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-086-040-AERO-PROPULSIVE-COUPLING-AND-AIRFRAME-INTEGRATION
     ATLAS-086 (Boundary Layer Ingestion Propulsion) · Aero-Propulsive Coupling and Airframe Integration
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Aero-Propulsive Coupling and Airframe Integration

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-086 BLI Propulsion](https://img.shields.io/badge/ATLAS--086-BLI%20Propulsion-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-STRUCTURES](https://img.shields.io/badge/Q--Division-Q--STRUCTURES-orange)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

ATLAS subsubject 086-040 defines the aero-propulsive coupling model, the thrust–drag bookkeeping methodology, the structural attachment of the BLI propulsor assemblies to the aft fuselage, and the interfaces with the broader airframe aerodynamic and structural models.

---

## §2 Aero-Propulsive Coupling Model

### 2.1 Thrust–Drag Bookkeeping

BLI propulsion requires a non-standard thrust–drag bookkeeping because the BLI fan simultaneously produces thrust and modifies the airframe boundary-layer drag. The AMPEL360E eWTW uses the **Power Balance Method (PBM)** as the primary bookkeeping framework:

| Term | Symbol | Value (Cruise) | Notes |
|---|---|---|---|
| Net propulsive force (NPF) | F_N | 12.5 kN (per propulsor) | Fan exit momentum − inlet capture drag |
| BLI wake ingestion credit | ΔD_wake | −1.8 kN (per propulsor) | Drag reduction from momentum re-energisation |
| Inlet installation drag | D_install | +0.35 kN (per propulsor) | Ram drag + external wetted area |
| Net BLI benefit (per propulsor) | F_net | 1.45 kN drag reduction | NPF credit minus installation penalty |
| Combined BLI drag reduction | ΔD_total | −2.90 kN | Both propulsors; ~5.8 % of total fuselage drag |

### 2.2 Power Balance Equation

```
Φ_jet = Φ_shaft − Φ_dissipation − Φ_BL_kinetic_loss
```

where:
- **Φ_jet** = jet kinetic power (useful thrust work)
- **Φ_shaft** = PMSM shaft mechanical power input (120 kW each)
- **Φ_dissipation** = viscous dissipation in S-duct + fan stage
- **Φ_BL_kinetic_loss** = kinetic energy of ingested BL flow (recovered by fan)

The BL kinetic energy recovery constitutes approximately **18 %** of shaft power at cruise, which is the primary source of the BLI efficiency benefit vs. a podded equivalent fan.

---

## §3 Airframe Structural Integration

### 3.1 Structural Attachment

Each BLI propulsor assembly attaches to the aft fuselage at **four hardpoints** on the pressure-vessel bulkhead at FS 43.5 m (rear pressure bulkhead). The attachment uses:

| Hardpoint | Load Path | Fastener | Notes |
|---|---|---|---|
| HP-086-A (upper fwd) | Fan axial thrust | 4× M12 Ti-6Al-4V bolts | Primary thrust path |
| HP-086-B (upper aft) | Fan axial + torque | 4× M12 Ti-6Al-4V bolts | Torque reaction path |
| HP-086-C (lower port) | Lateral load | 4× M12 Ti-6Al-4V bolts | Lateral stiffness |
| HP-086-D (lower stbd) | Lateral + vertical | 4× M12 Ti-6Al-4V bolts | Combined lateral/vertical |

### 3.2 Load Cases

| Load Case | Fan Thrust (kN) | Side Load (kN) | Vertical Load (kN) | Factor |
|---|---|---|---|---|
| Cruise normal | 12.5 | 0 | 1.2 (gravity) | 1.0 |
| Manoeuvre 2.5g | 12.5 | 0 | 3.0 | 2.5 |
| Gust + yaw 15° | 12.5 | 4.5 | 1.2 | 1.0 |
| Fan blade-off (IBR-2) | 0 (shut down) | 18.0 (impulse) | 0 | Ultimate |
| Hard landing 3 m/s | 12.5 | 0 | 6.0 | 1.5 |

---

## §4 Aerodynamic Interaction Effects

### 4.1 Fuselage Upwash and Inflow Angle

At angles of attack > 4°, the aft fuselage upwash modifies the effective inflow angle at the BLI inlet aperture. The BLICU accounts for this via an **AoA correction table** loaded from the FADEC AoA signal (AFDX VL-086-01):

| AoA (°) | Inflow Angle at Inlet (°) | DC60 Correction | BLICU Speed Trim |
|---|---|---|---|
| 0 | 0.5 | 0 | Nominal |
| 4 | 2.8 | +0.02 | −150 RPM |
| 8 | 6.1 | +0.05 | −300 RPM |
| 12 | 9.5 | +0.09 | BLI caution mode |

### 4.2 Propulsor–Airframe Interference Drag

Installation of the BLI nacelle on the aft fuselage creates a small interference drag increment:

| Item | ΔCD × 10⁻⁴ | Notes |
|---|---|---|
| Nacelle–fuselage junction fairing | −1.8 | Net favourable (favourable pressure gradient) |
| OGV and nozzle base drag | +0.9 | |
| Bypass door (closed) external drag | +0.3 | |
| **Net installation ΔCD** | **−0.6** | **Favourable net — junction fairing dominant** |

---

## §5 CG and Mass Properties

| Assembly | Mass (kg) | CG Location (FS m) |
|---|---|---|
| BLI-PA-1 (fan + PMSM) | 148 | FS 43.1 |
| BLI-PA-2 (fan + PMSM) | 148 | FS 43.1 |
| MCU-086-1 and MCU-086-2 | 22 each | FS 41.5 (aft avionics bay) |
| S-duct inlets (× 2) | 68 each | FS 41.6 |
| BLICU | 8 | FS 41.5 |
| **BLI system total** | **494 kg** | **FS 42.9** |

> CG shift due to BLI system relative to OEW reference: **−0.12 m** (aft shift from OEW CG at FS 21.4 m).

---

## §6 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-086-040-001 | PBM validation with full-vehicle CFD — aero-propulsive coupling map freeze | Q-HORIZON | CDR |
| OI-086-040-002 | Blade-off impulse load — dynamic FEM transient analysis for aft bulkhead | Q-STRUCTURES | Phase 2 |
| OI-086-040-003 | CG shift assessment — impact on AMPEL360E centre-of-gravity envelope | Q-STRUCTURES | PDR |
| OI-086-040-004 | AoA correction table validation — flight simulation data required | Q-GREENTECH | CDR |
