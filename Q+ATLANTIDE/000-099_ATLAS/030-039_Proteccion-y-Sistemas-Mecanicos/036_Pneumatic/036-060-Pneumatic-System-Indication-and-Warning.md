---
document_id: "QATL-ATLAS-000099-ATLAS-030039-036-060"
title: "036-060 — Pneumatic System Indication and Warning"
short_title: "ATA 36 Indication and Warning"
subsubject: "060"
subsubject_title: "Pneumatic System Indication and Warning"
file_name: "036-060-Pneumatic-System-Indication-and-Warning.md"
sns_reference: "036-60"
dmc_prefix: "DMC-<PROGRAMME>-<VARIANT>-036-60"
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
  - "[PROGRAMME-AIRCRAFT]"
  - "S1000D"
  - "ATA 36"
  - "Pneumatic"
  - "indication"
  - "warning"
  - "CAS"
  - "ECAM"
  - "PNEU EAC FAULT"
  - "PNEU LO PR"
  - "bleed-less"
  - "AFDX"
  - "CS-25.1438"
standard_scope: agnostic
programme_specific: false
---

# 036-060 — Pneumatic System Indication and Warning
### [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT] · ATA 36 · Q+ATLANTIDE ATLAS Scaffold

---

## §0 Hyperlink Policy

All internal links in this document use relative paths from the current directory. External regulatory and standards references use anchor links defined in [§20 References](#20-references). Links marked **TBD** indicate targets not yet allocated within the CSDB or ATLAS hierarchy. Programme-level links traverse five directory levels (`../../../../../`) to reach the repository root. No absolute URLs are used for internal navigation.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `036-060 — Pneumatic System Indication and Warning`.

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

### 3.1 [PROGRAMME-VARIANT] Pneumatic Indication Architecture

The ATA 36 indication and warning system for the [PROGRAMME-VARIANT] provides:

1. **Crew Alerting System (CAS) alerts** — two primary alerts via ECAM CAS window:
   - `PNEU EAC FAULT` (amber) — EAC motor fault, controller fault, or overcurrent
   - `PNEU LO PR` (amber) — manifold pressure below P_low threshold (leak or EAC failure)

2. **ECAM Pneumatic System Page** (TBD — if dedicated page created):
   - EAC status (ON / OFF / FAULT) — text annunciation
   - Manifold pressure — analogue or digital readout (psi)
   - SOV status (Door Seal / Water Tank) — OPEN / CLOSED
   - System schematic (simplified) showing EAC → manifold → consumers

3. **Maintenance terminal** (ATA 45):
   - Full EAC parameters: outlet pressure, motor current, temperature, run hours
   - SOV position (each)
   - CMC fault log for ATA 36
   - Ground test mode activation

### 3.2 Indications NOT Present on [PROGRAMME-VARIANT] (vs. Conventional)

| Indication | Conventional Aircraft | [PROGRAMME-VARIANT] |
|---|---|---|
| ENG 1 BLEED ON/OFF | Yes (both engines) | **None** — no bleed |
| CROSS BLEED OPEN/CLOSED | Yes | **None** — no cross-bleed |
| Bleed valve position (each) | Yes | **None** — no bleed valve |
| Pre-cooler outlet temperature | Yes | **None** — no pre-cooler |
| BLEED OVHT alert | Yes (amber/red) | **None** — no OHT (bleed-less) |
| BLEED LEAK alert | Yes | **None** — replaced by PNEU LO PR |
| HP/LP selection indication | Yes (some types) | **None** |
| Pack valve status (from bleed) | Yes (ATA 21 bleed valve indication) | **None** — EDC sourced |
| APU BLEED indication | Yes | **None** — no APU |

---

## §4 Scope

### 4.1 Included
- CAS alert: "PNEU EAC FAULT" (amber) — definition, trigger logic, display, reset condition
- CAS alert: "PNEU LO PR" (amber) — definition, trigger logic, display, reset condition
- ECAM Pneumatic System Page content specification (if page created — TBD)
- ECAM page: EAC ON/OFF/FAULT, manifold pressure readout, SOV status display
- ECAM page simplified schematic: EAC → filter → regulator → manifold → consumers
- AFDX data interface from ATA 36 sensors/CMC to ECAM (ATA 31)
- Overhead or central pedestal panel provisions for EAC ON/OFF switch (TBD — if manual switch fitted)
- Maintenance terminal readout for ATA 36 parameters and fault log

### 4.2 Excluded
- Bleed valve indications (not applicable)
- Cross-bleed valve indications (not applicable)
- Bleed OVHT alerts (not applicable)
- ATA 26 fire/smoke alerts (separate — ATA 26 scope)
- ECS/Pressurisation ECAM page (ATA 21 — separate)
- Wing anti-ice ECAM page (ATA 30 — separate; no ATA 36 supply)

---

## §5 Architecture Description

### 5.1 CAS Alert Definitions

| Alert Text | Colour | Priority | Trigger Condition | Reset Condition |
|---|---|---|---|---|
| PNEU EAC FAULT | Amber | Caution | EAC motor controller fault signal active | EAC fault cleared + CMC reset |
| PNEU LO PR | Amber | Caution | Manifold pressure < P_low (TBD psi) for T_detect (TBD s) | Manifold pressure returns to ≥ P_low + hysteresis |

### 5.2 ECAM Pneumatic Page Content (TBD — Provisional)

```
PNEUMATIC                               [ATA 36]
─────────────────────────────────────────────────
  EAC        [ON  / OFF / FAULT]
  MANIFOLD   [XX.X psi]
  SOV DS     [OPEN / CLSD]
  SOV WT     [OPEN / CLSD]

  ┌──────────────────────────────────────────┐
  │  [EAC]──[F]──[REG]──[ACC]──[MFD]        │
  │                           │              │
  │                      [SOV DS]─ Door Seals│
  │                      [SOV WT]─ Water Tank│
  └──────────────────────────────────────────┘
NOTE: This [PROGRAMME-VARIANT] has no engine bleed air.
      ATA 36 = residual low-pressure circuit only.
─────────────────────────────────────────────────
```
*(Schematic above is indicative only — final display format TBD per ATA 31 ECAM design standard)*

### 5.3 AFDX Data Interface

| Data Item | Source | Bus | Destination | Refresh Rate |
|---|---|---|---|---|
| EAC ON/OFF status | EAC motor controller | AFDX | CMC → ECAM | <img src="https://img.shields.io/badge/TBD-red"> Hz |
| EAC FAULT flag | EAC motor controller | AFDX | CMC → ECAM | <img src="https://img.shields.io/badge/TBD-red"> Hz |
| Manifold pressure (primary) | Pressure transducer | AFDX | CMC → ECAM | <img src="https://img.shields.io/badge/TBD-red"> Hz |
| SOV-DS position | SOV micro-switch | AFDX | CMC → ECAM | <img src="https://img.shields.io/badge/TBD-red"> Hz |
| SOV-WT position | SOV micro-switch | AFDX | CMC → ECAM | <img src="https://img.shields.io/badge/TBD-red"> Hz |
| PNEU EAC FAULT CAS | CMC logic | AFDX | CMC → CAS | Event-driven |
| PNEU LO PR CAS | CMC logic | AFDX | CMC → CAS | Event-driven |

### 5.4 Cockpit Panel Provisions

| Item | Location | Type | Status |
|---|---|---|---|
| EAC ON/OFF switch | Overhead panel (TBD) or pedestal | Latching toggle / guarded switch (TBD) | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC FAULT light | Integrated with switch (TBD) or ECAM only | Amber LED / ECAM only (TBD) | <img src="https://img.shields.io/badge/TBD-red"> |
| Pneumatic ECAM page access | ECAM keypad / touch (ATA 31) | Software page selection | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §6 Functional Breakdown

| Function | Component | Interface | Status |
|---|---|---|---|
| PNEU EAC FAULT alert generation | CMC ATA 36 logic | ATA 36-010 EAC → CMC → ECAM CAS | <img src="https://img.shields.io/badge/TBD-red"> |
| PNEU LO PR alert generation | CMC pressure logic | ATA 36-020 transducers → CMC → ECAM CAS | <img src="https://img.shields.io/badge/TBD-red"> |
| ECAM Pneumatic Page display | ECAM display system (ATA 31) | AFDX from CMC | <img src="https://img.shields.io/badge/TBD-red"> |
| Manifold pressure readout | ECAM display | CMC → AFDX → ECAM | <img src="https://img.shields.io/badge/TBD-red"> |
| SOV position display | ECAM display | CMC → AFDX → ECAM | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC status display | ECAM display | CMC → AFDX → ECAM | <img src="https://img.shields.io/badge/TBD-red"> |
| Maintenance terminal readout | ATA 45 terminal | CMC data | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §7 System Context Diagram

```mermaid
flowchart LR
    subgraph SENSORS["ATA 36 Sensors"]
        EAC_STAT["EAC Status\n(motor controller)"]
        PT_MFD["Manifold Pressure\nTransducer(s)"]
        SOV_FB["SOV Position\nFeedback"]
    end
    subgraph CMC["CMC / OMS (ATA 45)"]
        CMC_LOGIC["CMC ATA 36\nFault Logic"]
        FAULT_LOG["Fault Log\n(maintenance data)"]
    end
    subgraph ECAM_SYS["ECAM / CAS (ATA 31)"]
        CAS_WIN["CAS Window\nPNEU EAC FAULT\nPNEU LO PR"]
        PNEU_PAGE["Pneumatic\nSystem Page\n(TBD)"]
    end
    subgraph MAINT["Maintenance Terminal"]
        MAINT_TERM["ATA 45 Terminal\nFull parameter readout\nFault log"]
    end
    subgraph CREW["Crew Interface"]
        COCKPIT["Cockpit Panel\nEAC ON/OFF switch\n(TBD)"]
    end
    subgraph NONE["Not Present on [PROGRAMME-VARIANT]"]
        BLEED_IND["Bleed Valve Ind.\n(N/A)"]
        XBLEED["Cross-Bleed Ind.\n(N/A)"]
        OVHT["BLEED OVHT\n(N/A)"]
    end

    EAC_STAT --> CMC_LOGIC
    PT_MFD --> CMC_LOGIC
    SOV_FB --> CMC_LOGIC
    CMC_LOGIC --> CAS_WIN
    CMC_LOGIC --> PNEU_PAGE
    CMC_LOGIC --> FAULT_LOG
    FAULT_LOG --> MAINT_TERM
    COCKPIT --> CMC_LOGIC

    style NONE fill:#ffebee,stroke:#f44336
    style ECAM_SYS fill:#fff3e0,stroke:#FF9800
    style CMC fill:#f3e5f5,stroke:#9C27B0
    style SENSORS fill:#e8f4fd,stroke:#2196F3
```

---

## §8 Internal Functional Architecture

```mermaid
flowchart TB
    A["ATA 36 Sensor Data\n(EAC, pressure, SOV)"]
    B["CMC ATA 36 Logic\n(fault assessment)"]
    C{"EAC Fault?"}
    D{"P_manifold\n< P_low?"}
    E["CAS: PNEU EAC FAULT\n(amber)"]
    F["CAS: PNEU LO PR\n(amber)"]
    G["ECAM Pneumatic Page\nUpdated (EAC, pressure, SOV)"]
    H["No Alert\n(status normal)"]
    I["Fault Log\n(CMC record)"]
    J["Maintenance Terminal\nAlert readable"]
    K["Crew Acknowledges\nAlert"]
    L["Crew Takes Action\nper QRH TBD"]

    A --> B
    B --> C
    B --> D
    C -- Yes --> E --> K --> L
    D -- Yes --> F --> K --> L
    C -- No --> H
    D -- No --> H
    B --> G
    E --> I --> J
    F --> I
```

---

## §9 Lifecycle Traceability

```mermaid
flowchart LR
    LC02["LC02\nIndication\nRequirements"] --> LC03
    LC03["LC03\nCAS / ECAM\nPage Design"] --> LC05
    LC05["LC05\nAFDX ICD\nand CMC Logic"] --> LC06
    LC06["LC06\nAlert Logic\nTest Plan"] --> LC10
    LC10["LC10\nCS-25.1321\n/ CS-25.1309"] --> LC11
    LC11["LC11\nCrew Training\nQRH entries"] --> LC12
    LC12["LC12\nMaintenance\nTerminal readout"]
```

---

## §10 Interfaces

| Interface | ATA Chapter | Description | Direction |
|---|---|---|---|
| EAC motor controller | ATA 36-010 | EAC ON/OFF, FAULT status to CMC | ATA 36-010 → ATA 36-060 |
| Manifold pressure transducers | ATA 36-020 | Pressure data to CMC | ATA 36-020 → ATA 36-060 |
| SOV position feedback | ATA 36-030/040 | SOV open/closed status to CMC | ATA 36-030 → ATA 36-060 |
| CMC / OMS | ATA 45 | Fault logic, data consolidation, AFDX output | ATA 36-060 ↔ ATA 45 |
| ECAM display system | ATA 31 | CAS alerts and system page display | ATA 36-060 → ATA 31 |
| Cockpit panel | ATA 31 | EAC ON/OFF switch (TBD) | Crew → ATA 36-060 |
| Maintenance terminal | ATA 45 | Full parameter readout and fault log | ATA 36-060 → ATA 45 |
| AFDX bus | ATA 42 | Data transport from CMC to ECAM | ATA 36-060 → ATA 42 |

---

## §11 Operating Modes

| Mode | CAS Active | ECAM Page | Maint Terminal |
|---|---|---|---|
| Normal — EAC running, no fault | None | Normal (all green) | Live data |
| EAC FAULT | PNEU EAC FAULT (amber) | EAC shows FAULT | Fault code + run hours |
| PNEU LO PR | PNEU LO PR (amber) | Pressure readout in amber | Pressure data + fault flag |
| Both alerts | Both amber alerts | EAC FAULT + pressure amber | Both fault codes |
| Maintenance mode | None (ground — EAC test) | N/A | Active test readout |
| Circuit depressurised / EAC OFF | None (if commanded OFF) | EAC shows OFF | OFF status |

---

## §12 Monitoring and Diagnostics

| Alert | Trigger | Inhibit Conditions | Cockpit Effect |
|---|---|---|---|
| PNEU EAC FAULT | EAC fault signal from motor controller | Ground test mode (TBD) | Amber CAS, ECAM pneumatic page |
| PNEU LO PR | Manifold P < P_low for T_detect | EAC intentionally OFF (no demand) | Amber CAS, pressure amber on ECAM page |
| SOV disagree (TBD) | SOV command ≠ feedback for >TBD s | Transition time (TBD) | CMC fault log only (no crew alert TBD) |

---

## §13 Maintenance Concept

### 13.1 Maintenance Terminal Readout
Via ATA 45 maintenance terminal:
- EAC status: ON / OFF / FAULT
- EAC motor current (A): <img src="https://img.shields.io/badge/TBD-red">
- EAC motor temperature (°C): <img src="https://img.shields.io/badge/TBD-red">
- EAC run hours: <img src="https://img.shields.io/badge/TBD-red">
- Manifold pressure (primary + redundant) (psi): live
- SOV-DS position: OPEN / CLSD
- SOV-WT position: OPEN / CLSD
- Fault log: up to TBD entries (PNEU EAC FAULT, PNEU LO PR with timestamp)
- Ground test mode: activate EAC and SOVs for maintenance test

### 13.2 CAS Alert Response (QRH — TBD)
- "PNEU EAC FAULT": check EAC switch ON; if fault persists → maintenance action post-flight (EAC fault isolation per S1000D DM 036-10-400)
- "PNEU LO PR": check EAC running; if pressure low with EAC ON → possible leak; monitor; maintenance action post-flight (leak test per S1000D DM 036-70 procedure)

---

## §14 S1000D / CSDB Mapping

| DM Code (planned) | Info Code | Title | Status |
|---|---|---|---|
| DMC-<PROGRAMME>-<VARIANT>-036-60-00A-040A-A | 040 | ATA 36-060 — Pneumatic Indication and Warning — Description | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| DMC-<PROGRAMME>-<VARIANT>-036-60-00A-300A-A | 300 | ATA 36-060 — CAS Alert Functional Test | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<PROGRAMME>-<VARIANT>-036-60-00A-400A-A | 400 | ATA 36-060 — ECAM Indication Fault Isolation | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §15 Footprints

| Item | Notes | Status |
|---|---|---|
| ECAM Pneumatic Page | Software — no additional hardware | <img src="https://img.shields.io/badge/TBD-red"> |
| CAS alerts (2) | Software entries in CAS database | <img src="https://img.shields.io/badge/TBD-red"> |
| EAC ON/OFF switch (TBD) | If fitted: small panel switch; mass negligible | <img src="https://img.shields.io/badge/TBD-red"> |
| AFDX ICD entries | Software / data — no hardware | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §16 Safety and Certification

| Requirement | Standard | Applicability | Notes |
|---|---|---|---|
| Pneumatic systems indication | CS-25.1438 | Full | Alert coverage for ATA 36 |
| Flight crew alerting | CS-25.1309 + AMC | Full | Alert priority, colour, logic per CS-25.1322 |
| Display arrangement | CS-25.1321 | Full | ECAM page layout and readability |
| Systems and installations | CS-25.1309 | Full | Alert logic failure modes |
| No bleed indications | N/A | Confirmed | [PROGRAMME-VARIANT] ECAM does not include bleed valve or OHT indications |

---

## §17 Verification and Validation

| V&V Activity | Method | Acceptance Criteria | Status |
|---|---|---|---|
| PNEU EAC FAULT alert functional test | Induce EAC fault; verify CAS alert and ECAM page | Alert within TBD s; correct colour/priority | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| PNEU LO PR alert functional test | Reduce manifold pressure below P_low; verify alert | Alert within T_detect + TBD s | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Alert reset test | Clear fault; verify alert clears | Alert clears within TBD s | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| ECAM page readability | Cockpit evaluation | All parameters readable in ambient and low-light | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Manifold pressure indication accuracy | Compare ECAM readout to reference gauge | ± TBD psi | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Maintenance terminal readout functional | CMC terminal test with EAC running | All parameters displayed correctly | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| CMC fault log verification | Generate fault; verify log entry with timestamp | Log entry correct within TBD s | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| CS-25.1322 alert priority compliance | Analysis | Alert colour/priority per CS-25.1322 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §18 Glossary

| Term | Definition |
|---|---|
| CAS | Crew Alerting System — cockpit alert presentation system |
| ECAM | Electronic Centralised Aircraft Monitor — multi-function display for system status and alerts |
| PNEU EAC FAULT | Amber CAS alert indicating EAC motor/controller fault |
| PNEU LO PR | Amber CAS alert indicating manifold pressure below threshold |
| AFDX | Avionics Full-Duplex Switched Ethernet — aircraft data bus connecting CMC to ECAM |
| CMC | Central Maintenance Computer — processes ATA 36 sensor data and generates alerts |
| EAC | Electric Air Compressor — on-board pneumatic source (ATA 36-010) |
| SOV | Shutoff Valve — consumer branch isolation valve |
| Bleed-less architecture | No engine bleed air; eliminates most conventional pneumatic indications |
| ICD | Interface Control Document — defines AFDX data items between ATA 36 and ATA 31/42 |
| QRH | Quick Reference Handbook — crew procedure for CAS alert response |
| CS-25.1321 | EASA — Arrangement and visibility of instruments |
| CS-25.1322 | EASA — Flight crew alerting — alert categories and colours |
| CS-25.1438 | EASA — Pneumatic systems certification requirement |
| DO-160G | RTCA environmental qualification standard |
| P_low | Lower pressure threshold for PNEU LO PR alert (TBD psi) |

---

## §19 Citations

1. EASA CS-25 §25.1438 — Pneumatic Systems
2. EASA CS-25 §25.1309 — Systems and Installations
3. EASA CS-25 §25.1321 — Arrangement and Visibility of Instruments
4. EASA CS-25 §25.1322 — Flight Crew Alerting
5. RTCA DO-160G — Environmental Conditions and Test Procedures
6. S1000D Issue 5.0
7. ATA iSpec 2200 — ATA 36 Pneumatic / ATA 31 Indicating Systems

---

## §20 References

| Ref ID | Document | Source | Link |
|---|---|---|---|
| [ATA36] | ATA iSpec 2200 Chapter 36 | ATA | — |
| [ATA31] | ATA iSpec 2200 Chapter 31 — Instruments | ATA | — |
| [CS25-1438] | CS-25 §25.1438 | EASA | https://www.easa.europa.eu/ |
| [CS25-1322] | CS-25 §25.1322 | EASA | https://www.easa.europa.eu/ |
| [CS25-1321] | CS-25 §25.1321 | EASA | https://www.easa.europa.eu/ |
| [DO-160G] | RTCA DO-160G | RTCA | https://www.rtca.org/ |
| [S1000D] | S1000D Issue 5.0 | ASD/AIA | https://s1000d.org/ |
| [036-000] | ATA 36 General | Internal | [036-000](./036-000-Pneumatic-General.md) |
| [036-050] | ATA 36 Leak Detection | Internal | [036-050](./036-050-Leak-Detection-and-Overheat-Protection.md) |
| [036-080] | ATA 36 Monitoring / Diagnostics | Internal | [036-080](./036-080-Pneumatic-Monitoring-Diagnostics-and-Control-Interfaces.md) |

---

## §21 Open Issues

| Issue ID | Description | Owner | Priority | Status |
|---|---|---|---|---|
| OI-036-001 | **Retain or eliminate ATA 36**: if eliminated, ECAM page and CAS alerts not required | Q-AIR | Critical | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-025 | **Dedicated ECAM page**: whether ATA 36 warrants a dedicated ECAM page or is integrated into a "utilities" page — depends on system scope | Q-AIR / ATA 31 | Medium | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-026 | **EAC ON/OFF switch location**: overhead panel vs. ECAM touchscreen control vs. software-only (auto) — crew workload and philosophy | Q-AIR / human factors | Medium | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-027 | **CAS alert text finalisation**: "PNEU EAC FAULT" and "PNEU LO PR" text to be approved by human factors / authority | Q-AIR / ORB-LEG | Medium | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-028 | **SOV disagree alert**: whether to surface SOV position disagree to crew or maintenance-only — alert philosophy TBD | Q-AIR | Low | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-036-029 | **AFDX ICD**: ATA 36 → ATA 31/42 interface control document — not yet authored | Q-DATAGOV | High | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §22 Change Log

| Revision | Date | Author | Description |
|---|---|---|---|
| 0.1.0 | 2026-05-10 | Q+ATLANTIDE scaffold generator | Initial full-template scaffold — all sections present; minimal [PROGRAMME-VARIANT] indication set documented |
