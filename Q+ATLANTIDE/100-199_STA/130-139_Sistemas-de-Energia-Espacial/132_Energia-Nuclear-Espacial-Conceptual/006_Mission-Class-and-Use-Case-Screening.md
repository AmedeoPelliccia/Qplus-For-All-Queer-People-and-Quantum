---
document_id: QATL-ATLAS-1000-STA-130-139-03-132-006-MISSION-CLASS-AND-USE-CASE-SCREENING
title: "STA 130-139 · 03.132.006 — Mission Class and Use-Case Screening"
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
subsubject: "006"
subsubject_title: "Mission Class and Use-Case Screening"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · Section 03 · Subsection 132 · Subsubject 006 — Mission Class and Use-Case Screening

## 1. Purpose

Provides **mission-class screening criteria** for nuclear energy applicability: (1) Deep-space missions (>5 AU) where solar flux <0.04 S₀; (2) Permanently-shadowed lunar/Martian surface operations; (3) High-power NEP propulsion (>100 kW_e). Screening matrix maps power requirement vs. solar availability vs. nuclear TRL. Conceptual-only; no mission commitment.

## 2. Scope

- **Conceptual boundary applies** — this subsubject is designated conceptual-only per subsection README.md. All content is based on published, publicly available sources. No design, manufacture, deployment, fissile-material handling, or reactor operation is within scope.
- All nuclear energy performance claims cite published mission or technology assessment sources.

## 3. Diagram — Conceptual Overview

```mermaid
flowchart TD
    A["Published Sources\n(IAEA · NASA · ESA · peer-reviewed)"] --> B["Mission Class and Use-Case Screening\n(STA-132-006)"]
    B --> C["Conceptual-Only Boundary"]
    C --> D["No deployment · No manufacture\nNo fissile handling · ORB-LEG review required"]
    style C fill:#cc0000,color:#fff
    style D fill:#cc0000,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `132` — Energía Nuclear Espacial Conceptual |
| Subsubject | `006` — Mission Class and Use-Case Screening |
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
