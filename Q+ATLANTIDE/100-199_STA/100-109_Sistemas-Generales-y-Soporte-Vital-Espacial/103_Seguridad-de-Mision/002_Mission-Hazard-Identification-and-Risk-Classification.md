---
document_id: QATL-ATLAS-1000-STA-100-109-00-103-002-MISSION-HAZARD-IDENTIFICATION-AND-RISK-CLASSIFICATION
title: "STA 100-109 · 00.103.002 — Mission Hazard Identification and Risk Classification"
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
subsection: "103"
subsection_title: "Seguridad de Misión"
subsubject: "002"
subsubject_title: "Mission Hazard Identification and Risk Classification"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · Section 00 · Subsection 103 · Subsubject 002 — Mission Hazard Identification and Risk Classification

## 1. Purpose

Defines the **mission-level hazard identification methodology and risk classification framework** used throughout STA `100–199`, establishing the hazard log, severity/probability matrix, ALARP demonstration process, and risk acceptance authority, per ISO 14620-1[^iso14620] and MIL-STD-882E[^milstd882].

## 2. Scope

- Covers the *Mission Hazard Identification and Risk Classification* subsubject (`002`) of subsection `103`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Hazard log structure** — unique hazard ID, hazard description, initiating event, hazard barrier list, severity class (Cat-I–IV), probability class (A–E), current risk level, and residual risk.
  - **Severity × probability risk matrix** — 5×4 matrix with colour-coded risk regions (unacceptable, ALARP, acceptable) per ISO 14620-1[^iso14620].
  - **Hazard types** — structural failure, pressure loss (rapid depressurisation), toxic/chemical release, fire, radiation exposure, software/autonomy fault, collision/debris impact, and human-factor error.
  - **ALARP demonstration** — structured argument that risks are As Low As Reasonably Practicable, including cost-benefit analysis for Cat-II hazards.
  - **Risk acceptance authority** — Cat-I: eliminated by design (no waiver); Cat-II: Q-Division + ORB-LEG + Programme Safety Review Board (PSRB); Cat-III: Q-Division; Cat-IV: subsystem lead.
  - **Hazard reviews** — Preliminary Hazard Analysis (PHA) at Phase A, System Hazard Analysis (SHA) at Phase C, and Mission-level Hazard Review at ORR.

## 3. Diagram — Risk Classification Matrix

```mermaid
flowchart LR
    HID["Hazard Identification<br/>(hazard log — all STA subsystems)"]
    HID --> SEV["Severity Classification<br/>(Cat-I Catastrophic<br/>Cat-II Critical<br/>Cat-III Marginal<br/>Cat-IV Negligible)"]
    HID --> PROB["Probability Classification<br/>(A Frequent · B Probable<br/>C Occasional · D Remote · E Improbable)"]
    SEV --> MATRIX["Risk Matrix<br/>(severity × probability)"]
    PROB --> MATRIX
    MATRIX --> ALARP["ALARP Demonstration<br/>(Cat-I: eliminate · Cat-II: mitigate)"]
    ALARP --> PSRB["Risk Acceptance<br/>(PSRB · Q-SPACE · ORB-LEG)"]

    style MATRIX fill:#f39c12,color:#fff
    style PSRB fill:#e74c3c,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `103` — Seguridad de Misión |
| Subsubject | `002` — Mission Hazard Identification and Risk Classification |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/103_Seguridad-de-Mision/` |
| Document | `002_Mission-Hazard-Identification-and-Risk-Classification.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `100-109` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^iso14620]: **ISO 14620-1:2018 — Space Systems: Safety Requirements** — International standard for top-level safety requirements and hazard classification for all space missions.

[^ecssq40]: **ECSS-Q-ST-40C — Space Product Assurance: Safety** — European standard governing space-system safety analysis, hazard classification, and product assurance for mission-critical systems.

[^milstd882]: **MIL-STD-882E — System Safety** — US DoD standard providing the system safety programme requirements including hazard identification, risk classification, and FMEA methodology.

[^nastd8739]: **NASA-STD-8739.8 — Software Assurance Standard** — NASA software assurance requirements applicable to FDIR software and mission-safety critical software elements.

[^nasase]: **NASA/SP-2016-6105 Rev.2 — NASA Systems Engineering Handbook** — SE lifecycle and design-review gate criteria applicable to mission safety reviews.

### Applicable industry standards

- ISO 14620-1:2018 — Space Systems: Safety Requirements[^iso14620]
- ECSS-Q-ST-40C — Space Product Assurance: Safety[^ecssq40]
- MIL-STD-882E — System Safety[^milstd882]
- NASA-STD-8739.8 — Software Assurance Standard[^nastd8739]
- NASA/SP-2016-6105 Rev.2 — NASA Systems Engineering Handbook[^nasase]
