---
document_id: DMC-AMPEL360E-EWTW-021-040-14A-GROUP-README
title: "DMC Group — DMC-AMPEL360E-EWTW-021-040-14A"
programme: "AMPEL360e Wide Tube-and-Wing Family"
short_code: "eWTW"
system: "021 — Conditioning and Pressurization"
sub_system: "021-040 — Heating Subsystem"
component: "Heating Software Configuration and Control Data"
sns: "021-040-14A"
ata_reference: "ATA 21-40"
model_ident_code: "AMPEL360E"
system_diff_code: "EWTW"
system_code: "021"
sub_system_code: "0"
sub_sub_system_code: "40"
assy_code: "14A"
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

# DMC Group: DMC-AMPEL360E-EWTW-021-040-14A

## Identification

**Programme:** AMPEL360e Wide Tube-and-Wing Family  
**Short code:** eWTW  
**System:** 021 — Conditioning and Pressurization  
**Sub-system:** 021-040 — Heating Subsystem  
**Component:** Heating Software Configuration and Control Data  
**SNS node:** 021-040-14A  
**ATA reference:** ATA 21-40  
**DMC group:** DMC-AMPEL360E-EWTW-021-040-14A  

## Purpose

This DMC group contains the S1000D/CSDB scaffold for the **021-040 / 14A Heating Software Configuration and Control Data** node of the AMPEL360e eWTW Heating Subsystem.

The group covers design description, operation, maintenance, inspection, fault isolation, removal/installation, and illustrated parts data for the Heating Software Configuration and Control Data within the ATA 21-40 Heating Subsystem.

## System Scope

The Heating Software Configuration and Control Data is a constituent of the AMPEL360e eWTW Heating Subsystem (ATA 21-40). Its main functions include:

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
| `700_assemble-install-and-connect-procedures/` | 720 | assemble, install and connect procedures |
| `940_provisioning-data/` | 940 | provisioning data |
| `941_illustrated-parts-data/` | 941 | illustrated parts data |
| `C00_computer-systems-software-and-data/` | C00 | computer systems, software and data |

## Recommended Data Module Set

| Info code | Data module purpose | Suggested filename |
|---:|---|---|
| 040 | Heating Software Configuration and Control Data — Description | `DMC-AMPEL360E-EWTW-021-040-14A-040A-D_Heating-Software-Configuration-and-Control-Data-Description.xml` |
| 100 | Heating Software Configuration and Control Data — Operation | `DMC-AMPEL360E-EWTW-021-040-14A-100A-D_Heating-Software-Configuration-and-Control-Data-Operation.xml` |
| 300 | Heating Software Configuration and Control Data — Inspection | `DMC-AMPEL360E-EWTW-021-040-14A-300A-D_Heating-Software-Configuration-and-Control-Data-Inspection.xml` |
| 320 | Heating Software Configuration and Control Data — Functional Test | `DMC-AMPEL360E-EWTW-021-040-14A-320A-D_Heating-Software-Configuration-and-Control-Data-Functional-Test.xml` |
| 400 | Heating Software Configuration and Control Data — Fault Reporting | `DMC-AMPEL360E-EWTW-021-040-14A-400A-D_Heating-Software-Configuration-and-Control-Data-Fault-Reporting.xml` |
| 420 | Heating Software Configuration and Control Data — Fault Isolation | `DMC-AMPEL360E-EWTW-021-040-14A-420A-D_Heating-Software-Configuration-and-Control-Data-Fault-Isolation.xml` |
| 720 | Heating Software Configuration and Control Data — Install Procedure | `DMC-AMPEL360E-EWTW-021-040-14A-720A-D_Heating-Software-Configuration-and-Control-Data-Install-Procedure.xml` |
| 940 | Heating Software Configuration and Control Data — Provisioning Data | `DMC-AMPEL360E-EWTW-021-040-14A-940A-D_Heating-Software-Configuration-and-Control-Data-Provisioning-Data.xml` |
| 941 | Heating Software Configuration and Control Data — Illustrated Parts Data | `DMC-AMPEL360E-EWTW-021-040-14A-941A-D_Heating-Software-Configuration-and-Control-Data-Illustrated-Parts-Data.xml` |
| C00 | Heating Software Configuration and Control Data — Software Data | `DMC-AMPEL360E-EWTW-021-040-14A-C00A-D_Heating-Software-Configuration-and-Control-Data-Software-Data.xml` |

## Technical Boundaries

### Included

- all mechanical and electrical elements of the Heating Software Configuration and Control Data assembly;
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
| S1000D group path | `S1000D-CSDB/DMC/DMC-AMPEL360E-EWTW-021-040/14A_Heating-Software-Configuration-and-Control-Data` |
| Parent DMC group | `DMC-AMPEL360E-EWTW-021-040-00A` |
| SNS | `021-040-14A` |
| ATA reference | `ATA 21-40` |
| DMC prefix | `DMC-AMPEL360E-EWTW-021-040-14A` |
| Primary lifecycle use | LC05 Detailed Design / LC06 Verification Planning / LC11 Operation / LC12 Maintenance Support |

## Review and Governance

> Programme-controlled scaffold. Content is subject to BREX, SNS, applicability, DMRL, and CCB freeze before controlled release.

> **To be reviewed by system expert.**
