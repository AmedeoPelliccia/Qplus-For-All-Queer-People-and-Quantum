---
document_id: QATL-ATLAS-1000-STA-120-129-02-120-040-SOLID-PROPULSION-SYSTEMS
title: "STA 120-129 · 120-040 — Solid Propulsion Systems"
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
subsubject: "040"
subsubject_title: "Solid Propulsion Systems"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · 120-040 — Solid Propulsion Systems

## 1. Purpose

Defines **solid rocket motor (SRM) systems** — grain geometry, propellant formulations, insulation and case design, nozzle configuration, and ignition architecture — and their use in launch upper stages, kick motors, and separation systems.

## 2. Scope

- Grain geometries: cylindrical, star, finocyl, wagon-wheel (burn-rate tailoring); HTPB/AP/Al composite propellant; energetic binders (GAP); burn rate modifiers.
- Case design: filament-wound CFRP / metal-lined CFRP; internal insulation (EPDM/silicone); nozzle (graphite/C-C throat, submerged vs. exit nozzle).
- Ignition: electro-explosive devices (EEDs), safe/arm mechanisms; thermal pyro initiators.
- Performance drivers: volumetric loading fraction; burn rate pressure exponent (n); action time; total impulse; delivered Isp (250–280 s).

## 3. Diagram — Solid Rocket Motor Architecture

```mermaid
flowchart TD
    IGN["Igniter / EED<br/>(pyro initiator)"]
    IGN --> GRAIN["Propellant Grain<br/>(HTPB/AP/Al · star grain)"]
    GRAIN --> CHAMBER["Motor Case<br/>(CFRP / steel)"]
    CHAMBER --> NOZZLE["Nozzle<br/>(graphite throat · CFRP exit)"]
    NOZZLE --> THRUST["Thrust → Total Impulse"]
    INSUL["Internal Insulation<br/>(EPDM)"] -.-> CHAMBER
    style GRAIN fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `120` — Propulsión Química |
| Subsubject | `004` — Solid Propulsion Systems |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `120-040-Solid-Propulsion-Systems.md` (this file) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-35C — Propulsion General Requirements
- NASA-STD-8719.15 — Safety Standard for Explosives, Propellants and Pyrotechnics
