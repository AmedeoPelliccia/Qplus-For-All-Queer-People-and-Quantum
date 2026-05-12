---
document_id: QATL-ATLAS-1000-STA-100-109-00-109-030-DMC-SCHEMA-AND-SNS-MAPPING
title: "STA 100-109 · 109-030 — DMC-Schema-and-SNS-Mapping"
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
subsubject: "030"
subsubject_title: "DMC-Schema-and-SNS-Mapping"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 109-030 — DMC-Schema-and-SNS-Mapping

## 1. Purpose

Defines the **Data Module Code (DMC) schema and Standard Numbering System (SNS) mapping** for the Q+ATLANTIDE `100-109` code range per S1000D Issue 5.0[^s1000d].

DMC structure (S1000D 17-field): `{modelIdentCode}-{systemDiffCode}-{systemCode}-{subSystemCode}-{subSubSystemCode}-{assyCode}-{disassyCode}-{disassyCodeVariant}-{infoCode}-{infoCodeVariant}-{itemLocationCode}-{learnCode}-{learnEventCode}`. Q+ATLANTIDE mapping: modelIdentCode = `QATL`; systemCode derived from subsection number (e.g., `106` for Crew Health); subSystemCode from subsubject NNN code; infoCode by data module type (040 = description, 500 = procedure, 700 = maintenance, 912 = wiring data, 042 = BREX). SNS for `100-109`: top-level system codes 100–109 map to subsections; sub-system codes 000–090 map to subsubjects. SNS published as CSDB SNS data module and version-controlled.

## 2. Scope

- Covers the *DMC-Schema-and-SNS-Mapping* subsubject (`030`) of subsection `109`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All CSDB data modules governed by the BREX rules defined in `109-010` and the S1000D Issue 5.0 standard[^s1000d].

## 3. Diagram — DMC-Schema-and-SNS-Mapping

```mermaid
flowchart LR
    DMC_PARTS["DMC Field Structure<br/>(QATL-A-{sys}-{sub}-{ass}-…-{info}-A-{loc})"]
    DMC_PARTS --> QATL["modelIdentCode: QATL"]
    DMC_PARTS --> SYS["systemCode: 100–109<br/>(subsection number)"]
    DMC_PARTS --> SUB["subSystemCode: 000–090<br/>(subsubject NNN)"]
    DMC_PARTS --> INFO["infoCode: type<br/>(040·500·700·042)"]

    SNS_MAP["SNS Map<br/>(100-109 → subsections)"]
    SNS_MAP --> SYS
    style DMC_PARTS fill:#2c82c9,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `109` — Trazabilidad S1000D, CSDB y Evidencia |
| Subsubject | `030` — DMC-Schema-and-SNS-Mapping |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/109_Trazabilidad-S1000D-CSDB-y-Evidencia/` |
| Document | `109-030-DMC-Schema-and-SNS-Mapping.md` (this file) |
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
