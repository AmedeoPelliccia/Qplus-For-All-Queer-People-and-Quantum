---
document_id: DMC-AMPEL360E-EWTW-021-040-04A-GROUP-README
title: "DMC Group — DMC-AMPEL360E-EWTW-021-040-04A"
programme: "AMPEL360e Wide Tube-and-Wing Family"
short_code: "eWTW"
system: "021 — Conditioning and Pressurization"
sub_system: "021-040 — Heating Subsystem"
component: "Floor and Sidewall Heating Elements"
sns: "021-040-04A"
ata_reference: "ATA 21-40"
model_ident_code: "AMPEL360E"
system_diff_code: "EWTW"
system_code: "021"
sub_system_code: "0"
sub_sub_system_code: "40"
assy_code: "04A"
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

# DMC Group: DMC-AMPEL360E-EWTW-021-040-04A

## Identification

**Programme:** AMPEL360e Wide Tube-and-Wing Family  
**Short code:** eWTW  
**System:** 021 — Conditioning and Pressurization  
**Sub-system:** 021-040 — Heating Subsystem  
**Component:** Floor and Sidewall Heating Elements  
**SNS node:** 021-040-04A  
**ATA reference:** ATA 21-40  
**DMC group:** DMC-AMPEL360E-EWTW-021-040-04A  

## Purpose

This DMC group contains the S1000D/CSDB scaffold for the **021-040 / 04A Floor and Sidewall Heating Elements** node of the AMPEL360e eWTW Heating Subsystem.

The group covers design description, operation, maintenance, inspection, fault isolation, removal/installation, and illustrated parts data for the Floor and Sidewall Heating Elements within the ATA 21-40 Heating Subsystem.

## System Scope

The Floor and Sidewall Heating Elements is a constituent of the AMPEL360e eWTW Heating Subsystem (ATA 21-40). Its main functions include:

- provide or support the heating function for the assigned zone or element;
- interface with heating power supply, control, and overtemperature protection architecture;
- support maintenance, inspection, removal, and reinstallation activities;
- provide fault detection, isolation, and BITE interfaces where applicable.

## Info-Code Folder Index

| Folder | Info Code(s) | Use |
|---|---|---|
| `040_descriptive/` | 040 | system description / descriptive data module |
| `300_examinations-tests-and-checks/` | 300, 310 | inspection, examinations, tests and checks |
| `400_fault-reports-and-isolation-procedures/` | 400, 420 | fault reporting and fault isolation procedures |
| `500_disconnect-remove-and-disassembly-procedures/` | 520 | disconnect, remove and disassembly procedures |
| `600_repairs-and-locally-make-procedures-and-data/` | 600 | repairs and locally make procedures and data |
| `700_assemble-install-and-connect-procedures/` | 720 | assemble, install and connect procedures |
| `800_package-handling-storage-and-transportation/` | 800 | package, handling, storage and transportation procedures |
| `940_provisioning-data/` | 940 | provisioning data |
| `941_illustrated-parts-data/` | 941 | illustrated parts data |

## Recommended Data Module Set

| Info code | Data module purpose | Suggested filename |
|---:|---|---|
| 040 | Floor and Sidewall Heating Elements — Description | `DMC-AMPEL360E-EWTW-021-040-04A-040A-D_Floor-and-Sidewall-Heating-Elements-Description.xml` |
| 300 | Floor and Sidewall Heating Elements — Inspection | `DMC-AMPEL360E-EWTW-021-040-04A-300A-D_Floor-and-Sidewall-Heating-Elements-Inspection.xml` |
| 310 | Floor and Sidewall Heating Elements — Operational Check | `DMC-AMPEL360E-EWTW-021-040-04A-310A-D_Floor-and-Sidewall-Heating-Elements-Operational-Check.xml` |
| 400 | Floor and Sidewall Heating Elements — Fault Reporting | `DMC-AMPEL360E-EWTW-021-040-04A-400A-D_Floor-and-Sidewall-Heating-Elements-Fault-Reporting.xml` |
| 420 | Floor and Sidewall Heating Elements — Fault Isolation | `DMC-AMPEL360E-EWTW-021-040-04A-420A-D_Floor-and-Sidewall-Heating-Elements-Fault-Isolation.xml` |
| 520 | Floor and Sidewall Heating Elements — Remove Procedure | `DMC-AMPEL360E-EWTW-021-040-04A-520A-D_Floor-and-Sidewall-Heating-Elements-Remove-Procedure.xml` |
| 600 | Floor and Sidewall Heating Elements — Repair Data | `DMC-AMPEL360E-EWTW-021-040-04A-600A-D_Floor-and-Sidewall-Heating-Elements-Repair-Data.xml` |
| 720 | Floor and Sidewall Heating Elements — Install Procedure | `DMC-AMPEL360E-EWTW-021-040-04A-720A-D_Floor-and-Sidewall-Heating-Elements-Install-Procedure.xml` |
| 800 | Floor and Sidewall Heating Elements — Packaging Procedure | `DMC-AMPEL360E-EWTW-021-040-04A-800A-D_Floor-and-Sidewall-Heating-Elements-Packaging-Procedure.xml` |
| 940 | Floor and Sidewall Heating Elements — Provisioning Data | `DMC-AMPEL360E-EWTW-021-040-04A-940A-D_Floor-and-Sidewall-Heating-Elements-Provisioning-Data.xml` |
| 941 | Floor and Sidewall Heating Elements — Illustrated Parts Data | `DMC-AMPEL360E-EWTW-021-040-04A-941A-D_Floor-and-Sidewall-Heating-Elements-Illustrated-Parts-Data.xml` |

## Technical Boundaries

### Included

- all mechanical and electrical elements of the Floor and Sidewall Heating Elements assembly;
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
| S1000D group path | `S1000D-CSDB/DMC/DMC-AMPEL360E-EWTW-021-040/04A_Floor-and-Sidewall-Heating-Elements` |
| Parent DMC group | `DMC-AMPEL360E-EWTW-021-040-00A` |
| SNS | `021-040-04A` |
| ATA reference | `ATA 21-40` |
| DMC prefix | `DMC-AMPEL360E-EWTW-021-040-04A` |
| Primary lifecycle use | LC05 Detailed Design / LC06 Verification Planning / LC11 Operation / LC12 Maintenance Support |

## Review and Governance

> Programme-controlled scaffold. Content is subject to BREX, SNS, applicability, DMRL, and CCB freeze before controlled release.

> **To be reviewed by system expert.**
