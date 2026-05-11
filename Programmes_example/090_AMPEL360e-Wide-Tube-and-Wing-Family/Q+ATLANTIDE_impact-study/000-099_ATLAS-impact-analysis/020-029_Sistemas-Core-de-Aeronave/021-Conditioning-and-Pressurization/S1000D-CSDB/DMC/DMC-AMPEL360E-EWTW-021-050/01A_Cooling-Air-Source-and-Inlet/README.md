---
document_id: DMC-AMPEL360E-EWTW-021-050-01A-GROUP-README
title: "DMC Group — DMC-AMPEL360E-EWTW-021-050-01A"
programme: "AMPEL360e Wide Tube-and-Wing Family"
short_code: "eWTW"
system: "021 — Conditioning and Pressurization"
sub_system: "021-050 — Cooling Subsystem"
component: "Cooling Air Source and Inlet"
sns: "021-050-01A"
ata_reference: "ATA 21-50"
model_ident_code: "AMPEL360E"
system_diff_code: "EWTW"
system_code: "021"
sub_system_code: "0"
sub_sub_system_code: "50"
assy_code: "01A"
item_location_code: "D"
status: "programme-controlled-scaffold-placeholder"
created: 2026-05-11
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

# DMC Group: DMC-AMPEL360E-EWTW-021-050-01A

## Identification

**Programme:** AMPEL360e Wide Tube-and-Wing Family  
**Short code:** eWTW  
**System:** 021 — Conditioning and Pressurization  
**Sub-system:** 021-050 — Cooling Subsystem  
**Component:** Cooling Air Source and Inlet  
**SNS node:** 021-050-01A  
**ATA reference:** ATA 21-50  
**DMC group:** DMC-AMPEL360E-EWTW-021-050-01A  

## Purpose

This DMC group contains the S1000D/CSDB scaffold for the **021-050 / 01A Cooling Air Source and Inlet** node of the AMPEL360e eWTW Cooling Subsystem.

The group covers design description, operation, maintenance, inspection, fault isolation, removal/installation, and illustrated parts data for the Cooling Air Source and Inlet within the ATA 21-50 Cooling Subsystem.

## System Scope

The Cooling Air Source and Inlet is a constituent of the AMPEL360e eWTW Cooling Subsystem (ATA 21-50). Its main functions include:

- provide or support the cooling function for the assigned zone or element;
- interface with cooling power supply, control, and overtemperature protection architecture;
- support maintenance, inspection, removal, and reinstallation activities;
- provide fault detection, isolation, and BITE interfaces where applicable.

## Info-Code Folder Index

| Folder | Info Code(s) | Use |
|---|---|---|
| `040_descriptive/` | 040A | descriptive |
| `300_examinations-tests-and-checks/` | 300A, 310A | examinations tests and checks |
| `400_fault-reports-and-isolation-procedures/` | 420A | fault reports and isolation procedures |
| `500_disconnect-remove-and-disassembly-procedures/` | 520A | disconnect remove and disassembly procedures |
| `700_assemble-install-and-connect-procedures/` | 720A | assemble install and connect procedures |
| `941_illustrated-parts-data/` | 941A | illustrated parts data |

## Recommended Data Module Set

| Info code | Data module purpose | Suggested filename |
|---:|---|---|
| 040A | Description | `DMC-AMPEL360E-EWTW-021-050-01A-040A-D_System-Description.xml` |
| 300A | General Inspection | `DMC-AMPEL360E-EWTW-021-050-01A-300A-D_General-Inspection.xml` |
| 310A | Operational Check | `DMC-AMPEL360E-EWTW-021-050-01A-310A-D_Operational-Check.xml` |
| 420A | Fault Isolation Procedure | `DMC-AMPEL360E-EWTW-021-050-01A-420A-D_Fault-Isolation-Procedure.xml` |
| 520A | Remove | `DMC-AMPEL360E-EWTW-021-050-01A-520A-D_Remove.xml` |
| 720A | Install | `DMC-AMPEL360E-EWTW-021-050-01A-720A-D_Install.xml` |
| 941A | Illustrated Parts Data | `DMC-AMPEL360E-EWTW-021-050-01A-941A-D_Illustrated-Parts-Data.xml` |

## Technical Boundaries

### Included

- all mechanical and electrical elements of the Cooling Air Source and Inlet assembly;
- electrical power supply and control interfaces within the component boundary;
- thermal and airflow interfaces within the cooling subsystem boundary;
- mounting hardware, fasteners, and structural attachment interfaces;
- sensor, limiter, and BITE interfaces associated with this component;
- wiring, connectors, and bonding interfaces within the component boundary;
- maintenance access panels and mounting interfaces directly associated with this component.

### Excluded

- elements assigned to adjacent cooling subsystem components;
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
| S1000D group path | `S1000D-CSDB/DMC/DMC-AMPEL360E-EWTW-021-050/01A_Cooling-Air-Source-and-Inlet` |
| Parent DMC group | `DMC-AMPEL360E-EWTW-021-050-01A` |
| SNS | `021-050-01A` |
| ATA reference | `ATA 21-50` |
| DMC prefix | `DMC-AMPEL360E-EWTW-021-050-01A` |
| Primary lifecycle use | LC05 Detailed Design / LC06 Verification Planning / LC11 Operation / LC12 Maintenance Support |

## Review and Governance

> Programme-controlled scaffold. Content is subject to BREX, SNS, applicability, DMRL, and CCB freeze before controlled release.

> **To be reviewed by system expert.**
