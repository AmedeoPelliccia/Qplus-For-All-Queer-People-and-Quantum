---
document_id: QATL-ATLAS-1000-STA-100-109-00-109-060-TECHNICAL-PUBLICATION-OUTPUT-AND-DELIVERY
title: "STA 100-109 · 109-060 — Technical-Publication-Output-and-Delivery"
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
subsubject: "060"
subsubject_title: "Technical-Publication-Output-and-Delivery"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 109-060 — Technical-Publication-Output-and-Delivery

## 1. Purpose

Defines the **technical publication output formats, rendering pipeline, and delivery architecture** for Q+ATLANTIDE `100-109` technical documentation per S1000D Issue 5.0[^s1000d] and ASD-STE100[^asdste100].

Output formats: S1000D page-oriented output (PDF via XSLT/XSL-FO transformation); S1000D interactive electronic technical publication (IETP, HTML5); on-board electronic procedure viewer (CSDB subset, secured, read-only on crew MFD). Publication modules (PM): define assembly order and applicability for each publication; publication types include: Crew Procedures Manual, Maintenance Manual, Emergency Procedures, IPD Catalog. Rendering pipeline: CSDB XML DMs → XSLT stylesheet → XSL-FO → PDF/HTML5 → quality check → delivery. ASD-STE100[^asdste100] compliance: automated STE checker run on all procedural DMs (infoCode 500) before release; non-compliant DMs returned to author. Delivery: crew on-board copy via CSDB sync; ground copy via CSDB master.

## 2. Scope

- Covers the *Technical-Publication-Output-and-Delivery* subsubject (`060`) of subsection `109`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All CSDB data modules governed by the BREX rules defined in `109-010` and the S1000D Issue 5.0 standard[^s1000d].

## 3. Diagram — Technical-Publication-Output-and-Delivery

```mermaid
flowchart LR
    CSDB_XML["CSDB XML Data Modules"]
    CSDB_XML --> XSLT["XSLT Stylesheet<br/>(XSL-FO)"]
    XSLT --> PDF["PDF Output<br/>(page-oriented)"]
    XSLT --> HTML5["HTML5 IETP<br/>(interactive)"]
    CSDB_XML --> ONBOARD["On-Board Viewer<br/>(secured subset · MFD)"]

    STE_CHECK["ASD-STE100 Checker<br/>(procedural DMs)"] --> CSDB_XML
    PDF & HTML5 & ONBOARD --> DELIVERY["Delivery<br/>(crew copy · ground master)"]
    style CSDB_XML fill:#2c82c9,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `109` — Trazabilidad S1000D, CSDB y Evidencia |
| Subsubject | `060` — Technical-Publication-Output-and-Delivery |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/109_Trazabilidad-S1000D-CSDB-y-Evidencia/` |
| Document | `109-060-Technical-Publication-Output-and-Delivery.md` (this file) |
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
