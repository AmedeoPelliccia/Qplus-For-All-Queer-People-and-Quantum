---
document_id: QATL-ATLAS-1000-STA-110-119-01-110-010-ORBITAL-STRUCTURES-CONTROLLED-DEFINITION
title: "STA 110-119 · 110-010 — Orbital Structures Controlled Definition"
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
subsubject: "010"
subsubject_title: "Orbital Structures Controlled Definition"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 110-119 · 110-010 — Orbital Structures Controlled Definition

## 1. Purpose

Establishes the **normative definition and controlled scope** of orbital structures within the Q+ATLANTIDE STA band, defining applicability limits, key controlled terms, and the regulatory reference hierarchy per ECSS-E-ST-32C[^ecsse32].

## 2. Scope

- Covers the *Orbital Structures Controlled Definition* subsubject (`001`) of subsection `110`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Controlled definition** — Orbital Structures as the aggregate of structural elements (primary, secondary, mechanisms) that maintain spacecraft geometry, transmit loads, and protect payloads throughout all mission phases (launch, ascent, orbit, re-entry, landing) for structures operating in the space environment.
  - **Applicability boundary** — STA `110` covers structures for all Q+ATLANTIDE STA-band missions: LEO stations, cis-lunar vehicles, lunar surface systems, and interplanetary transit craft; excludes propulsion structures (→ `130`) and landing gear (→ `150`).
  - **Controlled vocabulary** — *primary structure*, *secondary structure*, *interface control document (ICD)*, *design limit load (DLL)*, *design ultimate load (DUL)*, *margin of safety (MoS)*, *factors of safety (FoS)*, *design verification*.
  - **Safety classification** — structural-mission critical; all structural elements shall have defined load paths, factors of safety per ECSS-E-ST-32-10C[^ecsse3210]/NASA-STD-5001B[^nasastd5001], and structural verification evidence.
  - **Relationship to other subsections** — `111` (materials), `112` (thermal protection), `100` (system architecture); structural interfaces declared in `005`.

## 3. Diagram — Orbital Structures Controlled Definition Framework

```mermaid
flowchart TD
    A["ECSS-E-ST-32C · NASA-STD-5001B<br/>Regulatory Anchors"]
    A --> B["Orbital Structures Controlled Definition<br/>(001 — this document)"]
    B --> C["Applicability Boundary<br/>(LEO · cis-lunar · lunar · interplanetary)"]
    B --> D["Controlled Vocabulary<br/>(DLL · DUL · MoS · FoS · ICD)"]
    B --> E["Safety Classification<br/>(structural-mission critical)"]
    C --> F["002 — Primary/Secondary Elements"]
    D --> G["004 — Load Paths"]
    E --> H["010 — Traceability & Evidence"]
    style B fill:#1f3a93,color:#fff
```

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `110` — Estructuras Orbitales |
| Subsubject | `001` — Orbital Structures Controlled Definition |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/110_Estructuras-Orbitales/` |
| Document | `110-010-Orbital-Structures-Controlled-Definition.md` (this file) |
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
