---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-050-NDT-METHOD-SELECTION-AND-APPLICABILITY"
title: "ATLAS 050-059 · 05.051.050 — NDT Method Selection and Applicability"
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

# ATLAS 050-059 · 05.051.050 — NDT Method Selection and Applicability

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Provides selection criteria and applicability guidance for NDT methods used in structural inspection including ultrasonic, eddy current, radiography, thermography, and shearography. Method selection must be justified by the inspection requirement and supported by qualification data demonstrating the required probability of detection.

---

## 2. Scope

### 2.1 Context

NDT method selection depends on the material type, geometry, expected flaw type, accessibility, and required probability of detection (POD). No single NDT method is universally applicable to all structural inspection scenarios; the selection must be justified by the inspection task, material properties, and available qualification data. Method combinations may be required for complex geometries or multi-mode damage scenarios.

POD demonstration is required to validate that the selected method and technique can reliably detect the target flaw size at the defined inspection interval threshold. POD data must be developed in accordance with MIL-HDBK-1823A or equivalent methodology. Where POD data does not exist for a specific configuration, conservative assumptions or additional inspection passes must be applied.

### 2.2 Scope Diagram

```mermaid
graph TD
    A[Inspection Requirement Defined] --> B{Material Type?}
    B -->|Metallic| C[UT / Eddy Current / Radiography]
    B -->|Composite| D[UT / Tap Test / Thermography / Shearography]
    C --> E[Define Expected Flaw Type: Crack/Corrosion/Disbond]
    D --> E
    E --> F[Assess Accessibility and Component Geometry]
    F --> G[Select Method with Documented POD]
    G --> H[Qualify Technique and Personnel]
    H --> I[Execute Inspection and Record Results]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| UT Applicability | Thickness 1–100 mm metallic and composite |
| EC Applicability | Surface and near-surface cracks in conductive metals |
| Thermography Applicability | Bondline and composite disbond ≤ 25 mm depth |
| POD Target | 90% POD at 95% confidence (MIL-HDBK-1823A) |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-050-NDT-METHOD-SELECTION-AND-APPLICABILITY` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-050-Inspection-NDT-and-Damage-Tolerance-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| NAS 410 / EN 4179 | NDT Personnel Qualification and Certification |
| MIL-HDBK-1823A | Nondestructive Evaluation System Reliability Assessment |
| ASTM E2533 | Standard Guide for NDE of Polymer Matrix Composites |
| AMM 51-10-00 | NDT Method Selection and Guidance |
