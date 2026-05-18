---
document_id: QATL-ATLAS-1000-STA-110-119-01-113-070-LUBRICATION-WEAR-COLD-WELDING-AND-VACUUM-COMPATIBILITY
title: "STA 110-119 · 113-070 — Lubrication Wear Cold Welding and Vacuum Compatibility"
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
subsubject: "070"
subsubject_title: "Lubrication Wear Cold Welding and Vacuum Compatibility"
---
# STA 110-119 · 113-070 — Lubrication Wear Cold Welding and Vacuum Compatibility

## 1. Purpose

Defines the **tribology and vacuum-compatibility requirements** for space mechanisms, covering lubricant selection, wear-life budgets, cold-welding prevention, outgassing limits, and material-pair compatibility per ECSS-E-ST-33-01C[^ecsse3301] and ECSS-Q-ST-70C[^iso9283].

## 2. Scope

- Covers the *Lubrication, Wear, Cold Welding and Vacuum Compatibility* subsubject (`007`) of subsection `113`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Dry lubricants** — MoS₂ (sputtered/burnished), PTFE-filled composites, WS₂ coatings, and ion-beam-deposited DLC; application methods and thickness specifications.
  - **Fluid lubricants** — Braycote 601EF, Nye-tril 181, and Krytox GPL-series greases; operating temperature range, viscosity index, and contamination control requirements.
  - **Wear mechanisms** — adhesive wear, abrasive wear, fretting wear, and fatigue-spalling; wear-life model (Archard equation) and wear-rate testing per ISO 9283[^iso9283].
  - **Cold welding** — adhesion of like-metal pairs in vacuum; prohibited contact pairs (Au–Au, In–In, Al–Al), mandatory dissimilar-material interfaces, and thin-film barrier coatings.
  - **Outgassing and contamination** — TML ≤ 1.0 % and CVCM ≤ 0.1 % per ECSS-Q-ST-70C; lubricant outgassing rates and compatibility with adjacent optical surfaces and electronics.
  - **Vacuum compatibility testing** — tribometer testing in representative vacuum (≤ 10⁻⁶ mbar), thermal-vacuum cycling, and lubricant life-test matrix.

## 3. Diagram — Tribology and Vacuum Compatibility Logic

```mermaid
flowchart TB
    MAT["Material-Pair Selection<br/>(cold-weld avoidance · dissimilar metals)"]
    MAT --> DRY["Dry Lubricants<br/>(MoS₂ · PTFE · WS₂ · DLC)"]
    MAT --> FLU["Fluid Lubricants<br/>(Braycote · Nye-tril · Krytox)"]
    DRY & FLU --> WEAR["Wear-Life Budget<br/>(Archard model · tribometer test)"]
    DRY & FLU --> OUT["Outgassing Check<br/>(TML ≤ 1.0 % · CVCM ≤ 0.1 %)"]
    WEAR & OUT --> TV["Thermal-Vacuum Life Test<br/>(≤ 10⁻⁶ mbar · cycling)"]
    TV --> EV["Evidence Package<br/>(→ 113-080)"]
    style MAT fill:#1f3a93,color:#fff
    style EV fill:#2c82c9,color:#fff
```

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `113` — Mecanismos Espaciales y Desplegables |
| Subsubject | `070` — Lubrication Wear Cold Welding and Vacuum Compatibility |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/113_Mecanismos-Espaciales-y-Desplegables/` |
| Document | `113-070-Lubrication-Wear-Cold-Welding-and-Vacuum-Compatibility.md` (this file) |
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
