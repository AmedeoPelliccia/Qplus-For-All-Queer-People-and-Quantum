---
document_id: QATL-ATLAS-1000-STA-120-129-02-120-001-CHEMICAL-PROPULSION-CONTROLLED-DEFINITION
title: "STA 120-129 · 02.120.001 — Chemical Propulsion Controlled Definition"
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
subsubject: "001"
subsubject_title: "Chemical Propulsion Controlled Definition"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · Section 02 · Subsection 120 · Subsubject 001 — Chemical Propulsion Controlled Definition

## 1. Purpose

Establishes the **normative definition and controlled scope** of chemical propulsion within the Q+ATLANTIDE STA band, per ECSS-E-ST-35C[^ecssest35].

## 2. Scope

- Covers controlled definition for subsection `120`.
- **Controlled definition** — Chemical propulsion systems convert stored chemical energy (combustion or decomposition of propellants) into kinetic energy via controlled thrust generation to achieve orbital manoeuvring, attitude control, and de-orbit for Q+ATLANTIDE space platforms.
- **Applicability boundary** — STA `120` covers all chemical propulsion systems on Q+ATLANTIDE STA-band platforms; excludes electric propulsion (→ `121`), advanced/nuclear propulsion (→ `123`), and aerodynamic surfaces (→ ATLAS band).
- **Controlled vocabulary** — *specific impulse (Isp)*, *thrust*, *propellant mass fraction*, *mixture ratio (O/F)*, *characteristic velocity (c*)*, *thrust coefficient (C_F)*, *propellant combination*, *pressure-fed*, *pump-fed*, *monopropellant*, *bipropellant*.
- **Safety classification** — propulsion-critical; all propulsion elements shall have documented hazard analysis, propellant compatibility, and pressure-system assurance per NASA-STD-8719.15[^nasastd871915].

## 3. Diagram — Chemical Propulsion Definition Framework

```mermaid
flowchart TD
    A["ECSS-E-ST-35C · NASA-STD-8719.15<br/>Regulatory Anchors"]
    A --> B["Chemical Propulsion<br/>Controlled Definition (001)"]
    B --> C["Applicability Boundary<br/>(liquid · solid · hybrid)"]
    B --> D["Controlled Vocabulary<br/>(Isp · thrust · O/F · c*)"]
    B --> E["Safety Classification<br/>(propulsion-critical)"]
    C --> F["002 — Propellant Families"]
    D --> G["009 — Performance Metrics"]
    E --> H["010 — Safety & Assurance"]
    style B fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `120` — Propulsión Química |
| Subsubject | `001` — Chemical Propulsion Controlled Definition |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `001_Chemical-Propulsion-Controlled-Definition.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |

## 5. References & Citations

[^ecssest35]: **ECSS-E-ST-35C — Propulsion General Requirements** — European standard for space propulsion systems.

[^nasastd871915]: **NASA-STD-8719.15 — Safety Standard for Explosives, Propellants and Pyrotechnics**.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-35C — Propulsion General Requirements[^ecssest35]
- NASA-STD-8719.15 — Safety Standard for Explosives, Propellants and Pyrotechnics[^nasastd871915]
