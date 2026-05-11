---
document_id: QATL-ATLAS-1000-STA-120-129-02-122-020-NUCLEAR-THERMAL-PROPULSION-CONCEPTS
title: "STA 120-129 · 122-020 — Nuclear Thermal Propulsion Concepts"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "120-129"
section: "02"
subsection: "122"
subsubject: "020"
subsubject_title: "Nuclear Thermal Propulsion Concepts"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · 122-020 — Nuclear Thermal Propulsion Concepts

## 1. Purpose

Surveys **nuclear thermal propulsion (NTP) concepts** at the conceptual level for Q+ATLANTIDE STA-band awareness and mission planning purposes.

## 2. Scope

- **Conceptual-only boundary** — All content is conceptual-level. No reactor design data, fissile material specifications, or operational deployment parameters are included.
- **Solid-core NTP** — Fission reactor heats hydrogen propellant through solid fuel elements (graphite-composite, CERMET); Isp ~800–900 s; historical: NERVA/ROVER programme.
- **Liquid-core NTP** — Fuel in liquid phase allows higher core temperatures; theoretical Isp ~1 200–2 000 s; concept only, TRL 2.
- **Gas-core NTP** — Open/closed-cycle concepts; theoretical Isp > 5 000 s; concept only, TRL 1.
- **Key conceptual parameters** — Thrust-to-weight ratio (NTP: ~5–10× better than chemical for deep space), warm-up/cool-down time, radiation dose accumulation, re-start envelope.
- **Mission relevance** — Conceptual screening for crewed Mars missions, outer planet fast transit; not applicable below TRL 4 threshold without separate programme authority.

## 3. Diagram — NTP Concept Taxonomy

```mermaid
flowchart TD
    A["Nuclear Thermal Propulsion<br/>Concept Survey (002)"]
    A --> B["Solid-Core NTP<br/>(NERVA heritage · Isp ~900s · TRL 3-5)"]
    A --> C["Liquid-Core NTP<br/>(Isp ~1200-2000s · TRL 2)"]
    A --> D["Gas-Core NTP<br/>(Isp >5000s · TRL 1)"]
    B --> E["Mission Screening: Mars crewed transit"]
    style A fill:#7b0000,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `122` — Propulsión Nuclear Conceptual |
| Subsubject | `002` — Nuclear Thermal Propulsion Concepts |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Safety boundary | conceptual-only |
| Document | `122-020-Nuclear-Thermal-Propulsion-Concepts.md` (this file) |

## 5. References & Citations

[^nasatm103642]: **NASA-TM-103642 — Electric Propulsion Development**.

[^iaeatecdoc1819]: **IAEA-TECDOC-1819 — Space Nuclear Power and Propulsion**.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- IAEA-TECDOC-1819 — Space Nuclear Power and Propulsion[^iaeatecdoc1819]
- NASA-NSS 1676.1 — Nuclear Safety Policy
