---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-082-050-THRUSTER-CHAMBER-GRID-AND-ELECTRODE-INTERFACES"
register: ATLAS-1000
title: "Thruster Chamber, Grid and Electrode Interfaces"
ata: "ATLAS-082 (Plasma and Ionic Propulsion Concepts)"
sns: "082-050-00"
subsection: "082"
subsubject_code: "050"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-GREENTECH, Q-HPC, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0082-050"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-082-050-THRUSTER-CHAMBER-GRID-AND-ELECTRODE-INTERFACES
     ATLAS-082 (Plasma and Ionic Propulsion Concepts) · Thruster Chamber, Grid and Electrode Interfaces
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Thruster Chamber, Grid and Electrode Interfaces

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-082 Plasma & Ionic](https://img.shields.io/badge/ATLAS--082-Plasma%20%26%20Ionic%20Propulsion-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-STRUCTURES](https://img.shields.io/badge/Q--Division-Q--STRUCTURES-brown)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Thruster Chamber, Grid and Electrode Interfaces`.

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
## §3 HET Discharge Channel Geometry

### 3.1 Annular Channel Dimensions (500 mN class HET)

| Parameter | Value |
|---|---|
| Outer diameter (D_o) | 100 mm |
| Inner diameter (D_i) | 70 mm |
| Channel width (w = (D_o − D_i) / 2) | 15 mm |
| Channel depth (L_ch) | 30 mm |
| Mean diameter (D_m) | 85 mm |
| Channel volume | ~3.8 cm³ |
| Anode–exit gap | 32 mm |
| Thruster overall envelope (D × L) | 130 mm × 90 mm |
| Mass (thruster head, without PPU) | ≤ 1.8 kg |

### 3.2 Channel Wall Material and Erosion

The discharge channel walls are fabricated from boron nitride–silicon dioxide (BN-SiO₂, grade HP) ceramic:

| Property | BN-SiO₂ Value |
|---|---|
| Thermal conductivity | 25–30 W/(m·K) |
| Max service temperature | 950 °C |
| Sputter yield (Xe⁺ at 300 eV, normal incidence) | ~0.01 atoms/ion |
| Channel erosion rate (wall recession at nominal) | ≤ 0.05 mm / 1 000 h |
| Required wall thickness (for 8 000 h life) | ≥ 0.5 mm above minimum |
| Nominal wall thickness (initial) | 4 mm |

Channel erosion is the primary life-limiting mechanism for HET. The **erosion life model** tracks cumulative ion fluence on the channel wall and predicts end-of-life (EOL) channel depth:

```
Δx_wall = (Ṅ_i × Y_sp × A_Xe) / (ρ_BN × N_A)    [m/s]
```

where Ṅ_i = ion flux on wall (m⁻² s⁻¹), Y_sp = sputter yield, A_Xe = Xe molar mass, ρ_BN = BN-SiO₂ density, N_A = Avogadro number. A channel wall recession of > 3 mm triggers a thruster life-limit alert in the PPPU health monitor.

---

## §4 GIE Grid Assembly

### 4.1 Grid Set Configuration (30 cm, 3-grid)

| Grid | Material | Thickness | Hole pattern | Voltage |
|---|---|---|---|---|
| Screen | C/C composite (PyC coated) | 0.38 mm | Hexagonal, 1.91 mm diam., 2.4 mm pitch | +1 200 V |
| Accel | C/C composite (PyC coated) | 0.51 mm | Hexagonal, 1.14 mm diam., 2.4 mm pitch | −200 V |
| Decel | Mo sheet | 0.51 mm | Hexagonal, 1.9 mm diam., 2.4 mm pitch | 0 V (ground) |

### 4.2 Grid Mounting and Alignment

Grid assembly is mounted on a **Inconel 625 grid support ring** which attaches to the downstream face of the discharge chamber via six titanium Ti-6Al-4V fasteners. Grid-to-grid alignment is maintained by ceramic (Al₂O₃) standoff insulators:

| Parameter | Value |
|---|---|
| Screen–accel gap | 0.66 mm ± 0.05 mm |
| Accel–decel gap | 3.00 mm ± 0.10 mm |
| Co-planarity tolerance (each grid) | ≤ 0.10 mm TIR |
| Lateral alignment (grid centres) | ≤ 0.25 mm |
| Grid assembly mass | ≤ 0.8 kg |
| Mounting preload (fastener) | 8 ± 1 N·m |

### 4.3 Grid Erosion Life Model

Accel grid erosion by backstreaming electrons and charge-exchange Xe⁺ ions is modelled as:

```
ṁ_erosion = J_cex × Y_sp(E_cex) × m_grid_material
```

At nominal J_cex ≈ 0.2 mA/cm² and E_cex ≈ 200 eV:
- C/C accel grid erosion rate: ~ 2 µm / 1 000 h (at aperture edge)
- Life limit: > 3.0 mm cumulative recession at accel aperture edge → grid replacement

---

## §5 Thruster Electrode Interfaces

### 5.1 HET Anode

The annular anode is machined from TZM (molybdenum-titanium-zirconium alloy) and serves as both the gas distribution manifold and the positive discharge voltage terminal:

| Parameter | Value |
|---|---|
| Material | TZM alloy (Mo–0.5Ti–0.08Zr) |
| Operating voltage | +300 V (discharge potential) |
| Max temperature | 900 °C (radiation-cooled) |
| Xenon distribution slots | 36 × azimuthal slots, 0.8 mm width |
| Electrical connection | PTFE-insulated TZM flex braid → PPPU HV+ terminal |
| Fastener isolation | Al₂O₃ washers at all mounting points |

### 5.2 HET Cathode (Hollow Cathode)

The hollow cathode assembly is mounted on the outer body of the HET via a three-point Ti-6Al-4V bracket, positioned 10 mm downstream and 15 mm radially outboard of the channel exit:

| Parameter | Value |
|---|---|
| Cathode tube material | Mo–Re alloy (2 % Re) |
| Insert material | BaO-W porous matrix |
| Orifice plate | Mo, 0.4 mm diameter orifice |
| Keeper electrode | Mo ring, +15 V above cathode potential |
| Heater | Bifilar wound W coil, 25 W, 12 V DC |
| Thermal isolation | Al₂O₃ sleeve between cathode body and bracket |

### 5.3 GIE Screen and Keeper (Hollow Cathode) Electrode

GIE screen grid potential (+1 200 V) is applied via a shielded coaxial HV cable (3 kV rated) from the PPPU HV supply module. The keeper electrode of the GIE hollow cathode is located at the downstream centreline, +15 V above cathode floating potential.

---

## §6 Airframe Mechanical Interfaces

### 6.1 HET Installation (Aft Fuselage Lower Quadrant)

| Interface | Specification |
|---|---|
| Mounting frame | Al 7075-T6 thruster pylon, bolted to aft frames FR-82A / FR-82B |
| Attach points | 4× M8 Ti-6Al-4V bolts; torque 22 ± 2 N·m |
| Gimbal provision | ±5° pitch / ±3° yaw articulation (research phase; spring-centred) |
| Thermal separation | Ti standoffs (6 mm dia.) providing 30 mm air gap to structure; radiation shield plate |
| Vibration isolation | Lord mount elastomeric isolators (fn = 20 Hz); attenuation ≥ 15 dB above 50 Hz |
| Plume clearance | 250 mm minimum from any structural surface in 30° half-angle cone |
| Propellant connection | Swaged SS316L Swagelok tube fitting, 1/4 in. OD, at thruster inlet port |
| HV cable routing | PTFE conduit along pylon; 50 mm min separation from control cables |

### 6.2 GIE Installation (Aft Nacelle Fairing)

| Interface | Specification |
|---|---|
| Mounting frame | CFRP fairing insert panel, bonded to nacelle aft frame |
| Attach points | 6× M6 Ti-6Al-4V inserts; torque 10 ± 1 N·m |
| Alignment | ± 0.5° thrust vector alignment to aircraft longitudinal axis |
| Thermal separation | Ceramic fibre blanket (Nextel 440) 12 mm behind discharge chamber |
| Vibration isolation | Sorbothane 40A pad mounts (fn ≈ 15 Hz) |
| Plume clearance | 300 mm from nacelle structure |

---

## §7 Inspection, Removal and Replacement

| Task | Interval | Procedure |
|---|---|---|
| HET channel visual inspection | 2 500 h or at every C-check | Borescope through anode gas slots; compare wall depth to erosion life chart |
| HET hollow cathode replacement | 5 000 h or on PPPU BITE alert CAT-082-HC | Remove aft fairing; disconnect HV braid and propellant tube; replace cathode assembly |
| GIE accel grid replacement | 8 000 h or on PPPU BITE alert GIE-082-GRID | Remove nacelle fairing panel; disconnect HV cable; extract grid assembly |
| COPV Xe vessel proof test | Annual or per Airworthiness Directive | Off-aircraft hydrostatic test to 225 bar with GN₂; visual inspection |
| Anode cleaning (HET) | C-check | Ultrasonic bath (deionised water + IPA); re-torque anode feed fasteners |

---

## §8 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-082-050-001 | Finalise HET pylon attachment loads (FEM analysis at 9 g crash load case per CS-25.561) | Q-STRUCTURES | CDR |
| OI-082-050-002 | GIE fairing insert bondline fatigue assessment (thermal cycle −55 °C to +120 °C, 10 000 cycles) | Q-STRUCTURES | CDR |
| OI-082-050-003 | Gimbal actuator selection and PPPU control interface for research-phase vector thrust | Q-INDUSTRY | Phase 2 |
