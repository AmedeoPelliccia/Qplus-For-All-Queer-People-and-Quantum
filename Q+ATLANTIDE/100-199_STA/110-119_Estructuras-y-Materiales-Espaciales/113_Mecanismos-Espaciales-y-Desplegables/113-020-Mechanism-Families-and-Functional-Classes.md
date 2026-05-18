---
document_id: QATL-ATLAS-1000-STA-110-119-01-113-020-MECHANISM-FAMILIES-AND-FUNCTIONAL-CLASSES
title: "STA 110-119 · 113-020 — Mechanism Families and Functional Classes"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "110-119"
section: "01"
section_title: "Estructuras y Materiales Espaciales"
subsection: "113"
subsection_title: "Mecanismos Espaciales y Desplegables"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
subsubject: "020"
subsubject_title: "Mechanism Families and Functional Classes"
---
# STA 110-119 · 113-020 — Mechanism Families and Functional Classes

## 1. Purpose

Defines the **taxonomy of space mechanism families and functional classes** used to classify all STA `113` mechanisms, establishing consistent identification, heritage traceability, and design-rule assignment per ECSS-E-ST-33-01C[^ecsse3301].

## 2. Scope

- Covers the *Mechanism Families and Functional Classes* subsubject (`002`) of subsection `113`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Deployment mechanisms** — solar array deployment, antenna boom deployment, mast extension, and membrane deployment mechanisms driven by spring-stored energy or motor drive.
  - **Retention and release mechanisms** — hold-down release devices (HDR), non-explosive actuators (NEA), pyrotechnic release devices, and clamp-band systems.
  - **Drive and pointing mechanisms** — solar array drive assembly (SADA), antenna pointing mechanisms (APM), scan mechanisms, and articulated platform drives.
  - **Docking and berthing mechanisms** — soft-capture mechanisms, active/passive common berthing mechanisms (CBM), International Docking System Standard (IDSS) compliant interfaces.
  - **Bearing and interface mechanisms** — slip rings, rotary joints, flexible connections, and slip/flex interfaces for power and signal transfer across rotating interfaces.
  - **Functional class matrix** — classification by mission criticality (MCI / non-MCI), deployment type (single-shot / multi-cycle), and drive type (pyrotechnic / spring / motor / pneumatic).

## 3. Diagram — Mechanism Families and Functional Classes

```mermaid
flowchart TB
    ROOT["Space Mechanism Taxonomy<br/>(ECSS-E-ST-33-01C)"]
    ROOT --> DEP["Deployment Mechanisms<br/>(solar array · boom · mast · membrane)"]
    ROOT --> RET["Retention and Release<br/>(HDR · NEA · pyrotechnic · clamp-band)"]
    ROOT --> DRV["Drive and Pointing<br/>(SADA · APM · scan · articulated)"]
    ROOT --> DOC["Docking and Berthing<br/>(soft-capture · CBM · IDSS)"]
    ROOT --> BRG["Bearing and Interface<br/>(slip-ring · rotary joint · flex)"]
    DEP --> MCI["MCI Classification<br/>(single-shot / multi-cycle)"]
    RET --> MCI
    style ROOT fill:#1f3a93,color:#fff
    style MCI fill:#2c82c9,color:#fff
```

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `113` — Mecanismos Espaciales y Desplegables |
| Subsubject | `020` — Mechanism Families and Functional Classes |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/113_Mecanismos-Espaciales-y-Desplegables/` |
| Document | `113-020-Mechanism-Families-and-Functional-Classes.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`113-000-General.md`](./113-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `110-119` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ecsse3301]: **ECSS-E-ST-33-01C Rev.2 — Space Engineering: Mechanisms** — European standard governing design, development, qualification and acceptance of space mechanisms including release devices, hinges, latches, drives and deployable systems.

[^ecsse33]: **ECSS-E-ST-33C — Space Engineering: Mechanisms General Requirements** — European standard defining general requirements for space mechanism design, analysis, testing, and documentation.

[^nasastd5017]: **NASA-STD-5017A — Design, Development, and Test Standard for Mechanisms** — NASA standard for mechanism design, development, qualification and acceptance testing.

[^nasahdbk7005]: **NASA-HDBK-7005 — Dynamic Environmental Criteria** — NASA handbook providing dynamic environmental criteria applicable to mechanism qualification testing.

[^iso9283]: **ISO 9283:1998 — Manipulating Industrial Robots: Performance Criteria and Related Test Methods** — Applicable to robotic deployment and drive systems performance characterisation.

### Applicable industry standards

- ECSS-E-ST-33-01C Rev.2 — Space Engineering: Mechanisms[^ecsse3301]
- ECSS-E-ST-33C — Space Engineering: Mechanisms General Requirements[^ecsse33]
- NASA-STD-5017A — Design, Development, and Test Standard for Mechanisms[^nasastd5017]
- NASA-HDBK-7005 — Dynamic Environmental Criteria[^nasahdbk7005]
- ISO 9283:1998 — Manipulating Industrial Robots: Performance Criteria and Related Test Methods[^iso9283]
