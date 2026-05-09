---
document_id: QATL-ATLAS-1000-STA-110-119-01-110-020-PRIMARY-AND-SECONDARY-STRUCTURAL-ELEMENTS
title: "STA 110-119 · 110-020 — Primary and Secondary Structural Elements"
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
subsection: "110"
subsection_title: "Estructuras Orbitales"
subsubject: "020"
subsubject_title: "Primary and Secondary Structural Elements"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 110-119 · 110-020 — Primary and Secondary Structural Elements

## 1. Purpose

Defines the **architecture and classification of primary and secondary structural elements** for orbital systems — covering load-bearing primary structure, secondary bracketry, equipment panels, and interface fittings — per ECSS-E-ST-32C[^ecsse32].

## 2. Scope

- Covers the *Primary and Secondary Structural Elements* subsubject (`002`) of subsection `110`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Primary structure** — load-bearing elements that carry design limit loads and transfer structural loads to the launch vehicle interface (LVI) or habitat primary ring; must satisfy DUL margins without failure.
  - **Secondary structure** — non-load-path-critical elements (equipment panels, thermal blanket attachment brackets, cable trays, handrail fittings) requiring minimum MoS = 0.0 at DLL.
  - **Structural topology** — longerons, frames, ribs, honeycomb sandwich panels, and monocoque shells; material selection from `111`.
  - **Interface fittings** — mechanical interfaces between modules (bolted flanges, alignment pins, separation bolts); ICD documentation requirement.
  - **Mass budget** — structural mass estimation methodology; mass margin policy (15% at PDR, 5% at CDR per ECSS-E-ST-32C[^ecsse32]).
  - **Manufacturing and assembly constraints** — minimum bend radii, fastener access windows, surface treatment requirements (→ `111`).

## 3. Diagram — Primary/Secondary Structural Element Hierarchy

```mermaid
flowchart TB
    LVI["Launch Vehicle Interface (LVI)<br/>(separation system)"]
    LVI --> PRI["Primary Structure<br/>(longerons · frames · shells · rings)"]
    PRI --> SEC["Secondary Structure<br/>(panels · brackets · trays · fittings)"]
    PRI --> MOD["Module-to-Module Interface<br/>(bolted flange · ICD)"]
    SEC --> EQUIP["Equipment / Payload<br/>(mounted on secondary)"]
    MOD --> DOCK["Docking / Berthing Interface<br/>(→ 005)"]

    style PRI fill:#1f3a93,color:#fff
    style LVI fill:#2c82c9,color:#fff
```

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `110` — Estructuras Orbitales |
| Subsubject | `002` — Primary and Secondary Structural Elements |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/110_Estructuras-Orbitales/` |
| Document | `110-020-Primary-and-Secondary-Structural-Elements.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`110-000-General.md`](./110-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `110-119` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ecsse32]: **ECSS-E-ST-32C Rev.1 — Space Engineering: Structural General Requirements** — European standard governing structural design, analysis, testing, and documentation for space systems.

[^ecsse3210]: **ECSS-E-ST-32-10C — Space Engineering: Structural Factors of Safety for Spaceflight Hardware** — European standard defining factors of safety applicable to STA structural elements.

[^nasastd5001]: **NASA-STD-5001B — Structural Design and Test Factors of Safety for Spaceflight Hardware** — NASA factors-of-safety standard applicable to orbital structure design and test verification.

[^nasatm2012]: **NASA/TM-2012-217519 — Best Practices for Structural and Mechanical Systems** — NASA technical memo on structural design best practices for crewed and uncrewed systems.

[^iso11960]: **ISO 15630-1:2019 / ECSS-Q-ST-70C — Materials Testing and Qualification** — Material qualification and structural testing standard used in conjunction with ECSS-E-ST-32C.

### Applicable industry standards

- ECSS-E-ST-32C Rev.1 — Space Engineering: Structural General Requirements[^ecsse32]
- ECSS-E-ST-32-10C — Structural Factors of Safety for Spaceflight Hardware[^ecsse3210]
- NASA-STD-5001B — Structural Design and Test Factors of Safety[^nasastd5001]
- NASA/TM-2012-217519 — Best Practices for Structural and Mechanical Systems[^nasatm2012]
- ECSS-Q-ST-70C — Space Product Assurance: Materials, Processes and their Data[^iso11960]
