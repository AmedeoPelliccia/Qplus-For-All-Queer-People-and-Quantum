---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-040-COMPOSITE-DAMAGE-ASSESSMENT-AND-CLASSIFICATION"
title: "ATLAS 050-059 · 05.051.040 — Composite Damage Assessment and Classification"
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
subsubject: "040"
subsubject_title: "Composite Repair and Bonding Practices"
parent_subsubject_doc: ./README.md
---

# ATLAS 050-059 · 05.051.040 — Composite Damage Assessment and Classification

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Establishes the methodology for assessing and classifying damage in composite structure including delamination, impact damage, fibre fracture, and core damage. Accurate classification determines the repair scheme and approval level required to restore structural airworthiness.

---

## 2. Scope

### 2.1 Context

Composite damage cannot always be detected visually. Low-energy impacts can cause barely visible impact damage (BVID) with significant internal delamination extending well beyond the visible indentation. NDT is required to define the true damage boundary before any repair scheme is selected. Damage is classified as allowable, repairable, or requiring replacement based on SRM criteria.

BVID thresholds are defined in the SRM for each structural zone and are based on the residual strength and damage tolerance analysis conducted during aircraft certification. Damage exceeding the BVID threshold in area or depth is classified as visible impact damage (VID) and requires a formal repair disposition with engineering approval.

### 2.2 Scope Diagram

```mermaid
graph TD
    A[Impact or Damage Event] --> B[Visual Inspection — BVID/VID Check]
    B --> C[NDT Assessment — UT Pulse-Echo or Tap Test]
    C --> D[Define Damage Zone Boundary +12mm beyond visible]
    D --> E[Compare to SRM ADL]
    E --> F{Classification}
    F -->|Within ADL| G[Allowable — Accept with monitoring]
    F -->|Exceeds ADL repairable| H[Repairable — Select Repair Scheme]
    F -->|Exceeds repair limits| I[Replace Component]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| BVID Dent Depth Threshold | Per SRM (typically ≤ 6 mm) |
| NDT Boundary Extension | +12 mm beyond visible damage boundary |
| Damage Types | Delamination, matrix crack, fibre fracture, core crush |
| Classification Categories | Category 1 (Allowable) / 2 (Repairable) / 3 (Replace) |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-040-COMPOSITE-DAMAGE-ASSESSMENT-AND-CLASSIFICATION` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-040-Composite-Repair-and-Bonding-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| SRM 51-00 | Composite Allowable Damage Limit Tables |
| EASA CS-25.571 | Composite Structure Damage Tolerance Requirements |
| ASTM D7136 | Measuring Damage Resistance of Polymer Matrix Composites |
| FAA AC 20-107B | Composite Aircraft Structure Certification |
