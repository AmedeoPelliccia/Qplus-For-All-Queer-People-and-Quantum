---
document_id: QATL-ATLAS-1000-ATLAS-030-039-03-034-070-WEATHER-RADAR-AND-NAVIGATION-SENSOR-FUSION
title: "ATLAS 030-039 · 03.034.070 — Weather Radar and Navigation Sensor Fusion"
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
subsection: "034"
subsection_title: "Navigation"
subsubject: "070"
subsubject_title: "Weather Radar and Navigation Sensor Fusion"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-AIR, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 030-039 · Section 03 · Subsection 034 · 070 — Weather Radar and Navigation Sensor Fusion

## 1. Purpose

Documents airborne weather radar (predictive windshear, turbulence, precipitation), radar altimeter, multi-sensor navigation fusion (IRS+GPS+VOR+DME), and FMS position selection logic.

## 2. Scope

- Weather radar antenna, transceiver, scan patterns, and tilt control.
- Predictive Windshear System (PWS) detection and alert criteria.
- Radar altimeter (RALT) antenna installation, data bus, and alert thresholds.
- Multi-sensor navigation filter: IRS/GPS/DME-DME/VOR-DME position computation.
- FMS navigation sensor priority and integrity voting.
- Not in scope: weather display on ND/MFD (ATA 31) or pilot advisory for turbulence avoidance (procedure).

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `030-039` |
| Section | `03` — Protección & Sistemas Mecánicos |
| Subsection | `034` — Navigation |
| Subsubject | `070` — Weather Radar and Navigation Sensor Fusion |
| Primary Q-Division | Q-MECHANICS[^qdiv] |
| Support Q-Divisions | Q-AIR, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/034_Navigation/` |
| Document | `034-070-Weather-Radar-and-Navigation-Sensor-Fusion.md` (this file) |
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
    SUB["034 — Navigation<br/>(ATA 34)"]:::subsection
    THIS["034-070<br/>Weather Radar and Navigation S…"]:::document

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

### Domain-Specific Terms — ATA 34 Navigation

| Term / Acronym | Expansion | Definition |
|---|---|---|
| **ADC** | Air Data Computer | Computer converting pitot-static pressures and total air temperature into calibrated airspeed, Mach, altitude, and vertical speed. |
| **ADIRS** | Air Data and Inertial Reference System | Integrated unit combining ADC and IRS functions; standard on modern commercial transports. |
| **ADSB** | Automatic Dependent Surveillance – Broadcast | Surveillance technology in which aircraft broadcast GPS-derived position, enabling ground stations and other aircraft to track traffic without active radar. |
| **DME** | Distance Measuring Equipment | VHF/UHF radio navigation aid providing slant-range distance from the aircraft to a ground transponder. |
| **EGPWS** | Enhanced Ground Proximity Warning System | TAWS variant (Honeywell brand name) adding terrain database look-ahead to the classic GPWS envelope-protection modes. |
| **GNSS** | Global Navigation Satellite System | Generic term for satellite constellations providing position, navigation, and timing (GPS, GLONASS, Galileo, BeiDou). |
| **GPS** | Global Positioning System | US DoD satellite constellation providing worldwide navigation signals; primary civilian GNSS for commercial aviation. |
| **ILS** | Instrument Landing System | Ground-based radio navigation aid providing lateral (localiser) and vertical (glidepath) guidance for precision approach to a runway. |
| **IRS** | Inertial Reference System | Navigation system computing position, velocity, and attitude from accelerometer and gyroscope data without external reference. |
| **IRU** | Inertial Reference Unit | Hardware sensor assembly (gyros + accelerometers) within an ADIRS or IRS. |
| **MCDU** | Multipurpose Control and Display Unit | Crew interface for entering and monitoring FMS navigation data, performance parameters, and datalink messages. |
| **MMR** | Multi-Mode Receiver | Integrated receiver processing ILS, GPS/GNSS, MLS, and GLS signals for approach and navigation guidance. |
| **RNP** | Required Navigation Performance | Performance-based navigation standard specifying the accuracy and onboard monitoring capability required for a route or procedure. |
| **SBAS** | Satellite-Based Augmentation System | Wide-area augmentation of GNSS providing improved accuracy and integrity (e.g., WAAS in North America, EGNOS in Europe). |
| **TAWS** | Terrain Awareness and Warning System | Onboard terrain protection system using GPS position and terrain databases to provide look-ahead warnings. |
| **TCAS** | Traffic Collision Avoidance System | Onboard surveillance system that interrogates transponders of nearby aircraft and issues Resolution Advisories (RAs) to avoid collisions. |
| **VOR** | VHF Omnidirectional Range | Ground-based VHF radio navigation beacon providing magnetic bearing information to equipped aircraft. |
| **WXR** | Weather Radar | Onboard airborne weather detection radar providing precipitation, turbulence, and wind-shear detection. |
