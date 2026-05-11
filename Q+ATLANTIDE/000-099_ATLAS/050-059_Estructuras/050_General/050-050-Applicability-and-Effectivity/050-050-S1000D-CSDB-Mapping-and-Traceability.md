---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-050-S1000D-CSDB-MAPPING-AND-TRACEABILITY"
title: "ATLAS 050-059 · 05.050.050 — S1000D CSDB Mapping and Traceability"
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
subsubject_title: "S1000D CSDB Mapping and Traceability"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.050.050 — S1000D CSDB Mapping and Traceability

## 1. Purpose

Defines the **S1000D data module code (DMC) mapping and CSDB traceability** for all applicability and effectivity documentation within subsubject `050`, ensuring each ATLAS document has a corresponding S1000D DMC and that the CSDB applicability annotations are consistent with the PDCM master effectivity register.

## 2. Scope

### 2.1 Context

Subsubject `050` applicability and effectivity documents are primarily descriptive (infoCode `040`) data modules in the S1000D sense — they describe the rules and data structures governing effectivity rather than providing step-by-step maintenance procedures. The CSDB system module (infoCode `00S`) captures the applicability cross-reference table that maps PDCM effectivity tokens to S1000D `<applic>` element values, providing the authoritative lookup used by all publication-filtering tools.

The AMPEL360 eWTW uses S1000D Issue 5.0 with the AMPEL360 project-specific Business Rules Decision Points (BRDPs) documented in BREX-AMPEL360-001.

### 2.2 CSDB Applicability Traceability Flow

```mermaid
flowchart LR
    A[PDCM Effectivity Token e.g. POST-SB-050-001] --> B[Cross-Reference Table DMC-AMPEL360-A-00S-050-00AA-00SA-A]
    B --> C[S1000D applic element value]
    C --> D[CSDB data module applic annotation]
    D --> E[Publication filter query]
    E --> F[Aircraft-specific output correct content only]
    B --> G[ATLAS YAML effectivity field]
    G --> H[ATLAS document version control]
```

### 2.3 DMC Assignment Table — Subsubject 050

| ATLAS Document | DMC (abbreviated) | Info Code | Status |
|---|---|---|---|
| Applicability-Overview | `DMC-AMPEL360-A-050-050-00AA-040A-A` | 040 — Description | draft |
| Programme-Applicability-Rules | `DMC-AMPEL360-A-050-050-01AA-040A-A` | 040 — Description | draft |
| Aircraft-Effectivity-Config-Baselines | `DMC-AMPEL360-A-050-050-02AA-040A-A` | 040 — Description | draft |
| Structural-Variant-Applicability | `DMC-AMPEL360-A-050-050-03AA-040A-A` | 040 — Description | draft |
| Serial-Number-Block-Effectivity | `DMC-AMPEL360-A-050-050-04AA-040A-A` | 040 — Description | draft |
| Retrofit-SB-Effectivity | `DMC-AMPEL360-A-050-050-05AA-040A-A` | 040 — Description | draft |
| Inspection-Applicability-Thresholds | `DMC-AMPEL360-A-050-050-06AA-040A-A` | 040 — Description | draft |
| Repair-Applicability-ADL | `DMC-AMPEL360-A-050-050-07AA-040A-A` | 040 — Description | draft |
| Applicability-Governance-Change | `DMC-AMPEL360-A-050-050-08AA-040A-A` | 040 — Description | draft |
| CSDB XRef Table | `DMC-AMPEL360-A-00S-050-00AA-00SA-A` | 00S — BREX/XRef | draft |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-050-S1000D-CSDB-MAPPING-AND-TRACEABILITY` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/050_General/050-050-Applicability-and-Effectivity/` |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| S1000D Issue 5.0 | International specification for technical publications |
| BREX-AMPEL360-001 | AMPEL360 Business Rules Exchange Object |
| ASD-STE100 | Simplified Technical English |
| [`./README.md`](./README.md) | Subsubject 050 index |
| [`../README.md`](../README.md) | 050_General subsection index |
