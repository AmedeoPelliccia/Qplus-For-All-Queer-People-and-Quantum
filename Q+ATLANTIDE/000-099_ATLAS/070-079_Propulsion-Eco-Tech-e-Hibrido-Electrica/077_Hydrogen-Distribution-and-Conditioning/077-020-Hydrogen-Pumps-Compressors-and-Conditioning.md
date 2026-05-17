---
document_id: "QATL-ATLAS-1000-ATLAS-070-079-07-077-020-HYDROGEN-PUMPS-COMPRESSORS-AND-CONDITIONING"
register: ATLAS-1000
title: "Hydrogen Pumps, Compressors and Conditioning"
ata: "ATA 28 (GH₂/LH₂ Distribution)"
sns: "077-020-00"
subsection: "077"
subsubject_code: "020"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-GREENTECH, Q-HPC, Q-AIR, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0077-020"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-070-079-07-077-020-HYDROGEN-PUMPS-COMPRESSORS-AND-CONDITIONING
     ATA 28 (GH₂/LH₂ Distribution) · Hydrogen Pumps, Compressors and Conditioning
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Hydrogen Pumps, Compressors and Conditioning

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATA 28 GH₂/LH₂ Distribution](https://img.shields.io/badge/ATA-28%20GH%E2%82%82%2FLH%E2%82%82-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-MECHANICS](https://img.shields.io/badge/Q--Division-Q--MECHANICS-orange)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden. Every linked document must exist in the Q+ATLANTIDE repository
> before the link is activated. Broken links are treated as open issues and must be resolved
> before the document is promoted from `DRAFT` to `APPROVED`.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Hydrogen Pumps, Compressors and Conditioning`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 Applicability

| Applicability Level | Rule |
|---|---|
| Standard taxonomy | Applies to the ATLAS node `077` |
| Programme implementation | Conditional; determined by programme architecture, trade studies, certification basis, and applicability model |
| Product configuration | Defined in the programme-specific configuration baseline |
| Effectivity | Defined in the programme CSDB / applicability layer |
| Non-applicability | Must be explicitly stated in the programme impact-study branch when excluded |
## §3 Functional Description ![DRAFT]

The programme-defined aircraft type uses two **cryogenic centrifugal LH₂ pumps** (Pump-A, port; Pump-B, starboard), one per storage tank feed path. Each pump is a hermetically-sealed, brushless-DC-motor-driven centrifugal unit operating fully submerged in LH₂ (or at near-cryogenic inlet conditions), eliminating shaft-seal hydrogen leak paths. The motor winding is cryogenically compatible (polyimide insulation rated to 4 K) and cooled by the LH₂ flow through the pump.

**Operating principle:** Pump speed is commanded by the HDCMU via a variable-frequency drive (VFD) control signal. Speed modulation adjusts LH₂ volumetric flow rate and discharge pressure, allowing the HDCMU to precisely match hydrogen supply to FCCU demand. Nominal cruise operating speed: 8 000–12 000 RPM; maximum: 15 000 RPM. Discharge pressure boost: 0–3.5 bar above tank inlet pressure (max discharge 6.5 bar(a) at minimum tank pressure).

**Cavitation protection:** The pump inlet is fitted with a cryogenic **Net Positive Suction Head (NPSH)** margin monitor — a differential pressure transducer comparing static head at tank outlet to pump inlet. If NPSH margin falls below 0.3 bar, the HDCMU reduces pump speed to prevent cavitation, which would cause instantaneous LH₂ vaporisation in the pump and flow interruption.

**Cross-feed capability:** A normally-closed **cross-connect shutoff valve** (XCSOV) on the pump discharge manifold allows Pump-B to back-feed the port (Pump-A) vaporizer if Pump-A fails, and vice versa. The HDCMU activates cross-feed automatically upon confirmed pump fault.

**GH₂ conditioning note:** No separate GH₂ recirculation compressor is required in the programme-defined aircraft type architecture; recirculation of anode tail-gas in the PEMFC stacks is managed within the FCCU domain (ATLAS 075). The conditioning function in subsubject 077-020 refers to pump-driven flow conditioning and LH₂ stability management upstream of the vaporizers.

---

## §4 Functional Breakdown

| ID | Name | Description | Lead Division |
|---|---|---|---|
| F-001 | Pump-A cryogenic centrifugal unit | Port-side LH₂ pump; brushless DC; hermetic; ATEX IIC; rated 3.5 bar boost max | Q-MECHANICS |
| F-002 | Pump-B cryogenic centrifugal unit | Stbd-side LH₂ pump; identical to Pump-A; redundant | Q-MECHANICS |
| F-003 | Variable-frequency drives (VFD A/B) | HDCMU-commanded PWM drives; closed-loop speed control; 270 V DC input | Q-HPC |
| F-004 | NPSH margin monitors | Differential pressure sensors at pump inlets; cavitation prevention logic | Q-HPC |
| F-005 | Cross-connect shutoff valve (XCSOV) | NC solenoid valve; pump-discharge cross-connect; HDCMU auto-commanded on pump fault | Q-MECHANICS |
| F-006 | Pump inlet filters | 50 µm cryogenic sintered SS filter elements; protect pump impeller from particulate | Q-MECHANICS |
| F-007 | Pump health monitoring | Speed sensor (Hall effect); motor winding temperature (Pt-1000 cryo); vibration accelerometer | Q-HPC |

---

## §5 Pump Architecture — Mermaid Diagram

```mermaid
flowchart TB
    TANK_A[Tank-A LH₂ Feed] --> FILT_A[Pump-A Inlet Filter 50 µm]
    FILT_A --> NPSH_A[NPSH Monitor A]
    NPSH_A --> PUMP_A[Cryo Centrifugal Pump A 8–15 k RPM]
    PUMP_A -->|Discharge A| XCSOV[Cross-Connect SOV XCSOV NC]
    PUMP_A -->|Primary Port| VAP_A_IN[Vaporizer-A Inlet]
    TANK_B[Tank-B LH₂ Feed] --> FILT_B[Pump-B Inlet Filter 50 µm]
    FILT_B --> NPSH_B[NPSH Monitor B]
    NPSH_B --> PUMP_B[Cryo Centrifugal Pump B 8–15 k RPM]
    PUMP_B -->|Primary Stbd| VAP_B_IN[Vaporizer-B Inlet]
    PUMP_B -->|Discharge B| XCSOV
    XCSOV -->|Cross-feed Port→Stbd or Stbd→Port| VAP_A_IN
    XCSOV --> VAP_B_IN
    HDCMU[HDCMU Channel A/B] -->|VFD Command| PUMP_A
    HDCMU -->|VFD Command| PUMP_B
    HDCMU -->|XCSOV Command| XCSOV
    HDCMU <-- NPSH_A
    HDCMU <-- NPSH_B
```

---

## §6 Components and LRUs

| Component | Part Number | Qty | Location | Maintenance Interval | Notes |
|---|---|---|---|---|---|
| Cryo LH₂ Pump A | CPMP-A-PN-TBD | 1 | Aft pylon, port | 2 500 FH overhaul / on condition | Hermetic brushless-DC; ATEX IIC T4 |
| Cryo LH₂ Pump B | CPMP-B-PN-TBD | 1 | Aft pylon, stbd | 2 500 FH overhaul / on condition | Identical to Pump-A |
| VFD Controller A | VFD-A-PN-TBD | 1 | EE bay | Software update per SB; C-check BITE | 270 V DC input; 0–15 000 RPM command |
| VFD Controller B | VFD-B-PN-TBD | 1 | EE bay | Software update per SB; C-check BITE | Identical to VFD-A |
| Cross-Connect SOV (XCSOV) | XCSOV-PN-TBD | 1 | Pump discharge manifold | A-check operational test | NC solenoid; ATEX IIC; cryo-compatible |
| Pump Inlet Filter A | PIF-A-PN-TBD | 1 | Upstream Pump-A | C-check element replacement | 50 µm sintered SS316L; ΔP alarm at 0.5 bar |
| Pump Inlet Filter B | PIF-B-PN-TBD | 1 | Upstream Pump-B | C-check element replacement | Identical to PIF-A |
| NPSH Differential Pressure Sensor A | NPSH-A-PN-TBD | 1 | Pump-A inlet | Annual calibration | Cryo-rated; 0–5 bar range |
| NPSH Differential Pressure Sensor B | NPSH-B-PN-TBD | 1 | Pump-B inlet | Annual calibration | Identical to NPSH-A |

---

## §7 Performance Specification

| Parameter | Minimum | Nominal | Maximum | Notes |
|---|---|---|---|---|
| Pump operating speed | 4 000 RPM (idle) | 10 000 RPM (cruise) | 15 000 RPM | HDCMU speed-limited |
| LH₂ volumetric flow per pump | 0.5 L/min | 2.5 L/min | 5.0 L/min | At max PEMFC demand |
| Discharge pressure boost | 0 bar | 2.0 bar | 3.5 bar | Above tank inlet pressure |
| Max discharge pressure | — | — | 6.5 bar(a) | At min tank pressure 1.5 bar |
| Pump inlet temperature | 18 K | 20–25 K | 30 K | LH₂ saturation conditions |
| NPSH margin minimum | 0.3 bar | 0.5 bar | — | Below min: pump speed reduced |
| Motor winding temperature | — | 20 K | 100 K | Cryo cooling via LH₂ flow |
| Cavitation-free NPSH (NPSHr) | — | 0.4 bar | — | Design requirement |

---

## §8 Interfaces

| Interface | Connected System | Medium | Function |
|---|---|---|---|
| LH₂ inlet (×2) | ATLAS 077-010 — Cryogenic feed lines | LH₂ cryogenic | LH₂ supply to pump inlet |
| Discharge (×2) | ATLAS 077-010 — Pump discharge lines | Pressurised LH₂ | Pump output to vaporizer |
| VFD power (×2) | ATA 24 HVDC 270 V bus | HVDC cable | Pump motor excitation |
| VFD control (×2) | HDCMU (077-080) | PWM / AFDX | Speed command from HDCMU |
| NPSH sensor signals | HDCMU (077-080) | AFDX / analogue | Cavitation margin monitoring |
| Speed/temperature/vibration signals | HDCMU (077-080) | Analogue / AFDX | Pump health monitoring |
| XCSOV actuation | HDCMU (077-080) | 28 V DC solenoid | Cross-feed activation |

---

## §9 Maintenance Tasks

| Task | Interval | Procedure Reference |
|---|---|---|
| Pump A/B operational check (speed, flow, ΔP) | A-check (600 FH) | AMM 28-77-020-201 |
| Pump inlet filter ΔP check | A-check | AMM 28-77-020-202 |
| NPSH sensor calibration check | Annual | AMM 28-77-020-203 |
| Pump inlet filter element replacement | C-check (6 000 FH) | AMM 28-77-020-204 |
| VFD BITE / software configuration check | C-check | AMM 28-77-020-205 |
| Pump removal and installation | 2 500 FH / on condition | AMM 28-77-020-301 |

---

## §10 Revision History

| Rev | Date | Author | Description |
|---|---|---|---|
| 0.1 | 2026-05-12 | Q-MECHANICS | Initial DRAFT baseline release |
