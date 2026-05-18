---
document_id: QATL-ATLAS-1000-STA-110-119-01-113-050-DOCKING-HATCH-SEAL-AND-ACCESS-MECHANISMS
title: "STA 110-119 · 113-050 — Docking Hatch Seal and Access Mechanisms"
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
subsubject: "050"
subsubject_title: "Docking Hatch Seal and Access Mechanisms"
---
# STA 110-119 · 113-050 — Docking Hatch Seal and Access Mechanisms

## 1. Purpose

Defines the **design and verification requirements** for docking, hatch, seal, and access mechanisms in Q+ATLANTIDE crewed-space and robotic-mission systems, covering soft-capture, hard-dock, pressure-seal, and EVA/IVA access mechanism design per ECSS-E-ST-33-01C[^ecsse3301] and IDSS interface requirements.

## 2. Scope

- Covers the *Docking, Hatch, Seal and Access Mechanisms* subsubject (`005`) of subsection `113`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Soft-capture mechanisms** — probe-and-drogue, androgynous peripheral assemblies (APAS), and IDSS-compliant low-impact docking system (LIDS); capture-cone geometry and misalignment tolerance.
  - **Hard-dock mechanisms** — structural latch sets, preload adjustment, and load-path verification through docked interface; structural handshake load cases.
  - **Hatch mechanisms** — inner pressure hatch, outer hatch, and combined hatch design; hatch actuation force, seal compression, and equalisation valve.
  - **Pressure seal design** — elastomeric dual-seal concepts, seal-groove geometry, leak-before-burst philosophy, and proof/leak-test requirements.
  - **EVA and IVA access mechanisms** — airlock inner/outer hatch, handrail and foot-restraint attachment fittings, tether anchor points, and EVA tool accommodation.
  - **Docking mechanism qualification** — capture envelope test, structural proof load, pressurisation/depressurisation cycling, and seal leak test evidence.

## 3. Diagram — Docking and Access Mechanism Architecture

```mermaid
flowchart TB
    SOFT["Soft-Capture Mechanism<br/>(probe-drogue · APAS · LIDS)"]
    SOFT --> HARD["Hard-Dock Latches<br/>(structural latch set · preload)"]
    HARD --> HATCH["Hatch Mechanisms<br/>(inner · outer · combined)"]
    HATCH --> SEAL["Pressure Seal<br/>(dual elastomeric · LBB · leak test)"]
    HATCH --> EVA["EVA / IVA Access<br/>(airlock · handrail · tether)"]
    SEAL --> QUAL["Docking Evidence<br/>(capture · proof load · cycling)"]
    style SOFT fill:#1f3a93,color:#fff
    style QUAL fill:#2c82c9,color:#fff
```

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `113` — Mecanismos Espaciales y Desplegables |
| Subsubject | `050` — Docking Hatch Seal and Access Mechanisms |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/113_Mecanismos-Espaciales-y-Desplegables/` |
| Document | `113-050-Docking-Hatch-Seal-and-Access-Mechanisms.md` (this file) |
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
