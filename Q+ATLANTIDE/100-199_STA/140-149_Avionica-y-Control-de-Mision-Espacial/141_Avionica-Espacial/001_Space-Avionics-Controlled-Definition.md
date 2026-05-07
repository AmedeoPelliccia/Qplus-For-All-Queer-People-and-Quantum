---
document_id: QATL-ATLAS-1000-STA-140-149-04-141-001-SPACE-AVIONICS-CONTROLLED-DEFINITION
title: "STA 140-149 · 04.141.001 — Space Avionics Controlled Definition"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "140-149"
section: "04"
section_title: "Aviónica y Control de Misión Espacial"
subsection: "141"
subsection_title: "Aviónica Espacial"
subsubject: "001"
subsubject_title: "Space Avionics Controlled Definition"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 140-149 · Section 04 · Subsection 141 · Subsubject 001 — Space Avionics Controlled Definition

## 1. Purpose

Establishes the **normative definition and controlled scope** of space avionics within the Q+ATLANTIDE STA band, per ECSS-E-ST-50C[^ecssest50c].

## 2. Scope

- **Controlled definition** — Space avionics encompasses the onboard electronic hardware, data handling systems, and communication interfaces that acquire, process, distribute, and store data from sensors, generate commands to actuators and payloads, and manage telemetry and telecommand exchanges with ground stations throughout all mission phases.
- **Applicability boundary** — STA `141` covers the avionics hardware layer on Q+ATLANTIDE STA-band platforms: onboard computers, data handling units, avionics buses, interface units, and power conditioning electronics; excludes GNC algorithm software (→ `140`), flight software execution (→ `142`), ground control (→ `143`), and autonomy management (→ `144`).
- **Controlled vocabulary** — *Onboard Computer (OBC)*; *Data Handling Unit (DHU)*; *Remote Terminal Unit (RTU)*; *Error Detection and Correction (EDAC)*; *Fault Detection, Isolation and Recovery (FDIR)*; *Total Ionising Dose (TID)*; *Single Event Effect (SEE)*; *SpaceWire*; *MIL-STD-1553B*; *CCSDS PUS*.
- **Safety classification** — mission-avionics critical; avionics failures may result in loss of command/control, telemetry blackout, or mission loss.
- **Interface boundaries** — space avionics interfaces with: GNC sensors and actuators (→ `140`); flight software hosted on OBC (→ `142`); power distribution subsystem (→ `133`); payload instruments; and ground segment via RF link.

## 3. Diagram — Space Avionics Scope Boundary

```mermaid
flowchart TD
    A["ECSS-E-ST-50C · ECSS-E-ST-40C<br/>Regulatory Anchors"]
    A --> B["Space Avionics<br/>Controlled Definition (001)"]
    B --> C["Applicability Boundary<br/>(OBC · DHU · buses · interfaces)"]
    B --> D["Controlled Vocabulary<br/>(EDAC · SEE · SpaceWire · PUS)"]
    B --> E["Safety Classification<br/>(mission-avionics critical)"]
    C --> F["002 — OBC & Data Handling"]
    C --> G["003 — TC/TM Interfaces"]
    E --> H["010 — Traceability & Governance"]
    style B fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `140-149` |
| Section | `04` — Aviónica y Control de Misión Espacial |
| Subsection | `141` — Aviónica Espacial |
| Subsubject | `001` — Space Avionics Controlled Definition |
| Primary Q-Division | Q-SPACE[^qdiv] |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Document | `001_Space-Avionics-Controlled-Definition.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |

## 5. References & Citations

[^ecssest50c]: **ECSS-E-ST-50C — Communications** — European standard for spacecraft on-board data handling.

[^ecssest40c]: **ECSS-E-ST-40C — Software Engineering** — Interface definition between avionics hardware and software.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-50C — Communications[^ecssest50c]
- ECSS-E-ST-40C — Software Engineering[^ecssest40c]
