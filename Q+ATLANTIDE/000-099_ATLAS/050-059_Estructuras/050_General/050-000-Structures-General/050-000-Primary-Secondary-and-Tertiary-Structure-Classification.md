---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-000-PRIMARY-SECONDARY-AND-TERTIARY-STRUCTURE-CLASSIFICATION"
title: "ATLAS 050-059 · 05.050.000 — Primary, Secondary and Tertiary Structure Classification"
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
subsection: "050"
subsection_title: "General"
subsubject: "000"
subsubject_title: "Primary Secondary and Tertiary Structure Classification"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
standard_scope: agnostic
programme_specific: false
---

# ATLAS 050-059 · 05.050.000 — Primary, Secondary and Tertiary Structure Classification

## 1. Purpose

Defines the [PROGRAMME-AIRCRAFT] **structural classification scheme**: Primary (PSE), Secondary (SSE), and Tertiary Structure, including PSE-list, associated inspection categories, and MSG-3 classification matrix.

## 2. Scope

### 2.1 Classification Definitions

| Class | Acronym | Definition |
|---|---|---|
| Primary Structure | PSE | Structural elements whose failure would result in loss of the aircraft or would significantly reduce structural integrity; subject to CS-25.571 DT requirements |
| Secondary Structure | SSE | Structural elements that, upon failure, would not directly cause loss of the aircraft but may compromise safety, impede continued operations, or cause significant consequential damage |
| Tertiary Structure | TSE | Non-safety-critical structural elements (fairings, brackets, antenna mounts) whose failure has no direct effect on airworthiness |

### 2.2 PSE List (Top-Level, Baseline)

| PSE ID | Description | CS-25 basis | Inspection category |
|---|---|---|---|
| PSE-F01 | Fuselage pressure vessel skin (all stations) | §25.571 DT | A-check visual + 2C HFEC |
| PSE-W01 | Wing box upper and lower skins | §25.571 DT | A-check visual + LFEC/PAUT |
| PSE-W02 | Wing front and rear spar | §25.571 DT | C-check PAUT |
| PSE-J01 | WFIJ primary fittings | §25.571 DT + safe-life by analysis | 2C NDT |
| PSE-P01 | Pylon main fitting and attach bolts | §25.571 + §25.581 | C-check ACFM + OTF inspection |
| PSE-H01 | HTP attachment fittings | §25.571 | 2C HFEC/PAUT |
| PSE-D01 | Passenger door primary frames | §25.571 | 4C PAUT |

### 2.3 Classification Decision Flowchart

```mermaid
flowchart TD
    A[Structural Element] --> B{Failure causes loss of aircraft?}
    B -- Yes --> C[PSE — Primary Structural Element]
    B -- No --> D{Failure significantly impairs safety or operations?}
    D -- Yes --> E[SSE — Secondary Structural Element]
    D -- No --> F[TSE — Tertiary Structural Element]
    C --> G[Apply CS-25.571 DT]
    E --> H[Apply inspection programme]
    F --> I[On-condition maintenance]
```

### 2.4 Regulatory Mapping

| Classification | Inspection basis | SRM reference |
|---|---|---|
| PSE | Damage-Tolerant per CS-25.571(b) | SRM Chapter 51 |
| PSE (exceptions) | Safe-life per CS-25.571(c) — landing gear, fasteners | SRM Chapter 32 |
| SSE | MSG-3 task analysis | SRM Chapter 05 |
| TSE | On-condition, no programmed inspection | SRM Chapter 51 |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-000-PRIMARY-SECONDARY-AND-TERTIARY-STRUCTURE-CLASSIFICATION` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| CS-25.571 | Damage-tolerance and fatigue evaluation of structure |
| MSG-3 Rev 3 | Airline/Manufacturer Maintenance Program Development |
| [`./README.md`](./README.md) | Subsubject index |
