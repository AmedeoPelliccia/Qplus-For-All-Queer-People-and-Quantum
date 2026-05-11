---
document_id: QATL-ATLAS-1000-STA-130-139-03-132-050-POWER-CONVERSION-THERMAL-REJECTION-AND-SHIELDING
title: "STA 130-139 · 132-050 — Power Conversion Thermal Rejection and Shielding"
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
subsubject: "050"
subsubject_title: "Power Conversion Thermal Rejection and Shielding"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · 132-050 — Power Conversion Thermal Rejection and Shielding

## 1. Purpose

Surveys **published power conversion and thermal rejection concepts** for space nuclear systems: thermoelectric (Seebeck effect, η ≈ 5–8%), Stirling (η ≈ 20–30%), Brayton (η ≈ 20–35%). Shadow-shield geometry for crew/electronics protection. All concepts cited from published mission and technology assessment sources.

## 2. Scope

- **Conceptual boundary applies** — this subsubject is designated conceptual-only per subsection README.md. All content is based on published, publicly available sources. No design, manufacture, deployment, fissile-material handling, or reactor operation is within scope.
- All nuclear energy performance claims cite published mission or technology assessment sources.

## 3. Diagram — Conceptual Overview

```mermaid
flowchart TD
    A["Published Sources\n(IAEA · NASA · ESA · peer-reviewed)"] --> B["Power Conversion, Thermal Rejection and Shielding\n(STA-132-005)"]
    B --> C["Conceptual-Only Boundary"]
    C --> D["No deployment · No manufacture\nNo fissile handling · ORB-LEG review required"]
    style C fill:#cc0000,color:#fff
    style D fill:#cc0000,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `132` — Energía Nuclear Espacial Conceptual |
| Subsubject | `005` — Power Conversion, Thermal Rejection and Shielding |
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
