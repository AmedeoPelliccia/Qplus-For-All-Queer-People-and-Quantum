---
document_id: "QATL-ATLAS-1000-ATLAS-070-079-071-020"
register: ATLAS-1000
title: "Motor Drive Unit (MDU) and Inverter"
ata: "071"
sns: "071-020-00"
subsection: "071"
subsubject_code: "020"
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
s1000d_dmc: "DMC-AMPEL360E-EWTW-0071-020"
---

# Motor Drive Unit (MDU) and Inverter

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: 071](https://img.shields.io/badge/ATA-071-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-brightgreen)

---

## §0 Hyperlink Policy
All hyperlinks in this document are **relative**. Absolute URLs are forbidden.

## §1 Purpose
This document specifies the Motor Drive Unit (MDU) hardware design for the AMPEL360E eWTW, including the Silicon Carbide (SiC) MOSFET three-phase voltage-source inverter topology, DC link capacitor bank, gate drive circuitry, current sensing, and protection functions. It defines the MDU as the power electronics heart of the propulsion chain, converting 540 V HVDC bus power to variable-frequency AC for the PMSM.

## §2 Applicability
| Aircraft | Variant | MSN Range | Effectivity |
|---|---|---|---|
| AMPEL360E | eWTW | All | From EIS |

## §3 Functional Description ![DRAFT](https://img.shields.io/badge/-DRAFT-yellow)
Each Motor Drive Unit comprises a full three-phase two-level voltage-source inverter (VSI) built around six SiC MOSFET power switches rated at 1200 V / 600 A each (paralleled pairs giving 1200 A per switch position). Silicon Carbide is selected over conventional Si IGBTs to achieve lower switching losses at 20 kHz, enabling a more compact thermal design and reducing DC link ripple current. The 20 kHz switching frequency also shifts acoustic noise above human perception thresholds, important for urban and suburban operations. Each switch pair is mounted on a dedicated cold-plate segment of the MDU housing, cooled by the shared liquid cooling loop (see 071-050).

The DC link is provisioned with a film capacitor bank (total 2400 µF equivalent) designed to absorb PWM ripple current while limiting voltage overshoot to ≤5 % at maximum rated load step. A pre-charge circuit (soft-charge relay + NTC thermistor network) limits inrush current to ≤20 A during HVDC bus connection, protecting both the capacitor bank and bus contactors. A dedicated Insulated Gate Bipolar Transistor (IGBT) pre-charge switch and bleed resistor are included for controlled bus discharge during maintenance lockout. Current sensors (closed-loop Hall-effect, bandwidth 50 kHz) are placed in each of the three output phases and on the DC link, providing the MCU with real-time current vector data for FOC.

The MDU Controller Card (MDU-CC) is an FPGA-based board (Xilinx UltraScale+) that receives SVPWM gate timing from the MCU over a fibre-optic link, applies dead-time insertion (300 ns), and drives the isolated gate driver ICs for each SiC switch. The MDU-CC also performs local over-current, over-voltage, under-voltage, and over-temperature hardware trips within 5 µs, independent of MCU software, to provide hard-wired fault protection compliant with DO-254 DAL-B.

## §4 Functional Breakdown
| ID | Function | Description | Owner | DAL |
|---|---|---|---|---|
| F-071-020-01 | DC-AC Power Conversion | Convert 540 V DC input to 3-phase variable-frequency AC output for PMSM | Q-GREENTECH | DAL-B |
| F-071-020-02 | Gate Drive Control | Receive SVPWM timing from MCU, insert dead-time, and drive SiC MOSFET gates | Q-GREENTECH | DAL-B |
| F-071-020-03 | DC Link Voltage Regulation | Maintain stable DC link voltage via capacitor bank; limit pre-charge inrush | Q-GREENTECH | DAL-C |
| F-071-020-04 | Fault Current Protection | Hardware over-current trip (≤5 µs) isolating PMSM phases from HVDC bus | Q-GREENTECH | DAL-B |
| F-071-020-05 | Thermal Monitoring | Sense SiC junction and cold-plate temperatures; report to MHM and MCU | Q-MECHANICS | DAL-C |

## §5 System Context
```mermaid
graph TD
    HVDC["HVDC Bus 540V"] -->|Bus contactor| PRECHG["Pre-charge Circuit"]
    PRECHG -->|Charged DC| DCLINK["DC Link Capacitor Bank (2400µF)"]
    DCLINK -->|Smooth DC| BRIDGE["SiC MOSFET 3-phase Bridge (6 switches)"]
    BRIDGE -->|3-phase AC var freq| PMSM["PMSM Motor (071-010)"]
    MCU["MCU-071 (071-030)"] -->|SVPWM timing - fibre| MDUC["MDU Controller Card (FPGA)"]
    MDUC -->|Gate signals + dead-time| GATEDRV["Gate Driver ICs (×6)"]
    GATEDRV --> BRIDGE
    CURSEN["3-phase Current Sensors"] -->|i_a, i_b, i_c| MCU
    BRIDGE --> CURSEN
    TEMPSEN["SiC Temp Sensors (×6)"] -->|Junction temps| MDUC
    MDUC -->|Fault status| MCU
    COLD["MDU Cold Plate (071-050)"] --> BRIDGE
```

## §6 Internal Architecture
```mermaid
graph TD
    subgraph INPUT["Input Stage"]
        CONTACTOR["HVDC Bus Contactor"]
        PRECHG2["Pre-charge Resistor + Switch"]
        BLEED["Bleed Resistor (discharge)"]
    end
    subgraph DCLINK_BLK["DC Link"]
        CAPS["Film Capacitor Bank (2400µF)"]
        DCSENSE["DC Link Voltage Sensor"]
    end
    subgraph INVERTER["Inverter Bridge"]
        Q1["SiC Switch Q1 (Ph-A High)"]
        Q2["SiC Switch Q2 (Ph-A Low)"]
        Q3["SiC Switch Q3 (Ph-B High)"]
        Q4["SiC Switch Q4 (Ph-B Low)"]
        Q5["SiC Switch Q5 (Ph-C High)"]
        Q6["SiC Switch Q6 (Ph-C Low)"]
    end
    subgraph CONTROL_HW["MDU Controller Card"]
        FPGA["Xilinx UltraScale+ FPGA"]
        GDRV["Isolated Gate Drivers (×6)"]
        HWTRIP["HW Trip Logic (<5µs)"]
    end
    CONTACTOR --> PRECHG2
    PRECHG2 --> CAPS
    CAPS --> Q1 & Q3 & Q5
    Q2 & Q4 & Q6 --> GND_REF["DC Negative Rail"]
    FPGA --> GDRV --> Q1 & Q2 & Q3 & Q4 & Q5 & Q6
    HWTRIP -->|Gate inhibit| GDRV
```

## §7 Components and LRUs
| LRU ID | Name | P/N | Qty | Location |
|---|---|---|---|---|
| LRU-071-020-01 | SiC Power Module Assembly (3-phase bridge) | AMP-SiC-1200-3PH | 2 | MDU housing, per motor |
| LRU-071-020-02 | DC Link Capacitor Bank | AMP-DCLINK-2400 | 2 | MDU housing, per motor |
| LRU-071-020-03 | Gate Driver Board | AMP-GDB-071 | 2 | MDU housing, mounted on SiC module |
| LRU-071-020-04 | Current Sensor Assembly (3-phase + DC link) | AMP-CURSEN-071 | 2 | MDU phase output busbars |
| LRU-071-020-05 | MDU Controller Card (FPGA) | AMP-MDU-CC-071 | 2 | MDU control bay, per motor |

## §8 Interfaces
| Interface | Source | Destination | Protocol | Notes |
|---|---|---|---|---|
| IF-071-020-01 | HVDC Main Bus (071-080) | MDU DC input | 540 V DC, hardwire busbar | 1200 A peak capacity |
| IF-071-020-02 | MCU-071 (071-030) | MDU Controller Card | Fibre-optic serial, 100 Mbit/s | SVPWM timing + mode commands |
| IF-071-020-03 | MDU Controller Card | MCU-071 | CAN-FD | Fault status, temp telemetry |
| IF-071-020-04 | SiC bridge output | PMSM Terminal Box (071-010) | 3-phase AC via shielded cable | Lemo MIL-SPEC HV connector |
| IF-071-020-05 | Coolant loop (071-050) | MDU Cold Plate | Liquid coolant, ¾" SAE fitting | 8 L/min, ≤40 °C inlet |

## §9 Operating Modes
| Mode | Trigger | Description | Power State | Notes |
|---|---|---|---|---|
| Pre-charge | Bus connect command | Soft-charge DC link via NTC resistor network | Standby | Duration <2 s |
| Standby | Pre-charge complete | DC link at nominal voltage, gates inhibited | Standby | Ready for modulation in <10 ms |
| Motoring | Gate enable + SVPWM | Normal inverter operation driving PMSM | 0–100 % rated | FOC current commands from MCU |
| Regenerative | Negative torque demand | Power flow reversed; MDU acts as active rectifier | Negative | Limited by bus absorption capability |
| Fault Inhibit | Hardware trip | All gates inhibited within 5 µs; DC link held charged | Zero output | Fault logged; await MCU reset command |

## §10 Performance and Budgets ![DRAFT](https://img.shields.io/badge/-DRAFT-yellow)
| Parameter | Requirement | Current Estimate | Unit | Status |
|---|---|---|---|---|
| Switching frequency | 20 | 20 | kHz | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| DC input voltage range | 540 ±10 % | 486–594 | V | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Peak output phase current | ≥3500 | 3500 | A | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| MDU conversion efficiency | ≥98.5 | 98.6 | % | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| SiC junction thermal limit | ≤175 °C | 85 °C (cold-plate) | °C | ![TBD](https://img.shields.io/badge/-TBD-orange) |

## §11 Safety, Redundancy and Fault Tolerance
- Hardware over-current trip implemented in FPGA logic (DO-254 DAL-B) responds within 5 µs, fully independent of MCU software to prevent cascading failures from software faults.
- Dual-redundant DC link voltage sensors feed both the MDU Controller Card and MCU-071; disagreement between sensors within 5 % triggers a CAS advisory and a manual inspection requirement.
- SiC MOSFET gate drivers include desaturation detection circuits; if any switch exits saturation under current, the associated leg is hard-tripped within 500 ns, preventing uncontrolled energy dump.
- Pre-charge circuit limits inrush current to ≤20 A, protecting both DC link capacitors and HVDC bus contactors from mechanical fatigue due to repetitive high-current transients.
- Maintenance discharge path (bleed resistor + IGBT switch) reduces DC link to ≤50 V within 30 s after bus disconnection, enabling safe maintenance access per CDCCL safety requirements.

## §12 Maintenance and Diagnostics
| Task | Interval | Tool | Reference |
|---|---|---|---|
| DC link capacitor ESR and capacitance measurement | 1200 FH | AMP-CAP-TESTER-01 | AMM 071-20-11 |
| SiC module thermal resistance check (Rth-jc) | 600 FH | MDU BITE + thermal data log | AMM 071-20-21 |
| Gate driver isolation voltage test | C-check | BITE self-test or bench tester | AMM 071-20-31 |
| Current sensor offset and gain calibration | 600 FH | MCU calibration mode + PC tool | AMM 071-20-41 |

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
| SPICE / circuit simulation | SiC switching losses, DC link ripple, gate drive margins | LTspice + SiC vendor SPICE models | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| MDU hardware-in-the-loop | FPGA gate logic with simulated PMSM loads | AMP HIL rig AMP-HIL-071 | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Full-power bench test | Efficiency map, switching waveforms, thermal soak at rated power | AMP Power Electronics Lab | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| EMC / DO-160G Section 16 | Conducted and radiated emissions, susceptibility | EMC certified test house | ![TBD](https://img.shields.io/badge/-TBD-orange) |

## §16 Glossary
| Term | Definition |
|---|---|
| MDU | Motor Drive Unit — the inverter assembly for one PMSM channel |
| SiC MOSFET | Silicon Carbide Metal-Oxide-Semiconductor Field-Effect Transistor |
| VSI | Voltage-Source Inverter — inverter topology maintaining stiff DC link voltage |
| DC Link | Energy storage capacitor bank bridging the HVDC bus and inverter bridge |
| Dead-time | Blanking interval inserted between complementary gate signals to prevent shoot-through |
| SVPWM | Space Vector Pulse Width Modulation — optimal PWM technique minimising harmonics |
| Desaturation | Condition where MOSFET leaves linear saturation due to excessive current |
| Rth-jc | Junction-to-case thermal resistance of semiconductor device |
| ESR | Equivalent Series Resistance of capacitor; indicator of degradation |
| Pre-charge | Controlled DC link energisation to limit capacitor inrush current |

## §17 Open Issues
| ID | Description | Owner | Priority | Status |
|---|---|---|---|---|
| OI-071-020-001 | Confirm SiC module supplier qualification to AQS (Aviation Quality Standard) and radiation environment | @copilot | High | Open |
| OI-071-020-002 | Define EMI filter topology between HVDC contactor and MDU input (coordinate with 071-080) | @copilot | Medium | Open |

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
| 071-000 | Electric Motor and Drive Systems — General Overview | [071-000-Electric-Motor-and-Drive-Systems-General.md](071-000-Electric-Motor-and-Drive-Systems-General.md) |
| 071-010 | PMSM Motor Design and Specifications | [071-010-PMSM-Motor-Design-and-Specifications.md](071-010-PMSM-Motor-Design-and-Specifications.md) |
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
