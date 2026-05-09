---
document_id: QATL-ATLAS-1000-STA-130-139-03-130-060-POWER-CONVERSION-REGULATION-AND-MPPT
title: "STA 130-139 · 130-060 — Power Conversion Regulation and MPPT"
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
subsubject: "060"
subsubject_title: "Power Conversion Regulation and MPPT"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · 130-060 — Power Conversion Regulation and MPPT

## 1. Purpose

Defines **power conversion, bus voltage regulation and maximum power point tracking (MPPT)** interfaces for solar arrays on Q+ATLANTIDE STA-band platforms.

## 2. Scope

- **S3R (Sequential Switching Shunt Regulator)** — shunt regulation; fixed bus voltage; standard for GEO; low EMI; high efficiency.
- **MPPT converters** — perturb-and-observe, incremental conductance, or model-based algorithms; maximises power harvest under partial illumination and temperature variation; preferred for LEO with frequent eclipse transitions.
- **Bus voltage standards** — 28 V regulated (small platforms); 50 V / 100 V unregulated or regulated (medium); 120 V / 160 V (large/ISS-class).
- **Efficiency allocation** — array-to-bus efficiency ≥ 90%; converter thermal dissipation to thermal budget (→ `112_Proteccion-Termica-y-Radiacion`).
- **Interfaces** — array output voltage range → MPPT/shunt input; regulated bus → battery charge controller (→ `131`); distribution harness (→ `133`).

## 3. Diagram — Power Conversion Chain

```mermaid
flowchart LR
    A["Solar Array Output\n(Voc, Isc, Vmpp)"] --> B["MPPT Converter\nor S3R Shunt"]
    B --> C["Regulated Bus\n(28V / 50V / 100V)"]
    C --> D["Battery Charge\n(→ 131)"]
    C --> E["Distribution Bus\n(→ 133)"]
    style A fill:#1f3a93,color:#fff
    style C fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `130` — Energía Solar |
| Subsubject | `006` — Power Conversion, Regulation and MPPT |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |

## 5. References & Citations

[^ecssest20]: **ECSS-E-ST-20C — Electrical and Electronic**.
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards
- ECSS-E-ST-20C — Electrical and Electronic[^ecssest20]
- ECSS-E-ST-20-08C — Photovoltaic Assemblies and Components
