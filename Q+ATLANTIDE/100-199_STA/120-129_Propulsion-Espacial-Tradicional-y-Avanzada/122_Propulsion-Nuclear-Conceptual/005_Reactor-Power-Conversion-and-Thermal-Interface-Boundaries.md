---
document_id: QATL-ATLAS-1000-STA-120-129-02-122-005-REACTOR-POWER-CONVERSION-AND-THERMAL-INTERFACE-BOUNDARIES
title: "STA 120-129 · 02.122.005 — Reactor Power Conversion and Thermal Interface Boundaries"
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
subsubject: "005"
subsubject_title: "Reactor Power Conversion and Thermal Interface Boundaries"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · Section 02 · Subsection 122 · Subsubject 005 — Reactor Power Conversion and Thermal Interface Boundaries

## 1. Purpose

Defines **conceptual reactor power conversion system architectures and thermal interface boundaries** for nuclear propulsion systems.

## 2. Scope

- **Conceptual-only boundary** — All content is conceptual-level; no reactor core design, fuel element specifications, or enrichment level data.
- **Power conversion concepts**:
  - *Thermoelectric (TE)* — direct conversion, η ~5–8%; used in RPS; scalable to reactor systems at reduced efficiency.
  - *Thermionic* — electron emission conversion, η ~5–12%; SNAP-10A heritage.
  - *Brayton cycle* — closed-cycle gas turbine, η ~20–35%; 10–1 000 kW_e class; rotating machinery challenge in space.
  - *Stirling cycle* — regenerative reciprocating, η ~25–35%; ASRG concept; scalable to reactor.
- **Thermal rejection interface** — Waste heat rejection via space radiator; radiator area drives spacecraft configuration; conceptual sizing at ~5–20 m²/kW_e rejected.
- **Interface with thruster** — Power conversion electrical output → PPU (STA `121` `006`) → electric thrusters; thermal rejection system interfaced with STA `112_Proteccion-Termica-y-Radiacion`.

## 3. Diagram — Power Conversion Conceptual Chain

```mermaid
flowchart LR
    A["Reactor Core<br/>(conceptual boundary)"] --> B["Power Conversion<br/>(TE/Brayton/Stirling)"]
    B --> C["Electrical Output<br/>(kW_e to MW_e)"]
    B --> D["Waste Heat<br/>(→ radiator rejection)"]
    C --> E["PPU & EP Thrusters<br/>(→ 121.006 / 004)"]
    D --> F["Space Radiator<br/>(→ 112 TCS interface)"]
    style A fill:#7b0000,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `122` — Propulsión Nuclear Conceptual |
| Subsubject | `005` — Reactor Power Conversion and Thermal Interface Boundaries |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Safety boundary | conceptual-only |
| Document | `005_Reactor-Power-Conversion-and-Thermal-Interface-Boundaries.md` (this file) |

## 5. References & Citations

[^iaeatecdoc1819]: **IAEA-TECDOC-1819 — Space Nuclear Power and Propulsion**.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- IAEA-TECDOC-1819 — Space Nuclear Power and Propulsion[^iaeatecdoc1819]
- NASA-NSS 1676.1 — Nuclear Safety Policy
