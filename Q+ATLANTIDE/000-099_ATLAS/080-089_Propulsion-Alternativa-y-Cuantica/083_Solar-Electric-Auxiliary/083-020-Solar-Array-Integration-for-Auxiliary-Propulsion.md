---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-083-020-SOLAR-ARRAY-INTEGRATION-FOR-AUXILIARY-PROPULSION"
register: ATLAS-1000
title: "Solar Array Integration for Auxiliary Propulsion"
ata: "ATLAS-083 (Solar-Electric Auxiliary)"
sns: "083-020-00"
subsection: "083"
subsubject_code: "020"
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
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0083-020"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-083-020-SOLAR-ARRAY-INTEGRATION-FOR-AUXILIARY-PROPULSION
     ATLAS-083 (Solar-Electric Auxiliary) · Solar Array Integration
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Solar Array Integration for Auxiliary Propulsion

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

This document defines the agnostic ATLAS standard-level architecture context for `Solar Array Integration for Auxiliary Propulsion`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 Applicability

| Applicability Level | Rule |
|---|---|
| Standard taxonomy | Applies to the ATLAS node `083` |
| Programme implementation | Conditional; determined by programme architecture, trade studies, certification basis, and applicability model |
| Product configuration | Defined in the programme-specific configuration baseline |
| Effectivity | Defined in the programme CSDB / applicability layer |
| Non-applicability | Must be explicitly stated in the programme impact-study branch when excluded |
## §3 PV Panel Area Allocation

| Zone | Area (m²) | Panel Count | MPPT Channel | Orientation |
|---|---|---|---|---|
| Upper fuselage crown (FR 20–FR 60) | 8.0 | 12 panels | CH-1, CH-2 | Near-horizontal; shaded by engines < 5° yaw |
| Wing upper skin — inboard (rib 0–rib 8) | 8.0 | 16 panels | CH-3, CH-4 | 5° dihedral; optimised for FL350 cruise incidence |
| Wing upper skin — outboard (rib 8–rib 18) | 6.0 | 12 panels | CH-4, CH-5 | 7° dihedral; highest irradiance at cruise |
| Winglet upper surface | 2.0 | 4 panels | CH-6 | Near-vertical; optimises for low-sun angles |
| **Total active area** | **24.0** | **44 panels** | **6 channels** | — |

---

## §4 Cell Technology

| Parameter | GaAs Triple-Junction (Selected) | CIGS (Alternative) | Si Monocrystalline (Reference) |
|---|---|---|---|
| AM1.5 efficiency (η) | 31 % | 18 % | 24 % |
| Temperature coefficient (Pmax) | −0.21 %/°C | −0.36 %/°C | −0.40 %/°C |
| Cell thickness | 100 µm (epitaxial lift-off) | 2 µm (thin film) | 150–200 µm |
| Radiation hardness | Excellent (space heritage) | Moderate | Poor above FL400 |
| Areal mass | 0.6 kg/m² | 0.4 kg/m² | 1.2 kg/m² |
| Justification | Best η and temperature coefficient for high-altitude; GaAs sub-cells tuned to AM0 spectrum at FL350 | Lower cost but insufficient η to meet 120 kW target on 24 m² | Insufficient η; excessive mass |

---

## §5 Laminate Construction

Each PV panel is a **glass/CFRP pre-preg sandwich laminate** comprising the following layers (outer to inner):

1. **Anti-reflection coated borosilicate cover glass** — 0.3 mm; transmittance > 93 %; impact resistant per ASTM F1830
2. **Silicone encapsulant** — 0.15 mm; UV-stable; electrically isolating; accommodates CTE differential
3. **GaAs TJ cell array** — 100 µm epitaxial cells; series-parallel string per panel; bypass diodes (one per sub-string of 6 cells, Schottky, 10 A reverse current)
4. **Silicone encapsulant** (rear) — 0.15 mm
5. **Fibre pre-preg substrate** — 0.5 mm CFRP (quasi-isotropic); provides panel stiffness
6. **Adhesive bond layer** — 0.12 mm epoxy film (FM-300); panel-to-skin bonding
7. **[PROGRAMME-AIRCRAFT] outer skin CFRP** — primary structure (not modified)

**CTE mismatch management:** GaAs CTE (5.7 ppm/°C) vs. CFRP (1–3 ppm/°C). Differential CTE induces peel stress at bond line. Analysis target: peel stress < 0.5 MPa at −55 °C; accommodated by compliant silicone encapsulant and controlled panel aspect ratio (max 600 mm × 400 mm per panel).

---

## §6 MPPT Architecture

| Channel | Zone(s) Served | Topology | Input Voltage Range | Output Voltage | Rated Power |
|---|---|---|---|---|---|
| CH-1 | Fuselage crown — forward | Synchronous boost | 40–120 V DC | 700 V DC link | 20 kW |
| CH-2 | Fuselage crown — aft | Synchronous boost | 40–120 V DC | 700 V DC link | 20 kW |
| CH-3 | Wing inboard port | Synchronous boost | 40–120 V DC | 700 V DC link | 20 kW |
| CH-4 | Wing inboard stbd + outboard port | Synchronous boost | 40–120 V DC | 700 V DC link | 20 kW |
| CH-5 | Wing outboard stbd | Synchronous boost | 40–120 V DC | 700 V DC link | 20 kW |
| CH-6 | Winglets (port + stbd) | Synchronous boost | 30–80 V DC | 700 V DC link | 10 kW |

**MPPT algorithm:** Perturb-and-Observe (P&O) with variable step size; step size adapted based on irradiance rate-of-change estimate (weather feed from EPMS). Tracking speed: 10 ms per P&O cycle. Partial shading: independent MPPT per channel prevents string-to-string mismatch losses.

---

## §7 String Sizing and Bypass Diode Strategy

Each panel contains two series strings of 24 cells (Voc ≈ 66 V per string, Vmp ≈ 58 V). Two strings per panel are wired in parallel, giving panel output: Vmp ≈ 58 V, Imp ≈ 3.1 A, Pmp ≈ 180 W (STC). Panels are wired in series groups of 2 (Vmp ≈ 116 V) then in parallel groups to each MPPT channel.

**Bypass diodes:** One Schottky bypass diode per sub-string of 6 cells (4 diodes per string × 2 strings = 8 diodes per panel). Reverse current rating 10 A; forward voltage ≤ 0.45 V at 5 A; operating range −55 °C to +125 °C.

**Blocking diodes:** One per MPPT input branch (panel group), preventing reverse current from DC link into partially shaded strings. Rating: 600 V, 15 A, Schottky.

---

## §8 Bus Bar Routing and Electrical ICD

- PV string wiring: 14 AWG twisted-pair, silicone insulated, rated 600 V DC; routed in dedicated conduit below panel substrate, thermally isolated from fuel system.
- Junction boxes at FR 20 (fuselage forward), rib 0 (wing root), rib 18 (wing tip) consolidate string outputs and connect to dedicated MPPT input cables.
- MPPT input cables: 10 AWG, 600 V DC rated, shielded; routed through wing-to-fuselage fairings to SEACU bay.
- Grounding and bonding: PV panel frames bonded to airframe structure per DO-160G Section 22; shield drain connected at single point (SEACU chassis) to prevent ground loops.

---

## §9 Aerodynamic Smoothness Requirements

| Requirement | Value | Rationale |
|---|---|---|
| Panel surface waviness (wave height) | ≤ 0.5 mm per 300 mm chord | Laminar flow preservation on wing upper surface |
| Panel step height at leading edge | ≤ 0.2 mm (feathered) | Forward-facing step transition; laminar-turbulent trigger management |
| Panel step height at trailing edge | ≤ 0.5 mm (backward-facing) | Less critical; drag increment acceptable |
| Inter-panel gap | ≤ 1.0 mm | Prevent localised separation at gaps |
| Surface finish | Ra ≤ 0.8 µm (64 µin) | Per [PROGRAMME-AIRCRAFT] skin finish standard |

---

## §10 Thermal Effects on PV Efficiency

Panel operating temperature at FL350 under cruise solar loading:

| Condition | Panel Temp (°C) | Efficiency Δ vs. STC | Net η |
|---|---|---|---|
| Ground, no airflow, full sun | +65 | −8.4 % | 22.6 % |
| FL100 cruise, M 0.4 | +35 | −2.1 % | 28.9 % |
| FL350 cruise, M 0.78 (design point) | +20 | +1.05 % | **32.05 %** |
| FL350, night (reference) | −40 | — | N/A |

Temperature coefficient applied: **−0.21 %/°C** (Pmax) relative to STC 25 °C.

---

## §11 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-083-020-001 | Peel stress analysis under −55 °C / +85 °C thermal cycling (5 000 cycles) — confirm 0.5 MPa limit | Q-STRUCTURES | PDR |
| OI-083-020-002 | Aerodynamic drag increment from panel step height — CFD validation | Q-STRUCTURES | CDR |
| OI-083-020-003 | Lightning attachment zone analysis for wing tip PV panels (winglet CH-6) — surge arrestor sizing | Q-INDUSTRY | PDR |
| OI-083-020-004 | MPPT algorithm qualification under rapid irradiance change (cloud entry/exit transient < 100 ms) | Q-HPC | CDR |
