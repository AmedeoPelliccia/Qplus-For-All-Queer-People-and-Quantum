---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-050-VISUAL-AND-DETAILED-INSPECTION-PRACTICES"
title: "ATLAS 050-059 · 05.051.050 — Visual and Detailed Inspection Practices"
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

# ATLAS 050-059 · 05.051.050 — Visual and Detailed Inspection Practices

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Defines the standards and methods for visual general (VGI), visual detailed (VDI), and special detailed (SDI) inspections of aircraft structure. These inspection types form the foundation of the MSG-3 scheduled maintenance programme and must be applied with consistent technique to achieve the required probability of detection.

---

## 2. Scope

### 2.1 Context

Visual inspections form the primary detection method for obvious structural anomalies including cracks, corrosion, dents, and disbonds. VGI covers general condition from normal access distance and is typically performed at line maintenance visits. VDI requires direct access and lighting to a distance of ≤ 60 cm to detect fine cracks and early corrosion. SDI requires additional tooling such as borescopes, mirrors, or enhanced lighting to access confined or hidden structural areas.

Illumination quality is critical to inspection effectiveness. Inspectors must verify that lighting is adequate before beginning the inspection and must supplement natural or ambient light where required. Relevant training records and task cards must be accessible during execution, and the inspector must be familiar with the specific SRM ADL limits applicable to the zone being inspected.

### 2.2 Scope Diagram

```mermaid
graph TD
    A[Inspection Scheduled] --> B[Access Structure per AMM]
    B --> C{Select Inspection Type}
    C -->|VGI| D[Survey from Normal Access Distance — arm's length]
    C -->|VDI| E[Survey at ≤ 60 cm with ≥ 500 lux illumination]
    C -->|SDI| F[Use Tooling: Borescope/Mirror/Magnifier at ≤ 15 cm]
    D --> G[Record Findings]
    E --> G
    F --> G
    G --> H[Compare to ADL / SRM Limits]
    H --> I{Within Limits?}
    I -->|Yes| J[Accept and Sign Off]
    I -->|No| K[Initiate Repair Action]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| VGI Inspection Distance | Arm's length (approximately 60 cm or greater) |
| VDI Inspection Distance | ≤ 60 cm with adequate artificial illumination |
| SDI Inspection Distance | ≤ 15 cm; tooling required |
| Minimum Illumination (VDI) | ≥ 500 lux; ≥ 1000 lux for SDI |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-050-VISUAL-AND-DETAILED-INSPECTION-PRACTICES` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-050-Inspection-NDT-and-Damage-Tolerance-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| ATA iSpec 2200 | Inspection Category Definitions |
| EASA CS-25.1529 | Instructions for Continued Airworthiness |
| MSG-3 Rev 2 | Inspection Task Definition and Classification |
| AMM 51-10-00 | General Structural Inspection Procedures |
