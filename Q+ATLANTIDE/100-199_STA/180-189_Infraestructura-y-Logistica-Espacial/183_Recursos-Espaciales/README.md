---
document_id: QATL-ATLAS-1000-STA-180-189-08-183-README
title: "STA 180-189 · 08.183 — Recursos Espaciales (Subsection Index)"
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
subsection: "183"
subsection_title: "Recursos Espaciales"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "103_Seguridad-de-Mision"
  - "111_Materiales-Espaciales"
  - "120_Propulsion-Quimica"
  - "121_Propulsion-Electrica"
  - "123_Propulsion-Avanzada"
  - "130_Energia-Solar"
  - "131_Baterias-y-Almacenamiento"
  - "133_Distribucion-Electrica"
  - "170_Servicing-Orbital"
  - "180_Bases-Orbitales"
  - "181_Logistica-Cis-Lunar"
  - "182_Transporte-Espacial"
safety_boundary: "space-resource critical; requires explicit ISRU assumptions, extraction and processing boundaries, resource-chain traceability, planetary-protection controls, sustainability criteria, legal admissibility and lifecycle evidence"
legal_boundary: "space resources require explicit treaty, jurisdictional, planetary-protection and mission-authorization review before operational admission"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 180-189 · Section 08 · Subsection 183 — Recursos Espaciales

## 1. Purpose

Subsection-level index for *Recursos Espaciales* (`183`) within STA `180-189` — *Infraestructura y Logística Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Covers the subsubject namespace `00`–`10` (11 active) of subsection `183` *Space Resources*; `11`–`99` reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- This subsection is designated **space-resource critical** with an additional **legal boundary**; all subsubjects require explicit ISRU assumptions, extraction and processing boundaries, resource-chain traceability, planetary-protection controls, sustainability criteria, legal admissibility review and lifecycle evidence.

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 00 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 01 | Space Resources Controlled Definition | [`001_Space-Resources-Controlled-Definition.md`](./001_Space-Resources-Controlled-Definition.md) | active |
| 02 | Resource Classes and Mission Roles | [`002_Resource-Classes-and-Mission-Roles.md`](./002_Resource-Classes-and-Mission-Roles.md) | active |
| 03 | In-Situ Resource Utilization (ISRU) | [`003_In-Situ-Resource-Utilization-ISRU.md`](./003_In-Situ-Resource-Utilization-ISRU.md) | active |
| 04 | Water Ice, Volatiles and Consumables | [`004_Water-Ice-Volatiles-and-Consumables.md`](./004_Water-Ice-Volatiles-and-Consumables.md) | active |
| 05 | Regolith, Metals and Construction Feedstocks | [`005_Regolith-Metals-and-Construction-Feedstocks.md`](./005_Regolith-Metals-and-Construction-Feedstocks.md) | active |
| 06 | Energy Resources and Surface Power Interfaces | [`006_Energy-Resources-and-Surface-Power-Interfaces.md`](./006_Energy-Resources-and-Surface-Power-Interfaces.md) | active |
| 07 | Extraction, Processing, Storage and Transfer Boundaries | [`007_Extraction-Processing-Storage-and-Transfer-Boundaries.md`](./007_Extraction-Processing-Storage-and-Transfer-Boundaries.md) | active |
| 08 | Sustainability, Planetary Protection and Legal Constraints | [`008_Sustainability-Planetary-Protection-and-Legal-Constraints.md`](./008_Sustainability-Planetary-Protection-and-Legal-Constraints.md) | active |
| 09 | ECSS / NASA / CCSDS / UNOOSA and Artemis Accords Mapping | [`009_ECSS-NASA-CCSDS-UNOOSA-and-Artemis-Accords-Mapping.md`](./009_ECSS-NASA-CCSDS-UNOOSA-and-Artemis-Accords-Mapping.md) | active |
| 10 | Traceability, Evidence and Lifecycle Governance | [`010_Traceability-Evidence-and-Lifecycle-Governance.md`](./010_Traceability-Evidence-and-Lifecycle-Governance.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `180-189` |
| Section | `08` — Infraestructura y Logística Espacial |
| Subsection | `183` — Recursos Espaciales |
| Subsubject namespace | `00`–`10` (11 active); `11`–`99` reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/180-189_Infraestructura-y-Logistica-Espacial/183_Recursos-Espaciales/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE` and `governance_class = baseline` from the parent STA section. This subsection is designated **space-resource critical** with an additional **legal boundary** (space resources require explicit treaty, jurisdictional, planetary-protection and mission-authorization review before operational admission). All subsubjects require explicit ISRU assumptions, extraction and processing boundaries, resource-chain traceability, planetary-protection controls, sustainability criteria, legal admissibility review and lifecycle evidence. The `no_aaa_rule` applies: the identifier "AAA" must not be used for any safety-critical element. Extensions added under `11`–`99` shall preserve those header fields, carry both `safety_boundary` and `legal_boundary` declarations, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `180-189` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
