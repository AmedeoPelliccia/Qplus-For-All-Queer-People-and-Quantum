---
document_id: QATL-ATLAS-1000-STA-190-199-09-191-README
title: "STA 190-199 · 09.191 — Hábitats Avanzados (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "190-199"
section: "09"
section_title: "Sistemas Avanzados, Conceptos y Futuro Espacial"
subsection: "191"
subsection_title: "Hábitats Avanzados"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-DATAGOV, Q-HPC, Q-GREENTECH, Q-STRUCTURES, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
safety_boundary: "advanced-habitat critical; requires explicit habitability requirements, closed-loop ECLSS assumptions, radiation sheltering, crew-health controls, emergency safe-haven logic, modular-interface validation, resource integration and lifecycle traceability"
claim_discipline: "advanced habitat concepts require declared mission context, human-rating assumptions, environmental boundary conditions, technology-readiness screening, verification evidence and independent safety review before architectural admission"
no_aaa_rule: true
---

# STA 190-199 · Section 09 · Subsection 191 — Hábitats Avanzados

## 1. Purpose

Subsection-level index for *Hábitats Avanzados* (`191`) within STA `190-199` — *Sistemas Avanzados, Conceptos y Futuro Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

> **Safety boundary:** advanced-habitat critical — all subsubject entries require explicit habitability requirements, closed-loop ECLSS assumptions, radiation sheltering, crew-health controls, emergency safe-haven logic, modular-interface validation, resource integration and lifecycle traceability.

## 2. Scope

- Reserves the subsubject namespace `00`–`99` of subsection `191` *Advanced Habitats*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Governs the controlled baseline for advanced habitat taxonomy, ECLSS, radiation protection, human factors, structural/thermal/power interfaces, surface/orbital/interplanetary boundaries, standards mapping and lifecycle governance.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`191-000-General.md`](./191-000-General.md) | active |
| 010 | Advanced Habitats Controlled Definition | [`191-010-Advanced-Habitats-Controlled-Definition.md`](./191-010-Advanced-Habitats-Controlled-Definition.md) | active |
| 020 | Habitat Classes and Mission Roles | [`191-020-Habitat-Classes-and-Mission-Roles.md`](./191-020-Habitat-Classes-and-Mission-Roles.md) | active |
| 030 | Modular Habitat Architecture and Expansion Logic | [`191-030-Modular-Habitat-Architecture-and-Expansion-Logic.md`](./191-030-Modular-Habitat-Architecture-and-Expansion-Logic.md) | active |
| 040 | Closed Loop ECLSS and Regenerative Life Support | [`191-040-Closed-Loop-ECLSS-and-Regenerative-Life-Support.md`](./191-040-Closed-Loop-ECLSS-and-Regenerative-Life-Support.md) | active |
| 050 | Radiation Protection Safe Haven and Shielding Concepts | [`191-050-Radiation-Protection-Safe-Haven-and-Shielding-Concepts.md`](./191-050-Radiation-Protection-Safe-Haven-and-Shielding-Concepts.md) | active |
| 060 | Human Factors Crew Health and Long Duration Habitability | [`191-060-Human-Factors-Crew-Health-and-Long-Duration-Habitability.md`](./191-060-Human-Factors-Crew-Health-and-Long-Duration-Habitability.md) | active |
| 070 | Structure Thermal Power and Resource Interfaces | [`191-070-Structure-Thermal-Power-and-Resource-Interfaces.md`](./191-070-Structure-Thermal-Power-and-Resource-Interfaces.md) | active |
| 080 | Surface Orbital and Interplanetary Habitat Boundaries | [`191-080-Surface-Orbital-and-Interplanetary-Habitat-Boundaries.md`](./191-080-Surface-Orbital-and-Interplanetary-Habitat-Boundaries.md) | active |
| 090 | Traceability Evidence and Lifecycle Governance | [`191-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./191-090-Traceability-Evidence-and-Lifecycle-Governance.md) | active |

## 4. Footprint & Governance

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `190-199` |
| Section | `09` — Sistemas Avanzados, Conceptos y Futuro Espacial |
| Subsection | `191` — Hábitats Avanzados |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-DATAGOV, Q-HPC, Q-GREENTECH, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/190-199_Sistemas-Avanzados-Conceptos-y-Futuro-Espacial/191_Habitats-Avanzados/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE` and `governance_class = baseline` from the parent STA section. Extensions added under `00`–`99` shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — Q-SPACE is the primary authority for all advanced habitat standards within Q+ATLANTIDE; Q-HORIZON, Q-DATAGOV, Q-HPC, Q-GREENTECH, Q-STRUCTURES, and Q-INDUSTRY provide supporting governance. See [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline, subject to formal change control under ORB-PMO and ORB-LEG review gates.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

### Applicable industry standards

- NASA-STD-3001 Vol.1 — NASA Space Flight Human-System Standard: Crew Health (NASA, 2015)
- NASA-STD-3001 Vol.2 — NASA Space Flight Human-System Standard: Human Factors, Habitability and Environmental Health (NASA, 2011)
- NASA/SP-2010-3407 — Human Integration Design Handbook (HIDH) (NASA, 2010)
- ECSS-E-ST-34C — Space engineering: Environmental control and life support (ESA, 2008)
- ECSS-Q-ST-70C — Space product assurance: Materials, mechanical parts and processes (ESA, 2014)
- ECSS-E-ST-10-03C — Space engineering: Testing (ESA, 2012)
