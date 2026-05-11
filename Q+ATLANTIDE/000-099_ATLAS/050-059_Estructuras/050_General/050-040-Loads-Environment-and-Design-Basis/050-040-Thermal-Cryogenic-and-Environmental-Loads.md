---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-040-THERMAL-CRYOGENIC-AND-ENVIRONMENTAL-LOADS"
title: "ATLAS 050-059 · 05.050.040 — Thermal, Cryogenic and Environmental Loads"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../../README.md
parent_section_doc: ../../README.md
parent_subsection_doc: ../README.md
parent_subsubject_doc: ./README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "050-059"
section: "05"
section_title: "Estructuras"
subsection: "050"
subsection_title: "General"
subsubject: "040"
subsubject_title: "Thermal, Cryogenic and Environmental Loads"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.050.040 — Thermal, Cryogenic and Environmental Loads

## 1. Purpose

Defines the **thermal, cryogenic, and environmental loads** that the AMPEL360 eWTW structure must accommodate: temperature gradients from the LH₂ propulsion system, kinetic heating at high Mach conditions, atmospheric icing, acoustic loads, lightning, and HIRF; and their structural implications for material properties, allowables, and fatigue life.

## 2. Scope

### 2.1 Context

The AMPEL360 eWTW presents a uniquely wide thermal operating range. LH₂ fuel storage at −253 °C (20 K) generates cryogenic gradients in tank-attachment fittings, internal bulkheads, and adjacent frames — requiring cryogenically rated CFRP and metallic material specifications. At the opposite extreme, APU bay skin reaches +85 °C during extended ground operations, and leading-edge de-icing systems cycle between −55 °C (cruise) and +120 °C. These gradients impose thermally induced strains that are combined with mechanical loads in the sizing analyses.

Environmental loads also encompass: acoustic fatigue from distributed-propulsion noise (≥ 165 dB OASPL near nacelle fairings); lightning direct-effects zoning per CS-25.581; and HIRF susceptibility per CS-25.1317.

### 2.2 Thermal Load Source Map

```mermaid
graph TD
    A[Thermal and Environmental Loads] --> B[Cryogenic Zone]
    A --> C[Hot Zone]
    A --> D[Cyclic Zone]
    A --> E[Other Environmental]
    B --> B1[LH2 Tank -253 deg C]
    B --> B2[Cryo Attach Fittings]
    C --> C1[APU Bay plus 85 deg C]
    C --> C2[Engine Pylon plus 150 deg C nacelle]
    D --> D1[Wing Leading Edge De-ice Cycle]
    D --> D2[Pressurisation Cycle]
    E --> E1[Acoustic Fatigue DEP Nacelles]
    E --> E2[Lightning Direct Effects Zone 1A]
    E --> E3[HIRF Shielding]
```

### 2.3 Thermal Environment Zones

| Zone ID | Location | T_min (°C) | T_max (°C) | Governing Load |
|---|---|---|---|---|
| TZ-01 | LH₂ tank and attach | −253 | +20 | Cryogenic ΔT gradient |
| TZ-02 | APU bay skin | −55 | +85 | Hot soak + pressurisation |
| TZ-03 | Wing L/E (de-ice) | −55 | +120 | Thermal cycle fatigue |
| TZ-04 | Nacelle fairing | −55 | +150 | Acoustic + thermal |
| TZ-05 | Fuselage skin (general) | −55 | +70 | Kinetic heating + ΔP |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-040-THERMAL-CRYOGENIC-AND-ENVIRONMENTAL-LOADS` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/050_General/050-040-Loads-Environment-and-Design-Basis/` |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| CS-25.581 | Lightning protection |
| CS-25.1317 | HIRF protection |
| AC 20-107B | Composite aircraft structure — environmental effects |
| SC-AMPEL360-LH2-001 | Special Condition — cryogenic structural effects |
| [`./README.md`](./README.md) | Subsubject 040 index |
| [`../README.md`](../README.md) | 050_General subsection index |
