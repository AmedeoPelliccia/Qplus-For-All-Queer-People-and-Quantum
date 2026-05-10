---
document_id: DMC-AMPEL360E-EWTW-021-040-09A-GROUP-README
title: "DMC Group — DMC-AMPEL360E-EWTW-021-040-09A"
programme: "AMPEL360e Wide Tube-and-Wing Family"
short_code: "eWTW"
system: "021 — Conditioning and Pressurization"
sub_system: "021-040 — Heating Subsystem"
component: "Heating Control Valves and Airflow Interfaces"
sns: "021-040-09A"
ata_reference: "ATA 21-40"
model_ident_code: "AMPEL360E"
system_diff_code: "EWTW"
system_code: "021"
sub_system_code: "0"
sub_sub_system_code: "40"
assy_code: "09A"
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

# DMC Group: DMC-AMPEL360E-EWTW-021-040-09A

## Identification

**Programme:** AMPEL360e Wide Tube-and-Wing Family  
**Short code:** eWTW  
**System:** 021 — Conditioning and Pressurization  
**Sub-system:** 021-040 — Heating Subsystem  
**Component:** Heating Control Valves and Airflow Interfaces  
**SNS node:** 021-040-09A  
**ATA reference:** ATA 21-40  
**DMC group:** DMC-AMPEL360E-EWTW-021-040-09A  

## Purpose

This DMC group contains the S1000D/CSDB scaffold for the **021-040 / 09A Heating Control Valves and Airflow Interfaces** node of the AMPEL360e eWTW Heating Subsystem.

The group covers design description, operation, maintenance, inspection, fault isolation, removal/installation, and illustrated parts data for the Heating Control Valves and Airflow Interfaces within the ATA 21-40 Heating Subsystem.

## System Scope

The Heating Control Valves and Airflow Interfaces is a constituent of the AMPEL360e eWTW Heating Subsystem (ATA 21-40). Its main functions include:

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
| `700_assemble-install-and-connect-procedures/` | 720 | assemble, install and connect procedures |
| `940_provisioning-data/` | 940 | provisioning data |
| `941_illustrated-parts-data/` | 941 | illustrated parts data |

## Recommended Data Module Set

| Info code | Data module purpose | Suggested filename |
|---:|---|---|
| 040 | Heating Control Valves and Airflow Interfaces — Description | `DMC-AMPEL360E-EWTW-021-040-09A-040A-D_Heating-Control-Valves-and-Airflow-Interfaces-Description.xml` |
| 300 | Heating Control Valves and Airflow Interfaces — Inspection | `DMC-AMPEL360E-EWTW-021-040-09A-300A-D_Heating-Control-Valves-and-Airflow-Interfaces-Inspection.xml` |
| 310 | Heating Control Valves and Airflow Interfaces — Operational Check | `DMC-AMPEL360E-EWTW-021-040-09A-310A-D_Heating-Control-Valves-and-Airflow-Interfaces-Operational-Check.xml` |
| 400 | Heating Control Valves and Airflow Interfaces — Fault Reporting | `DMC-AMPEL360E-EWTW-021-040-09A-400A-D_Heating-Control-Valves-and-Airflow-Interfaces-Fault-Reporting.xml` |
| 420 | Heating Control Valves and Airflow Interfaces — Fault Isolation | `DMC-AMPEL360E-EWTW-021-040-09A-420A-D_Heating-Control-Valves-and-Airflow-Interfaces-Fault-Isolation.xml` |
| 520 | Heating Control Valves and Airflow Interfaces — Remove Procedure | `DMC-AMPEL360E-EWTW-021-040-09A-520A-D_Heating-Control-Valves-and-Airflow-Interfaces-Remove-Procedure.xml` |
| 720 | Heating Control Valves and Airflow Interfaces — Install Procedure | `DMC-AMPEL360E-EWTW-021-040-09A-720A-D_Heating-Control-Valves-and-Airflow-Interfaces-Install-Procedure.xml` |
| 940 | Heating Control Valves and Airflow Interfaces — Provisioning Data | `DMC-AMPEL360E-EWTW-021-040-09A-940A-D_Heating-Control-Valves-and-Airflow-Interfaces-Provisioning-Data.xml` |
| 941 | Heating Control Valves and Airflow Interfaces — Illustrated Parts Data | `DMC-AMPEL360E-EWTW-021-040-09A-941A-D_Heating-Control-Valves-and-Airflow-Interfaces-Illustrated-Parts-Data.xml` |

## Technical Boundaries

### Included

- all mechanical and electrical elements of the Heating Control Valves and Airflow Interfaces assembly;
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
| S1000D group path | `S1000D-CSDB/DMC/DMC-AMPEL360E-EWTW-021-040/09A_Heating-Control-Valves-and-Airflow-Interfaces` |
| Parent DMC group | `DMC-AMPEL360E-EWTW-021-040-00A` |
| SNS | `021-040-09A` |
| ATA reference | `ATA 21-40` |
| DMC prefix | `DMC-AMPEL360E-EWTW-021-040-09A` |
| Primary lifecycle use | LC05 Detailed Design / LC06 Verification Planning / LC11 Operation / LC12 Maintenance Support |

## Review and Governance

> Programme-controlled scaffold. Content is subject to BREX, SNS, applicability, DMRL, and CCB freeze before controlled release.

> **To be reviewed by system expert.**
