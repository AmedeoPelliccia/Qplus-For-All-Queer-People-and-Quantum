---
document_id: QATL-ATLAS-1000-STA-100-109-00-100-008-SAFETY-RISK-AND-ASSURANCE-BOUNDARIES
title: "STA 100-109 · 00.100.008 — Safety Risk and Assurance Boundaries"
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
subsubject: "008"
subsubject_title: "Safety Risk and Assurance Boundaries"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · Section 00 · Subsection 100 · Subsubject 008 — Safety, Risk and Assurance Boundaries

## 1. Purpose

Defines the **top-level safety classification, risk acceptance criteria, and product-assurance boundaries** for all systems within the STA `100–199` band, establishing the framework that governs hazard identification, risk controls, and assurance activities per ISO 14620-1[^iso14620], ECSS-Q-ST-40C, and ANSI/AIAA S-102A[^ansiaiaa].

## 2. Scope

- Covers the *Safety, Risk and Assurance Boundaries* subsubject (`008`) of subsection `100`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Safety classification** — Catastrophic (Cat-I), Critical (Cat-II), Marginal (Cat-III), and Negligible (Cat-IV) hazard classes per ISO 14620-1[^iso14620] applied to STA systems.
  - **Risk matrix** — probability × severity matrix defining acceptable risk regions and ALARP demonstration requirements for each STA subsection.
  - **Fault management** — autonomous fault detection, isolation, and recovery (FDIR) allocation between on-board systems (`144_Autonomia`) and ground control (`143_Control-de-Mision`) per ANSI/AIAA S-102A[^ansiaiaa].
  - **Product assurance (PA) plan** — quality, reliability, and EEE-parts assurance obligations per ECSS-Q-ST-40C, applicable to all STA subsections.
  - **Safety boundaries with adjacent bands** — interface to CYB `800–899` for cybersecurity assurance and to DTTA `200–299` for dual-use technology assurance.
  - **Residual risk acceptance authority** — Q-Division (technical), ORB-LEG (legal), and Programme Safety Review Board (PSRB) authority levels.

## 3. Diagram — Safety and Risk Control Flow

```mermaid
flowchart TD
    H["Hazard Identification<br/>(all STA subsections)"]
    H --> CLASS["Hazard Classification<br/>(Cat-I → Cat-IV per ISO 14620-1)"]
    CLASS --> RISK["Risk Assessment<br/>(probability × severity matrix)"]
    RISK --> ALARP["ALARP Demonstration<br/>(acceptable risk region)"]
    ALARP --> FDIR["FDIR Allocation<br/>(on-board 144 vs ground 143)"]
    ALARP --> PA["Product Assurance Plan<br/>(ECSS-Q-ST-40C)"]
    PA --> CCB["Configuration Control<br/>(006 Lifecycle Governance)"]
    ALARP -. "residual risk" .-> PSRB["Programme Safety Review Board<br/>(Q-SPACE · ORB-LEG)"]

    style H fill:#e74c3c,color:#fff
    style ALARP fill:#f39c12,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `100` — Arquitectura General Espacial |
| Subsubject | `008` — Safety, Risk and Assurance Boundaries |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/100_Arquitectura-General-Espacial/` |
| Document | `008_Safety-Risk-and-Assurance-Boundaries.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |
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

[^ecssq40]: **ECSS-Q-ST-40C — Space Product Assurance: Software Product Assurance** — Governs product assurance requirements for space software and system artefacts within STA.

### Applicable industry standards

- ECSS-E-ST-10C Rev.1 — Space Engineering: System Engineering General Requirements[^ecss10]
- ECSS-E-ST-10-02C — Space Environment[^ecss10_02]
- NASA/SP-2016-6105 Rev.2 — NASA Systems Engineering Handbook[^nasase]
- CCSDS 130.0-G-3 — Overview of Space Communications Protocols[^ccsds]
- ISO 14620-1:2018 — Space Systems: Safety Requirements[^iso14620]
- ANSI/AIAA S-102A-2004 — Performance-Based Fault Management Handbook[^ansiaiaa]
- ECSS-Q-ST-40C — Space Product Assurance[^ecssq40]
