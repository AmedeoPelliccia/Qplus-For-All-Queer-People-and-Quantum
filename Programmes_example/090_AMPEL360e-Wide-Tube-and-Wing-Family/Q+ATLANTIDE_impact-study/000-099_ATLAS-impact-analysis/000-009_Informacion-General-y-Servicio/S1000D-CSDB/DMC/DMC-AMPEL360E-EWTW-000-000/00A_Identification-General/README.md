---
document_id: DMC-AMPEL360E-EWTW-000-000-00A-GROUP-README
title: "DMC Group — DMC-AMPEL360E-EWTW-000-000-00A"
programme: "AMPEL360e Wide Tube-and-Wing Family"
short_code: "eWTW"
system: "000 — Identification"
sub_system: "000-000 — Identification General"
component: "Identification General"
sns: "000-000-00A"
ata_reference: "ATA 00-000"
model_ident_code: "AMPEL360E"
system_diff_code: "EWTW"
system_code: "000"
sub_system_code: "0"
sub_sub_system_code: "00"
assy_code: "00A"
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

# DMC Group: DMC-AMPEL360E-EWTW-000-000-00A

## Identification

**Programme:** AMPEL360e Wide Tube-and-Wing Family  
**Short code:** eWTW  
**System:** 000 — Identification  
**Sub-system:** 000-000 — Identification General  
**Component:** Identification General  
**SNS node:** 000-000-00A  
**ATA reference:** ATA 00-000  
**DMC group:** DMC-AMPEL360E-EWTW-000-000-00A  

## Purpose

This DMC group contains the S1000D/CSDB scaffold for the **000-000 / 00A Identification General** node of the AMPEL360e eWTW aircraft.

The group covers system description, identification use, identification checks, discrepancy and fault isolation, data module management, provisioning data, and illustrated identification data for the Identification General within the ATA 00-000 scope.

## System Scope

The Identification General component provides the top-level identification framework for the AMPEL360e eWTW aircraft. Its main functions include:

- provide overall aircraft identification data, model, and variant designation;
- support maintenance and operational use of aircraft identification markings and plates;
- enable identification checks for aircraft configuration traceability;
- provide discrepancy reporting and fault isolation baseline for identification elements;
- support provisioning and illustrated parts identification data.

## Info-Code Folder Index

| Folder | Info Code(s) | Use |
|---|---|---|
| `040_descriptive/` | 040A | system description / descriptive data module |
| `100_operation/` | 100A | operation / identification use |
| `300_examinations-tests-and-checks/` | 300A | identification checks |
| `400_fault-reports-and-isolation-procedures/` | 400A | discrepancy reporting and fault isolation |
| `900_data-module-management/` | 900A | data module management |
| `940_provisioning-data/` | 940A | provisioning data |
| `941_illustrated-parts-data/` | 941A | illustrated identification data |

## Recommended Data Module Set

| Info code | Data module purpose | Suggested filename |
|---:|---|---|
| 040A | System Description | `DMC-AMPEL360E-EWTW-000-000-00A-040A-D_System-Description.xml` |
| 100A | Identification Use | `DMC-AMPEL360E-EWTW-000-000-00A-100A-D_Identification-Use.xml` |
| 300A | Identification Check | `DMC-AMPEL360E-EWTW-000-000-00A-300A-D_Identification-Check.xml` |
| 400A | Identification Discrepancy and Fault Isolation | `DMC-AMPEL360E-EWTW-000-000-00A-400A-D_Identification-Discrepancy-Isolation.xml` |
| 900A | Identification Data Management | `DMC-AMPEL360E-EWTW-000-000-00A-900A-D_Identification-Data-Management.xml` |
| 940A | Provisioning Data | `DMC-AMPEL360E-EWTW-000-000-00A-940A-D_Provisioning-Data.xml` |
| 941A | Illustrated Identification Data | `DMC-AMPEL360E-EWTW-000-000-00A-941A-D_Illustrated-Identification-Data.xml` |

## Technical Boundaries

### Included

- all aircraft identification plates, labels, and markings within the identification boundary;
- model designation, serial number, and variant identification data;
- configuration identification and effectivity data;
- maintenance identification checks and traceability elements;
- provisioning baseline for identification hardware;
- illustrated parts data for identification components.

### Excluded

- system-level identification covered by individual ATA chapter identification modules;
- supplier-controlled proprietary identification data unless released to the CSDB baseline;
- ground support equipment identification not permanently installed on the aircraft;
- regulatory airworthiness certificates (covered by separate documentation streams).

## Traceability

| Trace item | Value |
|---|---|
| ATLAS branch | `000-099_ATLAS/000-009_Informacion-General-y-Servicio` |
| Programme path | `Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family` |
| S1000D group path | `S1000D-CSDB/DMC/DMC-AMPEL360E-EWTW-000-000/00A_Identification-General` |
| Parent DMC group | `DMC-AMPEL360E-EWTW-000-000-00A` |
| SNS | `000-000-00A` |
| ATA reference | `ATA 00-000` |
| DMC prefix | `DMC-AMPEL360E-EWTW-000-000-00A` |
| Primary lifecycle use | LC05 Detailed Design / LC06 Verification Planning / LC11 Operation / LC12 Maintenance Support |

## Review and Governance

> Programme-controlled scaffold. Content is subject to BREX, SNS, applicability, DMRL, and CCB freeze before controlled release.

> **To be reviewed by system expert.**
