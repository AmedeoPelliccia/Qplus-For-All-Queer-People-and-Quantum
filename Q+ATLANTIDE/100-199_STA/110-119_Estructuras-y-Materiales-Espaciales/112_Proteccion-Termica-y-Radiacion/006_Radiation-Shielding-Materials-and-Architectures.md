---
document_id: QATL-ATLAS-1000-STA-110-119-01-112-006-RADIATION-SHIELDING-MATERIALS-AND-ARCHITECTURES
title: "STA 110-119 · 01.112.006 — Radiation Shielding Materials and Architectures"
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
subsubject: "006"
subsubject_title: "Radiation Shielding Materials and Architectures"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-GREENTECH, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 110-119 · Section 01 · Subsection 112 · Subsubject 006 — Radiation Shielding Materials and Architectures

## 1. Purpose

Defines the **radiation shielding materials and architectural configurations** used to attenuate ionising radiation to within the dose budget, covering aluminium shielding, hydrogenous shielding materials, spot shielding, and structural integration approaches.

## 2. Scope

- Covers radiation shielding design within subsection `112`.
- Concepts in scope: aluminium equivalent shielding depth (mm Al-eq); polyethylene and water-filled panels for high-energy proton shielding; spot shielding for radiation-sensitive components; tantalum spot shields for SEE-sensitive devices; tiered shielding architecture (platform wall → equipment enclosure → spot shield); mass penalty vs. dose reduction trade; Monte Carlo transport codes (GEANT4, MULASSIS, SHIELDOSE-2).

## 3. Diagram — Shielding Architecture

```mermaid
flowchart LR
    ENV["Radiation Environment<br/>(005 — TID · fluence · LET)"]
    ENV --> WALL["Platform Wall Shielding<br/>(Al structural panels)"]
    WALL --> BOX["Equipment Box<br/>(additional Al wall)"]
    BOX --> SPOT["Spot Shield<br/>(Ta foil / Pb-Bi · SEE-critical parts)"]
    SPOT --> COMP["Component TID<br/>(within allowable)"]
    HYDRO["Hydrogenous Shield<br/>(polyethylene / water)"]
    WALL --> HYDRO
    HYDRO --> COMP
    style SPOT fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `112` — Protección Térmica y Radiación |
| Subsubject | `006` — Radiation Shielding Materials and Architectures |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `006_Radiation-Shielding-Materials-and-Architectures.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-10-04C — Space Environment
- NASA-HDBK-4002A — Mitigating In-Space Charging Effects
- ESA SHIELDOSE-2 — Dose-depth curve tool
