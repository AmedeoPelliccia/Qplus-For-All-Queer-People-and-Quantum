---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-040-GROUND-LOADS-AND-LANDING-LOADS"
title: "ATLAS 050-059 · 05.050.040 — Ground Loads and Landing Loads"
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
subsubject_title: "Ground Loads and Landing Loads"
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

# ATLAS 050-059 · 05.050.040 — Ground Loads and Landing Loads

## 1. Purpose

Defines the **ground loads and landing loads** applicable to the [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT] structure, including landing-gear vertical and drag reactions, ground-handling towing and jacking loads, braking and pivoting loads, and the influence of the aircraft's high-energy-density cryogenic mass on gear-strut dynamic response.

## 2. Scope

### 2.1 Context

CS-25.471 governs ground loads. For the [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT], the adoption of an unconventional undercarriage arrangement (tricycle with centre-mounted main gear due to the low-wing distributed-propulsion layout) produces atypical spin-up/spring-back load distributions. The LH₂ tank mass located aft of centre also creates a critical nose-gear reaction during braked roll-out. All landing-gear load cases are computed for maximum landing weight (MLW) and maximum take-off weight (MTOW) where applicable.

Taxi loads account for runway roughness exceedances per CS-25.491. Towing, jacking, and tie-down loads are specified in the ground-handling load cases per CS-25.509 and programme requirements.

### 2.2 Ground Load Cases Flowchart

```mermaid
flowchart TD
    A[Landing Event] --> B{Gear Configuration}
    B -->|All-gear level landing| C[Level Landing CS-25.479]
    B -->|Tail-down landing| D[Tail-Down Landing CS-25.481]
    B -->|One-gear landing| E[One-Gear CS-25.483]
    C --> F[Spin-Up Load]
    C --> G[Spring-Back Load]
    F --> H[Structural Analysis Gear Fitting and Keel Beam]
    G --> H
    D --> H
    E --> H
    H --> I[Margin Check vs Allowables]
```

### 2.3 Key Ground Load Cases

| Case | CS-25 Ref | Load Factor (n_z) | Critical Structure |
|---|---|---|---|
| Level landing | 25.479 | ≤ 2.0 (per sink rate) | Main gear fitting, keel beam |
| Tail-down landing | 25.481 | Variable | Aft fuselage keel, bulkhead |
| One-gear landing | 25.483 | n_z + lateral | Fuselage frame, skin lap joints |
| Braking on runway | 25.493 | Braking coefficient 0.8 | Nose-gear drag strut |
| Pivoting on ground | 25.495 | Lateral | Main gear drag brace |
| Towing | 25.509 | 0.6 × MTOW (forward) | Tow bar attachment |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-040-GROUND-LOADS-AND-LANDING-LOADS` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/050_General/050-040-Loads-Environment-and-Design-Basis/` |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| CS-25.471 | Ground loads — general |
| CS-25.479 | Level-landing conditions |
| CS-25.481 | Tail-down landing conditions |
| CS-25.493 | Braked-roll conditions |
| CS-25.509 | Towing loads |
| [`./README.md`](./README.md) | Subsubject 040 index |
| [`../README.md`](../README.md) | 050_General subsection index |
