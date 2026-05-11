---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-060-CORROSION-PREVENTION-AND-CONTROL-PRACTICES"
title: "ATLAS 050-059 · 05.051.060 — Corrosion Prevention and Control Practices"
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
subsubject: "060"
subsubject_title: "Corrosion Protection, Sealing and Surface Treatment"
parent_subsubject_doc: ./README.md
---

# ATLAS 050-059 · 05.051.060 — Corrosion Prevention and Control Practices

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Defines the corrosion prevention and control practices applied during maintenance and repair of Q+ATLANTIDE aircraft structures, including treatment methods for each corrosion category. These practices implement the CPCP and ensure structural surfaces are restored to their designed corrosion protection standard.

---

## 2. Scope

### 2.1 Context

Corrosion prevention relies on a layered system: material selection with inherent corrosion resistance, surface treatment (anodising or plating), barrier coatings (primer and topcoat), sealants at structural interfaces, and drainage design to prevent moisture accumulation. Active corrosion must be removed to bare metal and the affected area assessed for structural impact before re-treatment is applied.

Category 1 corrosion (surface only, ≤ 4% material loss) requires removal and re-treatment without structural repair. Category 2 corrosion requires removal, depth measurement against SRM allowable damage limits, and re-treatment; if within limits no structural repair is required. Category 3 corrosion exceeds the ADL and requires engineering disposition before re-treatment.

### 2.2 Scope Diagram

```mermaid
graph TD
    A[Corrosion Detected] --> B[Assess Category: Cat 1/2/3]
    B --> C[Cat 1: Remove by Blending/Abrasion — No SRM Action]
    B --> D[Cat 2: Remove, Measure Depth vs SRM ADL, Re-treat]
    B --> E[Cat 3: Engineering Disposition Required Before Any Action]
    C --> F[Apply Alodine + Primer + Topcoat + Sealant]
    D --> F
    E --> G[Engineering Approval] --> F
    F --> H[Inspect Treated Area]
    H --> I[Document CPCP Record]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Category 1 Threshold | Surface only, ≤ 4% material thickness loss |
| Category 2 Threshold | Pit depth within SRM ADL, no secondary structural damage |
| Category 3 Definition | Exceeds ADL or involves structural damage requiring repair |
| Re-treatment Sequence | Removal → Alodine → Epoxy Primer → Sealant → Topcoat |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-060-CORROSION-PREVENTION-AND-CONTROL-PRACTICES` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-060-Corrosion-Protection-Sealing-and-Surface-Treatment/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| EASA AD 2002-0117 | CPCP Framework and Category Definitions |
| FAA AC 43-4B Chapter 5 | Corrosion Treatment Methods |
| AMM Chapter 51 | Corrosion Removal and Re-treatment Procedures |
| ATA MSG-3 CPCP Baseline | CPCP Task Development Guidelines |
