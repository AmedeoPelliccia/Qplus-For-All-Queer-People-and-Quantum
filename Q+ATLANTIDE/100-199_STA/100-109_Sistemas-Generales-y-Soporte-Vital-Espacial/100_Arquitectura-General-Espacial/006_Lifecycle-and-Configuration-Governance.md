---
document_id: QATL-ATLAS-1000-STA-100-109-00-100-006-LIFECYCLE-AND-CONFIGURATION-GOVERNANCE
title: "STA 100-109 · 00.100.006 — Lifecycle and Configuration Governance"
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
subsubject: "006"
subsubject_title: "Lifecycle and Configuration Governance"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · Section 00 · Subsection 100 · Subsubject 006 — Lifecycle and Configuration Governance

## 1. Purpose

Establishes the **lifecycle phase definitions and configuration-control authority** for STA systems within the Q+ATLANTIDE programme, mapping the space mission lifecycle to the SSOT LC01–LC14 gates and declaring the configuration governance rules per ECSS-E-ST-10C[^ecss10] and NASA/SP-2016-6105[^nasase].

## 2. Scope

- Covers the *Lifecycle and Configuration Governance* subsubject (`006`) of subsection `100`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Lifecycle phases** — Mission Concept (Phase 0), Preliminary Analysis (Phase A), Definition (Phase B), Development (Phase C/D), Operations (Phase E), and Disposal (Phase F), mapped to Q+ATLANTIDE SSOT/LC01–LC14 gates.
  - **Design review gates** — SRR, MDR, PDR, CDR, QR, ORR, FRR, MRR, and EOM review definitions and entry/exit criteria.
  - **Configuration baseline hierarchy** — functional baseline (FBL), allocated baseline (ABL), and product baseline (PBL) per ECSS-E-ST-10C[^ecss10].
  - **Change control authority** — Q-Division (technical authority per rule N-002), ORB-PMO (programme oversight), and Configuration Control Board (CCB) composition rules.
  - **Document and artefact control** — CSDB data modules, ICD versions, and STA-specific controlled document types within the Q+ATLANTIDE baseline.
  - **Disposal and deorbit governance** — ISO 24113 compliance gating at Phase E/F.

## 3. Diagram — STA Lifecycle and Configuration Gates

```mermaid
flowchart LR
    P0["Phase 0<br/>Mission Concept"] --> PA["Phase A<br/>Prelim. Analysis"]
    PA --> PB["Phase B<br/>Definition"]
    PB --> PCD["Phase C/D<br/>Development"]
    PCD --> PE["Phase E<br/>Operations"]
    PE --> PF["Phase F<br/>Disposal"]

    P0 -. "SRR" .-> PA
    PA -. "MDR/PDR" .-> PB
    PB -. "CDR" .-> PCD
    PCD -. "QR/ORR/FRR" .-> PE
    PE -. "MRR/EOM" .-> PF

    PB --> FBL["Functional Baseline<br/>(FBL)"]
    PCD --> ABL["Allocated Baseline<br/>(ABL)"]
    PCD --> PBL["Product Baseline<br/>(PBL)"]

    style P0 fill:#1f3a93,color:#fff
    style PE fill:#2c82c9,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `100` — Arquitectura General Espacial |
| Subsubject | `006` — Lifecycle and Configuration Governance |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/100_Arquitectura-General-Espacial/` |
| Document | `006_Lifecycle-and-Configuration-Governance.md` (this file) |
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

[^iso24113]: **ISO 24113:2019 — Space Systems: Space Debris Mitigation Requirements** — Governs end-of-life disposal orbit, deorbit burn sizing, and passivation requirements in Phase F.

### Applicable industry standards

- ECSS-E-ST-10C Rev.1 — Space Engineering: System Engineering General Requirements[^ecss10]
- ECSS-E-ST-10-02C — Space Environment[^ecss10_02]
- NASA/SP-2016-6105 Rev.2 — NASA Systems Engineering Handbook[^nasase]
- CCSDS 130.0-G-3 — Overview of Space Communications Protocols[^ccsds]
- ISO 14620-1:2018 — Space Systems: Safety Requirements[^iso14620]
- ANSI/AIAA S-102A-2004 — Performance-Based Fault Management Handbook[^ansiaiaa]
- ISO 24113:2019 — Space Systems: Space Debris Mitigation Requirements[^iso24113]
