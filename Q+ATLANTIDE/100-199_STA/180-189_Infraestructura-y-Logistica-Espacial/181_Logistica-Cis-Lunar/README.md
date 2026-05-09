---
document_id: QATL-ATLAS-1000-STA-180-189-08-181-README
title: "STA 180-189 · 08.181 — Logística Cis-Lunar (Subsection Index)"
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
subsection: "181"
subsection_title: "Logística Cis-Lunar"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-GREENTECH, Q-INDUSTRY]
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
  - "153_Comunicacion-Intersatelite"
  - "170_Servicing-Orbital"
  - "180_Bases-Orbitales"
  - "182_Transporte-Espacial"
  - "183_Recursos-Espaciales"
safety_boundary: "cis-lunar logistics critical; requires explicit transfer-architecture control, depot-node governance, cargo and consumables traceability, rendezvous schedule assurance, contingency logistics, traffic coordination and lifecycle evidence"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 180-189 · Section 08 · Subsection 181 — Logística Cis-Lunar

## 1. Purpose

Subsection-level index for *Logística Cis-Lunar* (`181`) within STA `180-189` — *Infraestructura y Logística Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Covers the subsubject namespace `00`–`10` (11 active) of subsection `181` *Cis-Lunar Logistics*; `11`–`99` reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- This subsection is designated **cis-lunar logistics critical**; all subsubjects require explicit transfer-architecture control, depot-node governance, cargo and consumables traceability, rendezvous schedule assurance, contingency logistics, traffic coordination and lifecycle evidence.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`181-000-General.md`](./181-000-General.md) | active |
| 010 | Cis Lunar Logistics Controlled Definition | [`181-010-Cis-Lunar-Logistics-Controlled-Definition.md`](./181-010-Cis-Lunar-Logistics-Controlled-Definition.md) | active |
| 020 | Cis Lunar Logistics Domain and Mission Roles | [`181-020-Cis-Lunar-Logistics-Domain-and-Mission-Roles.md`](./181-020-Cis-Lunar-Logistics-Domain-and-Mission-Roles.md) | active |
| 030 | Earth Orbit Lunar Orbit Transfer Architecture | [`181-030-Earth-Orbit-Lunar-Orbit-Transfer-Architecture.md`](./181-030-Earth-Orbit-Lunar-Orbit-Transfer-Architecture.md) | active |
| 040 | Cargo Transport Staging and Depot Nodes | [`181-040-Cargo-Transport-Staging-and-Depot-Nodes.md`](./181-040-Cargo-Transport-Staging-and-Depot-Nodes.md) | active |
| 050 | Propellant Water Power and Consumables Logistics | [`181-050-Propellant-Water-Power-and-Consumables-Logistics.md`](./181-050-Propellant-Water-Power-and-Consumables-Logistics.md) | active |
| 060 | Lunar Surface Orbit and Gateway Interfaces | [`181-060-Lunar-Surface-Orbit-and-Gateway-Interfaces.md`](./181-060-Lunar-Surface-Orbit-and-Gateway-Interfaces.md) | active |
| 070 | Traffic Coordination Rendezvous and Schedule Control | [`181-070-Traffic-Coordination-Rendezvous-and-Schedule-Control.md`](./181-070-Traffic-Coordination-Rendezvous-and-Schedule-Control.md) | active |
| 080 | Supply Chain Resilience and Contingency Operations | [`181-080-Supply-Chain-Resilience-and-Contingency-Operations.md`](./181-080-Supply-Chain-Resilience-and-Contingency-Operations.md) | active |
| 090 | Traceability Evidence and Lifecycle Governance | [`181-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./181-090-Traceability-Evidence-and-Lifecycle-Governance.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `180-189` |
| Section | `08` — Infraestructura y Logística Espacial |
| Subsection | `181` — Logística Cis-Lunar |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-GREENTECH, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/180-189_Infraestructura-y-Logistica-Espacial/181_Logistica-Cis-Lunar/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE` and `governance_class = baseline` from the parent STA section. This subsection is designated **cis-lunar logistics critical**; all subsubjects require explicit transfer-architecture control, depot-node governance, cargo and consumables traceability, rendezvous schedule assurance, contingency logistics, traffic coordination and lifecycle evidence. The `no_aaa_rule` applies: the identifier "AAA" must not be used for any safety-critical element. Extensions added under `11`–`99` shall preserve those header fields, carry the `safety_boundary` declaration, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `180-189` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
