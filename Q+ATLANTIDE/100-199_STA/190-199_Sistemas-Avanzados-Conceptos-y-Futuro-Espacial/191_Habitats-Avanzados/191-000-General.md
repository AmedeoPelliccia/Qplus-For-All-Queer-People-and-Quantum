---
document_id: QATL-ATLAS-1000-STA-190-199-09-191-000-GENERAL
title: "STA 190-199 · 191-000 — General"
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
subsubject: "000"
subsubject_title: "General"
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

# STA 190-199 · 191-000 — General

## §1 Purpose

This document is the entry-point for **Advanced Habitats (191)** within the Q+ATLANTIDE Space Technology Architecture (STA), code range 190-199, section 09 — *Sistemas Avanzados, Conceptos y Futuro Espacial*.[^baseline] It establishes the taxonomic scope, controlled vocabulary, and navigational index for all ten controlled subsubject documents (001–010) that together define the complete Q+ATLANTIDE Advanced Habitats discipline baseline.[^archtable]

Advanced Habitats (subsection 191) addresses pressurised human-occupied volumes designed for long-duration space operations beyond ISS baseline capability. The subsection spans habitat taxonomy and controlled definition (001–002), modular architecture principles (003), closed-loop life support (004), radiation protection (005), human factors and crew health (006), structural-thermal-power-resource interfaces (007), deployment-context boundaries (008), standards mapping (009), and lifecycle governance (010).[^qdiv]

> **Safety boundary (inherited):** advanced-habitat critical — all entries in this subsection require explicit habitability requirements, closed-loop ECLSS assumptions, radiation sheltering, crew-health controls, emergency safe-haven logic, modular-interface validation, resource integration and lifecycle traceability before architectural admission.[^gov]

## §2 Scope

The following ten subsubject files constitute the complete 191 — *Hábitats Avanzados* controlled baseline:

| ID | File | One-line description |
|----|------|----------------------|
| 010 | [191-010-Advanced-Habitats-Controlled-Definition.md](./191-010-Advanced-Habitats-Controlled-Definition.md) | Q+ATLANTIDE controlled definition of "Advanced Habitat": pressurised volume, ≥30-day long-duration, taxonomy, exclusions, and TRL threshold for architectural admission. |
| 020 | [191-020-Habitat-Classes-and-Mission-Roles.md](./191-020-Habitat-Classes-and-Mission-Roles.md) | Formal classification of orbital relay, cislunar gateway, lunar surface, Mars surface, transit, and deep-space habitat classes with mission-role definitions, crew complement and duration ranges. |
| 030 | [191-030-Modular-Habitat-Architecture-and-Expansion-Logic.md](./191-030-Modular-Habitat-Architecture-and-Expansion-Logic.md) | Modular architecture principles including pressurised module interfaces (NDS/IBDM), expansion logic rules, structural coupling, pressurisation/leak-check protocols, and mass/volume budget logic. |
| 040 | [191-040-Closed-Loop-ECLSS-and-Regenerative-Life-Support.md](./191-040-Closed-Loop-ECLSS-and-Regenerative-Life-Support.md) | Closed-loop ECLSS architecture: atmospheric control, CO₂ removal, O₂ generation, water recovery, waste management, loop-closure metrics, and resupply minimisation targets. |
| 050 | [191-050-Radiation-Protection-Safe-Haven-and-Shielding-Concepts.md](./191-050-Radiation-Protection-Safe-Haven-and-Shielding-Concepts.md) | Radiation environment per habitat class, shielding mass trades, active/passive concepts, safe-haven requirements (≥30 g/cm² Al-equiv.), SPE shelter triggers, and NASA-STD-3001 dose-constraint compliance. |
| 060 | [191-060-Human-Factors-Crew-Health-and-Long-Duration-Habitability.md](./191-060-Human-Factors-Crew-Health-and-Long-Duration-Habitability.md) | Net habitable volume per crewmember, acoustic/lighting/thermal comfort, exercise equipment, private quarters, medical capability tiers, microgravity countermeasures, and behavioural health provisions. |
| 070 | [191-070-Structure-Thermal-Power-and-Resource-Interfaces.md](./191-070-Structure-Thermal-Power-and-Resource-Interfaces.md) | Structural interface requirements, MMOD protection tiers, thermal control (ATCS/ETCS/radiators), power bus definitions (28 VDC/120 VDC), and ISRU resource integration interfaces. |
| 080 | [191-080-Surface-Orbital-and-Interplanetary-Habitat-Boundaries.md](./191-080-Surface-Orbital-and-Interplanetary-Habitat-Boundaries.md) | Boundary declarations for each deployment context: LEO orbital, cislunar gateway, lunar surface, Mars surface, and interplanetary transit — covering gravity, radiation, comm delay, resupply and egress. |
| 090 | [191-090-Traceability-Evidence-and-Lifecycle-Governance.md](./191-090-Traceability-Evidence-and-Lifecycle-Governance.md) | Function-to-standard mapping table covering NASA-STD-3001, HIDH, ECSS-E-ST-34C, ECSS-Q-ST-70C, ECSS-E-ST-10-03C, ECSS-M-ST-10C, and JSC 63557 across all 191 subsubject functions. |
| 100 | [`191-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./191-090-Traceability-Evidence-and-Lifecycle-Governance.md) | Evidence package requirements for ECLSS, radiation, habitability, structural, power/thermal and ISRU integration; review gates (SRR/MDR/PDR/CDR/HRR/ORR); and full lifecycle from concept to decommissioning. |

## §3 Footprint

| Attribute | Value |
|-----------|-------|
| Architecture | Space Technology Architecture (STA) |
| Master range | 100–199 |
| Code range | 190-199 |
| Section | 09 — Sistemas Avanzados, Conceptos y Futuro Espacial |
| Subsection | 191 — Hábitats Avanzados |
| Subsubject | 000 — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-DATAGOV, Q-HPC, Q-GREENTECH, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | baseline[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/190-199_Sistemas-Avanzados-Conceptos-y-Futuro-Espacial/191_Habitats-Avanzados/` |
| Document | `191-000-General.md` |
| Parent subsection | [README.md](./README.md) |
| Parent architecture | [../../README.md](../../README.md) |
| Parent baseline | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

## §4 References & Citations

[^baseline]: Q+ATLANTIDE controlled baseline (v1.0.0). All documents in this subsection are governed under the Q+ATLANTIDE taxonomy and traceability ecosystem.[^n001]
[^archtable]: §3 Architecture Table (parent) — see [../../README.md](../../README.md) for the STA master architecture table.
[^qdiv]: Q-Division authority — Q-SPACE is the primary division authority for all STA 190-199 advanced habitat documents; Q-HORIZON, Q-DATAGOV, Q-HPC, Q-GREENTECH, Q-STRUCTURES, and Q-INDUSTRY provide supporting governance.
[^gov]: Governance class — baseline. Documents at this class require formal change control via ORB-PMO and ORB-LEG review gates.
[^nastd3001v1]: NASA-STD-3001 Vol.1 — *NASA Space Flight Human-System Standard: Crew Health* (NASA, 2015).
[^nastd3001v2]: NASA-STD-3001 Vol.2 — *NASA Space Flight Human-System Standard: Human Factors, Habitability and Environmental Health* (NASA, 2011).
[^hidh]: NASA/SP-2010-3407 — *Human Integration Design Handbook (HIDH)* (NASA, 2010).
[^ecss34]: ECSS-E-ST-34C — *Space engineering: Environmental control and life support* (ESA, 2008).
[^n001]: Note N-001: Q+ATLANTIDE is a taxonomy and traceability ecosystem, not a mission or programme. All document IDs, baseline references, and governance entries are internal to the Q+ATLANTIDE register.

### Applicable industry standards

- NASA-STD-3001 Vol.1 — NASA Space Flight Human-System Standard: Crew Health (NASA, 2015)[^nastd3001v1]
- NASA-STD-3001 Vol.2 — NASA Space Flight Human-System Standard: Human Factors, Habitability and Environmental Health (NASA, 2011)[^nastd3001v2]
- NASA/SP-2010-3407 — Human Integration Design Handbook (HIDH) (NASA, 2010)[^hidh]
- ECSS-E-ST-34C — Space engineering: Environmental control and life support (ESA, 2008)[^ecss34]
- ECSS-Q-ST-70C — Space product assurance: Materials, mechanical parts and processes (ESA, 2014)
- ECSS-E-ST-10-03C — Space engineering: Testing (ESA, 2012)
