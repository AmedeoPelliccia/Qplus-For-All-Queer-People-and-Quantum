---
document_id: QATL-ATLAS-1000-ATLAS-060-069-06-README
title: "ATLAS 060-069 · 06 — Propulsión Tradicional (Section Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "060-069"
section: "06"
section_title: "Propulsión Tradicional"
section_title_en: "Traditional Propulsion"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-MECHANICS, Q-AIR, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 060-069 · Section 06 — Propulsión Tradicional

## 1. Purpose

Section-level index for *Propulsión Tradicional* (`060-069`) within the ATLAS band. Propulsión tradicional: hélices, turbinas, control de motor, ignición, indicación, escape, aceite y arranque.

This section is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. Bands classify technologies, Q-Divisions provide technical authority and ORB-Functions provide enterprise support[^n002].

## 2. Scope

- Aggregates the subsections within the `060-069` code range listed in §3.
- Inherits Q-Division authority and ORB support from the parent row in [`../README.md` §3](../README.md#3-architecture-table)[^archtable].
- Each subsection folder contains its own `README.md` (subsection index) and may contain Overview and subsubject documents.

## 3. Subsection Index

| Code | Title | Folder | Status |
|---:|---|---|---|
| `060` | Standard Practices — Propeller/Rotor | [`060_Standard-Practices-Propeller-Rotor/`](./060_Standard-Practices-Propeller-Rotor/) | active |
| `061` | Propellers and Propulsors | [`061_Propellers-and-Propulsors/`](./061_Propellers-and-Propulsors/) | active |
| `062` | Power Plant | [`062_Power-Plant/`](./062_Power-Plant/) | active |
| `063` | Engine — Turbine | [`063_Engine-Turbine/`](./063_Engine-Turbine/) | active |
| `064` | Engine Fuel and Control | [`064_Engine-Fuel-and-Control/`](./064_Engine-Fuel-and-Control/) | active |
| `065` | Ignition | [`065_Ignition/`](./065_Ignition/) | active |
| `066` | Air Compressor | [`066_Air-Compressor/`](./066_Air-Compressor/) | active |
| `067` | Engine Controls | [`067_Engine-Controls/`](./067_Engine-Controls/) | active |
| `068` | Engine Indicating | [`068_Engine-Indicating/`](./068_Engine-Indicating/) | active |
| `069` | Exhaust, Oil and Starting | [`069_Exhaust-Oil-and-Starting/`](./069_Exhaust-Oil-and-Starting/) | active |

## 4. Interfaces Diagram

```mermaid
flowchart TB
    PARENT["ATLAS-1000<br/>(`000–099` master range)"]:::parent
    SEC["Section 06 · 060-069<br/>Propulsión Tradicional"]:::sec
    PARENT --> SEC

    subgraph SUBS["Subsections"]
        direction LR
        SUB_060["060 — Standard Practices — Propeller/Rotor (ATA 60)"]:::sub
        SUB_061["061 — Propellers & Propulsors (ATA 61)"]:::sub
        SUB_062["062 — Power Plant (ATA 71)"]:::sub
        SUB_063["063 — Engine — Turbine (ATA 72)"]:::sub
        SUB_064["064 — Engine Fuel & Control (ATA 73)"]:::sub
        SUB_065["065 — Ignition (ATA 74)"]:::sub
        SUB_066["066 — Air Compressor (ATA 75)"]:::sub
        SUB_067["067 — Engine Controls (ATA 76)"]:::sub
        SUB_068["068 — Engine Indicating (ATA 77)"]:::sub
        SUB_069["069 — Exhaust, Oil & Starting (ATA 78–80)"]:::sub
    end
    SEC --> SUBS

    QPRIM["Q-GREENTECH<br/>(primary Q-Division)"]:::qdiv
    QSUPP["Q-MECHANICS, Q-AIR, Q-INDUSTRY<br/>(support Q-Divisions)"]:::qdiv
    ORB["ORB-PMO, ORB-FIN<br/>(ORB support)"]:::orb

    SEC --> QPRIM
    SEC -.-> QSUPP
    SEC -.-> ORB

    SUBS --> SUB_060
    SUBS --> SUB_061
    SUBS --> SUB_062
    SUBS --> SUB_063
    SUBS --> SUB_064
    SUBS --> SUB_065
    SUBS --> SUB_066
    SUBS --> SUB_067
    SUBS --> SUB_068
    SUBS --> SUB_069
    EXT_S07["§07 · Hybrid-Electric (070-079)"]:::ext
    SUB_062 -. "hybrid integration" .- EXT_S07

    classDef parent fill:#1f3a93,stroke:#0b1d4a,color:#fff
    classDef sec fill:#2c82c9,stroke:#0b1d4a,color:#fff
    classDef sub fill:#eaf3fb,stroke:#2c82c9,color:#0b1d4a
    classDef qdiv fill:#f6e6ff,stroke:#7d3c98,color:#3b1f4d
    classDef orb fill:#fff4dd,stroke:#b9770e,color:#5a3b00
    classDef ext fill:#fdebd0,stroke:#b9770e,color:#5a3b00,stroke-dasharray:3 3
```

*Solid arrows show parent→section→subsection ownership and primary Q-Division authority; dotted arrows show support Q-Divisions, ORB enterprise support, and notable cross-section interfaces.*

## 5. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `060-069` |
| Section | `06` — Propulsión Tradicional |
| Subsections | 10 populated |
| Primary Q-Division | Q-GREENTECH[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-AIR, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/060-069_Propulsion-Tradicional/` |
| Document | `README.md` (this file) |
| Parent architecture | [`../README.md`](../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsections under this section inherit `architecture_code = ATLAS`, `primary_q_division = Q-GREENTECH` and `governance_class = baseline` from this section header. Templates declared in this section must populate `architecture_band`, `architecture_code = ATLAS`, `q_division_owner` and `orb_function_support` per the Templates System[^templates]. The No-AAA Rule[^n004] applies.

## 6. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Architecture Table (parent)** — [`../README.md` §3](../README.md#3-architecture-table). Source of authority for primary/support Q-Divisions and ORB support of this section.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^templates]: **§5 — Templates System** — [`organization/Q+ATLANTIDE.md` §5](../../../organization/Q+ATLANTIDE.md#5-templates-system).

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../organization/Q+ATLANTIDE.md#4-notes).

[^n002]: **Note N-002** — Architecture bands classify technologies; Q-Divisions provide technical authority; ORB-Functions provide enterprise support. See [`organization/Q+ATLANTIDE.md` §4](../../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../../organization/Q+ATLANTIDE.md#4-notes).
