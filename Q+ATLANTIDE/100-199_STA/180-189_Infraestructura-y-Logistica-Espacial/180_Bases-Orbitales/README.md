---
document_id: QATL-ATLAS-1000-STA-180-189-08-180-README
title: "STA 180-189 · 08.180 — Bases Orbitales (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "180-189"
section: "08"
section_title: "Infraestructura y Logística Espacial"
subsection: "180"
subsection_title: "Bases Orbitales"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-STRUCTURES, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "101_Habitabilidad"
  - "102_Soporte-Vital-ECLSS"
  - "103_Seguridad-de-Mision"
  - "110_Estructuras-Orbitales"
  - "112_Proteccion-Termica-y-Radiacion"
  - "130_Energia-Solar"
  - "131_Baterias-y-Almacenamiento"
  - "133_Distribucion-Electrica"
  - "140_GNC-Guiado-Navegacion-y-Control"
  - "143_Control-de-Mision"
  - "170_Servicing-Orbital"
  - "173_Ensamblaje-en-Orbita"
  - "181_Logistica-Cis-Lunar"
  - "182_Transporte-Espacial"
  - "183_Recursos-Espaciales"
safety_boundary: "orbital-infrastructure critical; requires explicit traffic-interface control, docking/berthing validation, power/thermal/ECLSS integration, logistics traceability, emergency survivability, maintenance support and lifecycle governance"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 180-189 · Section 08 · Subsection 180 — Bases Orbitales

## 1. Purpose

Subsection-level index for *Bases Orbitales* (`180`) within STA `180-189` — *Infraestructura y Logística Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Covers the subsubject namespace `00`–`10` (11 active) of subsection `180` *Orbital Bases*; `11`–`99` reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- This subsection is designated **orbital-infrastructure critical**; all subsubjects require explicit traffic-interface control, docking/berthing validation, power/thermal/ECLSS integration, logistics traceability, emergency survivability, maintenance support and lifecycle governance.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`180-000-General.md`](./180-000-General.md) | active |
| 010 | Orbital Bases Controlled Definition | [`180-010-Orbital-Bases-Controlled-Definition.md`](./180-010-Orbital-Bases-Controlled-Definition.md) | active |
| 020 | Orbital Base Classes and Mission Roles | [`180-020-Orbital-Base-Classes-and-Mission-Roles.md`](./180-020-Orbital-Base-Classes-and-Mission-Roles.md) | active |
| 030 | Habitable and Uncrewed Base Architecture | [`180-030-Habitable-and-Uncrewed-Base-Architecture.md`](./180-030-Habitable-and-Uncrewed-Base-Architecture.md) | active |
| 040 | Docking Berthing and Traffic Interfaces | [`180-040-Docking-Berthing-and-Traffic-Interfaces.md`](./180-040-Docking-Berthing-and-Traffic-Interfaces.md) | active |
| 050 | Power Thermal ECLSS and Resource Interfaces | [`180-050-Power-Thermal-ECLSS-and-Resource-Interfaces.md`](./180-050-Power-Thermal-ECLSS-and-Resource-Interfaces.md) | active |
| 060 | Logistics Storage Cargo and Inventory Control | [`180-060-Logistics-Storage-Cargo-and-Inventory-Control.md`](./180-060-Logistics-Storage-Cargo-and-Inventory-Control.md) | active |
| 070 | Maintenance Servicing and Assembly Support | [`180-070-Maintenance-Servicing-and-Assembly-Support.md`](./180-070-Maintenance-Servicing-and-Assembly-Support.md) | active |
| 080 | Safety Zones Emergency Modes and Survivability | [`180-080-Safety-Zones-Emergency-Modes-and-Survivability.md`](./180-080-Safety-Zones-Emergency-Modes-and-Survivability.md) | active |
| 090 | Traceability Evidence and Lifecycle Governance | [`180-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./180-090-Traceability-Evidence-and-Lifecycle-Governance.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `180-189` |
| Section | `08` — Infraestructura y Logística Espacial |
| Subsection | `180` — Bases Orbitales |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-STRUCTURES, Q-GREENTECH, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/180-189_Infraestructura-y-Logistica-Espacial/180_Bases-Orbitales/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE` and `governance_class = baseline` from the parent STA section. This subsection is designated **orbital-infrastructure critical**; all subsubjects require explicit traffic-interface control, docking/berthing validation, power/thermal/ECLSS integration, logistics traceability, emergency survivability, maintenance support and lifecycle governance. The `no_aaa_rule` applies: the identifier "AAA" must not be used for any safety-critical element. Extensions added under `11`–`99` shall preserve those header fields, carry the `safety_boundary` declaration, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `180-189` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
