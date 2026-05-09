---
document_id: QATL-ATLAS-1000-STA-120-129-02-120-050-HYBRID-PROPULSION-SYSTEMS
title: "STA 120-129 · 120-050 — Hybrid Propulsion Systems"
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
subsubject: "050"
subsubject_title: "Hybrid Propulsion Systems"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · 120-050 — Hybrid Propulsion Systems

## 1. Purpose

Defines **hybrid propulsion system architectures** combining a liquid/gaseous oxidiser with a solid fuel, covering throttleability, safety advantages, and mission applicability.

## 2. Scope

- Configurations: liquid oxidiser + solid fuel (N₂O/HTPB, LOX/HTPB, H₂O₂/HTPB, GOX/HTPB); gaseous oxidiser variants.
- Throttleability: oxidiser mass flow control (throttle valve) enables variable thrust (10–100%); restart capability distinguishes hybrid from solid.
- Safety: no energetic pre-mix (oxidiser separated from fuel at rest); lower handling hazard vs. bipropellant hypergolic; compatible with non-toxic oxidiser options (N₂O, H₂O₂).
- Limitations: regression rate uniformity; O/F shift with burn time; lower TRL vs. liquid or solid in orbital applications.

## 3. Diagram — Hybrid System Architecture

```mermaid
flowchart LR
    OX["Oxidiser Tank<br/>(N₂O / LOX)"]
    OX --> VALVE["Throttle Valve"]
    VALVE --> INJ["Injector"]
    INJ --> FUEL["Solid Fuel Grain<br/>(HTPB)"]
    FUEL --> COMB["Combustion Zone"]
    COMB --> NOZ["Nozzle → Thrust"]
    style FUEL fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `120` — Propulsión Química |
| Subsubject | `005` — Hybrid Propulsion Systems |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `120-050-Hybrid-Propulsion-Systems.md` (this file) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-35C — Propulsion General Requirements
