---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-085-050-PROPULSOR-AIRFRAME-INTEGRATION-AND-AERO-PROPULSIVE-COUPLING"
register: ATLAS-1000
title: "Propulsor Airframe Integration and Aero-Propulsive Coupling"
ata: "ATLAS-085 (Distributed Electric Propulsion Architecture)"
sns: "085-050-00"
subsection: "085"
subsubject_code: "050"
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
s1000d_dmc: "DMC-AMPEL360E-EWTW-0085-050"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-085-050-PROPULSOR-AIRFRAME-INTEGRATION-AND-AERO-PROPULSIVE-COUPLING
     ATLAS-085 (Distributed Electric Propulsion Architecture) · Propulsor Airframe Integration and Aero-Propulsive Coupling
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Propulsor Airframe Integration and Aero-Propulsive Coupling

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-085 DEP Architecture](https://img.shields.io/badge/ATLAS--085-DEP%20Architecture-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-STRUCTURES](https://img.shields.io/badge/Q--Division-Q--STRUCTURES-blue)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

ATLAS subsubject 085-050 defines the structural integration of each DEP propulsor into the AMPEL360E eWTW airframe, quantifies the aero-propulsive coupling effects (BLI efficiency gain, nacelle drag, trim drag changes), specifies the load cases for nacelle attachment structures, and establishes the aero-propulsive gain model used by the DEPCU thrust allocator and the BGSCU energy management scheduler.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA Reference | ATLAS-085 — 085-050 Propulsor Airframe Integration and Aero-Propulsive Coupling |
| Certification Basis | CS-25.571; CS-25.903(d); CS-25.307; CS-25.143; CS-25.147 |
| S1000D SNS | 085-050-00 |

---

## §3 Structural Integration Summary

| Propulsor | Attachment Structure | Load Path | Design Limit Load | Fatigue Spectrum | Notes |
|---|---|---|---|---|---|
| P1 (over-wing port) | CFRP nacelle pylon + 3-lug failsafe fitting | Wing-root rib #3; spar web | 185 kN (combined thrust + gyro) | 60 000 FC (design life) | Fan-blade-off (FBO) case governs lug sizing |
| P2 (over-wing stbd) | Mirror of P1 | Wing-root rib #3 stbd | 185 kN | 60 000 FC | Same |
| P3 (aft-fuse port) | Titanium truss frame + 4-bolt flange | Fuselage frame #68 + stringer; CFRP keel beam | 220 kN (combined) | 60 000 FC | Higher axial load due to aft moment arm |
| P4 (aft-fuse stbd) | Mirror of P3 | Fuselage frame #68 + stringer stbd | 220 kN | 60 000 FC | Same |

---

## §4 Fan-Blade-Off (FBO) Containment Requirements

Per CS-25.903(d), each nacelle must demonstrate uncontained rotor disc failure does not lead to:
- Structural failure of a primary flight control surface.
- Penetration of a pressurised fuselage zone.
- Fuel tank puncture.
- Loss of control of a second propulsor within the same half-plane.

**FBO Containment Design Provisions:**

| Propulsor | Containment Ring Material | Burst Zone Clearance | Critical Structure Avoidance |
|---|---|---|---|
| P1 | Ti-6Al-4V containment ring, 12 mm wall | ≥ 500 mm clear of wing main spar | Wing fuel tank outer wall > 1 200 mm from burst zone |
| P2 | As P1 | As P1 (mirror) | As P1 (mirror) |
| P3 | Ti-6Al-4V containment ring, 14 mm wall | ≥ 400 mm from pressure vessel frame #68 | No fuel tank within 800 mm; flight control cables rerouted to port keel |
| P4 | As P3 | As P3 (mirror) | Flight control cables rerouted to stbd keel |

---

## §5 Aero-Propulsive Coupling Model

The aero-propulsive gain model relates propulsor power to net vehicle force (thrust minus drag) accounting for BLI ingestion, nacelle inlet drag, and fan wake effects. The model is implemented in the DEPCU thrust allocator as a look-up table indexed by: Mach number (0.0–0.85), altitude (0–13 000 m), and per-propulsor shaft power (0–500 kW).

### §5.1 BLI Power Saving Coefficient (η_BLI)

The BLI power saving coefficient expresses the fractional reduction in shaft power required to produce a given thrust relative to an equivalent free-stream propulsor.

| Propulsor Pair | η_BLI (cruise M 0.78, FL 350) | η_BLI (approach, M 0.20, 300 m) | Notes |
|---|---|---|---|
| P3 + P4 (aft fuselage) | 0.12 (12 % saving) | 0.08 (8 % saving) | Thick BL at FS 1 640; highest η_BLI |
| P1 + P2 (over-wing root) | 0.04 (4 % saving) | 0.02 (2 % saving) | Thinner BL at FS 450; lower gain |

### §5.2 Nacelle Parasite Drag Coefficient

| Propulsor | ΔCD_nacelle (cruise, unflanged) | ΔCD_nacelle (TOGA) | Notes |
|---|---|---|---|
| P1 / P2 | 0.0009 each | 0.0006 each | Flush NACA inlet; low parasite |
| P3 / P4 | 0.0011 each | 0.0007 each | D-duct; slightly higher wetted area |

### §5.3 Trim Drag Impact

The aft placement of P3 and P4 produces a nose-up pitching moment at high power. The horizontal tailplane must generate a balancing download. At TOGA with P3+P4 at 500 kW each, the estimated trim drag penalty is ΔCD_trim = 0.0007, equivalent to a reduction of ~2 % in net thrust at TOGA.

---

## §6 Aero-Propulsive Gain Interaction with DEPCU Allocator

The DEPCU integrates the η_BLI look-up table into its per-propulsor torque allocator. At each 10 ms cycle, the allocator solves a constrained optimisation:

```
minimise:  Σ P_shaft_i / (η_MDU_i × η_PMSM_i × (1 + η_BLI_i))   for i = P1…P4
subject to: Σ T_net_i ≥ T_demand (from FADEC)
            T_net_P1 = T_net_P2  (symmetry constraint, normal ops)
            T_net_P3 = T_net_P4  (symmetry constraint, normal ops)
            P_shaft_i ≤ P_max_i  (MDU/PMSM thermal limit)
```

In asymmetric mode (single propulsor failure), the symmetry constraints are relaxed and the yaw moment budget from FMS is substituted.

---

## §7 Load Cases Summary

| Load Case | Description | Governing Propulsor | Max Load (kN) | Design Margin |
|---|---|---|---|---|
| LC-001 | Takeoff TOGA — max thrust, zero yaw | P3 + P4 | 220 kN (per pylon) | 1.5 DLL |
| LC-002 | Fan-blade-off at 6 600 RPM | P3 (worst case: heavier disc) | 1 100 kN (impulse) | Containment |
| LC-003 | Manoeuvre — 2.5g pull-up at Vd | All propulsors | 185 kN (P1/P2) | 1.5 DLL |
| LC-004 | Landing — 2.0g vertical; full DEP thrust | P3 + P4 | 230 kN | 1.5 DLL |
| LC-005 | Taxi — full regen braking (4× fans) | P1–P4 (regen reaction) | 40 kN reaction (combined) | 2.0 DLL |
| LC-006 | Gyroscopic — 180°/s yaw rate at max RPM | All propulsors (worst P3) | 95 kN gyro moment | 1.5 DLL |

---

## §8 Interfaces

| Interface | Connected System | Protocol | Data |
|---|---|---|---|
| Thrust demand (net vehicle) | FADEC — ATA 73 via DEPCU | AFDX VL-085-01 | Total thrust demand; phase profile |
| Yaw moment budget | FMS — ATA 22 via DEPCU | AFDX VL-085-03 | Permissible yaw moment for diff-thrust |
| Structural load monitoring | SHM (structural health monitoring) | Strain gauge CAN bus | P3/P4 pylon strain; nacelle vibration |
| Nacelle thermal interface | DEP-TML coolant loop | Physical EGW coolant lines | Motor and MDU heat rejection |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-085-050-001 | P3/P4 FBO impulse load — fuselage frame #68 ultimate load test plan | Q-STRUCTURES | CDR |
| OI-085-050-002 | η_BLI model validation — CFD high-fidelity RANS at cruise condition | Q-HORIZON | Phase 2 |
| OI-085-050-003 | Trim drag at TOGA P3+P4 max power — horizontal stabiliser sizing impact | Q-STRUCTURES | PDR |
| OI-085-050-004 | DEPCU allocator constrained optimisation solver performance — 10 ms budget | Q-HPC | CDR |
| OI-085-050-005 | Aft nacelle mount fatigue spectrum — 60 000 FC goal vs. measured taxi loads | Q-STRUCTURES | CDR |
