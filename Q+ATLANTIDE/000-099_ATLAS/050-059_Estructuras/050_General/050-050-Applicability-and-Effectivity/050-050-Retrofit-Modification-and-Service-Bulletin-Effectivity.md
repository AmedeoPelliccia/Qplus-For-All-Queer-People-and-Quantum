---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-050-RETROFIT-MODIFICATION-AND-SERVICE-BULLETIN-EFFECTIVITY"
title: "ATLAS 050-059 · 05.050.050 — Retrofit, Modification and Service Bulletin Effectivity"
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
subsubject_title: "Retrofit, Modification and Service Bulletin Effectivity"
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

# ATLAS 050-059 · 05.050.050 — Retrofit, Modification and Service Bulletin Effectivity

## 1. Purpose

Defines the **retrofit, modification, and service-bulletin (SB) effectivity** framework for [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT] structural documentation, specifying how post-delivery structural changes are tracked, how SB incorporation state affects applicable maintenance limits and inspection thresholds, and how CSDB applicability annotations are updated post-SB.

## 2. Scope

### 2.1 Context

Once an [PROGRAMME-AIRCRAFT] aircraft enters service, its structural configuration evolves through the incorporation of service bulletins, airworthiness directives (ADs), and operator-requested modifications. Each incorporated SB changes the structural definition of the affected aircraft, which in turn changes the applicability of structural maintenance tasks, repair schemes, and inspection limits. The [PROGRAMME-AIRCRAFT] CSDB maintains a parallel document state for pre- and post-SB configurations, allowing publication outputs to reflect the actual aircraft configuration.

Mandatory SBs triggered by AD actions are tracked in the AD Compliance Register (ADCR), which is cross-referenced against the PDCM to determine current aircraft structural state. Optional SBs are tracked per aircraft in the operator's own configuration management system, with the CSDB providing the filtering logic.

### 2.2 SB Effectivity Processing

```mermaid
flowchart TD
    A[Service Bulletin SB Issued] --> B[PDCM: SB incorporation event logged per SN]
    B --> C[CSDB applicability updated: POST-SB-n]
    C --> D{AD or Optional?}
    D -->|Mandatory AD| E[ADCR updated; compliance deadline tracked]
    D -->|Optional SB| F[Operator records SB incorporation]
    E --> G[Maintenance manual output pre-SB and post-SB]
    F --> G
    G --> H[Aircraft-specific maintenance schedule]
```

### 2.3 SB Effectivity Encoding Rules

| SB Status | Effectivity Token | Documentation Action |
|---|---|---|
| Pre-SB (original config) | `PRE-SB-{number}` | Retain original task/limit in CSDB |
| Post-SB (SB incorporated) | `POST-SB-{number}` | Add new task/limit with post-SB applicability |
| Mandatory AD compliance | `POST-AD-{ref}` | Replace original data module with revised |
| Operator modification (STC) | `STC-{number}` | Separate applicability in CSDB |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-050-RETROFIT-MODIFICATION-AND-SERVICE-BULLETIN-EFFECTIVITY` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/050_General/050-050-Applicability-and-Effectivity/` |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| S1000D Issue 5.0 | Applicability annotations for SB incorporation |
| CS-25 Subpart D | Airworthiness Directives process |
| ADCR-[PROGRAMME-AIRCRAFT]-001 | AD Compliance Register |
| [`./README.md`](./README.md) | Subsubject 050 index |
| [`../README.md`](../README.md) | 050_General subsection index |
