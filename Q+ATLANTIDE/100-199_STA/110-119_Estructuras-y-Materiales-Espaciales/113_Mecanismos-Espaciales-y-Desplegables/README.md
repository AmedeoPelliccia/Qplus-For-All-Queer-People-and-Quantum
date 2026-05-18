---
document_id: QATL-ATLAS-1000-STA-110-119-01-113-README
title: "STA 110-119 · 01.113 — Mecanismos Espaciales y Desplegables (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
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
linked_nodes:
  - "110_Estructuras-Orbitales"
  - "111_Materiales-Espaciales"
  - "112_Proteccion-Termica-y-Radiacion"
  - "114_Cargas-Mecanicas-Vibracion-y-Choque"
safety_boundary: "space mechanisms and deployable systems critical; requires explicit mechanism function definition, kinematic verification, deployment evidence, lubrication and vacuum compatibility assessment, life testing and lifecycle traceability"
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 110-119 · Section 01 · Subsection 113 — Mecanismos Espaciales y Desplegables

## 1. Purpose

Subsection-level index for *Mecanismos Espaciales y Desplegables* (`113`) within STA `110-119` — *Estructuras y Materiales Espaciales*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **space mechanisms and deployable systems critical**: all subsubjects require explicit mechanism function definition, kinematic verification, deployment evidence, lubrication and vacuum compatibility assessment, life testing, and lifecycle traceability.

## 2. Scope

- Populates the subsubject namespace `000`–`090` of subsection `113` *Space Mechanisms and Deployable Systems*; subsubjects `091`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `110_Estructuras-Orbitales`, `111_Materiales-Espaciales`, `112_Proteccion-Termica-y-Radiacion`, `114_Cargas-Mecanicas-Vibracion-y-Choque`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`113-000-General.md`](./113-000-General.md) | active |
| 010 | Space Mechanisms Controlled Definition | [`113-010-Space-Mechanisms-Controlled-Definition.md`](./113-010-Space-Mechanisms-Controlled-Definition.md) | active |
| 020 | Mechanism Families and Functional Classes | [`113-020-Mechanism-Families-and-Functional-Classes.md`](./113-020-Mechanism-Families-and-Functional-Classes.md) | active |
| 030 | Hinges Latches Locks and Release Devices | [`113-030-Hinges-Latches-Locks-and-Release-Devices.md`](./113-030-Hinges-Latches-Locks-and-Release-Devices.md) | active |
| 040 | Deployable Solar Array Antenna Boom and Mast Systems | [`113-040-Deployable-Solar-Array-Antenna-Boom-and-Mast-Systems.md`](./113-040-Deployable-Solar-Array-Antenna-Boom-and-Mast-Systems.md) | active |
| 050 | Docking Hatch Seal and Access Mechanisms | [`113-050-Docking-Hatch-Seal-and-Access-Mechanisms.md`](./113-050-Docking-Hatch-Seal-and-Access-Mechanisms.md) | active |
| 060 | Actuators Drives Motors and Transmission Elements | [`113-060-Actuators-Drives-Motors-and-Transmission-Elements.md`](./113-060-Actuators-Drives-Motors-and-Transmission-Elements.md) | active |
| 070 | Lubrication Wear Cold Welding and Vacuum Compatibility | [`113-070-Lubrication-Wear-Cold-Welding-and-Vacuum-Compatibility.md`](./113-070-Lubrication-Wear-Cold-Welding-and-Vacuum-Compatibility.md) | active |
| 080 | Qualification Life Testing and Deployment Evidence | [`113-080-Qualification-Life-Testing-and-Deployment-Evidence.md`](./113-080-Qualification-Life-Testing-and-Deployment-Evidence.md) | active |
| 090 | Traceability Evidence and Lifecycle Governance | [`113-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./113-090-Traceability-Evidence-and-Lifecycle-Governance.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `113` — Mecanismos Espaciales y Desplegables |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Safety boundary | space mechanisms and deployable systems critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/113_Mecanismos-Espaciales-y-Desplegables/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE`, `support_q_divisions = [Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]`, and `governance_class = baseline` from the parent STA section. Extensions added under `091`–`099` shall preserve those header fields, declare the `safety_boundary`, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
