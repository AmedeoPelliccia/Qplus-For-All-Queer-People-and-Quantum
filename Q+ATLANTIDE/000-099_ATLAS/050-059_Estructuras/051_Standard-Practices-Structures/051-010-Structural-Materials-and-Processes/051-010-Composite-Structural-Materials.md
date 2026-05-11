---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-010-COMPOSITE-STRUCTURAL-MATERIALS"
title: "ATLAS 050-059 · 05.051.010 — Composite Structural Materials"
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
subsubject: "010"
subsubject_title: "Structural Materials and Processes"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.051.010 — Composite Structural Materials

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Specifies the approved composite structural materials for Q+ATLANTIDE aircraft structures, including CFRP, GFRP, and AFRP systems, along with their prepreg/wet layup specifications and cure cycle requirements.

---

## 2. Scope

### 2.1 Context

Carbon-fibre reinforced polymer (CFRP) is the primary composite material used for primary structure including wing skins, empennage panels, and fuselage barrel sections. Approved prepreg systems are listed in the Composite Materials Register (CMR).

Composite materials require controlled storage, shelf-life management, and certified cure cycles. Any deviation from approved cure cycle parameters must be documented and assessed for structural impact before acceptance.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[Composite Materials] --> B[Carbon Fibre — CFRP]
        A --> C[Glass Fibre — GFRP]
        A --> D[Aramid — AFRP]
        B --> E[Prepreg Systems]
        B --> F[Wet Layup Systems]
        E --> G[Autoclave Cure]
        F --> H[Out-of-Autoclave / OOA]
        G & H --> I[CMR Approval Required]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Primary CFRP | HexPly M21/T800 (or approved equiv.) |
| GFRP Application | Radome, fairings, secondary |
| Cure Temp Range | 120–180 °C per prepreg spec |
| CMR Reference | ATLAS-CMR-051-010 |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-010-COMPOSITE-STRUCTURAL-MATERIALS` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-010-Structural-Materials-and-Processes/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| ASTM D3039 | Tensile Properties — Composites |
| ASTM D7264 | Flexural Properties — Composites |
| MIL-HDBK-17-1F | Polymer Matrix Composites — Guidelines |
| AMM 51-77-00 | Repair of Composite Structure |
