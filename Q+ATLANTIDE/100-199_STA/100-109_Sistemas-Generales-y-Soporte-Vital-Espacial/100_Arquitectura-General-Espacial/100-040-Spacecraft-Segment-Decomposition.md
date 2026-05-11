---
document_id: QATL-ATLAS-1000-STA-100-109-00-100-040-SPACECRAFT-SEGMENT-DECOMPOSITION
title: "STA 100-109 · 100-040 — Spacecraft Segment Decomposition"
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
subsection: "100"
subsection_title: "Arquitectura General Espacial"
subsubject: "040"
subsubject_title: "Spacecraft Segment Decomposition"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · 100-040 — Spacecraft Segment Decomposition

## 1. Purpose

Defines the **standard segment decomposition** applied to all spacecraft systems within the STA band — breaking a space mission into its space, ground, launch, and user segments, and mapping each segment to the applicable STA subsections, per NASA/SP-2016-6105[^nasase] and ECSS-E-ST-10C[^ecss10].

## 2. Scope

- Covers the *Spacecraft Segment Decomposition* subsubject (`004`) of subsection `100`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Space segment** — spacecraft bus (structures 110–119, power 130–139, avionics 140–149, comms 150–159) and payload (sensors/instruments 160–169).
  - **Ground segment** — mission control, TT&C stations, and data ground processing (mapped to STA `143_Control-de-Mision` and `152_Redes-Espaciales`).
  - **Launch segment** — launch vehicle interfaces and launch-site integration (mapped to STA `120–129` propulsion and `182_Transporte-Espacial`).
  - **User segment** — end-user receiving equipment and data exploitation chains (mapped to STA `163_Observacion`).
  - **Decomposition tree** — authoritative WBS-level breakdown compliant with NASA SE Handbook Chapter 4[^nasase], with unique IDs per STA subsection.
  - **Interface Control Documents (ICDs)** — inter-segment ICDs declared at this level and controlled through `006_Lifecycle-and-Configuration-Governance`.

## 3. Diagram — Spacecraft Segment Decomposition

```mermaid
flowchart TB
    MISSION["Space Mission<br/>(STA 100–199)"]
    MISSION --> SS["Space Segment<br/>(Bus + Payload)"]
    MISSION --> GS["Ground Segment<br/>(TT&C · Mission Ops · Data)"]
    MISSION --> LS["Launch Segment<br/>(LV · Launch Site)"]
    MISSION --> US["User Segment<br/>(Ground Terminals · Data Users)"]

    SS --> BUS["Spacecraft Bus<br/>Structures 110–119<br/>Power 130–139<br/>Avionics 140–149<br/>Comms 150–159"]
    SS --> PL["Payload<br/>Sensors 160–169"]
    GS --> MCC["Mission Control<br/>143_Control-de-Mision"]
    GS --> NET["Space Networks<br/>152_Redes-Espaciales"]
    LS --> PROP["Propulsion<br/>120–129"]
    LS --> XPORT["Space Transport<br/>182_Transporte-Espacial"]
    US --> OBS["Observation & Data<br/>163_Observacion"]

    style MISSION fill:#1f3a93,color:#fff
    style SS fill:#2c82c9,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `100` — Arquitectura General Espacial |
| Subsubject | `004` — Spacecraft Segment Decomposition |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/100_Arquitectura-General-Espacial/` |
| Document | `100-040-Spacecraft-Segment-Decomposition.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`100-000-General.md`](./100-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `100-109` row (Section `00` — Sistemas Generales y Soporte Vital Espacial, Primary Q-Division Q-SPACE).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ecss10]: **ECSS-E-ST-10C Rev.1 — Space Engineering: System Engineering General Requirements** — European standard governing space-system architecture decomposition, requirement flow-down, and V&V planning.

[^ecss10_02]: **ECSS-E-ST-10-02C — Space Environment** — Defines the space-environment models (radiation belts, solar protons, thermal environment) that bound all STA architecture designs.

[^nasase]: **NASA/SP-2016-6105 Rev.2 — NASA Systems Engineering Handbook** — Authoritative SE reference used for mission-class taxonomy, segment decomposition, and lifecycle governance across NASA programmes.

[^ccsds]: **CCSDS 130.0-G-3 — Overview of Space Communications Protocols** — CCSDS Green Book that frames ground-to-space communication architecture at the mission-control interface layer.

[^iso14620]: **ISO 14620-1:2018 — Space Systems: Safety Requirements** — International standard for top-level safety and risk requirements applicable to all space mission classes.

[^ansiaiaa]: **ANSI/AIAA S-102A-2004 — Performance-Based Fault Management Handbook** — Fault management design framework guiding safety and assurance boundaries in the STA band.

### Applicable industry standards

- ECSS-E-ST-10C Rev.1 — Space Engineering: System Engineering General Requirements[^ecss10]
- ECSS-E-ST-10-02C — Space Environment[^ecss10_02]
- NASA/SP-2016-6105 Rev.2 — NASA Systems Engineering Handbook[^nasase]
- CCSDS 130.0-G-3 — Overview of Space Communications Protocols[^ccsds]
- ISO 14620-1:2018 — Space Systems: Safety Requirements[^iso14620]
- ANSI/AIAA S-102A-2004 — Performance-Based Fault Management Handbook[^ansiaiaa]
