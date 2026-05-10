---
document_id: "QATL-ATLAS-000099-ATLAS-030039-037-080"
title: "037-080 — Vacuum Monitoring, Diagnostics, and Control Interfaces"
short_title: "Vacuum Monitoring and Diagnostics"
subsubject: "080"
subsubject_title: "Vacuum Monitoring, Diagnostics, and Control Interfaces"
file_name: "037-080-Vacuum-Monitoring-Diagnostics-and-Control-Interfaces.md"
sns_reference: "037-80"
dmc_prefix: "DMC-AMPEL360E-EWTW-037-80"
programme: "AMPEL360e eWTW"
programme_link: "../../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/"
short_code: "AMPEL360e-eWTW"
register: "Q+ATLANTIDE ATLAS"
register_link: "../../../../../Q+ATLANTIDE/"
architecture_band: "030-039 Protection and Mechanical Systems"
architecture_band_link: "../../../"
architecture_band_title: "Protection and Mechanical Systems"
code_range: "037"
code_range_link: "../../"
code_range_title: "Vacuum"
node_code: "037"
node_title: "Vacuum"
node_link: "./"
parent_path: "Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/037_Vacuum/"
parent_path_link: "./"
ata_reference: "ATA 37"
ata_reference_link: "https://www.airlines.org/dataset/ata-spec-2200/"
s1000d_applicability: "S1000D Issue 5.0"
s1000d_link: "https://www.s1000d.org/"
domain: "Airworthiness / Aircraft Systems"
domain_link: "https://www.easa.europa.eu/en/document-library/easy-access-rules/easy-access-rules-large-aeroplanes-cs-25"
primary_q_division: "Q-DIGITAL"
primary_q_division_link: "../../../../../Q-DIGITAL/"
support_q_divisions: ["Q-SYSTEMS", "Q-AVIONICS", "Q-SAFETY"]
orb_functions: ["FUNCTION-VACUUM-MONITORING", "FUNCTION-VACUUM-DIAGNOSTICS", "FUNCTION-BITE", "FUNCTION-OMS"]
classification: "UNCLASSIFIED — ENGINEERING SCAFFOLD"
status: "DRAFT"
revision: "0.1.0"
created: "2025-07-14"
updated: "2025-07-14"
authoring_mode: "AI-assisted scaffold"
review_status: "PENDING"
lifecycle_phase: "LC02 — System Definition"
traceability: ["CS-25.1438", "CS-25.1301", "CS-25.1309", "AMC 25.831"]
keywords: ["ATA 37", "Vacuum", "CMC", "OMS", "BITE", "diagnostics", "fault codes", "EVG monitoring", "waste tank level", "freeze protection", "AFDX"]
---

# 037-080 — Vacuum Monitoring, Diagnostics, and Control Interfaces
### AMPEL360e eWTW · ATA 37 · Q+ATLANTIDE ATLAS Scaffold

**Status:** <img src="https://img.shields.io/badge/DRAFT-yellow">
**Revision:** 0.1.0 | **Created:** 2025-07-14 | **Updated:** 2025-07-14

---

## §0 Hyperlink Policy

All links in this document are relative within the Q+ATLANTIDE ATLAS repository unless explicitly marked as external. External links reference publicly available standards only. Internal cross-references use relative paths from the `037_Vacuum/` node. All YAML `*_link` fields follow this convention.

---

## §1 Purpose

This document defines the **monitoring, diagnostics, and control interface architecture** for the ATA 37 Vacuum System on the AMPEL360e eWTW. It specifies:
- All monitored parameters (sensors, ranges, fault thresholds)
- BITE (Built-In Test Equipment) functionality — power-up self-test and continuous monitoring
- CMC / OMS data flow and fault logging
- Maintenance diagnostic commands and control interfaces
- Freeze protection monitoring concept
- OMS health trend analysis (EVG degradation)
- Data bus architecture (AFDX / ARINC 429 TBD)

---

## §2 Applicability

| Item | Value |
|------|-------|
| Aircraft Programme | AMPEL360e eWTW |
| ATA Chapter | 37 — Vacuum |
| Subsubject | 037-80 — Monitoring, Diagnostics, and Control Interfaces |
| Certification Basis | CS-25 Amendment 27 (TBD) |
| Applicable Standards | CS-25.1438, CS-25.1301, CS-25.1309, AMC 25.831 |
| Revision Status | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| Configuration | ~100-pax single-aisle electric |

---

## §3 System / Function Overview

### 3.1 Monitored Parameters

| Parameter | Sensor Type | Location | Normal Range | Advisory Threshold | Fault Threshold | CMC Response |
|-----------|-------------|----------|--------------|-------------------|-----------------|--------------|
| Manifold vacuum | Piezoresistive transducer | Vacuum manifold body | −0.7 to −1.0 bar gauge | < −0.5 bar | < −0.3 bar | VAC LO → VAC SYS FAULT |
| EVG-1 motor current | Hall-effect current sensor | EVG-1 controller | <img src="https://img.shields.io/badge/TBD-red"> A | > TBD A (over) | > TBD A or < TBD A (stall) | EVG-1 FAULT |
| EVG-2 motor current | Hall-effect current sensor | EVG-2 controller | <img src="https://img.shields.io/badge/TBD-red"> A | > TBD A | > TBD A or < TBD A | EVG-2 FAULT |
| EVG-1 outlet pressure | Pressure sensor | EVG-1 outlet port | <img src="https://img.shields.io/badge/TBD-red"> bar | TBD | TBD | EVG-1 FAULT |
| EVG-2 outlet pressure | Pressure sensor | EVG-2 outlet port | <img src="https://img.shields.io/badge/TBD-red"> bar | TBD | TBD | EVG-2 FAULT |
| Waste tank fill level | Capacitive / float (TBD) | Waste tank — ATA 38 | 0–74% | > 75% | > 95% | WASTE TANK HI / FULL |
| EFV-1 position | Micro-switch / optical TBD | EFV-1 Lavatory FWD | Open/Closed | Slow response TBD | Stuck open/closed | LAV-1 FAULT TBD |
| EFV-2 position | Micro-switch / optical TBD | EFV-2 Lavatory MID | Open/Closed | Slow response TBD | Stuck open/closed | LAV-2 FAULT TBD |
| EFV-3 position | Micro-switch / optical TBD | EFV-3 Lavatory AFT | Open/Closed | Slow response TBD | Stuck open/closed | LAV-3 FAULT TBD |
| Freeze temp (TBD) | NTC thermistor TBD | Waste line cold zone TBD | > +5°C | < +5°C | < 0°C | FREEZE RISK TBD |
| EVG-1 vibration | Accelerometer TBD | EVG-1 housing TBD | < TBD g RMS | TBD | TBD | EVG-1 VIBRATION FAULT TBD |

> **Note:** Sensor types, locations, and thresholds are <img src="https://img.shields.io/badge/TBD-red"> pending supplier selection and system design freeze. OI-037-001 (EVG sizing) affects sensor specifications.

### 3.2 BITE Description

Built-In Test Equipment (BITE) functions for ATA 37:

| BITE Function | Type | Trigger | Duration | Pass Criteria | Fail Action |
|--------------|------|---------|----------|---------------|-------------|
| EVG-1 power-up self-test | Automatic | Power-up / reset | < TBD s | Vacuum achieved ≥ −0.7 bar in < TBD s; current nominal | CMC fault code logged; EVG-2 auto-start |
| EVG-2 power-up self-test | Automatic | Power-up / reset (after EVG-1 pass) | < TBD s | Same as EVG-1 criteria | CMC fault code logged; VAC SYS FAULT alert |
| EFV continuity check | Automatic | Power-up | < 1 s TBD | Solenoid coil resistance within limits | CMC EFV fault code |
| Manifold transducer check | Automatic | Power-up | < 1 s TBD | Transducer reading plausible (aircraft on ground → near-atmospheric) | CMC transducer fault |
| Manual vacuum test | Commanded | Maintenance terminal | ~20 min | Per ground test acceptance criteria | Fault detail on terminal |

---

## §4 Scope

This document covers:
- Sensor architecture and monitored parameter list
- BITE (power-up and continuous) definition
- CMC data collection, fault logging, and OMS interface
- Maintenance terminal diagnostic commands and control interface
- Freeze protection monitoring concept (OI-037-005)
- Data bus architecture (AFDX / ARINC 429 TBD)
- OMS health trend analysis concept

This document does **not** cover: hardware sensor procurement, CMC hardware (ATA 45), ECAM display (ATA 31), or ground test procedures (037-070).

---

## §5 Architecture Description

### 5.1 Monitoring Architecture

```
EVG-1 Controller ──────────────────────────────────────┐
 └ Motor current sensor                                 │
 └ Outlet pressure sensor                               │
 └ Self-test (BITE)                                     │
                                                        ├──→ Data Concentrator (ATA 42 / LRU TBD)
EVG-2 Controller ──────────────────────────────────────┤        │
 └ Motor current sensor                                 │        ↓
 └ Outlet pressure sensor                               │   AFDX Bus (ATA 42)
 └ Self-test (BITE)                                     │        │
                                                        │        ↓
Manifold Transducer ────────────────────────────────────┤   CMC (ATA 45)
                                                        │    │          │
Waste Tank Level Sensor (ATA 38) ───────────────────────┤    ↓          ↓
                                                        │  ECAM       OMS /
EFV-1/2/3 Position Sensors ─────────────────────────────┘  CAS     Maintenance
                                                               Terminal
Freeze Temp Sensor (TBD) ──────────────────────────────────→ Data Concentrator
```

### 5.2 Control Interface Description

The maintenance terminal (OMS) provides the following control commands to the vacuum system (authorized personnel only, with audit trail):

| Command | Target | Mode | Safety Interlock |
|---------|--------|------|-----------------|
| EVG-1 START | EVG-1 controller | Ground only | Aircraft weight-on-wheels (WoW) or maintenance mode active |
| EVG-1 STOP | EVG-1 controller | Ground only | WoW or maintenance mode |
| EVG-2 START | EVG-2 controller | Ground only | WoW or maintenance mode |
| EVG-2 STOP | EVG-2 controller | Ground only | WoW or maintenance mode |
| EFV-1/2/3 OPEN | EFV solenoid | Ground test only | Maintenance mode + waste tank < 95% |
| EFV-1/2/3 CLOSE | EFV solenoid | Ground test only | Maintenance mode |
| SOV OPEN | SOV solenoid | Maintenance | WoW or maintenance mode |
| SOV CLOSE | SOV solenoid | Maintenance | WoW or maintenance mode |
| FAULT LOG CLEAR | CMC NVM | Maintenance | Authorized personnel (Level 2 access TBD) |
| VACUUM TEST START | Automated test sequence | Ground | WoW; EVG not running |

### 5.3 Data Bus Architecture

| Bus | Protocol | Used For | Status |
|-----|----------|----------|--------|
| AFDX (ARINC 664) | Ethernet-based | CMC ↔ EVG controller, ECAM, OMS | <img src="https://img.shields.io/badge/TBD-red"> — confirm with avionics ICD |
| ARINC 429 | Serial bus | Alternative if AFDX not available on this LRU | <img src="https://img.shields.io/badge/TBD-red"> |
| RS-485 | Serial | EVG internal controller to data concentrator TBD | <img src="https://img.shields.io/badge/TBD-red"> |
| CAN bus | Controller Area Network | Alternative EVG controller bus TBD | <img src="https://img.shields.io/badge/TBD-red"> |
| Discrete wiring | Hard-wired | EFV flush button, flush indicator, EFV position (analog) | Planned |

---

## §6 Functional Breakdown

### 6.1 Continuous In-Service Monitoring Functions

| Function ID | Description | Update Rate | Data Destination |
|-------------|-------------|-------------|-----------------|
| MON-037-01 | Manifold vacuum measurement | 1 Hz TBD | CMC, ECAM |
| MON-037-02 | EVG-1 motor current measurement | 10 Hz TBD | CMC, EVG controller |
| MON-037-03 | EVG-2 motor current measurement | 10 Hz TBD | CMC, EVG controller |
| MON-037-04 | Waste tank level measurement | 0.1 Hz TBD | CMC, ECAM (ATA 38 sensor) |
| MON-037-05 | EFV position monitoring | Event-driven | CMC, flush indicator |
| MON-037-06 | Freeze temperature monitoring | 0.1 Hz TBD (if installed) | CMC |
| MON-037-07 | EVG run-time accumulation | 1 Hz | CMC NVM |
| MON-037-08 | Vacuum pull-down time (per EVG start) | Per-event | CMC NVM (OMS trend) |

### 6.2 OMS Health Trend Analysis

The OMS monitors EVG performance trends over time:

| Trend Parameter | Nominal Baseline | Degradation Indicator | OMS Alert Threshold |
|----------------|-----------------|----------------------|---------------------|
| EVG-1 pull-down time (to −0.7 bar) | TBD s (established at delivery) | Pull-down time increasing by > TBD s over TBD flights | OMS advisory — schedule EVG inspection |
| EVG-2 pull-down time | TBD s | Same as EVG-1 | OMS advisory |
| EVG-1 run hours since last service | 0 h at service | > TBD h | OMS scheduled maintenance alert |
| EVG-2 run hours since last service | 0 h at service | > TBD h | OMS scheduled maintenance alert |
| Flush cycle count since last service | 0 at service | > TBD cycles | OMS odour filter replacement advisory |

---

## §7 System Context Diagram

```mermaid
flowchart LR
    EVG1_CTRL[EVG-1 Controller\nSensors: current\noutlet pressure\nself-test] --> DC[Data Concentrator\nLRU TBD]
    EVG2_CTRL[EVG-2 Controller\nSensors: current\noutlet pressure\nself-test] --> DC
    MAN_T[Manifold Transducer\nPressure sensor] --> DC
    EFV_POS[EFV-1/2/3\nPosition sensors] --> DC
    TANK_LVL[Waste Tank Level\nSensor ATA 38] --> DC
    TEMP_S[Freeze Temp Sensor TBD\nWaste line] --> DC

    DC -->|AFDX / ARINC 429 TBD| CMC[CMC ATA 45\nFault logic\nData logging]
    CMC -->|AFDX| ECAM[ECAM\nVAC page\nCAS alerts]
    CMC -->|OMS data| OMS_TERM[OMS Maintenance\nTerminal]
    CMC -->|ACARS TBD| GROUND_UPLINK[Ground Uplink\nACOMS TBD]
    OMS_TERM -->|Commands| CMD_BUS[Command Bus\nSOV / EFV / EVG control]
    CMD_BUS --> EVG1_CTRL & EVG2_CTRL
```

---

## §8 Internal Functional Architecture

```mermaid
flowchart TB
    PWR_UP[Aircraft power-up] --> BITE_AUTO[Automatic BITE\nEVG self-test\nEFV continuity\nTransducer check]
    BITE_AUTO -->|Pass| NRM_MON[Normal in-service\nmonitoring begins]
    BITE_AUTO -->|Fail| BITE_FAIL[CMC fault code logged\nCAS alert generated]

    NRM_MON --> CONT_MON[Continuous parameter\nmonitoring 1 Hz TBD]
    CONT_MON --> FAULT_DET{Fault detected?}
    FAULT_DET -->|NO| CONT_MON
    FAULT_DET -->|YES| FAULT_CLASS{Fault\nclassification}
    FAULT_CLASS -->|Advisory| ADV_LOG[CMC logs advisory\nOMS alert]
    FAULT_CLASS -->|Caution| CAS_GEN[CMC generates\nCAS alert\nECAM VAC page update]
    CAS_GEN --> EVG_FAIL{EVG-1 fault?}
    EVG_FAIL -->|YES| EVG2_AUTO[EVG-2\nauto-start]
    EVG2_AUTO --> MON_RESTORE{Vacuum\nrestored?}
    MON_RESTORE -->|YES| DEGRADE[Degraded mode\nEVG-2 running\nCMC log continues]
    MON_RESTORE -->|NO| SYS_FAULT[VAC SYS FAULT\nCAS amber\nBoth EVGs failed]

    MAINT_CMD[Maintenance terminal\ndiagnostic command] --> AUTH_CHK{Authorized\nmode?}
    AUTH_CHK -->|YES| CMD_EXE[Execute command\nEVG / EFV / SOV control]
    AUTH_CHK -->|NO| CMD_REJ[Command rejected\nLog attempt]
    CMD_EXE --> LOG_CMD[Log command\naudit trail CMC]
```

---

## §9 Lifecycle Traceability

```mermaid
flowchart LR
    LC02[LC02\nRequirements\nCS-25.1309\nSafety assessment\nmonitoring req.] --> LC03[LC03\nSystem Definition\nSensor architecture\nBITE definition\nData bus selection]
    LC03 --> LC04[LC04\nSoftware\nDesign\nCMC fault logic\nOMS trend algorithm]
    LC04 --> LC05[LC05\nHardware +\nSoftware\nDevelopment\nSensor procurement\nData concentrator]
    LC05 --> LC06[LC06\nIntegration\nAFDX ICD\nvalidation]
    LC06 --> LC08[LC08\nGround Test\nBITE test\nFault injection\nCMC validation]
    LC08 --> LC09[LC09\nFlight Test\nIn-flight\nmonitoring\nvalidation]
    LC09 --> LC10[LC10\nCertification\nCS-25.1309\ncompliance\nFMEA approval]
    LC10 --> LC11[LC11\nIn-Service\nAMM 037-80\nOMS trend\noperational]
```

---

## §10 Interfaces

| Interface ID | ATA Chapter | Direction | Protocol | Description | Status |
|-------------|-------------|-----------|----------|-------------|--------|
| IF-037-080-001 | ATA 45 (CMC/OMS) | ATA 37 ↔ ATA 45 | AFDX | All monitoring data to CMC; maintenance commands from OMS to EVG/EFV/SOV | <img src="https://img.shields.io/badge/TBD-red"> |
| IF-037-080-002 | ATA 31 (ECAM) | ATA 45 → ATA 31 | AFDX | CAS alerts, ECAM VAC page data (via CMC to ECAM) | <img src="https://img.shields.io/badge/TBD-red"> |
| IF-037-080-003 | ATA 38 | ATA 38 → ATA 37/CMC | AFDX / discrete | Waste tank level sensor data | <img src="https://img.shields.io/badge/TBD-red"> |
| IF-037-080-004 | ATA 42 | ATA 37 ↔ ATA 42 | AFDX | AFDX network infrastructure | <img src="https://img.shields.io/badge/TBD-red"> |
| IF-037-080-005 | ATA 24 | ATA 24 → ATA 37 | Power | 115 VAC for EVG; 28 VDC for EFV solenoids, sensors, controllers | <img src="https://img.shields.io/badge/TBD-red"> |
| IF-037-080-006 | Ground (ACARS) | ATA 45 → Ground | ACARS TBD | OMS health trend data uplink to airline maintenance | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §11 Operating Modes

| Mode ID | Mode Name | Description | BITE | Monitoring | Maintenance Control |
|---------|-----------|-------------|------|------------|---------------------|
| OM-037-80-01 | BITE mode | Power-up self-test sequence | Active — auto | Limited | Disabled |
| OM-037-80-02 | Normal monitoring | In-service continuous monitoring | Passive (continuous) | Full | Disabled (flight) |
| OM-037-80-03 | Degraded monitoring | EVG-1 fault; EVG-2 running | Passive | Full | Disabled |
| OM-037-80-04 | Fault — total vacuum loss | Both EVGs failed; CAS alert active | Passive | Reduced (fault state) | Disabled |
| OM-037-80-05 | Ground test mode | Maintenance terminal-commanded test | Manual (commanded) | Full | Enabled |
| OM-037-80-06 | Maintenance diagnostic mode | Fault log review, parameter view, component command | N/A | Full read | Enabled (authorized) |
| OM-037-80-07 | Ground power-up BITE | Auto BITE on ground power application | Active — auto | Full | Disabled during BITE |

---

## §12 Monitoring and Diagnostics — Fault Code Table

| Fault Code | Description | Severity | Auto Action | Maintenance Action |
|------------|-------------|----------|-------------|-------------------|
| F-037-001 | EVG-1 failed to reach vacuum threshold within TBD s | Caution | EVG-2 auto-start | Inspect EVG-1; check CMC log |
| F-037-002 | EVG-2 failed to reach vacuum threshold (EVG-1 also failed) | Warning | CAS VAC SYS FAULT | Replace EVG with fault; vacuum system test |
| F-037-003 | Manifold vacuum below VAC LO threshold | Caution | Log; EVG-2 start if EVG-1 on | Check EVG status; check for line leak |
| F-037-004 | EFV-1 stuck open (position feedback after de-energize = OPEN) | Caution | Log; alert crew/cabin | Inspect EFV-1; replace if stuck |
| F-037-005 | EFV-2 stuck open | Caution | Log; alert | Inspect EFV-2; replace if stuck |
| F-037-006 | EFV-3 stuck open | Caution | Log; alert | Inspect EFV-3; replace if stuck |
| F-037-007 | EFV-1 stuck closed (failed to open on command) | Advisory | Log | Inspect EFV-1 solenoid; check wiring |
| F-037-008 | EFV-2 stuck closed | Advisory | Log | Inspect EFV-2 solenoid |
| F-037-009 | EFV-3 stuck closed | Advisory | Log | Inspect EFV-3 solenoid |
| F-037-010 | Waste tank fill level > 75% (WASTE TANK HI) | Advisory | Log; ECAM display | Plan expedited ground service |
| F-037-011 | Waste tank fill level > 95% (WASTE TANK FULL) | Caution | CAS alert | Limit lavatory use; immediate ground service |
| F-037-012 | Manifold transducer out of range / failed | Advisory | Log; use secondary TBD | Replace manifold transducer |
| F-037-013 | Freeze temperature < threshold (TBD) | Advisory | Log; alert TBD | Check waste line freeze protection |
| F-037-014 | EVG-1 over-current | Caution | EVG-1 shutdown; EVG-2 auto-start | Inspect EVG-1 motor |
| F-037-015 | EVG-2 over-current | Caution | EVG-2 shutdown; CAS | Inspect EVG-2 motor |
| F-037-016 | SOV failed to open on command | Caution | Log; attempt retry | Inspect SOV solenoid; check wiring |
| F-037-017 | SOV failed to close on command | Caution | Log | Inspect SOV; check wiring |

> **Note:** Fault code list is <img src="https://img.shields.io/badge/TBD-red"> — this represents the planned concept. Final fault codes will be defined during CMC software design.

---

## §13 Maintenance Concept

### 13.1 Fault Isolation Using CMC

1. Access OMS maintenance terminal → ATA 37 → Fault Log
2. Note fault code(s) and timestamp(s)
3. Cross-reference fault code to AMM FI DM (info code 400)
4. Follow fault isolation procedure in AMM (see §14 for DM codes)
5. Execute directed maintenance action (component test, replacement)
6. Clear fault log (authorized access)
7. Run vacuum system functional test (037-070 ground test procedure)
8. Confirm fault resolved; close maintenance record

### 13.2 OMS Trend Monitoring

| Trend | Review Frequency | Threshold for Action |
|-------|-----------------|----------------------|
| EVG pull-down time trend | Every 50 flights TBD | Increasing by > TBD s |
| EVG run hours since last service | Continuous | > TBD h |
| Flush cycle count | Continuous | > TBD cycles (odour filter) |
| Fault event frequency | Weekly TBD | > TBD faults / 100 flights |

---

## §14 S1000D / CSDB Mapping

| DM Code | Info Code | Title | Status |
|---------|-----------|-------|--------|
| DMC-AMPEL360E-EWTW-037-80-00-00A-040A-A | 040 | Vacuum Monitoring and Diagnostics — Description | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-AMPEL360E-EWTW-037-80-00-00A-300A-A | 300 | CMC / OMS Monitoring Check | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-AMPEL360E-EWTW-037-80-00-00A-400A-A | 400 | Vacuum System Fault Isolation — EVG Fault | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-AMPEL360E-EWTW-037-80-00-00A-400B-A | 400 | Vacuum System Fault Isolation — EFV Fault | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-AMPEL360E-EWTW-037-80-00-00A-400C-A | 400 | Vacuum System Fault Isolation — Manifold Transducer Fault | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §15 Footprints

| Item | Value |
|------|-------|
| Data concentrator (LRU) | <img src="https://img.shields.io/badge/TBD-red"> dimensions, mass |
| Manifold transducer | <img src="https://img.shields.io/badge/TBD-red"> dimensions |
| EFV position sensor (each) | <img src="https://img.shields.io/badge/TBD-red"> dimensions |
| Freeze temp sensor (if installed) | <img src="https://img.shields.io/badge/TBD-red"> |
| AFDX bandwidth (ATA 37 monitoring) | <img src="https://img.shields.io/badge/TBD-red"> kbps |
| CMC storage (ATA 37 fault log) | <img src="https://img.shields.io/badge/TBD-red"> kB NVM |
| Wiring mass (monitoring) | <img src="https://img.shields.io/badge/TBD-red"> kg |

---

## §16 Safety and Certification

| Requirement | Reference | Compliance Method | Status |
|-------------|-----------|-------------------|--------|
| Equipment function and installation | CS-25.1301 | Inspection + test | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Safety assessment — monitoring failures | CS-25.1309 | FMEA: monitoring failure → undetected EVG fault | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Vacuum system integrity | CS-25.1438 | Monitoring as part of leak detection strategy | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| BITE completeness | CS-25.1309 | BITE coverage analysis | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Software (CMC fault logic) | DO-178C Level TBD | Software development assurance | <img src="https://img.shields.io/badge/TBD-red"> |
| Hardware (data concentrator) | DO-254 Level TBD | Hardware design assurance | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §17 Verification and Validation

| V&V ID | Activity | Method | Acceptance Criteria | Status |
|--------|----------|--------|---------------------|--------|
| VV-037-080-001 | BITE power-up test | Ground test | All BITE checks pass within TBD s | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| VV-037-080-002 | Fault injection — EVG-1 fault | Ground test (simulated) | CMC logs F-037-001; EVG-2 auto-starts | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| VV-037-080-003 | Fault injection — EFV stuck open | Ground test (simulated) | CMC logs F-037-004; CAS advisory | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| VV-037-080-004 | OMS trend data validation | Analysis + ground test | Pull-down time trend data logged correctly | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| VV-037-080-005 | Maintenance command authorization test | Ground test | Unauthorized commands rejected; audit trail logged | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| VV-037-080-006 | AFDX data integrity test | Integration test | All ATA 37 parameters received by CMC with correct values | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| VV-037-080-007 | Freeze protection sensor check | Ground test (cold environment TBD) | Advisory generated at correct temperature threshold | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §18 Glossary

| Term | Definition |
|------|-----------|
| ADIRU | Air Data Inertial Reference Unit — solid-state; no vacuum connection on eWTW |
| AFDX | Avionics Full-Duplex Switched Ethernet (ARINC 664 Part 7) — primary data bus |
| ATA 37 | Air Transport Association chapter for Vacuum systems |
| BITE | Built-In Test Equipment — automated self-test capability of the vacuum system |
| CMC | Central Maintenance Computer — collects, logs, and processes system health data |
| CS-25.1438 | EASA CS for vacuum/pneumatic plumbing integrity |
| DO-178C | Software Considerations in Airborne Systems and Equipment Certification |
| DO-254 | Design Assurance Guidance for Airborne Electronic Hardware |
| EFV | Electrically actuated Flush Valve |
| EVG | Electric Vacuum Generator — motor-driven vacuum pump |
| Fault code | Coded identifier for a specific fault condition logged in CMC NVM |
| Freeze protection | Thermal protection for waste lines (OI-037-005) |
| Gyroscopic instruments | Vacuum-driven AI, DI, TC — **eliminated on eWTW** (ADIRU) |
| Manifold | Vacuum distribution header |
| NRV | Non-Return Valve |
| NVM | Non-Volatile Memory — fault log and run-hour data storage |
| Odour filter | Activated carbon filter on manifold vent |
| OMS | On-board Maintenance System (ATA 45) |
| PTFE | Polytetrafluoroethylene — vacuum line material |
| SOV | Shutoff Valve — solenoid-operated; between EVG and manifold |
| Vacuum transducer | Piezoresistive pressure sensor measuring manifold vacuum |
| VRV | Vacuum Relief Valve — limits maximum system vacuum |
| VWS | Vacuum Waste System |
| Waste tank | ATA 38 scope waste collection vessel |

---

## §19 Citations

1. EASA CS-25 Amendment 27 (TBD), §25.1438 — Pressurisation and pneumatic systems
2. EASA CS-25 §25.1309 — Equipment, systems and installations
3. EASA CS-25 §25.1301 — Function and installation
4. DO-178C — Software Considerations in Airborne Systems
5. DO-254 — Design Assurance Guidance for Airborne Electronic Hardware
6. ARINC 664 Part 7 (AFDX) — Avionics Full-Duplex Switched Ethernet
7. ATA iSpec 2200 Chapter 37 — Vacuum
8. S1000D Issue 5.0

---

## §20 References

| Ref | Document | Link |
|-----|----------|------|
| R-080-001 | 037-000 Vacuum General | [037-000](./037-000-Vacuum-General.md) |
| R-080-002 | 037-010 Vacuum Sources (EVG) | [037-010](./037-010-Vacuum-Sources.md) |
| R-080-003 | 037-050 Consumers and Interfaces | [037-050](./037-050-Vacuum-Consumers-and-System-Interfaces.md) |
| R-080-004 | 037-060 Indication and Warning | [037-060](./037-060-Vacuum-System-Indication-and-Warning.md) |
| R-080-005 | 037-070 Ground Service and Test | [037-070](./037-070-Vacuum-Ground-Service-and-Test-Interfaces.md) |
| R-080-006 | ATA 45 OMS | Separate ATLAS node |
| R-080-007 | ATA 31 CMC | Separate ATLAS node |

---

## §21 Open Issues

| OI ID | Description | Owner | Priority | Status |
|-------|-------------|-------|----------|--------|
| OI-037-001 | EVG count and sizing — affects sensor count, BITE complexity, fault code list | Systems Eng | HIGH | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-037-002 | Dry-flush vs. vacuum toilet — if dry-flush, all ATA 37 monitoring eliminated | Chief Architect | CRITICAL | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-037-003 | Waste tank level sensor type (capacitive vs. float) — affects CMC interface | Structures | MEDIUM | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-037-004 | Vacuum line routing — affects sensor placement and freeze sensor location | Structures | HIGH | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-037-005 | **Freeze protection monitoring** — sensor location, alarm threshold, and pilot/ground alert strategy TBD | Systems Eng | MEDIUM | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-037-006 | Odour filter tracking — should CMC track flush cycles and alert for filter replacement? | Certification | MEDIUM | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-037-007 | Ground service panel location — does not affect monitoring architecture | Ground Ops | LOW | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §22 Change Log

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| 0.1.0 | 2025-07-14 | AI-assisted scaffold | Initial scaffold — §0–§22; monitored parameters table, BITE, fault codes, OMS trend concept; all thresholds and bus protocols TBD |

---
*Q+ATLANTIDE ATLAS — ATA 37 Vacuum — 037-080 Monitoring, Diagnostics, and Control Interfaces — AMPEL360e eWTW*
*Classification: UNCLASSIFIED — ENGINEERING SCAFFOLD*
