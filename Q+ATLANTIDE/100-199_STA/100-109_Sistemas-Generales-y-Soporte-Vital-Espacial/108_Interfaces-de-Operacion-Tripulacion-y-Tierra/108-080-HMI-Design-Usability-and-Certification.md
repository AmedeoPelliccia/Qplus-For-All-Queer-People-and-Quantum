---
document_id: QATL-ATLAS-1000-STA-100-109-00-108-080-HMI-DESIGN-USABILITY-AND-CERTIFICATION
title: "STA 100-109 · 108-080 — HMI-Design-Usability-and-Certification"
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
subsection: "108"
subsection_title: "Interfaces de Operación Tripulación y Tierra"
subsubject: "080"
subsubject_title: "HMI-Design-Usability-and-Certification"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 108-080 — HMI-Design-Usability-and-Certification

## 1. Purpose

Defines the **HMI design, usability evaluation, and certification** requirements for all Q+ATLANTIDE crew interfaces, specifying the human factors evaluation process, usability testing requirements, and design assurance evidence per MIL-STD-1472G[^milstd1472] and NASA-STD-3001 Vol.2[^nastd3001v2].

HMI design process: iterative human-centred design lifecycle per ISO 9241-210; task analysis → concept design → prototype → usability test → final design → certification. Usability testing requirements: ≥ 6 crew (or representative users) per evaluation session; task-based protocol for all safety-critical interfaces; success criterion ≥ 90 % task completion rate; error rate < 5 % for critical tasks; test conducted in simulated microgravity environment (underwater or parabolic flight) for physical interface evaluations. Certification evidence: usability test report (participants · tasks · pass/fail · error analysis); HFE verification matrix (requirement → test case → result); all stored as CSDB data modules in subsection `109`.

## 2. Scope

- Covers the *HMI-Design-Usability-and-Certification* subsubject (`080`) of subsection `108`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All HMI designs require human factors evaluation per MIL-STD-1472G[^milstd1472] and NASA-STD-3001 Vol.2[^nastd3001v2].

## 3. Diagram — HMI-Design-Usability-and-Certification

```mermaid
flowchart LR
    TASK_ANAL["Task Analysis<br/>(safety-critical tasks identified)"]
    CONCEPT["Concept Design<br/>(ISO 9241-210 HCD)"]
    PROTOTYPE["Prototype Evaluation"]
    TEST["Usability Test<br/>(≥ 6 crew · task-based<br/>≥ 90% completion · < 5% error)"]
    CERT["HFE Certification<br/>(matrix · CSDB evidence)"]

    TASK_ANAL --> CONCEPT --> PROTOTYPE --> TEST --> CERT
    style TEST fill:#2c82c9,color:#fff
    style CERT fill:#2c82c9,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `108` — Interfaces de Operación Tripulación y Tierra |
| Subsubject | `080` — HMI-Design-Usability-and-Certification |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/108_Interfaces-de-Operacion-Tripulacion-y-Tierra/` |
| Document | `108-080-HMI-Design-Usability-and-Certification.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`108-000-General.md`](./108-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management.

[^ecsse1011]: **ECSS-E-ST-10-11C — Spacecraft Environment Interaction** — Applied here for operations interface monitoring standards.

[^nastd3001v2]: **NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health** — Display, control, and HMI design requirements for crewed spacecraft operations.

[^milstd1472]: **MIL-STD-1472G — Human Engineering** — Anthropometric, display, control-force, and cognitive load requirements.

[^ccsds]: **CCSDS 401.0-B — Radio Frequency and Modulation Systems; CCSDS 131.0-B — TM Synchronization and Channel Coding** — Uplink/downlink communications standards.

### Applicable industry standards

- ECSS-E-ST-10-11C — Spacecraft Environment Interaction[^ecsse1011]
- NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health[^nastd3001v2]
- MIL-STD-1472G — Human Engineering[^milstd1472]
- CCSDS — Radio Frequency and Modulation Systems[^ccsds]
