---
document_id: QATL-ATLAS-1000-STA-180-189-08-182-README
title: "STA 180-189 · 08.182 — Transporte Espacial (Subsection Index)"
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
subsection: "182"
subsection_title: "Transporte Espacial"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "103_Seguridad-de-Mision"
  - "120_Propulsion-Quimica"
  - "121_Propulsion-Electrica"
  - "123_Propulsion-Avanzada"
  - "130_Energia-Solar"
  - "131_Baterias-y-Almacenamiento"
  - "133_Distribucion-Electrica"
  - "140_GNC-Guiado-Navegacion-y-Control"
  - "143_Control-de-Mision"
  - "150_SATCOM"
  - "152_Redes-Espaciales"
  - "170_Servicing-Orbital"
  - "180_Bases-Orbitales"
  - "181_Logistica-Cis-Lunar"
  - "183_Recursos-Espaciales"
safety_boundary: "space-transport critical; requires explicit trajectory assurance, propulsion/power/thermal constraints, docking and transfer-interface validation, cargo/crew boundary control, rendezvous governance, traffic coordination and lifecycle traceability"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 180-189 · Section 08 · Subsection 182 — Transporte Espacial

## 1. Purpose

Subsection-level index for *Transporte Espacial* (`182`) within STA `180-189` — *Infraestructura y Logística Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Covers the subsubject namespace `00`–`10` (11 active) of subsection `182` *Space Transport*; `11`–`99` reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- This subsection is designated **space-transport critical**; all subsubjects require explicit trajectory assurance, propulsion/power/thermal constraints, docking and transfer-interface validation, cargo/crew boundary control, rendezvous governance, traffic coordination and lifecycle traceability.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`182-000-General.md`](./182-000-General.md) | active |
| 010 | Space Transport Controlled Definition | [`182-010-Space-Transport-Controlled-Definition.md`](./182-010-Space-Transport-Controlled-Definition.md) | active |
| 020 | Space Transport Classes and Mission Roles | [`182-020-Space-Transport-Classes-and-Mission-Roles.md`](./182-020-Space-Transport-Classes-and-Mission-Roles.md) | active |
| 030 | Launch to Orbit Transport Interfaces | [`182-030-Launch-to-Orbit-Transport-Interfaces.md`](./182-030-Launch-to-Orbit-Transport-Interfaces.md) | active |
| 040 | Orbital Transfer and In Space Transport | [`182-040-Orbital-Transfer-and-In-Space-Transport.md`](./182-040-Orbital-Transfer-and-In-Space-Transport.md) | active |
| 050 | Cargo Crew and Service Transport Boundaries | [`182-050-Cargo-Crew-and-Service-Transport-Boundaries.md`](./182-050-Cargo-Crew-and-Service-Transport-Boundaries.md) | active |
| 060 | Docking Berthing and Transfer Interfaces | [`182-060-Docking-Berthing-and-Transfer-Interfaces.md`](./182-060-Docking-Berthing-and-Transfer-Interfaces.md) | active |
| 070 | Propulsion Power and Thermal Transport Constraints | [`182-070-Propulsion-Power-and-Thermal-Transport-Constraints.md`](./182-070-Propulsion-Power-and-Thermal-Transport-Constraints.md) | active |
| 080 | Trajectory Operations Rendezvous and Traffic Control | [`182-080-Trajectory-Operations-Rendezvous-and-Traffic-Control.md`](./182-080-Trajectory-Operations-Rendezvous-and-Traffic-Control.md) | active |
| 090 | Traceability Evidence and Lifecycle Governance | [`182-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./182-090-Traceability-Evidence-and-Lifecycle-Governance.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `180-189` |
| Section | `08` — Infraestructura y Logística Espacial |
| Subsection | `182` — Transporte Espacial |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/180-189_Infraestructura-y-Logistica-Espacial/182_Transporte-Espacial/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE` and `governance_class = baseline` from the parent STA section. This subsection is designated **space-transport critical**; all subsubjects require explicit trajectory assurance, propulsion/power/thermal constraints, docking and transfer-interface validation, cargo/crew boundary control, rendezvous governance, traffic coordination and lifecycle traceability. The `no_aaa_rule` applies: the identifier "AAA" must not be used for any safety-critical element. Extensions added under `11`–`99` shall preserve those header fields, carry the `safety_boundary` declaration, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `180-189` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
