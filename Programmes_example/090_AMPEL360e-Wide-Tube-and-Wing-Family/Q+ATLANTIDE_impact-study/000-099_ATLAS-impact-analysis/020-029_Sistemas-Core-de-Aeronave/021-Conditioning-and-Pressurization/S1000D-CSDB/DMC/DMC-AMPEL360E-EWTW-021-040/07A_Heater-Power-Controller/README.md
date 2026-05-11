---
document_id: DMC-AMPEL360E-EWTW-021-040-07A-GROUP-README
title: "DMC Group — DMC-AMPEL360E-EWTW-021-040-07A"
programme: "AMPEL360e Wide Tube-and-Wing Family"
short_code: "eWTW"
system: "021 — Conditioning and Pressurization"
sub_system: "021-040 — Heating Subsystem"
component: "Heater Power Controller"
sns: "021-040-07A"
ata_reference: "ATA 21-40"
model_ident_code: "AMPEL360E"
system_diff_code: "EWTW"
system_code: "021"
sub_system_code: "0"
sub_sub_system_code: "40"
assy_code: "07A"
item_location_code: "D"
status: "programme-controlled-scaffold-placeholder"
created: 2026-05-10
classification: "open-technical-scaffold"
primary_q_division: "Q-DATAGOV"
support_q_divisions:
  - "Q-AIR"
  - "Q-MECHANICS"
  - "Q-INDUSTRY"
lifecycle_phase:
  - "LC03"
  - "LC05"
  - "LC06"
  - "LC11"
  - "LC12"
review_status: "to-be-reviewed-by-system-expert"
---

# DMC Group: DMC-AMPEL360E-EWTW-021-040-07A

## Identification

**Programme:** AMPEL360e Wide Tube-and-Wing Family  
**Short code:** eWTW  
**System:** 021 — Conditioning and Pressurization  
**Sub-system:** 021-040 — Heating Subsystem  
**Component:** Heater Power Controller  
**SNS node:** 021-040-07A  
**ATA reference:** ATA 21-40  
**DMC group:** DMC-AMPEL360E-EWTW-021-040-07A  

## Purpose

This DMC group contains the S1000D/CSDB scaffold for the **021-040 / 07A Heater Power Controller** node of the AMPEL360e eWTW Heating Subsystem.

The group covers design description, operation, maintenance, inspection, fault isolation, removal/installation, and illustrated parts data for the Heater Power Controller within the ATA 21-40 Heating Subsystem.

## System Scope

The Heater Power Controller is a constituent of the AMPEL360e eWTW Heating Subsystem (ATA 21-40). Its main functions include:

- provide or support the heating function for the assigned zone or element;
- interface with heating power supply, control, and overtemperature protection architecture;
- support maintenance, inspection, removal, and reinstallation activities;
- provide fault detection, isolation, and BITE interfaces where applicable.

## Info-Code Folder Index

| Folder | Info Code(s) | Use |
|---|---|---|
| `040_descriptive/` | 040 | system description / descriptive data module |
| `100_operation/` | 100 | operation / operating procedures |
| `300_examinations-tests-and-checks/` | 300, 320 | inspection, examinations, tests and checks |
| `400_fault-reports-and-isolation-procedures/` | 400, 420 | fault reporting and fault isolation procedures |
| `500_disconnect-remove-and-disassembly-procedures/` | 520 | disconnect, remove and disassembly procedures |
| `700_assemble-install-and-connect-procedures/` | 720 | assemble, install and connect procedures |
| `940_provisioning-data/` | 940 | provisioning data |
| `941_illustrated-parts-data/` | 941 | illustrated parts data |
| `C00_computer-systems-software-and-data/` | C00 | computer systems, software and data |

## Recommended Data Module Set

| Info code | Data module purpose | Suggested filename |
|---:|---|---|
| 040 | Heater Power Controller — Description | `DMC-AMPEL360E-EWTW-021-040-07A-040A-D_Heater-Power-Controller-Description.xml` |
| 100 | Heater Power Controller — Operation | `DMC-AMPEL360E-EWTW-021-040-07A-100A-D_Heater-Power-Controller-Operation.xml` |
| 300 | Heater Power Controller — Inspection | `DMC-AMPEL360E-EWTW-021-040-07A-300A-D_Heater-Power-Controller-Inspection.xml` |
| 320 | Heater Power Controller — Functional Test | `DMC-AMPEL360E-EWTW-021-040-07A-320A-D_Heater-Power-Controller-Functional-Test.xml` |
| 400 | Heater Power Controller — Fault Reporting | `DMC-AMPEL360E-EWTW-021-040-07A-400A-D_Heater-Power-Controller-Fault-Reporting.xml` |
| 420 | Heater Power Controller — Fault Isolation | `DMC-AMPEL360E-EWTW-021-040-07A-420A-D_Heater-Power-Controller-Fault-Isolation.xml` |
| 520 | Heater Power Controller — Remove Procedure | `DMC-AMPEL360E-EWTW-021-040-07A-520A-D_Heater-Power-Controller-Remove-Procedure.xml` |
| 720 | Heater Power Controller — Install Procedure | `DMC-AMPEL360E-EWTW-021-040-07A-720A-D_Heater-Power-Controller-Install-Procedure.xml` |
| 940 | Heater Power Controller — Provisioning Data | `DMC-AMPEL360E-EWTW-021-040-07A-940A-D_Heater-Power-Controller-Provisioning-Data.xml` |
| 941 | Heater Power Controller — Illustrated Parts Data | `DMC-AMPEL360E-EWTW-021-040-07A-941A-D_Heater-Power-Controller-Illustrated-Parts-Data.xml` |
| C00 | Heater Power Controller — Software Data | `DMC-AMPEL360E-EWTW-021-040-07A-C00A-D_Heater-Power-Controller-Software-Data.xml` |

## Technical Boundaries

### Included

- all mechanical and electrical elements of the Heater Power Controller assembly;
- electrical power supply and control interfaces within the component boundary;
- thermal and airflow interfaces within the heating subsystem boundary;
- mounting hardware, fasteners, and structural attachment interfaces;
- sensor, limiter, and BITE interfaces associated with this component;
- wiring, connectors, and bonding interfaces within the component boundary;
- maintenance access panels and mounting interfaces directly associated with this component.

### Excluded

- elements assigned to adjacent heating subsystem components;
- cabin temperature-control algorithms outside the component control boundary;
- pressurization-control architecture (ATA 21-30);
- anti-ice and de-ice systems (ATA 30);
- supplier-controlled proprietary design data unless released to the CSDB baseline;
- ground support equipment not permanently installed on the aircraft.

## Traceability

| Trace item | Value |
|---|---|
| ATLAS branch | `000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/021-Conditioning-and-Pressurization` |
| Programme path | `Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family` |
| S1000D group path | `S1000D-CSDB/DMC/DMC-AMPEL360E-EWTW-021-040/07A_Heater-Power-Controller` |
| Parent DMC group | `DMC-AMPEL360E-EWTW-021-040-00A` |
| SNS | `021-040-07A` |
| ATA reference | `ATA 21-40` |
| DMC prefix | `DMC-AMPEL360E-EWTW-021-040-07A` |
| Primary lifecycle use | LC05 Detailed Design / LC06 Verification Planning / LC11 Operation / LC12 Maintenance Support |

## Review and Governance

> Programme-controlled scaffold. Content is subject to BREX, SNS, applicability, DMRL, and CCB freeze before controlled release.

> **To be reviewed by system expert.**
