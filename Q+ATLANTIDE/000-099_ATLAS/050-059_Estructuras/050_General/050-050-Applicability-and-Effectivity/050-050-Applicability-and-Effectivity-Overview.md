---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-050-APPLICABILITY-AND-EFFECTIVITY-OVERVIEW"
title: "ATLAS 050-059 · 05.050.050 — Applicability and Effectivity Overview"
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
subsubject: "050"
subsubject_title: "Applicability and Effectivity Overview"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.050.050 — Applicability and Effectivity Overview

## 1. Purpose

Provides the programme-level overview of the **applicability and effectivity** framework for AMPEL360 eWTW structural documentation: the rules by which documents, tasks, limits, and repair schemes are scoped to specific aircraft, configuration variants, serial-number blocks, and modification states.

## 2. Scope

### 2.1 Context

Applicability and effectivity are the mechanisms that prevent applying an incorrect maintenance task, repair scheme, or structural limit to an aircraft it was not designed for. The AMPEL360 eWTW programme anticipates multiple structural variants (baseline, extended-range, freighter derivative) and a long production run during which modifications, retrofits, and service bulletins will progressively change the configuration of individual aircraft.

All structural documents — including inspection thresholds, repair allowances, and replacement limits — carry an explicit applicability statement encoded in both human-readable form and in S1000D applicability annotations (using the CSDB applicability filtering mechanism). The AMPEL360 Product Definition and Configuration Management system (PDCM) provides the master effectivity register from which applicability is derived.

### 2.2 Applicability Framework

```mermaid
graph TD
    A[PDCM Master Effectivity Register] --> B[Aircraft Model Effectivity]
    A --> C[Serial Number Block Effectivity]
    A --> D[Modification and SB Effectivity]
    B --> E[Structural Variant Rules]
    C --> F[Production Configuration Baseline]
    D --> G[Post-Delivery Retrofit Status]
    E --> H[Document Applicability Filter]
    F --> H
    G --> H
    H --> I[S1000D CSDB Applicability Annotation]
    I --> J[Maintenance Manual Publication Output]
```

### 2.3 Applicability Types Summary

| Type | Scope | Owner | Update Trigger |
|---|---|---|---|
| Programme applicability | All AMPEL360 aircraft | Programme office | New derivative launch |
| Model applicability | Specific variant (e.g., ER) | Structures design | Design change order |
| Serial-number effectivity | Production block | Production planning | SB incorporation |
| SB/modification effectivity | Post-delivery aircraft | Service engineering | SB release |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-050-APPLICABILITY-AND-EFFECTIVITY-OVERVIEW` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/050_General/050-050-Applicability-and-Effectivity/` |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| S1000D Issue 5.0 | Applicability filtering chapter |
| ATA iSpec 2200 | Configuration and effectivity management |
| [`./README.md`](./README.md) | Subsubject 050 index |
| [`../README.md`](../README.md) | 050_General subsection index |
