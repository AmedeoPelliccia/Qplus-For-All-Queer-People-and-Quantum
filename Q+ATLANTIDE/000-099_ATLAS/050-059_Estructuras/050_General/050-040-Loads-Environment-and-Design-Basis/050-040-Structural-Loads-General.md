---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-040-STRUCTURAL-LOADS-GENERAL"
title: "ATLAS 050-059 · 05.050.040 — Structural Loads General"
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
subsubject_title: "Structural Loads General"
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

# ATLAS 050-059 · 05.050.040 — Structural Loads General

## 1. Purpose

Defines the **general structural loads framework** for the [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT]: the classification taxonomy of all load types, the principles for load combination, the load sources mapped to structural components, and the governing regulatory references that control each load category.

## 2. Scope

### 2.1 Context

Structural loads on the [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT] arise from aerodynamic, inertial, propulsive, pressurisation, thermal, and ground-handling sources. All loads are classified as either *external* (directly specified by CS-25 or the design basis) or *internal* (derived by structural analysis from external inputs). Load combinations follow CS-25.301 and the programme-specific load combination matrix LCM-[PROGRAMME-AIRCRAFT]-001.

Loads are further classified by probability of occurrence: *limit loads* (probable in service), *ultimate loads* (limit × 1.5 safety factor), and *proof loads* (for pressurised components). Each classification dictates the allowable structural response and margin-of-safety criteria.

### 2.2 Load Classification Tree

```mermaid
graph LR
    A[Structural Loads] --> B[External Loads]
    A --> C[Internal Reactions]
    B --> B1[Aerodynamic]
    B --> B2[Inertial / Mass]
    B --> B3[Propulsive Thrust]
    B --> B4[Ground Contact]
    B --> B5[Pressure Differential]
    B --> B6[Thermal / Cryogenic]
    C --> C1[Axial Force N]
    C --> C2[Shear Force V]
    C --> C3[Bending Moment M]
    C --> C4[Torsion T]
```

### 2.3 Load Source–Component Mapping

| Load Source | Primary Structural Component | Governing CS-25 Article |
|---|---|---|
| Aerodynamic lift | Wing spar, centre-wing box | 25.301, 25.333 |
| Fuselage inertia | Fuselage frames, longerons | 25.301 |
| Thrust / torque | Engine mount, pylon, rear spar | 25.361 |
| Landing impact | Main-gear fitting, keel beam | 25.473 |
| Pressurisation | Fuselage skin, frames, bulkheads | 25.365 |
| Cryogenic gradient | LH₂ tank attachment structure | Special Condition |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-040-STRUCTURAL-LOADS-GENERAL` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/050_General/050-040-Loads-Environment-and-Design-Basis/` |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| CS-25.301 | Loads — general |
| CS-25.303 | Factor of safety |
| CS-25.305 | Strength and deformation |
| LCM-[PROGRAMME-AIRCRAFT]-001 | Load Combination Matrix (programme document) |
| [`./README.md`](./README.md) | Subsubject 040 index |
| [`../README.md`](../README.md) | 050_General subsection index |
