---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-060-LINE-BASE-AND-DEPOT-MAINTENANCE-BOUNDARIES"
title: "ATLAS 050-059 · 05.050.060 — Line, Base and Depot Maintenance Boundaries"
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
subsubject: "060"
subsubject_title: "Line, Base and Depot Maintenance Boundaries"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.050.060 — Line, Base and Depot Maintenance Boundaries

## 1. Purpose

Defines the **line, base, and depot maintenance level boundaries** for AMPEL360 eWTW structural tasks: which tasks may be accomplished at line (transit/overnight), which require base-maintenance access and tooling, and which require full depot-level disassembly — ensuring that structural maintenance activities are assigned to the capability level at which they can be safely and effectively performed.

## 2. Scope

### 2.1 Context

Maintenance level boundaries for structural tasks are driven by three factors: access complexity (how many panels, fairings, or structural covers must be removed); tooling and equipment requirements (standard vs. special tooling, calibrated NDT equipment); and skill and certification requirements (level 2 NDT certification, composite repair authorisation). The AMPEL360 eWTW's high composite content means that many structural inspections require thermographic or HFEC equipment available only at certified base-maintenance facilities.

Line-maintenance structural tasks are typically limited to visual walk-around checks, minor damage assessment against ADL tables, and opportunistic visual access via already-open doors. Depot-level tasks include wing-spar HFEC inspections requiring full wing-panel removal, LH₂ tank attach-fitting inspections, and major repairs requiring autoclave cure capability.

### 2.2 Maintenance Level Allocation

```mermaid
flowchart LR
    A[Structural Task] --> B{Access type?}
    B -->|Walk-around or door access| C[Line Maintenance L]
    B -->|Panel removal required| D{Tooling?}
    D -->|Standard tooling| E[Base Maintenance B]
    D -->|Special tooling or NDT equipment| F{Depot NDT capability?}
    F -->|Yes| G[Base or Depot B-D]
    F -->|No, autoclave required| H[Depot Maintenance D]
    C --> I[AMM Task Card]
    E --> I
    G --> I
    H --> I
```

### 2.3 Structural Task Level Allocation Summary

| Task Type | Level | Access Required | Certification |
|---|---|---|---|
| Visual walk-around (skin, doors) | L | None — external | Cat A line certifier |
| General visual (open-panel access) | B | Standard panel removal | Cat B1/B2 base certifier |
| HFEC lap-joint inspection | B | Panel removal + HFEC probe | Level 2 HFEC + Cat B1 |
| Thermographic CFRP inspection | B | Panel removal + thermographic equipment | Level 2 thermographic |
| LH₂ fitting DPI inspection | D | Full belly-fairing removal | Level 2 DPI + H₂ hazmat cert |
| Wing spar cap HFEC (access panel removed) | D | Wing under-surface panel removal | Level 2 HFEC + authorised inspector |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-060-LINE-BASE-AND-DEPOT-MAINTENANCE-BOUNDARIES` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/050_General/050-060-Maintenance-Concept-General/` |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| MSG-3 Rev 3 | Maintenance level allocation rules |
| EASA Part-145 | Maintenance organisation approval — capability scopes |
| EASA Part-66 | Aircraft maintenance licence — NDT certifications |
| [`./README.md`](./README.md) | Subsubject 060 index |
| [`../README.md`](../README.md) | 050_General subsection index |
