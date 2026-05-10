---
document_id: QATL-ATLAS-1000-STA-120-129-02-120-030-LIQUID-PROPULSION-SYSTEMS
title: "STA 120-129 · 120-030 — Liquid Propulsion Systems"
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
section_title: "Propulsión Espacial Tradicional y Avanzada"
subsection: "120"
subsection_title: "Propulsión Química"
subsubject: "030"
subsubject_title: "Liquid Propulsion Systems"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · 120-030 — Liquid Propulsion Systems

## 1. Purpose

Defines the **liquid propulsion system architectures** — pressure-fed and pump-fed — for main propulsion engines and reaction-control system (RCS) thrusters on Q+ATLANTIDE STA-band platforms.

## 2. Scope

- Covers liquid propulsion system topologies within subsection `120`.
- Architectures: pressure-fed blow-down (simple, variable thrust); pressure-fed regulated (constant chamber pressure); turbopump-fed (gas generator, staged combustion, expander cycle); electric pump-fed (EP-fed) emerging architectures.
- Components: propellant tanks (→ `007`); pressurant (He/N₂); latch valves; pyro valves; main injectors; main chamber; nozzle (→ `006`); RCS thruster clusters (200 mN – 400 N range).

## 3. Diagram — Liquid Propulsion System Topology

```mermaid
flowchart LR
    PRES["Pressurant Bottle<br/>(He / N₂)"]
    PRES --> TANK_F["Fuel Tank<br/>(MMH · LH₂ · RP-1)"]
    PRES --> TANK_O["Oxidiser Tank<br/>(NTO · LOX · MON)"]
    TANK_F --> MIX["Main Engine Injector"]
    TANK_O --> MIX
    MIX --> COMB["Combustion Chamber (006)"]
    COMB --> NOZ["Nozzle → Thrust"]
    TANK_F --> RCS["RCS Thrusters"]
    TANK_O --> RCS
    style COMB fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `120` — Propulsión Química |
| Subsubject | `003` — Liquid Propulsion Systems |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `120-030-Liquid-Propulsion-Systems.md` (this file) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-35C — Propulsion General Requirements
- NASA-STD-5012 — Structural Test Requirements for Liquid Propulsion Systems
