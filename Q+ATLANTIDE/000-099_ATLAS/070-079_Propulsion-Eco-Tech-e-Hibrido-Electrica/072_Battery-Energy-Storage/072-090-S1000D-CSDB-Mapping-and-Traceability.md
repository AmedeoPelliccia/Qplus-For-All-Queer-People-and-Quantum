---
document_id: "QATL-ATLAS-1000-ATLAS-070-079-072-090"
register: ATLAS-1000
title: "S1000D CSDB Mapping and Traceability"
ata: "072"
sns: "072-090-00"
subsection: "072"
subsubject_code: "090"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HPC, Q-MECHANICS, Q-AIR, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0072-090"
---

# S1000D CSDB Mapping and Traceability

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: 072](https://img.shields.io/badge/ATA-072-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-brightgreen)

---

## §0 Hyperlink Policy
All hyperlinks in this document are **relative**. Absolute URLs are forbidden.

## §1 Purpose
This document provides the S1000D Data Module Code (DMC) mapping for all Battery Energy Storage (072) documents, defining the Common Source Database (CSDB) allocation, Business Rules Exchange (BREX) reference, and traceability between the ATLAS-1000 subsubject files and the S1000D publication set for the AMPEL360E eWTW.

## §2 Applicability
| Aircraft | Variant | MSN Range | Effectivity |
|---|---|---|---|
| AMPEL360E | eWTW | All | From EIS |

## §3 Functional Description ![DRAFT](https://img.shields.io/badge/-DRAFT-yellow)
The AMPEL360E eWTW technical publications are structured under S1000D Issue 5.0. The Battery Energy Storage subsystem (subsystem code `0072`) maps to the SNS (Standard Numbering System) range `0072-000` through `0072-090`. Data modules are allocated within the CSDB under CAGE code `AMPEL` and model identifier `360E-EWTW`.

The BREX data module `BREX-072-v1` governs the business rules applicable to all 072-series data modules, including applicability management, graphic standards, warning/caution format, and revision control. Data module requirements lists (DMRL) for 072 cover 30 planned data modules across the AMM (Aircraft Maintenance Manual), CMM (Component Maintenance Manual), and FIM (Fault Isolation Manual) publication types.

All ATLAS-1000 subsubject files (072-000 through 072-090) serve as source content for corresponding S1000D data modules. The `document_id` field in each file header provides the cross-reference key. Changes to ATLAS subsubject content shall be reflected in the corresponding CSDB data module at the next scheduled revision cycle.

## §4 S1000D DMC Allocation Table
| ATLAS File | SNS | DMC | Info Code | Title | Pub Type |
|---|---|---|---|---|---|
| 072-000 | 0072-000 | DMC-AMPEL360E-EWTW-0072-000-A-00A-A | 000 | Battery Energy Storage — General | AMM |
| 072-010 | 0072-010 | DMC-AMPEL360E-EWTW-0072-010-A-00A-A | 000 | Battery Cell and Module Design | AMM |
| 072-020 | 0072-020 | DMC-AMPEL360E-EWTW-0072-020-A-00A-A | 000 | Battery Pack Architecture | AMM |
| 072-030 | 0072-030 | DMC-AMPEL360E-EWTW-0072-030-A-00A-A | 000 | Battery Management System | AMM |
| 072-040 | 0072-040 | DMC-AMPEL360E-EWTW-0072-040-A-00A-A | 000 | Battery Thermal Management | AMM |
| 072-050 | 0072-050 | DMC-AMPEL360E-EWTW-0072-050-A-00A-A | 000 | HV Contactors and Protection | AMM |
| 072-060 | 0072-060 | DMC-AMPEL360E-EWTW-0072-060-A-00A-A | 000 | Battery State Estimation | AMM |
| 072-070 | 0072-070 | DMC-AMPEL360E-EWTW-0072-070-A-00A-A | 000 | Battery Safety and TR Protection | AMM |
| 072-080 | 0072-080 | DMC-AMPEL360E-EWTW-0072-080-A-00A-A | 000 | Battery Charging and Ground Support | AMM |
| 072-090 | 0072-090 | DMC-AMPEL360E-EWTW-0072-090-A-00A-A | 000 | S1000D CSDB Mapping | AMM |

## §5 DMRL Summary
| DM Ref | DMC | Info Code | Pub Type | Status |
|---|---|---|---|---|
| DM-072-AMM-001 | DMC-AMPEL360E-EWTW-0072-000-A-00A-A | 000 | AMM | Planned |
| DM-072-AMM-002 | DMC-AMPEL360E-EWTW-0072-010-A-00A-A | 000 | AMM | Planned |
| DM-072-AMM-003 | DMC-AMPEL360E-EWTW-0072-020-A-00A-A | 000 | AMM | Planned |
| DM-072-AMM-004 | DMC-AMPEL360E-EWTW-0072-030-A-00A-A | 000 | AMM | Planned |
| DM-072-AMM-005 | DMC-AMPEL360E-EWTW-0072-040-A-00A-A | 000 | AMM | Planned |
| DM-072-AMM-006 | DMC-AMPEL360E-EWTW-0072-050-A-00A-A | 000 | AMM | Planned |
| DM-072-AMM-007 | DMC-AMPEL360E-EWTW-0072-060-A-00A-A | 000 | AMM | Planned |
| DM-072-AMM-008 | DMC-AMPEL360E-EWTW-0072-070-A-00A-A | 000 | AMM | Planned |
| DM-072-AMM-009 | DMC-AMPEL360E-EWTW-0072-080-A-00A-A | 000 | AMM | Planned |
| DM-072-AMM-010 | DMC-AMPEL360E-EWTW-0072-090-A-00A-A | 000 | AMM | Planned |
| DM-072-CMM-001 | DMC-AMPEL360E-EWTW-0072-010-C-00A-A | 000 | CMM | Planned |
| DM-072-CMM-002 | DMC-AMPEL360E-EWTW-0072-030-C-00A-A | 000 | CMM | Planned |
| DM-072-CMM-003 | DMC-AMPEL360E-EWTW-0072-040-C-00A-A | 000 | CMM | Planned |
| DM-072-CMM-004 | DMC-AMPEL360E-EWTW-0072-050-C-00A-A | 000 | CMM | Planned |
| DM-072-CMM-005 | DMC-AMPEL360E-EWTW-0072-060-C-00A-A | 000 | CMM | Planned |
| DM-072-FIM-001 | DMC-AMPEL360E-EWTW-0072-030-F-00A-A | 000 | FIM | Planned |
| DM-072-FIM-002 | DMC-AMPEL360E-EWTW-0072-040-F-00A-A | 000 | FIM | Planned |
| DM-072-FIM-003 | DMC-AMPEL360E-EWTW-0072-050-F-00A-A | 000 | FIM | Planned |
| DM-072-FIM-004 | DMC-AMPEL360E-EWTW-0072-070-F-00A-A | 000 | FIM | Planned |
| DM-072-IPD-001 | DMC-AMPEL360E-EWTW-0072-000-P-00A-A | 000 | IPD | Planned |
| DM-072-IPD-002 | DMC-AMPEL360E-EWTW-0072-010-P-00A-A | 000 | IPD | Planned |
| DM-072-IPD-003 | DMC-AMPEL360E-EWTW-0072-020-P-00A-A | 000 | IPD | Planned |
| DM-072-IPD-004 | DMC-AMPEL360E-EWTW-0072-030-P-00A-A | 000 | IPD | Planned |
| DM-072-IPD-005 | DMC-AMPEL360E-EWTW-0072-040-P-00A-A | 000 | IPD | Planned |
| DM-072-IPD-006 | DMC-AMPEL360E-EWTW-0072-050-P-00A-A | 000 | IPD | Planned |
| DM-072-IPD-007 | DMC-AMPEL360E-EWTW-0072-060-P-00A-A | 000 | IPD | Planned |
| DM-072-IPD-008 | DMC-AMPEL360E-EWTW-0072-070-P-00A-A | 000 | IPD | Planned |
| DM-072-IPD-009 | DMC-AMPEL360E-EWTW-0072-080-P-00A-A | 000 | IPD | Planned |
| DM-072-CIR-001 | DMC-AMPEL360E-EWTW-0072-000-W-00A-A | 000 | WDM | Planned |
| DM-072-CIR-002 | DMC-AMPEL360E-EWTW-0072-050-W-00A-A | 000 | WDM | Planned |

**Total 072 DMRL: 30 data modules**

## §6 BREX Reference
| BREX ID | Version | Applicable DMs | Status |
|---|---|---|---|
| BREX-072-v1 | 1.0 | All DMC-AMPEL360E-EWTW-0072-* | Planned |

BREX-072-v1 inherits from the aircraft-level BREX `BREX-AMPEL360E-EWTW-MASTER-v1` and adds subsystem-specific rules for:
- Battery-specific warning/caution format (HV, H₂, cryogenic/thermal hazards)
- Applicability management for dual-pack (L/R) effectivity
- Graphic standards for HVDC schematic symbols
- Data module revision control linked to BMS software versions

## §7 Traceability Matrix
| ATLAS File | S1000D DMC | LRUs Covered | Open Issues |
|---|---|---|---|
| 072-000 | DMC-...-0072-000 | BPA-NMC-250-L/R, BMU × 2, MSD × 2, TMM × 2 | OI-072-000-001/002 |
| 072-010 | DMC-...-0072-010 | CELL-NMC811-100AH × 1344, MOD × 56, CSC × 56 | OI-072-010-001/002 |
| 072-020 | DMC-...-0072-020 | TRAY × 2, Busbars × 54, Contactors × 4, MSD × 2 | OI-072-020-001/002 |
| 072-030 | DMC-...-0072-030 | BMU-A, BMU-B, CCDL harness | OI-072-030-001/002 |
| 072-040 | DMC-...-0072-040 | Pump × 2, BTHX × 2, TCV × 2, Heater × 2 | OI-072-040-001/002 |
| 072-050 | DMC-...-0072-050 | Main Cont × 2, PC Cont × 2, MSD × 2, IRM × 2 | OI-072-050-001/002 |
| 072-060 | DMC-...-0072-060 | BMU (EKF host) × 2 | OI-072-060-001/002 |
| 072-070 | DMC-...-0072-070 | Novec Canister × 2, FSC × 1, Gas Sensors × 2 | OI-072-070-001/002 |
| 072-080 | DMC-...-0072-080 | DC Connector × 2, OBC × 1, Charge Contactor × 2 | OI-072-080-001/002 |
| 072-090 | DMC-...-0072-090 | — (traceability document) | — |

## §8 CSDB Configuration
| Parameter | Value |
|---|---|
| S1000D Issue | 5.0 |
| CAGE Code | AMPEL |
| Model Identifier | 360E-EWTW |
| SNS Range (072) | 0072-000 to 0072-090 |
| BREX | BREX-072-v1 |
| CSDB instance | Q+ATLANTIDE CSDB (planned) |
| Language | en-US |

## §9 Operating Modes
| Mode | Description | Trigger | Notes |
|---|---|---|---|
| CSDB Authoring | Create/update DMs from ATLAS source | Scheduled revision | Controlled change process |
| CSDB Review | QA review of DM content and applicability | Per DM lifecycle | ATA Spec 2300 compliance |
| Publication Build | Compile IETP / PDF from CSDB | Release milestone | S1000D publication set |
| BREX Validation | Validate DMs against BREX-072-v1 | Per commit | Automated CSDB validation |

## §10 Performance and Budgets ![DRAFT](https://img.shields.io/badge/-DRAFT-yellow)
| Parameter | Value | Status |
|---|---|---|
| Total DMs planned (072) | 30 | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| DMs created | 0 (CSDB not yet instantiated) | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| ATLAS source files | 10 (072-000 to 072-090) | ACTIVE |
| BREX compliance | Planned | ![TBD](https://img.shields.io/badge/-TBD-orange) |

## §11 Safety, Redundancy and Fault Tolerance
Not applicable — this document defines traceability records only and has no operational safety function.

## §12 Maintenance and Diagnostics
| Task | Interval | Tool | Reference |
|---|---|---|---|
| DMRL review and update | Per release cycle | CSDB authoring tool | Q+ATLANTIDE Config Mgmt Plan |
| BREX validation run | Per ATLAS commit | CSDB validation engine | BREX-072-v1 |
| Traceability matrix review | Per design change | Manual review | This document |

## §13 Footprint
| Metric | Value |
|---|---|
| ATLAS source files | 10 (072-000 to 072-090) |
| S1000D DMs planned | 30 |
| Publication types | AMM, CMM, FIM, IPD, WDM |
| BREX document | BREX-072-v1 |

## §14 Safety and Certification References
| Standard | Requirement | Applicability | Status | Notes |
|---|---|---|---|---|
| S1000D Issue 5.0 | Technical publications | All 072 DMs | Planned | Primary standard |
| ATA iSpec 2200 | ATA data set format | Legacy mapping | Planned | ATA chapter 72 |
| ASD SX000i | Integrated Logistic Support | ILS data product | Planned | S-Series compliance |

## §15 V&V Approach
| Phase | Method | Tool/Facility | Status |
|---|---|---|---|
| BREX validation | Automated schema + BREX check | CSDB tool | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| DMRL completeness check | Cross-check DMRL vs LRU list | Manual | ![TBD](https://img.shields.io/badge/-TBD-orange) |
| Publication build verification | Build IETP, verify all DMs render | CSDB publication tool | ![TBD](https://img.shields.io/badge/-TBD-orange) |

## §16 Glossary
| Term | Definition |
|---|---|
| AMM | Aircraft Maintenance Manual |
| BREX | Business Rules Exchange |
| CAGE | Commercial and Government Entity code |
| CMM | Component Maintenance Manual |
| CSDB | Common Source Database |
| DM | Data Module |
| DMC | Data Module Code |
| DMRL | Data Module Requirements List |
| FIM | Fault Isolation Manual |
| IETP | Interactive Electronic Technical Publication |
| IPD | Illustrated Parts Data |
| SNS | Standard Numbering System |
| WDM | Wiring Data Module |

## §17 Open Issues
| ID | Description | Owner | Priority | Status |
|---|---|---|---|---|
| OI-072-090-001 | Instantiate Q+ATLANTIDE CSDB instance; migrate ATLAS files to DMs | @copilot | High | Open |
| OI-072-090-002 | Finalise BREX-072-v1 rules with tech pubs team | @copilot | Medium | Open |

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
| 072-000 | Battery Energy Storage — General | [072-000-Battery-Energy-Storage-General.md](072-000-Battery-Energy-Storage-General.md) |
| 072-010 | Battery Cell and Module Design | [072-010-Battery-Cell-and-Module-Design.md](072-010-Battery-Cell-and-Module-Design.md) |
| 072-020 | Battery Pack Architecture | [072-020-Battery-Pack-Architecture.md](072-020-Battery-Pack-Architecture.md) |
| 072-030 | Battery Management System (BMS) | [072-030-Battery-Management-System-BMS.md](072-030-Battery-Management-System-BMS.md) |
| 072-040 | Battery Thermal Management | [072-040-Battery-Thermal-Management.md](072-040-Battery-Thermal-Management.md) |
| 072-050 | HV Contactors and Protection | [072-050-HV-Contactors-and-Protection.md](072-050-HV-Contactors-and-Protection.md) |
| 072-060 | Battery State Estimation | [072-060-Battery-State-Estimation.md](072-060-Battery-State-Estimation.md) |
| 072-070 | Battery Safety and Thermal Runaway Protection | [072-070-Battery-Safety-and-Thermal-Runaway-Protection.md](072-070-Battery-Safety-and-Thermal-Runaway-Protection.md) |
| 072-080 | Battery Charging and Ground Support | [072-080-Battery-Charging-and-Ground-Support.md](072-080-Battery-Charging-and-Ground-Support.md) |

## §20 Change Log
| Rev | Date | Author | Summary |
|---|---|---|---|
| 0.1 | 2026-05-12 | @copilot | Initial creation |
