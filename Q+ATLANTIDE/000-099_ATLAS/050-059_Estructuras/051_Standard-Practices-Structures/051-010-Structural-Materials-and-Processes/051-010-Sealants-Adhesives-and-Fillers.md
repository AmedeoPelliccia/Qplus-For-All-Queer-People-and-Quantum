---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-010-SEALANTS-ADHESIVES-AND-FILLERS"
title: "ATLAS 050-059 · 05.051.010 — Sealants, Adhesives, and Fillers"
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

# ATLAS 050-059 · 05.051.010 — Sealants, Adhesives, and Fillers

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Specifies the approved sealants, structural adhesives, and filler materials for use in structural applications, including application methods, cure times, and compatibility with adjacent materials.

---

## 2. Scope

### 2.1 Context

Sealants serve multiple structural and systems functions in aircraft: fuel tank sealing (integral tanks), pressure cabin sealing, corrosion protection at faying surfaces, and aerodynamic smoothing. Each application class requires a specific sealant chemistry.

Structural adhesives are used for both primary and secondary bonding applications and must be selected from the Approved Materials List (AML). Mixing, application, and cure must follow the approved process specification without deviation.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[Sealant / Adhesive Requirement] --> B[Check AML]
        B --> C{Application Class?}
        C -- Fuel Tank --> D[Class B Polysulfide]
        C -- Pressure Cabin --> E[Class A Polysulfide / Polythioether]
        C -- Faying Surface --> F[Corrosion-Inhibiting Sealant]
        C -- Structural Bond --> G[Film / Paste Adhesive]
        D & E & F & G --> H[Apply per Process Spec]
        H --> I[Cure & Inspect]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Fuel Tank Sealant | PR-1776B / PRC-1422 (or equiv.) |
| Pressure Seal | PR-1440 series |
| Structural Adhesive | EA9696 / FM-300 film |
| AML Authority | Q-STRUCTURES Materials Eng |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-010-SEALANTS-ADHESIVES-AND-FILLERS` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-010-Structural-Materials-and-Processes/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| MIL-S-81733 | Sealing and Coating Compound — Corrosion Inhibiting |
| AMS 3277 | Polysulfide Sealant — Fuel Resistant |
| AMM 51-35-00 | Sealant Application |
| Airbus SRM 51-23 | Sealant Reference Manual |
