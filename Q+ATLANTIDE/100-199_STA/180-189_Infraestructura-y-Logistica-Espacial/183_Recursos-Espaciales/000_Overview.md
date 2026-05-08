---
document_id: QATL-ATLAS-1000-STA-180-189-08-183-000-OVERVIEW
title: "STA 180-189 · 08.183.000 — Overview"
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
subsection: "183"
subsection_title: "Recursos Espaciales"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 180-189 · Section 08 · Subsection 183 — Recursos Espaciales

## 1. Purpose

Overview entry-point for the *Recursos Espaciales* subsection within the `180-189` code range (Section `08` — *Infraestructura y Logística Espacial*) of the **STA** architecture band (*Space Technology Architecture*, master range `100–199`).

This subsubject (`000 Overview`) introduces the STA 180-189.183 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the space-resources framework — controlled definition, resource classes and mission roles, in-situ resource utilisation (ISRU), water-ice and volatiles, regolith and construction feedstocks, energy resources and surface-power interfaces, extraction/processing/storage/transfer boundaries, sustainability and planetary-protection constraints, applicable standards mapping, and lifecycle traceability — governing all resource-extraction and utilisation activities within the Q+ATLANTIDE deep-space programme. This subsection is designated **space-resource critical** and carries an explicit **legal boundary** requiring treaty and jurisdictional review.

## 2. Scope

- Covers the *Recursos Espaciales* slice of the parent code range `180-189`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`001`–`010`) extend this Overview; the populated set in this baseline is `001`–`010`, indexed in [`README.md`](./README.md).
- Concepts in scope across the subsection:
  - **Space Resources Controlled Definition** (`001`) — normative vocabulary, applicability limits, and regulatory anchors including the Outer Space Treaty[^ost] and Artemis Accords[^artemis].
  - **Resource Classes and Mission Roles** (`002`) — taxonomy of extractable resources (volatiles, regolith, metals, energy) and their mission-enabling roles.
  - **In-Situ Resource Utilisation — ISRU** (`003`) — ISRU system architecture, process chains, and mission integration requirements.
  - **Water, Ice, Volatiles and Consumables** (`004`) — extraction, processing and supply of water, oxygen, hydrogen and other consumables.
  - **Regolith, Metals and Construction Feedstocks** (`005`) — regolith beneficiation, metal extraction, and additive-manufacturing feedstock production.
  - **Energy Resources and Surface-Power Interfaces** (`006`) — solar, nuclear and fuel-cell energy sourcing at the surface and interface to orbital power nodes.
  - **Extraction, Processing, Storage and Transfer Boundaries** (`007`) — system boundaries for extraction through to point-of-use or transfer to orbital logistics.
  - **Sustainability, Planetary Protection and Legal Constraints** (`008`) — COSPAR planetary-protection categories, sustainability criteria, and legal admissibility requirements.
  - **ECSS / NASA / CCSDS / UNOOSA and Artemis Accords Mapping** (`009`) — standards and treaty cross-reference for all `183` subsubjects.
  - **Traceability, Evidence and Lifecycle Governance** (`010`) — resource-chain traceability, evidence package, and change-authority rules.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `180-189` |
| Section | `08` — Infraestructura y Logística Espacial |
| Subsection | `183` — Recursos Espaciales |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/180-189_Infraestructura-y-Logistica-Espacial/183_Recursos-Espaciales/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `180-189` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ost]: **Outer Space Treaty (1967)** — Treaty on Principles Governing the Activities of States in the Exploration and Use of Outer Space, including the Moon and Other Celestial Bodies. Establishes that outer space is not subject to national appropriation; resource extraction status subject to national legislation.

[^artemis]: **Artemis Accords (2020)** — Bilateral agreements establishing norms for responsible civil space exploration, including provisions on space resources extraction and utilisation consistent with the Outer Space Treaty.

### Applicable industry standards

- Outer Space Treaty (1967)[^ost]
- Artemis Accords (2020)[^artemis]
- COSPAR Planetary Protection Policy (2017 rev.) — Committee on Space Research planetary-protection categories I–V
- ECSS-E-ST-10-04C — Space Engineering: Space Environment
- NASA-STD-8719.27 — Planetary Protection Provisions for Robotic Extraterrestrial Missions
- ISECG Global Exploration Roadmap (2018) — International Space Exploration Coordination Group resource-utilisation framework
