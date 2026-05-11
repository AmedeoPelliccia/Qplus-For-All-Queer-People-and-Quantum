---
document_id: DMC-AMPEL360E-EWTW-021-050-14A-GROUP-README
title: "DMC Group — DMC-AMPEL360E-EWTW-021-050-14A"
programme: "AMPEL360e Wide Tube-and-Wing Family"
short_code: "eWTW"
system: "021 — Conditioning and Pressurization"
sub_system: "021-050 — Cooling Subsystem"
component: "Cooling Software Configuration and Control Data"
sns: "021-050-14A"
ata_reference: "ATA 21-50"
model_ident_code: "AMPEL360E"
system_diff_code: "EWTW"
system_code: "021"
sub_system_code: "0"
sub_sub_system_code: "50"
assy_code: "14A"
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

# DMC Group: DMC-AMPEL360E-EWTW-021-050-14A

## Identification

**Programme:** AMPEL360e Wide Tube-and-Wing Family  
**Short code:** eWTW  
**System:** 021 — Conditioning and Pressurization  
**Sub-system:** 021-050 — Cooling Subsystem  
**Component:** Cooling Software Configuration and Control Data  
**SNS node:** 021-050-14A  
**ATA reference:** ATA 21-50  
**DMC group:** DMC-AMPEL360E-EWTW-021-050-14A  

## Purpose

This DMC group contains the S1000D/CSDB scaffold for the **021-050 / 14A Cooling Software Configuration and Control Data** node of the AMPEL360e eWTW Cooling Subsystem.

The group covers design description, operation, maintenance, inspection, fault isolation, removal/installation, and illustrated parts data for the Cooling Software Configuration and Control Data within the ATA 21-50 Cooling Subsystem.

## System Scope

The Cooling Software Configuration and Control Data is a constituent of the AMPEL360e eWTW Cooling Subsystem (ATA 21-50). Its main functions include:

- provide or support the cooling function for the assigned zone or element;
- interface with cooling power supply, control, and overtemperature protection architecture;
- support maintenance, inspection, removal, and reinstallation activities;
- provide fault detection, isolation, and BITE interfaces where applicable.

## Info-Code Folder Index

| Folder | Info Code(s) | Use |
|---|---|---|
| `C00_computer-systems-software-and-data/` | C00A, C10A, C20A | computer systems software and data |

## Recommended Data Module Set

| Info code | Data module purpose | Suggested filename |
|---:|---|---|
| C00A | Computer System Description | `DMC-AMPEL360E-EWTW-021-050-14A-C00A-D_Computer-System-Description.xml` |
| C10A | Software Configuration Data | `DMC-AMPEL360E-EWTW-021-050-14A-C10A-D_Software-Configuration-Data.xml` |
| C20A | Diagnostic Data | `DMC-AMPEL360E-EWTW-021-050-14A-C20A-D_Diagnostic-Data.xml` |

## Technical Boundaries

### Included

- all mechanical and electrical elements of the Cooling Software Configuration and Control Data assembly;
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
| S1000D group path | `S1000D-CSDB/DMC/DMC-AMPEL360E-EWTW-021-050/14A_Cooling-Software-Configuration-and-Control-Data` |
| Parent DMC group | `DMC-AMPEL360E-EWTW-021-050-14A` |
| SNS | `021-050-14A` |
| ATA reference | `ATA 21-50` |
| DMC prefix | `DMC-AMPEL360E-EWTW-021-050-14A` |
| Primary lifecycle use | LC05 Detailed Design / LC06 Verification Planning / LC11 Operation / LC12 Maintenance Support |

## Review and Governance

> Programme-controlled scaffold. Content is subject to BREX, SNS, applicability, DMRL, and CCB freeze before controlled release.

> **To be reviewed by system expert.**
