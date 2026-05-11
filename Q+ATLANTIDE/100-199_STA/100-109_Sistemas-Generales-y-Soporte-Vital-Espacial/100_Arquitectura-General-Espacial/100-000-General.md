---
document_id: QATL-ATLAS-1000-STA-100-109-00-100-000-GENERAL
title: "STA 100-109 · 100-000 — General"
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
subsubject: "000"
subsubject_title: "General"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · 100-000 — General

## 1. Purpose

Overview entry-point for the *Arquitectura General Espacial* subsection within the `100-109` code range (Section `00` — *Sistemas Generales y Soporte Vital Espacial*) of the **STA** architecture band (*Space Technology Architecture*, master range `100–199`).

This subsubject (`000 Overview`) introduces the STA 100-109.100 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4. It establishes the architectural framework — controlled definition, system boundaries, mission taxonomy, segment decomposition, ground interfaces, lifecycle governance, standards mapping, safety boundaries, and Q-Division traceability — governing all general space architecture activities within the Q+ATLANTIDE programme.

## 2. Scope

- Covers the *Arquitectura General Espacial* slice of the parent code range `100-109`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`001`–`009`) under this subsection extend this Overview with detailed modules; the populated set in this baseline is `001`–`009`, indexed in [`README.md`](./README.md).
- Concepts in scope across the subsection:
  - **STA General Architecture Controlled Definition** (`001`) — normative definition of the Space Technology Architecture band and its relationship to Q+ATLANTIDE per ECSS-E-ST-10C[^ecss10].
  - **Space System Architecture Boundaries** (`002`) — envelope definitions, exclusion criteria, and interfaces with adjacent architecture bands.
  - **Mission Class and Orbital Regime Taxonomy** (`003`) — classification of mission classes (LEO, MEO, GEO, HEO, lunar, interplanetary) per ECSS-E-ST-10-02C[^ecss10_02].
  - **Spacecraft Segment Decomposition** (`004`) — breakdown into space, ground, launch, and user segments per NASA/SP-2016-6105[^nasase].
  - **Ground Segment and Mission Control Interfaces** (`005`) — communication architecture and data-flow interfaces per CCSDS 130.0-G-3[^ccsds].
  - **Lifecycle and Configuration Governance** (`006`) — lifecycle phase definitions, baseline gates, and configuration-control authority.
  - **ECSS / NASA / CCSDS Standards Mapping** (`007`) — cross-reference of applicable standards to the STA band subsubjects.
  - **Safety, Risk and Assurance Boundaries** (`008`) — top-level safety classification and risk acceptance criteria per ISO 14620-1[^iso14620].
  - **Q-Division and ORB Function Traceability** (`009`) — traceability matrix linking Q-Division authority rows to this subsection's outputs.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `100` — Arquitectura General Espacial |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/100_Arquitectura-General-Espacial/` |
| Document | `100-000-General.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

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
