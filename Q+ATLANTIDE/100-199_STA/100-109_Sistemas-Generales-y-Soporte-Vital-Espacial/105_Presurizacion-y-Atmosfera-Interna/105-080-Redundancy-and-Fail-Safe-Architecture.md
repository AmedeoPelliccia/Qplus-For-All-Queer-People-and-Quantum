---
document_id: QATL-ATLAS-1000-STA-100-109-00-105-080-REDUNDANCY-AND-FAIL-SAFE-ARCHITECTURE
title: "STA 100-109 · 105-080 — Redundancy and Fail-Safe Architecture"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "100-109"
section: "00"
section_title: "Sistemas Generales y Soporte Vital Espacial"
subsection: "105"
subsection_title: "Presurización y Atmósfera Interna"
subsubject: "080"
subsubject_title: "Redundancy and Fail-Safe Architecture"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 105-080 — Redundancy and Fail-Safe Architecture

## 1. Purpose

Defines the **redundancy and fail-safe architecture** for the pressurization subsystem, specifying the minimum redundancy levels, fault-tolerance logic, and fail-safe valve states that ensure crew survivability after any credible single-point failure per ECSS-Q-ST-40C[^ecssq40].

Pressurization subsystem redundancy philosophy: all safety-critical functions (pressure regulation, overpressure protection, pressure monitoring) are dual-redundant with independent failure modes. Fail-safe states: PRV fails closed (prevents runaway pressurization); OFV fails open (prevents structural overpressure); PRV-B (backup regulator) fails closed and activates on PRV-A failure. The monitoring system uses 2-of-3 voting for alarm activation on cabin pressure to prevent spurious alarms from single sensor failures. Crew emergency O₂ masks are provided at ≤ 30 s reach from any crew position.

## 2. Scope

- Covers the *Redundancy and Fail-Safe Architecture* subsubject (`080`) of subsection `105`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All design decisions traceable to source standards and CSDB evidence per subsection `109`.

## 3. Diagram — Redundancy and Fail-Safe Architecture

```mermaid
flowchart TB
    subgraph PRIMARY["Primary Pressure Path"]
        PRV_A["PRV-A<br/>(primary regulator)"]
        OFV_A["OFV-A<br/>(primary outflow)"]
    end
    subgraph BACKUP["Backup Pressure Path"]
        PRV_B["PRV-B<br/>(backup regulator)"]
        OFV_B["OFV-B<br/>(backup outflow)"]
    end
    GAS["Gas Supply"] --> PRV_A & PRV_B
    PRV_A & PRV_B --> CABIN["Cabin Volume"]
    CABIN --> OFV_A & OFV_B
    CABIN --> SRV["SRV<br/>(passive — no power needed)"]

    FDIR["FDIR Logic<br/>(2-of-3 pressure voting)"] --> PRV_B
    style CABIN fill:#eaf3fb,stroke:#2c82c9
    style SRV fill:#e74c3c,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `105` — Presurización y Atmósfera Interna |
| Subsubject | `080` — Redundancy and Fail-Safe Architecture |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/105_Presurizacion-y-Atmosfera-Interna/` |
| Document | `105-080-Redundancy-and-Fail-Safe-Architecture.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`105-000-General.md`](./105-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management.

[^ecsse34]: **ECSS-E-ST-34C Rev.1 — Space Engineering: Environmental Control and Life Support** — Primary standard for pressurization design, cabin atmosphere, and leak detection requirements.

[^nastd3001]: **NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health** — Cabin pressure and atmospheric composition requirements for crew health.

[^nasajsc]: **NASA/JSC-65591 — ECLSS Design and Performance Requirements** — Pressurization system design reference for ISS-class crewed modules.

[^iso20521]: **ISO 20521 — Space Systems: Human Spaceflight** — Crew habitability and pressurization requirements for crewed spacecraft.

### Applicable industry standards

- ECSS-E-ST-34C Rev.1 — Space Engineering: Environmental Control and Life Support[^ecsse34]
- NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health[^nastd3001]
- NASA/JSC-65591 — ECLSS Design and Performance Requirements[^nasajsc]
- ISO 20521 — Space Systems: Human Spaceflight[^iso20521]
