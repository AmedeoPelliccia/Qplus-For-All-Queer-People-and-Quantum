---
document_id: DMC-AMPEL360E-EWTW-021-010-04A-GROUP-README
title: "DMC Group — DMC-AMPEL360E-EWTW-021-010-04A"
programme: "AMPEL360e Wide Tube-and-Wing Family"
short_code: "eWTW"
system: "021 — Conditioning and Pressurization"
sub_system: "021-010 — Compression Subsystem"
component: "Compressor Control Unit"
sns: "021-010-04A"
ata_reference: "ATA 21-10"
model_ident_code: "AMPEL360E"
system_diff_code: "EWTW"
system_code: "021"
sub_system_code: "0"
sub_sub_system_code: "10"
assy_code: "04A"
item_location_code: "D"
status: "programme-controlled-scaffold-placeholder"
document_status: "DRAFT"
completion_status: "To Be Completed"
review_status: "to-be-reviewed-by-system-expert"
created: 2026-05-09
classification: "open-technical-scaffold"
primary_q_division: "Q-DATAGOV"
support_q_divisions:
  - "Q-AIR"
  - "Q-MECHANICS"
  - "Q-INDUSTRY"
  - "Q-HPC"
lifecycle_phase:
  - "LC03"
  - "LC05"
  - "LC06"
  - "LC11"
  - "LC12"
---

![DRAFT](https://img.shields.io/badge/DRAFT-yellow)
![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)
![TBD](https://img.shields.io/badge/TBD-red)

# DMC Group: DMC-AMPEL360E-EWTW-021-010-04A

<img width="1536" height="1024" alt="AMPEL360e EWTW 021-010 / 04A Compressor Control Unit — technical illustration showing control-unit housing, connector panel, internal electronics, system function diagram, aircraft locator, sensor inputs, actuator outputs, maintenance port, and vibration-isolated mounting" src="https://github.com/user-attachments/assets/21a8d104-77b6-4a25-8af1-e079a8526721" />

***Figure 1 — DMC-AMPEL360E-EWTW-021-010-04A Compressor Control Unit. Technical illustration showing the electronic control-unit housing, connector panel, internal electronics, system function diagram, pressure/temperature/speed sensor inputs, actuator outputs, aircraft-system interfaces, maintenance port, vibration-isolated mounting, and forward lower fuselage equipment-bay locator.***

## Identification

**Programme:** AMPEL360e Wide Tube-and-Wing Family  
**Short code:** eWTW  
**System:** 021 — Conditioning and Pressurization  
**Sub-system:** 021-010 — Compression Subsystem  
**Component:** Compressor Control Unit  
**SNS node:** 021-010-04A  
**ATA reference:** ATA 21-10  
**DMC group:** DMC-AMPEL360E-EWTW-021-010-04A  

## Purpose

This DMC group contains the S1000D/CSDB scaffold for the **021-010 / 04A Compressor Control Unit** node of the AMPEL360e EWTW compression subsystem.

The group covers the descriptive, operational, inspection, test, fault isolation, removal, installation, provisioning, illustrated-parts, software-configuration, and diagnostic-data modules required to support the electronic control and monitoring unit associated with the electric cabin air compressor.

## System Scope

The Compressor Control Unit monitors and controls the electric cabin air compressor and its associated drive, sensors, actuator outputs, protection logic, operating modes, and maintenance diagnostics.

The component-level scope includes:

- control-unit housing;
- power input connector;
- data/control connector;
- sensor input connector;
- actuator output connector;
- Ethernet or maintenance port, where applicable;
- microprocessor and control logic;
- memory and configuration data;
- input/output interface electronics;
- power supply and conditioning module;
- BITE and diagnostic functions;
- pressure, temperature, speed, voltage, and current monitoring interfaces;
- compressor drive motor and inverter interface;
- electric cabin air compressor interface;
- vibration-isolated mounting base.

## Info-Code Folder Index

| Folder | Info Code(s) | Use |
|---|---:|---|
| `040_descriptive/` | 040 | System description / descriptive data module |
| `100_operation/` | 100 | Operation data module |
| `300_examinations-tests-and-checks/` | 300, 320 | Inspection, operational checks, and functional tests |
| `400_fault-reports-and-isolation-procedures/` | 400, 420 | Fault reporting and fault isolation procedures |
| `500_disconnect-remove-and-disassembly-procedures/` | 520 | Disconnect, remove, and disassembly procedures |
| `700_assemble-install-and-connect-procedures/` | 720, 740 | Assemble, install, and connect procedures |
| `940_provisioning-data/` | 940 | Provisioning data |
| `941_illustrated-parts-data/` | 941 | Illustrated parts data |
| `C00_computer-systems-software-and-data/` | C00, C10, C20 | Computer systems, software configuration, and diagnostic data |

## Recommended Data Module Set

| Info code | Data module purpose | Suggested filename | Status |
|---:|---|---|---|
| 040 | Compressor control unit description | `DMC-AMPEL360E-EWTW-021-010-04A-040A-D_System-Description.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 100 | Compressor control unit operation | `DMC-AMPEL360E-EWTW-021-010-04A-100A-D_Operation.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 300 | General inspection / examination | `DMC-AMPEL360E-EWTW-021-010-04A-300A-D_General-Inspection.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 320 | Functional test | `DMC-AMPEL360E-EWTW-021-010-04A-320A-D_Functional-Test.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 400 | Fault isolation introduction | `DMC-AMPEL360E-EWTW-021-010-04A-400A-D_Fault-Isolation.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 420 | Fault isolation procedure | `DMC-AMPEL360E-EWTW-021-010-04A-420A-D_Fault-Isolation-Procedure.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 520 | Remove procedure | `DMC-AMPEL360E-EWTW-021-010-04A-520A-D_Remove.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 720 | Install procedure | `DMC-AMPEL360E-EWTW-021-010-04A-720A-D_Install.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 740 | Connect / restore procedure | `DMC-AMPEL360E-EWTW-021-010-04A-740A-D_Connect-and-Restore.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 940 | Provisioning data | `DMC-AMPEL360E-EWTW-021-010-04A-940A-D_Provisioning-Data.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 941 | Illustrated parts data | `DMC-AMPEL360E-EWTW-021-010-04A-941A-D_Illustrated-Parts-Data.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| C00 | Computer system / embedded control description | `DMC-AMPEL360E-EWTW-021-010-04A-C00A-D_Computer-System-Description.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| C10 | Software configuration data | `DMC-AMPEL360E-EWTW-021-010-04A-C10A-D_Software-Configuration-Data.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| C20 | Diagnostic data / fault memory interface | `DMC-AMPEL360E-EWTW-021-010-04A-C20A-D_Diagnostic-Data.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |

## Technical Boundaries

### Included

- compressor control unit housing;
- control electronics;
- power supply and conditioning electronics;
- microprocessor and control logic;
- memory and configuration data;
- input/output interface board;
- sensor input interfaces;
- actuator output interfaces;
- data/control connector;
- maintenance or Ethernet port, where applicable;
- BITE and diagnostic logic;
- status indicator LEDs, where applicable;
- vibration-isolated mounting interface;
- S1000D/CSDB traceability for the 021-010 / 04A node.

### Excluded

- internal aerodynamic compressor stage;
- motor and inverter power electronics unless allocated to 03A;
- electric cabin air compressor mechanical assembly unless allocated to 02A;
- upstream aircraft power-generation architecture;
- downstream air distribution and pressurization logic;
- supplier-proprietary firmware or source code unless released to the CSDB baseline;
- final certified software/hardware assurance classification until programme verification is complete.

## Interface Summary

| Interface | Type | Description | Status |
|---|---|---|---|
| Power input | Electrical | DC or conditioned aircraft power input to the control unit | ![TBD](https://img.shields.io/badge/TBD-red) |
| Data/control connector | Digital / discrete | Command, status, BITE, health monitoring, and control communication | ![TBD](https://img.shields.io/badge/TBD-red) |
| Sensor input connector | Analog / digital | Pressure, temperature, speed, current, voltage, and position sensing as applicable | ![TBD](https://img.shields.io/badge/TBD-red) |
| Actuator output connector | Control output | Command output to valves, actuators, inverter, or compressor-control elements | ![TBD](https://img.shields.io/badge/TBD-red) |
| Maintenance port | Data | Local maintenance, software/configuration access, or diagnostic data interface | ![TBD](https://img.shields.io/badge/TBD-red) |
| Motor and inverter interface | Control / monitoring | Interface to 03A Compressor Drive Motor and Inverter | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| Compressor interface | Control / monitoring | Interface to 02A Electric Cabin Air Compressor | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| Mounting interface | Mechanical | Vibration-isolated installation on equipment-bay structure | ![TBD](https://img.shields.io/badge/TBD-red) |

## Safety and Maintenance Notes

The Compressor Control Unit shall be treated as safety-relevant electronic control equipment for the compression subsystem.

Maintenance content shall include:

- electrical isolation before access;
- ESD precautions;
- connector protection and pin-damage prevention;
- software/configuration part-number verification;
- data-load authorization controls, where applicable;
- bonding and grounding verification;
- environmental sealing inspection;
- moisture and contamination checks;
- connector torque and locking verification;
- BITE confirmation after replacement;
- functional test after installation or software/configuration change.

## Software and Data Configuration

Software and configuration data for the Compressor Control Unit shall remain controlled under the applicable computer-systems, software, and diagnostic-data folders.

The following data categories shall be treated as configuration-controlled:

- control-unit software part number;
- configuration data set;
- calibration parameters;
- sensor scaling parameters;
- fault-threshold tables;
- BITE and diagnostic message tables;
- communication data dictionary;
- applicable software loading procedure;
- rollback or recovery procedure, where applicable.

## Traceability

| Trace item | Value |
|---|---|
| ATLAS branch | `000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/021-Conditioning-and-Pressurization` |
| Programme path | `Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family` |
| S1000D group path | `S1000D-CSDB/DMC/DMC-AMPEL360E-EWTW-021-010/04A_Compressor-Control-Unit` |
| Parent DMC group | `DMC-AMPEL360E-EWTW-021-010-00A` |
| Related DMC group | `DMC-AMPEL360E-EWTW-021-010-02A` |
| Related DMC group | `DMC-AMPEL360E-EWTW-021-010-03A` |
| SNS | `021-010-04A` |
| ATA reference | `ATA 21-10` |
| DMC prefix | `DMC-AMPEL360E-EWTW-021-010-04A` |
| Primary lifecycle use | LC05 Detailed Design / LC06 Verification Planning / LC11 Operation / LC12 Maintenance Support |

## Review and Governance

> Programme-controlled scaffold. Content is subject to BREX, SNS, applicability, DMRL, software/configuration control, and CCB freeze before controlled release.

> **To be reviewed by system expert.**
