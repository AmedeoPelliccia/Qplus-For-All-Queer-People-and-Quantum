---
document_id: "QATL-ATLAS-1000-ATLAS-070-079-072-080"
register: ATLAS-1000
title: "Battery Charging and Ground Support"
ata: "072"
sns: "072-080-00"
subsection: "072"
subsubject_code: "080"
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
s1000d_dmc: "DMC-AMPEL360E-EWTW-0072-080"
---

# Battery Charging and Ground Support

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: 072](https://img.shields.io/badge/ATA-072-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-brightgreen)

---

## §0 Hyperlink Policy
All hyperlinks in this document are **relative**. Absolute URLs are forbidden.

## §1 Purpose
This document defines the ground charging architecture, procedures, and ground support equipment (GSE) requirements for the AMPEL360E eWTW battery system, covering DC fast charging, AC charging, regenerative energy acceptance, cell balancing, and turnaround time requirements.

## §2 Applicability
| Aircraft | Variant | MSN Range | Effectivity |
|---|---|---|---|
| AMPEL360E | eWTW | All | From EIS |

## §3 Functional Description ![DRAFT](https://img.shields.io/badge/-DRAFT-yellow)
The AMPEL360E supports two ground charging modes: DC fast charging via a dedicated Ground Support Equipment (GSE) DC charger, and AC charging via an on-board charger (OBC) connected to standard airport AC ground power. In both cases, charge power flows through the Battery Interface Unit (BIU) which performs voltage conversion and current regulation under BMS supervision.

**DC Fast Charging** uses a GSE-provided DC source at up to 800 V / 350 kW (per pack, 700 kW total aircraft), connected to the aircraft via a high-power DC connector on each wing root. The BMS negotiates charge parameters with the GSE via a CAN FD communication link (CCS2 / CHAdeMO-equivalent protocol adapted for aviation). Charge current is regulated to maintain cell temperature within the 10–35°C target range; above 35°C, charge current is derated. The BMS controls the charging contactors and terminates charge when target SoC (default 95%) or cell balance threshold is reached.

**AC Charging** uses standard 400 Hz or 50/60 Hz AC ground power (115/200V 3-phase) fed into the on-board charger which converts to DC at up to 100 kW total. This mode is used for overnight top-up or maintenance charging. The OBC includes active power factor correction (PFC) and galvanic isolation.

**Cell Balancing** is performed during the constant-voltage (CV) tail phase of charging, using passive balancing (resistive bleed) on the CSC to equalize cell voltages to within ±10 mV across the pack. Active balancing is reserved for a future upgrade path.

**Turnaround Time** target is ≤45 minutes to charge from minimum operational reserve (15% SoC) to 95% SoC at full DC fast charge power.

## §4 Functional Breakdown
| ID | Function | Description | Owner | DAL |
|---|---|---|---|---|
| F-072-080-01 | DC Fast Charging | Negotiate and control up to 350 kW DC per pack | Q-GREENTECH | DAL B |
| F-072-080-02 | AC Charging (OBC) | Convert AC ground power to controlled DC charge | Q-INDUSTRY | DAL C |
| F-072-080-03 | Charge Contactor Control | Manage charge path contactors under BMS supervision | Q-GREENTECH | DAL B |
| F-072-080-04 | Cell Balancing | Passive balance via CSC resistive bleed during CV phase | Q-HPC | DAL C |
| F-072-080-05 | Charge Termination | Terminate at target SoC, temperature limit or fault | Q-GREENTECH | DAL B |
| F-072-080-06 | GSE Communication | CAN FD charge negotiation protocol | Q-HPC | DAL C |

## §5 System Context
```mermaid
graph TD
    GSE_DC[DC Fast Charger GSE 350kW] -->|800V DC| DC_PORT[Wing Root DC Connector]
    DC_PORT -->|via BIU| BMS_CHG[BMS Charge Controller]
    AC_GND[AC Ground Power 115/200V] -->|3-phase| OBC[On-Board Charger 100kW]
    OBC -->|DC regulated| BMS_CHG
    BMS_CHG -->|charge current| PACK[Battery Packs]
    BMS_CHG <-->|CAN FD protocol| GSE_DC
    BMS_CHG -->|cell V/T| CSC_BAL[CSC Cell Balancing]
    BMS_CHG -->|status| ACMS[ACMS / Ground Station]
    BMS_CHG -->|charge state| MCDU[MCDU / Maintenance Panel]
```

## §6 Internal Architecture
```mermaid
graph LR
    subgraph CHARGE_PATH[Charge Path - One Pack]
        DC_CON[DC Connector] --> CHG_CONT[Charge Contactor]
        CHG_CONT --> BIU_CHG[BIU Charge Regulator]
        BIU_CHG --> PACK_CHG[Pack Charging Bus ~800V]
    end
    BMS_CC[BMS Charge Controller] --> CHG_CONT
    BMS_CC --> BIU_CHG
    CSC_B[CSC Balancing] -.->|passive bleed| PACK_CHG
    BMS_CC <-->|CAN FD| GSE_COMM[GSE Communication]
```

## §7 Components and LRUs
| LRU ID | Name | P/N | Qty | Location |
|---|---|---|---|---|
| LRU-072-080-01 | Wing Root DC Charge Connector | CONN-DC-800V-072 | 2 | Wing root (1 per bay) |
| LRU-072-080-02 | On-Board Charger (OBC) | OBC-AC-100KW-072 | 1 | Avionics/equipment bay |
| LRU-072-080-03 | Charge Path Contactor | CONT-CHG-800V | 2 | Pack charge path |
| LRU-072-080-04 | BIU Charge Regulator Module | BIU-CHG-350KW | 2 | Wing root |
| LRU-072-080-05 | CSC Balancing Resistor Array | BAL-RES-CSC-072 | 56 | One per module (within CSC) |

## §8 Interfaces
| Interface | Source | Destination | Protocol | Notes |
|---|---|---|---|---|
| IF-072-080-01 | GSE DC Charger | Wing Root DC Connector | 800V DC power | Up to 350 kW per bay |
| IF-072-080-02 | GSE DC Charger | BMS | CAN FD | Charge negotiation (current, voltage, SoC target) |
| IF-072-080-03 | OBC | BIU | DC regulated | AC-to-DC conversion |
| IF-072-080-04 | BMS | Charge Contactor | 28V discrete | Open/close control |
| IF-072-080-05 | BMS | BIU Charge Regulator | CAN FD | Current setpoint |
| IF-072-080-06 | BMS | ACMS | ARINC 429 | Charge status, SoC progress |
| IF-072-080-07 | BMS | MCDU | ARINC 429 | Charge status display |

## §9 Operating Modes
| Mode | Trigger | Description | Max Power | Notes |
|---|---|---|---|---|
| DC Fast Charge | GSE DC connected | BMS negotiates, BIU regulates | 350 kW/pack | CCS2-aviation protocol |
| AC Trickle Charge | AC ground connected | OBC converts, BMS controls | 100 kW total | Overnight / maintenance |
| Balancing (CV Phase) | End of CC phase | CSC passive bleed; ΔV ≤10 mV | <1 kW | End of charge |
| Charge Inhibit | Cell T <10°C or >35°C | Charge suspended; heater activated | 0 | Temperature limit |
| Charge Complete | Target SoC or balance | BMS opens charge contactor | 0 | GSE can disconnect |
| Fault Termination | OVP / OTP / comms loss | BMS terminates charge, logs fault | 0 | CAS alert |

## §10 Performance and Budgets ![DRAFT](https://img.shields.io/badge/-DRAFT-yellow)
| Parameter | Requirement | Current Estimate | Unit | Status |
|---|---|---|---|---|
| DC fast charge power (per pack) | ≥350 | 350 | kW | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Turnaround charge time (15→95% SoC) | ≤45 | 42 | min | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| AC charge power | ≥80 | 100 | kW | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Cell balancing accuracy | ±10 | ±10 | mV | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Charge efficiency (DC fast) | ≥95 | 96 | % | ![TBD](https://img.shields.io/badge/-TBD-orange) |

## §11 Safety, Redundancy and Fault Tolerance
- BMS terminates charging immediately on loss of GSE communication (timeout 5 s) to prevent uncontrolled charging.
- Charge path contactor is fail-safe open; loss of BMS power terminates charging.
- Temperature-based charge inhibit prevents lithium plating during low-temperature charging and cell damage during high-temperature charging.
- Ground fault monitoring on the AC charge path; GFCI in OBC trips on ground fault.
- Galvanic isolation in OBC prevents GSE ground faults from propagating into the aircraft HV system.

## §12 Maintenance and Diagnostics
| Task | Interval | Tool | Reference |
|---|---|---|---|
| DC connector inspection (contacts, seals) | A-Check | Visual; contact gauge | AMM 072-80-01 |
| OBC output voltage and current calibration | 2000 FH | DC calibration bench | CMM 072-80-02 |
| Charge contactor contact resistance | 1000 FH | DLRO | AMM 072-80-03 |
| Cell balance verification (post-charge ΔV log) | Per-flight (automatic ACMS) | ACMS ground station | AMM 072-80-04 |
| GSE communication protocol test | B-Check | GSE emulator + laptop | AMM 072-80-05 |

## §13 Footprint
| Metric | Value |
|---|---|
| DC charge connector | Wing root, 2× (one per pack) |
| DC charge protocol | CCS2-aviation adapted |
| Max DC charge power | 700 kW total (2 × 350 kW) |
| AC charge source | 115/200V 3-phase, 400 Hz or 50/60 Hz |
| Balancing method | Passive (CSC resistive bleed) |
| Turnaround target | 42 min (15→95% SoC) |

## §14 Safety and Certification References
| Standard | Requirement | Applicability | Status | Notes |
|---|---|---|---|---|
| CS-25 | Electrical — charging system | HV charge installation | Planned | CS-25.1353 |
| DO-178C | BMS charge control software DAL B | Charge logic | Planned | Included in BMS SW |
| IEC 61851 | EV conductive charging | DC charge connector / protocol | Planned | Aviation adaptation |
| ARP4754A | Safety analysis — charging | Charge function | Planned | FHA |
| CS-25 | AC power sources | OBC AC input | Planned | CS-25.1353 |

## §15 V&V Approach
| Phase | Method | Tool/Facility | Status |
|---|---|---|---|
| Charge power acceptance test | Full 350 kW charge; measure pack thermal and electrical | Battery integration rig | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Turnaround time test | 15→95% SoC under DC fast charge | Integration rig | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Balancing accuracy test | Measure ΔV across all cells at end of CV phase | GSE-BMS-DIAG-01 | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Charge fault termination | Inject OVP/comms loss; verify termination | HIL bench | ![TBD](https://img.shields.io/badge/-TBD-orange) |

## §16 Glossary
| Term | Definition |
|---|---|
| BIU | Battery Interface Unit |
| CC / CV | Constant Current / Constant Voltage — charge phases |
| CCS2 | Combined Charging System 2 — DC fast charge standard |
| GFCI | Ground Fault Circuit Interrupter |
| GSE | Ground Support Equipment |
| OBC | On-Board Charger |
| PFC | Power Factor Correction |

## §17 Open Issues
| ID | Description | Owner | Priority | Status |
|---|---|---|---|---|
| OI-072-080-001 | Define aviation DC charge connector standard with ATA/IATA working group | @copilot | High | Open |
| OI-072-080-002 | Validate 42-minute turnaround target against airport GSE power availability | @copilot | Medium | Open |

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
| 072-060 | Battery State Estimation | [072-060-Battery-State-Estimation.md](072-060-Battery-State-Estimation.md) |
| 072-090 | S1000D CSDB Mapping and Traceability | [072-090-S1000D-CSDB-Mapping-and-Traceability.md](072-090-S1000D-CSDB-Mapping-and-Traceability.md) |

## §20 Change Log
| Rev | Date | Author | Summary |
|---|---|---|---|
| 0.1 | 2026-05-12 | @copilot | Initial creation |
