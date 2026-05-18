---
document_id: QATL-ATLAS-1000-STA-110-119-01-113-000-GENERAL
title: "STA 110-119 · 113-000 — General"
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
subsubject: "000"
subsubject_title: "General"
---
# STA 110-119 · 113-000 — General

## 1. Purpose

Overview entry-point for the *Mecanismos Espaciales y Desplegables* subsection within the `110-119` code range (Section `01` — *Estructuras y Materiales Espaciales*) of the **STA** architecture band (*Space Technology Architecture*, master range `100–199`).

This subsubject (`000 Overview`) introduces the STA 110-119.113 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the space mechanisms and deployable systems framework governing controlled definitions, mechanism family taxonomy, hinges/latches/locks/release devices, deployable solar-array/antenna/boom/mast systems, docking/hatch/seal/access mechanisms, actuators/drives/motors/transmission elements, lubrication/wear/cold-welding/vacuum compatibility, qualification/life testing, and lifecycle governance for Q+ATLANTIDE crewed-space and robotic-mission systems. This subsection is designated **space mechanisms and deployable systems critical**.

## 2. Scope

- Covers the *Mecanismos Espaciales y Desplegables* slice of the parent code range `110-119`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`001`–`010`) extend this Overview; the populated set in this baseline is `001`–`010`, indexed in [`README.md`](./README.md).
- Concepts in scope across the subsection:
  - **Space Mechanisms Controlled Definition** (`001`) — normative definition, scope, and applicability per ECSS-E-ST-33-01C[^ecsse3301].
  - **Mechanism Families and Functional Classes** (`002`) — taxonomy of deployment, retention/release, drive, bearing, and interface mechanism classes.
  - **Hinges, Latches, Locks and Release Devices** (`003`) — hinge design, latch geometry, lock mechanisms, and pyrotechnic/non-explosive release devices.
  - **Deployable Solar Array, Antenna, Boom and Mast Systems** (`004`) — fold/roll/scissor deployment architectures, drive train, hold-down release, and deployment sequence logic.
  - **Docking, Hatch, Seal and Access Mechanisms** (`005`) — soft-capture, hard-dock, CBM/IDSS hatch seal, and EVA/IVA access mechanism design.
  - **Actuators, Drives, Motors and Transmission Elements** (`006`) — stepper/DC/brushless motors, gear trains, lead screws, harmonic drives, and position-feedback architectures.
  - **Lubrication, Wear, Cold Welding and Vacuum Compatibility** (`007`) — dry lubricants, MoS₂/PTFE coatings, cold-weld prevention, outgassing limits, and wear-life budgets.
  - **Qualification, Life Testing and Deployment Evidence** (`008`) — functional/deployment cycling test programme, life test margins, qualification and acceptance evidence package.
  - **ECSS / NASA Mechanisms Standards Mapping** (`009`) — normative standards cross-reference for all `113` subsubjects.
  - **Traceability, Evidence and Lifecycle Governance** (`010`) — mechanisms compliance evidence package and lifecycle change authority.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `113` — Mecanismos Espaciales y Desplegables |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/113_Mecanismos-Espaciales-y-Desplegables/` |
| Document | `113-000-General.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

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
