---
document_id: QATL-ATLAS-1000-STA-100-109-00-107-080-EMERGENCY-COMMUNICATIONS-AND-DISTRESS-SIGNALLING
title: "STA 100-109 · 107-080 — Emergency-Communications-and-Distress-Signalling"
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
subsubject: "080"
subsubject_title: "Emergency-Communications-and-Distress-Signalling"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 107-080 — Emergency-Communications-and-Distress-Signalling

## 1. Purpose

Defines the **emergency communications and distress signalling** architecture for Q+ATLANTIDE missions, specifying redundant emergency communication paths, distress beacon standards, and ground emergency communication protocols per CCSDS emergency standards[^ccsds].

Emergency communication system provides three independent paths: (1) Primary: spacecraft primary RF link (S-band/X-band) to mission control; (2) Secondary: TDRSS relay (for LEO missions) providing near-continuous coverage; (3) Tertiary: UHF/VHF emergency radio (crew module, battery-powered, independent of main power bus). Distress beacons: ELT transmitting 406 MHz (Cospas-Sarsat) + 121.5 MHz homing; EPIRB for water landing; personal locator beacon (PLB) per crew member. Emergency communication protocol: activation within 60 seconds of emergency declaration; continuous ELT transmission until SAR contact confirmed; voice authentication protocol for abort commands to prevent false abort triggers.

## 2. Scope

- Covers the *Emergency-Communications-and-Distress-Signalling* subsubject (`080`) of subsection `107`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All emergency/abort systems are life-safety critical per MIL-STD-882E[^milstd882] Hazard Risk Index I.

## 3. Diagram — Emergency-Communications-and-Distress-Signalling

```mermaid
flowchart TB
    PRIMARY["Primary RF Link<br/>(S-band/X-band · MCC)"]
    SECONDARY["TDRSS Relay<br/>(near-continuous LEO coverage)"]
    TERTIARY["UHF/VHF Emergency Radio<br/>(battery-independent · crew)"]

    PRIMARY & SECONDARY & TERTIARY --> COMMS_ARCH["Emergency Comms Architecture<br/>(3 independent paths)"]

    ELT["ELT — 406 MHz<br/>(Cospas-Sarsat)"]
    PLB["PLB per Crew<br/>(personal locator)"]
    ELT & PLB --> SAR_ACTIV["SAR Activation<br/>(< 60 s from emergency declaration)"]
    style COMMS_ARCH fill:#2c82c9,color:#fff
    style SAR_ACTIV fill:#e74c3c,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `107` — Supervivencia, Emergencia y Aborto |
| Subsubject | `080` — Emergency-Communications-and-Distress-Signalling |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/107_Supervivencia-Emergencia-y-Aborto/` |
| Document | `107-080-Emergency-Communications-and-Distress-Signalling.md` (this file) |
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
