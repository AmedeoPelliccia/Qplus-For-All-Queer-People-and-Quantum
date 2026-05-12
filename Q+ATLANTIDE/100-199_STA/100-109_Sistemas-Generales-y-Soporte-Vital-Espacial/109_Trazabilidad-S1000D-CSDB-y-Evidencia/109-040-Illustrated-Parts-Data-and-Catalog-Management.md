---
document_id: QATL-ATLAS-1000-STA-100-109-00-109-040-ILLUSTRATED-PARTS-DATA-AND-CATALOG-MANAGEMENT
title: "STA 100-109 · 109-040 — Illustrated-Parts-Data-and-Catalog-Management"
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
subsubject: "040"
subsubject_title: "Illustrated-Parts-Data-and-Catalog-Management"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 109-040 — Illustrated-Parts-Data-and-Catalog-Management

## 1. Purpose

Defines the **Illustrated Parts Data (IPD) and catalog management** architecture for Q+ATLANTIDE subsystems `100-109`, specifying parts data module structure, figure numbering, and ASD S2000M integration per S1000D Issue 5.0[^s1000d] and ASD S2000M[^asds2000m].

IPD data modules (infoCode 941 — Illustrated Parts Data): structured parts breakdown with figure references, part numbers, cage codes, quantity per assembly, and effectivity. Parts catalog: each LRU (Line Replaceable Unit) and ORU (On-orbit Replaceable Unit) in subsystems 100–109 has an IPD entry; parts linked to maintenance procedures (infoCode 700) and procurement data (ASD S2000M[^asds2000m]). Figure numbering: S1000D IPD figure sheets with hotspot annotations linking figure callouts to parts table rows. Parts data lifecycle: new parts added via CCB-approved change request; deleted/superseded parts retained with deletion record for traceability; interchangeable parts listed with all interchange candidates.

## 2. Scope

- Covers the *Illustrated-Parts-Data-and-Catalog-Management* subsubject (`040`) of subsection `109`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All CSDB data modules governed by the BREX rules defined in `109-010` and the S1000D Issue 5.0 standard[^s1000d].

## 3. Diagram — Illustrated-Parts-Data-and-Catalog-Management

```mermaid
flowchart TB
    IPD_DM["IPD Data Module<br/>(infoCode 941 · parts breakdown)"]
    IPD_DM --> PART_TABLE["Parts Table<br/>(part no · cage · qty · effectivity)"]
    IPD_DM --> FIGURES["IPD Figures<br/>(hotspot annotations)"]
    PART_TABLE --> MX_PROC["Maintenance Procedure<br/>(infoCode 700 · cross-ref)"]
    PART_TABLE --> S2000M["ASD S2000M<br/>(procurement · materiel mgmt)"]
    PART_TABLE --> CCB_CHANGE["CCB Change Request<br/>(parts lifecycle)"]
    style IPD_DM fill:#2c82c9,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `109` — Trazabilidad S1000D, CSDB y Evidencia |
| Subsubject | `040` — Illustrated-Parts-Data-and-Catalog-Management |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/109_Trazabilidad-S1000D-CSDB-y-Evidencia/` |
| Document | `109-040-Illustrated-Parts-Data-and-Catalog-Management.md` (this file) |
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
