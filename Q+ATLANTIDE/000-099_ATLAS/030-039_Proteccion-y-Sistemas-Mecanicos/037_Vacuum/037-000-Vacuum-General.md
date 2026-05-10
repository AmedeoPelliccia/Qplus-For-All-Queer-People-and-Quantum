---
document_id: "QATL-ATLAS-000099-ATLAS-030039-037-000"
title: "037-000 — Vacuum — General"
short_title: "ATA 37 General"
subsubject: "000"
subsubject_title: "Vacuum — General"
file_name: "037-000-Vacuum-General.md"
sns_reference: "037-00"
dmc_prefix: "DMC-AMPEL360E-EWTW-037-00"
ata_chapter: 37
aircraft: "AMPEL360e eWTW"
project: "Q+ATLANTIDE"
status: "DRAFT"
keywords:
  - "ATA 37"
  - "Vacuum"
  - "EVG"
  - "Electric Vacuum Generator"
  - "VWS"
  - "Vacuum Waste System"
  - "CS-25.1438"
  - "eWTW"
  - "no-gyro-vacuum"
  - "lavatory"
  - "VRV"
  - "SOV"
  - "EFV"
  - "CMC"
created: "2025-07-14"
revised: "2025-07-14"
revision: "0.1"
author: "Q+ATLANTIDE ATLAS Working Group"
---

# 037-000 — Vacuum — General
### AMPEL360e eWTW · ATA 37 · Q+ATLANTIDE ATLAS Scaffold

**Status:** <img src="https://img.shields.io/badge/DRAFT-yellow">  
**Revision:** 0.1 — 2025-07-14  
**Classification:** Q-AIR Primary

---

## §0 Hyperlink Policy

All cross-references within this document use relative Markdown links anchored to section headings within the Q+ATLANTIDE ATLAS repository. External regulatory references (CS-25, AMC) are cited by document identifier only; no live URLs are embedded because regulatory document URLs are subject to change without notice. Internal DMC cross-references follow the pattern `DMC-AMPEL360E-EWTW-037-XX-YYYY-A`. Traceability links to CSDB are maintained in §14. Where a parameter is not yet determined, the badge <img src="https://img.shields.io/badge/TBD-red"> is used inline.

---

## §1 Purpose

This document provides the general overview and system-level description of ATA Chapter 37 — Vacuum — as applied to the **AMPEL360e eWTW** (Electric Wide-body Twin-engine Widebody) aircraft. It establishes:

1. The rationale for the elimination of conventional vacuum-driven gyroscopic instruments on the eWTW.
2. The residual role of vacuum in the aircraft: the **Vacuum Waste System (VWS)** serving lavatory toilets.
3. The top-level architecture of the **Electric Vacuum Generator (EVG)** and its integration with ATA 38 (Water and Waste).
4. Certification basis under CS-25.1438 and related articles.
5. The document hierarchy for ATA 37, covering subsubjects 037-000 through 037-090.

This document is authoritative for system boundary definition and interfaces for all lower-level ATA 37 documents.

---

## §2 Applicability

| Item | Value |
|---|---|
| Aircraft Programme | AMPEL360e eWTW |
| Variant | All variants (unless noted) |
| ATA Chapter | 37 — Vacuum |
| Document Tier | Level 2 — System Description Document (SDD) |
| Effectivity | MSN 0001 onwards (TBD) |
| Preceding Document | QATL-ATLAS-000099-ATLAS-030039-037-000 Rev 0.0 (scaffold) |

This document applies to all systems that produce, distribute, regulate, or consume vacuum pressure aboard the AMPEL360e eWTW. It explicitly excludes vacuum associated with:
- Pneumatic actuation (ATA 36)
- Cabin pressurisation differential (ATA 21)
- Fuel venting suction (ATA 28)

---

## §3 System/Function Overview

### 3.1 Conventional Aircraft Context

In conventional transport aircraft, ATA 37 covers two primary vacuum applications:

1. **Vacuum-driven gyroscopic instruments** — attitude indicator, directional gyro, and turn coordinator powered by engine-driven vacuum pumps (typically 4–5 in Hg suction). These provide mechanical backup to pitot-static and electrical flight instruments.
2. **Vacuum autopilot servos** — used on older aircraft types for autopilot actuation where hydraulic/electric actuators were not fitted.
3. **Vacuum waste systems** — galley/lavatory suction toilets on newer-generation narrow/widebodies.

### 3.2 eWTW Vacuum Philosophy

The AMPEL360e eWTW departs from this convention in two critical respects:

| Conventional Use | eWTW Status | Reason |
|---|---|---|
| Vacuum gyroscopic instruments | **ELIMINATED** | ADIRU/IRS (ATA 34) provides all attitude and heading data digitally; no mechanical gyros fitted |
| Vacuum autopilot servos | **ELIMINATED** | Full fly-by-wire (FBW) with electric actuators (ATA 27); no vacuum-powered control surfaces |
| Vacuum waste system (toilets) | **RETAINED** | Primary and only use of ATA 37 on eWTW |

The elimination of vacuum gyroscopes removes a significant maintenance burden (pump replacement, filter changes, suction gauge calibration) and eliminates a failure mode that has historically caused spatial disorientation accidents when vacuum supply failed undetected.

### 3.3 Vacuum Waste System (VWS) Overview

The VWS uses differential pressure (cabin pressure above ambient inside waste lines) to transport waste from toilet bowls to waste tanks:

- **Electric Vacuum Generator (EVG):** motor-driven pump maintaining manifold vacuum of approximately −0.7 to −1.0 bar gauge <img src="https://img.shields.io/badge/TBD-red">
- **Vacuum manifold:** distributes vacuum to all toilet connections
- **Electric Flush Valve (EFV):** solenoid valve per toilet, initiates flush cycle
- **Non-Return Valve (NRV/check valve):** per toilet connection, prevents backflow
- **Vacuum Relief Valve (VRV):** limits maximum manifold vacuum
- **Shutoff Valve (SOV):** isolates EVG from manifold for maintenance
- **Waste tanks:** ATA 38 boundary (waste storage and ground servicing)

---

## §4 Scope

### 4.1 In-Scope

- All vacuum generation equipment (EVG units, motor controllers)
- Vacuum manifold and distribution lines from EVG outlet to toilet inlet NRVs
- Regulation and protection valves (VRV, SOV)
- Monitoring and diagnostics (vacuum transducers, CMC interface, ECAM messages)
- Interfaces with ATA 24 (electrical power), ATA 31 (indicating), ATA 38 (water and waste)

### 4.2 Out-of-Scope

- Waste tanks, waste servicing ports, and ground drain equipment (ATA 38)
- Toilet bowl assemblies and seat mechanisms (ATA 25)
- Cabin pressurisation (ATA 21)
- Avionics air supply (ATA 21)

### 4.3 Document Hierarchy

| Subsubject | Title | Status |
|---|---|---|
| 037-000 | Vacuum — General | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 037-010 | Vacuum Sources | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 037-020 | Vacuum Distribution | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 037-030 | Vacuum Regulation and Shutoff | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 037-040 | Vacuum Pumps, Ejectors, Valves, and Lines | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 037-050 | Vacuum Consumers and System Interfaces | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-060 | Vacuum System Indication and Warning | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-070 | Vacuum Ground Service and Test Interfaces | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-080 | Vacuum Monitoring, Diagnostics, and Control Interfaces | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-090 | S1000D/CSDB Mapping and Traceability | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §5 Architecture Description

### 5.1 System Architecture Summary

The ATA 37 Vacuum system on the eWTW consists of a single-purpose subsystem: the Vacuum Waste System (VWS). There is no multi-purpose vacuum bus serving instruments or autopilot.

```
[AC Bus (ATA 24)] ──────► [EVG Motor Controller]
                                    │
                              [EVG-1 (Primary)]
                              [EVG-2 (Standby)]
                                    │
                              [SOV (N/O solenoid)]
                                    │
                          [Vacuum Main Manifold]
                         /          │           \
                    [VRV]     [Pressure        [Branch lines]
                  (relief)    Transducer]      /     │     \
                                           [NRV-1] [NRV-2] [NRV-3]
                                              │       │       │
                                          [Toilet] [Toilet] [Toilet]
                                              └───────┴───────┘
                                                      │
                                              [Waste Tank (ATA 38)]
```

### 5.2 Redundancy Strategy

EVG redundancy: Two units (primary + standby). Automatic switchover on primary fault. <img src="https://img.shields.io/badge/TBD-red"> — exact switchover logic and timing TBD pending EVG supplier selection.

---

## §6 Functional Breakdown

| Subsubject | Function | Key Components | Status |
|---|---|---|---|
| 037-000 | System overview and general | All ATA 37 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 037-010 | Vacuum generation | EVG-1, EVG-2, motor controllers | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 037-020 | Vacuum distribution | Manifold, branch lines, NRVs | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 037-030 | Regulation and shutoff | VRV, SOV, EVG controller, transducer | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 037-040 | Pumps, ejectors, valves, lines | EVG, EFV, NRV, VRV, SOV, lines | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 037-050 | Consumers and interfaces | Toilets (ATA 25), waste tanks (ATA 38) | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-060 | Indication and warning | ECAM, CMC, crew alerts | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-070 | Ground service and test | Ground test port, drain panel | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-080 | Monitoring, diagnostics, control | AFDX, CMC, BITE | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-090 | S1000D/CSDB mapping | DMC assignments, data module codes | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §7 System Context Diagram

```mermaid
flowchart LR
    ATA24["ATA 24\nElectrical Power\n(AC Bus 115VAC)"]
    ATA31["ATA 31\nIndicating/Recording\n(ECAM/CMC)"]
    ATA38["ATA 38\nWater & Waste\n(Waste Tanks)"]
    ATA25["ATA 25\nEquipment & Furnishings\n(Toilet Bowls)"]

    EVG1["EVG-1\n(Primary)"]
    EVG2["EVG-2\n(Standby)"]
    SOV["SOV\n(Shutoff Valve)"]
    Manifold["Vacuum Manifold\n(Main)"]
    VRV["VRV\n(Relief Valve)"]
    PT["Pressure\nTransducer"]
    NRV1["NRV-1"]
    NRV2["NRV-2"]
    NRV3["NRV-3"]
    T1["Toilet-1"]
    T2["Toilet-2"]
    T3["Toilet-3+"]
    CMC["CMC\n(AFDX)"]

    ATA24 -->|"115VAC"| EVG1
    ATA24 -->|"115VAC"| EVG2
    EVG1 --> SOV
    EVG2 --> SOV
    SOV --> Manifold
    Manifold --> VRV
    Manifold --> PT
    PT -->|"vacuum signal"| CMC
    CMC --> ATA31
    Manifold --> NRV1 --> T1 --> ATA38
    Manifold --> NRV2 --> T2 --> ATA38
    Manifold --> NRV3 --> T3 --> ATA38
    ATA25 -.->|"toilet bowl\nassembly"| T1
    ATA25 -.->|"toilet bowl\nassembly"| T2
    ATA25 -.->|"toilet bowl\nassembly"| T3
```

---

## §8 Internal Functional Architecture

```mermaid
flowchart TB
    PWR["Power ON\n(AC Bus Available)"]
    EVGEN["EVG Enable\n(Controller Command)"]
    SPINUP["EVG Spins Up\n(Motor Speed Ramp)"]
    VACBLD["Vacuum Builds\n(Manifold)"]
    VACCHK{"Vacuum at\nSet-Point?\n(~−0.7 bar TBD)"}
    CMCFLT["CMC Fault\n(LOW VAC warning)"]
    HOLD["Steady-State Hold\n(EVG cycles on/off)"]
    FLUSHD["Flush Demand\n(Passenger presses button)"]
    EFVOPEN["EFV Opens\n(1.5s TBD)"]
    WASTE["Waste Flows\n(differential pressure)"]
    TANK["Waste Tank\n(ATA 38)"]
    EFVCLOSE["EFV Closes\n(cycle complete)"]
    READY["System Ready\nfor next flush"]

    PWR --> EVGEN --> SPINUP --> VACBLD --> VACCHK
    VACCHK -- "Yes" --> HOLD
    VACCHK -- "No" --> CMCFLT
    CMCFLT --> EVGEN
    HOLD --> FLUSHD
    FLUSHD --> EFVOPEN --> WASTE --> TANK
    TANK --> EFVCLOSE --> READY --> HOLD
```

---

## §9 Lifecycle Traceability

```mermaid
flowchart LR
    REQ["Requirements\n(CS-25.1438,\nCS-25.1301/1309)"]
    SRD["System Requirements\nDocument (SRD)"]
    SDD["System Description\nDocument (SDD)\n037-000"]
    ICD["Interface Control\nDocuments (ICDs)\nATA 24/31/38"]
    COMP["Component Specs\n(EVG, EFV, VRV, SOV)"]
    VTP["V&T Plan\n(§17)"]
    TEST["Test Reports\n(pull-down, leak,\nflush cycle)"]
    CERT["CS-25 Certification\n(CS-25.1438)"]
    EIS["Entry Into Service"]
    MAINT["Maintenance\n(AMM/CMM)"]

    REQ --> SRD --> SDD --> ICD --> COMP
    SDD --> VTP --> TEST --> CERT --> EIS --> MAINT
```

---

## §10 Interfaces

| Interface | ATA Chapter | Direction | Signal/Medium | Notes |
|---|---|---|---|---|
| Electrical power supply | ATA 24 | In | 115 VAC <img src="https://img.shields.io/badge/TBD-red"> | Powers EVG motor controllers |
| Ground electrical power | ATA 24 | In | 115 VAC GPU | EVG operable on ground power |
| Waste tanks | ATA 38 | Out | Waste (liquid/solid) | Tanks receive toilet waste; serviced per ATA 38 |
| Toilet bowl assemblies | ATA 25 | Bi | Mechanical, electrical | EFV flush valve integrated with toilet; flush button signal |
| ECAM/SDAC | ATA 31 | Out | AFDX | Vacuum system status pages, crew alerts |
| CMC/OMS | ATA 45 | Bi | AFDX | Fault codes, maintenance data, BITE |
| Odour filter vent | ATA 21 | Out | Air (filtered) | Tank vent air exits via odour filter to cabin/ambient <img src="https://img.shields.io/badge/TBD-red"> |
| Freeze protection | ATA 30 | In | Heat (electric trace) | Waste line freeze protection <img src="https://img.shields.io/badge/TBD-red"> |

---

## §11 Operating Modes

| Mode | Description | EVG State | SOV | EFV |
|---|---|---|---|---|
| Normal — In-flight | EVG maintains manifold vacuum; toilets available | Running (cycling) | Open | Closed (ready) |
| Normal — Ground | EVG on ground power; toilets available for boarding/deplaning | Running | Open | Closed (ready) |
| Flush Active | Passenger flush cycle in progress | Running | Open | Open (1.5 s TBD) |
| Standby (EVG-2 Active) | EVG-1 fault; EVG-2 auto-started | EVG-2 running | Open | Closed (ready) |
| Maintenance Isolation | SOV closed; EVG off; ground drain open | Off | Closed | Closed |
| Total Vacuum Loss | Both EVGs failed; no flush capability | Off | Closed | Locked closed |
| Ground Drain | Waste tanks drained via ATA 38 service panel | Off | Closed | Closed |

---

## §12 Monitoring and Diagnostics

| Parameter | Sensor | Threshold | CMC Action | ECAM Message |
|---|---|---|---|---|
| Manifold vacuum | Pressure transducer | < −0.5 bar (low) <img src="https://img.shields.io/badge/TBD-red"> | Fault log, EVG-2 start | VAC SYS LO PRESS |
| Manifold vacuum | Pressure transducer | > −1.2 bar (over-vacuum) | Fault log, VRV check advisory | VAC SYS HI PRESS |
| EVG-1 motor current | Motor controller | Over-current / stall | Fault log, EVG-2 start | VAC GEN 1 FAULT |
| EVG-2 motor current | Motor controller | Over-current / stall | Fault log, crew alert | VAC GEN 2 FAULT |
| SOV position | Position sensor | Disagree | Fault log | VAC SOV FAULT |
| EFV flush cycle time | Timer | > 5 s (stuck open) | Fault log, EFV close command | LAVATORY FAULT |
| Waste tank level | Float/ultrasonic (ATA 38) | Full | Advisory via ATA 38 | WASTE TANK FULL |

---

## §13 Maintenance Concept

| Task | Interval | Skill Level | Reference |
|---|---|---|---|
| EVG filter inspection/replacement | <img src="https://img.shields.io/badge/TBD-red"> | L2 Avionics/Mechanical | AMM 37-10-XX |
| EVG oil replenishment (if oil-sealed) | <img src="https://img.shields.io/badge/TBD-red"> | L2 | AMM 37-10-XX |
| NRV check valve functional test | Annual / C-check | L2 | AMM 37-20-XX |
| VRV pop test | Annual / C-check | L2 | AMM 37-30-XX |
| SOV open/close function test | Annual / C-check | L2 | AMM 37-30-XX |
| Vacuum line visual inspection | Annual | L1 | AMM 37-20-XX |
| Vacuum decay leak test | C-check | L2 | AMM 37-40-XX |
| Odour filter replacement | <img src="https://img.shields.io/badge/TBD-red"> | L1 | AMM 38-XX-XX |
| EFV flush cycle test | A-check | L1 | AMM 37-40-XX |
| CMC fault log review | As required | L1 | AMM 45-XX-XX |

---

## §14 S1000D/CSDB Mapping

| DMC Code | Title | Infocode |
|---|---|---|
| DMC-AMPEL360E-EWTW-037-00-00-00A-040A-D | ATA 37 General Description | 040 (Description) |
| DMC-AMPEL360E-EWTW-037-00-00-00A-200A-D | ATA 37 Maintenance Practices | 200 (Maintenance) |
| DMC-AMPEL360E-EWTW-037-00-00-00A-520A-D | ATA 37 Fault Isolation | 520 (Fault Isolation) |
| DMC-AMPEL360E-EWTW-037-10-00-00A-040A-D | Vacuum Sources Description | 040 |
| DMC-AMPEL360E-EWTW-037-20-00-00A-040A-D | Vacuum Distribution Description | 040 |
| DMC-AMPEL360E-EWTW-037-30-00-00A-040A-D | Vacuum Regulation Description | 040 |
| DMC-AMPEL360E-EWTW-037-40-00-00A-040A-D | Pumps, Valves, Lines Description | 040 |

CSDB publication target: <img src="https://img.shields.io/badge/TBD-red">

---

## §15 Footprints

| Component | Location | Volume (L) | Mass (kg) | Notes |
|---|---|---|---|---|
| EVG-1 | Aft service compartment <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | Primary unit |
| EVG-2 | Aft service compartment <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | Standby unit |
| Vacuum manifold | Bilge / lower sidewall <img src="https://img.shields.io/badge/TBD-red"> | — | <img src="https://img.shields.io/badge/TBD-red"> | Routing TBD |
| SOV | Adjacent to EVG outlet | — | <img src="https://img.shields.io/badge/TBD-red"> | |
| VRV | Manifold tee | — | <img src="https://img.shields.io/badge/TBD-red"> | |
| Total ATA 37 estimated mass | — | — | <img src="https://img.shields.io/badge/TBD-red"> | |

---

## §16 Safety and Certification

### 16.1 Certification Basis

| Regulation | Topic | Applicability |
|---|---|---|
| CS-25.1438 | Pressurisation and pneumatic systems | Applies to VWS vacuum system |
| CS-25.1301 | Function and installation | All ATA 37 equipment |
| CS-25.1309 | Equipment, systems and installations | EVG, EFV, VRV, SOV safety assessment |
| AMC 25.831 | Ventilation (odour/contamination) | Waste tank vent and odour filter |
| CS-25.869 | Fire protection (electrical equipment) | EVG motor fire risk |

### 16.2 Eliminated Hazards (vs. Conventional ATA 37)

| Conventional Hazard | eWTW Status | Reason |
|---|---|---|
| Vacuum gyro failure → spatial disorientation | **ELIMINATED** | No vacuum gyros; ADIRU/IRS provides attitude data (ATA 34) |
| Vacuum pump oil contamination of instruments | **ELIMINATED** | No instrument vacuum supply |
| Engine-driven vacuum pump seizure | **ELIMINATED** | No engine-driven vacuum pumps |

### 16.3 Failure Effects (VWS Specific)

| Failure | Effect | Severity | Mitigation |
|---|---|---|---|
| EVG-1 failure | Switchover to EVG-2; no flush loss | Minor | Auto-switchover + CMC alert |
| EVG-1 + EVG-2 failure | No toilet flushing; passenger discomfort | Major (non-hazardous) | Crew advisory; dispatch with MEL |
| SOV stuck closed | No vacuum to manifold | Major | SOV position monitoring; bypass TBD |
| SOV stuck open | Cannot isolate for maintenance | Minor | Manual override TBD |
| VRV fails to relieve | Over-vacuum; potential line damage | Hazardous | Secondary protection <img src="https://img.shields.io/badge/TBD-red"> |
| EFV stuck open | Continuous waste flow; tank over-capacity | Major | Auto-close timer, CMC fault |
| Line rupture | Vacuum loss; odour ingress | Major | SOV close; odour filter |

---

## §17 Verification and Validation

| Test | Method | Acceptance Criteria | Status |
|---|---|---|---|
| EVG vacuum pull-down test | Rig test — sealed manifold | Achieve set-point vacuum in < X seconds TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Manifold vacuum accuracy | Transducer calibration bench test | ±0.02 bar vs. reference gauge | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| VRV pop test | Rig test — apply increasing vacuum | VRV opens at set-point ±5% TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| SOV open/close functional test | Ground test | Operates within < 2 s, position confirmed | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| EFV flush cycle test | Ground test (water substitute) | Cycle completes within 1.5 s TBD; no leakage | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Vacuum decay leak test | System test — pressurised decay | < X mbar/min decay TBD at set vacuum | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| CMC fault flag test | Fault injection simulation | All defined fault codes logged correctly | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Fill-level sensor (ATA 38) | Ground test — fill to threshold | Sensor triggers advisory at correct fill level | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Auto-switchover EVG-1 → EVG-2 | Fault injection (EVG-1 shutdown) | EVG-2 starts within X seconds TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §18 Glossary

| Term | Definition |
|---|---|
| ADIRU | Air Data Inertial Reference Unit — digital replacement for vacuum-driven gyros |
| ATA 37 | Air Transport Association chapter covering vacuum systems |
| CMC | Central Maintenance Computer |
| CS-25.1438 | EASA CS-25 airworthiness standard for pressurisation and pneumatic systems |
| ECAM | Electronic Centralised Aircraft Monitor |
| EFV | Electric Flush Valve — solenoid valve initiating toilet flush cycle |
| EVG | Electric Vacuum Generator — motor-driven vacuum pump |
| FBW | Fly-By-Wire — electric flight control system eliminating need for vacuum autopilot servos |
| Freeze protection | Heating of waste lines to prevent freezing at altitude (ATA 30 interface) |
| Gyroscopic instruments | Attitude/heading instruments driven by vacuum suction — **eliminated on eWTW** |
| IRS | Inertial Reference System |
| Manifold | Common distribution tube connecting EVG to all toilet branch lines |
| MEL | Minimum Equipment List |
| NRV | Non-Return Valve (check valve) — prevents backflow from waste line to manifold |
| Odour filter | Activated-carbon filter on waste tank vent preventing odour release to cabin |
| PTFE | Polytetrafluoroethylene — chemically resistant lining for vacuum waste lines |
| SOV | Shutoff Valve — solenoid valve isolating EVG from manifold |
| Vacuum transducer | Pressure sensor measuring manifold vacuum; feeds EVG controller and CMC |
| VRV | Vacuum Relief Valve — limits maximum manifold vacuum to prevent over-pressure damage |
| VWS | Vacuum Waste System |
| Waste tank | Containment vessel for toilet waste; ATA 38 boundary |

---

## §19 Citations

1. EASA CS-25 Amendment 27 — Certification Specifications for Large Aeroplanes, Book 1, CS-25.1438 "Pressurisation and Pneumatic Systems."
2. EASA CS-25 Amendment 27 — CS-25.1301 "Function and Installation."
3. EASA CS-25 Amendment 27 — CS-25.1309 "Equipment, Systems and Installations."
4. EASA AMC 25.831 — Acceptable Means of Compliance for Ventilation.
5. ATA iSpec 2200 Chapter 37 — Vacuum (reference chapter definition).
6. S1000D Issue 5.0 — International Specification for Technical Publications.
7. AMPEL360e eWTW System Requirements Document (SRD-eWTW-037) — <img src="https://img.shields.io/badge/TBD-red">

---

## §20 References

| Document | Description | Status |
|---|---|---|
| QATL-ATLAS-000099-ATLAS-030039-037-010 | Vacuum Sources | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| QATL-ATLAS-000099-ATLAS-030039-037-020 | Vacuum Distribution | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| QATL-ATLAS-000099-ATLAS-030039-037-030 | Vacuum Regulation and Shutoff | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| QATL-ATLAS-000099-ATLAS-030039-037-040 | Vacuum Pumps, Ejectors, Valves, and Lines | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| QATL-ATLAS-000099-ATLAS-030039-038-000 | Water and Waste — General (ATA 38) | <img src="https://img.shields.io/badge/TBD-red"> |
| QATL-ATLAS-000099-ATLAS-030039-024-000 | Electrical Power — General (ATA 24) | <img src="https://img.shields.io/badge/TBD-red"> |
| QATL-ATLAS-000099-ATLAS-030039-034-000 | Navigation — General (ATA 34, ADIRU) | <img src="https://img.shields.io/badge/TBD-red"> |
| AMM-AMPEL360E-037 | Aircraft Maintenance Manual Chapter 37 | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §21 Open Issues

| OI ID | Title | Status | Owner |
|---|---|---|---|
| OI-037-001 | EVG count and sizing (qty, rated vacuum, motor power) | <img src="https://img.shields.io/badge/TBD-red"> | Systems Engineering |
| OI-037-002 | Dry-flush vs. vacuum toilet decision | <img src="https://img.shields.io/badge/TBD-red"> | Cabin Design / Marketing |
| OI-037-003 | Waste tank material and capacity (CFRP vs. stainless steel) | <img src="https://img.shields.io/badge/TBD-red"> | Structures / ATA 38 |
| OI-037-004 | Vacuum line routing through composite fuselage (penetration sealing) | <img src="https://img.shields.io/badge/TBD-red"> | Stress / Systems |
| OI-037-005 | Freeze protection for waste lines (altitude, electric trace heating) | <img src="https://img.shields.io/badge/TBD-red"> | Thermal / ATA 30 |
| OI-037-006 | Odour filter certification and replacement interval | <img src="https://img.shields.io/badge/TBD-red"> | Cabin Systems |
| OI-037-007 | Ground waste drain panel location | <img src="https://img.shields.io/badge/TBD-red"> | Ground Ops / ATA 38 |

---

## §22 Change Log

| Revision | Date | Author | Description |
|---|---|---|---|
| 0.0 | 2025-07-01 | Q+ATLANTIDE WG | Initial scaffold created |
| 0.1 | 2025-07-14 | Q+ATLANTIDE WG | Full content draft — all §0–§22 populated |
