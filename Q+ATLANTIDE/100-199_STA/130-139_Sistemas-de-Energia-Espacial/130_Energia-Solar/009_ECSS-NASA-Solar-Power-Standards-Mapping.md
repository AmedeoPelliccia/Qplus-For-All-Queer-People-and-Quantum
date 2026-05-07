---
document_id: QATL-ATLAS-1000-STA-130-139-03-130-009-ECSS-NASA-SOLAR-POWER-STANDARDS-MAPPING
title: "STA 130-139 · 03.130.009 — ECSS-NASA Solar Power Standards Mapping"
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
subsection: "130"
subsubject: "009"
subsubject_title: "ECSS-NASA Solar Power Standards Mapping"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · Section 03 · Subsection 130 · Subsubject 009 — ECSS-NASA Solar Power Standards Mapping

## 1. Purpose

Maps applicable **ECSS and NASA solar power standards** to Q+ATLANTIDE STA-band subsection `130` design, qualification, and verification activities.

## 2. Scope

| Standard | Scope | Applicability |
|---|---|---|
| ECSS-E-ST-20C | Electrical and Electronic — EPS general requirements | Design, IVV |
| ECSS-E-ST-20-08C | Photovoltaic assemblies and components | Cell/array qualification |
| ECSS-E-ST-20-06C | Spacecraft charging — design and verification | Array surface charging |
| NASA-HDBK-4002B | Mitigating in-space charging effects | Charging control |
| NASA-RP-1345 | Handbook for high-voltage EPS design | HV array design |
| MIL-STD-461G | EMC requirements (government reference) | Array EMC |

## 3. Diagram — Standards Traceability

```mermaid
flowchart LR
    A["Solar Array\nDesign & Test"]
    A --> B["ECSS-E-ST-20C\nEPS General"]
    A --> C["ECSS-E-ST-20-08C\nPV Qualification"]
    A --> D["ECSS-E-ST-20-06C\nCharging Control"]
    A --> E["NASA-HDBK-4002B\nIn-Space Charging"]
    style A fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `130` — Energía Solar |
| Subsubject | `009` — ECSS-NASA Solar Power Standards Mapping |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |

## 5. References & Citations

[^ecssest20]: **ECSS-E-ST-20C** — Electrical and Electronic.
[^ecssest2008c]: **ECSS-E-ST-20-08C** — Photovoltaic Assemblies and Components.
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards
- ECSS-E-ST-20C[^ecssest20]
- ECSS-E-ST-20-08C[^ecssest2008c]
- NASA-HDBK-4002B
