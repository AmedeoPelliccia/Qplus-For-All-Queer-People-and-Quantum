---
document_id: QATL-ATLAS-1000-STA-100-109-00-103-003-CREW-SAFETY-AND-SURVIVABILITY-BOUNDARIES
title: "STA 100-109 · 00.103.003 — Crew Safety and Survivability Boundaries"
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
subsubject: "003"
subsubject_title: "Crew Safety and Survivability Boundaries"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · Section 00 · Subsection 103 · Subsubject 003 — Crew Safety and Survivability Boundaries

## 1. Purpose

Defines the **crew safety and survivability envelope** — the design-level boundaries that must not be violated during any mission phase to maintain crew survival — including structural loads, atmosphere exposure limits, radiation limits, and thermal/acoustic thresholds, per NASA-STD-3001 Vol.1 and ISO 14620-1[^iso14620].

## 2. Scope

- Covers the *Crew Safety and Survivability Boundaries* subsubject (`003`) of subsection `103`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Structural load limits** — maximum sustained acceleration (≤ 3 g seated), dynamic load limits during launch/re-entry (±16 g in Z-axis per NASA-STD-3001), impact limits for contingency landing.
  - **Atmosphere survivability** — cabin pressure range 50–103 kPa; hypoxia threshold (O₂ pp < 16 kPa), hypercapnia threshold (CO₂ pp > 1.0 kPa — incapacitation risk); emergency limits for depressurisation contingency.
  - **Radiation survivability** — acute radiation dose limits for solar particle events (short-exposure, non-cancer risk from NASA-STD-3001 Vol.1), shielding minimum from `101.004`.
  - **Thermal survivability** — cabin temperature limits for crew tolerance (10–35 °C at extremes), EVA suit thermal limits, and fire detection and suppression timeline requirements.
  - **Acoustic survivability** — impulsive noise limits (≤ 140 dB peak SPL), continuous noise ceiling (≤ 85 dB-A for non-protected crew time).
  - **Time-to-safety** — maximum allowable time for crew to reach safe-haven or escape system from any crew position: ≤ 3 minutes for contingency scenarios.

## 3. Diagram — Crew Survivability Envelope

```mermaid
flowchart TB
    ENV["Mission Environment<br/>(launch · orbit · re-entry · landing)"]
    ENV --> STRUCT["Structural Loads<br/>(≤3 g sustained · ±16 g Z dynamic)"]
    ENV --> ATMOS["Atmosphere Limits<br/>(O₂ pp 16–23 kPa<br/>CO₂ pp ≤1.0 kPa emergency)"]
    ENV --> RAD["Radiation Limits<br/>(REID · acute SPE dose)"]
    ENV --> THERM["Thermal Limits<br/>(10–35 °C crew | fire suppression)"]
    ENV --> ACOU["Acoustic Limits<br/>(≤85 dB-A continuous<br/>≤140 dB-A peak)"]

    STRUCT --> BOUND["Crew Survivability Boundary<br/>(must not be violated)"]
    ATMOS --> BOUND
    RAD --> BOUND
    THERM --> BOUND
    ACOU --> BOUND
    BOUND --> ABORT["→ Abort/Escape if violated<br/>(005 Abort Modes)"]

    style BOUND fill:#e74c3c,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `103` — Seguridad de Misión |
| Subsubject | `003` — Crew Safety and Survivability Boundaries |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/103_Seguridad-de-Mision/` |
| Document | `003_Crew-Safety-and-Survivability-Boundaries.md` (this file) |
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
