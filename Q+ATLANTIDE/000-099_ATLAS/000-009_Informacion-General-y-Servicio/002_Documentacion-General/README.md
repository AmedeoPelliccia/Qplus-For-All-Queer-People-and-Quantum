---
document_id: QATL-ATLAS-1000-ATLAS-000-009-00-002-README
title: "ATLAS 000-009 · 00.002 — Documentación General (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "000-009"
section: "00"
section_title: "Información General y Servicio"
subsection: "002"
subsection_title: "Documentación General"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-GROUND, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 000-009 · Section 00 · Subsection 002 — Documentación General

## 1. Purpose

Subsection-level index for *Documentación General* (`002`) within ATLAS `000-009` — *Información General y Servicio* — Publication set, S1000D CSDB architecture, revision control, and language/localization policy.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is the **third Subject** of the first Code range (`000-009`) of the ATLAS master range (`000–099`), and serves as the publication-control layer that materialises what ATLAS describes.

## 2. Scope

- Defines and governs the subsubject namespace `000`–`099` of subsection `002` *Documentación General*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Contains the Overview, canonical publication-set mapping, S1000D/CSDB architecture, publication-module assembly, revision control, and language/localization policy for the programme.
- **Boundary rule**: this subsection defines the *structure* of publication; the *content* of published data modules lives in each Code range's CSDB respectively.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 001 | Publication Set and Manual Map | [`001_Publication-Set-and-Manual-Map.md`](./001_Publication-Set-and-Manual-Map.md) | active |
| 002 | S1000D CSDB and Data Modules | [`002_S1000D-CSDB-and-Data-Modules.md`](./002_S1000D-CSDB-and-Data-Modules.md) | active |
| 003 | Publication Modules and Manuals | [`003_Publication-Modules-and-Manuals.md`](./003_Publication-Modules-and-Manuals.md) | active |
| 004 | Revision, Issue and Distribution Control | [`004_Revision-Issue-and-Distribution-Control.md`](./004_Revision-Issue-and-Distribution-Control.md) | active |
| 005 | Language, Localization and STE | [`005_Language-Localization-and-STE.md`](./005_Language-Localization-and-STE.md) | active |

## 4. Interfaces Diagram

```mermaid
flowchart TB
    SEC["Section 00 · 000-009<br/>Información General y Servicio"]:::sec
    SUB["Subsection 002<br/>Documentación General"]:::sub
    SEC --> SUB

    subgraph SUBS["Subsubjects"]
        direction LR
        S000["000 — Overview"]:::sss
        S001["001 — Publication Set<br/>& Manual Map"]:::sss
        S002["002 — S1000D CSDB<br/>& Data Modules"]:::sss
        S003["003 — Publication Modules<br/>& Manuals"]:::sss
        S004["004 — Revision, Issue<br/>& Distribution Control"]:::sss
        S005["005 — Language,<br/>Localization & STE"]:::sss
    end
    SUB --> SUBS

    QPRIM["Q-DATAGOV<br/>(primary Q-Division)"]:::qdiv
    QSUPP["Q-GROUND, Q-AIR<br/>(support Q-Divisions)"]:::qdiv
    ORB["ORB-PMO, ORB-LEG<br/>(ORB support)"]:::orb

    SUB --> QPRIM
    SUB -.-> QSUPP
    SUB -.-> ORB

    CSDB["CSDB<br/>(content lives in each<br/>Code range)"]:::ext
    SUB -. "defines structure;<br/>content in CSDB" .- CSDB

    classDef sec fill:#2c82c9,stroke:#0b1d4a,color:#fff
    classDef sub fill:#eaf3fb,stroke:#2c82c9,color:#0b1d4a
    classDef sss fill:#d5eaff,stroke:#2c82c9,color:#0b1d4a
    classDef qdiv fill:#f6e6ff,stroke:#7d3c98,color:#3b1f4d
    classDef orb fill:#fff4dd,stroke:#b9770e,color:#5a3b00
    classDef ext fill:#fdebd0,stroke:#b9770e,color:#5a3b00,stroke-dasharray:3 3
```

*Solid arrows show parent→subsection→subsubject ownership and primary Q-Division authority; dotted arrows show support Q-Divisions, ORB enterprise support, and the CSDB boundary.*

## 5. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `000-009` |
| Section | `00` — Información General y Servicio |
| Subsection | `002` — Documentación General |
| Subsubject namespace | `000`–`099` |
| Subsubjects populated | 6 (000–005) |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-GROUND, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/000-009_Informacion-General-y-Servicio/002_Documentacion-General/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-DATAGOV` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `000`–`099` shall preserve those header fields and reuse the footnote set declared here.

## Sibling-Subject Pointers

| Subject | Folder | Relationship |
|---|---|---|
| `000` — Identificación | [`../000_Identificacion/`](../000_Identificacion/) | Aircraft/programme identifiers that appear in publication metadata and DMC |
| `001` — Configuración | [`../001_Configuracion/`](../001_Configuracion/) | Effectivity/variant data consumed by Publication Modules (PM applicability filtering) |
| `003` — Operaciones Básicas | [`../003_Operaciones-Basicas/`](../003_Operaciones-Basicas/) | Operational-procedure DMs that are assembled and published per this subsection's rules |

## Change Log

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-05-07 | Initial population of subsubjects 000–005; status promoted to active |

## 6. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
