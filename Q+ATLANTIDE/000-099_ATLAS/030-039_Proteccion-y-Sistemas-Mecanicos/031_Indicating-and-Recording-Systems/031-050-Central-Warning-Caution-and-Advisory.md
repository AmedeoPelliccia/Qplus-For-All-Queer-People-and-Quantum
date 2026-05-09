---
document_id: QATL-ATLAS-1000-ATLAS-030-039-03-031-050-CENTRAL-WARNING-CAUTION-AND-ADVISORY
title: "ATLAS 030-039 · 03.031.050 — Central Warning, Caution and Advisory"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../../README.md
parent_section_doc: ../../README.md
parent_subsection_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "030-039"
section: "03"
section_title: "Protección & Sistemas Mecánicos"
subsection: "031"
subsection_title: "Indicating and Recording Systems"
subsubject: "050"
subsubject_title: "Central Warning, Caution and Advisory"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-AIR, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 030-039 · Section 03 · Subsection 031 · 050 — Central Warning, Caution and Advisory

## 1. Purpose

Covers the Master Warning/Caution (MW/MC) system, Electronic Centralized Aircraft Monitor (ECAM) or equivalent EICAS crew-alerting logic, and aural/visual annunciation architecture.

## 2. Scope

- Warning (red), caution (amber), and advisory (white/cyan) alert categories.
- ECAM/EICAS alert messages, synoptic pages, and inhibit logic.
- Aural tone generation and flight-phase inhibit tables.
- Integration with other systems' BITE outputs and fault consolidation.
- Not in scope: engine monitoring display content (ATA 77) or autopilot alerts (ATA 22).

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `030-039` |
| Section | `03` — Protección & Sistemas Mecánicos |
| Subsection | `031` — Indicating and Recording Systems |
| Subsubject | `050` — Central Warning, Caution and Advisory |
| Primary Q-Division | Q-MECHANICS[^qdiv] |
| Support Q-Divisions | Q-AIR, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/031_Indicating-and-Recording-Systems/` |
| Document | `031-050-Central-Warning-Caution-and-Advisory.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent section | [`../../README.md`](../../README.md) |
| Parent architecture | [`../../../README.md`](../../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md) |

> **Footprint Notes**
> - **Architecture**: `ATLAS` is the controlled term for the Aircraft Top-Level Architecture Schema/System within the Q+ATLANTIDE-1000 register.
> - **Primary Q-Division**: Q-MECHANICS holds technical authority for mechanical and electro-mechanical aircraft systems.
> - **Support Q-Divisions**: Q-AIR provides systems integration oversight; Q-STRUCTURES provides structural interface authority.
> - **Governance class**: `baseline` documents are subject to formal change control under the Q+ATLANTIDE Configuration Management Plan.
> - **ORB support**: ORB-PMO coordinates programme management; ORB-LEG provides regulatory and certification support.


## 4. Interfaces Diagram

```mermaid
flowchart TB
    BASELINE["Q+ATLANTIDE Baseline"]:::baseline
    ATLAS["ATLAS-1000 · 000–099"]:::atlas
    SEC["Section 03 · 030-039<br/>Protección &amp; Sistemas Mecánicos"]:::section
    SUB["031 — Indicating and Recording Sys…<br/>(ATA 31)"]:::subsection
    THIS["031-050<br/>Central Warning Caution and Ad…"]:::document

    BASELINE --> ATLAS --> SEC --> SUB --> THIS

    QPRIM["Q-MECHANICS[^qdiv]<br/>(primary authority)"]:::qdiv
    QSUPP["Q-AIR · Q-STRUCTURES[^qdiv]<br/>(support)"]:::qdiv
    ORB["ORB-PMO · ORB-LEG<br/>(enterprise support)"]:::orb

    THIS --> QPRIM
    THIS -.-> QSUPP
    THIS -.-> ORB

    classDef baseline fill:#1f3a93,stroke:#0b1d4a,color:#fff
    classDef atlas fill:#154360,stroke:#0b1d4a,color:#fff
    classDef section fill:#2c82c9,stroke:#0b1d4a,color:#fff
    classDef subsection fill:#85c1e9,stroke:#2c82c9,color:#0b1d4a
    classDef document fill:#ffd700,stroke:#b8860b,color:#000
    classDef qdiv fill:#f6e6ff,stroke:#7d3c98,color:#3b1f4d
    classDef orb fill:#e9f7ef,stroke:#1e8449,color:#145a32
```

## 5. References & Citation Map

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../../organization/Q+ATLANTIDE.md#4-notes).

### Citation & Traceability Map

| Ref | Target Document | Relationship | Scope |
|---|---|---|---|
| [^baseline] | [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md) | Normative baseline | ATLAS-1000 register authority |
| [^qdiv] | [`organization/Q-Divisions/`](../../../../../organization/Q-Divisions/) | Technical authority | Q-Division assignment |
| [^gov] | Q+ATLANTIDE governance class definition | Governance class | Change-management classification |
| [^n001] | [`organization/Q+ATLANTIDE.md §4`](../../../../../organization/Q+ATLANTIDE.md#4-notes) | Taxonomy note | Ecosystem scope clarification |

---

## Glossary

### Common Terms & Acronyms

| Term / Acronym | Expansion | Definition |
|---|---|---|
| **ATA** | Air Transport Association | Industry body that publishes iSpec 2200 (formerly ATA Spec. 100), the standard chapter-numbering scheme for aircraft systems documentation. |
| **ATLAS** | Aircraft Top Level Architecture Schema/System | The controlled architecture taxonomy and documentation framework within the Q+ATLANTIDE-1000 register; governs chapters 000–099. |
| **baseline** | — | A formally approved version of a document or configuration item, subject to formal change control, forming the reference for further development or maintenance. |
| **CSDB** | Common Source Data Base | The central repository defined by S1000D for storing, managing, and exchanging Data Modules and Publication Modules. |
| **DMC** | Data Module Code | Unique alphanumeric identifier for a single S1000D Data Module, encoding model identification, system/sub-system, information code, and variant. |
| **governance\_class** | — | Classification field in Q+ATLANTIDE YAML frontmatter that indicates the change-control regime (`baseline`, `programme-controlled`, `legacy-deprecated`, etc.). |
| **NNN** | — | Three-digit ATA-SNS sub-subject code (e.g., `010`, `020`, …, `090`) used as the local identifier within a subsection folder. |
| **ORB** | Operations Review Board | Enterprise-level governance body within the Q+ATLANTIDE organisational structure, responsible for cross-domain oversight and authorisation. |
| **ORB-LEG** | ORB — Legal & Regulatory | ORB function providing legal compliance, regulatory (EASA/FAA) liaison, and certification boundary advisory services. |
| **ORB-PMO** | ORB — Programme Management Office | ORB function providing programme scheduling, resource, and milestone control across all Q-Division work-packages. |
| **Q+ATLANTIDE** | — | The master controlled documentation baseline and taxonomy ecosystem for the ATLAS-1000 architecture register; versioned governance reference for all architecture bands (000–999). |
| **Q-AIR** | Q-Division — Air Systems | Technical-authority Q-Division responsible for aerodynamics, air-data systems, and systems integration oversight. |
| **Q-DATAGOV** | Q-Division — Data Governance | Technical-authority Q-Division responsible for data standards, traceability, and CSDB publication governance. |
| **Q-GREENTECH** | Q-Division — Green Technologies | Technical-authority Q-Division responsible for sustainable propulsion, energy, and environmental compliance. |
| **Q-GROUND** | Q-Division — Ground Systems | Technical-authority Q-Division responsible for ground handling, servicing interfaces, and airport compatibility. |
| **Q-INDUSTRY** | Q-Division — Industry & Supply Chain | Technical-authority Q-Division responsible for industrial producibility, supplier qualification, and manufacturing interfaces. |
| **Q-MECHANICS** | Q-Division — Mechanical Systems | Technical-authority Q-Division responsible for mechanical and electro-mechanical aircraft systems; primary authority for ATLAS sections 030–039. |
| **Q-STRUCTURES** | Q-Division — Structures | Technical-authority Q-Division responsible for structural interfaces, loads, and airframe integrity. |
| **S1000D** | — | International specification (ASD/AIA/ATA) for the production and procurement of technical publications; defines the Data Module (DM) paradigm and CSDB architecture. |
| **SNS** | Standard Numbering System | The ATA/S1000D hierarchical chapter-section-subject numbering scheme mapping physical/functional aircraft systems to a standardised code space. |
| **YAML** | YAML Ain't Markup Language | Human-readable data-serialisation language used for document frontmatter (metadata header blocks) throughout the Q+ATLANTIDE baseline. |

### Domain-Specific Terms — ATA 31 Indicating and Recording Systems

| Term / Acronym | Expansion | Definition |
|---|---|---|
| **ACARS** | Aircraft Communications Addressing and Reporting System | Digital datalink for air/ground communications; feeds data to ACMS. |
| **ACMS** | Aircraft Condition Monitoring System | Onboard system that acquires, processes, and stores flight parameter data for trend monitoring and predictive maintenance. |
| **CVR** | Cockpit Voice Recorder | Crash-survivable recorder capturing flight-deck audio (crew, ATC, ambient); mandatory under ICAO Annex 6. |
| **DAR** | Digital ACMS Recorder / Digital AIDS Recorder | Solid-state high-speed recording unit collecting FDR-class parameters at high sample rates. |
| **EIS** | Engine Indicating System | Integrated display suite presenting engine parameters (N1, N2, EGT, FF, oil) on the flight deck. |
| **EFIS** | Electronic Flight Instrument System | Cathode-ray-tube or LCD-based flight instrument suite comprising PFD and ND; replaces electromechanical instruments. |
| **EICAS** | Engine Indication and Crew Alerting System | Boeing-type integrated display providing engine parameters and system alerts on the flight deck centre panel. |
| **ECAM** | Electronic Centralised Aircraft Monitor | Airbus-type monitoring and display system providing systems synoptic pages, engine data, and crew warnings. |
| **FDR** | Flight Data Recorder | Crash-survivable recorder that stores flight parameters (position, attitude, control inputs) for accident investigation. |
| **FWC** | Flight Warning Computer | Core processor for ECAM/EICAS that evaluates sensor inputs and generates crew alert messages. |
| **GPWS** | Ground Proximity Warning System | Advisory system alerting crew to terrain proximity; legacy precursor to TAWS (Mode 1–5 envelope protection). |
| **ICAO** | International Civil Aviation Organisation | UN specialised agency establishing international standards and recommended practices for civil aviation. |
| **MCP** | Mode Control Panel | Glareshield-mounted panel on which pilots select autoflight modes, target speed, altitude, and heading. |
| **ND** | Navigation Display | Crew display unit showing horizontal situation, flight plan route, terrain, weather, and traffic overlays. |
| **PFD** | Primary Flight Display | Crew display unit consolidating attitude, airspeed, altitude, vertical speed, and ILS deviation data. |
| **QAR** | Quick Access Recorder | Removable solid-state flight data recorder providing easy, rapid access to FDR-class data for airline maintenance analysis. |
| **WEU** | Warning Electronic Unit | Hardware unit generating discrete audio/visual warnings (Master Warning, Master Caution, chimes) based on FWC output. |
