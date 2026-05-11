---
document_id: QATL-ATLAS-1000-STA-110-119-01-112-030-PASSIVE-THERMAL-PROTECTION-MATERIALS-AND-COATINGS
title: "STA 110-119 · 112-030 — Passive Thermal Protection Materials and Coatings"
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
subsubject: "030"
subsubject_title: "Passive Thermal Protection Materials and Coatings"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-GREENTECH, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 110-119 · 112-030 — Passive Thermal Protection Materials and Coatings

## 1. Purpose

Defines the **passive thermal protection (TPS) materials and surface coatings** used to control spacecraft temperatures without active power, covering multi-layer insulation (MLI), optical solar reflectors (OSR), thermal control paints, ablative systems, and foam insulation.

## 2. Scope

- Covers passive TPS materials within subsection `112`.
- Concepts in scope: MLI design (number of layers, spacer type, Beta-cloth outer layer, Kapton inner); OSR properties (α/ε ratio); second-surface mirrors; thermal control coatings (black/white paint, gold evaporation); foam insulation; ablative TPS (PICA, Avcoat); on-orbit aging and α degradation.

## 3. Diagram — Passive TPS Material Stack

```mermaid
flowchart TD
    OUTER["Outer Layer<br/>(Beta-cloth · OSR · white paint)"]
    OUTER --> MLI["MLI Blanket<br/>(Kapton · Mylar layers · Dacron net)"]
    MLI --> INNER["Inner Layer<br/>(Kapton aluminised)"]
    INNER --> STRUCT["Structural Surface<br/>(primary/secondary structure)"]
    COAT["Surface Coating<br/>(α / ε selected per orbit)"]
    STRUCT --- COAT
    style MLI fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `112` — Protección Térmica y Radiación |
| Subsubject | `003` — Passive Thermal Protection Materials and Coatings |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `112-030-Passive-Thermal-Protection-Materials-and-Coatings.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-31C — Thermal Control
- ECSS-Q-ST-70C — Space Product Assurance: Materials
- NASA-STD-6016A — Standard Materials and Processes Requirements for Spacecraft
