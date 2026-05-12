---
document_id: QATL-ATLAS-1000-STA-100-109-00-107-010-EMERGENCY-ABORT-CONTROLLED-DEFINITION
title: "STA 100-109 · 107-010 — Emergency-Abort-Controlled-Definition"
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
subsection: "107"
subsection_title: "Supervivencia, Emergencia y Aborto"
subsubject: "010"
subsubject_title: "Emergency-Abort-Controlled-Definition"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 107-010 — Emergency-Abort-Controlled-Definition

## 1. Purpose

Establishes the **controlled normative definition** of the Emergency and Abort subsystem, fixing controlled vocabulary, classification scheme, and scope boundaries per ECSS-Q-ST-40C[^ecssq40] and MIL-STD-882E[^milstd882].

Controlled terms: **Abort** (commanded or autonomous mission termination with crew survival as primary objective); **Emergency** (off-nominal event requiring immediate crew protective action); **Escape System** (hardware providing crew separation from launch vehicle or spacecraft in emergency); **LAS** (Launch Abort System); **ALAS** (Autonomous Launch Abort System); **GPC** (General Purpose Computer, monitors abort triggers); **TUC** (Time of Useful Consciousness, relevant to atmosphere emergencies). Classification: Class I abort (immediate life risk, autonomous trigger); Class II abort (elevated life risk, crew-commanded or ground-commanded); Class III emergency (enhanced monitoring, procedural response).

## 2. Scope

- Covers the *Emergency-Abort-Controlled-Definition* subsubject (`010`) of subsection `107`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All emergency/abort systems are life-safety critical per MIL-STD-882E[^milstd882] Hazard Risk Index I.

## 3. Diagram — Emergency-Abort-Controlled-Definition

```mermaid
flowchart LR
    subgraph ABORT_SYS["Abort Classification"]
        C1["Class I Abort<br/>(autonomous · immediate)"]
        C2["Class II Abort<br/>(crew/ground-commanded)"]
        C3["Class III Emergency<br/>(procedural response)"]
    end
    GPC["GPC Abort Logic<br/>(autonomous trigger)"] --> C1
    CREW["Crew Command<br/>(manual trigger)"] --> C2
    GROUND["Ground Command<br/>(uplink trigger)"] --> C2 & C3
    style C1 fill:#e74c3c,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `107` — Supervivencia, Emergencia y Aborto |
| Subsubject | `010` — Emergency-Abort-Controlled-Definition |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/107_Supervivencia-Emergencia-y-Aborto/` |
| Document | `107-010-Emergency-Abort-Controlled-Definition.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`107-000-General.md`](./107-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management.

[^ecssq40]: **ECSS-Q-ST-40C — Safety** — ESA safety standards applicable to space systems including abort, emergency, and hazard management.

[^iso14620]: **ISO 14620-1:2018 — Space Systems Safety Requirements** — International safety requirements for space launch vehicles and spacecraft.

[^milstd882]: **MIL-STD-882E — System Safety** — Hazard analysis methodology (PHL, SSHA, SHA, SSHA, O&SHA) and risk acceptance criteria.

[^nastd8739]: **NASA-STD-8739.8A — Software Assurance Standard** — Software safety requirements applicable to abort and emergency management systems.

### Applicable industry standards

- ECSS-Q-ST-40C — Safety[^ecssq40]
- ISO 14620-1:2018 — Space Systems Safety Requirements[^iso14620]
- MIL-STD-882E — System Safety[^milstd882]
- NASA-STD-8739.8A — Software Assurance Standard[^nastd8739]

[^nastd3001]: **NASA-STD-3001 Vol.1 & Vol.2 — Human Integration Design Handbook**.
[^ccsds]: **CCSDS 401.0-B — Radio Frequency and Modulation Systems** — Emergency communications protocols for crewed spacecraft.
