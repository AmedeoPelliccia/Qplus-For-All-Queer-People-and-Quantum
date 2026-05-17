---
document_id: "QATL-ATLAS-000099-ATLAS-030039-039-020"
title: "039-020 — Circuit Breaker and Protection Panels"
short_title: "ATA 39 CBPs"
subsubject: "020"
subsubject_title: "Circuit Breaker and Protection Panels"
file_name: "039-020-Circuit-Breaker-and-Protection-Panels.md"
sns_reference: "039-20"
dmc_prefix: "DMC-<PROGRAMME>-<VARIANT>-039-20"
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
  - "[PROGRAMME-AIRCRAFT]"
  - "S1000D"
  - "ATA 39"
  - "Circuit Breaker Panel"
  - "CBP"
  - "SSCB"
  - "Solid-State Circuit Breaker"
  - "thermal-magnetic CB"
  - "trip-free"
  - "CBP-1"
  - "CBP-2"
  - "270 VDC"
  - "CS-25.1353"
standard_scope: agnostic
programme_specific: false
---

# 039-020 — Circuit Breaker and Protection Panels
### [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT] · ATA 39 · Q+ATLANTIDE ATLAS Scaffold

**Status:** <img src="https://img.shields.io/badge/DRAFT-yellow">  
**Revision:** 0.1.0 — 2026-05-10  
**Classification:** Q-AIR Primary | Q-MECHANICS / Q-DATAGOV / Q-HPC / Q-GROUND / Q-INDUSTRY Support

---

## §0 Hyperlink Policy

All cross-references within this document use relative Markdown links. External regulatory references (CS-25, DO-160G) are cited by identifier only. Internal DMC cross-references follow `DMC-<PROGRAMME>-<VARIANT>-039-20-YYYY-A`. Badge <img src="https://img.shields.io/badge/TBD-red"> marks unresolved parameters; <img src="https://img.shields.io/badge/DRAFT-yellow"> and <img src="https://img.shields.io/badge/To_Be_Completed-orange"> indicate work-in-progress and planned content.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `039-020 — Circuit Breaker and Protection Panels`.

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

### 3.1 CBP Architecture

The [PROGRAMME-VARIANT] carries three circuit breaker panel locations:

| CBP | Location | Access | Voltage Levels Served | CB Count |
|---|---|---|---|---|
| CBP-1 | Aft overhead cockpit | Crew-accessible in flight | 28 VDC, 115 VAC | <img src="https://img.shields.io/badge/TBD-red"> |
| CBP-2 | Aft E/E bay (ground access only) | Ground / maintenance | 28 VDC, 115 VAC | <img src="https://img.shields.io/badge/TBD-red"> |
| CBP-3 | Forward under-floor (TBD) | Ground / maintenance | 28 VDC TBD | <img src="https://img.shields.io/badge/TBD-red"> |

### 3.2 CB Technology Options

Two circuit breaker technologies are under evaluation (OI-039-001):

**Option A — Thermal-Magnetic Circuit Breakers (TM-CB):**
- Mature technology; industry-standard for commercial aviation.
- Bi-metal thermal element (overload) + magnetic element (short-circuit trip).
- Trip time–current curve (TCC) per RTCA DO-160 application.
- Collar colour identifies ATA system grouping (industry convention).
- Manual reset: crew or maintenance technician pushes button to reset.
- No remote monitoring capability (no digital trip log).
- No remote reset (crew/maintenance must physically reset).

**Option B — Solid-State Circuit Breakers (SSCBs):**
- Electronic trip circuit (FET or GTO); configurable trip threshold.
- Digital trip log: records trip time-stamp, pre-trip current, junction temperature.
- Remote status monitoring via AFDX to CMC (ATA 45).
- Remote reset via maintenance terminal — ground-only (per certification; crew cannot remotely reset in flight).
- Faster trip time than thermal-magnetic.
- Weight reduction potential: <img src="https://img.shields.io/badge/TBD-red"> (supplier data pending).
- Certification maturity: TBD — OI-039-001.

### 3.3 Trip-Free Design

All circuit breakers — thermal-magnetic or SSCB — must be **trip-free**: once the protection mechanism has detected a fault and initiated a trip, the device cannot be held in the closed position by external force. This is a mandatory safety requirement per CS-25.1353 and ATA engineering standard. Pull-to-reset CBs (push-in to reset, stays out on trip) meet this requirement.

### 3.4 Colour-Coded Collar Convention

All CBP circuit breakers are identified by a colour-coded collar on the CB button per the ATA / AECMA convention grouping CBs by ATA system chapter:

| Collar Colour | System (ATA Chapter) | Example |
|---|---|---|
| White | Lights / Cabin (ATA 33) | Cabin lighting circuits |
| Green | Flight controls (ATA 27 / 29) | EMA control circuits ([PROGRAMME-VARIANT]) |
| Blue | Avionics / Instruments (ATA 31/34/42) | IMA module power |
| Red | Fire protection (ATA 26) | Fire detection loop power |
| Yellow | Fuel (ATA 28) | Fuel pump power |
| Orange | ECS / Pneumatic (ATA 21) | ECS compressor control power |
| Grey | Miscellaneous / Utility | Galley utility outlets TBD |
| Tan/Brown | Communication (ATA 23) | VHF transceiver power |

Note: Final colour assignments TBD pending complete system electrical load analysis (ELA). <img src="https://img.shields.io/badge/TBD-red">

---

## §4 Scope

### 4.1 In-Scope

- CBP-1 panel structure and all CB assemblies (crew overhead)
- CBP-2 panel structure and all CB assemblies (E/E bay)
- CBP-3 panel structure (TBD, pending OI-039-007)
- SSCB modules (if selected — OI-039-001)
- CB collar colour identification
- CBP panel identification labels and circuit labels
- SSCB AFDX interface module (if fitted)
- HVDC branch protection concept (contactor/fuse TBD — OI-039-005)

### 4.2 Out-of-Scope

- Main bus contactors and BTCs (→ 039-030)
- PDUs and SSPCs (→ 039-030)
- Panel wiring harnesses to CB studs (→ 039-070)

---

## §5 Architecture Description

### 5.1 CBP-1 (Aft Overhead, Crew-Accessible)

CBP-1 is mounted in the aft section of the overhead panel (P6), accessible to both crew members in flight. It carries circuit breakers for:
- Flight deck avionics power feeds (28 VDC)
- Cabin and galley circuit branches (28 VDC and 115 VAC)
- Critical systems accessible to crew per abnormal/emergency procedures

CBP-1 layout is organised by ATA chapter column groupings with clear labelling. CB count: <img src="https://img.shields.io/badge/TBD-red"> (target < 200 CBs pending electrical load analysis).

### 5.2 CBP-2 (Aft E/E Bay, Maintenance Access)

CBP-2 is located in the aft E/E bay, accessible on the ground with E/E bay doors open. It carries:
- IMA rack power feeds
- Navigation and communications equipment branches
- System-level 28 VDC / 115 VAC branches for ATA chapters without CBP-1 representation

CB count: <img src="https://img.shields.io/badge/TBD-red">.

### 5.3 SSCB Architecture (if selected)

If SSCB technology is selected (OI-039-001), the SSCB modules would be integrated in a dedicated controller rack within the CBP assembly:
- SSCB controller module communicates with CMC via AFDX.
- Trip log stored in non-volatile memory within SSCB controller.
- Remote reset: ground maintenance terminal command → AFDX → SSCB controller → SSCB close.
- In-flight remote reset: **prohibited** — safety latch logic prevents remote reset in flight (weight-on-wheels or flight logic inhibit).

---

## §6 Functional Breakdown

| ID | Function | Components | Interface | Status |
|---|---|---|---|---|
| 039-020-F01 | Overcurrent protection (28 VDC) | TM-CB or SSCB on CBP-1/2/3 | Hardwired series protection | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 039-020-F02 | Overcurrent protection (115 VAC) | TM-CB or SSCB on CBP-1/2 | Hardwired series protection | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 039-020-F03 | SSCB digital trip log | SSCB controller | AFDX → CMC | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 039-020-F04 | SSCB remote status monitoring | SSCB controller | AFDX → CMC | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 039-020-F05 | SSCB remote reset (ground only) | SSCB controller | Maintenance terminal → AFDX | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 039-020-F06 | CB identification (colour collar) | Collar on CB button | Visual | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| 039-020-F07 | HVDC branch protection (TBD) | HVDC fuse / contactor | ATA 24 interface | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §7 System Context Diagram

```mermaid
flowchart LR
    ATA24["ATA 24\nElectrical Power\n(28 VDC / 115 VAC / 270 VDC buses)"]
    CBP1["CBP-1\nAft Overhead\n(crew-accessible)"]
    CBP2["CBP-2\nAft E/E Bay\n(maintenance access)"]
    CBP3["CBP-3 TBD\nFwd Under-floor"]
    LOADS_FD["Flight Deck\nAvionics Loads"]
    LOADS_CAB["Cabin / Galley\nLoads"]
    LOADS_SYS["System\nLoads (ATA chapters)"]
    SSCB_CTRL["SSCB Controller\n(if fitted)"]
    AFDX_SW["AFDX Switch"]
    CMC["CMC ATA 45\n(maintenance data)"]
    MAINT["Maintenance Terminal\n(ground only)"]

    ATA24 -->|"28V / 115V buses"| CBP1 & CBP2 & CBP3
    CBP1 -->|"branch circuits"| LOADS_FD & LOADS_CAB
    CBP2 -->|"branch circuits"| LOADS_SYS
    CBP1 & CBP2 -.->|"SSCB data (if fitted)"| SSCB_CTRL
    SSCB_CTRL -->|"AFDX trip log / status"| AFDX_SW
    AFDX_SW -->|"AFDX"| CMC
    MAINT -->|"reset cmd (ground)"| AFDX_SW
```

---

## §8 Internal Functional Architecture

```mermaid
flowchart TB
    subgraph CBP1["CBP-1 Aft Overhead"]
        CB_ATA33["ATA 33 CBs\n(lights, white collar)"]
        CB_ATA27["ATA 27 CBs\n(EMA control, green collar)"]
        CB_ATA23["ATA 23 CBs\n(comms, tan collar)"]
        CB_ATA28["ATA 28 CBs\n(fuel, yellow collar)"]
        CB_ATA26["ATA 26 CBs\n(fire, red collar)"]
    end
    subgraph CBP2["CBP-2 Aft E/E Bay"]
        CB_IMA["IMA Rack CBs\n(blue collar)"]
        CB_NAV["Nav / Comms CBs\n(blue/tan collar)"]
        CB_ECS["ECS CBs\n(orange collar)"]
        CB_UTIL["Utility CBs\n(grey collar)"]
    end
    subgraph SSCB_LAYER["SSCB Controller (optional)"]
        SSCB_CTRL["SSCB Controller Module"]
        NV_LOG["Non-Volatile Trip Log"]
        RESET_LOGIC["Remote Reset Logic\n(ground-only latch)"]
    end
    BUS28["28 VDC Bus (ATA 24)"]
    BUS115["115 VAC Bus (ATA 24)"]
    AFDX["AFDX Switch"]
    CMC["CMC (ATA 45)"]

    BUS28 --> CB_ATA33 & CB_ATA27 & CB_ATA23 & CB_ATA28 & CB_ATA26
    BUS115 --> CB_ATA33 & CB_ECS & CB_UTIL
    BUS28 --> CB_IMA & CB_NAV & CB_ECS & CB_UTIL
    SSCB_CTRL --> NV_LOG & RESET_LOGIC
    SSCB_CTRL --> AFDX
    AFDX --> CMC
```

---

## §9 Lifecycle Traceability

```mermaid
flowchart LR
    LC02["LC02\nRequirements\nCB rating per ELA,\nSSCB decision criteria"]
    LC03["LC03\nArchitecture\nCBP location selection,\nHVDC protection concept"]
    LC05["LC05\nDetailed Design\nCBP layout, collar assignment,\nSSCB controller design"]
    LC06["LC06\nVerification Planning\nCB trip/reset test plan,\nSSCB log verification plan"]
    LC10["LC10\nCertification\nCS-25.1353 compliance,\nSSCB certification TBD"]
    LC11["LC11\nOperation\nAbnormal proc: CB reset,\nFCOM CBP section"]
    LC12["LC12\nMaintenance\nAMM 39-20: CB reset,\nSSCB status check, CBP replacement"]

    LC02 --> LC03 --> LC05 --> LC06 --> LC10 --> LC11 --> LC12
```

---

## §10 Interfaces

| Interface | Direction | Counterpart | Signal Type | Notes |
|---|---|---|---|---|
| 28 VDC main bus | In | ATA 24 PDU / bus | Electrical (28 VDC) | Bus feed to CBP stud bars |
| 115 VAC main bus | In | ATA 24 AC bus | Electrical (115 VAC) | AC bus feed to CBP |
| 270 VDC HVDC | In | ATA 24 HVDC bus | Electrical (270 VDC) | HVDC protection TBD — OI-039-005 |
| Branch circuit outputs | Out | Various loads (ATA 21–45) | Electrical (28V/115V) | Protected branch circuits |
| SSCB status AFDX | Out | CMC (ATA 45) | AFDX | Trip log, state, temperature |
| Remote reset command | In | Maintenance terminal | AFDX (ground-only inhibit) | SSCB remote reset |
| Physical trip indicator | Visual | Crew / Maintenance | Mechanical (button out) | TM-CB trip visible on panel |

---

## §11 Operating Modes

| Mode | CB State | SSCB Monitoring | Remote Reset |
|---|---|---|---|
| Normal Flight | All CBs IN; automatic trip on fault | AFDX status transmitted | Inhibited in flight |
| Abnormal — CB Trip | Tripped CB button out (or SSCB open) | SSCB trip log written to CMC | Manual reset by crew (TM-CB); ground-only for SSCB |
| Ground — Maintenance | CBs available for test | Full log access via CMC terminal | SSCB remote reset available |
| Ground — GPU Power | CBs IN; aircraft systems powered by GPU | SSCB monitoring active | SSCB remote reset available |
| Unpowered (cold) | CB mechanical state preserved | No monitoring | No remote capability |

---

## §12 Monitoring and Diagnostics

| Parameter | Sensor / Source | CMC Signal | Alert |
|---|---|---|---|
| CB trip state (TM-CB) | Visual / mechanical (button out) | None (no automatic signal) | Crew visual check |
| CB trip state (SSCB) | SSCB controller digital state | AFDX → CMC | "CBP FAULT" advisory per SSCB trip |
| SSCB pre-trip current | SSCB current sensor | AFDX log entry | Stored in CMC log; no real-time alert |
| SSCB junction temperature | SSCB internal temperature sensor | AFDX log | Overtemperature advisory TBD |
| SSCB trip count | SSCB non-volatile log | CMC query | Prognostic indicator TBD |
| CBP panel supply voltage | Bus voltage monitor (in PDU, ATA 24) | AFDX | Bus undervoltage / overvoltage alert |

---

## §13 Maintenance Concept

### 13.1 On-Wing Maintenance

| Task | Interval | Access | Skill Level |
|---|---|---|---|
| Visual CBP scan for tripped CBs | Per crew procedure (post-flight or on call) | CBP-1 overhead; CBP-2 E/E bay | Line maintenance |
| TM-CB reset (manual push-in) | On condition after fault clearance | Direct panel access | Line maintenance |
| SSCB remote reset (ground) | On condition via CMC terminal | CMC terminal | Line maintenance |
| SSCB trip log download | Each visit or on condition | CMC terminal | Line maintenance |
| CB collar check and identification | A-check TBD | CBP-1 / CBP-2 visual | Line maintenance |
| CBP panel label/placard inspection | A-check TBD | CBP visual | Line maintenance |
| TM-CB replacement (tripped or failed) | On condition | Unplug and replace (direct panel) | Line maintenance |
| SSCB module replacement | On condition | Module extraction from controller rack | Line maintenance (trained) |
| HVDC protection device inspection | C-check TBD | E/E bay access | Base maintenance |

### 13.2 Off-Wing

- TM-CB: no off-wing maintenance — replace on condition.
- SSCB controller module: depot BITE test, non-volatile log clear, calibration per CMM TBD.

---

## §14 S1000D/CSDB Mapping

| Document | DMC Pattern | Info Code | Status |
|---|---|---|---|
| CBP description | DMC-<PROGRAMME>-<VARIANT>-039-20-00A-040A-A | 040 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| CB reset procedure | DMC-<PROGRAMME>-<VARIANT>-039-20-00A-300A-A | 300 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| CB (TM-CB) replacement | DMC-<PROGRAMME>-<VARIANT>-039-20-00A-520A-A | 520 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| SSCB module replacement | DMC-<PROGRAMME>-<VARIANT>-039-20-01A-520A-A | 520 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| SSCB log download | DMC-<PROGRAMME>-<VARIANT>-039-20-00A-920A-A | 920 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Fault isolation — CBP | DMC-<PROGRAMME>-<VARIANT>-039-20-00A-400A-A | 400 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

Full DMRL in [039-090](./039-090-S1000D-CSDB-Mapping-and-Traceability.md).

---

## §15 Footprints

| Parameter | Value |
|---|---|
| CBP-1 CB count | <img src="https://img.shields.io/badge/TBD-red"> |
| CBP-2 CB count | <img src="https://img.shields.io/badge/TBD-red"> |
| CBP-3 CB count | <img src="https://img.shields.io/badge/TBD-red"> (if fitted) |
| Total CB count (all panels) | <img src="https://img.shields.io/badge/TBD-red"> |
| CB trip current range | <img src="https://img.shields.io/badge/TBD-red"> (1 A to TBD A) |
| CB voltage rating | 28 VDC / 115 VAC (LV); 270 VDC (HVDC TBD) |
| SSCB controller mass (if fitted) | <img src="https://img.shields.io/badge/TBD-red"> |
| CBP-1 panel mass | <img src="https://img.shields.io/badge/TBD-red"> |
| CBP-2 panel mass | <img src="https://img.shields.io/badge/TBD-red"> |
| HVDC protection device type | <img src="https://img.shields.io/badge/TBD-red"> (fuse or contactor; OI-039-005) |

---

## §16 Safety and Certification

| Requirement | Standard | Application |
|---|---|---|
| Electrical equipment and installations | CS-25.1353 | CBP trip-free design; wiring protection; HVDC protection |
| System safety — failure effects | CS-25.1309 | CB failure modes: fail-trip (safe) vs. fail-hold-closed (hazardous — prevented by trip-free design) |
| Environmental qualification | DO-160G | All CB assemblies: temperature, vibration, humidity, altitude |
| Trip-free design | CS-25.1353(a) | Cannot hold CB closed during a fault trip — mandatory |
| SSCB certification maturity | <img src="https://img.shields.io/badge/TBD-red"> | OI-039-001 — SSCB may require novel means of compliance |
| CB identification | ATA / AECMA convention | Colour collar + placard label per ATA system chapter |
| HVDC protection | CS-25.1353 + emerging standards TBD | 270 VDC protection devices under evaluation |
| In-flight remote reset prohibition | CS-25 / operational requirement | SSCB remote reset inhibited in flight (WOW or flight logic) |

---

## §17 Verification and Validation

| Test | Method | Acceptance Criterion | Status |
|---|---|---|---|
| CB trip test | Apply overcurrent at rated trip level; time to trip | Trips within TCC curve tolerance | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| CB reset test | Manual reset after trip | CB resets and holds; no retrial-trip on good circuit | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Trip-free test | Attempt to hold CB closed during fault | Cannot be held in — trips regardless of applied force | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| SSCB digital log verification | Trip event; read log via CMC terminal | Log entry with time-stamp, current, temperature within 1 s of trip | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| SSCB remote reset (ground) | Command reset via maintenance terminal | CB closes; confirmed in AFDX state message | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| SSCB in-flight remote reset inhibit | Simulate flight condition; attempt remote reset | Reset command rejected (inhibited) | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| CB collar identification | Visual check all CBs | Each CB has correct collar colour per ATA chapter assignment | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DO-160G environmental (CBP) | Per DO-160G categories applicable | All categories pass per qualification test plan | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Panel bonding resistance | Milliohm meter | ≤ 2.5 mΩ panel-to-structure | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Panel wiring insulation test | Megger 500 VDC | ≥ TBD MΩ per circuit | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| LED backlight brightness (SSCB panel) | Luminance meter | Within TBD cd/m² range | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §18 Glossary

| Term | Definition |
|---|---|
| CBP | Circuit Breaker Panel — panel assembly carrying circuit breakers protecting individual electrical circuits |
| TM-CB | Thermal-Magnetic Circuit Breaker — conventional CB using bi-metal thermal element (overload) and magnetic element (short circuit trip) |
| SSCB | Solid-State Circuit Breaker — electronic CB with digital trip logging, remote monitoring, and configurable trip threshold |
| Trip-free | CB design property: device cannot be held closed during a fault trip by external force on the actuator |
| Collar | Colour-coded ring on CB button identifying ATA system group for maintenance and operations identification |
| ELA | Electrical Load Analysis — systematic accounting of all aircraft electrical loads used to size buses, CBs, and wiring |
| TCC | Time-Current Curve — curve defining CB trip time as a function of fault current level |
| HVDC | High Voltage DC — the [PROGRAMME-VARIANT] 270 VDC bus architecture (vs. conventional 28 VDC and 115 VAC) |
| Remote reset | Ability to close a tripped SSCB via a data bus command rather than physical manual reset; permitted on ground only |
| WOW | Weight on Wheels — landing gear compressed sensor signal indicating aircraft is on ground |
| Non-volatile memory | Electronic memory retaining data when power is removed — used in SSCB controller for trip log storage |
| PDU | Power Distribution Unit — upstream device distributing bus power to CBP stud bars |
| AFDX | Avionics Full-Duplex Switched Ethernet — aircraft data bus (ARINC 664 Part 7) used for SSCB status reporting |
| CMC | Central Maintenance Computer (ATA 45) — receives SSCB logs and circuit health data |
| BITE | Built-In Test Equipment — embedded self-test in SSCB controller for fault detection |

---

## §19 Citations

1. EASA CS-25.1353 — Electrical equipment and installations.
2. EASA CS-25.1309 — Equipment, systems, and installations — system safety.
3. RTCA/EUROCAE DO-160G — Environmental Conditions and Test Procedures.
4. MIL-PRF-5764 (or equivalent TBD) — Circuit breaker military performance specification reference.
5. Q+ATLANTIDE ATLAS [039-000 General](./039-000-Electrical-Electronic-Panels-and-Multipurpose-Components-General.md).
6. Q+ATLANTIDE ATLAS [039-030 Relay, Contactor, and Power Distribution Panels](./039-030-Relay-Contactor-and-Power-Distribution-Panels.md).
7. Q+ATLANTIDE ATLAS [039-090 S1000D/CSDB Mapping](./039-090-S1000D-CSDB-Mapping-and-Traceability.md).

---

## §20 References

| Ref | Document | Notes |
|---|---|---|
| [R1] | CS-25.1353 | Electrical installations — CBP trip-free, HVDC protection |
| [R2] | CS-25.1309 | System safety — CB failure mode analysis |
| [R3] | DO-160G | Environmental qualification for CB panels |
| [R4] | MIL-PRF-5764 TBD | CB performance spec reference (or equivalent) |
| [R5] | ATA 24 — Electrical Power ATLAS | Bus power feed to CBPs |
| [R6] | ATA 45 — CMC ATLAS | SSCB log reception and fault reporting |
| [R7] | 039-030 | PDU and SSPC — upstream power distribution |
| [R8] | 039-080 | Panel monitoring and BITE — SSCB health monitoring |

---

## §21 Open Issues

| ID | Description | Owner | Status |
|---|---|---|---|
| OI-039-001 | SSCB vs. TM-CB decision: weight, cost, certification maturity for 270 VDC circuits | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-039-005 | 270 VDC vs. 115 VAC primary distribution — HVDC CBP protection scheme TBD | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-039-007 | Forward E/E bay (CBP-3) inclusion decision | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-039-012 | ELA (Electrical Load Analysis) completion — required to determine CB ratings and counts | Q-AIR | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-039-013 | SSCB certification means of compliance (novel item per CS-25 / EASA SC TBD) | Q-AIR / ORB-LEG | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §22 Change Log

| Revision | Date | Author | Description |
|---|---|---|---|
| 0.1.0 | 2026-05-10 | Q+ATLANTIDE ATLAS Working Group | Initial full-template draft; all 23 sections populated; [PROGRAMME-VARIANT] CBP context incorporated |
| 0.0.0 | 2026-05-10 | Q+ATLANTIDE ATLAS Working Group | Scaffold stub created |
