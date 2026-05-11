---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-020-FASTENER-TYPES-AND-CLASSIFICATION"
title: "ATLAS 050-059 · 05.051.020 — Fastener Types and Classification"
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

# ATLAS 050-059 · 05.051.020 — Fastener Types and Classification

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Classifies all fastener types used in Q+ATLANTIDE aircraft structures according to loading direction, material, head type, thread form, and installation method, providing a taxonomy for selection and documentation.

---

## 2. Scope

### 2.1 Context

Fasteners are classified into shear fasteners (designed primarily for shear load transfer), tension fasteners (designed for axial load), and combination fasteners (capable of carrying both shear and tension). Each class has specific installation and inspection requirements.

The classification system aligns with NAS, MS, and AN standards, and with proprietary fastener systems (e.g., Hi-Lok®, Lockbolt®, Huck®) that are approved for specific applications in the Q+ATLANTIDE airframe.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[Fastener Classification] --> B[By Load Direction]
        A --> C[By Material]
        A --> D[By Installation]
        B --> E[Shear]
        B --> F[Tension]
        B --> G[Combination]
        C --> H[Aluminium / Titanium / Steel / CRES]
        D --> I[Clearance Fit]
        D --> J[Interference Fit]
        D --> K[Blind Install]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Standard Systems | NAS, MS, AN, BAC, SPS |
| Proprietary Fasteners | Hi-Lok, Lockbolt, Huck, Cherry |
| Material Classes | Al 2024, Ti-6Al-4V, CRES A286 |
| Coating | Cadmium, IVD Aluminium, Dry Film |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-020-FASTENER-TYPES-AND-CLASSIFICATION` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-020-Fasteners-Hardware-and-Joining-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| NAS1097 | 100° Flush Head Shear Screws |
| MS27039 | Countersunk Machine Screws |
| Hi-Lok Installation | HL Product Data Sheet |
| EASA CS-25.607 | Fastener Provisions |
