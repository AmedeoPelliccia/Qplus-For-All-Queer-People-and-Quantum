---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-040-LIMIT-AND-ULTIMATE-LOAD-DEFINITIONS"
title: "ATLAS 050-059 · 05.050.040 — Limit and Ultimate Load Definitions"
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
subsubject_title: "Limit and Ultimate Load Definitions"
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

# ATLAS 050-059 · 05.050.040 — Limit and Ultimate Load Definitions

## 1. Purpose

Defines **limit loads** and **ultimate loads** for the [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT] structural programme, establishes the safety factors and design criteria mandated by CS-25 Subpart C, and specifies the acceptance criteria for structural demonstrations at each load level.

## 2. Scope

### 2.1 Context

CS-25.301 defines *limit loads* as the maximum loads expected in service; the structure must support limit loads without detrimental permanent deformation. CS-25.303 mandates a safety factor of 1.5 applied to limit loads to obtain *ultimate loads*, which the structure must sustain without failure for at least three seconds. For the [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT], additional programme-specific safety factors are applied where novel materials (CFRP laminates, metal-matrix composites) or novel load types (cryogenic cycling, hydrogen embrittlement) create elevated uncertainty in analytical models.

Proof loads (1.0 × limit) apply to pressurised vessels and tank attachment fittings; these are verified by pressurisation proof tests during ground testing.

### 2.2 Load Level Derivation Chain

```mermaid
flowchart TD
    A[Aerodynamic / FE Model] --> B[Limit Load LL]
    B -->|× 1.5 CS-25.303| C[Ultimate Load UL]
    B -->|× 1.0| D[Proof Load PL]
    C -->|Structural analysis| E[Internal Forces N V M T]
    E -->|Compare with allowable| F{Margin of Safety ≥ 0?}
    F -->|Yes| G[Compliant]
    F -->|No| H[Redesign Required]
```

### 2.3 Safety Factor Summary

| Load Level | Factor vs. Limit | Acceptance Criterion |
|---|---|---|
| Proof load | 1.00 | No leakage; elastic behaviour |
| Limit load | 1.00 | No detrimental permanent deformation |
| Ultimate load | 1.50 | No failure for ≥ 3 s |
| CFRP scatter factor | ×1.15 add. (B-basis) | Per AC 20-107B |
| Cryogenic penalty | ×1.10 add. (programme SC) | LH₂ thermal cycling uncertainty |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-040-LIMIT-AND-ULTIMATE-LOAD-DEFINITIONS` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/050_General/050-040-Loads-Environment-and-Design-Basis/` |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| CS-25.301 | Loads — general |
| CS-25.303 | Factor of safety |
| CS-25.305 | Strength and deformation |
| AC 20-107B | Composite Aircraft Structure |
| [`./README.md`](./README.md) | Subsubject 040 index |
| [`../README.md`](../README.md) | 050_General subsection index |
