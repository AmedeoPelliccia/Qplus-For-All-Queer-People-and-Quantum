---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-082-010-PLASMA-PROPULSION-BASELINE-AND-SCOPE"
register: ATLAS-1000
title: "Plasma Propulsion Baseline and Scope"
ata: "ATLAS-082 (Plasma and Ionic Propulsion Concepts)"
sns: "082-010-00"
subsection: "082"
subsubject_code: "010"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HORIZON, Q-HPC, Q-STRUCTURES]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0082-010"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-082-010-PLASMA-PROPULSION-BASELINE-AND-SCOPE
     ATLAS-082 (Plasma and Ionic Propulsion Concepts) · Plasma Propulsion Baseline and Scope
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Plasma Propulsion Baseline and Scope

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-082 Plasma & Ionic](https://img.shields.io/badge/ATLAS--082-Plasma%20%26%20Ionic%20Propulsion-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-teal)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Plasma Propulsion Baseline and Scope`.

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
## §3 Mission Trade Space

The PIPC programme targets three distinct mission roles for the programme-defined aircraft type research platform:

**Role A — Drag-Reduction Plasma Actuation (DRPA):** Dielectric barrier discharge (DBD) plasma actuators distributed along the wing leading edge and nacelle lip generate ionic wind and boundary layer energisation, delaying flow separation and reducing skin-friction drag by an estimated 3–7 % under cruise conditions (M 0.78, FL 350). This role requires low power (< 2 kW total) and does not consume propellant.

**Role B — Auxiliary Ionic Thrust (AIT):** Hall-effect thrusters (HET) installed at the aft fuselage provide supplementary thrust of 0.5–2.5 N total for extended cruise segments where primary turbofan throttle reduction is desirable. Propellant (Xe) is consumed at 0.1–0.5 mg/s per thruster.

**Role C — Research Demonstration (RD):** Gridded ion engines (GIE) are operated on dedicated test flight segments to characterise in-flight plasma plume behaviour, EMC impact, and structural thermal loading for future programme phase assessments.

### 3.1 Technology Selection Summary

| Technology | Role | Thrust Range | Isp Range | Power per Unit | Propellant |
|---|---|---|---|---|---|
| DBD Plasma Actuator | A | N/A (drag reduction) | N/A | 100–500 W | None |
| Hall-Effect Thruster (HET) | B | 50–500 mN | 1 500–3 000 s | 1–6 kW | Xe (or Kr) |
| Gridded Ion Engine (GIE) | C (research) | 10–250 mN | 2 500–5 000 s | 0.5–3 kW | Xe |
| MPD Thruster (future) | TBD | 0.5–5 N | 1 000–8 000 s | 50–200 kW | Xe / H₂ |

MPD thrusters are noted as a **future concept** pending HVDC power budget expansion (requires > 50 kW, currently not available on programme-defined aircraft type HVDC 270 V bus at research phase).

---

## §4 Performance Baseline

| Parameter | Minimum (Design Floor) | Target | Stretch Goal |
|---|---|---|---|
| Total Auxiliary Thrust (Role B) | 0.5 N | 2.0 N | 4.0 N |
| HET Specific Impulse | 1 500 s | 2 000 s | 2 500 s |
| GIE Specific Impulse | 2 500 s | 3 500 s | 5 000 s |
| Total Propellant Load (Xe) | 8 kg | 12 kg | 20 kg |
| Total Plasma Propulsion Power | 5 kW | 12 kW | 15 kW |
| DRPA Drag Reduction | 2 % | 5 % | 7 % |
| Thruster Lifetime (HET) | 5 000 h | 8 000 h | 12 000 h |
| Thruster Lifetime (GIE) | 8 000 h | 15 000 h | 20 000 h |

---

## §5 Propellant Budget

| Item | Xe Mass (kg) | Notes |
|---|---|---|
| 4× HET operational load (Role B, 500 h/unit) | 7.2 | 0.3 mg/s × 4 × 500 h × 3 600 s/h |
| 4× GIE research load (Role C, 200 h/unit) | 2.9 | 0.1 mg/s × 4 × 200 h × 3 600 s/h |
| System contingency (10 %) | 1.0 | |
| **Total nominal Xe load** | **11.1** | Rounded to 12 kg per §10 budget |
| Reserve (no-fly abort budget) | 1.0 | Xe vessel retained for ground disposal |

---

## §6 Power Budget

| Consumer | Nominal Power (kW) | Peak Power (kW) | Source |
|---|---|---|---|
| 4× HET (Role B, full throttle) | 12.0 | 15.0 | HVDC 270 V via PPPU |
| 4× GIE (Role C, nominal) | 4.0 | 6.0 | HVDC 270 V via PPPU |
| DBD Plasma Actuators (Role A) | 1.5 | 2.0 | HVDC 270 V via PPPU |
| PPPU internal losses (η = 0.93) | 0.9 | 1.1 | — |
| **PPPU total draw from HVDC 270 V** | **14.0 (HET+DBD)** | **16.1 (all, not concurrent)** | HVDC 270 V bus |

> **Note:** All three roles are **not operated concurrently**. The maximum simultaneous draw is Role B (HET) + Role A (DBD) = 13.5 kW, within the 15 kW PPPU rated input.

---

## §7 Technology Readiness Levels (TRL)

| Technology | Current TRL | Target TRL (Phase 2) | Limiting Factor |
|---|---|---|---|
| HET — xenon, 500 mN class | TRL 5 (lab demonstration) | TRL 7 (prototype aircraft) | Plume impingement certification, Xe ATEX |
| GIE — xenon, 250 mN class | TRL 5 | TRL 6 (aircraft ground test) | EMC qualification, grid erosion life |
| DBD Plasma Actuator | TRL 4 (sub-scale wind tunnel) | TRL 6 (full-scale flight test) | Power density, electrode durability |
| MPD Thruster | TRL 3 (concept study) | TRL 5 (Phase 3) | Power availability (> 50 kW required) |

---

## §8 Interfaces

| Interface | Connected System | Protocol | Data |
|---|---|---|---|
| Power supply | HVDC 270 V — ATLAS 073 | HVDC cable | Up to 15 kW input to PPPU |
| Thrust integration | FADEC — ATA 73 | AFDX VL-082-03 | Advisory thrust increment report (no primary loop) |
| Propellant monitoring | CMS — ATA 45 | AFDX VL-082-01 | Xe mass remaining, manifold pressure, XMFC health |
| Research data | EPMS | AFDX VL-082-02 | Full performance telemetry, plume diagnostics |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-082-010-001 | Krypton propellant trade: cost vs. Isp benefit vs. ATEX certificate impact | Q-GREENTECH | PDR |
| OI-082-010-002 | HET throttle schedule integration with FADEC fuel burn optimisation | Q-HORIZON | CDR |
| OI-082-010-003 | DBD actuator scaling from sub-scale wind tunnel to full wing chord | Q-GREENTECH | Phase 2 |
