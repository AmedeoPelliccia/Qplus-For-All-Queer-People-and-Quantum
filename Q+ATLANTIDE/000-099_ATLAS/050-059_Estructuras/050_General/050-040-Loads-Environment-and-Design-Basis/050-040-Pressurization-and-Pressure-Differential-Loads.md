---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-040-PRESSURIZATION-AND-PRESSURE-DIFFERENTIAL-LOADS"
title: "ATLAS 050-059 · 05.050.040 — Pressurization and Pressure Differential Loads"
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
subsubject_title: "Pressurization and Pressure Differential Loads"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
standard_scope: agnostic
programme_specific: false
---

# ATLAS 050-059 · 05.050.040 — Pressurization and Pressure Differential Loads

## 1. Purpose

Defines the **pressurisation and pressure-differential loads** for the [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT] fuselage and tank attachment structures, including the maximum differential pressure, proof and burst pressure criteria, combined pressurisation-plus-bending load cases, and fatigue contributions from pressurisation cycling.

## 2. Scope

### 2.1 Context

The [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT] cabin is pressurised to maintain a 6,000 ft cabin altitude at the aircraft's maximum operating altitude of FL 410. This produces a maximum differential pressure (ΔP_max) of 65.0 kPa at operational conditions. The design relief valve setting provides an upper bound of 68.5 kPa. Combined with fuselage bending loads, the pressurisation cases drive skin thickness and frame pitch in the constant-section fuselage barrel.

The LH₂ fuel tanks operate at internal overpressure (ullage management) and must also withstand a negative differential (sloshing and cryogenic shrinkage) addressed by Special Condition SC-[PROGRAMME-AIRCRAFT]-LH2-001. Pressurisation cycling contributes the dominant fatigue mechanism for the fuselage skin and is tracked against the design service goal (DSG) of 90,000 flight cycles.

### 2.2 Pressurisation Load Cycle

```mermaid
sequenceDiagram
    participant G as Ground (ΔP = 0)
    participant C as Climb (ΔP rising)
    participant CR as Cruise (ΔP = 65 kPa)
    participant D as Descent (ΔP falling)
    G->>C: Pressurisation start
    C->>CR: Max differential reached
    CR->>D: Depressurisation start
    D->>G: Ground ΔP = 0 (one flight cycle)
    Note over G,CR: Each cycle contributes to fatigue crack growth in fuselage skin
```

### 2.3 Pressure Load Cases

| Case | ΔP (kPa) | Combined Load | Acceptance Criterion |
|---|---|---|---|
| Normal max diff | 65.0 | + fuselage bending | MS ≥ 0.0 (ultimate) |
| Relief valve setting | 68.5 | Cabin pressurisation alone | No failure |
| Proof test | 68.5 | Static, no bending | Elastic, no leakage |
| Burst (CS-25.365) | 68.5 × 2.0 = 137 | Pressurisation only | No catastrophic failure |
| LH₂ tank negative | −10.0 | Cryogenic shrinkage | MS ≥ 0.0 (limit) |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-040-PRESSURIZATION-AND-PRESSURE-DIFFERENTIAL-LOADS` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/050_General/050-040-Loads-Environment-and-Design-Basis/` |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| CS-25.365 | Pressurised compartment loads |
| CS-25.571 | Fatigue evaluation — pressurisation cycling |
| AMC 25.365 | Compliance methods for pressurised structure |
| SC-[PROGRAMME-AIRCRAFT]-LH2-001 | Special Condition — LH₂ tank pressurisation |
| [`./README.md`](./README.md) | Subsubject 040 index |
| [`../README.md`](../README.md) | 050_General subsection index |
