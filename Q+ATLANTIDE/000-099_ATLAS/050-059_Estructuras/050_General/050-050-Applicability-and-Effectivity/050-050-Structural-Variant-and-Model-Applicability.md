---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-050-STRUCTURAL-VARIANT-AND-MODEL-APPLICABILITY"
title: "ATLAS 050-059 · 05.050.050 — Structural Variant and Model Applicability"
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
subsubject_title: "Structural Variant and Model Applicability"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.050.050 — Structural Variant and Model Applicability

## 1. Purpose

Defines how structural documentation applicability is scoped to specific **AMPEL360 eWTW variants and model types**, cataloguing the structural differences between the baseline and derivative variants and the rules for selecting the applicable repair schemes, inspection limits, and structural data modules for each model.

## 2. Scope

### 2.1 Context

The AMPEL360 eWTW family is planned to include the baseline medium-haul variant, an extended-range (ER) variant with a strengthened centre-wing box and additional LH₂ tank capacity, and a potential freighter (F) derivative. Each variant introduces structural differences that affect applicable inspection thresholds, repair allowances, and structural limits. These differences are captured in the Structural Variant Difference Register (SVDR), which maps each structural zone and PSE to the variants for which it applies.

Model applicability in the CSDB is encoded using S1000D product attributes and product attribute values, allowing a single publication to deliver variant-specific content to the appropriate operator fleet without maintaining entirely separate document sets.

### 2.2 Variant Applicability Resolution

```mermaid
flowchart LR
    A[Structural Task or Data Module] --> B{Variant Applicability?}
    B -->|Common to all variants| C[Tag: ALL-AMPEL360]
    B -->|Baseline only| D[Tag: AMPEL360-BL]
    B -->|ER variant only| E[Tag: AMPEL360-ER]
    B -->|Freighter only| F[Tag: AMPEL360-F]
    C --> G[CSDB Product Attribute Filter]
    D --> G
    E --> G
    F --> G
    G --> H[Variant-Specific Publication Output]
```

### 2.3 Structural Variant Differences

| Structural Zone | Baseline | ER Variant | Freighter Variant |
|---|---|---|---|
| Centre-wing box lower panel thickness | 8.0 mm CFRP | 10.5 mm CFRP | 12.0 mm CFRP |
| LH₂ tank attach frame pitch | 635 mm | 500 mm (extra tank) | n/a (no pax tank) |
| Cabin floor beam section | Std 100 × 50 mm | Std 100 × 50 mm | Heavy 150 × 75 mm |
| Fuselage skin gauge (barrel) | 2.2 mm | 2.2 mm | 2.8 mm (cargo loads) |
| MTOW (structural sizing) | 78,000 kg | 85,000 kg | 90,000 kg |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-050-STRUCTURAL-VARIANT-AND-MODEL-APPLICABILITY` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/050_General/050-050-Applicability-and-Effectivity/` |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| S1000D Issue 5.0 | Product attribute applicability |
| SVDR-AMPEL360-001 | Structural Variant Difference Register |
| [`./README.md`](./README.md) | Subsubject 050 index |
| [`../README.md`](../README.md) | 050_General subsection index |
