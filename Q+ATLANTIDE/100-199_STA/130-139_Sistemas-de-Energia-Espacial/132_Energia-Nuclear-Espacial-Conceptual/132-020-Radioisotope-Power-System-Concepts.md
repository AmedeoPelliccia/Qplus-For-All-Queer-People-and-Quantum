---
document_id: QATL-ATLAS-1000-STA-130-139-03-132-020-RADIOISOTOPE-POWER-SYSTEM-CONCEPTS
title: "STA 130-139 · 132-020 — Radioisotope Power System Concepts"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "130-139"
section: "03"
subsection: "132"
subsubject: "020"
subsubject_title: "Radioisotope Power System Concepts"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · 132-020 — Radioisotope Power System Concepts

## 1. Purpose

Surveys **published radioisotope power system (RPS) concepts** applicable to Q+ATLANTIDE STA-band mission-class screening. RTG (SNAP-19, GPHS-RTG, MMRTG) power levels range from 5–290 W_e using Pu-238 heat sources. All data cited from publicly available NASA/DOE sources only. No new RPS design is within scope of this conceptual document.

## 2. Scope

- **Conceptual boundary applies** — this subsubject is designated conceptual-only per subsection README.md. All content is based on published, publicly available sources. No design, manufacture, deployment, fissile-material handling, or reactor operation is within scope.
- All nuclear energy performance claims cite published mission or technology assessment sources.

## 3. Diagram — Conceptual Overview

```mermaid
flowchart TD
    A["Published Sources\n(IAEA · NASA · ESA · peer-reviewed)"] --> B["Radioisotope Power System Concepts\n(STA-132-002)"]
    B --> C["Conceptual-Only Boundary"]
    C --> D["No deployment · No manufacture\nNo fissile handling · ORB-LEG review required"]
    style C fill:#cc0000,color:#fff
    style D fill:#cc0000,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `132` — Energía Nuclear Espacial Conceptual |
| Subsubject | `002` — Radioisotope Power System Concepts |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Safety boundary | **conceptual-only** |
| Governance class | `baseline`[^gov] |

## 5. References & Citations

[^iaeass6]: **IAEA Safety Series No. 6** — Principles Relevant to the Use of Nuclear Power Sources in Outer Space.
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards
- IAEA Safety Series No. 6[^iaeass6]
- Outer Space Treaty (1967) — Article IV
