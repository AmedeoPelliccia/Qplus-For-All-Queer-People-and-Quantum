---
document_id: QATL-ATLAS-1000-STA-110-119-01-113-030-HINGES-LATCHES-LOCKS-AND-RELEASE-DEVICES
title: "STA 110-119 · 113-030 — Hinges Latches Locks and Release Devices"
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
subsubject: "030"
subsubject_title: "Hinges Latches Locks and Release Devices"
---
# STA 110-119 · 113-030 — Hinges Latches Locks and Release Devices

## 1. Purpose

Defines the **design requirements and verification approach** for hinges, latches, locks, and release devices used in Q+ATLANTIDE space mechanisms, covering kinematic design, preload management, and release-device qualification per ECSS-E-ST-33-01C[^ecsse3301].

## 2. Scope

- Covers the *Hinges, Latches, Locks and Release Devices* subsubject (`003`) of subsection `113`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Hinge design** — pin-clevis hinges, living hinges, tape-spring hinges, and bi-stable composite hinge design; stiffness and deployment-torque characterisation.
  - **Latch mechanisms** — over-centre latches, hook latches, roller latches, and redundant latch systems for structural capture at end of deployment.
  - **Lock devices** — pin locks, detent locks, anti-backdriving locks, and position-verification sensors for confirmed-lock status.
  - **Non-explosive release devices (NEA)** — shape-memory alloy (SMA) actuators, wax actuators, paraffin actuators, and electro-mechanical release mechanisms.
  - **Pyrotechnic release devices** — explosive bolts, separation nuts, guillotine cutters, and pin-pullers; shock-level prediction and interface compatibility per `114-040`.
  - **Driving torque margin (DTM)** — DTM ≥ 2.0 requirement for deployment hinges; friction torque budget methodology; margin verification through measurement and analysis.

## 3. Diagram — Hinges Latches Locks and Release Device Hierarchy

```mermaid
flowchart TB
    A["Retention and Release Architecture"]
    A --> B["Hinge Types<br/>(pin-clevis · tape-spring · living · bi-stable)"]
    A --> C["Latch Types<br/>(over-centre · hook · roller · redundant)"]
    A --> D["Lock Devices<br/>(pin · detent · anti-backdriving)"]
    A --> E["Release Devices"]
    E --> E1["NEA<br/>(SMA · wax · paraffin · EM)"]
    E --> E2["Pyrotechnic<br/>(explosive bolt · separation nut · guillotine)"]
    B & C --> DTM["DTM ≥ 2.0 Verification<br/>(torque budget · friction model)"]
    E2 --> SHOCK["Shock Interface<br/>(→ 114-040 Pyroshock)"]
    style A fill:#1f3a93,color:#fff
    style DTM fill:#2c82c9,color:#fff
```

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `113` — Mecanismos Espaciales y Desplegables |
| Subsubject | `030` — Hinges Latches Locks and Release Devices |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/113_Mecanismos-Espaciales-y-Desplegables/` |
| Document | `113-030-Hinges-Latches-Locks-and-Release-Devices.md` (this file) |
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
