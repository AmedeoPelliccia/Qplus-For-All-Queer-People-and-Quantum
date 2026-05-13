---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-085-070-THERMAL-EMC-AND-STRUCTURAL-INTEGRATION-CONSTRAINTS"
register: ATLAS-1000
title: "Thermal EMC and Structural Integration Constraints"
ata: "ATLAS-085 (Distributed Electric Propulsion Architecture)"
sns: "085-070-00"
subsection: "085"
subsubject_code: "070"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-GREENTECH, Q-INDUSTRY, Q-HORIZON]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0085-070"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-085-070-THERMAL-EMC-AND-STRUCTURAL-INTEGRATION-CONSTRAINTS
     ATLAS-085 (Distributed Electric Propulsion Architecture) · Thermal EMC and Structural Integration Constraints
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Thermal EMC and Structural Integration Constraints

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

ATLAS subsubject 085-070 defines the thermal management requirements and DEP Thermal Management Loop (DEP-TML) architecture for the four propulsor stations, establishes electromagnetic compatibility (EMC) constraints for the MDU switching transients and HVDC cable routing, and specifies the structural integration constraints including vibration isolation, nacelle mount stiffness, and PMSM/MDU fastener and torque requirements.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA Reference | ATLAS-085 — 085-070 Thermal EMC and Structural Integration Constraints |
| Certification Basis | DO-160G Sections 8 (vibration), 19 (induced signal susceptibility), 21 (RF emissions); CS-25.571; CS-25.1353 |
| S1000D SNS | 085-070-00 |

---

## §3 DEP Thermal Management Loop (DEP-TML)

The DEP-TML is a dedicated ethylene-glycol/water (EGW) coolant loop that thermally manages MDU-1 through MDU-4 and their co-located PMSM housings. The loop is integrated with the ATLAS-074 Thermal Management Hybrid system via a dedicated heat exchanger (DEP-RAHX — Rams Air Heat Exchanger).

### §3.1 DEP-TML Architecture

```mermaid
flowchart LR
    PUMP_A[DEP-TML Pump A\n12 L/min (primary)] -->|EGW supply| MANIFOLD[DEP Supply Manifold\n50 °C max]
    PUMP_B[DEP-TML Pump B\n12 L/min (standby)] -->|EGW supply| MANIFOLD
    MANIFOLD -->|Branch P1| MDU1_CP[MDU-1 Cold Plate\nPMSM-1 Housing]
    MANIFOLD -->|Branch P2| MDU2_CP[MDU-2 Cold Plate\nPMSM-2 Housing]
    MANIFOLD -->|Branch P3| MDU3_CP[MDU-3 Cold Plate\nPMSM-3 Housing]
    MANIFOLD -->|Branch P4| MDU4_CP[MDU-4 Cold Plate\nPMSM-4 Housing]
    MDU1_CP -->|EGW return| RETURN[DEP Return Manifold]
    MDU2_CP -->|EGW return| RETURN
    MDU3_CP -->|EGW return| RETURN
    MDU4_CP -->|EGW return| RETURN
    RETURN -->|Hot EGW| DEPRAHX[DEP-RAHX\nRam Air HX]
    DEPRAHX -->|Cooled EGW| PUMP_A
```

### §3.2 DEP-TML Parameters

| Parameter | Value | Notes |
|---|---|---|
| Coolant fluid | 50/50 EGW (ethylene glycol / water) | AS 50 specification |
| DEP-TML pump flow rate | 12 L/min (per pump) | One active; one standby |
| Supply temperature (max) | 50 °C | Monitored by DEPCU; thermal derate above 50 °C |
| Return temperature (max, TOGA) | 72 °C | Includes MDU and PMSM heat at full power |
| MDU cold plate heat rejection | 10 kW max per MDU (at 98 % efficiency, 500 kW) | Total 40 kW |
| PMSM housing heat rejection | 8 kW max per PMSM (at 96 % efficiency, 500 kW) | Total 32 kW |
| Total DEP-TML heat rejection | 72 kW | At full TOGA power |
| DEP-RAHX ram air inlet area | 0.18 m² | Flush flush NACA scoop; aft fuselage |
| DEP-RAHX effectiveness | ≥ 0.75 | At cruise, 30 g/s ram air |

---

## §4 EMC Constraints

### §4.1 MDU Switching Emissions (DO-160G Section 21)

Each MDU generates high-frequency emissions due to IGBT switching at 10 kHz. The following constraints apply:

| Requirement | Limit | Test Method | Mitigation |
|---|---|---|---|
| Radiated emissions (RE102) | Class M (military/research) | DO-160G §21.4 | Integral CM choke + EMC shield in MDU housing |
| Conducted emissions (CE102) | Class M | DO-160G §21.3 | X/Y filter capacitors; shielded HVDC cable |
| Susceptibility (RS103) | Class M | DO-160G §21.5 | MDU IGBT gate driver optocoupled; DEPCU DAL B shielded housing |
| HVDC cable radiated | Class L (lower limit, long cable run P3/P4) | DO-160G §21.4 | Braided shielded HVDC cable, 85 % coverage; bonded to airframe every 500 mm |

### §4.2 HVDC Cable EMC Routing Constraints

| Cable Run | EMC Routing Requirement | Separation from Avionics |
|---|---|---|
| DPDP → P1/P2 (wing) | Route through dedicated conduit; no co-routing with AFDX / CAN cables | ≥ 300 mm from avionics bus ducts |
| DPDP → P3/P4 (fuselage keel) | Dedicated keel conduit; bonded ground straps every 500 mm | ≥ 400 mm from flight control harnesses |
| CAN bus (MDU ↔ DEPCU) | Twisted shielded pair; shield grounded at DEPCU end only | ≥ 150 mm from HVDC power cables |

### §4.3 Common-Mode Choke Specification (MDU-integrated)

| Parameter | Requirement |
|---|---|
| Inductance (common-mode) | ≥ 500 µH at 10 kHz |
| Attenuation at 10 kHz | ≥ 40 dB |
| Current rating | 700 A continuous |
| Temperature rating | −55 °C to +125 °C |

---

## §5 Vibration Isolation and Structural Mount Constraints

### §5.1 PMSM and MDU Vibration Environment

The PMSM rotational unbalance and fan aerodynamic forcing generate vibration loads on the nacelle structure. The MDU, being co-located, must tolerate:

| Vibration Source | Frequency Range | Peak Amplitude | DO-160G Category |
|---|---|---|---|
| Fan rotational (6 000 RPM = 100 Hz) | 100 Hz fundamental + harmonics to 1 000 Hz | 2.0 g (sinusoidal) | Category S (sinusoidal sweep) |
| Fan BPF (18 blades × 100 Hz = 1 800 Hz) | 1 800 Hz | 1.5 g | Category R (random) |
| Airframe buffet (approach) | 5–50 Hz | 0.8 g | Category R |
| Combined random (in-flight cruise) | 5–2 000 Hz | 0.5 g RMS | DO-160G §8 Curve C |

### §5.2 Vibration Isolation Mounts

PMSM-1 through PMSM-4 are each mounted on a set of four elastomeric vibration isolation mounts to attenuate structural transmission to the airframe:

| Mount Specification | P1 / P2 (over-wing) | P3 / P4 (aft-fuselage) |
|---|---|---|
| Mount type | Elastomeric shear mount (4 per PMSM) | Elastomeric shear mount (4 per PMSM) |
| Stiffness (lateral) | 1 200 kN/m | 1 500 kN/m |
| Stiffness (axial / thrust) | 6 000 kN/m | 8 000 kN/m |
| Damping ratio | 0.08–0.12 | 0.08–0.12 |
| Natural frequency (isolated system) | ~25 Hz (lateral) | ~28 Hz (lateral) |
| Temperature range | −55 °C to +120 °C | −55 °C to +120 °C |
| Replacement interval | 12 000 FC or 6 years | 12 000 FC or 6 years |

### §5.3 MDU Fastener Torque Requirements

| Fastener Location | Size | Torque | Locking |
|---|---|---|---|
| MDU cold plate to PMSM housing | M10 × 1.5 stainless | 45 N·m | Nordlock washer |
| MDU to nacelle frame | M12 × 1.75 stainless | 65 N·m | Thread-locking compound (Loctite 243) |
| PMSM to isolation mount | M16 × 2.0 stainless | 120 N·m | Castellated nut + split pin |
| BTB to DPDP panel | M8 × 1.25 | 22 N·m | Nordlock washer |

---

## §6 DEP-TML Maintenance Procedures Summary

| Task | Interval | Description |
|---|---|---|
| DEP-TML coolant EGW sample | A-check | Inhibitor concentration check; pH 7.5–9.0; top-up if required |
| DEP-TML pump A/B flow check | A-check | Flow rate ≥ 10 L/min confirmed via GSE flow meter |
| DEP-RAHX ram air inlet inspect | A-check | Visual; no FOD blockage; no fin corrosion |
| DEP-TML full flush and refill | 4 000 h / 4 years | Replace EGW with fresh AS 50 mix; bleed air purge |
| DEP-TML pump A/B replacement | 8 000 h | LRU replacement; flow test post-installation |
| MDU cold plate O-ring inspect | C-check | Coolant fitting O-ring condition; no seepage |

---

## §7 Interfaces

| Interface | Connected System | Protocol | Data |
|---|---|---|---|
| DEP-TML coolant | TMS — ATLAS-074 | Physical EGW lines | Heat rejection; pump control |
| MDU temp telemetry | DEPCU | CAN ISO 11898 | Cold plate inlet/outlet temp; derate trigger |
| PMSM winding temp | MDU (via embedded sensor) | CAN (via MDU) | Winding temp; derating action |
| EMC bonding | Airframe ground | Physical bonding straps | HVDC cable shield; nacelle bonding |
| Vibration monitoring | SHM (structural health) | Strain gauge / accelerometer CAN | PMSM vibration; bearing health |

---

## §8 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-085-070-001 | DEP-TML pump P3/P4 line length (28 m) — pressure drop at 12 L/min | Q-STRUCTURES | PDR |
| OI-085-070-002 | MDU DO-160G Category S sinusoidal sweep at 2.0 g — qualification test article | Q-INDUSTRY | CDR |
| OI-085-070-003 | HVDC cable braided shield coverage (85 %) — RE102 compliance verification | Q-INDUSTRY | CDR |
| OI-085-070-004 | PMSM isolation mount natural frequency — avoid resonance with fan BPF 1 800 Hz | Q-STRUCTURES | CDR |
| OI-085-070-005 | DEP-RAHX ram air inlet drag increment — CFD and wind tunnel verification | Q-HORIZON | Phase 2 |
