---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-082-020-IONIC-PROPULSION-CONCEPTS-AND-OPERATING-PRINCIPLES"
register: ATLAS-1000
title: "Ionic Propulsion Concepts and Operating Principles"
ata: "ATLAS-082 (Plasma and Ionic Propulsion Concepts)"
sns: "082-020-00"
subsection: "082"
subsubject_code: "020"
primary_q_division: Q-HORIZON
support_q_divisions: [Q-GREENTECH, Q-HPC, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0082-020"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-082-020-IONIC-PROPULSION-CONCEPTS-AND-OPERATING-PRINCIPLES
     ATLAS-082 (Plasma and Ionic Propulsion Concepts) · Ionic Propulsion Concepts and Operating Principles
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Ionic Propulsion Concepts and Operating Principles

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-082 Plasma & Ionic](https://img.shields.io/badge/ATLAS--082-Plasma%20%26%20Ionic%20Propulsion-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-HORIZON](https://img.shields.io/badge/Q--Division-Q--HORIZON-orange)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Ionic Propulsion Concepts and Operating Principles`.

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
## §3 Fundamental Physics

### 3.1 Thrust Generation in Ionic Systems

An ionic or plasma thruster generates thrust by expelling charged particles (ions) at high exhaust velocity v_e. The fundamental thrust equation is:

```
F = ṁ × v_e = ṁ × Isp × g₀
```

where:
- **F** = thrust (N)
- **ṁ** = propellant mass flow rate (kg/s)
- **v_e** = effective exhaust velocity (m/s)
- **Isp** = specific impulse (s)
- **g₀** = standard gravity = 9.80665 m/s²

For a singly charged xenon ion (Xe⁺, mass m_i = 2.18 × 10⁻²⁵ kg, charge e = 1.602 × 10⁻¹⁹ C) accelerated through a potential difference V_b (beam voltage):

```
v_i = √(2 × e × V_b / m_i)
```

At V_b = 1 000 V:  v_i ≈ 38 100 m/s  →  Isp ≈ 3 885 s

This illustrates why electrostatic ion thrusters achieve Isp values orders of magnitude above chemical rockets (Isp ≈ 250–450 s) at the cost of very low thrust-to-power ratios.

### 3.2 Thrust-to-Power Ratio

```
η_t = F² / (2 × P_jet × ṁ)
```

For a HET operating at 300 V, 5 A (P = 1.5 kW), producing 90 mN:

```
T/P ≈ 60 mN/kW
```

This low T/P is the primary limitation of plasma propulsion for aviation applications, motivating the PIPC programme's focus on high-altitude, low-drag-penalty auxiliary roles rather than primary lift/thrust generation.

### 3.3 Tsiolkovsky Rocket Equation (Propellant Budget)

```
Δv = Isp × g₀ × ln(m₀ / m_f)
```

For programme-defined aircraft type auxiliary role (Δv budget ≈ 50 m/s for drag offset equivalent):
- At Isp = 2 000 s: Xe mass fraction = 0.0025 (negligible vs. aircraft mass)
- Confirms ionic propulsion is mass-efficient for small Δv augmentation tasks

---

## §4 Hall-Effect Thruster (HET) Operating Principles

A Hall-effect thruster (also known as a stationary plasma thruster, SPT) operates as follows:

1. **Propellant Injection:** Xenon gas is injected radially into an annular ceramic discharge channel from an anode at the upstream end.
2. **Electron Trapping:** A radial magnetic field (B_r ~ 10–20 mT, from external magnetic circuit) traps electrons in azimuthal ExB drift (Hall current), preventing them from streaming directly to the anode.
3. **Ionisation Zone:** The trapped electrons collide with injected Xe atoms near the exit plane, ionising them (Xe → Xe⁺ + e⁻). Ionisation rate peaks where electron density and neutral density product is maximum.
4. **Ion Acceleration:** The axial electric field E_z (~ 10–20 V/mm, established between anode and virtual cathode at the exit plane) accelerates Xe⁺ ions axially to form the thrust beam.
5. **Neutralisation:** An external hollow cathode emits electrons to neutralise the ion beam, preventing spacecraft/aircraft body charge build-up.

**Key HET parameters for programme-defined aircraft type (500 mN class):**

| Parameter | Value |
|---|---|
| Discharge voltage | 250–350 V |
| Discharge current | 10–20 A |
| Input power | 3–6 kW |
| Propellant (Xe) flow rate | 0.2–0.5 mg/s |
| Isp (nominal) | 1 800–2 400 s |
| Thrust (nominal) | 100–500 mN |
| Thruster efficiency η_t | 55–65 % |
| Channel diameter (outer) | 100 mm |

---

## §5 Gridded Ion Engine (GIE) Operating Principles

A gridded ion engine uses electrostatic ion optics for direct ion extraction and acceleration:

1. **Discharge Chamber:** Xenon is ionised in a cylindrical discharge chamber by either electron bombardment (thermionic or hollow cathode discharge) or RF excitation (radiofrequency ion engine, RIT). The discharge chamber contains a quasi-neutral Xe plasma at electron temperature Te ≈ 3–7 eV and ion density n_i ≈ 10¹⁷–10¹⁸ m⁻³.
2. **Screen Grid:** A biased screen grid (V_screen ~ +1 000 to +2 000 V relative to spacecraft/aircraft ground) confines the discharge plasma and allows ions to be drawn towards the extraction optics.
3. **Accel Grid:** An accelerator grid (V_accel ~ −150 to −300 V) below the screen grid provides the ion-optical lens function: it focuses and collimates the ion beam, suppresses backstreaming electrons.
4. **Decel Grid (optional):** A third decelerator grid (~ground potential) reduces beam divergence and controls final ion energy.
5. **Beam Neutralisation:** An external hollow cathode neutralises the extracted ion beam.

**Key GIE parameters for programme-defined aircraft type (250 mN class):**

| Parameter | Value |
|---|---|
| Screen voltage | +1 200 V |
| Accel voltage | −200 V |
| Beam current | 2.0 A |
| Input power | 2.8 kW |
| Propellant (Xe) flow rate | 0.08 mg/s |
| Isp (nominal) | 3 200 s |
| Thrust (nominal) | 250 mN |
| Thruster efficiency η_t | 70–80 % |
| Grid diameter | 30 cm |

---

## §6 Magnetoplasmadynamic (MPD) Thruster Principles

An MPD thruster accelerates plasma via electromagnetic (Lorentz) body force (J × B). The discharge current J flowing through the propellant plasma interacts with the self-induced or applied magnetic field B to produce an axial body force F = J × B. Unlike electrostatic thrusters, MPD devices can sustain high propellant throughput and thrust density, but require orders-of-magnitude higher power (> 50 kW) not currently available on the programme-defined aircraft type research platform. MPD is documented here for future programme phase reference.

---

## §7 Dielectric Barrier Discharge (DBD) Plasma Actuator Principles

DBD plasma actuators for aerodynamic flow control (Role A) operate on a fundamentally different principle from thrust-generating thrusters:

1. **Electrode Configuration:** Two asymmetric electrodes — one exposed to the flow, one encapsulated beneath a dielectric material (polyimide or ceramic) — are separated by the dielectric layer (0.5–3 mm thick).
2. **AC Excitation:** A high-voltage AC signal (2–20 kV, 1–30 kHz) applied between the electrodes creates a cold plasma (partial ionisation, Te ~ 1–3 eV, n_e ~ 10¹⁶–10¹⁸ m⁻³) at the exposed electrode edge.
3. **Ionic Wind:** Momentum transfer from ionised air molecules to neutral air via ion-neutral collisions generates a near-wall induced velocity (v_ind ~ 1–10 m/s), energising the boundary layer and delaying flow separation.
4. **No Propellant Consumed:** DBD actuators use ambient air as the working fluid; no xenon or stored propellant is required.
5. **Power Requirement:** 100–500 W per actuator panel section (wing leading edge, nacelle lip).

DBD actuators are the most near-term applicable technology for programme-defined aircraft type in-service integration due to their low risk profile and absence of stored propellant.

---

## §8 Comparative Summary

| Technology | Isp (s) | Thrust | Power | Propellant | TRL | Aviation Role |
|---|---|---|---|---|---|---|
| DBD Plasma Actuator | N/A | Drag reduction | 0.1–2 kW | None (air) | 4–5 | Flow control |
| Hall-Effect Thruster | 1 500–3 000 | 50–500 mN | 1–6 kW | Xe/Kr | 5 | Auxiliary thrust |
| Gridded Ion Engine | 2 500–5 000 | 10–250 mN | 0.5–3 kW | Xe | 5 | Research demo |
| MPD Thruster | 1 000–8 000 | 0.5–5 N | 50–200 kW | Xe/H₂ | 3 | Future |
| Turbofan (reference) | ≈ 4 000 eq. | 100–300 kN | ~20 MW | Jet-A/SAF | 9 | Primary thrust |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-082-020-001 | In-atmosphere performance correction for HET (reduced exhaust plasma diffusion in dense air) | Q-HORIZON | PDR |
| OI-082-020-002 | DBD actuator power optimisation at M 0.78 cruise Reynolds number | Q-GREENTECH | Phase 2 |
| OI-082-020-003 | GIE grid erosion model validation for Xe beam at 1 200 V — sputter yield data needed | Q-HPC | CDR |
