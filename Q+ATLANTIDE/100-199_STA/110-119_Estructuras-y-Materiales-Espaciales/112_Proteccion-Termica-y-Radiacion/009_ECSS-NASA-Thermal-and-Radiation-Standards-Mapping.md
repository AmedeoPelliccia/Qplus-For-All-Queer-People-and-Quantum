---
document_id: QATL-ATLAS-1000-STA-110-119-01-112-009-ECSS-NASA-THERMAL-AND-RADIATION-STANDARDS-MAPPING
title: "STA 110-119 · 01.112.009 — ECSS / NASA Thermal and Radiation Standards Mapping"
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
subsubject: "009"
subsubject_title: "ECSS / NASA Thermal and Radiation Standards Mapping"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-GREENTECH, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 110-119 · Section 01 · Subsection 112 · Subsubject 009 — ECSS / NASA Thermal and Radiation Standards Mapping

## 1. Purpose

Provides the **normative standards cross-reference** for all `112` subsubjects, mapping ECSS and NASA standard identifiers to the thermal and radiation protection topics covered by subsection `112`.

## 2. Scope

- Covers thermal and radiation standards mapping for subsection `112`.
- Standards in scope:

| Standard | Scope | Applicable `112` Subsubjects |
|---|---|---|
| ECSS-E-ST-31C | Thermal control design, analysis, verification | 001, 002, 003, 004, 008 |
| ECSS-E-ST-10-04C | Space environment models | 001, 005, 006, 007, 008 |
| ECSS-E-HB-31-01 Part 1 | Thermal design handbook | 002, 003, 004 |
| ECSS-Q-ST-70C | Space materials (TPS coatings, MLI) | 003, 008 |
| ECSS-Q-ST-70-01C | Cleanliness and contamination | 003 |
| NASA-STD-6016A | Materials and processes for spacecraft | 003 |
| NASA-HDBK-4001 | Electrical grounding (radiation shielding context) | 006, 007 |
| NASA-HDBK-4002A | Mitigating in-space charging | 005, 006 |
| NASA-STD-3001 Vol.1 | Crew health (radiation dose limits) | 007 |
| NCRP Report 132 | Radiation protection guidance for LEO crew | 007 |
| NASA-HDBK-7005 | Dynamic environmental criteria (thermal fatigue) | 008 |

## 3. Diagram — Standards Mapping Overview

```mermaid
flowchart TD
    S31["ECSS-E-ST-31C<br/>Thermal Control"]
    S1004["ECSS-E-ST-10-04C<br/>Space Environment"]
    SQ70["ECSS-Q-ST-70C<br/>Materials"]
    N6016["NASA-STD-6016A<br/>Materials & Processes"]
    N3001["NASA-STD-3001<br/>Crew Health"]
    S31 --> SS002["002 · 003 · 004 · 008"]
    S1004 --> SS005["005 · 006 · 007 · 008"]
    SQ70 --> SS003["003 · 008"]
    N6016 --> SS003
    N3001 --> SS007["007"]
    style S31 fill:#1f3a93,color:#fff
    style S1004 fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `112` — Protección Térmica y Radiación |
| Subsubject | `009` — ECSS / NASA Thermal and Radiation Standards Mapping |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `009_ECSS-NASA-Thermal-and-Radiation-Standards-Mapping.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-31C — Thermal Control
- ECSS-E-ST-10-04C — Space Environment
- ECSS-E-HB-31-01 Part 1 — Thermal Design Handbook
- ECSS-Q-ST-70C — Space Product Assurance: Materials
- NASA-STD-6016A — Standard Materials and Processes Requirements for Spacecraft
- NASA-HDBK-4002A — Mitigating In-Space Charging Effects
- NASA-STD-3001 Vol.1 — Crew Health Requirements
- NCRP Report 132 — Radiation Protection Guidance for LEO
