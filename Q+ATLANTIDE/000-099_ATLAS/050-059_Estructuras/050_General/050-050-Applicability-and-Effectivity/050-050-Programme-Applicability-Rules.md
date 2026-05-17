---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-050-PROGRAMME-APPLICABILITY-RULES"
title: "ATLAS 050-059 · 05.050.050 — Programme Applicability Rules"
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
subsubject_title: "Programme Applicability Rules"
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

# ATLAS 050-059 · 05.050.050 — Programme Applicability Rules

## 1. Purpose

Defines the **programme-level applicability rules** governing how [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT] structural documents, tasks, and limits are scoped to the overall programme: the applicability hierarchy, authoring conventions, and the change-control process that updates applicability when a new derivative or major modification enters the programme.

## 2. Scope

### 2.1 Context

Programme applicability is the highest-level applicability layer, encompassing all aircraft types within the [PROGRAMME-AIRCRAFT] family. A document or task tagged with programme-level applicability applies to every [PROGRAMME-AIRCRAFT] aircraft unless overridden by a more specific model, variant, or serial-number effectivity. Programme applicability rules are owned by the Programme Office and reviewed at each programme milestone (PDR, CDR, TRR).

Authoring rules specify that every structural ATLAS document must declare an `applicability` field in its YAML frontmatter, and every S1000D data module must carry a corresponding `<applic>` element populated from the PDCM. Documents with programme-wide scope use the token `ALL-[PROGRAMME-AIRCRAFT]` as their applicability code.

### 2.2 Programme Applicability Resolution

```mermaid
flowchart TD
    A[Document Authoring] --> B{Applicability Level?}
    B -->|Programme-wide| C[Tag: ALL-[PROGRAMME-AIRCRAFT]]
    B -->|Model-specific| D[Tag: [PROGRAMME-AIRCRAFT]-ER or [PROGRAMME-AIRCRAFT]-F etc]
    B -->|SN-block| E[Tag: SN 001-150 etc]
    C --> F[PDCM Programme Register]
    D --> F
    E --> F
    F --> G[S1000D CSDB applic element]
    G --> H[Publication filter output]
```

### 2.3 Programme Applicability Hierarchy

| Level | Code Pattern | Description | Override Lower? |
|---|---|---|---|
| Programme | `ALL-[PROGRAMME-AIRCRAFT]` | All variants and serial numbers | No (highest scope) |
| Type | `[PROGRAMME-AIRCRAFT]-{type}` | Specific model type (baseline, ER, F) | Yes (narrows) |
| Configuration | `[PROGRAMME-AIRCRAFT]-{type}-C{n}` | Configuration baseline | Yes |
| Serial block | `SN-{from}-{to}` | Production block | Yes |
| Post-SB | `POST-SB-{number}` | Aircraft incorporating specific SB | Yes |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-050-PROGRAMME-APPLICABILITY-RULES` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/050_General/050-050-Applicability-and-Effectivity/` |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| S1000D Issue 5.0 | Applicability filtering and CSDB authoring |
| ATA iSpec 2200 | Chapter 5 — effectivity management |
| PDCM-[PROGRAMME-AIRCRAFT]-001 | Product Definition and Configuration Management Plan |
| [`./README.md`](./README.md) | Subsubject 050 index |
| [`../README.md`](../README.md) | 050_General subsection index |
