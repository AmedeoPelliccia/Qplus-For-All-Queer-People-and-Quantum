---
document_id: "QATL-ATLAS-000099-ATLAS-030039-038-050"
title: "038-050 — Toilet and Vacuum Waste System"
short_title: "Toilet and Vacuum Waste System"
subsubject: "050"
subsubject_title: "Toilet and Vacuum Waste System"
file_name: "038-050-Toilet-and-Vacuum-Waste-System.md"
sns_reference: "038-05"
dmc_prefix: "DMC-<PROGRAMME>-<VARIANT>-038-05"
programme: "[PROGRAMME-AIRCRAFT] programme-defined aircraft configuration Family"
programme_link: "../../../../../[PROGRAMME-PATH]/090_[PROGRAMME-AIRCRAFT]-Wide-Tube-and-Wing-Family/"
short_code: "[PROGRAMME-VARIANT]"
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
  - "[PROGRAMME-AIRCRAFT]"
  - "S1000D"
  - "ATA 38"
  - "Water and Waste"
  - "Toilet"
  - "VWS"
  - "Vacuum Waste"
  - "EFV"
  - "WIV"
  - "waste tank"
  - "odour filter"
  - "flush valve"
  - "rinse nozzle"
  - "activated carbon"
  - "black water"
standard_scope: agnostic
programme_specific: false
---

# 038-050 — Toilet and Vacuum Waste System
### [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT] · ATA 38 · Q+ATLANTIDE ATLAS Scaffold

**Status:** <img src="https://img.shields.io/badge/DRAFT-yellow">  
**Revision:** 0.1.0 — 2026-05-10  
**Classification:** Q-AIR Primary | Q-MECHANICS / Q-DATAGOV / Q-GREENTECH / Q-GROUND Support

---

## §0 Hyperlink Policy

All cross-references within this document use relative Markdown links anchored to section headings within the Q+ATLANTIDE ATLAS repository. External regulatory references are cited by document identifier only. Internal DMC cross-references follow the pattern `DMC-<PROGRAMME>-<VARIANT>-038-05-YYYY-A`. Where a parameter is not yet determined, the badge <img src="https://img.shields.io/badge/TBD-red"> is used inline.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `038-050 — Toilet and Vacuum Waste System`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 Applicability

| Applicability Level | Rule |
|---|---|
| Standard taxonomy | Applies to the ATLAS node `<NODE>` |
| Programme implementation | Conditional; determined by programme architecture, trade studies, certification basis, and applicability model |
| Product configuration | Defined in the programme-specific configuration baseline |
| Effectivity | Defined in the programme CSDB / applicability layer |
| Non-applicability | Must be explicitly stated in the programme impact-study branch when excluded |
## §3 System/Function Overview

### 3.1 Toilet System Architecture

The [PROGRAMME-VARIANT] uses a vacuum-flush toilet system where differential pressure (cabin pressure above waste-line pressure) transports waste from the toilet bowl to the waste tank. The vacuum is generated by the Electric Vacuum Generator (EVG — ATA 37).

**ATA 37 scope:** EVG, SOV, VRV, vacuum manifold and lines up to and including the flush valve vacuum inlet port.  
**ATA 38 scope:** Toilet bowl assembly (bowl, seat, lid, flush button), EFV, WIV, rinse nozzle, waste collection lines, waste tank, sensors, odour filter, and ground drain fittings.

### 3.2 Flush Cycle

A single flush cycle proceeds as follows:
1. Passenger presses flush button → flush controller command → EFV commanded open.
2. EFV opens (solenoid energised): vacuum from ATA 37 manifold applied to WIV.
3. WIV opens: differential pressure transports waste from bowl to waste collector line.
4. Simultaneously, rinse water nozzle activates: small volume (~0.3–0.5 L TBD) of potable water sprays bowl interior.
5. EFV commanded closed after ~1.5 s flush cycle TBD.
6. WIV closes. Bowl refills with rinse water for next passenger.

### 3.3 Waste Tank Summary

| Parameter | Value |
|---|---|
| Waste tank count | <img src="https://img.shields.io/badge/TBD-red"> (~3 per-lav or 1 consolidated — OI-038-005) |
| Capacity per tank | <img src="https://img.shields.io/badge/TBD-red"> (~15–20 L per lavatory) |
| Material | <img src="https://img.shields.io/badge/TBD-red"> (stainless steel or CFRP) |
| Location | <img src="https://img.shields.io/badge/TBD-red"> (belly, aft of wing) |
| Level sensing | Capacitive, 3-level (normal/high/full) |
| Overflow sensor | Reed switch or float |
| Temperature sensor | NTC (freeze protection alert) |
| Odour vent | Activated carbon filter + check valve |

---

## §4 Scope

### 4.1 In-Scope

- Toilet bowl assemblies (bowl, seat, lid, flush button) — interface to EFV and rinse nozzle
- Electric Flush Valve (EFV) per toilet — solenoid, flush cycle controller
- Waste Inlet Valve (WIV) per toilet — vacuum interface between bowl outlet and waste line
- Rinse water supply branch per toilet — from potable water header (ATA 38-010)
- Rinse water nozzle (spray nozzle inside bowl)
- Waste collector lines — PTFE-lined; from each toilet to waste tank(s)
- Waste tank(s) — vessel, mounting, fittings
- Waste tank accessories: level sensor (capacitive, 3-level), overflow sensor, temperature sensor, odour filter vent assembly, deodoriser tablet dispenser TBD
- Ground drain fitting per tank or consolidated single-point drain
- Waste tank inspection port
- Waste tank rinse fitting (for ground rinse of tank interior)

### 4.2 Out-of-Scope

- Vacuum generation (EVG, SOV, VRV, vacuum manifold): → ATA 37
- Toilet bowl furniture and installation: → ATA 25
- Potable water supply to rinse nozzle (distribution header): → [038-010](./038-010-Potable-Water-System.md)
- Grey water sink drain: → [038-040](./038-040-Waste-Water-Drainage.md)

---

## §5 Architecture Description

### 5.1 System Flow

```
[ATA 37 EVG vacuum] ──────────────────────────────────┐
                                                        ↓
[Potable water header (ATA 38-010)] → [Rinse nozzle supply]
                                                ↓
                                       [Toilet Bowl (ATA 25)]
                                          [Flush button]
                                                ↓  (flush command)
                                          [EFV-1 (solenoid)]  ← [Vacuum from ATA 37]
                                                ↓
                                          [WIV-1]
                                                ↓
                                     [Waste collector line 1 (PTFE)]
                                                ↓
                                     [Waste Tank 1 (or manifold)]
                                      ├── Level sensor (3-level capacitive)
                                      ├── Overflow sensor (reed/float)
                                      ├── Temperature sensor (NTC)
                                      ├── Odour vent (activated carbon + NRV)
                                      ├── Inspection port
                                      └── Ground drain fitting (gravity/vacuum)
```

(Repeated for Toilet-2, Toilet-3, etc.)

### 5.2 ATA 37 / ATA 38 Interface Boundary

| Component | ATA Chapter |
|---|---|
| EVG-1, EVG-2 | ATA 37 |
| SOV (shutoff valve) | ATA 37 |
| VRV (vacuum relief valve) | ATA 37 |
| Vacuum manifold and distribution lines | ATA 37 |
| Flush valve vacuum inlet fitting | ATA 37/38 boundary |
| EFV (flush valve body, solenoid, controller) | **ATA 38** |
| WIV (waste inlet valve) | **ATA 38** |
| Toilet bowl assembly | **ATA 38** (bowl/hardware); ATA 25 (furniture) |
| Waste collector lines | **ATA 38** |
| Waste tanks | **ATA 38** |
| Ground drain fittings | **ATA 38** |

---

## §6 Functional Breakdown

| Component | Function | Qty | Status |
|---|---|---|---|
| Toilet bowl assemblies | Receive waste; flush button; seat/lid | TBD (~3) | ATA 25 interface |
| EFV-1, EFV-2, EFV-3 | Solenoid flush valve; 1.5 s cycle TBD | TBD (~3) | <img src="https://img.shields.io/badge/TBD-red"> |
| WIV-1, WIV-2, WIV-3 | Vacuum differential valve; bowl to waste line | TBD (~3) | <img src="https://img.shields.io/badge/TBD-red"> |
| Rinse nozzle (RN-1 to RN-3) | Pre-wet/rinse bowl interior | TBD (~3) | ~0.3–0.5 L/flush TBD |
| Waste collector lines | PTFE-lined; transport waste to tank | TBD m | <img src="https://img.shields.io/badge/TBD-red"> |
| Waste tank(s) | Store toilet waste | TBD (~3 or 1 consol.) | OI-038-005 |
| Level sensor (LS-W) | Capacitive; 3-level (normal/high/full) | Per tank | <img src="https://img.shields.io/badge/TBD-red"> |
| Overflow sensor (OS-W) | Reed switch or float; full alert | Per tank | <img src="https://img.shields.io/badge/TBD-red"> |
| Temperature sensor (TS-W) | NTC; freeze protection alert | Per tank | <img src="https://img.shields.io/badge/TBD-red"> |
| Odour vent filter (OVF-W) | Activated carbon + NRV; vent tank to cabin zone TBD | Per tank | <img src="https://img.shields.io/badge/TBD-red"> |
| Deodoriser dispenser (TBD) | Tablet/gel deodoriser in bowl or tank | Per toilet TBD | OI TBD |
| Ground drain fitting (GDF-W) | Gravity/vacuum drain interface for ground service | Per tank or 1 consolidated | <img src="https://img.shields.io/badge/TBD-red"> |
| Waste tank inspection port | Access for inspection and cleaning | Per tank | <img src="https://img.shields.io/badge/TBD-red"> |
| Ground rinse fitting | Tank interior rinse connection | 1 (consolidated) TBD | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §7 System Context Diagram

```mermaid
flowchart LR
    ATA37["ATA 37\nVacuum\n(EVG vacuum supply\nto EFV inlet)"]
    ATA38_010["ATA 38-010\nPotable Water\n(rinse nozzle supply)"]
    ATA25["ATA 25\nFurnishings\n(toilet bowl, flush button)"]
    ATA24["ATA 24\nElectrical Power\n(EFV solenoid power)"]
    CMC["CMC / ATA 45"]
    GND["Ground Service\n(waste vacuum truck,\nrinse water)"]

    EFV["EFV\n(Electric Flush Valve)\nsolenoid, 1.5 s TBD"]
    WIV["WIV\n(Waste Inlet Valve)"]
    RINSE["Rinse Nozzle\n(~0.3–0.5 L/flush TBD)"]
    LINES["Waste Collector Lines\n(PTFE-lined)"]
    WTANK["Waste Tank(s)\n(stainless/CFRP,\nTBD L per tank)"]
    SENSORS["Tank Sensors\n(level, overflow, temp)"]
    VENT["Odour Vent Filter\n(activated carbon + NRV)"]
    DRAIN["Ground Drain\nFitting"]

    ATA37 -->|"vacuum supply"| EFV
    ATA38_010 -->|"rinse water"| RINSE
    ATA25 -.->|"toilet bowl\nflush button"| EFV
    ATA24 -->|"solenoid power"| EFV
    EFV --> WIV --> LINES --> WTANK
    RINSE --> WTANK
    WTANK --> SENSORS -->|"level/overflow/temp"| CMC
    WTANK --> VENT
    WTANK --> DRAIN --> GND
```

---

## §8 Internal Functional Architecture

```mermaid
flowchart TB
    BTN["Flush Button\n(passenger command)"]
    CTRL["EFV Controller\n(flush cycle logic)"]
    EFV["Electric Flush Valve\n(solenoid, 1.5 s TBD)"]
    VAC["Vacuum Supply\n(ATA 37 EVG)"]
    WIV["Waste Inlet Valve\n(WIV)"]
    BOWL["Toilet Bowl\n(ATA 25)"]
    RINSE_V["Rinse Nozzle\n(potable water spray)"]
    WCLINE["Waste Collector Line\n(PTFE-lined)"]
    WTANK["Waste Tank\nStainless/CFRP\nTBD L"]
    LS["Level Sensor\n(capacitive, 3-level)"]
    OS["Overflow Sensor\n(reed switch/float)"]
    TS["Temperature Sensor\n(NTC — freeze alert)"]
    OVF["Odour Vent Filter\n(activated carbon + NRV)"]
    DEOS["Deodoriser Dispenser\n(TBD)"]
    DRAIN["Ground Drain Fitting\n(gravity / vacuum truck)"]
    INSPECT["Inspection Port"]
    CMC["CMC Interface\n(AFDX)"]

    BTN --> CTRL --> EFV
    VAC --> EFV
    EFV --> WIV --> BOWL
    RINSE_V --> BOWL
    BOWL --> WCLINE --> WTANK
    WTANK --> LS --> CMC
    WTANK --> OS --> CMC
    WTANK --> TS --> CMC
    WTANK --> OVF
    WTANK --> DEOS
    WTANK --> DRAIN
    WTANK --> INSPECT
```

---

## §9 Lifecycle Traceability

```mermaid
flowchart LR
    REQ["Requirements\n(CS-25.1301, CS-25.1309,\nEASA AMC 25.831,\nCS-25.853)"]
    SRD["System Requirements\nDocument"]
    SDD["SDD 038-050\nToilet & Vacuum Waste System"]
    ICD["ICDs\n(ATA 37 vacuum,\nATA 38-010 water,\nATA 24 power, ATA 25 bowl)"]
    COMP["Component Specs\n(EFV, WIV, waste tank,\nsensors, odour filter)"]
    VTP["V&V Plan (§17)"]
    TEST["Test Reports\n(flush cycle, tank leak,\nlevel sensor, overflow)"]
    CERT["EASA/FAA Certification"]
    EIS["Entry Into Service"]
    MAINT["AMM / CMM / S1000D DMs"]

    REQ --> SRD --> SDD --> ICD --> COMP
    SDD --> VTP --> TEST --> CERT --> EIS --> MAINT
```

---

## §10 Interfaces

| Interface | ATA Chapter | Direction | Signal/Medium | Notes |
|---|---|---|---|---|
| Vacuum supply (ATA 37 EVG) | ATA 37 | In | Vacuum −0.7 to −1.0 bar TBD | EVG vacuum to EFV inlet; boundary at EFV vacuum inlet fitting |
| Rinse water supply | ATA 38-010 | In | Pressurised potable water | Cold water to rinse nozzle; ~0.3–0.5 L per flush |
| Toilet bowl assembly | ATA 25 | Bi | Mechanical + flush button signal | Bowl outlet to WIV; flush button to EFV controller |
| EFV solenoid power | ATA 24 | In | DC/AC TBD (galley/cabin bus) | Power for EFV solenoid actuation |
| Tank sensors to CMC | ATA 45 | Out | AFDX/ARINC TBD | Level, overflow, temp signals |
| Ground drain service | ATA 38-070 / Ground | Out | Waste fluid | Drain fitting for ground service truck |
| Odour vent | Cabin structure | Out | Air + carbon filter | Tank pressure equalisation with odour removed |

---

## §11 Operating Modes

| Mode | EFV | WIV | Rinse | Waste Tank | Notes |
|---|---|---|---|---|---|
| Normal Flight — Ready | Armed (solenoid idle) | Closed | Off | Accepting waste | Normal state between flushes |
| Flush Cycle Active | Open (solenoid ON) | Open | Active | Receiving waste | ~1.5 s cycle TBD |
| Flush Cycle Complete | Closed | Closed | Off | Level updated | Ready for next passenger |
| Tank Full (≥ 90% TBD) | Inhibited (TBD) | Inhibited | — | Full | "WASTE FULL" alert; no further flushing |
| Overflow | EFV inhibited | Closed | Off | Overflow alert | "WASTE OVFL" (red) |
| Freeze Risk | As normal | As normal | As normal | Freeze alert | THC or equivalent activates tank area heater |
| Ground — Service | EFV off | Off | Off | Draining | Ground drain valve open; waste truck connected |
| Maintenance | Off | Off | Off | Drained | Safe state; inspection port opened |

---

## §12 Monitoring and Diagnostics

| Parameter | Sensor | CMC Signal | Alert |
|---|---|---|---|
| Waste tank fill level | LS-W (capacitive, 3-level) | AFDX | "WASTE FULL" (amber ≥ 90% TBD) |
| Waste tank overflow | OS-W (reed switch / float) | Discrete | "WASTE OVFL" (red) |
| Waste tank temperature | TS-W (NTC) | AFDX | "WASTE FREEZE RISK" advisory < +4°C TBD |
| EFV-1 cycle count | CMC counter | CMC log | Maintenance advisory at TBD cycles |
| EFV-2 cycle count | CMC counter | CMC log | Maintenance advisory |
| EFV status (fault) | Current monitor | AFDX | "EFV FAULT" (caution) |
| Rinse water flow (TBD) | Flow sensor TBD | AFDX | Advisory on no-flow TBD |

---

## §13 Maintenance Concept

| Task | Access | Interval | Skill |
|---|---|---|---|
| Waste tank drain (turn/post-flight) | Ground service panel | Per turn / operator program | Line |
| Waste tank rinse | Ground rinse fitting | Per maintenance program | Line |
| Waste tank inspection | Inspection port | C-check TBD | Base |
| EFV function test | BITE / manual test | C-check TBD | Line/base |
| EFV R&R | Lavatory access | On condition | Line/base |
| WIV R&R | Lavatory access | On condition | Line/base |
| Odour filter replacement | Tank access | Per maintenance program TBD | Line |
| Deodoriser refill | Lavatory access | Per turn TBD | Line |
| Rinse nozzle inspection | Lavatory bowl access | C-check TBD | Line |
| Waste collector line inspection | Bilge / belly access | C-check TBD | Base |

---

## §14 S1000D/CSDB Mapping

| Document | DMC Pattern | Info Code | Status |
|---|---|---|---|
| System description — VWS | DMC-<PROGRAMME>-<VARIANT>-038-05-00A-040A-A | 040 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| EFV description | DMC-<PROGRAMME>-<VARIANT>-038-05-10A-040A-A | 040 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| EFV removal | DMC-<PROGRAMME>-<VARIANT>-038-05-10A-520A-A | 520 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| EFV installation | DMC-<PROGRAMME>-<VARIANT>-038-05-10A-720A-A | 720 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Waste tank description | DMC-<PROGRAMME>-<VARIANT>-038-05-20A-040A-A | 040 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Waste tank drain/service | DMC-<PROGRAMME>-<VARIANT>-038-05-20A-910A-A | 910 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Odour filter replacement | DMC-<PROGRAMME>-<VARIANT>-038-05-30A-720A-A | 720 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Fault isolation — VWS | DMC-<PROGRAMME>-<VARIANT>-038-05-00A-400A-A | 400 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §15 Footprints

| Parameter | Value |
|---|---|
| Waste tank count | <img src="https://img.shields.io/badge/TBD-red"> (OI-038-005) |
| Waste tank capacity | <img src="https://img.shields.io/badge/TBD-red"> (~15–20 L per lav) |
| Waste tank material | <img src="https://img.shields.io/badge/TBD-red"> (stainless or CFRP) |
| Waste tank location | <img src="https://img.shields.io/badge/TBD-red"> (belly, aft of wing) |
| EFV cycle time | <img src="https://img.shields.io/badge/TBD-red"> (~1.5 s) |
| Rinse water per flush | <img src="https://img.shields.io/badge/TBD-red"> (~0.3–0.5 L) |
| Number of EFV units | <img src="https://img.shields.io/badge/TBD-red"> (1 per toilet) |
| Waste collector line length | <img src="https://img.shields.io/badge/TBD-red"> m |
| System mass (VWS, excl. waste) | <img src="https://img.shields.io/badge/TBD-red"> kg |

---

## §16 Safety and Certification

| Requirement | Standard | Application |
|---|---|---|
| Equipment installation | CS-25.1301 | EFV, WIV, waste tank |
| System safety | CS-25.1309 | EFV failure modes; tank overflow; vacuum loss |
| Lavatory waste and air quality | EASA AMC 25.831 | Odour filter; cabin air protection |
| Material flammability | CS-25.853 | Waste tank material; collector line material |
| Freeze protection | CS-25.1419 | Tank temperature sensor; heater if tank in cold zone |
| EMC | CS-25.1353 | EFV solenoid; level sensor electronics |
| Backflow prevention (rinse) | Design requirement | NRV on rinse water supply to prevent waste backflow |
| Contamination separation | Physical + NRV | Waste lines never contact potable water circuit |

---

## §17 Verification and Validation

| Test | Method | Acceptance Criterion | Status |
|---|---|---|---|
| EWP flow test | Bench/rig | ≥ TBD L/min | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Tank leak test | Hydrostatic 1.5× WP | No leakage TBD min | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| EWH thermal test | Bench thermostat | Outlet ≥ 60°C; TMV ≤ 43°C TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| UV steriliser output test | UV intensity + log-reduction | ≥ 4-log TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Mast heater continuity test | Resistance at install | Within rated tolerance | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Flush cycle test | Functional rig; vacuum available | Waste transported ≤ 1.5 s TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Fill-level sensor accuracy | Cal 0/50/100% | ± TBD % | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Overflow sensor function | Simulated overfill | Alert within TBD s | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Grey water drain flow test | Max load | Clear within TBD s | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Potable water quality test | Sample analysis | Meets WHO/FAA standard | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Freeze protection activation test | Cold chamber | THC/heater activates; no freeze | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §18 Glossary

| Term | Definition |
|---|---|
| PWS | Potable Water System |
| EWP | Electric Water Pump |
| EWH | Electric Water Heater |
| VWS | Vacuum Waste System — complete toilet waste collection and storage subsystem |
| EFV | Electric Flush Valve — solenoid valve controlling vacuum flush cycle |
| WIV | Waste Inlet Valve — connects toilet bowl outlet to vacuum waste line |
| Mast drain | Heated overboard grey water nozzle |
| EMH | Electric Mast Heater |
| UV sterilisation | UV-C potable water treatment |
| Activated carbon filter | Removes odour from tank vent or chlorine from fill |
| LLDPE | Linear Low-Density Polyethylene |
| PEX | Cross-linked Polyethylene |
| Capacitive level sensor | Non-contact level measurement |
| NRV | Non-Return Valve |
| TMV | Thermostatic Mixing Valve |
| Grey water | Sink drainage |
| Black water | Toilet waste (liquid and solid) |
| Waste tank | Pressurised/unpressurised vessel collecting toilet waste |
| Freeze protection | Trace or zone heating preventing ice in water/waste system |
| Trace heating | Resistance elements on lines |
| THC | Trace Heater Controller |
| CMC | Central Maintenance Computer |
| OVF | Odour Vent Filter — activated carbon vent filter on waste tank |
| GDF | Ground Drain Fitting — tank drain interface for ground service truck |
| EVG | Electric Vacuum Generator (ATA 37) |
| SOV | Shutoff Valve (ATA 37 — isolates EVG from manifold) |
| PTFE | Polytetrafluoroethylene — waste line liner material |

---

## §19 Citations

1. EASA CS-25.1301 — Function and installation.
2. EASA CS-25.1309 — System safety.
3. EASA CS-25.853 — Material flammability.
4. EASA CS-25.1419 — Ice protection.
5. EASA AMC 25.831 — Lavatory waste; cabin air quality.
6. [037-000 Vacuum General](../037_Vacuum/037-000-Vacuum-General.md) — EVG, vacuum supply.
7. [038-000 General](./038-000-Water-and-Waste-General.md).
8. [038-010 Potable Water System](./038-010-Potable-Water-System.md) — rinse water supply.
9. [038-060 Indication and Warning](./038-060-Water-and-Waste-Indication-and-Warning.md).
10. [038-070 Servicing and Ground Interfaces](./038-070-Water-and-Waste-Servicing-and-Ground-Interfaces.md).

---

## §20 References

| Ref | Document | Notes |
|---|---|---|
| [R1] | CS-25.1301 | Installation |
| [R2] | CS-25.1309 | System safety |
| [R3] | CS-25.853 | Flammability |
| [R4] | CS-25.1419 | Freeze protection |
| [R5] | EASA AMC 25.831 | Lavatory waste, air quality |
| [R6] | [037-000](../037_Vacuum/037-000-Vacuum-General.md) | Vacuum EVG |
| [R7] | [038-000](./038-000-Water-and-Waste-General.md) | ATA 38 General |
| [R8] | [038-010](./038-010-Potable-Water-System.md) | Rinse water supply |
| [R9] | [038-060](./038-060-Water-and-Waste-Indication-and-Warning.md) | Indication |
| [R10] | [038-070](./038-070-Water-and-Waste-Servicing-and-Ground-Interfaces.md) | Ground servicing |

---

## §21 Open Issues

| ID | Description | Owner | Status |
|---|---|---|---|
| OI-038-001 | Tank capacity and material | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-002 | Tank pressurisation method | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-003 | EWH count, placement, power budget | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-004 | Grey water retention regulatory review | Q-AIR / ORB-LEG | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-005 | Waste tank count and capacity (per-lav vs. consolidated) | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-006 | Freeze protection strategy | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-007 | UV sterilisation certification and interval | Q-AIR / ORB-LEG | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-008 | Mast drain count and location | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-009 | Single-point servicing panel location | Q-AIR / Q-GROUND | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §22 Change Log

| Revision | Date | Author | Description |
|---|---|---|---|
| 0.1.0 | 2026-05-10 | Q+ATLANTIDE ATLAS Working Group | Initial full-template draft; all 23 sections; VWS, EFV, WIV, waste tank, sensors |
| 0.0.0 | 2026-05-10 | Q+ATLANTIDE ATLAS Working Group | Scaffold stub created |
