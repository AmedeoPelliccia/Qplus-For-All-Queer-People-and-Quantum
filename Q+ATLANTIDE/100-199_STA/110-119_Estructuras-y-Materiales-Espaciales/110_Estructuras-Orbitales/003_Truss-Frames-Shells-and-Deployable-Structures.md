---
document_id: QATL-ATLAS-1000-STA-110-119-01-110-003-TRUSS-FRAMES-SHELLS-AND-DEPLOYABLE-STRUCTURES
title: "STA 110-119 · 01.110.003 — Truss Frames Shells and Deployable Structures"
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
subsubject: "003"
subsubject_title: "Truss Frames Shells and Deployable Structures"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 110-119 · Section 01 · Subsection 110 · Subsubject 003 — Truss, Frames, Shells and Deployable Structures

## 1. Purpose

Defines the **structural topology options and design requirements** for truss assemblies, frame structures, shell/panel elements, and deployable structures used in orbital systems, per ECSS-E-ST-32C[^ecsse32].

## 2. Scope

- Covers the *Truss, Frames, Shells and Deployable Structures* subsubject (`003`) of subsection `110`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Truss assemblies** — space-frame trusses (ISS ITS-class), articulated trusses, thermal compensation truss design, and joint design (gussets, pin-connections, welded nodes).
  - **Frame structures** — ring frames, bulkheads, longerons, and keel structures; structural efficiency metrics (mass/stiffness ratio).
  - **Shell and panel elements** — cylindrical pressure shells (habitat modules), flat sandwich panels, conical adapters, and stiffened skins; design for minimum wall gauge and buckling stability.
  - **Deployable structures** — deployable solar array substrate trusses, hinged booms, unfurlable reflectors, and clamping/release mechanism interface with `150` (mechanisms); qualification test requirements for deployment reliability (≥ 99.5% reliability at 95% confidence per ECSS-E-ST-32C).
  - **Structural efficiency** — optimisation targets for truss and shell elements; finite element modelling requirements and mass-fraction targets.
  - **Launch stowage and deployment kinematics** — packed volume constraints, deployment sequence analysis, and deployment verification test.

## 3. Diagram — Structural Topology Options

```mermaid
flowchart LR
    subgraph FIXED["Fixed Structures"]
        TRUSS["Truss Assembly<br/>(space-frame)"]
        FRAME["Frame/Ring<br/>(bulkhead)"]
        SHELL["Shell/Panel<br/>(habitat module)"]
    end
    subgraph DEPLOY["Deployable Structures"]
        BOOM["Deployable Boom<br/>(solar array truss)"]
        UNFURL["Unfurlable<br/>(reflector / blanket)"]
    end
    TRUSS & FRAME & SHELL & BOOM & UNFURL --> LOADS["Load-Path Analysis<br/>(→ 004)"]
    BOOM & UNFURL --> MECH["Mechanisms Interface<br/>(→ 150)"]

    style LOADS fill:#1f3a93,color:#fff
```

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `110` — Estructuras Orbitales |
| Subsubject | `003` — Truss Frames Shells and Deployable Structures |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/110_Estructuras-Orbitales/` |
| Document | `003_Truss-Frames-Shells-and-Deployable-Structures.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |
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
