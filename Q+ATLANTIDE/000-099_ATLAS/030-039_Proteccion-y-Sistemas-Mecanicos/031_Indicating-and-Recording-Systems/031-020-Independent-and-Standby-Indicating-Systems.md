---
document_id: "QATL-ATLAS-000099-ATLAS-030039-031-020"
title: "031-020 — Independent and Standby Indicating Systems"
short_title: "Standby Instruments"
subsubject: "020"
subsubject_title: "Independent and Standby Indicating Systems"
file_name: "031-020-Independent-and-Standby-Indicating-Systems.md"
sns_reference: "031-20"
dmc_prefix: "DMC-<PROGRAMME>-<VARIANT>-031-20"
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
node_code: "031"
node_title: "Indicating and Recording Systems"
node_link: "./"
parent_path: "Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/031_Indicating-and-Recording-Systems/"
parent_path_link: "./"
ata_reference: "ATA 31"
ata_reference_link: "#20-references"
s1000d_applicability: "S1000D-CSDB-compatible"
s1000d_link: "https://s1000d.org/"
domain: "A-Aerospace"
domain_link: "../../../../../IDEALE-ESG/A-Aerospace/"
primary_q_division: "Q-MECHANICS"
primary_q_division_link: "../../../../../Q-Divisions/Q-MECHANICS/"
support_q_divisions:
  - name: "Q-AIR"
    link: "../../../../../Q-Divisions/Q-AIR/"
  - name: "Q-DATAGOV"
    link: "../../../../../Q-Divisions/Q-DATAGOV/"
orb_functions:
  - name: "ORB-PMO"
    link: "../../../../../ORB-Functions/ORB-PMO/"
  - name: "ORB-LEG"
    link: "../../../../../ORB-Functions/ORB-LEG/"
classification: "open-technical-scaffold"
status: "programme-controlled-scaffold"
revision: "0.1.0"
created: "2026-05-09"
updated: "2026-05-09"
authoring_mode: "deterministic-technical-publication"
review_status: "to-be-reviewed-by-system-expert"
lifecycle_phase:
  - code: "LC02"
    title: "Requirements Definition"
    link: "../../../../../Governance/Lifecycle/LC02-Requirements-Definition.md"
  - code: "LC03"
    title: "Architecture Definition"
    link: "../../../../../Governance/Lifecycle/LC03-Architecture-Definition.md"
  - code: "LC05"
    title: "Detailed Design"
    link: "../../../../../Governance/Lifecycle/LC05-Detailed-Design.md"
  - code: "LC06"
    title: "Verification Planning"
    link: "../../../../../Governance/Lifecycle/LC06-Verification-Planning.md"
  - code: "LC10"
    title: "Certification / Approval"
    link: "../../../../../Governance/Lifecycle/LC10-Certification-Approval.md"
  - code: "LC11"
    title: "Operation"
    link: "../../../../../Governance/Lifecycle/LC11-Operation.md"
  - code: "LC12"
    title: "Maintenance / Support"
    link: "../../../../../Governance/Lifecycle/LC12-Maintenance-Support.md"
traceability:
  atlas_node: "031_Indicating-and-Recording-Systems"
  atlas_node_link: "./"
  parent_branch: "030-039_Proteccion-y-Sistemas-Mecanicos"
  parent_branch_link: "../../"
  programme_path: "[PROGRAMME-PATH]/090_[PROGRAMME-AIRCRAFT]-Wide-Tube-and-Wing-Family"
  programme_path_link: "../../../../../[PROGRAMME-PATH]/090_[PROGRAMME-AIRCRAFT]-Wide-Tube-and-Wing-Family/"
  csdb_path: "TBD"
  csdb_path_link: "TBD"
  evidence_status: "draft"
  brex_status: "not-yet-validated"
  brex_link: "TBD"
  dmrl_status: "not-yet-frozen"
  dmrl_link: "TBD"
keywords:
  - "Q+ATLANTIDE"
  - "ATLAS"
  - "[PROGRAMME-AIRCRAFT]"
  - "S1000D"
  - "CSDB"
  - "ATA 31"
  - "Indicating and Recording"
  - "ISI"
  - "ISIS"
  - "standby instruments"
  - "standby airspeed"
  - "standby altimeter"
  - "standby compass"
standard_scope: agnostic
programme_specific: false
---

# 031-020 — Independent and Standby Indicating Systems
### [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT] · ATA 31 · Q+ATLANTIDE ATLAS Scaffold

---

## §0 Hyperlink Policy

All internal links use relative paths from the current directory. External regulatory and standards references use anchor links defined in [§20 References](#20-references). Links marked **TBD** indicate targets not yet allocated. Programme-level links traverse five directory levels (`../../../../../`). No absolute URLs are used for internal navigation.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `031-020 — Independent and Standby Indicating Systems`.

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
## §3 System / Function Overview

The ISI provides the last-resort flight reference for the crew in the event that all main display units and their driving computers fail. It is the only display that is powered independently of the main avionics network and can operate on battery power alone. The ISI contains its own AHRS (solid-state MEMS gyros and accelerometers), air data computer function (barometric altimeter and airspeed computation from standby pitot/static), and internal LCD display.

The standby compass is a purely passive magnetic instrument, providing heading reference without any electrical power. It is subject to compass swing calibration during aircraft build and after any maintenance that may affect the magnetic environment in its vicinity. Deviation card must be posted adjacent to the compass per regulatory requirements.

A standby radio altimeter display (if required by [PROGRAMME-VARIANT] operational requirements) would be driven by a dedicated radio altimeter receiver separate from the main radio altimeter systems. The need for a dedicated standby radio altimeter display versus relying on the ISI (which does not incorporate a radio altimeter function) is subject to the safety assessment and operational requirements definition currently in progress (see Open Issues).

---

## §4 Scope

### 4.1 Included
- ISI LRU: self-contained AHRS, air data, LCD display, internal battery
- Standby pitot probe (dedicated, separate from main ADC probes)
- Standby static ports (dedicated, separate from main ADC static system)
- Standby magnetic compass (wet or dry type — TBD)
- Standby radio altimeter display (if fitted — TBD)
- ISI internal battery and charger circuit
- ISI mounting tray and glareshield interface

### 4.2 Excluded
- Main ADIRU and ADC — covered under ATA 34
- Main pitot and static system — covered under ATA 34
- Main PFD display units — covered under 031-010
- DMC — covered under 031-060
- Radio altimeter transceivers (main system) — covered under ATA 34

---

## §5 Architecture Description

- **ISI self-containment**: All flight reference functions (AHRS, ADC, display) integrated in one LRU — no dependence on any external computer
- **Independent pitot/static**: Dedicated standby pitot probe and static ports with separate routing to ISI; no cross-connection with main ADC probes
- **Independent power**: ISI powered from 28VDC essential battery bus and internal rechargeable battery (minimum 30 min operation)
- **Battery monitoring**: ISI reports battery charge state to CMC; low battery generates a maintenance advisory
- **Continuous cross-check**: ISI attitude and air data cross-checked against main ADIRU outputs; disagreement triggers crew advisory via FWC
- **Standby compass**: Magnetically compensated wet compass or flux-gate type (TBD); mounted upper windshield frame; deviation card posted
- **ISI display format**: Fixed format (not configurable) — ADI, ASI, altimeter on single LCD panel; crew cannot reformat or select alternative pages

---

## §6 Functional Breakdown

| Function ID | Function Title | Description | Applicable System |
|---|---|---|---|
| F-001 | Standby Attitude (Pitch and Roll) | AHRS-based attitude indication on ISI LCD, independent of main ADIRU | ISI AHRS function |
| F-002 | Standby Airspeed | Air data computation from standby pitot; displayed on ISI LCD | ISI ADC function |
| F-003 | Standby Altitude | Barometric altitude from standby static; baroset knob on ISI | ISI ADC function |
| F-004 | Standby Compass / Heading | Magnetic heading from wet compass or flux-gate compass mounted in windshield frame | Standby compass LRU |
| F-005 | Standby Radio Altitude | Radio altimeter height below ~2500 ft AGL (if standby RA display fitted) | Standby RA display (TBD) |
| F-006 | Independent Power Supply Management | ISI internal battery charge management; monitoring and reporting to CMC | ISI battery subsystem |
| F-007 | ISI BITE and Self-Test | Continuous internal monitoring; crew-initiated ground self-test; BITE fault to CMC | ISI BITE function |

---

## §7 System Context Diagram

```mermaid
flowchart LR
    ISI_LRU[031-020 ISI LRU] --> GLARESHIELD[Glareshield Centre Panel]
    STDBY_PITOT[Standby Pitot Probe] -->|Pitot pressure| ISI_LRU
    STDBY_STATIC[Standby Static Ports] -->|Static pressure| ISI_LRU
    BAT_BUS[28VDC Essential Battery Bus] -->|Primary power| ISI_LRU
    ISI_INT_BAT[ISI Internal Battery] -->|Emergency power| ISI_LRU
    ISI_LRU -->|BITE status| CMC[031-080 CMC]
    ISI_LRU -.->|Cross-check disagreement| FWC[031-050 FWC]
    COMPASS[Standby Compass] --> WINDSHIELD_FRAME[Upper Windshield Frame]
    ATA24[ATA 24 — Essential Bus] -->|28VDC| BAT_BUS
    ISI_LRU -.->|Independent of| ADIRU[ATA 34 — Main ADIRU]
    ISI_LRU -.->|Independent of| IMA[IMA Platform]
```

---

## §8 Internal Functional Architecture

```mermaid
flowchart TB
    PITOT_PORT[Standby Pitot Input] --> ADC_FUNC[ISI Air Data Function]
    STATIC_PORT[Standby Static Input] --> ADC_FUNC
    ADC_FUNC --> ASI_DISP[Airspeed Display]
    ADC_FUNC --> ALT_DISP[Altitude Display]
    GYRO[MEMS Gyros + Accelerometers] --> AHRS_FUNC[ISI AHRS Function]
    AHRS_FUNC --> ATT_DISP[Attitude Display ADI]
    BARO_SET[Barosetting Knob] --> ADC_FUNC
    POWER_MGMT[Power Management] --> INT_BAT[Internal Battery]
    POWER_MGMT --> MAIN_POWER[Main 28VDC Input]
    BITE[BITE Monitor] --> ADC_FUNC
    BITE --> AHRS_FUNC
    BITE --> INT_BAT
    BITE -->|Fault status| CMC_IF[CMC Interface — A429]
    LCD[ISI LCD Display] --> ASI_DISP
    LCD --> ALT_DISP
    LCD --> ATT_DISP
```

---

## §9 Lifecycle Traceability

```mermaid
flowchart LR
    LC02[LC02 Requirements Definition] --> LC03[LC03 Architecture Definition]
    LC03 --> LC05[LC05 Detailed Design]
    LC05 --> LC06[LC06 Verification Planning]
    LC06 --> LC10[LC10 Certification / Approval]
    LC10 --> LC11[LC11 Operation]
    LC11 --> LC12[LC12 Maintenance / Support]
    LC12 --> LC13[LC13 Disposal / Decommission]
    LC02 -->|CS-25.1307 independence requirements| REQ[ISI System Requirements]
    LC03 -->|ISI supplier selection, pitot routing| ARCH[Standby Architecture]
    LC05 -->|ISI LRU design, pitot/static routing| DESIGN[ISI Design Package]
    LC06 -->|Independence test plan, battery test| VPLAN[Verification Plans]
    LC10 -->|Independence demonstration, EASA approval| TC[TC Data — 031-20]
    LC11 -->|QRH standby instrument procedures| OPS[QRH Procedures]
    LC12 -->|AMM 31-20: ISI battery test interval| MAINT[Maintenance Data]
```

---

## §10 Interfaces

| Interface ID | System / Chapter | Interface Type | Data / Signal | Direction | Status |
|---|---|---|---|---|---|
| IF-031-020-001 | ATA 24 Essential Battery Bus | 28VDC | Primary electrical power to ISI | ATA24 → ISI | <img src="https://img.shields.io/badge/TBD-red"> |
| IF-031-020-002 | ATA 34 Standby Pitot | Pneumatic | Standby pitot total pressure | Standby pitot → ISI | <img src="https://img.shields.io/badge/TBD-red"> |
| IF-031-020-003 | ATA 34 Standby Static | Pneumatic | Standby static pressure | Standby static → ISI | <img src="https://img.shields.io/badge/TBD-red"> |
| IF-031-020-004 | 031-080 CMC | ARINC 429 | BITE fault data from ISI | ISI → CMC | <img src="https://img.shields.io/badge/TBD-red"> |
| IF-031-020-005 | 031-050 FWC | AFDX / Discrete | ISI disagree advisory trigger | ISI → FWC | <img src="https://img.shields.io/badge/TBD-red"> |
| IF-031-020-006 | 031-010 (physical) | Mechanical | ISI mounting on glareshield centre position | Physical interface | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §11 Operating Modes

| Mode ID | Mode Name | Description | Entry Condition | Exit Condition |
|---|---|---|---|---|
| OM-001 | Active (Normal) | ISI operating on main bus power; cross-checking against main ADIRU | Aircraft powered, all buses healthy | Power loss or ISI failure |
| OM-002 | Alert (Disagree) | ISI attitude or air data disagrees with main PFD; advisory displayed on ISI LCD | ISI vs ADIRU disagreement > threshold | Disagreement resolved |
| OM-003 | Standby (Primary Reference) | Main PFDs failed; ISI is primary flight reference for crew; remains on main bus power | All main PFDs failed | Main PFDs restored |
| OM-004 | Battery-Powered | ISI operating on internal battery only; total aircraft electrical failure | Main bus power loss | Main bus power restored |
| OM-005 | Ground Test | Crew-initiated ISI self-test; all functions verified; BITE results displayed | Ground only + maintenance access | Test complete / pass / fail |

---

## §12 Monitoring and Diagnostics

The ISI performs continuous internal BITE monitoring covering the AHRS function (gyro drift, accelerometer health), air data function (pitot/static pressure transducer health), LCD display health, and internal battery charge state. Fault status is reported to the CMC via ARINC 429 at regular intervals. A failed AHRS or ADC function is displayed as a red cross over the affected parameter on the ISI LCD display, providing immediate crew awareness.

Battery charge monitoring: the ISI reports battery state of charge to the CMC. A battery charge below the serviceable threshold (TBD — typically 80% of rated capacity for 30-min reserve) generates a maintenance advisory, schedulable for the next ground check. Battery replacement interval is defined in the AMM (TBD — typically 2 years or per manufacturer specification).

A crew-initiated ground self-test is available from the cockpit (procedure in AMM 31-20). The self-test exercises all ISI internal functions including a brief battery power-only test (30-second duration), and reports pass/fail via the CMC and an ISI-local display indication.

---

## §13 Maintenance Concept

The ISI is an LRU replaced at line maintenance. No calibration of the AHRS or ADC is required after replacement — the ISI contains all calibration data internally. Battery replacement is performed by removing the ISI LRU and following the CMM (Component Maintenance Manual) battery replacement procedure (TBD). Post-installation, a mandatory ground self-test per AMM is required to confirm ISI serviceability before return to service.

The standby pitot probe and static ports require periodic cleaning and check for obstruction per AMM. The probe heating element (if fitted on standby pitot) is checked during the periodic pitot heat functional test. Standby compass swing is performed after any maintenance that alters the magnetic environment within 1 m of the compass; a deviation table is updated and posted adjacent to the compass per AMM procedure.

---

## §14 S1000D / CSDB Mapping

### 14.1 SNS to DMC Mapping

| SNS Code | Subsubject | DMC Prefix | Info Codes Planned | DMRL Status |
|---|---|---|---|---|
| 031-20 | Independent and Standby Indicating Systems | DMC-<PROGRAMME>-<VARIANT>-031-20 | 040, 300, 400, 520, 720 | <img src="https://img.shields.io/badge/TBD-red"> |
| 031-20-01 | ISI LRU | DMC-<PROGRAMME>-<VARIANT>-031-20-01 | 040, 400, 520, 720 | <img src="https://img.shields.io/badge/TBD-red"> |
| 031-20-02 | Standby Compass | DMC-<PROGRAMME>-<VARIANT>-031-20-02 | 040, 400, 520 | <img src="https://img.shields.io/badge/TBD-red"> |
| 031-20-03 | Standby Pitot and Static | DMC-<PROGRAMME>-<VARIANT>-031-20-03 | 040, 400, 520 | <img src="https://img.shields.io/badge/TBD-red"> |

### 14.2 Information Code Definitions (031-20)

| Info Code | Description | Notes |
|---|---|---|
| 040 | System description — ISI architecture, independence rationale | AMM/FCOM basis |
| 300 | Operation — standby instrument use procedures, battery-powered flight | QRH/FCOM |
| 400 | Maintenance — ISI ground test, battery check, compass swing | AMM tasks |
| 520 | Troubleshooting — ISI disagree fault, BITE codes | FRM/TSM |
| 720 | Removal and installation — ISI LRU R&R, standby pitot probe | AMM |

---

## §15 Footprints

### 15.1 Physical Footprint
- ISI: Single LRU, glareshield centre position; approximately 4×4 inch bezel (TBD per supplier); mounted between captain and FO positions
- Standby pitot probe: port or starboard fuselage nose area (separate from main probes), zone TBD
- Standby static ports: fuselage positions separate from main static system, zone TBD
- Standby compass: upper centre windshield frame, accessible to both pilots

### 15.2 Electrical / Data Footprint
- Power: 28VDC from essential battery bus (normal); internal battery (emergency, 30 min min)
- Data: ARINC 429 output to CMC (BITE); discrete output to FWC (disagree signal); pneumatic interface to standby pitot/static
- Battery: internal sealed rechargeable battery (lithium-ion or NiMH — TBD per supplier)

### 15.3 Maintenance Footprint
- ISI LRU: tool-free replacement (TBD per supplier; typically bayonet mount); no post-installation calibration
- Battery: replaced per CMM; interval per AMM (TBD — target 2 years or 80% capacity threshold)
- Standby pitot: cleaned per AMM interval; probe heat check per functional test schedule
- Compass swing: performed after magnetic-affecting maintenance; deviation card posted

### 15.4 Data Footprint
- ISI non-volatile BITE log: last 50 fault events stored internally; downloaded via CMC
- Battery charge state: transmitted to CMC at power-up and on request
- Compass swing deviation data: posted deviation table (physical card) + stored in aircraft maintenance record

---

## §16 Safety and Certification Considerations

| Requirement | Source | Description | Compliance Approach | Status |
|---|---|---|---|---|
| CS-25.1307(a) | EASA CS-25 | Standby instruments mandatory; independent of main avionics bus | ISI on independent battery bus + internal battery; separate pitot/static | <img src="https://img.shields.io/badge/TBD-red"> |
| CS-25.1303(b)(1) | EASA CS-25 | Magnetic compass mandatory | Standby wet or flux-gate compass fitted; deviation card posted | <img src="https://img.shields.io/badge/TBD-red"> |
| AMC 25.1307 | EASA AMC | ISI independence from main avionics power bus | Analysis + ground test demonstrating ISI operation with all main buses de-powered | <img src="https://img.shields.io/badge/TBD-red"> |
| CS-25.1309 | EASA CS-25 | Equipment failure condition analysis — standby instrument failure | FHA for ISI failure — expected minor failure condition (main PFDs available) | <img src="https://img.shields.io/badge/TBD-red"> |
| EUROCAE ED-14G | EUROCAE | Environmental qualification of ISI LRU | ISI qualified to ED-14G applicable categories (temperature, vibration, humidity) | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §17 Verification and Validation

| V&V ID | Requirement | Method | Success Criterion | Status |
|---|---|---|---|---|
| VV-031-020-001 | CS-25.1307 — standby instrument independence | Analysis + Ground Test | ISI operates correctly on internal battery with ALL main avionics buses de-energised | <img src="https://img.shields.io/badge/TBD-red"> |
| VV-031-020-002 | CS-25.1307 — standby pitot/static independence | Analysis | Standby pitot/static lines confirmed not cross-connected to main ADC probes | <img src="https://img.shields.io/badge/TBD-red"> |
| VV-031-020-003 | CS-25.1303 — standby compass visibility | Cockpit mock-up | Compass readable from both crew seated positions without excessive head movement | <img src="https://img.shields.io/badge/TBD-red"> |
| VV-031-020-004 | ISI battery — 30-minute reserve | Ground Test | ISI operates on internal battery for 30 minutes minimum under worst-case temperature | <img src="https://img.shields.io/badge/TBD-red"> |
| VV-031-020-005 | ISI accuracy — attitude | Ground Test + Flight Test | ISI attitude within ±2° of reference during steady flight (or per supplier MOPS) | <img src="https://img.shields.io/badge/TBD-red"> |
| VV-031-020-006 | ISI accuracy — airspeed and altitude | Ground Test (pitot-static rig) | ISI airspeed within ±5 kt and altitude within ±50 ft of reference (per MOPS) | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §18 Glossary

| Term | Acronym | Definition |
|---|---|---|
| Integrated Standby Instrument | ISI | Self-contained LRU providing standby attitude, airspeed, and altitude, independent of main avionics |
| Integrated Standby Instrument System | ISIS | Alternative designation for ISI used by some manufacturers |
| Attitude and Heading Reference System | AHRS | System providing aircraft attitude (pitch/roll) and heading using inertial sensors |
| Standby Airspeed | — | Airspeed indication derived from dedicated standby pitot probe, independent of main ADC |
| Standby Altimeter | — | Barometric altitude derived from dedicated standby static ports, independent of main ADC |
| Barometric Setting | Baroset | Altimeter datum reference pressure set by the crew (QNH or STD) |
| Pitot-Static System | — | System of probes and tubing providing total and static pressure for air data computation |
| Standby Compass | — | Magnetic compass (wet or flux-gate type) providing heading reference without electrical power dependency |
| Radio Altimeter | RA | Radar-based system measuring true height above ground; standby RA display may be fitted if required |
| Independent Power Supply | — | Electrical supply not shared with main avionics; includes internal battery as last-resort power source |
| Disagree Alert | — | Alert generated when ISI data differs from main ADIRU data beyond a defined threshold |
| Compass Swing | — | Calibration procedure to determine and correct magnetic compass deviation errors |
| Deviation Card | — | Table posted adjacent to compass showing residual deviation errors after compass swing |

---

## §19 Citations

| Citation ID | Source | Title / Description | Relevance |
|---|---|---|---|
| CIT-031-020-001 | EASA | CS-25 §1307(a) — Miscellaneous Equipment (standby instruments) | Primary regulatory requirement |
| CIT-031-020-002 | EASA | AMC 25.1307 — Acceptable Means of Compliance for standby instruments | ISI independence design guidance |
| CIT-031-020-003 | EASA | CS-25 §1303(b)(1) — Magnetic Compass | Standby compass requirement |
| CIT-031-020-004 | EUROCAE | ED-14G (DO-160G) — Environmental Qualification | ISI LRU environmental qualification |
| CIT-031-020-005 | EUROCAE | ED-12C (DO-178C) — Software Considerations | ISI AHRS and ADC software assurance |

---

## §20 References

| Ref ID | Document | Title | Version | Link |
|---|---|---|---|---|
| REF-031-020-001 | EASA CS-25 | Certification Specifications for Large Aeroplanes — §1307 | Amdt 27 | [CS-25](https://www.easa.europa.eu/) |
| REF-031-020-002 | EASA AMC 25.1307 | AMC to CS-25 §1307 — Standby Instruments | Current | [EASA AMC](https://www.easa.europa.eu/) |
| REF-031-020-003 | EUROCAE ED-14G | Environmental Conditions and Test Procedures for Airborne Equipment | 2012 | [ED-14G](https://eurocae.net/) |
| REF-031-020-004 | EUROCAE ED-12C | Software Considerations in Airborne Systems | 2011 | [ED-12C](https://eurocae.net/) |
| REF-031-020-005 | 031-000 | Indicating and Recording Systems — General | 0.1.0 | [031-000](./031-000-Indicating-and-Recording-General.md) |

---

## §21 Open Issues

| Issue ID | Description | Owner | Priority | Target Date | Status |
|---|---|---|---|---|---|
| OI-031-020-001 | ISI supplier selection not yet started | Procurement | High | LC03 | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-031-020-002 | Standby compass type — wet compass vs flux-gate not decided | Avionics Architect | Medium | LC03 | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-031-020-003 | Standby radio altitude display — requirement TBD; pending operational requirements review | Systems Engineer | Medium | LC02 | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-031-020-004 | ISI disagree alert threshold values not yet defined | Systems Safety | Medium | LC05 | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-031-020-005 | Battery capacity and replacement interval not yet defined (depends on ISI supplier) | Avionics Engineer | Low | LC05 | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §22 Change Log

| Revision | Date | Author | Description of Change |
|---|---|---|---|
| 0.1.0 | 2026-05-09 | ATLAS Scaffold Generator | Initial scaffold creation — all sections populated; marked DRAFT |

<img src="https://img.shields.io/badge/DRAFT-yellow"> This document is a programme-controlled scaffold. All content is subject to review by the responsible system expert before formal issue.
