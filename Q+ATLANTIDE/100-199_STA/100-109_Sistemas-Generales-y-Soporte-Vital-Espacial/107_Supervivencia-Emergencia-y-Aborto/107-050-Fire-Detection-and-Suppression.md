---
document_id: QATL-ATLAS-1000-STA-100-109-00-107-050-FIRE-DETECTION-AND-SUPPRESSION
title: "STA 100-109 · 107-050 — Fire-Detection-and-Suppression"
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
subsubject: "050"
subsubject_title: "Fire-Detection-and-Suppression"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 107-050 — Fire-Detection-and-Suppression

## 1. Purpose

Defines the **fire detection, suppression, and fire emergency response** architecture for Q+ATLANTIDE spacecraft habitation modules, specifying sensor types, suppression agents, and emergency procedures per ECSS-Q-ST-40C[^ecssq40].

Fire detection: dual-technology smoke detectors (photoelectric + ionisation) in all habitable volumes with < 1 min response time; CO detector array monitoring CO levels > 50 ppm as secondary fire indicator; temperature sensors monitoring for thermal runaway. Suppression: primary agent CO₂ (suitable for microgravity, electrically non-conductive); secondary agent Halon-1301 equivalent (if CO₂ insufficient); fixed suppression for avionics bays (automatic trigger); portable fire extinguishers in all habitable volumes within 3 m crew reach. Emergency procedure: crew dons oxygen masks, isolates ventilation, suppresses fire, activates emergency atmosphere purification; evacuation to safe module if suppression fails.

## 2. Scope

- Covers the *Fire-Detection-and-Suppression* subsubject (`050`) of subsection `107`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All emergency/abort systems are life-safety critical per MIL-STD-882E[^milstd882] Hazard Risk Index I.

## 3. Diagram — Fire-Detection-and-Suppression

```mermaid
flowchart TB
    SMOKE["Smoke/CO Detectors<br/>(photoelectric + ionisation · CO > 50 ppm)"]
    TEMP["Thermal Sensors<br/>(thermal runaway detection)"]
    SMOKE & TEMP --> ALERT["Fire Alert<br/>(< 1 min response)"]
    ALERT --> CREW_ACT["Crew Action<br/>(O₂ masks · vent isolation)"]
    ALERT --> SUPPRES["Suppression System<br/>(CO₂ primary · Halon secondary)"]
    SUPPRES --> FIXED["Fixed Suppression<br/>(avionics bay · auto)"]
    SUPPRES --> PORTABLE["Portable Extinguisher<br/>(< 3m reach · crew-used)"]
    CREW_ACT --> EVAC["Module Evacuation<br/>(if suppression fails)"]
    style ALERT fill:#e74c3c,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `107` — Supervivencia, Emergencia y Aborto |
| Subsubject | `050` — Fire-Detection-and-Suppression |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/107_Supervivencia-Emergencia-y-Aborto/` |
| Document | `107-050-Fire-Detection-and-Suppression.md` (this file) |
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
