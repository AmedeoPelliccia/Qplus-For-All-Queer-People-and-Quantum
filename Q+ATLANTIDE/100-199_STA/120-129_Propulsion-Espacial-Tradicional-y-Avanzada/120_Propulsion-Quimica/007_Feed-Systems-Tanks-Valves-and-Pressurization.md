---
document_id: QATL-ATLAS-1000-STA-120-129-02-120-007-FEED-SYSTEMS-TANKS-VALVES-AND-PRESSURIZATION
title: "STA 120-129 · 02.120.007 — Feed Systems, Tanks, Valves and Pressurization"
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
subsubject: "007"
subsubject_title: "Feed Systems, Tanks, Valves and Pressurization"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · Section 02 · Subsection 120 · Subsubject 007 — Feed Systems, Tanks, Valves and Pressurization

## 1. Purpose

Defines the **propellant feed system** — propellant tanks, pressurant bottles, fill/drain valves, filter assemblies, latch valves, pyro valves, and pressure-regulation components — and their structural and materials interfaces (→ `110`, `111`).

## 2. Scope

- Tank design: spherical/cylindrical metallic (Ti-6Al-4V, 6061-T6 Al) or COPV (carbon-overwrapped pressure vessel); propellant management devices (PMDs): screen/vane, surface-tension); tank MEOP; proof factor 1.5×; burst factor 2.0×.
- Pressurisation: blow-down (simple, Δ P_c with burnout) vs. regulated (bang-bang or PRV); pressurant: He, GN₂.
- Valves: isolation/latch valve (normally-closed); fill/drain valve; filter (10–25 μm); check valve; pressure-relief valve (PRV); pyro valve (one-shot actuator).
- Propellant compatibility: material selection per propellant (PTFE seals for NTO/MON; Ti-6Al-4V for MMH/NTO; 316SS for H₂O₂).

## 3. Diagram — Feed System Schematic

```mermaid
flowchart LR
    PRES["He Pressurant<br/>(regulated or blow-down)"]
    PRES --> PRV["Pressure Relief Valve"]
    PRES --> TANK_F["Fuel Tank (Ti/Al/COPV)"]
    PRES --> TANK_O["Oxidiser Tank"]
    TANK_F --> FILT_F["Filter"]
    TANK_O --> FILT_O["Filter"]
    FILT_F --> LV_F["Latch Valve"]
    FILT_O --> LV_O["Latch Valve"]
    LV_F --> ENGINE["Engine / Thruster (006)"]
    LV_O --> ENGINE
    style PRES fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `120` — Propulsión Química |
| Subsubject | `007` — Feed Systems, Tanks, Valves and Pressurization |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `007_Feed-Systems-Tanks-Valves-and-Pressurization.md` (this file) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-35C — Propulsion General Requirements
- NASA-STD-5012 — Structural Test Requirements for Liquid Propulsion Systems
- AIAA S-080 — Space Systems Metallic Pressure Vessels, Pressurised Structures and Pressure Components
