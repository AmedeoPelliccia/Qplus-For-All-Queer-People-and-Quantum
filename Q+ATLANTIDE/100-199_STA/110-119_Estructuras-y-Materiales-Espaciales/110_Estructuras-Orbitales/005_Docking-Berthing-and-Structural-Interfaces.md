---
document_id: QATL-ATLAS-1000-STA-110-119-01-110-005-DOCKING-BERTHING-AND-STRUCTURAL-INTERFACES
title: "STA 110-119 · 01.110.005 — Docking Berthing and Structural Interfaces"
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
subsubject: "005"
subsubject_title: "Docking Berthing and Structural Interfaces"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 110-119 · Section 01 · Subsection 110 · Subsubject 005 — Docking, Berthing and Structural Interfaces

## 1. Purpose

Defines the **docking, berthing and structural interface architecture** for orbital systems — covering hard-docking mechanisms, CBM/IDSS-compatible berthing rings, capture-latch design, and the ICD requirements that govern structural handshake between visiting vehicles and host platforms, per ECSS-E-ST-32C[^ecsse32].

## 2. Scope

- Covers the *Docking, Berthing and Structural Interfaces* subsubject (`005`) of subsection `110`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Docking mechanisms** — active and passive docking mechanisms; IDSS (International Docking System Standard) geometry and load-interface requirements; probe-drogue (legacy) vs. soft-docking (Androgynous Peripheral Attach System — APAS) design options.
  - **Berthing rings** — Common Berthing Mechanism (CBM) interface geometry (1,524 mm frame I.D.), CBM bolted structural connection, port structural ring stiffness requirement.
  - **Capture latches** — structural hook-latch design, preload torque requirements, cryogenic performance (−55°C to +100°C), and redundancy (4 latches minimum per CBM quadrant).
  - **ICD table format** — structural loads at interface (axial, lateral, moment, torsion), alignment tolerances, electrical bonding path, and mate/de-mate cycle life.
  - **Misalignment and compliance** — approach misalignment tolerances (translational ±0.1 m, angular ±10°) and docking mechanism stroke/compliance to absorb residual approach velocity.
  - **Structural handshake verification** — combined loads test at interface, docking loads test campaign, and flight-heritage qualification data.

## 3. Diagram — Docking and Berthing Structural Interface

```mermaid
flowchart LR
    VV["Visiting Vehicle<br/>(docking port)"]
    VV -->|"IDSS / APAS"| DOCK["Hard-Docking Mechanism<br/>(probe/drogue or soft-dock)"]
    VV -->|"CBM"| BERTH["Berthing Ring<br/>(CBM 4 latches/quadrant)"]

    DOCK & BERTH --> RING["Interface Ring<br/>(structural handshake)"]
    RING --> ILOAD["Interface Loads<br/>(Fx·Fy·Fz · Mx·My·Mz — ICD table)"]
    ILOAD --> PRIM["Host Primary Structure<br/>(→ 002)"]

    style RING fill:#1f3a93,color:#fff
    style ILOAD fill:#f39c12,color:#fff
```

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `110` — Estructuras Orbitales |
| Subsubject | `005` — Docking Berthing and Structural Interfaces |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/110_Estructuras-Orbitales/` |
| Document | `005_Docking-Berthing-and-Structural-Interfaces.md` (this file) |
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
