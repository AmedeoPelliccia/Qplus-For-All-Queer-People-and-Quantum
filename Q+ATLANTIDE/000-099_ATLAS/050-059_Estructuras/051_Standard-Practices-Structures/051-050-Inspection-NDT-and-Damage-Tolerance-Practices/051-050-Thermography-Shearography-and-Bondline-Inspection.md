---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-050-THERMOGRAPHY-SHEAROGRAPHY-AND-BONDLINE-INSPECTION"
title: "ATLAS 050-059 · 05.051.050 — Thermography, Shearography and Bondline Inspection"
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

# ATLAS 050-059 · 05.051.050 — Thermography, Shearography and Bondline Inspection

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Defines the application of flash thermography, active thermography, and shearography for the detection of disbonds, delaminations, and impact damage in composite and bonded structures. These methods provide full-field imaging capability suited to rapid large-area inspection of composite primary and secondary structure.

---

## 2. Scope

### 2.1 Context

Thermographic methods detect thermal anomalies caused by subsurface voids, disbonds, and delaminations. Flash thermography uses a high-energy xenon flash lamp to deposit surface heat and monitors the thermal decay pattern using a cooled IR camera. Areas with subsurface voids conduct heat more slowly, appearing as warm regions in the phase or amplitude image. Lock-in and pulsed thermography are used where greater depth penetration or sensitivity is required.

Shearography uses coherent laser illumination and electronic speckle pattern interferometry to measure surface strain distribution under applied mechanical or thermal loading. Subsurface defects cause anomalous strain concentrations that appear as fringe pattern discontinuities in the shearogram. Shearography requires controlled loading and a vibration-isolated measurement environment.

### 2.2 Scope Diagram

```mermaid
graph TD
    A[Composite or Bonded Structure] --> B[Select Method]
    B --> C[Flash Thermography — large area, accessible surface]
    B --> D[Pulsed or Lock-in Thermography — depth penetration]
    B --> E[Shearography — strain anomaly detection under load]
    C --> F[Calibrate IR Camera — Black Body Reference]
    D --> F
    E --> G[Apply Controlled Mechanical or Thermal Load]
    F --> H[Acquire Image Data]
    G --> H
    H --> I[Process Phase or Amplitude Map]
    I --> J[Identify Indications vs Acceptance Standard]
    J --> K[Record and Report]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Flash Energy | ≥ 4 kJ for 3 mm CFRP panel (per equipment spec) |
| IR Camera Frame Rate | ≥ 200 Hz for flash thermography |
| Thermal Contrast Resolution | ≥ 0.05°C for 3 mm depth disbond |
| Shearography Shear Amount | Typically 4–8 mm for composite panel inspection |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-050-THERMOGRAPHY-SHEAROGRAPHY-AND-BONDLINE-INSPECTION` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-050-Inspection-NDT-and-Damage-Tolerance-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| ASTM E1875 | Standard Guide for Thermographic Inspection |
| ASTM E2581 | Standard Practice for Shearography of Composites |
| NAS 410 Level 2 | NDT Personnel Qualification — Thermography |
| AMM 51-10-00 | Thermographic Inspection Procedures |
