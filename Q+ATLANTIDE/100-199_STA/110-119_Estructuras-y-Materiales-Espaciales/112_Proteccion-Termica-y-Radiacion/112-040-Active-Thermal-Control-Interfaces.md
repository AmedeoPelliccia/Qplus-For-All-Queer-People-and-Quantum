---
document_id: QATL-ATLAS-1000-STA-110-119-01-112-040-ACTIVE-THERMAL-CONTROL-INTERFACES
title: "STA 110-119 · 112-040 — Active Thermal Control Interfaces"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "110-119"
section: "01"
section_title: "Estructuras y Materiales Espaciales"
subsection: "112"
subsection_title: "Protección Térmica y Radiación"
subsubject: "040"
subsubject_title: "Active Thermal Control Interfaces"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-GREENTECH, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 110-119 · 112-040 — Active Thermal Control Interfaces

## 1. Purpose

Defines the **active thermal control interfaces** — heaters, thermostats, heat pipes, two-phase loops, deployable radiators, and fluid loop systems — and their integration constraints with the spacecraft power, structural, and ECLSS subsystems.

## 2. Scope

- Covers active TCS hardware and interfaces within subsection `112`.
- Concepts in scope: survival heaters (line/patch/cartridge); proportional heater controllers; variable-conductance heat pipes (VCHP); constant-conductance heat pipes (CCHP); capillary pumped loops (CPL); mechanically pumped fluid loops (MPFL); deployable radiator panels; interface with ECLSS thermal loops (→ `102`); interface with structure mounting (→ `110`).

## 3. Diagram — Active TCS Architecture

```mermaid
flowchart LR
    PWR["Power System<br/>(heater power budget)"]
    PWR --> HTR["Survival Heaters<br/>(line / patch / cartridge)"]
    HTR --> CTRL["Thermostat / PID Controller"]
    CTRL --> UNIT["Unit Temperature<br/>(operational range maintained)"]
    HP["Heat Pipes<br/>(VCHP / CCHP)"]
    LOOP["Fluid Loop<br/>(CPL / MPFL)"]
    RAD["Deployable Radiator"]
    HP --> RAD
    LOOP --> RAD
    UNIT --> HP
    UNIT --> LOOP
    style CTRL fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `112` — Protección Térmica y Radiación |
| Subsubject | `004` — Active Thermal Control Interfaces |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `112-040-Active-Thermal-Control-Interfaces.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-31C — Thermal Control
- ECSS-E-HB-31-01 Part 1 — Thermal Design Handbook
