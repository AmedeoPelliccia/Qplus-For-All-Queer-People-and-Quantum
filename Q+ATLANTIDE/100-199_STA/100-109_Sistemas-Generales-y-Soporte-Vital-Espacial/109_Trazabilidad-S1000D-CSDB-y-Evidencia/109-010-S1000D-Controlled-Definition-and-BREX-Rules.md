---
document_id: QATL-ATLAS-1000-STA-100-109-00-109-010-S1000D-CONTROLLED-DEFINITION-AND-BREX-RULES
title: "STA 100-109 · 109-010 — S1000D-Controlled-Definition-and-BREX-Rules"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "100-109"
section: "00"
section_title: "Sistemas Generales y Soporte Vital Espacial"
subsection: "109"
subsection_title: "Trazabilidad S1000D, CSDB y Evidencia"
subsubject: "010"
subsubject_title: "S1000D-Controlled-Definition-and-BREX-Rules"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 109-010 — S1000D-Controlled-Definition-and-BREX-Rules

## 1. Purpose

Establishes the **controlled normative definition** of S1000D and the Q+ATLANTIDE Business Rules Exchange (BREX) document, fixing the BREX rule set governing all data modules in the `100-109` code range per S1000D Issue 5.0[^s1000d].

Controlled terms: **BREX** (Business Rules Exchange — S1000D document type that defines project-specific usage rules for data module content, structure, and coding); **DMC** (Data Module Code — 17-field alphanumeric identifier unique to each data module); **SNS** (Standard Numbering System — hierarchical system map that maps physical/functional breakdown to DMC fields); **CSDB** (Common Source Data Base — repository of all S1000D data modules); **Issue** (approved version of a data module, stored with issue number and date); **Applicability** (conditional filter applying data module content to specific product variants or configurations). BREX scope: applies to all S1000D data modules authored for the `100-109` code range; BREX version controlled per subsection 109 CCB.

## 2. Scope

- Covers the *S1000D-Controlled-Definition-and-BREX-Rules* subsubject (`010`) of subsection `109`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All CSDB data modules governed by the BREX rules defined in `109-010` and the S1000D Issue 5.0 standard[^s1000d].

## 3. Diagram — S1000D-Controlled-Definition-and-BREX-Rules

```mermaid
flowchart LR
    BREX_DOC["BREX Document<br/>(Q+ATLANTIDE 100-109 BREX v1.0)"]
    BREX_DOC --> RULE1["Structure Rules<br/>(permitted XML elements)"]
    BREX_DOC --> RULE2["Coding Rules<br/>(DMC · SNS constraints)"]
    BREX_DOC --> RULE3["Applicability Rules<br/>(variant/config filter)"]
    BREX_DOC --> RULE4["Language Rules<br/>(ASD-STE100 enforcement)"]
    ALL_DMS["All DMs in 100–109"] --> BREX_VALID["BREX Validation<br/>(automated CI check)"]
    BREX_DOC --> BREX_VALID
    style BREX_DOC fill:#2c82c9,color:#fff
    style BREX_VALID fill:#2c82c9,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `109` — Trazabilidad S1000D, CSDB y Evidencia |
| Subsubject | `010` — S1000D-Controlled-Definition-and-BREX-Rules |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/109_Trazabilidad-S1000D-CSDB-y-Evidencia/` |
| Document | `109-010-S1000D-Controlled-Definition-and-BREX-Rules.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`109-000-General.md`](./109-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management.

[^s1000d]: **S1000D Issue 5.0 — International Specification for Technical Publications** — Governing standard for CSDB data module coding, SNS mapping, BREX, and technical publication production.

[^asdste100]: **ASD-STE100 Issue 7 — Simplified Technical English** — Writing standard for all S1000D procedural and descriptive content.

[^iso10303]: **ISO 10303-239 — STEP Product Life Cycle Support (PLCS)** — Data exchange standard for product and maintenance data compatible with S1000D CSDB.

[^asds2000m]: **ASD S2000M — International Specification for Materiel Management** — Parts data management integrated with CSDB IPD/illustrated parts data.

### Applicable industry standards

- S1000D Issue 5.0 — International Specification for Technical Publications[^s1000d]
- ASD-STE100 Issue 7 — Simplified Technical English[^asdste100]
- ISO 10303-239 — STEP PLCS[^iso10303]
- ASD S2000M — International Specification for Materiel Management[^asds2000m]
