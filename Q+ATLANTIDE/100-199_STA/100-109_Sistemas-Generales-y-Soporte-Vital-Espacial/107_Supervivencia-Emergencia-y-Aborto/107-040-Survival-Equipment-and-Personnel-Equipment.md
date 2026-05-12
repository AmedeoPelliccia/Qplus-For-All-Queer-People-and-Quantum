---
document_id: QATL-ATLAS-1000-STA-100-109-00-107-040-SURVIVAL-EQUIPMENT-AND-PERSONNEL-EQUIPMENT
title: "STA 100-109 · 107-040 — Survival-Equipment-and-Personnel-Equipment"
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
subsubject: "040"
subsubject_title: "Survival-Equipment-and-Personnel-Equipment"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 107-040 — Survival-Equipment-and-Personnel-Equipment

## 1. Purpose

Defines the **survival equipment and personal protective equipment** requirements for Q+ATLANTIDE crewed missions, specifying suits, personal life support, survival kits, and post-landing survival capabilities per NASA-STD-3001[^nastd3001].

Launch and entry suit (LES): IVA pressure suit providing emergency pressurization in cabin depressurization; operating pressure 34.5 kPa (5 psi); helmet visors with UV/solar protection; internal O₂ supply ≥ 10 minutes emergency reserve. Survival kits per crew member: emergency locator transmitter (ELT/PLB), personal flotation device (PFD), fresh water (2L), rations (3 days), first aid kit, signalling devices (mirror, flares, dye), exposure protection (thermal blanket, survival suit). Water landing capability: crew module buoyancy sufficient for ≥ 24 hours sea state 6; crew survival at 0–50 °C water temperature for ≥ 2 hours pending rescue.

## 2. Scope

- Covers the *Survival-Equipment-and-Personnel-Equipment* subsubject (`040`) of subsection `107`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All emergency/abort systems are life-safety critical per MIL-STD-882E[^milstd882] Hazard Risk Index I.

## 3. Diagram — Survival-Equipment-and-Personnel-Equipment

```mermaid
flowchart TB
    LES["Launch/Entry Suit (LES)<br/>(34.5 kPa IVA · O₂ ≥ 10 min)"]
    SURV_KIT["Survival Kit<br/>(ELT · PFD · water · rations · FA)"]
    WATER_LAND["Water Landing<br/>(buoyancy ≥ 24h · sea state 6)"]

    LES & SURV_KIT --> CREW_SURVIVAL["Crew Post-Landing Survival<br/>(≥ 72h autonomous)"]
    WATER_LAND --> CREW_SURVIVAL
    CREW_SURVIVAL --> SAR["SAR Recovery<br/>(subsubject 070)"]
    style LES fill:#2c82c9,color:#fff
    style CREW_SURVIVAL fill:#2c82c9,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `107` — Supervivencia, Emergencia y Aborto |
| Subsubject | `040` — Survival-Equipment-and-Personnel-Equipment |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/107_Supervivencia-Emergencia-y-Aborto/` |
| Document | `107-040-Survival-Equipment-and-Personnel-Equipment.md` (this file) |
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
