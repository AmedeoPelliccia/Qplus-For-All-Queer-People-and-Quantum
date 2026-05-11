---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-020-BONDED-JOINTS-AND-ADHESIVE-FASTENING"
title: "ATLAS 050-059 · 05.051.020 — Bonded Joints and Adhesive Fastening"
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

# ATLAS 050-059 · 05.051.020 — Bonded Joints and Adhesive Fastening

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Defines the design principles, installation procedures, and inspection requirements for structural bonded joints and adhesively fastened assemblies in Q+ATLANTIDE aircraft structures.

---

## 2. Scope

### 2.1 Context

Structural adhesive bonding distributes load over a large area, eliminating stress concentrations at discrete fastener locations and providing significant weight reduction compared to mechanically fastened joints of equivalent strength.

Bonded joints require stringent surface preparation, environmental control during bonding, and 100% ultrasonic inspection of the bond area post-cure to verify full adhesive contact and absence of disbonds or voids.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[Bonded Joint Requirement] --> B[Surface Preparation]
        B --> C[Adhesive Application]
        C --> D[Assembly & Pressure Application]
        D --> E[Cure Cycle]
        E --> F[Post-Cure Inspection]
        F --> G{UT — Accept?}
        G -- Pass --> H[Record & Release]
        G -- Fail --> I[Repair / Reject Disposition]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Adhesive System | Film or paste per AML |
| Surface Prep | PAA or grit blast + primer |
| Cure Method | Autoclave or oven + vacuum bag |
| Inspection | 100% UT scan — ASTM E1901 |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-020-BONDED-JOINTS-AND-ADHESIVE-FASTENING` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-020-Fasteners-Hardware-and-Joining-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| ASTM E1901 | UT of Adhesively Bonded Joints |
| AMM 51-77-12 | Bonded Repair Procedures |
| AMS 3267 | Film Adhesive Specification |
| EASA AMC 20-29 | Composite Bonded Structure |
