---
document_id: QATL-ATLAS-1000-STA-120-129-02-121-001-ELECTRIC-PROPULSION-CONTROLLED-DEFINITION
title: "STA 120-129 · 02.121.001 — Electric Propulsion Controlled Definition"
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
subsection: "121"
subsection_title: "Propulsión Eléctrica"
subsubject: "001"
subsubject_title: "Electric Propulsion Controlled Definition"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-HPC, Q-DATAGOV, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · Section 02 · Subsection 121 · Subsubject 001 — Electric Propulsion Controlled Definition

## 1. Purpose

Establishes the **normative definition and controlled scope** of electric propulsion within the Q+ATLANTIDE STA band, per ECSS-E-ST-35C[^ecssest35].

## 2. Scope

- **Controlled definition** — Electric propulsion systems convert electrical energy into thrust by accelerating a propellant using electrothermal heating, electrostatic fields, or electromagnetic forces, achieving specific impulses typically in the range of 500–10 000 s for Q+ATLANTIDE space platforms.
- **Applicability boundary** — STA `121` covers all electric propulsion subsystems on Q+ATLANTIDE STA-band platforms; excludes chemical propulsion (→ `120`), nuclear propulsion concepts (→ `122`), and advanced/experimental systems (→ `123`).
- **Controlled vocabulary** — *specific impulse (Isp)*, *thrust efficiency (η)*, *beam current*, *discharge voltage*, *Hall parameter*, *propellant utilisation efficiency*, *total impulse*, *power-to-thrust ratio*, *duty cycle*, *plume half-angle*.
- **Safety classification** — propulsion-critical; all EP subsystems shall have documented power-interface assurance, PPU validation evidence, plume interaction analysis, EMC characterisation, and thermal management per ECSS-E-HB-35A[^ecsshb35a].

## 3. Diagram — Electric Propulsion Definition Framework

```mermaid
flowchart TD
    A["ECSS-E-ST-35C · ECSS-E-HB-35A<br/>Regulatory Anchors"]
    A --> B["Electric Propulsion<br/>Controlled Definition (001)"]
    B --> C["Applicability Boundary<br/>(electrothermal · electrostatic · EM)"]
    B --> D["Controlled Vocabulary<br/>(Isp · η · beam · duty-cycle)"]
    B --> E["Safety Classification<br/>(propulsion-critical)"]
    C --> F["002 — EP Families"]
    D --> G["008 — Performance Metrics"]
    E --> H["010 — Testing & Assurance"]
    style B fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `121` — Propulsión Eléctrica |
| Subsubject | `001` — Electric Propulsion Controlled Definition |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `001_Electric-Propulsion-Controlled-Definition.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |

## 5. References & Citations

[^ecssest35]: **ECSS-E-ST-35C — Propulsion General Requirements** — European standard for space propulsion systems.

[^ecsshb35a]: **ECSS-E-HB-35A — Propulsion Handbook** — European handbook for space propulsion systems design and testing.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-35C — Propulsion General Requirements[^ecssest35]
- ECSS-E-HB-35A — Propulsion Handbook[^ecsshb35a]
