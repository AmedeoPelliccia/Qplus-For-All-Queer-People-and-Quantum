---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-000-STRUCTURAL-TOOLS-EQUIPMENT-AND-GSE-GENERAL"
title: "ATLAS 050-059 · 05.051.000 — Structural Tools, Equipment, and GSE — General"
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
subsubject: "000"
subsubject_title: "Standard Practices Structures General"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.051.000 — Structural Tools, Equipment, and GSE — General

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Identifies and describes the general tools, measuring equipment, and ground support equipment (GSE) required for structural maintenance tasks, including calibration and serviceability requirements.

---

## 2. Scope

### 2.1 Context

Correct tool selection is critical for structural work to prevent damage to structure, maintain torque accuracy, and ensure dimensional conformity. This document establishes the minimum tooling standard for ATLAS 051 structural tasks.

All torque tools, measuring instruments, and specialised structural tooling must be calibrated per an approved calibration schedule and bear a valid calibration sticker before use on aircraft structure.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[Structural Task Requirement] --> B[Select Tool Type]
        B --> C[Verify Calibration Status]
        C --> D{Calibration Valid?}
        D -- Yes --> E[Use Tool]
        D -- No --> F[Remove from Service]
        F --> G[Calibration Lab]
        E --> H[Record Tool Ref in Task Card]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Torque Wrenches | Calibrated ±4% — per ISO 6789 |
| Measuring Tools | CMM / micrometer / vernier |
| NDT Equipment | UT, ET, RT — per NDT Manual |
| GSE Cert | Annual inspection required |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-000-STRUCTURAL-TOOLS-EQUIPMENT-AND-GSE-GENERAL` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-000-Standard-Practices-Structures-General/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| AMM 20-13-00 | Torque Application |
| ISO 6789 | Torque Tool Calibration |
| EASA Part-145 Appendix II | Tool Control Requirements |
| AMM 51-00-00 | Structures General Tooling Notes |
