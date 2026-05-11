---
document_id: QATL-ATLAS-1000-STA-120-129-02-120-060-COMBUSTION-CHAMBERS-NOZZLES-AND-THRUST-GENERATION
title: "STA 120-129 · 120-060 — Combustion Chambers Nozzles and Thrust Generation"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "120-129"
section: "02"
section_title: "Propulsión Espacial Tradicional y Avanzada"
subsection: "120"
subsection_title: "Propulsión Química"
subsubject: "060"
subsubject_title: "Combustion Chambers Nozzles and Thrust Generation"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · 120-060 — Combustion Chambers Nozzles and Thrust Generation

## 1. Purpose

Defines the **combustion chamber and nozzle design** — chamber pressure, injector configuration, characteristic velocity (c*), thrust coefficient (C_F), nozzle expansion ratio, and thermal/structural margins — and the interface with TPS materials (→ `112`).

## 2. Scope

- Chamber design: cylindrical combustion chamber with converging-diverging (De Laval) nozzle; characteristic length (L*); chamber pressure P_c (1–300 bar); injector types (showerhead, swirl, impinging doublet/triplet, pintle).
- Nozzle: conical, bell (80% bell), truncated ideal contour (TIC); expansion ratio ε = A_e/A_t; nozzle materials (C-C, Nb, Iridium-lined Rhenium, film-cooled steel); radiation-cooled vs. film-cooled vs. regeneratively cooled.
- Performance: specific impulse Isp = c* · C_F / g₀; thrust F = C_F · P_c · A_t; delivered vs. theoretical Isp efficiency.

## 3. Diagram — Chamber and Nozzle Thermodynamics

```mermaid
flowchart LR
    INJ["Injector<br/>(propellant mixing)"]
    INJ --> COMB["Combustion Zone<br/>(P_c · T_c · c*)"]
    COMB --> THROAT["Nozzle Throat<br/>(M=1 · A_t)"]
    THROAT --> EXP["Nozzle Exit<br/>(ε = A_e/A_t · M_e)"]
    EXP --> THRUST["Thrust F = C_F · P_c · A_t"]
    style COMB fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `120` — Propulsión Química |
| Subsubject | `006` — Combustion Chambers, Nozzles and Thrust Generation |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `120-060-Combustion-Chambers-Nozzles-and-Thrust-Generation.md` (this file) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-35C — Propulsion General Requirements
- NASA-SP-8120 — Selection of Materials for Rocket Exhaust Plume Components
