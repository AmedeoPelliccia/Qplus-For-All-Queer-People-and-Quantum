---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-020-HYBRID-MECHANICAL-AND-BONDED-JOINTS"
title: "ATLAS 050-059 · 05.051.020 — Hybrid Mechanical and Bonded Joints"
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

# ATLAS 050-059 · 05.051.020 — Hybrid Mechanical and Bonded Joints

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Addresses the design, installation, and inspection of hybrid joints that combine mechanical fastening and adhesive bonding to maximise load transfer efficiency, damage tolerance, and joint stiffness in critical structural applications.

---

## 2. Scope

### 2.1 Context

Hybrid joints are used where the fail-safe requirement mandates that disbond of the adhesive layer shall not result in loss of structural integrity, with mechanical fasteners providing the secondary load path.

Analysis of hybrid joints must account for the differential stiffness of the adhesive and fastener load paths, ensuring that load redistribution after partial disbond remains within design allowables throughout the aircraft service life.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[Hybrid Joint] --> B[Adhesive Layer — Primary Load Path]
        A --> C[Mechanical Fasteners — Secondary]
        B --> D[Bond Area Design]
        C --> E[Fastener Pattern Design]
        D & E --> F[Combined Analysis]
        F --> G[Disbond Scenario Check]
        G --> H[Fail-Safe Confirmation]
        H --> I[Approved Design]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Primary Path | Adhesive bond — stiffness-matched |
| Secondary Path | Fastener pattern — fail-safe |
| Analysis Tool | FEA + classical closed-form |
| Inspection | UT bond + torque check fasteners |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-020-HYBRID-MECHANICAL-AND-BONDED-JOINTS` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-020-Fasteners-Hardware-and-Joining-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| EASA CS-25.571 | Damage Tolerance and Fatigue |
| AMC 20-29 | Composite Bonded Structure |
| ASTM D5961 | Bearing Response of Composites |
| EASA CS-25.305 | Strength and Deformation |
