---
document_id: "QATL-ATLAS-1000-ATLAS-070-079-072-070"
register: ATLAS-1000
title: "Battery Safety and Thermal Runaway Protection"
ata: "072"
sns: "072-070-00"
subsection: "072"
subsubject_code: "070"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HPC, Q-MECHANICS, Q-AIR, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0072-070"
standard_scope: agnostic
programme_specific: false
---

# Battery Safety and Thermal Runaway Protection

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: 072](https://img.shields.io/badge/ATA-072-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-brightgreen)

---

## §0 Hyperlink Policy
All hyperlinks in this document are **relative**. Absolute URLs are forbidden.

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Battery Safety and Thermal Runaway Protection`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 Applicability

| Applicability Level | Rule |
|---|---|
| Standard taxonomy | Applies to the ATLAS node `072` |
| Programme implementation | Conditional; determined by programme architecture, trade studies, certification basis, and applicability model |
| Product configuration | Defined in the programme-specific configuration baseline |
| Effectivity | Defined in the programme CSDB / applicability layer |
| Non-applicability | Must be explicitly stated in the programme impact-study branch when excluded |
## §3 Functional Description ![DRAFT](https://img.shields.io/badge/-DRAFT-yellow)
Thermal runaway (TR) is the primary catastrophic hazard for lithium-ion battery systems. The [PROGRAMME-AIRCRAFT] battery safety architecture applies a three-barrier defence-in-depth strategy: prevention, detection and suppression, and containment.

**Prevention** is achieved through the BMS protection functions (OVP, UVP, OCP, OTP) that maintain each cell within its safe operating area (SOA), and through the thermal management system that maintains cell temperature within the 20–30°C target range. Additionally, cell-to-cell mechanical compression and module-level containment housings rated to prevent single-cell TR propagation per IEC 62619 are applied.

**Detection** uses a multi-modal approach executed by the BMS within a 100 ms monitoring cycle: (1) abnormal cell temperature rate (dT/dt > 5°C/min on any single cell), (2) abnormal voltage drop on a single cell (ΔV > 200 mV from pack mean), and (3) optional electrolyte gas sensing (H₂/CO) via a gas sensor in each bay enclosure. Any two independent indicators trigger a TR event response; a single indicator triggers a TR precursor alert.

**Suppression** uses a dedicated Halon 1301 replacement agent (Novec 1230 or equivalent) stored in a compressed canister in each battery bay. Automatic discharge is triggered by the BMS on TR event detection. A manual discharge capability is provided at the fire panel on the flight deck. The suppression system is sized for a 30-second hold time in the battery bay volume.

**Containment** is provided by the module housing (aluminium with fire-resistant intumescent liner) and the bay enclosure (CFRP with fireproof sealing). Outgassing from any TR event is channelled through dedicated vent paths (see 072-020) to the wing lower surface outboard vent, away from the fuselage and engine intakes.

## §4 Functional Breakdown
| ID | Function | Description | Owner | DAL |
|---|---|---|---|---|
| F-072-070-01 | TR Prevention | BMS SOA enforcement (OVP, UVP, OCP, OTP) | Q-GREENTECH | DAL B |
| F-072-070-02 | TR Detection | Multi-modal dT/dt, ΔV and gas sensing; 100 ms | Q-HPC | DAL B |
| F-072-070-03 | TR Suppression Actuation | Auto / manual Novec 1230 discharge | Q-AIR | DAL A |
| F-072-070-04 | TR Propagation Containment | Module housing TR containment per IEC 62619 | Q-MECHANICS | DAL C |
| F-072-070-05 | Outgas Venting | Channel TR gases to outboard vent, away from fuselage | Q-MECHANICS | DAL C |
| F-072-070-06 | Crew Alerting and Procedures | CAS FIRE warning; QRH actions | Q-AIR | DAL A |

## §5 System Context
```mermaid
graph TD
    CELL_TR[Cell TR Event] -->|dT/dt ΔV gas| BMS_DET[BMS TR Detector DAL-B]
    BMS_DET -->|TR event| BMS_PROT[BMS Protection - open contactors]
    BMS_DET -->|suppression cmd| FIRE_CTRL[Fire Suppression Controller DAL-A]
    FIRE_CTRL -->|discharge| CANISTER[Novec 1230 Canister]
    CANISTER -->|agent| BAY[Battery Bay]
    BMS_DET -->|CAS signal| CAS[Crew Alerting - FIRE BAT L/R]
    BAY_VENT[Bay Vent Path] -->|outgas| OUTBOARD_VENT[Wing Outboard Vent]
    CREW[Crew Manual Discharge] -->|fire panel| FIRE_CTRL
```

## §6 Internal Architecture
```mermaid
graph LR
    subgraph DETECTION[TR Detection Logic - BMS]
        TEMP_RATE[dT/dt Monitor >5°C/min] --> OR2[2-of-3 Logic]
        VOLT_DROP[ΔV Monitor >200mV] --> OR2
        GAS_SENS[Gas Sensor H2/CO] --> OR2
        OR2 -->|TR event| PROTECTION[Open Contactors + Suppress]
        OR2 -->|single indicator| PRECURSOR[TR Precursor CAUTION]
    end
    subgraph SUPPRESSION[Suppression]
        FIRE_CTRL_S[Fire Controller DAL-A] --> CAN_L[Novec Canister Left]
        FIRE_CTRL_S --> CAN_R[Novec Canister Right]
    end
    PROTECTION --> FIRE_CTRL_S
```

## §7 Components and LRUs
| LRU ID | Name | P/N | Qty | Location |
|---|---|---|---|---|
| LRU-072-070-01 | Novec 1230 Suppression Canister | CANSTR-NOV1230-072 | 2 | Battery bay (1 per bay) |
| LRU-072-070-02 | Fire Suppression Controller | FSC-DAL-A-072 | 1 | Avionics bay |
| LRU-072-070-03 | Gas Sensor (H₂/CO) | GAS-SENS-H2CO-072 | 2 | Bay enclosure (1 per bay) |
| LRU-072-070-04 | Manual Discharge Switch | FIRE-SW-BAT-072 | 1 | Fire panel, flight deck |
| LRU-072-070-05 | Bay Vent Duct Assembly | VENT-DUCT-BAT-072 | 2 | Wing lower surface |

## §8 Interfaces
| Interface | Source | Destination | Protocol | Notes |
|---|---|---|---|---|
| IF-072-070-01 | BMS TR Detector | Fire Suppression Controller | 28V discrete | TR event command |
| IF-072-070-02 | Gas Sensor | BMS | 4–20 mA analogue | H₂/CO concentration |
| IF-072-070-03 | Fire Suppression Controller | Novec Canister | Squib / solenoid | Auto discharge |
| IF-072-070-04 | Manual Discharge Switch | Fire Suppression Controller | 28V discrete | Flight deck |
| IF-072-070-05 | BMS TR Detector | CAS | 28V discrete | FIRE BAT L/R warning |

## §9 Operating Modes
| Mode | Trigger | Description | Crew Action | Notes |
|---|---|---|---|---|
| Normal | All parameters in SOA | BMS monitoring, no alerts | None | Baseline |
| TR Precursor | Single indicator exceeded | CAS CAUTION BAT TEMP / BAT VOLT | Monitor; follow QRH | Inhibit max discharge |
| TR Event | 2-of-3 indicators | Auto contactor open + auto suppression | QRH BAT FIRE; manual discharge if needed | CAS FIRE BAT L/R |
| Post-Suppression | Discharge complete | Agent hold time 30 s; bay isolated | QRH continuation | Land ASAP |

## §10 Performance and Budgets ![DRAFT](https://img.shields.io/badge/-DRAFT-yellow)
| Parameter | Requirement | Current Estimate | Unit | Status |
|---|---|---|---|---|
| TR detection time (from onset) | ≤500 | 300 | ms | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Suppression agent hold time | ≥30 | 30 | s | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Cell-to-cell TR propagation | No propagation | Per IEC 62619 | — | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| dT/dt detection threshold | 5 | 5 | °C/min | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| ΔV detection threshold | 200 | 200 | mV | ![TBD](https://img.shields.io/badge/-TBD-orange) |

## §11 Safety, Redundancy and Fault Tolerance
- 2-of-3 detection logic reduces false positive rate while maintaining rapid response to genuine TR events.
- Fire Suppression Controller (FSC) is certified DAL A, independent of BMS; can be commanded by either flight crew manually if BMS auto-command fails.
- Module housing TR containment validated per IEC 62619 to prevent cell-to-cell propagation; limits event to single module.
- All bay materials (enclosure, wiring, insulation) are fire-resistant per CS-25.853 Class C minimum.
- Vent path designed and CFD-validated to prevent flammable gas accumulation inside aircraft fuselage or re-ingestion by engines.

## §12 Maintenance and Diagnostics
| Task | Interval | Tool | Reference |
|---|---|---|---|
| Gas sensor calibration | 1000 FH / Annual | Gas calibration kit | AMM [NODE]-[TASK] |
| Suppression canister pressure check | A-Check | Pressure gauge | AMM [NODE]-[TASK] |
| Suppression canister replacement | Per manufacturer life / on actuation | None (LRU swap) | AMM [NODE]-[TASK] |
| Fire panel switch functional test | A-Check | GSE-FIRE-TEST-072 | AMM [NODE]-[TASK] |
| Bay vent path inspection | C-Check | Visual / borescope | AMM [NODE]-[TASK] |
| LOTO procedure training | Per personnel certification | — | OMM 072-70-06 |

## §13 Footprint
| Metric | Value |
|---|---|
| Suppression agent | Novec 1230 (or equivalent Halon 1301 replacement) |
| Canister quantity | 1 per bay (2 total) |
| Hold time | 30 s |
| Gas sensors | H₂ and CO (1 dual-gas unit per bay) |
| Detection threshold dT/dt | 5°C/min |
| Detection threshold ΔV | 200 mV |

## §14 Safety and Certification References
| Standard | Requirement | Applicability | Status | Notes |
|---|---|---|---|---|
| CS-25 | Fire protection — battery | Bay fire suppression | Planned | CS-25.863 |
| CS-25 | Flammability — materials | Bay structure and wiring | Planned | CS-25.853 |
| IEC 62619 | LIB safety — TR propagation | Module TR containment | Planned | Cell/module level |
| ARP5765 | LIB installation guidance | Battery bay design | Planned | Guidance material |
| DO-178C | FSC software — DAL A | Fire suppression logic | Planned | Highest criticality |
| ARP4761 | Safety assessment | TR event FTA/FMEA | Planned | Catastrophic hazard |

## §15 V&V Approach
| Phase | Method | Tool/Facility | Status |
|---|---|---|---|
| Cell-level TR abuse test | Nail penetration, overcharge per IEC 62619 | Abuse test chamber | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Module TR propagation test | Single-cell TR induced; observe propagation | Battery abuse chamber | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Detection latency test | Inject TR signature, measure BMS response time | HIL bench | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Suppression system actuation test | Full system discharge, measure hold time | Bay mock-up | ![TBD](https://img.shields.io/badge/-TBD-orange) |

## §16 Glossary
| Term | Definition |
|---|---|
| CAS | Crew Alerting System |
| CFRP | Carbon Fibre Reinforced Polymer |
| FSC | Fire Suppression Controller |
| LOTO | Lock-Out / Tag-Out |
| QRH | Quick Reference Handbook |
| SOA | Safe Operating Area |
| TR | Thermal Runaway |
| dT/dt | Rate of temperature change — primary TR detection metric |

## §17 Open Issues
| ID | Description | Owner | Priority | Status |
|---|---|---|---|---|
| OI-072-070-001 | Confirm Novec 1230 supply chain availability; evaluate alternatives | @copilot | High | Open |
| OI-072-070-002 | Complete CFD analysis of vent path to verify no gas re-ingestion | @copilot | High | Open |

## §18 Status Legend
| Badge | Meaning |
|---|---|
| ![DRAFT](https://img.shields.io/badge/-DRAFT-yellow) | Content under active development |
| ![TBD](https://img.shields.io/badge/-TBD-orange) | Value or content to be determined |
| ![ACTIVE](https://img.shields.io/badge/-ACTIVE-brightgreen) | Approved and baselined |
| ![RESERVED](https://img.shields.io/badge/-RESERVED-lightgrey) | Placeholder |

## §19 Related Documents
| Code | Title | Link |
|---|---|---|
| 072-000 | Battery Energy Storage — General | [072-000-Battery-Energy-Storage-General.md](072-000-Battery-Energy-Storage-General.md) |
| 072-030 | Battery Management System (BMS) | [072-030-Battery-Management-System-BMS.md](072-030-Battery-Management-System-BMS.md) |
| 072-040 | Battery Thermal Management | [072-040-Battery-Thermal-Management.md](072-040-Battery-Thermal-Management.md) |
| 072-050 | HV Contactors and Protection | [072-050-HV-Contactors-and-Protection.md](072-050-HV-Contactors-and-Protection.md) |
| 072-080 | Battery Charging and Ground Support | [072-080-Battery-Charging-and-Ground-Support.md](072-080-Battery-Charging-and-Ground-Support.md) |
| 072-090 | S1000D CSDB Mapping and Traceability | [072-090-S1000D-CSDB-Mapping-and-Traceability.md](072-090-S1000D-CSDB-Mapping-and-Traceability.md) |

## §20 Change Log
| Rev | Date | Author | Summary |
|---|---|---|---|
| 0.1 | 2026-05-12 | @copilot | Initial creation |
