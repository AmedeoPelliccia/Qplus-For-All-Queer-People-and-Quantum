---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-083-050-AUXILIARY-ELECTRIC-PROPULSOR-CONCEPTS"
register: ATLAS-1000
title: "Auxiliary Electric Propulsor Concepts"
ata: "ATLAS-083 (Solar-Electric Auxiliary)"
sns: "083-050-00"
subsection: "083"
subsubject_code: "050"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HORIZON, Q-STRUCTURES, Q-HPC]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0083-050"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-083-050-AUXILIARY-ELECTRIC-PROPULSOR-CONCEPTS
     ATLAS-083 (Solar-Electric Auxiliary) · Auxiliary Electric Propulsor Concepts
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Auxiliary Electric Propulsor Concepts

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-083 Solar-Electric](https://img.shields.io/badge/ATLAS--083-Solar--Electric%20Auxiliary-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-teal)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Auxiliary Electric Propulsor Concepts`.

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
## §3 Concept A — Aft-Fuselage Boundary-Layer Ingestion (BLI) Fan

### 3.1 Description

Two PMSM direct-drive ducted fans embedded in the aft fuselage, ingesting the momentum-deficient boundary layer from the fuselage upper surface and re-energising the wake. The BLI configuration reduces jet kinetic energy losses, delivering a theoretically superior propulsive efficiency compared to free-stream podded fans of equivalent net thrust.

### 3.2 Performance Parameters

| Parameter | Value |
|---|---|
| Number of units | 2 (growth provision for 4) |
| Motor type | Interior PMSM (iPMSM), direct drive |
| Motor rated power | 40 kW per unit |
| Fan diameter | 350 mm |
| Fan tip speed | 250 m/s at max RPM (15 000 RPM) |
| Fan pressure ratio | 1.08 |
| Corrected airflow | 12 kg/s per fan (at FL350 cruise) |
| Net thrust per fan | 520 N at cruise (M 0.78, FL350) |
| Propulsive efficiency (BLI correction) | η_prop = 0.87 (8 % improvement vs. free-stream equivalent) |
| Specific power (motor + fan) | 2.0 kW/kg |

### 3.3 Structural Interface

- **Intake duct:** Titanium alloy (Ti-6Al-4V) lip; CFRP duct body; elliptical cross-section 400 mm × 350 mm; bird strike designed per CS-25.631 (1.8 kg bird at Vd − 15 kn)
- **Motor mount:** 4-point mount to aft fuselage Frame 72 bulkhead; vibration isolation (elastomeric pads, −30 dB at > 200 Hz)
- **Nacelle integration:** Flush with aft fuselage contour; access panel each side (C-check motor removal)

### 3.4 Noise Characteristics

- Tone noise: fan 1BPF at 15 000 RPM = 2 500 Hz (15 blades × 166.7 Hz shaft rate); well above 8 dB EPNdB ICAO Chapter 14 limit margin at cruise
- Broadband noise: < 60 dB(A) at 1 m (estimated); dominated by fuselage turbulent boundary layer ingestion

### 3.5 TRL and Risks

| Item | Value |
|---|---|
| Current TRL | 5 (ground rig demo, 20 kW scale model) |
| Target TRL Phase 2 | 7 (full-scale flight test) |
| Key Risk 1 | BLI distortion tolerance — iPMSM rotor structural fatigue under non-uniform inlet |
| Key Risk 2 | Bird strike ingestion capability — CFRP duct integrity with 1.8 kg bird |
| Key Risk 3 | Noise: ground operations and community noise at aft fuselage position |

---

## §4 Concept B — Distributed Leading-Edge Fan Array (DLEFA)

### 4.1 Description

Eight small ducted fans (100 mm diameter, 5 kW each, PMSM) distributed along the wing leading edge between rib 2 and rib 16 on each wing. The fans generate a suction effect that energises the leading-edge boundary layer, delaying flow separation and augmenting lift coefficient (CL) at high angle of attack. At cruise, the fans operate at low speed (30 % throttle) for turbulent transition delay.

### 4.2 Performance Parameters

| Parameter | Value |
|---|---|
| Number of fans per wing | 8 (16 total) |
| Fan power per unit | 5 kW at max throttle |
| Total power (all 16 at full) | 80 kW |
| Cruise power (30 % throttle) | 24 kW total |
| Fan diameter | 100 mm |
| Speed at max throttle | 30 000 RPM |
| CL augmentation (α = 8°) | ΔCL ≈ +0.25 (CFD estimate) |
| Drag reduction (cruise, BLC mode) | ~1.5 % (boundary layer control) |

### 4.3 Structural Interface

- Fans mounted within leading-edge D-nose rib bays; access via removable leading-edge panels
- Motor and fan assembly removable at each bay (bolt flange, 4 fasteners)
- Wiring routed in existing leading-edge conduit tray; individual SSPC per fan pair

### 4.4 TRL and Risks

| Item | Value |
|---|---|
| Current TRL | 3 (sub-scale wind tunnel model) |
| Target TRL Phase 2 | 5 (full-scale sub-section rig) |
| Key Risk 1 | Leading-edge ice accretion interface — DLEFA ingests ice in icing conditions |
| Key Risk 2 | Foreign object damage (FOD) at 100 mm fan diameter in low-altitude operations |
| Key Risk 3 | Maintenance complexity — 16 independent fan LRUs |

---

## §5 Concept C — Winglet-Mounted Pusher Pod (WMPP)

### 5.1 Description

Two pusher propeller pods mounted at the wingtip/winglet junction. Each pod contains a PMSM with folding 3-blade propeller (blade fold on ground to reduce hangar footprint and aerodynamic drag in non-operational mode). The pods provide supplementary thrust at climb and augment cruise efficiency by recovering winglet vortex energy.

### 5.2 Performance Parameters

| Parameter | Value |
|---|---|
| Number of pods | 2 (one per wingtip) |
| Motor rated power | 30 kW per pod |
| Propeller diameter | 1 200 mm (3-blade folding, CFRP) |
| Blade fold mechanism | Electric actuator (10 s fold/unfold); fold position drag CD increment < 0.0002 |
| Cruise net thrust per pod | 320 N at M 0.78, FL350 |
| Propulsive efficiency | η_prop = 0.82 (free-stream, pusher configuration) |
| Vortex energy recovery | ~1.5 % drag reduction (winglet-propeller interaction model) |

### 5.3 Structural Interface

- Wingtip pod attached to winglet root rib via titanium lug fitting (4 lugs); fail-safe: any 3 lugs carry full load
- Bird strike compliance per CS-25.631 for propeller
- Lightning strike: CFRP propeller blades have embedded copper mesh for bonding

### 5.4 TRL and Risks

| Item | Value |
|---|---|
| Current TRL | 4 (pod concept design; motor ground test) |
| Target TRL Phase 2 | 6 (ground rig and wind tunnel) |
| Key Risk 1 | Propeller blade containment in blade-off event — structural wing analysis required |
| Key Risk 2 | Aeroelastic interaction between wingtip pod and wing flutter mode |
| Key Risk 3 | Blade fold mechanism reliability — ice accretion on folded blades |

---

## §6 Concept Trade Summary

| Criterion | Concept A (BLI Fan) | Concept B (DLEFA) | Concept C (WMPP) |
|---|---|---|---|
| Propulsive efficiency improvement | 8 % (BLI benefit) | 1.5 % (drag reduction) | 2.5 % (combined) |
| Total system power | 80 kW (2×40 kW) | 80 kW (16×5 kW) | 60 kW (2×30 kW) |
| TRL (current) | 5 | 3 | 4 |
| Installation weight (est.) | 80 kg | 60 kg | 55 kg |
| Structural risk | Medium (BLI duct bird strike) | Low | High (blade-off, flutter) |
| Maintenance complexity | Low (2 LRUs) | High (16 LRUs) | Medium (2 pod LRUs + blade fold) |
| **Selection recommendation** | **Primary (Phase 1)** | Phase 2 option | Phase 2 option |

**Selected for Phase 1:** Concept A (BLI Fan, 2× 40 kW) as primary propulsor. Concepts B and C reserved for Phase 2 research evaluation.

---

## §7 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-083-050-001 | BLI inlet distortion coefficient (DC60) characterisation — CFD + wind tunnel | Q-HORIZON | PDR |
| OI-083-050-002 | iPMSM rotor fatigue analysis under BLI non-uniform inlet (HCF) | Q-STRUCTURES | CDR |
| OI-083-050-003 | Noise certification strategy for BLI fans at aft fuselage position (ICAO Annex 16) | Q-GREENTECH | Phase 2 |
| OI-083-050-004 | DLEFA leading-edge ice ingestion and icing certification path (CS-25 Appendix C / O) | Q-HORIZON | Phase 2 |
