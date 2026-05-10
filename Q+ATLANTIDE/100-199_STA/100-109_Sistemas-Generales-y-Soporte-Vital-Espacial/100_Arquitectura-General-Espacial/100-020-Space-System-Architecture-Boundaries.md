---
document_id: QATL-ATLAS-1000-STA-100-109-00-100-020-SPACE-SYSTEM-ARCHITECTURE-BOUNDARIES
title: "STA 100-109 · 100-020 — Space System Architecture Boundaries"
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
subsubject: "020"
subsubject_title: "Space System Architecture Boundaries"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · 100-020 — Space System Architecture Boundaries

## 1. Purpose

Defines the **system-level architecture boundaries** for the STA band — the interfaces, exclusion zones, and adjacency rules that delimit what falls within STA `100–199` versus adjacent architecture bands (ATLAS `000–099`, DTTA `200–299`, QCSAA `900–999`), in conformance with ECSS-E-ST-10C[^ecss10].

## 2. Scope

- Covers the *Space System Architecture Boundaries* subsubject (`002`) of subsection `100`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Physical boundary** — orbital altitude envelope (LEO at ≥160 km to deep-space missions), re-entry interfaces, and the Kármán line as the boundary with ATLAS aviation systems.
  - **Functional boundary** — space-domain functions (orbit/attitude control, thermal regulation, payload data handling, deep-space comms) that distinguish STA from ATLAS functions.
  - **Data/information boundary** — scope of STA data products, telemetry streams, and configuration items versus those controlled by QCSAA (`900–999`).
  - **Interface declarations** — formal interface control documents (ICDs) binding STA subsections to ATLAS propulsion (`060–089`) and QCSAA autonomy systems.
  - **Exclusion criteria** — elements explicitly out of STA scope (pure aeronautical systems, ground-only software, administrative data).
- Out of scope: the mission-class taxonomy (`003`) and individual segment decomposition (`004`).

## 3. Diagram — STA Architecture Boundary Map

```mermaid
flowchart LR
    subgraph STA["STA 100–199"]
        S1["Space Segment<br/>(orbit · attitude · payload)"]
        S2["Ground Segment<br/>(TT&C · mission ops)"]
        S3["Launch Segment<br/>(propulsion · fairing)"]
    end
    subgraph ATLAS["ATLAS 000–099"]
        A1["Aircraft Systems<br/>(airframe · avionics)"]
    end
    subgraph QCSAA["QCSAA 900–999"]
        Q1["Quantum/AI Software<br/>(autonomy · algorithms)"]
    end
    STA <-. "ICD: propulsion interfaces<br/>(STA 120–129 ↔ ATLAS 060–089)" .-> ATLAS
    STA <-. "ICD: autonomy hooks<br/>(STA 144 ↔ QCSAA 904)" .-> QCSAA
    KARMAN["Kármán Line (100 km)<br/>Physical boundary"]
    ATLAS -. below .- KARMAN
    KARMAN -. above .- STA
    style STA fill:#eaf3fb,stroke:#2c82c9
    style ATLAS fill:#f0f8e8,stroke:#27ae60
    style QCSAA fill:#f6e6ff,stroke:#7d3c98
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `100` — Arquitectura General Espacial |
| Subsubject | `002` — Space System Architecture Boundaries |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/100_Arquitectura-General-Espacial/` |
| Document | `100-020-Space-System-Architecture-Boundaries.md` (this file) |
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
