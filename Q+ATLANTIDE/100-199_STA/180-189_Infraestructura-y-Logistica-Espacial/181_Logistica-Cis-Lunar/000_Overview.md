---
document_id: QATL-ATLAS-1000-STA-180-189-08-181-000-OVERVIEW
title: "STA 180-189 · 08.181.000 — Overview"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "180-189"
section: "08"
section_title: "Infraestructura y Logística Espacial"
subsection: "181"
subsection_title: "Logística Cis-Lunar"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
safety_boundary: "cis-lunar logistics critical; requires explicit transfer-architecture control, depot-node governance, cargo and consumables traceability, rendezvous schedule assurance, contingency logistics, traffic coordination and lifecycle evidence"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 180-189 · Section 08 · Subsection 181 — Logística Cis-Lunar

## 1. Purpose

Overview entry-point for the *Logística Cis-Lunar* subsection within the `180-189` code range. Introduces the STA 180-189.181 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline][^n001]. Establishes the cis-lunar logistics framework — controlled definitions, domain and mission roles, Earth-to-lunar-orbit transfer architecture, cargo staging and depot nodes, propellant/consumables supply chains, surface/orbit/gateway interfaces, traffic coordination and rendezvous, supply-chain resilience, standards mapping, and lifecycle traceability — governing all cis-lunar logistics design activities within the Q+ATLANTIDE crewed-space programme.

This subsection is designated **cis-lunar logistics critical**. All subsubjects (`00`–`10`) collectively define the engineering and governance boundary for logistics operations within cis-lunar space, from low-Earth orbit staging through trans-lunar injection, gateway interfaces, and lunar surface delivery. Each subsubject carries explicit transfer-architecture control, depot-node governance, cargo and consumables traceability, rendezvous schedule assurance, contingency logistics, traffic coordination and lifecycle evidence requirements.

## 2. Scope

- **Controlled definitions**: cis-lunar space, logistics chain, transfer orbit, depot node, staging orbit, consumable manifest — see [`001_Cis-Lunar-Logistics-Controlled-Definition.md`](./001_Cis-Lunar-Logistics-Controlled-Definition.md)
- **Domain coverage**: LEO assembly orbit → TLI staging → NRHO/LLO Gateway → descent/ascent interface → lunar surface — see [`002_Cis-Lunar-Logistics-Domain-and-Mission-Roles.md`](./002_Cis-Lunar-Logistics-Domain-and-Mission-Roles.md)
- **Transfer architecture**: Hohmann/bi-elliptic, low-energy lunar transfer (LELT), free-return trajectories, delta-V trade space — see [`003_Earth-Orbit-Lunar-Orbit-Transfer-Architecture.md`](./003_Earth-Orbit-Lunar-Orbit-Transfer-Architecture.md)
- **Cargo classes**: crew provisions, propellant, orbital replacement units (ORUs), scientific payloads, surface assets — see [`004_Cargo-Transport-Staging-and-Depot-Nodes.md`](./004_Cargo-Transport-Staging-and-Depot-Nodes.md)
- **Depot node types**: LEO staging depot, NRHO gateway hub, lunar-orbit fuel depot — see [`004_Cargo-Transport-Staging-and-Depot-Nodes.md`](./004_Cargo-Transport-Staging-and-Depot-Nodes.md)
- **Propellant logistics**: cryogenic management (LH₂/LOX, LCH₄/LOX), boil-off control, xenon/krypton for EP, propellant transfer protocols — see [`005_Propellant-Water-Power-and-Consumables-Logistics.md`](./005_Propellant-Water-Power-and-Consumables-Logistics.md)
- **Consumables**: O₂, N₂, potable water, food, medical supplies — supply-rate modelling, days-of-supply (DOS) margins — see [`005_Propellant-Water-Power-and-Consumables-Logistics.md`](./005_Propellant-Water-Power-and-Consumables-Logistics.md)
- **Interface nodes**: ISS/Lunar Gateway (STA-180 [`180_Bases-Orbitales`](../180_Bases-Orbitales/)), transport vehicles (STA-182 [`182_Transporte-Espacial`](../182_Transporte-Espacial/)), surface resources (STA-183 [`183_Recursos-Espaciales`](../183_Recursos-Espaciales/)) — see [`006_Lunar-Surface-Orbit-and-Gateway-Interfaces.md`](./006_Lunar-Surface-Orbit-and-Gateway-Interfaces.md)
- **Traffic coordination**: launch windows, phasing orbits, rendezvous scheduling, conjunction assessment, CARA authority — see [`007_Traffic-Coordination-Rendezvous-and-Schedule-Control.md`](./007_Traffic-Coordination-Rendezvous-and-Schedule-Control.md)
- **Supply chain resilience**: minimum DOS reserves (30/60/90-day), emergency resupply fast-transit trajectories, failure mode effects — see [`008_Supply-Chain-Resilience-and-Contingency-Operations.md`](./008_Supply-Chain-Resilience-and-Contingency-Operations.md)
- **Standards**: Artemis Accords, ECSS-E-ST-60C (GNC), CCSDS 910.11-B-1 (proximity ops), NASA SP-2016-6105, ECSS-E-ST-35C — see [`009_ECSS-NASA-CCSDS-Cis-Lunar-Standards-Mapping.md`](./009_ECSS-NASA-CCSDS-Cis-Lunar-Standards-Mapping.md)
- **Lifecycle traceability**: requirements traceability, evidence packages, phase gate criteria (SRR→LRR→MOR), BCR/CCB change authority — see [`010_Traceability-Evidence-and-Lifecycle-Governance.md`](./010_Traceability-Evidence-and-Lifecycle-Governance.md)

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `180-189` |
| Section | `08` — Infraestructura y Logística Espacial |
| Subsection | `181` — Logística Cis-Lunar |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-GREENTECH, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/180-189_Infraestructura-y-Logistica-Espacial/181_Logistica-Cis-Lunar/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `180-189` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

### Applicable Industry Standards

| Standard | Issuing Body | Scope | Applicability to STA-181 |
|---|---|---|---|
| ECSS-E-ST-60C | ESA/ECSS | GNC — Guidance Navigation and Control | Transfer orbit design and rendezvous |
| CCSDS 910.11-B-1 | CCSDS | Rendezvous and Proximity Operations | Gateway/depot proximity |
| Artemis Accords (2020) | NASA et al. | Cis-lunar operations framework | Operational framework |
| NASA SP-2016-6105 Rev2 | NASA | Systems Engineering Handbook | Logistics architecture design |
| ECSS-E-ST-35C | ESA/ECSS | Space engineering — Propulsion | Propellant management |
