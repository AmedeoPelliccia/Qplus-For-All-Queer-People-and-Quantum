---
document_id: DMC-AMPEL360E-EWTW-021-010-03A-GROUP-README
title: "DMC Group — DMC-AMPEL360E-EWTW-021-010-03A"
programme: "AMPEL360e Wide Tube-and-Wing Family"
short_code: "eWTW"
system: "021 — Conditioning and Pressurization"
sub_system: "021-010 — Compression Subsystem"
component: "Compressor Drive Motor and Inverter"
sns: "021-010-03A"
ata_reference: "ATA 21-10"
model_ident_code: "AMPEL360E"
system_diff_code: "EWTW"
system_code: "021"
sub_system_code: "0"
sub_sub_system_code: "10"
assy_code: "03A"
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

# DMC Group: DMC-AMPEL360E-EWTW-021-010-03A

<img width="1536" height="1024" alt="AMPEL360e EWTW 021-010 / 03A Compressor Drive Motor and Inverter — technical illustration showing PMSM motor, inverter drive unit, high-voltage connectors, control connector, coolant interface, vibration isolators, motor cutaway, inverter top view, system function diagram, and aircraft locator" src="https://github.com/user-attachments/assets/7f0e6a57-b4dd-4b20-8fb1-ed1ef9b6b77d" />

***Figure 1 — DMC-AMPEL360E-EWTW-021-010-03A Compressor Drive Motor and Inverter. Technical illustration showing the electric drive motor, inverter/drive unit, high-voltage connectors, control connector, coolant interface, vibration-isolated mounting base, motor cutaway view, inverter top view, simplified function diagram, and forward lower fuselage equipment-bay locator.***

## Identification

**Programme:** AMPEL360e Wide Tube-and-Wing Family  
**Short code:** eWTW  
**System:** 021 — Conditioning and Pressurization  
**Sub-system:** 021-010 — Compression Subsystem  
**Component:** Compressor Drive Motor and Inverter  
**SNS node:** 021-010-03A  
**ATA reference:** ATA 21-10  
**DMC group:** DMC-AMPEL360E-EWTW-021-010-03A  

## Purpose

This DMC group contains the S1000D/CSDB scaffold for the **021-010 / 03A Compressor Drive Motor and Inverter** node of the AMPEL360e EWTW compression subsystem.

The group covers the descriptive, inspection, test, fault isolation, removal, installation, provisioning, illustrated-parts, software-configuration, and diagnostic-data modules required to support the electric motor and inverter assembly used to drive the cabin air compressor.

## System Scope

The Compressor Drive Motor and Inverter converts aircraft electrical power into controlled mechanical shaft power for the Electric Cabin Air Compressor.

The component-level scope includes:

- permanent-magnet synchronous motor or equivalent electric drive motor;
- inverter / drive unit;
- DC input interface;
- three-phase AC output interface to the motor;
- motor control unit or embedded control electronics;
- gate-driver and protection electronics;
- high-voltage connectors;
- control and data connector;
- cooling interface;
- shaft, rotor, stator, bearings, and housing;
- vibration-isolated mounting base;
- temperature, current, voltage, and speed sensing;
- BITE and diagnostic-data interface.

## Info-Code Folder Index

| Folder | Info Code(s) | Use |
|---|---:|---|
| `040_descriptive/` | 040 | System description / descriptive data module |
| `300_examinations-tests-and-checks/` | 300, 320 | Inspection, operational checks, and functional tests |
| `400_fault-reports-and-isolation-procedures/` | 400, 420 | Fault reporting and fault isolation procedures |
| `500_disconnect-remove-and-disassembly-procedures/` | 500, 520 | Disconnect, remove, and disassembly procedures |
| `700_assemble-install-and-connect-procedures/` | 720, 740 | Assemble, install, and connect procedures |
| `940_provisioning-data/` | 940 | Provisioning data |
| `941_illustrated-parts-data/` | 941 | Illustrated parts data |
| `C00_computer-systems-software-and-data/` | C00, C10, C20 | Computer systems, software configuration, and diagnostic data |

## Recommended Data Module Set

| Info code | Data module purpose | Suggested filename | Status |
|---:|---|---|---|
| 040 | Compressor drive motor and inverter description | `DMC-AMPEL360E-EWTW-021-010-03A-040A-D_System-Description.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 300 | General inspection / examination | `DMC-AMPEL360E-EWTW-021-010-03A-300A-D_General-Inspection.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 320 | Functional test | `DMC-AMPEL360E-EWTW-021-010-03A-320A-D_Functional-Test.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 400 | Fault isolation introduction | `DMC-AMPEL360E-EWTW-021-010-03A-400A-D_Fault-Isolation.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 420 | Fault isolation procedure | `DMC-AMPEL360E-EWTW-021-010-03A-420A-D_Fault-Isolation-Procedure.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 500 | Disconnect / prepare for removal | `DMC-AMPEL360E-EWTW-021-010-03A-500A-D_Disconnect.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 520 | Remove procedure | `DMC-AMPEL360E-EWTW-021-010-03A-520A-D_Remove.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 720 | Install procedure | `DMC-AMPEL360E-EWTW-021-010-03A-720A-D_Install.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 740 | Connect / restore procedure | `DMC-AMPEL360E-EWTW-021-010-03A-740A-D_Connect-and-Restore.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 940 | Provisioning data | `DMC-AMPEL360E-EWTW-021-010-03A-940A-D_Provisioning-Data.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| 941 | Illustrated parts data | `DMC-AMPEL360E-EWTW-021-010-03A-941A-D_Illustrated-Parts-Data.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| C00 | Computer system / embedded control description | `DMC-AMPEL360E-EWTW-021-010-03A-C00A-D_Computer-System-Description.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| C10 | Software configuration data | `DMC-AMPEL360E-EWTW-021-010-03A-C10A-D_Software-Configuration-Data.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| C20 | Diagnostic data / fault memory interface | `DMC-AMPEL360E-EWTW-021-010-03A-C20A-D_Diagnostic-Data.xml` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |

## Technical Boundaries

### Included

- compressor drive motor;
- inverter / drive unit;
- motor shaft and bearings;
- rotor and stator;
- cooling jacket or cooling interface;
- high-voltage DC input interface;
- three-phase AC output interface;
- control connector;
- motor control electronics;
- inverter protection logic;
- temperature, current, voltage, and speed sensing;
- vibration-isolated mounting base;
- BITE and diagnostic interface;
- software configuration and diagnostic data where applicable;
- S1000D/CSDB traceability for the 021-010 / 03A node.

### Excluded

- compressor aerodynamic stage internal design, unless directly coupled to the motor shaft boundary;
- cabin air compressor casing and pneumatic flow path outside the drive boundary;
- upstream electrical power generation and distribution architecture;
- downstream cabin air distribution;
- supplier-proprietary inverter firmware or motor-control algorithms unless released to the CSDB baseline;
- final certified electrical ratings until programme verification is complete.

## Interface Summary

| Interface | Type | Description | Status |
|---|---|---|---|
| DC power input | Electrical | Aircraft electrical power input to the inverter / drive unit | ![TBD](https://img.shields.io/badge/TBD-red) |
| Three-phase motor output | Electrical | Controlled AC output from inverter to motor phases | ![TBD](https://img.shields.io/badge/TBD-red) |
| Control connector | Data / discrete | Command, status, BITE, health monitoring, and diagnostic communication | ![TBD](https://img.shields.io/badge/TBD-red) |
| Cooling interface | Thermal / fluid | Air, liquid, or conduction cooling interface for motor and inverter thermal control | ![TBD](https://img.shields.io/badge/TBD-red) |
| Shaft interface | Mechanical | Mechanical drive connection from motor to compressor stage | ![TBD](https://img.shields.io/badge/TBD-red) |
| Mounting interface | Mechanical | Vibration-isolated installation on equipment-bay structure | ![TBD](https://img.shields.io/badge/TBD-red) |
| Diagnostic-data interface | Software / data | Fault memory, event data, software part number, and health-monitoring interface | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |

## Safety and Maintenance Notes

The Compressor Drive Motor and Inverter shall be treated as a high-energy electrical drive, rotating-machine assembly, and safety-relevant compressor-drive component.

Maintenance content shall include:

- electrical isolation before access;
- high-voltage absence verification;
- stored-energy discharge confirmation;
- inverter capacitor discharge wait time;
- ESD precautions for electronic modules;
- rotating-part and shaft-coupling precautions;
- hot-surface precautions after operation;
- coolant isolation and leak prevention, where applicable;
- connector protection and pin-damage prevention;
- bonding and grounding verification;
- post-installation functional test or BITE confirmation.

## Traceability

| Trace item | Value |
|---|---|
| ATLAS branch | `000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/021-Conditioning-and-Pressurization` |
| Programme path | `Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family` |
| S1000D group path | `S1000D-CSDB/DMC/DMC-AMPEL360E-EWTW-021-010/03A_Compressor-Drive-Motor-and-Inverter` |
| Parent DMC group | `DMC-AMPEL360E-EWTW-021-010-00A` |
| Related DMC group | `DMC-AMPEL360E-EWTW-021-010-02A` |
| SNS | `021-010-03A` |
| ATA reference | `ATA 21-10` |
| DMC prefix | `DMC-AMPEL360E-EWTW-021-010-03A` |
| Primary lifecycle use | LC05 Detailed Design / LC06 Verification Planning / LC11 Operation / LC12 Maintenance Support |

## Review and Governance

> Programme-controlled scaffold. Content is subject to BREX, SNS, applicability, DMRL, and CCB freeze before controlled release.

> **To be reviewed by system expert.**
