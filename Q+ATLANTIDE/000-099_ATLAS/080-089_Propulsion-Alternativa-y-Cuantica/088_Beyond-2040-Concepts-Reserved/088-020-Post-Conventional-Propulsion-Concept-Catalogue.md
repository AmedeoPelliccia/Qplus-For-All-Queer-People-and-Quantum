---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-088-020-POST-CONVENTIONAL-PROPULSION-CONCEPT-CATALOGUE"
register: ATLAS-1000
title: "Post-Conventional Propulsion Concept Catalogue"
ata: "ATLAS-088 (Beyond-2040 Concepts Reserved)"
sns: "088-020-00"
subsection: "088"
subsubject_code: "020"
primary_q_division: Q-HORIZON
support_q_divisions: [Q-GREENTECH, Q-HPC, Q-STRUCTURES]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0088-020"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-088-020-POST-CONVENTIONAL-PROPULSION-CONCEPT-CATALOGUE
     ATLAS-088 (Beyond-2040 Concepts Reserved) · Post-Conventional Propulsion Concept Catalogue
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Post-Conventional Propulsion Concept Catalogue

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-088 Beyond-2040](https://img.shields.io/badge/ATLAS--088-Beyond--2040%20Concepts%20Reserved-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-HORIZON](https://img.shields.io/badge/Q--Division-Q--HORIZON-purple)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Post-Conventional Propulsion Concept Catalogue`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 Catalogue Overview

The catalogue organises admitted concepts into the six technology families defined in 088-000 §3. For each concept the following fields are recorded:

| Field | Description |
|---|---|
| B2C-ID | Unique concept identifier within the family (e.g., B2C-F101) |
| Concept Name | Descriptive name |
| Physical Mechanism | Claimed physical effect driving thrust |
| TRL (2026) | Technology Readiness Level at catalogue entry |
| Status | B2C status code per 088-010 §3.2 |
| Physics Boundary Flag | Known-physics compliant (Y/N/Contested) |
| Lead Reference | Primary peer-reviewed publication or institutional report |
| B2CMU Notes | Internal review notes |

---

## §3 Family B2C-F100 — Field and Quantum-Vacuum Propulsion

| B2C-ID | Concept Name | Physical Mechanism | TRL | Status | Physics Flag | Lead Reference |
|---|---|---|---|---|---|---|
| B2C-F101 | Asymmetric EM Cavity (RF) | RF standing wave in asymmetric resonant cavity produces net thrust via radiation pressure imbalance | 2 | B2C-WATCH | Contested | Shawyer (2006); NASA White (2016, retracted); Tajmar et al. (2021, null result) |
| B2C-F102 | Mach Effect Thruster (MET) | Oscillating mass energy creates spacetime Mach transients; piezo-stack implementation | 3 | B2C-ACTIVE | Contested | Woodward (2012 book); Fearn & Woodward (2014); AIAA-2018-4867 |
| B2C-F103 | Quantum Vacuum Plasma Thruster | Claimed vacuum-fluctuation asymmetric reflection thrust; deep-vacuum experiment | 1 | B2C-WATCH | Contested | Putnam (2014); numerous null results in literature |
| B2C-F104 | Casimir Effect Micro-Thruster | Casimir pressure gradient across nano-structured plate array; nano-scale geometry | 1 | B2C-WATCH | Partially valid (Casimir force confirmed; thrust extraction mechanism contested) | Rodriguez et al. (2011); Chen & Mohideen (2020) |

**B2CMU Notes (F100 Family):** All F100 concepts require replication by a minimum of two independent laboratories with null-result uncertainty characterisation before status promotion. Current null-result weight is high. F102 (MET) shows the most consistent non-null experimental signal; Q-HORIZON to commission independent replication in 2027.

---

## §4 Family B2C-F200 — Compact Nuclear and Fusion Propulsion

| B2C-ID | Concept Name | Physical Mechanism | TRL | Status | Physics Flag | Lead Reference |
|---|---|---|---|---|---|---|
| B2C-F201 | Micro D-T Fusion Thruster | Magnetic confinement D-T fusion at micro-scale; plasma exhaust propulsion | 3 | B2C-ACTIVE | Y (physics valid; engineering feasibility contested) | ITER basis; Paluszek et al. (2020 airborne scale study) |
| B2C-F202 | Field-Reversed Configuration (FRC) Reactor | Compact FRC plasma equilibrium; self-sustaining fusion at reduced scale | 4 | B2C-PROMOTE | Y | TAE Technologies (2023 commercial plasma result) |
| B2C-F203 | Muon-Catalysed Fusion | Muons catalyse D-T fusion at near-ambient temperatures; muon source mass penalty | 2 | B2C-WATCH | Y (physics valid; energy balance negative at current muon yield) | Jones (1986); Petrov (2019 updated analysis) |
| B2C-F204 | Fission-Fragment Rocket (Airborne) | Direct fission-fragment exhaust from thin-film fissile material; extremely high Isp | 2 | B2C-WATCH | Y (physics valid; regulatory / safety constraints prohibitive for civil aviation) | Chapline (1988); Schmidt et al. (1999) |
| B2C-F205 | Aneutronic p-B11 Fusion | Proton–Boron-11 fusion; no neutron flux; charged-particle exhaust | 3 | B2C-ACTIVE | Y (physics valid; ignition temperature requirement very high) | Hora et al. (2017); Laberge (2019) |

**B2CMU Notes (F200 Family):** B2C-F202 (FRC) has reached TRL 4 in ground laboratory context (TAE Technologies 2023 result) and is eligible for promotion review. Promotion is conditional on safety case and radiological assessment per 088-070. B2C-F204 (fission-fragment) is maintained for research awareness only; civil aviation regulatory clearance is not foreseen before 2060.

---

## §5 Family B2C-F300 — Photonic and Directed-Energy Propulsion

| B2C-ID | Concept Name | Physical Mechanism | TRL | Status | Physics Flag | Lead Reference |
|---|---|---|---|---|---|---|
| B2C-F301 | Ground-Based Laser Ablation Assist | Pulsed laser ablation of ablator material on aircraft; thrust from ablation plume | 4 | B2C-ACTIVE | Y | Phipps et al. (2010); Parkin (2018 Breakthrough Propulsion study) |
| B2C-F302 | Microwave Power Beaming (MPB) | Rectenna on aircraft receives ground/orbital MW beam; powers electric propulsion | 5 | B2C-PROMOTE | Y | McSpadden & Mankins (2002); Shinohara (2021); JAXA Demos |
| B2C-F303 | Orbital Laser Propulsion (Lightsail) | Photon pressure from orbital laser sail; momentum transfer without propellant | 5 | B2C-ACTIVE | Y | Lubin (2016); Breakthrough Starshot; not applicable to atmospheric flight (noted) |
| B2C-F304 | Laser-Thermal Atmospheric Thruster | Laser heats atmospheric air; expanded hot gas provides thrust | 4 | B2C-ACTIVE | Y | Kare (1995); Myrabo (2002 PowerBeaming experiments); Cohen (2020) |

**B2CMU Notes (F300 Family):** B2C-F302 (MPB) and B2C-F301 are the highest-TRL concepts in the catalogue. B2C-F302 is promote-eligible pending safety case for continuous-wave MW beam operations over populated areas (088-070 issue). B2C-F303 applicability is limited to near-space; retained for awareness. B2C-F304 (laser-thermal) merits integration study (088-060) at reduced mission range.

---

## §6 Family B2C-F400 — Magnetohydrodynamic (MHD) Atmospheric Propulsion

| B2C-ID | Concept Name | Physical Mechanism | TRL | Status | Physics Flag | Lead Reference |
|---|---|---|---|---|---|---|
| B2C-F401 | MHD Atmospheric Accelerator | Ionised air magnetohydrodynamically accelerated through Lorentz force; no moving parts | 4 | B2C-ACTIVE | Y | Rosa (1968); Whitehead (1993); Gilland (2018 NASA) |
| B2C-F402 | Superconducting MHD Thruster | SC magnet MHD sea-water or ionised-air accelerator; silent, no rotating parts | 4 | B2C-ACTIVE | Y | Motora & Takezawa (1994 Yamato-1); Brown (2019 air adaptation) |
| B2C-F403 | Plasma Jet Magnetohydrodynamics | Lorentz-force plasma jet; distinct from ionic thruster by MHD bulk-plasma regime | 3 | B2C-ACTIVE | Y | Haas & Spores (1996); Hall-effect plasma extension into MHD regime |
| B2C-F404 | Electroaerodynamic (EAD) Body Force | Corona discharge body force on neutral air; solid-state propulsion | 5 | B2C-PROMOTE | Y | Masuyama & Barrett (2013); Xu et al. (2018 MIT EAD plane) |

**B2CMU Notes (F400 Family):** B2C-F404 (EAD) has reached TRL 5 with the MIT solid-state plane demonstration (Xu 2018) and is promote-eligible; target active subsection would be a new ATLAS subsection or extension of ATLAS-082. B2C-F401 and F402 require large superconducting magnet mass; MRL gap is large despite TRL 4. Boundary with ATLAS-082 must be clarified per OI-088-010-004.

---

## §7 Family B2C-F500 — Superconducting Motors (Room-Temperature SC)

| B2C-ID | Concept Name | Physical Mechanism | TRL | Status | Physics Flag | Lead Reference |
|---|---|---|---|---|---|---|
| B2C-F501 | HTS Axial Flux Motor (LN₂) | High-temperature SC winding; liquid-nitrogen cooled; high power density electric motor | 5 | B2C-PROMOTE | Y | Sivasubramaniam et al. (2010); Rolls-Royce HTS Motor Programme (2022) |
| B2C-F502 | Room-Temperature Superconductor Motor | RTSC (if demonstrated post-2030) motor; no cryogen; maximum power density | 1 | B2C-WATCH | Contested (RTSC unconfirmed as of 2026) | Dias et al. (2023, retracted); Snider et al. (2020); LK-99 (2023, non-replicable) |
| B2C-F503 | Superconducting Linear Induction Drive | SC linear motor for boundary-layer or rail-launch propulsion assist | 3 | B2C-ACTIVE | Y | Powell & Danby (1966 maglev basis); Thornton (2009 aircraft assist) |

**B2CMU Notes (F500 Family):** B2C-F501 (HTS motor, LN₂) is promote-eligible and closely related to DEP architecture in ATLAS-085; transition path is via ATLAS-085 extension or new subsection. B2C-F502 (RTSC motor) is B2C-WATCH pending credible independent experimental replication of any room-temperature SC material above ambient pressure; multiple prior claims have not reproduced. Annual watch review mandatory.

---

## §8 Family B2C-F600 — Space-Time Metric Engineering

| B2C-ID | Concept Name | Physical Mechanism | TRL | Status | Physics Flag | Lead Reference |
|---|---|---|---|---|---|---|
| B2C-F601 | Alcubierre Warp Drive | Local spacetime metric expansion/contraction to achieve apparent FTL travel | 1 | B2C-WATCH | N (requires exotic negative-energy matter, not demonstrated) | Alcubierre (1994); White (2013 modified energy requirement) |
| B2C-F602 | Gravitational Anomaly Thruster | Claimed coupling of EM field to gravitational field for inertia modification | 1 | B2C-WATCH | Contested (no reproducible data) | Podkletnov (1992, non-replicated); Tajmar et al. (2006 gravity modification, null result) |
| B2C-F603 | Quantum Inertia Modification | Rindler radiation / Unruh effect manipulation to reduce effective inertia | 1 | B2C-WATCH | Contested (Quantised Inertia theory; limited peer review) | McCulloch (2013, 2018) |

**B2CMU Notes (F600 Family):** All F600 concepts are maintained as **Horizon Watch only**. No programme resources are allocated. Scientific monitoring continues through Q-HORIZON literature scanning. Promotion criteria require demonstration of the claimed physical effect under controlled laboratory conditions with five independent replication events. This threshold has not been approached for any F600 concept as of 2026.

---

## §9 Concept Summary Dashboard

| Family | Total Concepts | B2C-WATCH | B2C-ACTIVE | B2C-PROMOTE | B2C-REJECT |
|---|---|---|---|---|---|
| F100 — Quantum Vacuum | 4 | 3 | 1 | 0 | 0 |
| F200 — Nuclear/Fusion | 5 | 2 | 2 | 1 | 0 |
| F300 — Photonic/Beamed | 4 | 0 | 2 | 2 | 0 |
| F400 — MHD | 4 | 0 | 3 | 1 | 0 |
| F500 — SC Motors | 3 | 1 | 1 | 1 | 0 |
| F600 — Metric Engineering | 3 | 3 | 0 | 0 | 0 |
| **Total** | **23** | **9** | **9** | **5** | **0** |

---

## §10 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-088-020-001 | Initiate independent replication programme for B2C-F102 (MET) — commission external laboratory | Q-HORIZON | 2027 |
| OI-088-020-002 | Formalise promotion review for B2C-F202 (FRC), F302 (MPB), F404 (EAD), F501 (HTS motor) — schedule B2CMU special gate review | Q-GREENTECH | PDR |
| OI-088-020-003 | Annual RTSC literature scan protocol for B2C-F502 — assign Q-HORIZON watch officer | Q-HORIZON | Q1 2027 |
| OI-088-020-004 | Catalogue template version control — establish formal document change control for B2C catalogue entries | Q-DATAGOV | PDR |
| OI-088-020-005 | Boundary definition with ATLAS-082 for B2C-F404 (EAD) and B2C-F401/F402 (MHD) | Q-GREENTECH / Q-HORIZON | PDR |
