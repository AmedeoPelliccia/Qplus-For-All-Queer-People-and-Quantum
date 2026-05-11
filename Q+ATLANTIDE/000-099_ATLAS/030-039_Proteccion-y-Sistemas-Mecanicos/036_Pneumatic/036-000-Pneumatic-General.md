---
document_id: "QATL-ATLAS-000099-ATLAS-030039-036-000"
title: "036-000 — Pneumatic — General"
short_title: "ATA 36 General"
subsubject: "000"
subsubject_title: "Pneumatic — General"
file_name: "036-000-Pneumatic-General.md"
sns_reference: "036-00"
dmc_prefix: "DMC-AMPEL360E-EWTW-036-00"
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
node_code: "036"
node_title: "Pneumatic"
node_link: "./"
parent_path: "Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/036_Pneumatic/"
parent_path_link: "./"
ata_reference: "ATA 36"
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
  atlas_node: "036_Pneumatic"
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
  - "ATA 36"
  - "Pneumatic"
  - "bleed-less architecture"
  - "EAC"
  - "Electric Air Compressor"
  - "no-bleed"
  - "CS-25.1438"
  - "eWTW"
---

# 036-000 — Pneumatic — General
### AMPEL360e eWTW · ATA 36 · Q+ATLANTIDE ATLAS Scaffold

---

## §0 Hyperlink Policy

All internal links in this document use relative paths from the current directory. External regulatory and standards references use anchor links defined in [§20 References](#20-references). Links marked **TBD** indicate targets not yet allocated within the CSDB or ATLAS hierarchy. Programme-level links traverse five directory levels (`../../../../../`) to reach the repository root. No absolute URLs are used for internal navigation.

---

## §1 Purpose

This document provides the top-level general description of ATA 36 — Pneumatic — as implemented on the AMPEL360e Wide Tube-and-Wing (eWTW) fully electric aircraft. It establishes the architectural philosophy, scope, and functional decomposition across nine subsubjects (036-010 through 036-090).

**Fundamental eWTW architectural difference**: The AMPEL360e eWTW is a **bleed-less / no-bleed** aircraft. Unlike conventional commercial transport aircraft that extract high-pressure, high-temperature air from engine compressor stages for pneumatic services (cabin pressurisation, wing anti-ice, hydraulic reservoir pressurisation), the eWTW **does not use engine bleed air for any purpose**. There are no High-Pressure (HP) or Low-Pressure (LP) bleed ports on the eWTW propulsion system. All functions traditionally served by engine bleed air are supplied by electric means on the eWTW.

ATA 36 on the eWTW therefore covers a **residual low-pressure pneumatic circuit** whose scope, necessity, and architecture remain **under architectural review** (see §21 Open Issues). If retained, the residual circuit provides pneumatic supply to a limited set of consumers: door seal inflation, potable water tank pressurisation, and ground pneumatic service. Air is sourced from one or more Electric Air Compressors (EAC) and/or a Ground Pneumatic Connector (external cart). Primary Q-Division is [Q-AIR](../../../../../Q-Divisions/Q-AIR/); supporting Q-Divisions are [Q-MECHANICS](../../../../../Q-Divisions/Q-MECHANICS/), [Q-DATAGOV](../../../../../Q-Divisions/Q-DATAGOV/), and [Q-GREENTECH](../../../../../Q-Divisions/Q-GREENTECH/).

---

## §2 Applicability

| Attribute | Value |
|---|---|
| Programme | AMPEL360e Wide Tube-and-Wing (eWTW) |
| ATA Chapter | 36 — Pneumatic |
| Aircraft Variant | eWTW-100 (baseline) |
| Propulsion | Full-electric (no engine bleed air; no hydraulic actuation) |
| Engine Bleed | **None** — bleed-less architecture |
| APU Bleed | **None** — no APU fitted; electric ground power unit equivalent |
| Residual Pneumatic | EAC-sourced low-pressure circuit (TBD — under review) |
| Working Pressure | <img src="https://img.shields.io/badge/TBD-red"> (estimated 3–50 psi range) |
| Certification Basis | CS-25.1438 (Pneumatic Systems); CS-25.1301/1309 |
| Environmental Std | DO-160G |
| S1000D Issue | 5.0 |
| SNS Reference | 036-00 |
| Applicability Code | ALL (all eWTW aircraft in programme) |
| Effectivity | From MSN 001 |

---

## §3 System / Function Overview

ATA 36 on the AMPEL360e eWTW covers the **residual low-pressure pneumatic system**, which is architecturally minimal compared to conventional bleed-air aircraft. The conventional ATA 36 scope on bleed-equipped aircraft includes: engine bleed air extraction, bleed valve control, cross-bleed manifold, high-temperature duct distribution, pre-coolers, and supply to ECS (ATA 21), wing anti-ice (ATA 30), and hydraulic reservoir pressurisation. **None of these apply to the eWTW.**

### 3.1 eWTW Pneumatic Consumers (If Residual Circuit Retained)

| Consumer | Nominal Pressure | Source | Status |
|---|---|---|---|
| Door seal inflation | 2–4 psi | EAC or ground | <img src="https://img.shields.io/badge/TBD-red"> |
| Potable water tank pressurisation | 3–5 psi | EAC or dedicated small pump | <img src="https://img.shields.io/badge/TBD-red"> |
| Ground pneumatic service | External cart | Ground connector | <img src="https://img.shields.io/badge/TBD-red"> |
| Wing anti-ice (ATA 30) | N/A | **NOT supplied by ATA 36** — electrothermal EWAI | Eliminated |
| Cabin pressurisation (ATA 21) | N/A | **NOT supplied by ATA 36** — EDC-sourced | Eliminated |
| Hydraulic reservoir pressurisation | N/A | **ELIMINATED** — no hydraulics | Eliminated |
| Pneumatic actuators | N/A | **ELIMINATED** — all electric actuators | Eliminated |
| Waste system | N/A | Vacuum waste — no pneumatic required | Eliminated |
| Rain repellent | N/A | Likely eliminated — TBD | <img src="https://img.shields.io/badge/TBD-red"> |

### 3.2 Residual EAC Architecture (If Retained)

If the ATA 36 pneumatic circuit is retained, the architecture consists of:
- One or two **Electric Air Compressors (EAC)** — motor-driven, sized for low-pressure, low-flow consumers
- **Air filter** (particulate, moisture separator)
- **Pressure regulator** — downstream of EAC, set point TBD
- **Pressure accumulator** — small buffer vessel for transient demand
- **Distribution manifold** — low-pressure, compact
- **Solenoid valves** — electrically controlled, normally closed, to each consumer branch
- **Check valves / NRV** — prevent backflow between branches
- **Pressure relief valve (PRV)** — overpressure protection
- **Pressure transducers** — manifold and branch monitoring

---

## §4 Scope

### 4.1 Included
- Residual low-pressure pneumatic circuit (if retained): EAC(s), filter, regulator, accumulator, manifold
- Pneumatic distribution lines to door seals and water tank (TBD)
- Solenoid shutoff valves (SOV) per consumer branch
- Check valves (NRV) and pressure relief valve (PRV)
- Ground pneumatic connector (external service receptacle, TBD)
- Manifold pressure transducers and branch pressure sensors
- CMC/OMS fault flagging for EAC and pressure faults
- Cockpit indication: EAC status, manifold pressure (if circuit retained)
- CAS alerts: "PNEU EAC FAULT" (amber), "PNEU LO PR" (amber)
- S1000D CSDB mapping for ATA 36 subsubjects (036-090)

### 4.2 Excluded
- Engine bleed air (NOT applicable — bleed-less architecture)
- APU bleed air (NOT applicable — no APU)
- Cross-bleed manifold (NOT applicable)
- Bleed valve / pre-cooler / HP/LP port (NOT applicable)
- Hot-air duct overheat (OHT) sensors (NOT required — no hot bleed)
- Wing anti-ice pneumatic supply (ATA 30 — electrothermal on eWTW)
- Cabin pressurisation pneumatic supply (ATA 21 — EDC-sourced)
- Hydraulic reservoir pressurisation (no hydraulics on eWTW)
- Pneumatic actuators (all electric on eWTW)

---

## §5 Architecture Description

### 5.1 Bleed-less Philosophy

The eWTW eliminates engine bleed by replacing bleed-supplied functions with electrically driven equivalents:
- **Cabin pressurisation (ATA 21)**: Electric Driven Compressors (EDC) — dedicated high-flow compressors, not part of ATA 36.
- **Wing anti-ice (ATA 30)**: Electrothermal Wing Anti-Ice (EWAI) system — electric heating mats in wing leading edge.
- **Engine nacelle anti-ice**: Electric (TBD).
- **Hydraulics**: ELIMINATED — eWTW is fully electric.

ATA 36 retains only the **residual low-pressure utility circuit** for functions that cannot be economically electrified (door seals, water tank pressurisation). Even these are under review for elimination or replacement by alternative means (e.g., electric compression door seals, electric water pump pressurisation).

### 5.2 EAC Configuration

| Parameter | Value |
|---|---|
| EAC quantity | <img src="https://img.shields.io/badge/TBD-red"> (1 or 2) |
| EAC type | Motor-driven reciprocating or scroll compressor |
| EAC rated pressure | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC rated flow | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC motor power | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC location | <img src="https://img.shields.io/badge/TBD-red"> (E/E bay or belly fairing) |
| EAC redundancy | <img src="https://img.shields.io/badge/TBD-red"> |
| Accumulator volume | <img src="https://img.shields.io/badge/TBD-red"> |
| Manifold material | <img src="https://img.shields.io/badge/TBD-red"> (aluminium alloy TBD) |
| Distribution tubing | <img src="https://img.shields.io/badge/TBD-red"> (aluminium, stainless, or PTFE-lined) |

---

## §6 Functional Breakdown

| Subsubject | Title | Status |
|---|---|---|
| 036-010 | Pneumatic Air Sources | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-020 | Pneumatic Air Distribution | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-030 | Pressure Regulation and Shutoff | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-040 | Pneumatic Valves, Ducts, and Manifolds | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-050 | Leak Detection and Overheat Protection | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-060 | Pneumatic System Indication and Warning | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-070 | Pneumatic Ground Service and Test Interfaces | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-080 | Pneumatic Monitoring, Diagnostics, and Control Interfaces | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-090 | S1000D / CSDB Mapping and Traceability | <img src="https://img.shields.io/badge/DRAFT-yellow"> |

---

## §7 System Context Diagram

```mermaid
flowchart LR
    subgraph SOURCES["Air Sources (ATA 36-010)"]
        EAC1["EAC-1\nElectric Air Compressor"]
        EAC2["EAC-2\n(TBD — if dual)"]
        GND["Ground Pneumatic\nConnector"]
    end
    subgraph COND["Conditioning (ATA 36-020/030)"]
        FLT["Air Filter"]
        REG["Pressure Regulator"]
        ACC["Accumulator"]
        PRV["Pressure Relief Valve"]
    end
    subgraph DIST["Distribution (ATA 36-040)"]
        MFD["Main Manifold"]
        SOV_DS["SOV — Door Seals"]
        SOV_WT["SOV — Water Tank"]
    end
    subgraph CONSUMERS["Consumers"]
        DS["Door Seals"]
        WT["Potable Water Tank\n(ATA 38)"]
    end
    subgraph MON["Monitoring (ATA 36-060/080)"]
        PT["Pressure Transducers"]
        CMC["CMC / OMS"]
        ECAM["ECAM / CAS"]
    end

    EAC1 --> FLT
    EAC2 --> FLT
    GND --> FLT
    FLT --> REG --> ACC --> MFD
    MFD --> PRV
    MFD --> SOV_DS --> DS
    MFD --> SOV_WT --> WT
    PT --> CMC --> ECAM

    style SOURCES fill:#e8f4fd,stroke:#2196F3
    style COND fill:#fff3e0,stroke:#FF9800
    style DIST fill:#e8f5e9,stroke:#4CAF50
    style CONSUMERS fill:#fce4ec,stroke:#E91E63
    style MON fill:#f3e5f5,stroke:#9C27B0
```

---

## §8 Internal Functional Architecture

```mermaid
flowchart TB
    A["Power ON / EAC Enable\n(from ELEC BUS — ATA 24)"]
    B["EAC Start Logic\n(CMC demand signal)"]
    C["EAC Compression\n(ambient → regulated pressure)"]
    D["Air Filter\n(particulate + moisture)"]
    E["Pressure Regulator\nSet-point TBD"]
    F{"Manifold Pressure\n≥ set-point?"}
    G["Accumulator Charged\n(pressure buffer)"]
    H["SOV Door Seals\n(open on demand)"]
    I["SOV Water Tank\n(open on demand)"]
    J["Door Seal Inflation\n2–4 psi"]
    K["Water Tank Pressurised\n3–5 psi"]
    L["Pressure Transducers\n(manifold + branch)"]
    M["CMC Fault Logic"]
    N["ECAM CAS Alert\nPNEU EAC FAULT / PNEU LO PR"]
    O["PRV Open on Overpressure\n(vent to atmosphere)"]

    A --> B --> C --> D --> E --> F
    F -- Yes --> G
    F -- No --> M
    G --> H --> J
    G --> I --> K
    L --> M --> N
    E --> O
```

---

## §9 Lifecycle Traceability

```mermaid
flowchart LR
    LC02["LC02\nRequirements\nDefinition"] --> LC03
    LC03["LC03\nArchitecture\nDefinition"] --> LC05
    LC05["LC05\nDetailed\nDesign"] --> LC06
    LC06["LC06\nVerification\nPlanning"] --> LC10
    LC10["LC10\nCertification\n/ Approval"] --> LC11
    LC11["LC11\nOperation"] --> LC12
    LC12["LC12\nMaintenance\n/ Support"]

    note1["Key Decision:\nRetain / Eliminate\nResidual Pneumatic?"]
    note2["CS-25.1438\nCompliance\nDemonstration"]
    note3["EAC Removal/Install\nS1000D DM Set"]

    LC03 --- note1
    LC10 --- note2
    LC12 --- note3
```

---

## §10 Interfaces

| Interface | ATA Chapter | Description | Direction |
|---|---|---|---|
| Electric power supply | ATA 24 | 28 VDC / 115 VAC for EAC motor, SOV actuation | ATA 24 → ATA 36 |
| ECS / Pressurisation | ATA 21 | No bleed supply from ATA 36; EDC is independent source | Informational |
| Wing Anti-Ice | ATA 30 | No bleed supply from ATA 36; EWAI is electric — cross-ref only | Informational |
| Potable Water | ATA 38 | Pneumatic pressurisation of water tank (TBD) | ATA 36 → ATA 38 |
| Doors | ATA 52 | Door seal inflation from manifold SOV (TBD) | ATA 36 → ATA 52 |
| CMC / OMS | ATA 45 | Fault flags, EAC status, pressure data via AFDX | ATA 36 → ATA 45 |
| ECAM / Display | ATA 31 | CAS alerts, EAC indication page | ATA 36 → ATA 31 |
| Ground Support | — | Ground pneumatic connector — external cart | External → ATA 36 |
| Propulsion | ATA 70–80 | **No interface** — no bleed ports on eWTW engines | None |
| APU | ATA 49 | **No interface** — no APU bleed on eWTW | None |

---

## §11 Operating Modes

| Mode | Description | EAC State | SOVs |
|---|---|---|---|
| Normal Flight | EAC on-demand; door seals inflated; water tank pressurised | Auto (demand) | Per consumer demand |
| Ground — Engines Running | EAC available (if retained); ground connector disconnected | Auto | Per consumer demand |
| Ground — GPU Only | EAC powered from ground power; ground connector may be connected | Auto or Manual | Per consumer demand |
| Maintenance | EAC manually commanded; circuit isolated for test | Manual via maintenance terminal | Manual |
| Fault — EAC Failure | CAS alert; accumulator provides residual pressure; graceful degradation | OFF / FAULT | Closed (no demand) |
| Fault — Pressure Loss | CMC flags PNEU LO PR; SOVs close; investigation required | Auto shutdown TBD | Closed |
| Ground Pneumatic Service | External cart connected to ground pneumatic connector | OFF (EAC bypassed) | Per service procedure |

---

## §12 Monitoring and Diagnostics

| Parameter | Sensor | Location | Threshold | CAS Alert |
|---|---|---|---|---|
| EAC status | Motor controller feedback | EAC unit | ON/OFF/FAULT | PNEU EAC FAULT (amber) |
| EAC outlet pressure | Pressure transducer | EAC outlet | <img src="https://img.shields.io/badge/TBD-red"> | PNEU LO PR (amber) |
| Manifold pressure | Pressure transducer | Main manifold | <img src="https://img.shields.io/badge/TBD-red"> | PNEU LO PR (amber) |
| Door seal pressure | Pressure transducer (TBD) | Per door (TBD) | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> |
| Water tank pressure | Pressure transducer | Water tank (ATA 38) | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC run hours | CMC accumulator | CMC | Maintenance interval TBD | Maintenance advisory |
| SOV position | Valve feedback (TBD) | Each SOV | Open/Closed | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §13 Maintenance Concept

### 13.1 Line Maintenance
- EAC filter replacement: scheduled interval TBD; accessible from <img src="https://img.shields.io/badge/TBD-red"> access panel
- Pressure transducer check: functional test via maintenance terminal
- SOV function test: open/close cycle via maintenance terminal
- System leak test: pressure decay test, acceptance criteria TBD

### 13.2 Base Maintenance
- EAC removal and installation: S1000D DM set (036-090 planned)
- Accumulator inspection / replacement: per pressure vessel inspection requirements
- Manifold inspection: visual and pressure test
- Ground connector inspection: coupling integrity, seal condition

### 13.3 Servicing
- Ground pneumatic connector: servicing procedure TBD (AMM ATA 36-070)
- EAC does not require fluid servicing (dry compression — TBD if oil-free scroll type confirmed)

---

## §14 S1000D / CSDB Mapping

| Subsubject | SNS | DMC Prefix | DM Types Planned | Status |
|---|---|---|---|---|
| 036-000 | 036-00 | DMC-AMPEL360E-EWTW-036-00 | 040 (Desc), 300 (Insp) | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-010 | 036-10 | DMC-AMPEL360E-EWTW-036-10 | 040, 300, 520, 720 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-020 | 036-20 | DMC-AMPEL360E-EWTW-036-20 | 040, 300 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-030 | 036-30 | DMC-AMPEL360E-EWTW-036-30 | 040, 300, 520, 720 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-040 | 036-40 | DMC-AMPEL360E-EWTW-036-40 | 040, 300 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-050 | 036-50 | DMC-AMPEL360E-EWTW-036-50 | 040, 300, 400 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-060 | 036-60 | DMC-AMPEL360E-EWTW-036-60 | 040, 300 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-070 | 036-70 | DMC-AMPEL360E-EWTW-036-70 | 040, 300, 400 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-080 | 036-80 | DMC-AMPEL360E-EWTW-036-80 | 040, 300, 400 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 036-090 | 036-90 | DMC-AMPEL360E-EWTW-036-90 | 040 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |

---

## §15 Footprints

| Item | Mass (kg) | Volume (L) | Location | Status |
|---|---|---|---|---|
| EAC-1 | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC-2 (if dual) | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> |
| Air filter | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> |
| Pressure regulator | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> |
| Accumulator | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> |
| Manifold + valves | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> |
| Distribution tubing | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | Throughout fuselage | <img src="https://img.shields.io/badge/TBD-red"> |
| Ground connector | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | Lower fuselage panel | <img src="https://img.shields.io/badge/TBD-red"> |
| **Total ATA 36** | <img src="https://img.shields.io/badge/TBD-red"> | — | — | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §16 Safety and Certification

| Requirement | Standard | Applicability | Notes |
|---|---|---|---|
| Pneumatic systems design | CS-25.1438 | Full | Primary certification paragraph for ATA 36 on eWTW |
| Equipment and installations | CS-25.1301 | Full | General equipment requirements |
| Systems and installations | CS-25.1309 | Full | Failure mode, effects, and criticality analysis (FMECA) required |
| Environmental qualification | DO-160G | Full (pressurised components) | Temperature, vibration, humidity per equipment category |
| Bleed air contamination | CS-25.831 | **Not applicable** | No bleed air — eWTW architecture eliminates this hazard |
| Ventilation | CS-25.831 | Informational only | No bleed air contamination pathway |
| Pressure vessel (accumulator) | CS-25.1438 + authority PED | Full | Accumulator design proof pressure TBD |

### 16.1 Failure Effects (High Level)

| Failure | Effect | Classification |
|---|---|---|
| EAC-1 failure (if single EAC) | Loss of pneumatic supply; accumulator provides transient; door seals may deflate after accumulator depletion | <img src="https://img.shields.io/badge/TBD-red"> |
| Manifold pressure loss | Potential door seal deflation; water tank depressurisation | <img src="https://img.shields.io/badge/TBD-red"> |
| SOV stuck open (door seal branch) | Door seal over-pressurisation (limited by PRV) | <img src="https://img.shields.io/badge/TBD-red"> |
| SOV stuck closed (door seal branch) | Door seal not inflated — door sealing degraded | <img src="https://img.shields.io/badge/TBD-red"> |
| PRV fails open | Continuous vent — loss of system pressure | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §17 Verification and Validation

| V&V Activity | Method | Acceptance Criteria | Status |
|---|---|---|---|
| EAC functional test | Ground test — power EAC, measure outlet pressure and flow | Pressure ≥ set-point; flow ≥ TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Regulator set-point verification | Ground test — downstream pressure measurement | Set-point ± TBD % | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| SOV open/close test | Ground test — command SOV, verify position feedback and downstream pressure change | Open: pressure downstream; Closed: no flow | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| System leak test (pressure decay) | Pressurize circuit to TBD psi, isolate EAC, monitor for TBD min | Pressure decay < TBD psi/min | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Ground connector coupling test | Connect ground pneumatic cart, verify supply to manifold | Manifold pressure achieved within TBD s | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Manifold pressure indication accuracy | Compare transducer output vs. reference gauge | ± TBD psi | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| CMC fault flag verification | Induce EAC fault; verify CMC flags and CAS alert | "PNEU EAC FAULT" within TBD s | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| CS-25.1438 compliance demonstration | Analysis + test | Authority acceptance | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DO-160G environmental qualification | Test per DO-160G categories | Pass all applicable categories | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §18 Glossary

| Term | Definition |
|---|---|
| ATA 36 | Air Transport Association chapter 36 — Pneumatic systems |
| Bleed-less architecture | Aircraft design in which no engine compressor bleed air is extracted; all pneumatic functions replaced by electric equivalents |
| EAC | Electric Air Compressor — motor-driven compressor providing low-pressure air for residual pneumatic consumers on eWTW |
| EDC | Electric Driven Compressor — high-flow compressor for cabin pressurisation (ATA 21); distinct from EAC |
| SOV | Shutoff Valve — electrically actuated solenoid valve controlling flow to a consumer branch |
| PRV | Pressure Relief Valve — prevents system overpressure by venting to atmosphere at set threshold |
| NRV | Non-Return Valve — check valve preventing reverse flow |
| OHT | Overheat sensor / loop — used on conventional aircraft to detect hot bleed duct rupture; **not required on eWTW** (no hot bleed) |
| CPCS | Cabin Pressure Control System (ATA 21) — sourced by EDC on eWTW, not by ATA 36 EAC |
| Manifold | Distribution header connecting pneumatic supply to multiple consumer branches |
| Accumulator | Pressurised vessel providing transient buffer capacity to maintain manifold pressure during EAC start lag or brief demand surges |
| Working pressure | Nominal operating pressure of the residual pneumatic circuit — TBD (3–50 psi range) |
| Ground pneumatic connector | External service receptacle on fuselage allowing connection of ground pneumatic cart for maintenance or servicing |
| CS-25.1438 | EASA Certification Specification paragraph governing pneumatic system design for large aeroplanes |
| DO-160G | RTCA standard for environmental conditions and test procedures for airborne equipment |
| CAS | Crew Alerting System — cockpit alert presentation layer |
| ECAM | Electronic Centralised Aircraft Monitor — multi-function display system for system status and alerts |
| CMC | Central Maintenance Computer — on-board system for fault recording, BITE, and maintenance support |
| EWAI | Electrothermal Wing Anti-Ice — electric heating system for wing leading edge ice protection (ATA 30); replaces bleed anti-ice |
| AFDX | Avionics Full-Duplex Switched Ethernet — aircraft data communication bus |

---

## §19 Citations

1. EASA Certification Specifications CS-25 Subpart F — Equipment, §25.1438 (Pneumatic Systems)
2. EASA CS-25 §25.1301 — Equipment and Installations (Function and Installation)
3. EASA CS-25 §25.1309 — Equipment, Systems, and Installations
4. RTCA DO-160G — Environmental Conditions and Test Procedures for Airborne Equipment
5. S1000D Issue 5.0 — International Specification for Technical Publications
6. ATA iSpec 2200 — Information Standards for Aviation Maintenance
7. ATA Chapter 36 — Pneumatic (SNS reference)
8. Q+ATLANTIDE ATLAS Node 036 — eWTW architectural framework
9. AMPEL360e eWTW System Architecture Document (SAD) — TBD reference
10. Q-AIR Division Technical Standard — Bleed-less Architecture Design Rules — TBD

---

## §20 References

| Ref ID | Document | Source | Link |
|---|---|---|---|
| [ATA36] | ATA iSpec 2200 Chapter 36 — Pneumatic | ATA | — |
| [CS25-1438] | CS-25 §25.1438 Pneumatic Systems | EASA | https://www.easa.europa.eu/ |
| [CS25-1301] | CS-25 §25.1301 Equipment and Installations | EASA | https://www.easa.europa.eu/ |
| [CS25-1309] | CS-25 §25.1309 Systems and Installations | EASA | https://www.easa.europa.eu/ |
| [DO-160G] | RTCA DO-160G Environmental Qualification | RTCA | https://www.rtca.org/ |
| [S1000D] | S1000D Issue 5.0 | ASD/AIA | https://s1000d.org/ |
| [ATA21] | ATA 21 — Air Conditioning / Pressurisation | Internal | [036-080](./036-080-Pneumatic-Monitoring-Diagnostics-and-Control-Interfaces.md) |
| [ATA30] | ATA 30 — Ice and Rain Protection | Internal | [036-050](./036-050-Leak-Detection-and-Overheat-Protection.md) |
| [ATA38] | ATA 38 — Water / Waste | Internal | [036-020](./036-020-Pneumatic-Air-Distribution.md) |
| [ATA52] | ATA 52 — Doors | Internal | [036-040](./036-040-Pneumatic-Valves-Ducts-and-Manifolds.md) |

---

## §21 Open Issues

| Issue ID | Description | Owner | Priority | Status |
|---|---|---|---|---|
| OI-036-001 | **Retain or eliminate ATA 36 residual pneumatic circuit**: architectural decision on whether any pneumatic circuit is needed on eWTW | Q-AIR | Critical | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-002 | **Door seal technology**: pneumatic inflation vs. electric compression seal (e.g., inflatable rubber vs. electric motor-driven compression) — TBD | Q-MECHANICS | High | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-003 | **Potable water pressurisation method**: pneumatic EAC vs. dedicated electric pump vs. bladder-type pressurisation — TBD | Q-AIR / ATA 38 | High | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-004 | **EAC sizing and quantity**: rated pressure, flow, power, single vs. dual EAC — depends on consumer finalisation | Q-AIR | High | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-005 | **Ground pneumatic connector retention**: whether to retain standard ground pneumatic receptacle or replace with ground electric supply only | Q-AIR | Medium | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-006 | **Manifold material and routing**: aluminium vs. stainless vs. PTFE-lined; routing through composite fuselage (bonding, grounding, penetration sealing) | Q-MECHANICS | Medium | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-007 | **Rain repellent system**: conventional rain repellent uses pneumatic blow — TBD if eliminated or retained on eWTW | Q-AIR | Low | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-008 | **CS-25.1438 compliance pathway**: formal compliance document and agreed test plan with authority — not yet initiated | Q-AIR / ORB-LEG | High | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §22 Change Log

| Revision | Date | Author | Description |
|---|---|---|---|
| 0.1.0 | 2026-05-10 | Q+ATLANTIDE scaffold generator | Initial full-template scaffold — all sections present; content TBD/DRAFT |
