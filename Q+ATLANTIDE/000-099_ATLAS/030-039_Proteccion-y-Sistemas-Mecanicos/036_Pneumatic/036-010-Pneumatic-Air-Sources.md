---
document_id: "QATL-ATLAS-000099-ATLAS-030039-036-010"
title: "036-010 — Pneumatic Air Sources"
short_title: "ATA 36 Air Sources"
subsubject: "010"
subsubject_title: "Pneumatic Air Sources"
file_name: "036-010-Pneumatic-Air-Sources.md"
sns_reference: "036-10"
dmc_prefix: "DMC-AMPEL360E-EWTW-036-10"
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
  - "Electric Air Compressor"
  - "EAC"
  - "no bleed"
  - "bleed-less"
  - "ground pneumatic connector"
  - "CS-25.1438"
---

# 036-010 — Pneumatic Air Sources
### AMPEL360e eWTW · ATA 36 · Q+ATLANTIDE ATLAS Scaffold

---

## §0 Hyperlink Policy

All internal links in this document use relative paths from the current directory. External regulatory and standards references use anchor links defined in [§20 References](#20-references). Links marked **TBD** indicate targets not yet allocated within the CSDB or ATLAS hierarchy. Programme-level links traverse five directory levels (`../../../../../`) to reach the repository root. No absolute URLs are used for internal navigation.

---

## §1 Purpose

This document describes the pneumatic air sources for the AMPEL360e eWTW residual pneumatic circuit (ATA 36-010). The most critical architectural fact is stated at the outset:

> **The AMPEL360e eWTW has NO engine bleed air. There are no HP or LP bleed ports on the eWTW propulsion system. There is no APU bleed air. All functions conventionally served by engine bleed are provided by electric systems.**

ATA 36 air sources on the eWTW are therefore limited to:
1. **Electric Air Compressor(s) (EAC)** — on-board, motor-driven, providing low-pressure air for residual pneumatic consumers (door seals, water tank pressurisation — TBD per §21 Open Issues).
2. **Ground Pneumatic Connector** — external receptacle for connection of ground pneumatic cart during maintenance and ground servicing operations.

This document defines the EAC specifications (to the extent known), the ground connector interface, the control and monitoring provisions, and the S1000D mapping for this subsubject.

---

## §2 Applicability

| Attribute | Value |
|---|---|
| Programme | AMPEL360e Wide Tube-and-Wing (eWTW) |
| ATA Subsubject | 036-010 — Pneumatic Air Sources |
| Engine Bleed | **None** — bleed-less architecture |
| APU Bleed | **None** — no APU; electric ground power equivalent |
| On-board Air Source | Electric Air Compressor(s) (EAC) |
| Ground Air Source | Ground Pneumatic Connector (external cart) |
| EAC Quantity | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC Rated Pressure | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC Rated Flow | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC Motor Power | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC Location | <img src="https://img.shields.io/badge/TBD-red"> |
| Ground Connector Type | <img src="https://img.shields.io/badge/TBD-red"> (standard aircraft pneumatic coupling TBD) |
| Ground Connector Location | Lower fuselage panel — <img src="https://img.shields.io/badge/TBD-red"> |
| Certification Basis | CS-25.1438; CS-25.1301/1309 |
| Environmental Std | DO-160G |
| S1000D SNS | 036-10 |

---

## §3 System / Function Overview

### 3.1 Conventional Aircraft vs. eWTW

| Feature | Conventional (bleed) | eWTW (bleed-less) |
|---|---|---|
| Primary air source | Engine HP/LP compressor bleed | **None** (no bleed) |
| APU air source | APU bleed compressor | **None** (no APU) |
| Cross-bleed capability | Cross-bleed manifold with isolation valve | **Not applicable** |
| Pre-cooler | Heat exchanger (fan air vs. bleed) | **Not applicable** |
| Bleed valve | Modulating bleed valve per engine | **Not applicable** |
| On-board electric compressor | Generally none for pneumatic | **EAC** (primary source) |
| Ground air source | Ground air cart | Ground pneumatic connector (if retained) |

### 3.2 EAC Function

The EAC(s) compress ambient air to the circuit working pressure (TBD, estimated 3–50 psi) to supply the residual pneumatic manifold. Key operational aspects:
- Commanded ON by CMC or manual maintenance switch
- Runs as-needed (demand-based control or continuous — TBD)
- Motor powered from aircraft electrical bus (ATA 24)
- Outlet air passes through filter, then pressure regulator, to manifold and accumulator
- EAC is non-bleed — no engine interface, no cross-bleed, no pre-cooler

### 3.3 Ground Pneumatic Connector Function

The ground pneumatic connector (if retained) provides an interface for:
- Maintenance blow-down of residual circuit
- Door seal inflation test with EAC de-energised
- Water tank pressurisation from ground (if EAC not used on ground for servicing)
- Cargo hold pneumatic cleaning (if applicable — TBD)
- Supply to circuit during maintenance procedures where EAC isolation is required

---

## §4 Scope

### 4.1 Included
- Electric Air Compressor(s) (EAC): motor unit, compression head, outlet port, local temperature and pressure sensors
- EAC inlet filter / air intake (ambient air intake with screen — location TBD)
- EAC motor controller and enable/disable interface (to CMC/ELMS)
- EAC outlet check valve (NRV — prevents backflow from accumulator into EAC on shutdown)
- Ground pneumatic connector: receptacle body, coupling, check valve, dust cap, location panel
- Ground connector isolation valve (solenoid — prevents ground air from entering when not connected)
- Interconnecting plumbing from EAC outlet to main filter inlet (ATA 36-020 interface)
- Interconnecting plumbing from ground connector to main filter inlet (ATA 36-020 interface)

### 4.2 Excluded
- Engine bleed valves / HP/LP ports (not applicable)
- APU bleed (not applicable)
- Pre-cooler / heat exchanger (not applicable)
- Main filter, pressure regulator, accumulator, manifold (covered in ATA 36-020/030/040)
- ECS EDC (ATA 21 — separate system, not ATA 36)
- Wing anti-ice (ATA 30 — electrothermal, no ATA 36 supply)

---

## §5 Architecture Description

### 5.1 EAC Architecture Options Under Review

| Option | Description | Status |
|---|---|---|
| Option A — Single EAC | One EAC sized for all residual consumers; accumulator provides buffer | <img src="https://img.shields.io/badge/TBD-red"> |
| Option B — Dual EAC | Two EACs (active/standby); improved availability; higher cost/mass | <img src="https://img.shields.io/badge/TBD-red"> |
| Option C — No EAC | Eliminate ATA 36 entirely; replace consumers with electric alternatives | <img src="https://img.shields.io/badge/TBD-red"> |

**Decision required**: See OI-036-001 and OI-036-004 in §21.

### 5.2 EAC Preliminary Specification (TBD)

| Parameter | Preliminary Estimate | Status |
|---|---|---|
| Compressor type | Scroll (oil-free) or diaphragm — TBD | <img src="https://img.shields.io/badge/TBD-red"> |
| Rated outlet pressure | TBD (estimated 50 psi max, regulated to consumer req.) | <img src="https://img.shields.io/badge/TBD-red"> |
| Rated flow (SCFM) | TBD (low — door seals + water tank only) | <img src="https://img.shields.io/badge/TBD-red"> |
| Motor type | Brushless DC or 3-phase AC — TBD | <img src="https://img.shields.io/badge/TBD-red"> |
| Motor rated power | TBD (estimated < 500 W) | <img src="https://img.shields.io/badge/TBD-red"> |
| Supply voltage | 28 VDC or 115 VAC — TBD (from ATA 24) | <img src="https://img.shields.io/badge/TBD-red"> |
| Ambient temp range | −40°C to +70°C per DO-160G | <img src="https://img.shields.io/badge/TBD-red"> |
| Altitude qualification | Ground to 43,000 ft (outlet pressure maintained by regulator) | <img src="https://img.shields.io/badge/TBD-red"> |
| Mass (est.) | TBD | <img src="https://img.shields.io/badge/TBD-red"> |
| MTBF (est.) | TBD | <img src="https://img.shields.io/badge/TBD-red"> |
| Oil-free | Yes (assumed — avoids oil contamination of pneumatic circuit) | <img src="https://img.shields.io/badge/TBD-red"> |

### 5.3 Ground Pneumatic Connector Specification (TBD)

| Parameter | Value |
|---|---|
| Connector standard | TBD (e.g., standard 2.5" aircraft pneumatic quick-disconnect) |
| Location | Lower fuselage skin panel — <img src="https://img.shields.io/badge/TBD-red"> |
| Max supply pressure from cart | <img src="https://img.shields.io/badge/TBD-red"> psi |
| Check valve | Yes — prevents backflow into ground cart when EAC active |
| Dust cap / cover | Hinged or removable — TBD |
| Ground isolation solenoid | TBD (normally closed solenoid — opens when cart connected and system enabled) |

---

## §6 Functional Breakdown

| Function | Component | Controlled By | Status |
|---|---|---|---|
| Air compression (on-board) | EAC motor + head | CMC / maintenance switch | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC enable/disable | Motor controller relay | CMC (AFDX command) | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC outlet NRV | Check valve | Passive (self-actuating) | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC air intake | Inlet screen + filter | Passive | <img src="https://img.shields.io/badge/TBD-red"> |
| Ground air supply | Ground connector + isolation valve | Ground crew / maintenance terminal | <img src="https://img.shields.io/badge/TBD-red"> |
| Source selection (EAC vs. ground) | NRV architecture (no active switching) | Passive priority | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §7 System Context Diagram

```mermaid
flowchart LR
    subgraph ELEC["Electrical Power (ATA 24)"]
        BUS["Aircraft Electrical Bus\n28 VDC / 115 VAC TBD"]
    end
    subgraph SOURCES["ATA 36-010: Air Sources"]
        EAC["EAC\nElectric Air Compressor\n(motor + head)"]
        NRV_EAC["NRV\n(EAC outlet check valve)"]
        GND_CONN["Ground Pneumatic\nConnector"]
        GND_ISO["Ground Isolation\nSolenoid Valve\n(TBD)"]
        INLET["EAC Air Intake\n(ambient air + screen)"]
    end
    subgraph DOWNSTREAM["ATA 36-020/030: Distribution"]
        FILTER["Main Air Filter"]
        REG["Pressure Regulator"]
        MANIFOLD["Manifold"]
    end
    subgraph CMC_INT["CMC / OMS (ATA 45)"]
        CMC["CMC\nEAC Status / Fault Flags"]
    end
    subgraph GND_EXT["External (Ground)"]
        CART["Ground Pneumatic Cart"]
    end

    BUS --> EAC
    INLET --> EAC
    EAC --> NRV_EAC --> FILTER
    CART --> GND_CONN --> GND_ISO --> FILTER
    FILTER --> REG --> MANIFOLD
    EAC --> CMC
    GND_ISO --> CMC

    style SOURCES fill:#e8f4fd,stroke:#2196F3
    style ELEC fill:#fff8e1,stroke:#FFC107
    style DOWNSTREAM fill:#e8f5e9,stroke:#4CAF50
    style CMC_INT fill:#f3e5f5,stroke:#9C27B0
    style GND_EXT fill:#fce4ec,stroke:#E91E63
```

---

## §8 Internal Functional Architecture

```mermaid
flowchart TB
    A["Aircraft Power Available\n(ATA 24 bus energised)"]
    B{"EAC Enable\nCommand?"}
    C["CMC Demand Signal\nor Manual Switch"]
    D["EAC Motor\nEnergised"]
    E["Air Intake\n(ambient filtered)"]
    F["Compression Stage\n(scroll/diaphragm TBD)"]
    G["EAC Outlet\nPressure Sensor"]
    H["NRV (Check Valve)\nPrevents Backflow"]
    I["To Main Filter\n(ATA 36-020)"]
    J{"EAC Fault\nDetected?"}
    K["CMC Fault Flag\nPNEU EAC FAULT"]
    L["EAC BITE\nSelf-Test on Power-Up"]
    M["Ground Connector\n(alternative path — maintenance)"]

    A --> B
    C --> B
    B -- Yes --> D
    D --> E --> F --> G --> H --> I
    G --> J
    J -- Yes --> K
    A --> L
    M --> I
```

---

## §9 Lifecycle Traceability

```mermaid
flowchart LR
    LC02["LC02\nRequirements\n(EAC performance req.)"] --> LC03
    LC03["LC03\nArchitecture\n(EAC type selection)"] --> LC05
    LC05["LC05\nDetailed Design\n(EAC + connector spec)"] --> LC06
    LC06["LC06\nV&V Planning\n(EAC test plan)"] --> LC10
    LC10["LC10\nCertification\n(CS-25.1438)"] --> LC11
    LC11["LC11\nOperation\n(EAC monitoring)"] --> LC12
    LC12["LC12\nMaintenance\n(EAC removal/install DM)"]

    OI1["OI-036-001\nRetain/Eliminate\nDecision"]
    OI4["OI-036-004\nEAC Sizing\nDecision"]

    LC02 --- OI1
    LC03 --- OI4
```

---

## §10 Interfaces

| Interface | ATA Chapter | Description | Direction |
|---|---|---|---|
| Electrical power | ATA 24 | 28 VDC / 115 VAC for EAC motor, ground isolation SOV | ATA 24 → ATA 36 |
| CMC / OMS | ATA 45 | EAC enable/disable command, EAC status, fault flags, run hours | ATA 36 ↔ ATA 45 |
| Main air filter | ATA 36-020 | EAC outlet air to main filter (downstream boundary) | ATA 36-010 → ATA 36-020 |
| Ground connector | — | External ground pneumatic cart (maintenance) | External → ATA 36-010 |
| ECS / Pressurisation | ATA 21 | **No interface** — EDC is separate source; EAC does NOT supply ATA 21 | None |
| Wing Anti-Ice | ATA 30 | **No interface** — electrothermal; EAC does NOT supply ATA 30 | None |
| APU | ATA 49 | **No interface** — no APU on eWTW | None |
| Propulsion | ATA 70–80 | **No interface** — no bleed ports | None |

---

## §11 Operating Modes

| Mode | EAC State | Ground Connector | Description |
|---|---|---|---|
| Normal flight — demand met | Running | Disconnected | EAC supplies manifold; accumulator buffering |
| Normal flight — demand satisfied | Standby / OFF | Disconnected | EAC idle; accumulator maintains pressure |
| Ground — GPU power | Available (demand) | Disconnected (or connected) | EAC operable from ground power |
| Ground maintenance | Manual command | May be connected | EAC or ground cart supplies circuit for test |
| EAC FAULT | OFF / FAULT | N/A | CMC flags fault; accumulator provides residual |
| Ground pneumatic service | OFF (isolated) | Connected (cart) | Ground cart provides air; EAC isolated by NRV |
| Post-maintenance | Reset by CMC | Disconnected | EAC re-enabled after maintenance release |

---

## §12 Monitoring and Diagnostics

| Parameter | Sensor | Threshold | Alert | Destination |
|---|---|---|---|---|
| EAC ON/OFF status | Motor controller relay feedback | — | Annunciation | CMC, ECAM |
| EAC FAULT | Motor controller fault output | Over-current / overtemp / stall | PNEU EAC FAULT (amber CAS) | CMC, ECAM |
| EAC outlet pressure | Pressure transducer (EAC outlet) | Below set-point | PNEU LO PR (amber CAS) | CMC, ECAM |
| EAC run hours | CMC software accumulator | Maintenance interval TBD | Maintenance advisory | CMC |
| EAC motor temperature | Motor winding thermistor (TBD) | Over-temp TBD | PNEU EAC FAULT | CMC |
| Ground connector status | Micro-switch or pressure sense (TBD) | Connected/Disconnected | Indication (maintenance terminal) | CMC |
| BITE | EAC built-in self-test | Power-up and commanded | Pass/Fail | CMC, maintenance terminal |

---

## §13 Maintenance Concept

### 13.1 On-Wing Maintenance (Line)
- **EAC filter/inlet screen inspection**: scheduled interval TBD; access via <img src="https://img.shields.io/badge/TBD-red"> access panel; refer to S1000D DM 036-10-00 (Inspect)
- **EAC BITE check**: commanded via maintenance terminal; pass/fail result logged in CMC
- **EAC run-hour check**: CMC readout; compare to maintenance interval
- **Ground connector inspection**: dust cap condition, coupling wear, seal condition — visual

### 13.2 Base / Heavy Maintenance
- **EAC removal**: S1000D DM DMC-AMPEL360E-EWTW-036-10-520 (Remove) — TBD
- **EAC installation**: S1000D DM DMC-AMPEL360E-EWTW-036-10-720 (Install) — TBD
- **EAC functional test post-install**: DM DMC-AMPEL360E-EWTW-036-10-300 (Inspect/Check)
- **Ground connector replacement**: TBD

### 13.3 Consumables
- EAC inlet filter element: P/N <img src="https://img.shields.io/badge/TBD-red">; interval TBD
- EAC (if non-repairable unit): P/N <img src="https://img.shields.io/badge/TBD-red">; LLP / on-condition TBD

---

## §14 S1000D / CSDB Mapping

| DM Code (planned) | Info Code | Title | Status |
|---|---|---|---|
| DMC-AMPEL360E-EWTW-036-10-00A-040A-A | 040 | ATA 36-010 — Pneumatic Air Sources — Description | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| DMC-AMPEL360E-EWTW-036-10-00A-300A-A | 300 | ATA 36-010 — EAC Inspection | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-AMPEL360E-EWTW-036-10-00A-520A-A | 520 | ATA 36-010 — EAC Removal | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-AMPEL360E-EWTW-036-10-00A-720A-A | 720 | ATA 36-010 — EAC Installation | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-AMPEL360E-EWTW-036-10-00A-400A-A | 400 | ATA 36-010 — EAC Fault Isolation | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §15 Footprints

| Item | Mass (kg) | Volume (L) | Location | Status |
|---|---|---|---|---|
| EAC-1 (compressor unit) | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC-2 (if dual) | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC motor controller | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> |
| NRV (EAC outlet) | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | Adjacent to EAC | <img src="https://img.shields.io/badge/TBD-red"> |
| Ground pneumatic connector | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | Lower fuselage panel | <img src="https://img.shields.io/badge/TBD-red"> |
| Ground isolation SOV | <img src="https://img.shields.io/badge/TBD-red"> | <img src="https://img.shields.io/badge/TBD-red"> | Near ground connector | <img src="https://img.shields.io/badge/TBD-red"> |
| **Total 036-010** | <img src="https://img.shields.io/badge/TBD-red"> | — | — | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §16 Safety and Certification

| Requirement | Standard | Applicability | Notes |
|---|---|---|---|
| Pneumatic systems | CS-25.1438 | Full | EAC as pneumatic source |
| Equipment and installations | CS-25.1301 | Full | EAC motor and controller installation |
| Systems and installations | CS-25.1309 | Full | EAC failure mode analysis; DAL TBD |
| Environmental qualification | DO-160G | EAC, motor controller, transducers | Temperature, vibration, humidity |
| Electrical systems | CS-25.1353 | Full (motor power wiring) | Battery and electrical system protection |
| Fire protection | CS-25.1197/1203 | Informational | EAC not bleed — no hot duct fire risk; motor overtemp is only thermal concern |
| Oil contamination | N/A | Not applicable if oil-free EAC | Oil-free compressor eliminates contamination risk |

### 16.1 Key Safety Note
Unlike conventional bleed air sources (which operate at 200–500°C and 40–60 psi), the EAC on the eWTW provides low-pressure, near-ambient-temperature air. There is **no hot bleed air hazard** associated with the ATA 36 air source on the eWTW. The EAC failure modes are primarily: motor overtemperature, motor stall, bearing failure (compressor), and controller failure.

---

## §17 Verification and Validation

| V&V Activity | Method | Acceptance Criteria | Status |
|---|---|---|---|
| EAC functional test | Ground test — power EAC, measure outlet pressure and flow at rated conditions | Pressure ≥ set-point TBD; flow ≥ TBD SCFM | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| EAC BITE self-test | Commanded via maintenance terminal on power-up | BITE PASS reported to CMC within TBD s | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| EAC fault flag verification | Induce EAC motor overcurrent; verify CMC fault flag and CAS alert | "PNEU EAC FAULT" within TBD s | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Ground connector coupling test | Connect calibrated ground cart; verify supply to manifold | Manifold pressure achieved within TBD s; no leak at coupling | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| NRV backflow test | Pressurize downstream; confirm no flow back through EAC outlet NRV | Zero backflow (< TBD leakage rate) | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| EAC run-hour CMC accumulation | Run EAC for known duration; verify CMC hour count | CMC hours ± TBD min | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DO-160G environmental qualification | Test per DO-160G categories (EAC unit) | Pass per applicable categories | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| CS-25.1438 compliance | Analysis + test evidence submission | Authority acceptance | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §18 Glossary

| Term | Definition |
|---|---|
| EAC | Electric Air Compressor — on-board motor-driven compressor providing low-pressure air for residual pneumatic consumers on eWTW |
| EDC | Electric Driven Compressor — high-flow compressor for cabin pressurisation (ATA 21); a separate, larger system not part of ATA 36 |
| Bleed-less architecture | Aircraft design with no engine compressor bleed air extraction |
| NRV | Non-Return Valve — check valve preventing reverse flow through EAC outlet on shutdown |
| SOV | Shutoff Valve — electrically actuated solenoid valve |
| BITE | Built-In Test Equipment — self-test logic within the EAC motor controller |
| CMC | Central Maintenance Computer — on-board fault recording and maintenance support system |
| OHT | Overheat sensor — used on conventional bleed duct systems; **not required on eWTW ATA 36** |
| Ground pneumatic connector | External service receptacle on fuselage for connection of ground pneumatic cart |
| CS-25.1438 | EASA CS-25 paragraph governing pneumatic system design |
| DO-160G | RTCA environmental qualification standard for airborne equipment |
| AFDX | Avionics Full-Duplex Switched Ethernet — aircraft data bus for CMC interface |
| CAS | Crew Alerting System |
| ECAM | Electronic Centralised Aircraft Monitor |
| SCFM | Standard Cubic Feet per Minute — volumetric flow rate at standard conditions |
| Motor controller | Electronic unit controlling EAC motor speed, current, and protection |

---

## §19 Citations

1. EASA CS-25 §25.1438 — Pneumatic Systems
2. EASA CS-25 §25.1301 — Equipment and Installations
3. EASA CS-25 §25.1309 — Systems and Installations
4. EASA CS-25 §25.1353 — Electrical Equipment and Installations
5. RTCA DO-160G — Environmental Conditions and Test Procedures
6. S1000D Issue 5.0 — Technical Publication Standard
7. ATA iSpec 2200 — ATA 36 Pneumatic
8. AMPEL360e eWTW Bleed-less Architecture Design Rules — TBD
9. Q-AIR Division — EAC Preliminary Specification — TBD

---

## §20 References

| Ref ID | Document | Source | Link |
|---|---|---|---|
| [ATA36] | ATA iSpec 2200 Chapter 36 — Pneumatic | ATA | — |
| [CS25-1438] | CS-25 §25.1438 Pneumatic Systems | EASA | https://www.easa.europa.eu/ |
| [CS25-1309] | CS-25 §25.1309 Systems and Installations | EASA | https://www.easa.europa.eu/ |
| [DO-160G] | RTCA DO-160G | RTCA | https://www.rtca.org/ |
| [S1000D] | S1000D Issue 5.0 | ASD/AIA | https://s1000d.org/ |
| [036-000] | ATA 36 General | Internal | [036-000](./036-000-Pneumatic-General.md) |
| [036-020] | ATA 36 Air Distribution | Internal | [036-020](./036-020-Pneumatic-Air-Distribution.md) |
| [ATA21] | ATA 21 — ECS / Pressurisation | Internal | — |
| [ATA24] | ATA 24 — Electrical Power | Internal | — |
| [ATA45] | ATA 45 — CMC / OMS | Internal | — |

---

## §21 Open Issues

| Issue ID | Description | Owner | Priority | Status |
|---|---|---|---|---|
| OI-036-001 | **Retain or eliminate ATA 36 circuit**: if consumers are all electrified, EAC and ground connector may be eliminated entirely | Q-AIR | Critical | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-004 | **EAC sizing**: rated pressure, flow, power, motor type — pending consumer finalisation | Q-AIR | High | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-004b | **EAC quantity**: single vs. dual — reliability vs. mass trade-off | Q-AIR | High | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-004c | **EAC location**: E/E bay, belly fairing, or other — structural and access trade-off | Q-MECHANICS | Medium | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-005 | **Ground pneumatic connector retention**: standard pneumatic receptacle or replaced by ground electric supply only | Q-AIR | Medium | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-009 | **EAC inlet air quality**: filtration requirements, moisture separator — depends on compressor type and consumer sensitivity | Q-MECHANICS | Medium | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-010 | **EAC DAL assignment**: criticality of EAC failure depends on consumer criticality (door seals) — FMECA required | Q-AIR / ORB-LEG | High | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §22 Change Log

| Revision | Date | Author | Description |
|---|---|---|---|
| 0.1.0 | 2026-05-10 | Q+ATLANTIDE scaffold generator | Initial full-template scaffold — all sections present; content TBD/DRAFT |
