---
document_id: QATL-ATLAS-1000-STA-110-119-01-112-020-THERMAL-CONTROL-BOUNDARIES-AND-PROTECTION-FUNCTIONS
title: "STA 110-119 · 112-020 — Thermal Control Boundaries and Protection Functions"
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
subsubject: "020"
subsubject_title: "Thermal Control Boundaries and Protection Functions"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-GREENTECH, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 110-119 · 112-020 — Thermal Control Boundaries and Protection Functions

## 1. Purpose

Defines the **thermal control boundaries** and the protective functions that maintain all spacecraft units within their allowable temperature limits across hot-case and cold-case design extremes.

## 2. Scope

- Covers the *Thermal Control Boundaries and Protection Functions* subsubject (`002`) of subsection `112`.
- Concepts in scope: thermal balance analysis; worst-case hot/cold mission phases; unit-level temperature limits (survival, operational); thermal interfaces and conductance paths; thermal protection function allocation (passive vs. active); margins per ECSS-E-ST-31C[^ecssest31].

## 3. Diagram — Thermal Control Boundaries

```mermaid
flowchart LR
    ENV["Space Environment<br/>(solar / albedo / OLR / eclipse)"]
    ENV --> HOT["Hot Case<br/>(max solar flux · max albedo)"]
    ENV --> COLD["Cold Case<br/>(eclipse · minimum power)"]
    HOT --> TLIM["Temperature Limits<br/>(operational · survival)"]
    COLD --> TLIM
    TLIM --> PASSIVE["Passive TPS<br/>(MLI · coatings · OSR)"]
    TLIM --> ACTIVE["Active Control<br/>(heaters · heat pipes · radiators)"]
    PASSIVE --> MARGIN["Thermal Margin ≥ 5 K (hot)<br/>≥ 10 K (cold)"]
    ACTIVE --> MARGIN
    style TLIM fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `112` — Protección Térmica y Radiación |
| Subsubject | `002` — Thermal Control Boundaries and Protection Functions |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `112-020-Thermal-Control-Boundaries-and-Protection-Functions.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |

## 5. References & Citations

[^ecssest31]: **ECSS-E-ST-31C — Thermal Control** — European standard for spacecraft thermal control design, analysis, and verification.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management.

### Applicable industry standards

- ECSS-E-ST-31C — Thermal Control[^ecssest31]
- ECSS-E-ST-10-04C — Space Environment
- NASA-SP-8105 — Hinge Moments of Aerodynamic Surfaces (thermal interface reference)
