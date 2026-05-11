---
document_id: QATL-ATLAS-1000-STA-130-139-03-130-070-DEGRADATION-RADIATION-AND-THERMAL-CYCLING-EFFECTS
title: "STA 130-139 · 130-070 — Degradation Radiation and Thermal Cycling Effects"
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
subsubject: "070"
subsubject_title: "Degradation Radiation and Thermal Cycling Effects"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · 130-070 — Degradation Radiation and Thermal Cycling Effects

## 1. Purpose

Establishes the **degradation model requirements** for solar arrays on Q+ATLANTIDE STA-band platforms, covering radiation-induced, thermal cycling, micrometeorite, and contamination effects.

## 2. Scope

- **Radiation degradation** — proton and electron fluence equivalence (1 MeV electrons); displacement damage dose (DDD); cell Pmax degradation at EOL; worst-case shielding assumptions.
- **Thermal cycling** — BOL/EOL temperature range (−180 °C to +120 °C typical); solder joint fatigue; interconnect flex fatigue; number of thermal cycles over mission life.
- **Mean degradation factor (MDF)** — combined radiation + contamination + micrometeorite erosion factor applied to BOL Pmax in power budget.
- **Contamination effects** — outgassing deposits on coverglass (→ `111_Materiales-Espaciales`); UV darkening; periodic power output monitoring.
- **Atomic oxygen (AO)** — relevant for LEO < 700 km; surface erosion of kapton flex circuits and adhesives; AO-resistant coatings required.

## 3. Diagram — Degradation Source Hierarchy

```mermaid
flowchart TD
    A["BOL Solar Array Power"] --> B["Radiation Degradation\n(proton/electron DDD)"]
    A --> C["Thermal Cycling\n(solder/interconnect fatigue)"]
    A --> D["Contamination\n(outgassing/AO erosion)"]
    B --> E["EOL MDF × BOL Pmax\n→ Power Budget (→ 008)"]
    C --> E
    D --> E
    style A fill:#1f3a93,color:#fff
    style E fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `130` — Energía Solar |
| Subsubject | `007` — Degradation, Radiation and Thermal Cycling Effects |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |

## 5. References & Citations

[^nasahdbk4002b]: **NASA-HDBK-4002B — Mitigating In-Space Charging Effects**.
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards
- ECSS-E-ST-20-08C — Photovoltaic Assemblies and Components
- NASA-HDBK-4002B — Mitigating In-Space Charging Effects[^nasahdbk4002b]
