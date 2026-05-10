---
document_id: QATL-ATLAS-1000-STA-130-139-03-131-080-ECLIPSE-PEAK-LOAD-AND-CONTINGENCY-ENERGY-BUDGETING
title: "STA 130-139 · 131-080 — Eclipse Peak Load and Contingency Energy Budgeting"
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
subsubject: "080"
subsubject_title: "Eclipse Peak Load and Contingency Energy Budgeting"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · 131-080 — Eclipse Peak Load and Contingency Energy Budgeting

## 1. Purpose

Establishes **energy budgeting methodology** for eclipse, peak-load, and contingency intervals for Q+ATLANTIDE STA-band platform batteries.

## 2. Scope

- **Eclipse energy sizing** — E_eclipse = P_load_avg × t_eclipse; battery capacity = E_eclipse / (DOD_limit × η_discharge); DOD_limit: 30% (LEO Li-ion), 80% (GEO Li-ion).
- **Peak-load provision** — transient peak power (actuator start, TM transmit) supplied from battery + array; peak duration constraint (< 5 s for capacitive peak); BMS current limit verified.
- **Contingency reserve** — 10–20% energy reserve above nominal eclipse case for FDIR recovery modes and extended eclipse (stuck SADM, off-pointing).
- **Safe-mode floor** — minimum 72 h safe-mode autonomy from battery alone (for crewed platforms: minimum 24 h from battery alone if arrays are partially occulted).
- **Sizing iteration** — eclipse energy sizing ↔ array sizing ↔ power budget (→ `130_008`) jointly iterated at PDR/CDR.

## 3. Diagram — Energy Budget Sizing Flow

```mermaid
flowchart TD
    A["Eclipse Duration\n(→ 130_008)"] --> B["Average Eclipse\nLoad Profile"]
    B --> C["Eclipse Energy\nRequirement (Wh)"]
    C --> D["Battery Capacity\nSizing (DOD limit)"]
    D --> E["Peak Load Check\n+ Contingency Reserve"]
    E --> F["CDR Battery\nCapacity Freeze"]
    style A fill:#1f3a93,color:#fff
    style F fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `131` — Baterías y Almacenamiento |
| Subsubject | `008` — Eclipse, Peak-Load and Contingency Energy Budgeting |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |

## 5. References & Citations

[^ecssest2010c]: **ECSS-E-ST-20-10C — Batteries**.
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards
- ECSS-E-ST-20-10C — Batteries[^ecssest2010c]
- ECSS-E-ST-20C — Electrical and Electronic
