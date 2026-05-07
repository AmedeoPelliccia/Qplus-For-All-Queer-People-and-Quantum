---
document_id: QATL-ATLAS-1000-STA-130-139-03-131-007-DEGRADATION-CYCLING-AND-LIFETIME-MODELLING
title: "STA 130-139 · 03.131.007 — Degradation, Cycling and Lifetime Modelling"
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
subsection: "131"
subsubject: "007"
subsubject_title: "Degradation, Cycling and Lifetime Modelling"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · Section 03 · Subsection 131 · Subsubject 007 — Degradation, Cycling and Lifetime Modelling

## 1. Purpose

Establishes **battery degradation modelling requirements** for Q+ATLANTIDE STA-band platforms, covering capacity fade, impedance growth, and EOL capacity margins.

## 2. Scope

- **Capacity fade model** — empirical Ah-throughput model; capacity retention C(n) = C₀ × (1 − α·n^β); parameters derived from qualification test data; EOL capacity ≥ 80% BOL.
- **Impedance growth** — internal resistance Ri increases with cycling; higher Ri reduces available energy and increases thermal dissipation; modelled for worst-case EOL discharge scenario.
- **Calendar ageing** — storage at elevated temperature accelerates capacity fade even without cycling; Arrhenius-based model for storage intervals.
- **DOD effect** — deeper DOD accelerates capacity fade; Rainflow cycle counting methodology for variable DOD profiles.
- **Margin requirement** — EOL power budget must include capacity fade margin; sizing margin ≥ 20% over mission life.

## 3. Diagram — Degradation Model

```mermaid
flowchart LR
    A["BOL Capacity C₀"] --> B["Cycle Count n\n+ DOD Profile"]
    B --> C["Capacity Fade\nC(n) = C₀·(1−α·nᵝ)"]
    A --> D["Calendar Ageing\n(Arrhenius model)"]
    C --> E["EOL Capacity\n(≥ 80% C₀)"]
    D --> E
    E --> F["Power Budget\nEOL Margin ≥ 20%"]
    style A fill:#1f3a93,color:#fff
    style F fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `131` — Baterías y Almacenamiento |
| Subsubject | `007` — Degradation, Cycling and Lifetime Modelling |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |

## 5. References & Citations

[^ecssest2010c]: **ECSS-E-ST-20-10C — Batteries**.
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards
- ECSS-E-ST-20-10C — Batteries[^ecssest2010c]
