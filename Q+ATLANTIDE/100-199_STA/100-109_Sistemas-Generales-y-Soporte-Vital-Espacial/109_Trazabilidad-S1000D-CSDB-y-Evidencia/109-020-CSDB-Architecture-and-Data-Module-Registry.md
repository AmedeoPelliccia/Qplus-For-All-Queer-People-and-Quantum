---
document_id: QATL-ATLAS-1000-STA-100-109-00-109-020-CSDB-ARCHITECTURE-AND-DATA-MODULE-REGISTRY
title: "STA 100-109 · 109-020 — CSDB-Architecture-and-Data-Module-Registry"
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
subsubject: "020"
subsubject_title: "CSDB-Architecture-and-Data-Module-Registry"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 109-020 — CSDB-Architecture-and-Data-Module-Registry

## 1. Purpose

Defines the **CSDB architecture, data module registry, and storage governance** for the Q+ATLANTIDE `100-109` code range per S1000D Issue 5.0[^s1000d] and ISO 10303-239[^iso10303].

CSDB architecture: structured repository containing: (1) Data Modules (DM) — the fundamental content units; (2) Data Module List (DML) — registry of all DMs with status, version, and applicability; (3) Publication Modules (PM) — assembly rules defining technical publications from DMs; (4) BREX DMs — governing business rules; (5) Applicability Cross-Reference Table (ACT) — maps product configurations to applicable DMs. Storage: version-controlled repository (Git-compatible); all DMs stored as XML (S1000D schema); human-readable markdown mirrors maintained as Q+ATLANTIDE canonical format. Registry fields per DM: DMC, title, type, issue number, status (preliminary/approved/deleted), applicability, responsible author, CCB approval reference.

## 2. Scope

- Covers the *CSDB-Architecture-and-Data-Module-Registry* subsubject (`020`) of subsection `109`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All CSDB data modules governed by the BREX rules defined in `109-010` and the S1000D Issue 5.0 standard[^s1000d].

## 3. Diagram — CSDB-Architecture-and-Data-Module-Registry

```mermaid
flowchart TB
    CSDB["Common Source Data Base (CSDB)"]
    CSDB --> DML["Data Module List (DML)<br/>(registry · status · version)"]
    CSDB --> DM_STORE["Data Module Storage<br/>(XML S1000D · markdown mirror)"]
    CSDB --> PM["Publication Modules (PM)<br/>(assembly rules)"]
    CSDB --> ACT["Applicability Cross-Ref Table<br/>(ACT · product config)"]
    CSDB --> BREX_STORE["BREX Documents<br/>(governing rules)"]

    DML --> CCB_TRACK["CCB Tracking<br/>(approval references)"]
    style CSDB fill:#2c82c9,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `109` — Trazabilidad S1000D, CSDB y Evidencia |
| Subsubject | `020` — CSDB-Architecture-and-Data-Module-Registry |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/109_Trazabilidad-S1000D-CSDB-y-Evidencia/` |
| Document | `109-020-CSDB-Architecture-and-Data-Module-Registry.md` (this file) |
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
