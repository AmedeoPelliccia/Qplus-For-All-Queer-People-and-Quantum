---
document_id: "QATL-ATLAS-000099-ATLAS-030039-039-030"
title: "039-030 — Relay, Contactor, and Power Distribution Panels"
short_title: "ATA 39 PDUs and Contactors"
subsubject: "030"
subsubject_title: "Relay, Contactor, and Power Distribution Panels"
file_name: "039-030-Relay-Contactor-and-Power-Distribution-Panels.md"
sns_reference: "039-30"
dmc_prefix: "DMC-AMPEL360E-EWTW-039-30"
programme: "AMPEL360e Wide Tube-and-Wing Family"
programme_link: "../../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/"
short_code: "eWTW"
register: "Q+ATLANTIDE"
register_link: "../../../../../Q+ATLANTIDE/"
architecture_band: "000-099_ATLAS"
architecture_band_link: "../../../"
architecture_band_title: "New Commercial Aircraft Architectures"
code_range: "030-039_Proteccion-y-Sistemas-Mecanicos"
code_range_link: "../../"
code_range_title: "Protección & Sistemas Mecánicos"
node_code: "039"
node_title: "Electrical/Electronic Panels and Multipurpose Components"
node_link: "./"
parent_path: "Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/039_Electrical-Electronic-Panels-and-Multipurpose-Components/"
parent_path_link: "./"
ata_reference: "ATA 39"
ata_reference_link: "#20-references"
s1000d_applicability: "S1000D-CSDB-compatible"
s1000d_link: "https://s1000d.org/"
domain: "A-Aerospace"
domain_link: "../../../../../IDEALE-ESG/A-Aerospace/"
primary_q_division: "Q-AIR"
primary_q_division_link: "../../../../../Q-Divisions/Q-AIR/"
support_q_divisions:
  - name: "Q-MECHANICS"
    link: "../../../../../Q-Divisions/Q-MECHANICS/"
  - name: "Q-DATAGOV"
    link: "../../../../../Q-Divisions/Q-DATAGOV/"
  - name: "Q-HPC"
    link: "../../../../../Q-Divisions/Q-HPC/"
  - name: "Q-GROUND"
    link: "../../../../../Q-Divisions/Q-GROUND/"
  - name: "Q-INDUSTRY"
    link: "../../../../../Q-Divisions/Q-INDUSTRY/"
orb_functions:
  - name: "ORB-PMO"
    link: "../../../../../ORB-Functions/ORB-PMO/"
  - name: "ORB-LEG"
    link: "../../../../../ORB-Functions/ORB-LEG/"
classification: "open-technical-scaffold"
status: "programme-controlled-scaffold"
revision: "0.1.0"
created: "2026-05-10"
updated: "2026-05-10"
authoring_mode: "deterministic-technical-publication"
review_status: "to-be-reviewed-by-system-expert"
lifecycle_phase:
  - code: "LC02"
    title: "Requirements Definition"
  - code: "LC03"
    title: "Architecture Definition"
  - code: "LC05"
    title: "Detailed Design"
  - code: "LC06"
    title: "Verification Planning"
  - code: "LC10"
    title: "Certification / Approval"
  - code: "LC11"
    title: "Operation"
  - code: "LC12"
    title: "Maintenance / Support"
traceability:
  atlas_node: "039_Electrical-Electronic-Panels-and-Multipurpose-Components"
  atlas_node_link: "./"
  parent_branch: "030-039_Proteccion-y-Sistemas-Mecanicos"
  parent_branch_link: "../../"
  csdb_path: "TBD"
  evidence_status: "draft"
  brex_status: "not-yet-validated"
  dmrl_status: "not-yet-frozen"
keywords:
  - "Q+ATLANTIDE"
  - "ATLAS"
  - "AMPEL360e"
  - "S1000D"
  - "ATA 39"
  - "PDU"
  - "Power Distribution Unit"
  - "SSPC"
  - "Solid-State Power Controller"
  - "BTC"
  - "Bus Tie Contactor"
  - "relay"
  - "contactor"
  - "load shedding"
  - "270 VDC"
---

# 039-030 — Relay, Contactor, and Power Distribution Panels
### AMPEL360e eWTW · ATA 39 · Q+ATLANTIDE ATLAS Scaffold

**Status:** <img src="https://img.shields.io/badge/DRAFT-yellow">  
**Revision:** 0.1.0 — 2026-05-10  
**Classification:** Q-AIR Primary | Q-MECHANICS / Q-DATAGOV / Q-HPC / Q-GROUND / Q-INDUSTRY Support

---

## §0 Hyperlink Policy

All cross-references use relative Markdown links. Regulatory references are cited by identifier. DMC cross-references follow `DMC-AMPEL360E-EWTW-039-30-YYYY-A`. Badge <img src="https://img.shields.io/badge/TBD-red"> marks unresolved parameters. Badges <img src="https://img.shields.io/badge/DRAFT-yellow"> and <img src="https://img.shields.io/badge/To_Be_Completed-orange"> indicate work-in-progress and planned content.

---

## §1 Purpose

This document describes **Relay, Contactor, and Power Distribution Panels** (subsubject 039-030) of the AMPEL360e eWTW. It covers:

1. Power Distribution Units (PDUs): PDU-1 (left main), PDU-2 (right main), PDU-3 (essential), PDU-4 (emergency) — converting and distributing bus power to load groups.
2. Solid-State Power Controllers (SSPCs): electronic load management controllers within each PDU providing programmable overcurrent, current sensing, and AFDX health reporting.
3. Bus Tie Contactors (BTCs): BTC-L and BTC-R enabling cross-feed between main buses.
4. High-voltage relay contactors: battery isolation and HVDC bus switching (ATA 24 interface).
5. DC motor contactors for ECS electric compressor and galley/ECS high-power loads.
6. Load-shed logic: SSPC programmable trip thresholds supporting degraded power state load management.
7. Relay reliability and AFDX interface for PDU health data to CMC.

---

## §2 Applicability

| Item | Value |
|---|---|
| Aircraft Programme | AMPEL360e eWTW |
| Variant | All variants |
| ATA Chapter / Subsubject | 39 — 039-030 Relay, Contactor, and Power Distribution Panels |
| Document Tier | Level 3 — Component/Assembly Description |
| Effectivity | MSN 0001 onwards <img src="https://img.shields.io/badge/TBD-red"> |

Includes all PDU assemblies, SSPC modules, BTCs, battery isolation contactors, and motor contactors. Excludes:
- Electrical power generation and main bus architecture: → ATA 24
- Circuit breaker panels (upstream protection): → 039-020

---

## §3 System/Function Overview

### 3.1 Power Distribution Architecture

The eWTW power distribution architecture comprises four bus tiers:

| Bus | PDU | Voltage | Priority | Powered By |
|---|---|---|---|---|
| Left Main Bus | PDU-1 | 28 VDC (or 115 VAC TBD) | Normal ops | Left IDG / TRU / Battery |
| Right Main Bus | PDU-2 | 28 VDC (or 115 VAC TBD) | Normal ops | Right IDG / TRU |
| Essential Bus | PDU-3 | 28 VDC | Degraded ops | Battery + essential TRU |
| Emergency Bus | PDU-4 | 28 VDC | Emergency | Battery direct |

Cross-feed between Left and Right Main Buses is achieved via Bus Tie Contactors (BTC-L / BTC-R).

### 3.2 SSPC Architecture

Each PDU contains an array of Solid-State Power Controllers (SSPCs). Each SSPC is a channel protecting and controlling one or more load circuits:

| SSPC Feature | Description |
|---|---|
| Electronic trip | FET-based; current sensed in real-time |
| Programmable trip threshold | Set per load via ground maintenance terminal or factory configuration |
| Current sensing | Used for health monitoring and diagnostic logging |
| Load shedding | Programmable priority: essential loads remain powered; non-essential loads shed in degraded power state |
| AFDX reporting | SSPC state (open/closed), current, temperature reported via AFDX to CMC |
| Manual override (ground) | Via maintenance terminal — force open or close for test TBD |

### 3.3 Bus Tie Contactors

BTC-L and BTC-R are electromechanical contactors enabling cross-feed between left and right main buses:
- Open (normal): each bus powered independently from its own generation source.
- Closed (cross-feed): one generation source feeds both buses during single generator failure.
- BTC logic: driven by electrical power management function hosted in IMA (ATA 24 / ATA 42).
- Contact state reported via position feedback relay to CMC via AFDX.
- Rated for ≥ 50,000 operations <img src="https://img.shields.io/badge/TBD-red"> (supplier confirmation pending).

### 3.4 Battery Isolation and HVDC Contactors

- Battery isolation contactors (BICs): normally open in flight; close to connect battery to emergency bus on loss of all generation. Controlled by ATA 24 battery management function.
- HVDC contactors: for 270 VDC bus connection / isolation (OI-039-005 — pending bus voltage decision).

---

## §4 Scope

### 4.1 In-Scope

- PDU-1, PDU-2, PDU-3, PDU-4 assemblies and SSPC modules
- BTC-L, BTC-R electromechanical contactors
- Battery isolation contactors (BICs)
- HVDC bus contactors TBD
- DC motor contactors for ECS electric compressor and large loads
- Load-shed logic configuration (SSPC priority settings)
- AFDX interface modules in PDUs
- PDU panel structures and mounting in E/E bay

### 4.2 Out-of-Scope

- Electrical power generation (IDGs, TRUs): → ATA 24
- Circuit breaker protection (CBPs): → 039-020
- Battery hardware: → ATA 24
- IMA hosted power management software: → ATA 42

---

## §5 Architecture Description

### 5.1 PDU Internal Architecture

Each PDU contains:
- **Bus bars**: copper or aluminium; rated for full bus current TBD.
- **SSPC array**: N channels per PDU (N TBD per ELA TBD).
- **AFDX interface module**: PDU health and SSPC state reporting to CMC.
- **Current monitoring**: per-SSPC and per-bus total current sensor.
- **Temperature monitoring**: PDU internal temperature sensor.
- **Manual test interface**: maintenance connector on PDU front panel (ground service only).

### 5.2 Load-Shed Priority Scheme

In degraded power state (single generator, essential bus only), the SSPC load-shed logic disconnects non-essential loads in priority order:

| Priority | Load Category | SSPC Action |
|---|---|---|
| 1 — Essential | Flight instruments, autopilot, communication | Always powered |
| 2 — Required | ECS minimum, fuel management, navigation | Maintained if power available |
| 3 — Comfort | Galley outlets, IFE, reading lights | Shed first on degraded power |
| 4 — Non-essential | Utility outlets, supplementary cabin | Shed with load reduction |

Load-shed thresholds are configured at factory and verified per maintenance schedule. Priority table: <img src="https://img.shields.io/badge/TBD-red"> (pending ELA).

---

## §6 Functional Breakdown

| ID | Function | Components | Interface | Status |
|---|---|---|---|---|
| 039-030-F01 | Bus power distribution (Left Main) | PDU-1 SSPC array | ATA 24 bus → load circuits | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 039-030-F02 | Bus power distribution (Right Main) | PDU-2 SSPC array | ATA 24 bus → load circuits | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 039-030-F03 | Essential bus power distribution | PDU-3 SSPC array | Battery / TRU → essential loads | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 039-030-F04 | Emergency bus power distribution | PDU-4 contactors / SSPC | Battery direct → emergency loads | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 039-030-F05 | Bus cross-feed | BTC-L / BTC-R | Left ↔ Right main bus | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 039-030-F06 | Battery isolation | BIC | Battery ↔ Emergency bus | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 039-030-F07 | Load shedding | SSPC priority logic | IMA load management function | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 039-030-F08 | PDU health reporting | AFDX module in PDU | AFDX → CMC | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 039-030-F09 | HVDC contactor switching | HVDC contactor TBD | ATA 24 HVDC bus | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §7 System Context Diagram

```mermaid
flowchart LR
    ATA24["ATA 24\nElectrical Power\n(IDG / TRU / Battery / GPU)"]
    PDU1["PDU-1\nLeft Main Bus"]
    PDU2["PDU-2\nRight Main Bus"]
    PDU3["PDU-3\nEssential Bus"]
    PDU4["PDU-4\nEmergency Bus"]
    BTC["BTC-L / BTC-R\nBus Tie Contactors"]
    BIC["BIC\nBattery Isolation\nContactors"]
    SSPC_LOADS["Load Circuits\n(all ATA system loads)"]
    IMA["IMA R1/R2\n(load management function)"]
    CMC["CMC ATA 45"]
    AFDX_SW["AFDX Switch"]

    ATA24 -->|"bus power"| PDU1 & PDU2 & PDU3 & PDU4
    PDU1 <-->|"cross-feed"| BTC
    BTC <-->|"cross-feed"| PDU2
    ATA24 -->|"battery → BIC"| BIC
    BIC -->|"battery connection"| PDU4
    PDU1 & PDU2 & PDU3 & PDU4 -->|"SSPC channels"| SSPC_LOADS
    PDU1 & PDU2 & PDU3 & PDU4 -->|"AFDX health"| AFDX_SW
    BTC -->|"state feedback"| AFDX_SW
    AFDX_SW <-->|"AFDX"| IMA
    AFDX_SW -->|"AFDX"| CMC
    IMA -->|"load shed commands"| AFDX_SW
```

---

## §8 Internal Functional Architecture

```mermaid
flowchart TB
    subgraph PDU1["PDU-1 Left Main Bus"]
        BUSBAR1["Bus Bar 28 VDC / 115 VAC TBD"]
        SSPC_ARRAY1["SSPC Array (N channels TBD)"]
        CURR_MON1["Bus Current Monitor"]
        TEMP1["Temperature Sensor"]
        AFDX_MOD1["AFDX Interface Module"]
    end
    subgraph PDU3["PDU-3 Essential Bus"]
        BUSBAR3["Bus Bar 28 VDC"]
        SSPC_ARRAY3["SSPC Array (essential loads)"]
        CURR_MON3["Bus Current Monitor"]
        AFDX_MOD3["AFDX Interface Module"]
    end
    subgraph BTC_UNIT["Bus Tie Contactors"]
        BTC_L["BTC-L\nElectromechanical"]
        BTC_R["BTC-R\nElectromechanical"]
        POS_FB["Position Feedback Relay"]
    end
    ATA24_BUS["ATA 24 Bus Feeds"]
    LOADS["Load Circuits"]
    AFDX["AFDX Switch"]
    CMC["CMC"]

    ATA24_BUS --> BUSBAR1 & BUSBAR3
    BUSBAR1 --> SSPC_ARRAY1 --> LOADS
    BUSBAR3 --> SSPC_ARRAY3 --> LOADS
    CURR_MON1 & TEMP1 --> AFDX_MOD1 --> AFDX
    CURR_MON3 --> AFDX_MOD3 --> AFDX
    BTC_L & BTC_R --> POS_FB --> AFDX
    AFDX --> CMC
```

---

## §9 Lifecycle Traceability

```mermaid
flowchart LR
    LC02["LC02\nRequirements\nBus architecture, load priorities,\nSSPC rating requirements"]
    LC03["LC03\nArchitecture\nPDU count/location,\nBTC topology, load-shed scheme"]
    LC05["LC05\nDetailed Design\nSSPC configuration, BTC sizing,\nPDU layout, AFDX interface"]
    LC06["LC06\nVerification Planning\nPDU load test, SSPC overcurrent,\nBTC operation count test"]
    LC10["LC10\nCertification\nCS-25.1353 / CS-25.1309\nDO-160G qualification"]
    LC11["LC11\nOperation\nLoad shed procedures,\nbus management FCOM"]
    LC12["LC12\nMaintenance\nAMM 39-30: PDU LRU R&R,\nSSPC configuration check"]

    LC02 --> LC03 --> LC05 --> LC06 --> LC10 --> LC11 --> LC12
```

---

## §10 Interfaces

| Interface | Direction | Counterpart | Signal Type | Notes |
|---|---|---|---|---|
| Main bus power (Left) | In | ATA 24 Left IDG/TRU | Electrical (28 VDC or 115 VAC TBD) | PDU-1 bus feed |
| Main bus power (Right) | In | ATA 24 Right IDG/TRU | Electrical (28 VDC or 115 VAC TBD) | PDU-2 bus feed |
| Essential bus power | In | ATA 24 Battery / TRU | Electrical (28 VDC) | PDU-3 bus feed |
| Emergency bus power | In | ATA 24 Battery | Electrical (28 VDC) | PDU-4 direct battery |
| SSPC load outputs | Out | All ATA system loads | Electrical (branch circuits) | Per ELA TBD |
| PDU health — AFDX | Out | CMC (ATA 45) / IMA (ATA 42) | AFDX | SSPC states, current, temperature |
| Load shed commands | In | IMA load management (ATA 42) | AFDX | SSPC open/close commands for shedding |
| BTC state feedback | Out | CMC / IMA | AFDX discrete | BTC open / closed position |
| BTC control | In | IMA electrical power management | AFDX discrete | BTC open / close command |
| Battery isolation contactor control | In | ATA 24 battery management | Hardwired + AFDX | BIC open / close |
| HVDC contactor control | In | ATA 24 HVDC management TBD | TBD | OI-039-005 |

---

## §11 Operating Modes

| Mode | PDU State | SSPC State | BTC State | Load Shedding |
|---|---|---|---|---|
| Normal Dual Generator | PDU-1/2 powered independently | All SSPCs closed, loads powered | BTC open (normal) | None |
| Single Generator (left) | PDU-1 powered; PDU-2 from BTC | BTC-L closed; PDU-2 from left bus | BTC-L closed | Level 1: comfort loads shed |
| Essential Bus Only | PDU-3 powered | Essential SSPCs only | All BTCs open | Level 2: comfort + required shed |
| Emergency | PDU-4 battery direct | Minimum emergency SSPCs | All contactors open | Level 3: only essential emergency |
| Ground GPU | All PDUs powered by GPU | All SSPCs per pre-flight config | Per maintenance config | None (GPU power available) |
| Maintenance Test | Selected PDU/SSPC test | Individual SSPC test | Individual BTC test | Manual configuration |

---

## §12 Monitoring and Diagnostics

| Parameter | Sensor / Source | CMC Signal | Alert |
|---|---|---|---|
| SSPC state (per channel) | SSPC controller | AFDX | Per-channel state in CMC log |
| SSPC current (per channel) | SSPC current sensor | AFDX | Overcurrent trend advisory TBD |
| PDU bus voltage | Bus voltage monitor in PDU | AFDX | "PDU UNDERVOLT" (caution) |
| PDU internal temperature | PDU temperature sensor | AFDX | "PDU TEMP HI" (advisory/caution) |
| BTC contact state | Position feedback relay | AFDX | "BUS TIE FAULT" (caution) if command/state mismatch |
| BIC state | Position feedback | AFDX | "BATT ISOL FAULT" (caution) |
| SSPC operation count | SSPC non-volatile log | CMC query | Prognostic advisory TBD |

---

## §13 Maintenance Concept

### 13.1 On-Wing Maintenance

| Task | Interval | Access | Skill Level |
|---|---|---|---|
| PDU visual inspection | A-check <img src="https://img.shields.io/badge/TBD-red"> | E/E bay access | Line maintenance |
| SSPC configuration check | C-check TBD | CMC terminal | Line maintenance |
| SSPC status log download | Each visit (CMC) | CMC terminal | Line maintenance |
| BTC operation count check | C-check TBD | CMC query | Line maintenance |
| BTC functional test | C-check TBD | Maintenance mode via CMC | Line/base |
| PDU connector and bonding inspection | C-check TBD | E/E bay access | Base maintenance |
| PDU (LRU) replacement | On condition | E/E bay; rack slides | Line maintenance (trained) |
| SSPC module replacement (if modular) | On condition | PDU access panel | Line maintenance (trained) |
| BTC contactor replacement | On condition | E/E bay | Base maintenance |

### 13.2 Off-Wing

- PDU: shop test per CMM; SSPC calibration; bus bar inspection.
- BTC: contact resistance measurement, overhaul at operation limit TBD.

---

## §14 S1000D/CSDB Mapping

| Document | DMC Pattern | Info Code | Status |
|---|---|---|---|
| PDU system description | DMC-AMPEL360E-EWTW-039-30-00A-040A-A | 040 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| PDU replacement | DMC-AMPEL360E-EWTW-039-30-00A-520A-A | 520 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| BTC functional test | DMC-AMPEL360E-EWTW-039-30-01A-300A-A | 300 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| SSPC configuration procedure | DMC-AMPEL360E-EWTW-039-30-00A-920A-A | 920 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Fault isolation — PDU | DMC-AMPEL360E-EWTW-039-30-00A-400A-A | 400 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

Full DMRL in [039-090](./039-090-S1000D-CSDB-Mapping-and-Traceability.md).

---

## §15 Footprints

| Parameter | Value |
|---|---|
| PDU count | 4 (PDU-1 through PDU-4) |
| SSPC count per PDU | <img src="https://img.shields.io/badge/TBD-red"> (pending ELA) |
| Total SSPC count | <img src="https://img.shields.io/badge/TBD-red"> |
| BTC count | 2 (BTC-L, BTC-R) |
| BIC count | <img src="https://img.shields.io/badge/TBD-red"> |
| BTC rated current | <img src="https://img.shields.io/badge/TBD-red"> A |
| BTC operation life | ≥ 50,000 operations <img src="https://img.shields.io/badge/TBD-red"> |
| PDU-1/2 mass (each) | <img src="https://img.shields.io/badge/TBD-red"> |
| PDU-3 mass | <img src="https://img.shields.io/badge/TBD-red"> |
| PDU-4 mass | <img src="https://img.shields.io/badge/TBD-red"> |
| PDU location | Aft E/E bay <img src="https://img.shields.io/badge/TBD-red"> |

---

## §16 Safety and Certification

| Requirement | Standard | Application |
|---|---|---|
| Electrical equipment and installations | CS-25.1353 | PDUs, BTCs, BICs, HVDC contactors |
| System safety — failure effects | CS-25.1309 | SSPC fail-open (safe) vs. fail-closed (hazardous for short circuit); BTC spurious close analysis |
| Environmental qualification | DO-160G | PDU, BTC, SSPC: vibration, temperature, humidity |
| Load-shed logic | CS-25.1309 | Degraded power state load management; essential loads always maintained |
| Contactor arc suppression | ARC suppression standard TBD | 270 VDC contactors require arc suppression per HVDC standards |
| Relay contact life | Supplier qualification | ≥ 50,000 operations for BTCs TBD |
| AFDX health reporting | ARINC 664 Pt 7 | PDU status on AFDX dual-star network |

---

## §17 Verification and Validation

| Test | Method | Acceptance Criterion | Status |
|---|---|---|---|
| PDU load test | Apply rated load per bus; measure SSPC and bus performance | All SSPCs stable; no false trip at rated load | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| SSPC overcurrent test | Inject overcurrent at TBD × rated; measure trip time | Trip within SSPC spec ± TBD% | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| SSPC load-shed test | Simulate degraded power; verify load shed sequence | Non-essential SSPCs open per priority table | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| BTC functional test | Command open/close; verify contact state and feedback | State changes within TBD ms; feedback matches command | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| BTC cross-feed test | Open one IDG; verify BTC closes and loads transfer | Bus voltage maintained within TBD% on transfer | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| BTC operation life test | Endurance test ≥ 50,000 operations (type test) | Contact resistance within spec after full life | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| BIC function test | Simulate loss of all generation; verify BIC closes | Battery connects to emergency bus within TBD ms | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| AFDX PDU health reporting | Monitor AFDX; inject SSPC state change | State change reflected in AFDX frame within TBD ms | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DO-160G environmental (PDU) | Per DO-160G categories | All categories pass per qualification test plan | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Panel bonding resistance | Milliohm meter | ≤ 2.5 mΩ | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| SSPC digital log verification | Trip event; read log | Log entry correct | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §18 Glossary

| Term | Definition |
|---|---|
| PDU | Power Distribution Unit — assembly distributing bus power to load circuits via SSPCs and contactors |
| SSPC | Solid-State Power Controller — electronic load controller providing overcurrent protection, current sensing, and AFDX health reporting |
| BTC | Bus Tie Contactor — electromechanical contactor enabling cross-feed between left and right main electrical buses |
| BIC | Battery Isolation Contactor — contactor connecting or isolating the battery from the bus |
| Bus bar | Conductor bar within PDU distributing bus power to multiple SSPC inputs |
| Load shedding | Controlled disconnection of non-essential loads to prevent overloading a degraded power source |
| SSPC priority | Assigned load priority used by load-shed logic to determine which loads to disconnect first |
| Cross-feed | Condition where one generator supplies both main buses via closed BTC |
| Arc suppression | Mechanism or device limiting electrical arc when DC contactor opens under load |
| ELA | Electrical Load Analysis — document listing all aircraft loads, bus assignments, and load demands |
| HVDC | High Voltage DC — 270 VDC bus used in eWTW all-electric architecture |
| IFE | In-Flight Entertainment — passenger entertainment system (non-essential load, shed first) |
| Position feedback relay | Small relay in BTC that monitors contact position and provides a discrete signal confirming open/closed state |
| AFDX | Avionics Full-Duplex Switched Ethernet (ARINC 664 Part 7) — data bus for PDU health reporting |
| CMC | Central Maintenance Computer (ATA 45) — receives PDU and SSPC health data |

---

## §19 Citations

1. EASA CS-25.1353 — Electrical equipment and installations.
2. EASA CS-25.1309 — Equipment, systems, and installations — system safety.
3. RTCA/EUROCAE DO-160G — Environmental Conditions and Test Procedures.
4. ARINC Report 664 Part 7 — AFDX data bus.
5. Q+ATLANTIDE ATLAS [039-000 General](./039-000-Electrical-Electronic-Panels-and-Multipurpose-Components-General.md).
6. Q+ATLANTIDE ATLAS [039-020 CBPs](./039-020-Circuit-Breaker-and-Protection-Panels.md).
7. Q+ATLANTIDE ATLAS [039-090 S1000D/CSDB Mapping](./039-090-S1000D-CSDB-Mapping-and-Traceability.md).

---

## §20 References

| Ref | Document | Notes |
|---|---|---|
| [R1] | CS-25.1353 | PDU, BTC, SSPC electrical installations |
| [R2] | CS-25.1309 | System safety — SSPC/BTC failure analysis |
| [R3] | DO-160G | Environmental qualification — PDU, BTC |
| [R4] | ARINC 664 Pt 7 | AFDX health reporting from PDUs |
| [R5] | ATA 24 — Electrical Power ATLAS | Bus architecture, IDG/TRU/battery feeds to PDUs |
| [R6] | ATA 42 — IMA ATLAS | Load management function hosting in IMA |
| [R7] | ATA 45 — CMC ATLAS | CMC receiving PDU health AFDX data |
| [R8] | 039-020 | CBPs — upstream protection |
| [R9] | 039-080 | Panel monitoring — SSPC and PDU BITE |

---

## §21 Open Issues

| ID | Description | Owner | Status |
|---|---|---|---|
| OI-039-001 | SSCB vs. TM-CB decision (affects SSPC integration with CBP) | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-039-005 | 270 VDC vs. 115 VAC primary distribution — PDU bus voltage TBD | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-039-014 | ELA completion — SSPC count and rating per PDU | Q-AIR | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-039-015 | BTC operation life target confirmation from supplier | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-039-016 | HVDC contactor arc suppression standard selection | Q-AIR / ORB-LEG | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §22 Change Log

| Revision | Date | Author | Description |
|---|---|---|---|
| 0.1.0 | 2026-05-10 | Q+ATLANTIDE ATLAS Working Group | Initial full-template draft; all 23 sections populated; eWTW PDU/SSPC/BTC context incorporated |
| 0.0.0 | 2026-05-10 | Q+ATLANTIDE ATLAS Working Group | Scaffold stub created |
