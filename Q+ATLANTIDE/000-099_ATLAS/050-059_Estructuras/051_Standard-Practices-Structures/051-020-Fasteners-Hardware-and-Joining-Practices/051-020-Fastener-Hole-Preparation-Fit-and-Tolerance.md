---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-020-FASTENER-HOLE-PREPARATION-FIT-AND-TOLERANCE"
title: "ATLAS 050-059 · 05.051.020 — Fastener Hole Preparation, Fit, and Tolerance"
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
subsection: "051"
subsection_title: "Standard Practices — Structures"
subsubject: "020"
subsubject_title: "Fasteners, Hardware and Joining Practices"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.051.020 — Fastener Hole Preparation, Fit, and Tolerance

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Specifies drilling procedures, hole preparation methods, fit classes, and dimensional tolerances for fastener holes in metallic and composite structural members on Q+ATLANTIDE aircraft.

---

## 2. Scope

### 2.1 Context

Fastener hole quality is a primary determinant of joint fatigue life. Hole surface finish, roundness, cylindricity, and edge break quality must meet specification to prevent fretting, stress concentrations, and crack initiation.

Composite materials require specific drilling parameters (feed rate, speed, backing material) to prevent delamination, fibre pull-out, and matrix cracking at the hole boundary, which would degrade bearing strength and fatigue life.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[Fastener Hole Required] --> B{Base Material?}
        B -- Metallic --> C[Carbide Drill — Dry]
        B -- Composite --> D[Diamond / PCD Drill — Backed]
        B -- Stack Drill --> E[Optimised Stack Parameters]
        C & D & E --> F[Inspect Hole Diameter]
        F --> G[Inspect Surface Finish & Edge Break]
        G --> H{Tolerance Met?}
        H -- Yes --> I[Proceed to Fastener Install]
        H -- No --> J[Next Oversize / Disposition]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Clearance Fit | H8/h7 — per NAS spec |
| Interference Fit | 0.0005–0.002 in interference |
| Surface Finish | Ra ≤ 63 µin for fatigue critical |
| Edge Break | 0.005–0.020 in chamfer both sides |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-020-FASTENER-HOLE-PREPARATION-FIT-AND-TOLERANCE` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-020-Fasteners-Hardware-and-Joining-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| AMM 51-43-00 | Rivet/Fastener Installation |
| NAS Standards | Hole Size Tables — NAS1836 |
| ASTM E2261 | Hole Quality Inspection |
| EASA CS-25.607 | Fastener Hole Requirements |
