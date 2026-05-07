---
document_id: QATL-ATLAS-1000-STA-110-119-01-110-009-ECSS-NASA-STRUCTURAL-STANDARDS-MAPPING
title: "STA 110-119 · 01.110.009 — ECSS NASA Structural Standards Mapping"
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
subsubject: "009"
subsubject_title: "ECSS NASA Structural Standards Mapping"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 110-119 · Section 01 · Subsection 110 · Subsubject 009 — ECSS / NASA Structural Standards Mapping

## 1. Purpose

Provides the **structural-specific standards cross-reference** mapping ECSS, NASA, and ISO standards to the STA `110` orbital-structures subsubjects, ensuring each structural module cites the correct normative hierarchy.

## 2. Scope

- Covers the *ECSS / NASA Structural Standards Mapping* subsubject (`009`) of subsection `110`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **ECSS structural mapping** — ECSS-E-ST-32C (structural general requirements), ECSS-E-ST-32-10C (factors of safety), ECSS-E-ST-32-01C (fracture control), ECSS-Q-ST-70C (materials/processes).
  - **NASA structural mapping** — NASA-STD-5001B (structural FoS), NASA-STD-5002 (loads, structural strength, and determination of margin of safety), NASA-HDBK-7005 (dynamic environment criteria).
  - **ISO mapping** — ISO 15630-1 (testing of metallic materials for reinforcement), used in conjunction with qualification testing.
  - **Standards traceability matrix** — tabular cross-reference of each `110` subsubject to primary and supporting standards.

| Subsubject | Primary Standards | Supporting Standards |
|---|---|---|
| 001 Definition | ECSS-E-ST-32C | NASA-STD-5001B |
| 002 Elements | ECSS-E-ST-32C | ECSS-Q-ST-70C |
| 003 Topology | ECSS-E-ST-32C | NASA-STD-5001B |
| 004 Loads | ECSS-E-ST-32-10C | NASA-STD-5001B, NASA-HDBK-7005 |
| 005 Docking/Berthing | ECSS-E-ST-32C | IDS Standard |
| 006 Assembly | ECSS-E-ST-32C | NASA assembly heritage |
| 007 Fatigue/DT | ECSS-E-ST-32C | ECSS-E-ST-32-01C |
| 008 Inspection/SHM | ECSS-E-ST-32C | NASA-STD-5001B |
| 010 Traceability | ECSS-E-ST-32C | ECSS-Q-ST-70C |

## 3. Diagram — Structural Standards Hierarchy

```mermaid
flowchart TB
    STA110["110 Orbital Structure Subsubjects"]
    STA110 --> ECSS32["ECSS-E-ST-32C<br/>(structural general)"]
    STA110 --> ECSS3210["ECSS-E-ST-32-10C<br/>(factors of safety)"]
    STA110 --> NASA5001["NASA-STD-5001B<br/>(structural FoS)"]
    STA110 --> NASAHDBK["NASA-HDBK-7005<br/>(dynamic env.)"]

    ECSS32 --> VER["Compliance Verification<br/>(A · T · I · D)"]
    ECSS3210 --> VER
    NASA5001 --> VER
    VER --> EP["Structural Evidence Package<br/>(lifecycle gate closure)"]

    style STA110 fill:#1f3a93,color:#fff
    style VER fill:#2c82c9,color:#fff
```

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `110` — Estructuras Orbitales |
| Subsubject | `009` — ECSS NASA Structural Standards Mapping |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/110_Estructuras-Orbitales/` |
| Document | `009_ECSS-NASA-Structural-Standards-Mapping.md` (this file) |
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
