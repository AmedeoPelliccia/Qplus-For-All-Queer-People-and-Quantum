---
document_id: "QATL-ATLAS-000099-ATLAS-030039-038-000"
title: "038-000 — Water and Waste — General"
short_title: "ATA 38 General"
subsubject: "000"
subsubject_title: "Water and Waste — General"
file_name: "038-000-Water-and-Waste-General.md"
sns_reference: "038-00"
dmc_prefix: "DMC-AMPEL360E-EWTW-038-00"
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
node_code: "038"
node_title: "Water and Waste"
node_link: "./"
parent_path: "Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/038_Water-and-Waste/"
parent_path_link: "./"
ata_reference: "ATA 38"
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
  - name: "Q-GREENTECH"
    link: "../../../../../Q-Divisions/Q-GREENTECH/"
  - name: "Q-GROUND"
    link: "../../../../../Q-Divisions/Q-GROUND/"
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
  atlas_node: "038_Water-and-Waste"
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
  - "ATA 38"
  - "Water and Waste"
  - "Potable Water"
  - "Vacuum Waste"
  - "PWS"
  - "VWS"
  - "EWP"
  - "EWH"
  - "general overview"
---

# 038-000 — Water and Waste — General
### AMPEL360e eWTW · ATA 38 · Q+ATLANTIDE ATLAS Scaffold

**Status:** <img src="https://img.shields.io/badge/DRAFT-yellow">  
**Revision:** 0.1.0 — 2026-05-10  
**Classification:** Q-AIR Primary | Q-MECHANICS / Q-DATAGOV / Q-GREENTECH / Q-GROUND Support

---

## §0 Hyperlink Policy

All cross-references within this document use relative Markdown links anchored to section headings within the Q+ATLANTIDE ATLAS repository. External regulatory references (CS-25, AMC, WHO, FAA) are cited by document identifier only; no live external URLs are embedded because regulatory document URLs are subject to change without notice. Internal DMC cross-references follow the pattern `DMC-AMPEL360E-EWTW-038-XX-YYYY-A`. Traceability links to the CSDB are maintained in §14. Where a parameter is not yet determined, the badge <img src="https://img.shields.io/badge/TBD-red"> is used inline. Badges <img src="https://img.shields.io/badge/DRAFT-yellow"> and <img src="https://img.shields.io/badge/To_Be_Completed-orange"> indicate work in progress or planned content respectively.

---

## §1 Purpose

This document provides the top-level general overview of **ATA Chapter 38 — Water and Waste** as applied to the **AMPEL360e eWTW** (~100-passenger, fully electric, medium-range) aircraft. It establishes:

1. The architecture and philosophy of the fully electric Potable Water System (PWS) — no engine bleed, no APU steam heating, electrically pressurised and heated.
2. The grey water drainage system — gravity drain to electrically heated mast drain nozzles.
3. The Vacuum Waste System (VWS) as the toilet/lavatory waste collection and storage subsystem, interfacing with ATA 37 (vacuum generation).
4. System boundaries between ATA 38 and adjacent ATA chapters (ATA 37, ATA 21, ATA 24, ATA 25, ATA 36).
5. The applicable certification basis (CS-25, WHO, FAA Part 121 Appendix A).
6. The document hierarchy for ATA 38, covering subsubjects 038-000 through 038-090.

This document is authoritative for system boundary definition and interfaces for all lower-level ATA 38 documents.

---

## §2 Applicability

| Item | Value |
|---|---|
| Aircraft Programme | AMPEL360e eWTW |
| Variant | All variants (unless noted) |
| ATA Chapter | 38 — Water and Waste |
| Document Tier | Level 2 — System Description Document (SDD) |
| Effectivity | MSN 0001 onwards <img src="https://img.shields.io/badge/TBD-red"> |
| Preceding Document | Scaffold Rev 0.0 |

This document applies to all systems that store, distribute, heat, or drain water and that collect, store, or service toilet waste aboard the AMPEL360e eWTW. It explicitly excludes:
- Cabin humidity and condensate management (ATA 21)
- Vacuum generation equipment (ATA 37)
- Toilet bowl assemblies and seat mechanisms (ATA 25)
- Galley cooling equipment drains unless routed into the ATA 38 grey drain network

---

## §3 System/Function Overview

### 3.1 eWTW ATA 38 Philosophy

The AMPEL360e eWTW adopts a fully electric water and waste management philosophy — no engine bleed air, no APU-derived heat, no pneumatic tank pressurisation from a traditional bleed source. All water heating, tank pressurisation, freeze protection, and grey-drain nozzle heating are achieved by electrical means.

| Function | Conventional Aircraft | eWTW Solution |
|---|---|---|
| Tank pressurisation | Bleed air from pneumatic manifold (ATA 36) | Electric Air Compressor (EAC) low-pressure air OR electric pump with bladder <img src="https://img.shields.io/badge/TBD-red"> |
| Water heating | Boiler fed by APU steam / bleed heat exchange | Electric Water Heaters (EWH), instant or storage type |
| Grey drain nozzle heating | Engine bleed or hot air duct | Electric Mast Heaters (EMH) |
| Freeze protection | Warm air blanket from cabin distribution | Electric trace heating on cold-zone lines |
| Toilet flushing | Vacuum from engine-driven vacuum pump | Electric Vacuum Generator (EVG — ATA 37) |

### 3.2 Subsystem Summary

ATA 38 on the eWTW is divided into two main loops:

**Clean Loop (Potable Water System — PWS):**
- Water tank (composite, pressurised) → Electric Water Pump (EWP) → UV sterilisation unit → activated carbon pre-filter → distribution lines → galleys and lavatories → Electric Water Heaters (EWH) at point of use.

**Dirty Loop (Waste System):**
- Grey water: lavatory and galley sinks → gravity drain lines → mast drain nozzles (overboard).
- Black water (toilet waste): flush cycle via EFV → vacuum transport (ATA 37 EVG) → waste collection tanks → ground drain service.

The two loops are maintained strictly separate. No cross-connection exists between the clean and dirty loops. Non-Return Valves (NRVs) are fitted at all clean-loop branch points to prevent backflow contamination.

---

## §4 Scope

### 4.1 In-Scope

- Potable water tank, fill port, overfill valve, vent filter, drain valve, level sensor, pressure sensor
- Electric Water Pump (EWP) and distribution piping
- Electric Water Heaters (EWH) at all galley and lavatory service points
- UV sterilisation unit (inline, at tank outlet or EWP outlet)
- Activated carbon pre-filter at fill point
- Cold-water distribution lines (LLDPE or PEX)
- Grey water drain lines, mast drain nozzles, Electric Mast Heaters (EMH)
- Toilet waste collection tanks (stainless or CFRP), fill-level sensors, overflow sensors, temperature sensors, odour filter vent
- Electric Flush Valves (EFV) and rinse water supply to lavatory bowls
- Waste tank ground drain fittings and single-point service panel
- Freeze protection trace heaters and Trace Heater Controller (THC)
- System indication: ECAM water quantity, waste fill level, CAS alerts
- BITE and CMC monitoring interfaces for all ATA 38 components

### 4.2 Out-of-Scope

- Vacuum generation equipment (EVG, SOV, VRV, vacuum manifold): → ATA 37
- Toilet bowl assemblies and seat mechanisms: → ATA 25
- Galley cooling systems: → ATA 25
- Cabin pressurisation: → ATA 21
- Electrical bus architecture and power distribution: → ATA 24
- Pneumatic supply for tank pressurisation option (EAC source): → ATA 36

### 4.3 Document Hierarchy

| Subsubject | Title | Status |
|---|---|---|
| 038-000 | Water and Waste — General | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-010 | Potable Water System | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-020 | Water Storage and Distribution | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-030 | Water Heaters and Service Interfaces | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-040 | Waste Water Drainage | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-050 | Toilet and Vacuum Waste System | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-060 | Water and Waste Indication and Warning | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-070 | Water and Waste Servicing and Ground Interfaces | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-080 | Water and Waste Monitoring, Diagnostics, and Control Interfaces | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-090 | S1000D/CSDB Mapping and Traceability | <img src="https://img.shields.io/badge/DRAFT-yellow"> |

---

## §5 Architecture Description

### 5.1 System Architecture Summary

The ATA 38 Water and Waste system consists of three discrete fluid circuits, each maintained separate:

**Circuit A — Potable Water (pressurised, clean):**
```
[Ground Fill Port] → [Activated Carbon Filter] → [Potable Water Tank]
    ← [EAC pressure / bladder TBD] ←
[Tank] → [EWP] → [UV Sterilisation] → [Cold Water Distribution Header]
    ├── [Galley FWD — EWH + faucet]
    ├── [Galley AFT — EWH + faucet]
    ├── [Lav-1 — EWH + faucet + rinse nozzle]
    ├── [Lav-2 — EWH + faucet + rinse nozzle]
    └── [Lav-3 — EWH + faucet + rinse nozzle] TBD
```

**Circuit B — Grey Water (gravity, dirty):**
```
[Galley FWD sink] ──┐
[Galley AFT sink] ──┤
[Lav-1 sink]      ──┤── [Gravity drain lines] → [Mast Drain-1] → [Overboard]
[Lav-2 sink]      ──┤                        → [Mast Drain-2] → [Overboard] TBD
[Lav-3 sink]      ──┘
```

**Circuit C — Black Water (vacuum transport, dirty):**
```
[Lav toilet bowls] → [EFV] → [Vacuum transport (ATA 37)] → [Waste Tank(s)] → [Ground Drain]
```

### 5.2 Pressurisation Options

Two candidate pressurisation strategies are under evaluation <img src="https://img.shields.io/badge/TBD-red">:
- **Option A:** Low-pressure air from Electric Air Compressor (EAC, ATA 36) — ~3.5 bar gauge to tank headspace.
- **Option B:** Bladder accumulator with electric pump — no air contact with water.

Option B is preferred from a water quality perspective (no risk of air contamination) but requires a larger tank volume or bladder package. Decision pending supplier selection (OI-038-002).

---

## §6 Functional Breakdown

| Subsubject | Function | Key Components | Status |
|---|---|---|---|
| 038-000 | System overview and general | All ATA 38 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-010 | Potable water system | Tank, EWP, UV, filter, NRVs | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-020 | Water storage and distribution | Tank, distribution lines, EWP, check valves | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-030 | Water heaters and service interfaces | EWH units, TMV, hot water branches | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-040 | Waste water drainage | Grey drain lines, mast drains, EMH | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-050 | Toilet and vacuum waste system | EFV, waste tanks, WIV, odour filter | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-060 | Indication and warning | ECAM, CAS, galley panel, CMC | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-070 | Servicing and ground interfaces | Fill port, drain fitting, service panel | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-080 | Monitoring, diagnostics, control | CMC, BITE, THC, AFDX | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 038-090 | S1000D/CSDB mapping | DMC assignments, DMRL | <img src="https://img.shields.io/badge/DRAFT-yellow"> |

---

## §7 System Context Diagram

```mermaid
flowchart LR
    ATA24["ATA 24\nElectrical Power\n(AC/DC buses)"]
    ATA36["ATA 36\nPneumatic\n(EAC pressure option)"]
    ATA37["ATA 37\nVacuum\n(EVG vacuum supply)"]
    ATA25["ATA 25\nFurnishings\n(Toilet bowls, galleys)"]
    ATA21["ATA 21\nAir Conditioning\n(cabin environment)"]
    GROUND["Ground Services\n(water fill truck,\nwaste vacuum truck)"]

    PWS["Potable Water System\n(Tank + EWP + UV + EWH)"]
    GWD["Grey Water Drainage\n(drain lines + mast drains)"]
    VWS["Vacuum Waste System\n(waste tanks + EFV)"]
    CMC["CMC / ECAM\n(ATA 31/45)"]

    ATA24 -->|"AC power"| PWS
    ATA24 -->|"AC power"| GWD
    ATA24 -->|"AC power"| VWS
    ATA36 -.->|"low-pressure air\n(Option A TBD)"| PWS
    ATA37 -->|"vacuum supply\n(EVG)"| VWS
    ATA25 -.->|"toilet bowls\ngalley fittings"| PWS
    ATA25 -.->|"toilet bowls"| VWS
    ATA21 -.->|"cabin temp\n(freeze ref)"| PWS
    GROUND -->|"potable fill"| PWS
    GROUND -->|"waste drain"| VWS
    PWS -->|"sensor data"| CMC
    GWD -->|"heater status"| CMC
    VWS -->|"fill level, faults"| CMC
```

---

## §8 Internal Functional Architecture

```mermaid
flowchart TB
    FILL["Ground Fill\n(pressure fill port)"]
    FILTER["Activated Carbon\nPre-filter"]
    TANK["Potable Water Tank\n(composite, TBD L)"]
    PRESS["Tank Pressurisation\n(EAC or bladder TBD)"]
    EWP["Electric Water Pump\n(EWP)"]
    UV["UV Sterilisation Unit"]
    HEADER["Cold Water\nDistribution Header"]
    EWH_FG["EWH — Galley FWD"]
    EWH_AG["EWH — Galley AFT"]
    EWH_L1["EWH — Lav-1"]
    EWH_L2["EWH — Lav-2"]
    EWH_L3["EWH — Lav-3 TBD"]
    RINSE["Rinse Nozzles\n(lavatory bowls)"]

    GREY_L1["Grey Drain — Lav-1 sink"]
    GREY_L2["Grey Drain — Lav-2 sink"]
    GREY_L3["Grey Drain — Lav-3 sink TBD"]
    GREY_G["Grey Drain — Galleys"]
    MAST["Mast Drain Nozzles\n(EMH heated)"]
    OB["Overboard"]

    EFV1["EFV-1"]
    EFV2["EFV-2"]
    EFV3["EFV-3 TBD"]
    WTANK["Waste Tank(s)\n(stainless/CFRP)"]
    VENT["Odour Vent Filter\n(activated carbon)"]
    DRAIN_SVC["Ground Drain\nService Fitting"]

    FILL --> FILTER --> TANK
    PRESS --> TANK
    TANK --> EWP --> UV --> HEADER
    HEADER --> EWH_FG
    HEADER --> EWH_AG
    HEADER --> EWH_L1
    HEADER --> EWH_L2
    HEADER --> EWH_L3
    HEADER --> RINSE

    GREY_L1 --> MAST
    GREY_L2 --> MAST
    GREY_L3 --> MAST
    GREY_G --> MAST
    MAST --> OB

    RINSE --> EFV1 --> WTANK
    RINSE --> EFV2 --> WTANK
    RINSE --> EFV3 --> WTANK
    WTANK --> VENT
    WTANK --> DRAIN_SVC
```

---

## §9 Lifecycle Traceability

```mermaid
flowchart LR
    REQ["Requirements\n(CS-25.1419, CS-25.853,\nWHO, 14 CFR Part 121 App A)"]
    SRD["System Requirements\nDocument (SRD)"]
    SDD["System Description\nDocument (SDD)\n038-000"]
    ICD["Interface Control\nDocuments (ICDs)\nATA 24/36/37/25"]
    COMP["Component Specs\n(EWP, EWH, UV unit,\nEFV, waste tank)"]
    VTP["V&V Plan\n(§17)"]
    TEST["Test Reports\n(flow, leak, thermal,\nflush, water quality)"]
    CERT["Certification\n(EASA CS-25 / FAA)"]
    EIS["Entry Into Service"]
    MAINT["Maintenance\n(AMM/CMM, S1000D DMs)"]

    REQ --> SRD --> SDD --> ICD --> COMP
    SDD --> VTP --> TEST --> CERT --> EIS --> MAINT
```

---

## §10 Interfaces

| Interface | ATA Chapter | Direction | Signal/Medium | Notes |
|---|---|---|---|---|
| Electrical power — EWP, EWH, UV | ATA 24 | In | AC/DC bus <img src="https://img.shields.io/badge/TBD-red"> | Powers all electric water and waste components |
| Electrical power — EMH trace heaters | ATA 24 | In | Low-voltage DC <img src="https://img.shields.io/badge/TBD-red"> | Mast heater and trace heater power |
| Pneumatic pressurisation (Option A) | ATA 36 | In | Low-pressure air ~3.5 bar <img src="https://img.shields.io/badge/TBD-red"> | EAC-derived tank headspace pressure |
| Vacuum supply to EFV | ATA 37 | In | −0.7 to −1.0 bar <img src="https://img.shields.io/badge/TBD-red"> | EVG vacuum to toilet flush circuit |
| Toilet bowl assemblies | ATA 25 | Bi | Mechanical, water | EFV + rinse nozzle integrated with bowl |
| Galley fittings | ATA 25 | In | Mechanical | Faucet connections, sink drain fittings |
| Indication / ECAM | ATA 31 | Out | Digital (AFDX/ARINC 429) | Water quantity, waste level, CAS messages |
| CMC / BITE | ATA 45 | Bi | AFDX <img src="https://img.shields.io/badge/TBD-red"> | Fault logging, sensor values, test commands |
| Cabin temperature (freeze ref) | ATA 21 | In | Discrete/analogue | Freeze protection logic reference |
| Ground fill — potable water | Ground | In | Fluid (potable water) | Pressure fill port |
| Ground drain — waste | Ground | Out | Fluid (waste) | Vacuum or gravity drain truck connect |

---

## §11 Operating Modes

| Mode | Description | EWP | EWH | EMH | THC |
|---|---|---|---|---|---|
| Normal Flight | Full service, passengers aboard | Running | Thermostatically controlled | As needed (temp sensor) | Monitoring |
| Ground — Pre-flight | GPU powered, catering load | Running or standby | Pre-heat (GPU) | Armed | Monitoring |
| Ground — Post-flight | Waste drain / water fill service | Off (during drain/fill) | Off | As needed | Monitoring |
| Transit / Turnaround | Quick turnaround service | Standby | Thermostatically controlled | As needed | Monitoring |
| Cold Soak | Aircraft on ground, below +4°C | Standby | Off | Active (trace heaters ON) | Freeze active |
| Maintenance | BITE, manual test, component R&R | Manual test only | Manual test only | Manual test | Manual |
| Emergency / Degraded | EWP fault — gravity backup via pressurisation | Off (gravity from tank pressure) | Off or manual | As needed | Auto |

---

## §12 Monitoring and Diagnostics

| Parameter | Sensor | Location | CMC Signal | Alert |
|---|---|---|---|---|
| Potable water quantity | Capacitive level sensor (LS-038-01) | Water tank | AFDX/ARINC 429 | "WATER LO" (amber < TBD%) |
| Water tank pressure | Pressure sensor (PS-038-01) | Tank | CMC log | Advisory if over/under TBD |
| EWP status | Current monitor, speed feedback | EWP unit | AFDX | "EWP FAULT" (caution) |
| EWH temperature | NTC thermistor per EWH | Each EWH | AFDX | "EWH FAULT" (caution) |
| UV lamp status | UV sensor / lamp hours counter | UV unit | AFDX | "UV FAULT" (advisory) |
| Waste tank fill level | Capacitive level (3-step) | Each waste tank | AFDX | "WASTE FULL" (amber ≥ 90%) |
| Waste tank overflow | Reed switch or float | Each waste tank | Discrete | "WASTE OVFL" (red) |
| Water line temperature | NTC probes in cold zones | Belly/tail lines | AFDX | "FREEZE RISK" → THC activates |
| Mast heater continuity | Resistance monitor | EMH units | AFDX | "DRAIN HTR FAULT" (caution) |
| Trace heater status | Current monitor | THC | AFDX | Fault if heater open circuit |

---

## §13 Maintenance Concept

### 13.1 On-Wing Maintenance

| Task | Interval | Access | Skill Level |
|---|---|---|---|
| Visual inspection water lines / tank area | A-check <img src="https://img.shields.io/badge/TBD-red"> | Belly fairing panels | Line maintenance |
| EWP filter/strainer clean | C-check TBD | EWP access panel | Line/base |
| UV lamp replacement | Per lamp hours (TBD, ~6000 h) | UV unit access panel | Line maintenance |
| Activated carbon filter replacement | Per maintenance program (TBD) | Fill port access | Line maintenance |
| EWH drain and flush | Periodic (TBD) | Lavatory/galley access | Line maintenance |
| Waste tank rinse and drain | Per turn or operator program | Ground service panel | Line maintenance |
| Mast drain nozzle inspection | C-check TBD | Lower fuselage belly | Base maintenance |
| Trace heater continuity check | A-check or C-check TBD | Inspection panels | Line/base |
| Water quality sample | Per operator water program | Sample port | Line maintenance |
| BITE/CMC fault review | Each visit | CMC terminal | Line maintenance |

### 13.2 Off-Wing Maintenance

- EWP: shop overhaul per manufacturer CMM, TBD interval.
- EWH: bench test and thermostat calibration at TBD interval.
- Waste tank: removal for full clean and inspection at TBD interval per CS / operator.

---

## §14 S1000D/CSDB Mapping

| Document | DMC Pattern | Info Code | Status |
|---|---|---|---|
| System description (this document) | DMC-AMPEL360E-EWTW-038-00-00A-040A-A | 040 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| Fault isolation — ATA 38 general | DMC-AMPEL360E-EWTW-038-00-00A-400A-A | 400 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Inspection — ATA 38 general | DMC-AMPEL360E-EWTW-038-00-00A-300A-A | 300 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

Full DMRL mapping in [038-090](./038-090-S1000D-CSDB-Mapping-and-Traceability.md).

---

## §15 Footprints

| Parameter | Value |
|---|---|
| Potable water tank capacity | <img src="https://img.shields.io/badge/TBD-red"> (target ~80–120 L for 100 pax) |
| Potable water tank location | <img src="https://img.shields.io/badge/TBD-red"> (aft belly fairing or forward galley area) |
| Waste tank capacity (per tank) | <img src="https://img.shields.io/badge/TBD-red"> (~15–20 L per lavatory) |
| Waste tank count | <img src="https://img.shields.io/badge/TBD-red"> (~3 for 3 lavatories, or 1 consolidated) |
| Waste tank location | <img src="https://img.shields.io/badge/TBD-red"> (belly, aft of wing) |
| Mast drain count | <img src="https://img.shields.io/badge/TBD-red"> (~2–4) |
| EWH count | <img src="https://img.shields.io/badge/TBD-red"> (1 per galley point + 1 per lavatory) |
| EWH power per unit | <img src="https://img.shields.io/badge/TBD-red"> (typically 1–2 kW) |
| EWP flow rate | <img src="https://img.shields.io/badge/TBD-red"> |
| System mass (dry) | <img src="https://img.shields.io/badge/TBD-red"> |
| Lavatory count | <img src="https://img.shields.io/badge/TBD-red"> (~3 for 100-pax configuration) |

---

## §16 Safety and Certification

| Requirement | Standard | Application |
|---|---|---|
| Freeze protection | CS-25.1419 | Water lines in cold zones; trace heating; freeze alert to crew |
| Flammability of tank material | CS-25.853 | Potable water tank and waste tank material approval |
| Water quality (onboard) | WHO Guidelines for Drinking-water Quality (4th Ed.) | Potable water purity; UV sterilisation; activated carbon filtration |
| Commercial operations water quality | 14 CFR Part 121 Appendix A | US operators; water quality testing program |
| Lavatory waste and air quality | EASA AMC 25.831 | Waste tank ventilation; odour control; cabin air protection |
| Equipment installation general | CS-25.1301 | All ATA 38 equipment fit for purpose |
| System safety (failure effects) | CS-25.1309 | EWP, EWH, EVG interface; failure mode analysis |
| Backflow prevention | NRV requirement | Separate clean/dirty loops; NRVs at all branch points |
| Materials in contact with potable water | NSF/ANSI 61 or equivalent <img src="https://img.shields.io/badge/TBD-red"> | Tank, tubing, fittings, UV unit wetted parts |
| Electromagnetic compatibility | CS-25.1353 | EWP motor, EWH, UV lamp EMI |

---

## §17 Verification and Validation

| Test | Method | Acceptance Criterion | Status |
|---|---|---|---|
| EWP flow test | Bench + rig test at rated pressure | Flow rate ≥ TBD L/min at TBD bar | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Tank leak test | Hydrostatic test at 1.5× working pressure | No leakage for TBD minutes | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| EWH thermal test | Bench test; thermostat set-point verification | Outlet ≤ 60°C, TMV outlet ≤ 43°C TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| UV steriliser output test | UV intensity measurement; log reduction test | ≥ 4-log reduction of test organism TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Mast heater continuity test | Resistance measurement at installation | Within tolerance of rated resistance TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Flush cycle test | Functional test on rig; vacuum available | Waste transported in ≤ 1.5 s per cycle TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Fill-level sensor accuracy | Calibration check at 0%, 50%, 100% fill | ± TBD% accuracy | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Overflow sensor function | Simulated overfill; discrete output check | Alert within TBD seconds | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Grey water drain flow test | Functional test at max simultaneous sink load | All drains clear within TBD seconds | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Potable water quality test | Water sample analysis per WHO/14 CFR 121 App A | Meets potable water standard | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Freeze protection activation test | Cold chamber test at −40°C ambient TBD | THC activates heaters; no pipe freeze | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| BITE self-test | Powerup BITE cycle | No false faults; real faults correctly reported | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §18 Glossary

| Term | Definition |
|---|---|
| PWS | Potable Water System — the complete system supplying clean drinking water to galleys and lavatories |
| EWP | Electric Water Pump — motorised pump providing pressurised flow in the potable water distribution circuit |
| EWH | Electric Water Heater — point-of-use or storage electric heater providing hot water at galley and lavatory outlets |
| VWS | Vacuum Waste System — toilet waste collection system using vacuum transport (ATA 37 EVG) and storage tanks |
| EFV | Electric Flush Valve — solenoid-actuated valve controlling the vacuum flush cycle of a lavatory toilet |
| WIV | Waste Inlet Valve — valve connecting toilet bowl outlet to the waste collector line under vacuum |
| Mast drain | Overboard drain nozzle on lower fuselage through which grey water exits; electrically heated to prevent ice blockage |
| EMH | Electric Mast Heater — resistance heater element fitted to mast drain nozzle |
| UV sterilisation | Ultraviolet light treatment of potable water to inactivate micro-organisms |
| Activated carbon filter | Filter medium removing chlorine, taste, odour, and trace organics from potable water |
| LLDPE | Linear Low-Density Polyethylene — flexible tubing material approved for potable water service |
| PEX | Cross-linked Polyethylene — flexible tubing material approved for potable water service, higher temperature rating |
| Capacitive level sensor | Non-contact sensor measuring fluid level by change in electrical capacitance |
| NRV | Non-Return Valve — check valve preventing reverse flow (backflow prevention in potable water circuit) |
| TMV | Thermostatic Mixing Valve — valve mixing hot and cold water to deliver output at a controlled temperature |
| Grey water | Waste water from sinks (not toilet waste); drained overboard via mast drains |
| Black water | Toilet waste (liquid and solid); transported via vacuum system to waste tanks |
| Waste tank | Pressurised or unpressurised tank collecting toilet waste for ground removal |
| Freeze protection | System of trace heaters, sensors, and controller (THC) preventing potable water line freezing |
| Trace heating | Electrical resistance heating elements bonded to water lines to maintain above-freezing temperature |
| THC | Trace Heater Controller — controller unit monitoring temperature probes and switching trace heaters |
| CMC | Central Maintenance Computer — aircraft maintenance data system receiving sensor data from ATA 38 components |
| EAC | Electric Air Compressor — compressor providing low-pressure air for tank pressurisation (Option A) |

---

## §19 Citations

1. EASA Certification Specifications CS-25 (Large Aeroplanes), Subpart F, CS-25.853 — Compartment interiors.
2. EASA Certification Specifications CS-25, CS-25.1301 — Function and installation.
3. EASA Certification Specifications CS-25, CS-25.1309 — Equipment, systems, and installations.
4. EASA Certification Specifications CS-25, CS-25.1419 — Ice protection.
5. EASA AMC 25.831 — Ventilation; cabin air quality and lavatory waste.
6. World Health Organization, *Guidelines for Drinking-water Quality*, 4th Edition. Geneva: WHO, 2011.
7. 14 CFR Part 121 Appendix A — Aircraft Drinking Water Rule (ADWR).
8. NSF/ANSI 61 — Drinking Water System Components — Health Effects (or equivalent <img src="https://img.shields.io/badge/TBD-red">).
9. Q+ATLANTIDE ATLAS [037-000 Vacuum General](../037_Vacuum/037-000-Vacuum-General.md) — EVG interface reference.
10. Q+ATLANTIDE ATLAS [038-090 S1000D/CSDB Mapping](./038-090-S1000D-CSDB-Mapping-and-Traceability.md).

---

## §20 References

| Ref | Document | Notes |
|---|---|---|
| [R1] | CS-25.1419 | Ice protection requirements |
| [R2] | CS-25.853 | Material flammability for tank/line materials |
| [R3] | CS-25.1301 / CS-25.1309 | Equipment installation and system safety |
| [R4] | EASA AMC 25.831 | Lavatory waste and cabin air quality |
| [R5] | WHO Guidelines for Drinking-water Quality (4th Ed.) | Potable water quality standard |
| [R6] | 14 CFR Part 121 Appendix A | ADWR — US commercial operations water quality |
| [R7] | NSF/ANSI 61 <img src="https://img.shields.io/badge/TBD-red"> | Material contact with potable water |
| [R8] | ATA 37 — [037-000](../037_Vacuum/037-000-Vacuum-General.md) | Vacuum system interface |
| [R9] | ATA 24 — Electrical Power (ATLAS) | Power supply interface |
| [R10] | ATA 36 — Pneumatic (ATLAS) | EAC pressurisation option interface |

---

## §21 Open Issues

| ID | Description | Owner | Status |
|---|---|---|---|
| OI-038-001 | Potable water tank capacity and material (CFRP vs. PE-lined aluminium; capacity TBD based on galley/lav count and range) | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-002 | Tank pressurisation method (EAC bleed from ATA 36 vs. dedicated electric pump with bladder) | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-003 | EWH count, placement, and power budget | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-004 | Grey water retention requirement — regulatory review needed (overboard drain vs. retention tank) | Q-AIR / ORB-LEG | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-005 | Waste tank count and capacity (per-lavatory vs. consolidated) | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-006 | Freeze protection strategy for belly lines (trace heating vs. routing only through heated zones) | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-007 | UV sterilisation unit certification and maintenance interval | Q-AIR / ORB-LEG | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-008 | Mast drain count and location | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-009 | Single-point servicing panel location and configuration (combined potable + waste on one panel) | Q-AIR / Q-GROUND | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §22 Change Log

| Revision | Date | Author | Description |
|---|---|---|---|
| 0.1.0 | 2026-05-10 | Q+ATLANTIDE ATLAS Working Group | Initial full-template draft; all 23 sections populated; eWTW ATA 38 context incorporated |
| 0.0.0 | 2026-05-10 | Q+ATLANTIDE ATLAS Working Group | Scaffold stub created |
