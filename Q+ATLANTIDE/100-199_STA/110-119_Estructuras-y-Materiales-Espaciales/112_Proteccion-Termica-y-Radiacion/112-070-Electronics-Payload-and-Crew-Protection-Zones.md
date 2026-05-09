---
document_id: QATL-ATLAS-1000-STA-110-119-01-112-070-ELECTRONICS-PAYLOAD-AND-CREW-PROTECTION-ZONES
title: "STA 110-119 · 112-070 — Electronics Payload and Crew Protection Zones"
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
subsubject: "070"
subsubject_title: "Electronics Payload and Crew Protection Zones"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-GREENTECH, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 110-119 · 112-070 — Electronics Payload and Crew Protection Zones

## 1. Purpose

Defines the **protection zone hierarchy** — electronics enclosures, payload sheltered volumes, and crewed safe-haven zones — establishing allowable dose limits per zone type and the interface with crew radiation safety protocols (→ `101`).

## 2. Scope

- Covers protection zone taxonomy within subsection `112`.
- Concepts in scope: electronics TID tolerance (typically 20–100 krad Si with RDM ≥ 2); payload zone dose budget; crew career dose limits (NCRP 132; 1 Sv career LEO); acute dose safe-haven threshold; dose alert levels during SPE events; zone boundary definition and physical implementation; cross-reference to habitability safe-haven (→ `101_Habitabilidad`) and ECLSS monitoring (→ `102_Soporte-Vital-ECLSS`).

## 3. Diagram — Protection Zone Hierarchy

```mermaid
flowchart TD
    CREW["Crew Habitat Zone<br/>(career dose ≤ 1 Sv · SPE safe-haven)"]
    PAY["Payload Zone<br/>(mission-specific dose budget)"]
    ELEC["Electronics Zone<br/>(TID ≤ rated with RDM ≥ 2)"]
    SHIELD["Platform Shielding<br/>(006 — structural + spot)"]
    SHIELD --> ELEC
    SHIELD --> PAY
    SHIELD --> CREW
    ELEC --> FDIR["FDIR / SEE Mitigation"]
    CREW --> HAVEN["Safe-Haven<br/>(101 — habitability interface)"]
    style CREW fill:#8b0000,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `112` — Protección Térmica y Radiación |
| Subsubject | `007` — Electronics, Payload and Crew Protection Zones |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `112-070-Electronics-Payload-and-Crew-Protection-Zones.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-10-04C — Space Environment
- NASA-STD-3001 Vol.1 — Crew Health (radiation dose limits)
- NCRP Report 132 — Radiation Protection Guidance for Activities in LEO
