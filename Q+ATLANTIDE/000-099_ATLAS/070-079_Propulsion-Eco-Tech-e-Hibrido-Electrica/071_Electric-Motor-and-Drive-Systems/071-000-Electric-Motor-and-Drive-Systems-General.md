---
document_id: "QATL-ATLAS-1000-ATLAS-070-079-071-000"
register: ATLAS-1000
title: "Electric Motor and Drive Systems — General Overview"
ata: "071"
sns: "071-000-00"
subsection: "071"
subsubject_code: "000"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HPC, Q-MECHANICS, Q-AIR, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-11"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0071-000"
---

# Electric Motor and Drive Systems — General Overview

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: 071](https://img.shields.io/badge/ATA-071-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-brightgreen)

---

## §0 Hyperlink Policy
All hyperlinks in this document are **relative**. Absolute URLs are forbidden.

## §1 Purpose
This document provides the general system-level overview of the Electric Motor and Drive Systems (subsection 071) for the AMPEL360E eWTW aircraft. It describes the dual aft-fuselage Permanent Magnet Synchronous Motor (PMSM) architecture, power distribution topology, and the integration of Boundary Layer Ingestion (BLI) propulsion. It serves as the top-level reference that frames all subordinate 071-NNN data modules.

## §2 Applicability
| Aircraft | Variant | MSN Range | Effectivity |
|---|---|---|---|
| AMPEL360E | eWTW | All | From EIS |

## §3 Functional Description ![DRAFT](https://img.shields.io/badge/-DRAFT-yellow)
The AMPEL360E eWTW features two aft-fuselage PMSM propulsion motors rated at 2 MW peak each, fed directly from the aircraft High-Voltage Direct Current (HVDC) 540 V bus. Each motor is mechanically coupled to a ducted fan propulsor positioned at the aft fuselage boundary layer ingestion (BLI) aperture, exploiting wake-filling to reduce overall aircraft drag and improve propulsive efficiency by approximately 8–12 % relative to a podded equivalent.

Power flows from the HVDC main bus through independent Motor Drive Units (MDU), which employ Silicon Carbide (SiC) MOSFET three-phase voltage-source inverters to convert DC power into precisely controlled AC at variable frequency and amplitude. Each Motor Control Unit (MCU) implements Field-Oriented Control (FOC) with Maximum Torque Per Ampere (MTPA) optimisation, receiving thrust demand signals from the Full Authority Digital Engine Control (FADEC) system over an ARINC 429 / AFDX interface.

The subsystem family covered by ATA 071 encompasses motor electromagnetic design (071-010), the MDU/inverter hardware (071-020), the MCU control software and control laws (071-030), BLI aerodynamic integration (071-040), thermal management (071-050), health monitoring and diagnostics (071-060), mechanical interfaces and transmission (071-070), electrical interfaces and power quality (071-080), and S1000D data management traceability (071-090). This document establishes the overarching system architecture and interfaces that govern all those sub-topics.

## §4 Functional Breakdown
| ID | Function | Description | Owner | DAL |
|---|---|---|---|---|
| F-071-000-01 | System Power Conversion | Convert HVDC 540 V bus power to mechanical shaft power via MDU and PMSM | Q-GREENTECH | DAL-B |
| F-071-000-02 | Motor Speed/Torque Control | Receive FADEC thrust demand and regulate PMSM speed and torque via MCU/FOC | Q-GREENTECH | DAL-B |
| F-071-000-03 | BLI Thrust Generation | Generate net propulsive thrust through aft-fuselage BLI ducted fan integration | Q-AIR | DAL-C |
| F-071-000-04 | Thermal Management | Monitor and control motor and MDU thermal state within safe operating limits | Q-MECHANICS | DAL-C |
| F-071-000-05 | Health Monitoring | Continuously assess motor system health and provide ECAM/CMS alerts | Q-HPC | DAL-C |

## §5 System Context
```mermaid
graph TD
    HVDC["HVDC Bus 540V"] --> MDU_P["MDU — Port"]
    HVDC --> MDU_S["MDU — Stbd"]
    MDU_P --> PMSM_P["PMSM — Port"]
    MDU_S --> PMSM_S["PMSM — Stbd"]
    PMSM_P --> FAN_P["BLI Fan — Port"]
    PMSM_S --> FAN_S["BLI Fan — Stbd"]
    FADEC["FADEC"] -->|Thrust Demand ARINC 429| MCU["MCU-071"]
    MCU -->|Gate Cmds| MDU_P
    MCU -->|Gate Cmds| MDU_S
    MHM["Motor Health Monitor"] -->|Alerts| CMS["CMS / ECAM"]
    PMSM_P -->|Sensors| MHM
    PMSM_S -->|Sensors| MHM
    TMS["Thermal Mgmt System"] --> PMSM_P
    TMS --> PMSM_S
    TMS --> MDU_P
    TMS --> MDU_S
```

## §6 Internal Architecture
```mermaid
graph TD
    subgraph MDU["Motor Drive Unit (071-020)"]
        INV["SiC Inverter"]
        DCL["DC Link Cap"]
    end
    subgraph MCU_BLK["Motor Control Unit (071-030)"]
        FOC["FOC / MTPA"]
        SVPWM["SVPWM Generator"]
    end
    subgraph PMSM_BLK["PMSM Motor (071-010)"]
        STATOR["Stator Windings"]
        ROTOR["NdFeB Rotor"]
        RES["Resolver"]
    end
    subgraph TMS_BLK["Thermal Mgmt (071-050)"]
        PUMP["Coolant Pump"]
        HEX["Heat Exchanger"]
    end
    subgraph MHM_BLK["Health Monitor (071-060)"]
        FFT["FFT Engine"]
        TREND["Trend Analysis"]
    end
    DCL --> INV
    INV --> STATOR
    ROTOR --> RES
    RES -->|Position| FOC
    FOC --> SVPWM
    SVPWM -->|Gate Signals| INV
    STATOR --> TMS_BLK
    INV --> TMS_BLK
    STATOR -->|Vibration/Temp| MHM_BLK
```

## §7 Components and LRUs
| LRU ID | Name | P/N | Qty | Location |
|---|---|---|---|---|
| LRU-071-000-01 | PMSM Motor — Port | AMP-PMSM-2000-P | 1 | Aft fuselage port nacelle |
| LRU-071-000-02 | PMSM Motor — Starboard | AMP-PMSM-2000-S | 1 | Aft fuselage stbd nacelle |
| LRU-071-000-03 | Motor Drive Unit — Port | AMP-MDU-540-P | 1 | Aft equipment bay port |
| LRU-071-000-04 | Motor Drive Unit — Stbd | AMP-MDU-540-S | 1 | Aft equipment bay stbd |
| LRU-071-000-05 | Motor Control Unit | AMP-MCU-071 | 1 | Avionics bay aft |

## §8 Interfaces
| Interface | Source | Destination | Protocol | Notes |
|---|---|---|---|---|
| IF-071-000-01 | HVDC Main Bus | MDU (Port + Stbd) | 540 V DC hardwire | 800 A continuous per channel |
| IF-071-000-02 | FADEC | MCU-071 | ARINC 429 / AFDX | Thrust demand + mode commands |
| IF-071-000-03 | MCU-071 | MDU (Port + Stbd) | Fibre-optic | Gate drive PWM + telemetry |
| IF-071-000-04 | MHM | CMS / ECAM | ARINC 429 | Health alerts and diagnostics |
| IF-071-000-05 | TMS | PMSM + MDU | Coolant lines + CAN | Thermal loop control and monitoring |

## §9 Operating Modes
| Mode | Trigger | Description | Power State | Notes |
|---|---|---|---|---|
| Off | Pre-power / ground safe | All motor systems de-energised | Zero | Maintenance mode possible |
| Initialise | FADEC power-up | MCU BITE, resolver lock, MDU precharge | Standby | <30 s to ready |
| Taxi | Taxi thrust demand | Low speed torque control, gear ratio 3.5:1 | 10–20 % rated | Noise-sensitive operation |
| Climb/Cruise | Full thrust demand | FOC at rated speed, MTPA optimised | Up to 100 % rated | Primary propulsion mode |
| Deceleration / Regen | Thrust reduction / descent | Regenerative braking into HVDC bus | Negative | Subject to bus absorption capacity |

## §10 Performance and Budgets ![DRAFT](https://img.shields.io/badge/-DRAFT-yellow)
| Parameter | Requirement | Current Estimate | Unit | Status |
|---|---|---|---|---|
| Peak power (each motor) | ≥2000 | 2000 | kW | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Continuous power (each motor) | ≥1500 | 1500 | kW | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| System electrical efficiency | ≥94 | 94.5 | % | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| HVDC bus voltage | 540 ±10 % | 540 | V | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Motor speed range | 0 – 6000 | 0 – 6000 | rpm | ![TBD](https://img.shields.io/badge/-TBD-orange) |

## §11 Safety, Redundancy and Fault Tolerance
- Dual independent motor channels (port and starboard) ensure continued single-channel operation following any single motor or MDU failure, maintaining minimum controllable thrust.
- Each MDU incorporates independent over-current, over-voltage and over-temperature hardware trip circuits compliant with DO-254 DAL-B, acting within 5 µs of fault detection.
- The MCU implements dual-redundant processing lanes (primary + monitor) with cross-lane comparison; disagreement triggers a safe-state shutdown of the affected channel within one control cycle (100 µs).
- Ground Fault Detection (GFD) units on each HVDC feed monitor isolation resistance continuously; resistance below 1 MΩ triggers a contactor open within 50 ms, isolating the fault from the main bus.
- Motor health monitoring (MHM) provides continuous prognostic alerting, enabling predictive maintenance actions before safety-critical degradation thresholds are reached.

## §12 Maintenance and Diagnostics
| Task | Interval | Tool | Reference |
|---|---|---|---|
| PMSM insulation resistance test | 600 FH or C-check | Megohmmeter AMP-IR-500 | AMM 071-00-11 |
| MDU cooling system flush and refill | 1200 FH | Coolant service cart AMP-CSC-01 | AMM 071-00-21 |
| MCU BITE full download and review | Every A-check | Ground laptop + ACMF software | AMM 071-00-31 |
| Resolver calibration verification | 600 FH | MCU diagnostic port + resolver test set | AMM 071-00-41 |

## §13 Footprint
| Dimension | Value | Unit | Notes |
|---|---|---|---|
| Physical mass | TBD | kg | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Envelope | TBD | mm | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Power draw (cont.) | TBD | W | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Cooling demand | TBD | kW | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Data interfaces | TBD | — | ![TBD](https://img.shields.io/badge/-TBD-orange) |

## §14 Safety and Certification References
| Standard | Requirement | Applicability | Status | Notes |
|---|---|---|---|---|
| DO-178C | Software level per DAL | MCU software | Planned | DAL-B baseline |
| DO-254 | Hardware design assurance | MDU FPGA | Planned | DAL-B baseline |
| ARP4754A | System development | Motor system | Planned | System-level |
| CS-25 | Airworthiness requirements | Aircraft-level | Planned | EASA primary |
| FAR Part 25 | Airworthiness requirements | Aircraft-level | Planned | FAA bilateral |

## §15 V&V Approach
| Phase | Method | Tool/Facility | Status |
|---|---|---|---|
| Model-in-the-Loop | MATLAB/Simulink simulation of FOC and system model | Q-HPC simulation cluster | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Hardware-in-the-Loop | MDU + MCU on real-time target with motor emulator | AMP HIL rig AMP-HIL-071 | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Motor test bench | Full-power PMSM + MDU endurance and efficiency | AMP Motor Test Facility | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Iron-bird / aircraft integration | End-to-end power, control and BLI tests | AMPEL360E iron-bird rig | ![TBD](https://img.shields.io/badge/-TBD-orange) |

## §16 Glossary
| Term | Definition |
|---|---|
| BLI | Boundary Layer Ingestion — propulsion concept re-energising the aircraft's boundary layer |
| PMSM | Permanent Magnet Synchronous Motor |
| MDU | Motor Drive Unit — the inverter assembly converting DC to AC for the PMSM |
| MCU | Motor Control Unit — the control computer implementing FOC and control laws |
| FOC | Field-Oriented Control — vector control technique decoupling torque and flux |
| MTPA | Maximum Torque Per Ampere — FOC optimisation minimising copper losses |
| HVDC | High-Voltage Direct Current — 540 V power distribution bus on AMPEL360E |
| FADEC | Full Authority Digital Engine Control — top-level thrust management computer |
| MHM | Motor Health Monitor — subsystem for prognostic and diagnostic monitoring |
| DAL | Design Assurance Level — per DO-178C/DO-254; criticality classification A–E |

## §17 Open Issues
| ID | Description | Owner | Priority | Status |
|---|---|---|---|---|
| OI-071-000-001 | Define regenerative braking energy absorption capacity with battery system (ATA 072) | @copilot | High | Open |
| OI-071-000-002 | Confirm HVDC bus grounding strategy and GFD threshold values with electrical team | @copilot | Medium | Open |

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
| 071-010 | PMSM Motor Design and Specifications | [071-010-PMSM-Motor-Design-and-Specifications.md](071-010-PMSM-Motor-Design-and-Specifications.md) |
| 071-020 | Motor Drive Unit (MDU) and Inverter | [071-020-Motor-Drive-Unit-MDU-and-Inverter.md](071-020-Motor-Drive-Unit-MDU-and-Inverter.md) |
| 071-030 | Motor Control Unit (MCU) and Control Laws | [071-030-Motor-Control-Unit-MCU-and-Control-Laws.md](071-030-Motor-Control-Unit-MCU-and-Control-Laws.md) |
| 071-040 | Boundary Layer Ingestion (BLI) Aerodynamic Integration | [071-040-Boundary-Layer-Ingestion-Integration.md](071-040-Boundary-Layer-Ingestion-Integration.md) |
| 071-050 | Motor Thermal Management System | [071-050-Motor-Thermal-Management.md](071-050-Motor-Thermal-Management.md) |
| 071-060 | Motor Health Monitoring and Diagnostics | [071-060-Motor-Health-Monitoring-and-Diagnostics.md](071-060-Motor-Health-Monitoring-and-Diagnostics.md) |
| 071-070 | Motor Mechanical Interface and Transmission | [071-070-Motor-Mechanical-Interface-and-Transmission.md](071-070-Motor-Mechanical-Interface-and-Transmission.md) |
| 071-080 | Motor Electrical Interface and Power Quality | [071-080-Motor-Electrical-Interface-and-Power-Quality.md](071-080-Motor-Electrical-Interface-and-Power-Quality.md) |
| 071-090 | S1000D CSDB Mapping and Traceability (071) | [071-090-S1000D-CSDB-Mapping-and-Traceability.md](071-090-S1000D-CSDB-Mapping-and-Traceability.md) |

## §20 Change Log
| Rev | Date | Author | Summary |
|---|---|---|---|
| 0.1 | 2026-05-11 | @copilot | Initial creation |
