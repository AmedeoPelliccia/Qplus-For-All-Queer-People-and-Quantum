---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-050-DAMAGE-TOLERANCE-AND-CRACK-GROWTH-PRINCIPLES"
title: "ATLAS 050-059 · 05.051.050 — Damage Tolerance and Crack Growth Principles"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../../README.md
parent_section_doc: ../../README.md
parent_subsection_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "050-059"
section: "05"
section_title: "Estructuras"
subsection: "051"
subsection_title: "Standard Practices — Structures"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
subsubject: "050"
subsubject_title: "Inspection, NDT and Damage-Tolerance Practices"
parent_subsubject_doc: ./README.md
---

# ATLAS 050-059 · 05.051.050 — Damage Tolerance and Crack Growth Principles

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Provides the engineering principles of damage tolerance design and crack growth methodology as applied to the structural inspection programme for Q+ATLANTIDE aircraft. These principles underpin the derivation of inspection thresholds and intervals published in the MPD.

---

## 2. Scope

### 2.1 Context

Damage tolerance methodology requires that structure containing the maximum undetected initial flaw will sustain design limit loads for the inspection interval without growing to critical crack size. Crack growth analysis uses linear elastic fracture mechanics (LEFM) with applied stress spectra from the fatigue load sequence. The inspection interval is set at half the crack growth period from detectable to critical size to account for inspection reliability.

The equivalent initial flaw size (EIFS) represents the maximum flaw size that may exist undetected after manufacture and inspection. It accounts for the POD of manufacturing inspection and is used as the starting point for crack growth analysis. For transport category aircraft, EIFS values are typically set conservatively to bound manufacturing variability.

### 2.2 Scope Diagram

```mermaid
graph TD
    A[Initial Flaw Assumption — EIFS/ADF] --> B[Apply Load Spectrum — Fatigue Mission Profile]
    B --> C[Crack Growth Integration — da/dN per Paris Law or NASGRO]
    C --> D[Compute Critical Crack Size — Kc fracture toughness]
    D --> E[Calculate Inspection Interval]
    E --> F[Apply 2× Safety Factor per CS-25.571]
    F --> G[Define Inspection Threshold — Initial Inspection Point]
    G --> H[Implement Threshold and Interval in MPD]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Equivalent Initial Flaw Size (EIFS) | Typically 1.27 mm half-crack for metallic structure |
| Residual Strength Requirement | ≥ Design Limit Load at critical crack size |
| Crack Growth Model | NASGRO (NASA/ESACRACK) or FASTRAN |
| Safety Factor on Interval | 2× per CS-25.571 damage tolerance requirements |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-050-DAMAGE-TOLERANCE-AND-CRACK-GROWTH-PRINCIPLES` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-050-Inspection-NDT-and-Damage-Tolerance-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| EASA CS-25.571 | Damage Tolerance and Fatigue Evaluation |
| NASGRO Fracture Mechanics Database | Crack Growth and Fracture Data for Aerospace Alloys |
| MIL-HDBK-1823A | Nondestructive Evaluation System Reliability |
| FAA AC 25.571-1D | Damage Tolerance and Fatigue Evaluation of Structure |
