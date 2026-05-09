---
document_id: QATL-ATLAS-1000-STA-110-119-01-112-README
title: "STA 110-119 · 01.112 — Protección Térmica y Radiación (Subsection Index)"
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
subsection: "112"
subsection_title: "Protección Térmica y Radiación"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-GREENTECH, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
linked_nodes:
  - "110_Estructuras-Orbitales"
  - "111_Materiales-Espaciales"
  - "101_Habitabilidad"
  - "102_Soporte-Vital-ECLSS"
  - "103_Seguridad-de-Mision"
safety_boundary: "thermal and radiation protection critical; requires explicit environmental assumptions, shielding verification, degradation evidence, crew/electronics exposure limits, material qualification and lifecycle traceability"
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 110-119 · Section 01 · Subsection 112 — Protección Térmica y Radiación

## 1. Purpose

Subsection-level index for *Protección Térmica y Radiación* (`112`) within STA `110-119` — *Estructuras y Materiales Espaciales*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **thermal and radiation protection critical**: all subsubjects require explicit environmental assumptions, shielding verification, degradation evidence, crew/electronics exposure limits, material qualification, and lifecycle traceability.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `112` *Thermal and Radiation Protection*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `110_Estructuras-Orbitales`, `111_Materiales-Espaciales`, `101_Habitabilidad`, `102_Soporte-Vital-ECLSS`, `103_Seguridad-de-Mision`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`112-000-General.md`](./112-000-General.md) | active |
| 010 | Thermal and Radiation Protection Controlled Definition | [`112-010-Thermal-and-Radiation-Protection-Controlled-Definition.md`](./112-010-Thermal-and-Radiation-Protection-Controlled-Definition.md) | active |
| 020 | Thermal Control Boundaries and Protection Functions | [`112-020-Thermal-Control-Boundaries-and-Protection-Functions.md`](./112-020-Thermal-Control-Boundaries-and-Protection-Functions.md) | active |
| 030 | Passive Thermal Protection Materials and Coatings | [`112-030-Passive-Thermal-Protection-Materials-and-Coatings.md`](./112-030-Passive-Thermal-Protection-Materials-and-Coatings.md) | active |
| 040 | Active Thermal Control Interfaces | [`112-040-Active-Thermal-Control-Interfaces.md`](./112-040-Active-Thermal-Control-Interfaces.md) | active |
| 050 | Radiation Environment and Exposure Regimes | [`112-050-Radiation-Environment-and-Exposure-Regimes.md`](./112-050-Radiation-Environment-and-Exposure-Regimes.md) | active |
| 060 | Radiation Shielding Materials and Architectures | [`112-060-Radiation-Shielding-Materials-and-Architectures.md`](./112-060-Radiation-Shielding-Materials-and-Architectures.md) | active |
| 070 | Electronics Payload and Crew Protection Zones | [`112-070-Electronics-Payload-and-Crew-Protection-Zones.md`](./112-070-Electronics-Payload-and-Crew-Protection-Zones.md) | active |
| 080 | Thermal Cycling Degradation and Lifetime Effects | [`112-080-Thermal-Cycling-Degradation-and-Lifetime-Effects.md`](./112-080-Thermal-Cycling-Degradation-and-Lifetime-Effects.md) | active |
| 090 | Traceability Evidence and Lifecycle Governance | [`112-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./112-090-Traceability-Evidence-and-Lifecycle-Governance.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `112` — Protección Térmica y Radiación |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-GREENTECH, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Safety boundary | thermal and radiation protection critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/112_Proteccion-Termica-y-Radiacion/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE`, `support_q_divisions = [Q-STRUCTURES, Q-GREENTECH, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]`, and `governance_class = baseline` from the parent STA section. Extensions added under `011`–`099` shall preserve those header fields, declare the `safety_boundary`, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
