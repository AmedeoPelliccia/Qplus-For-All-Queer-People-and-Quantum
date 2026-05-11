---
document_id: DMC-AMPEL360E-EWTW-021-010-01A-GROUP-README
title: "DMC Group — DMC-AMPEL360E-EWTW-021-010-01A"
programme: "AMPEL360e Wide Tube-and-Wing Family"
short_code: "eWTW"
system: "021 — Conditioning and Pressurization"
sub_system: "021-010 — Compression Subsystem"
component: "Air Source and Compressor Inlet"
sns: "021-010-01A"
ata_reference: "ATA 21-10"
model_ident_code: "AMPEL360E"
system_diff_code: "EWTW"
system_code: "021"
sub_system_code: "0"
sub_sub_system_code: "10"
assy_code: "01A"
item_location_code: "D"
status: "programme-controlled-scaffold-placeholder"
created: 2026-05-09
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

# DMC Group: DMC-AMPEL360E-EWTW-021-010-01A

<img width="1536" height="1024" alt="AMPEL360e EWTW 021-010 / 01A Air Source and Compressor Inlet — isometric technical detail view" src="https://github.com/user-attachments/assets/92d2da83-b5b4-48f7-9fa6-8d9c963ba9f3" />

***Figure 1 — Air Source and Compressor Inlet detail view, showing the inlet assembly, ram-air path, protection screen, anti-ice interface, flow-control elements, sensor probes, and downstream ACM interface.***

<img width="1536" height="1024" alt="AMPEL360e EWTW 021-010 / 01A Air Source and Compressor Inlet — inlet assembly highlighted in green" src="https://github.com/user-attachments/assets/8721f963-a003-4396-9283-45a209c63899" />

***Figure 2 — DMC-AMPEL360E-EWTW-021-010-01A Air Source and Compressor Inlet. Detail view extracted from the 021-010 / 00A Compression Subsystem illustration, with the inlet assembly highlighted in green for component-location identification.***

## Identification

**Programme:** AMPEL360e Wide Tube-and-Wing Family  
**Short code:** eWTW  
**System:** 021 — Conditioning and Pressurization  
**Sub-system:** 021-010 — Compression Subsystem  
**Component:** Air Source and Compressor Inlet  
**SNS node:** 021-010-01A  
**ATA reference:** ATA 21-10  
**DMC group:** DMC-AMPEL360E-EWTW-021-010-01A  

## Purpose

This DMC group contains the S1000D/CSDB scaffold for the **021-010 / 01A Air Source and Compressor Inlet** node of the AMPEL360e EWTW compression subsystem.

The group covers the air-source interface, inlet geometry, ram-air capture path, inlet protection screen, anti-ice interface, flow-control elements, sensor probes, and downstream interface to the Air Cycle Machine.

## System Scope

The Air Source and Compressor Inlet sub-subsystem provides controlled inlet airflow to the compression subsystem. Its main functions are:

- capture and stabilize ram air before compressor entry;
- protect the compressor inlet against FOD ingestion;
- support anti-ice protection of inlet lip, cowl, and relevant inlet surfaces;
- provide flow-control interfaces for stable compressor operation;
- provide inlet pressure and temperature sensing;
- connect upstream air-source elements with the downstream ACM inlet interface.

## Info-Code Folder Index

| Folder | Info Code(s) | Use |
|---|---:|---|
| `040_descriptive/` | 040 | System description / descriptive data module |
| `300_examinations-tests-and-checks/` | 300, 310 | Inspection, operational checks, and functional tests |
| `400_fault-reports-and-isolation-procedures/` | 400, 420 | Fault reporting and fault isolation procedures |
| `500_disconnect-remove-and-disassembly-procedures/` | 520 | Disconnect, remove, and disassembly procedures |
| `700_assemble-install-and-connect-procedures/` | 720 | Assemble, install, and connect procedures |
| `941_illustrated-parts-data/` | 941 | Illustrated parts data |

## Recommended Data Module Set

| Info code | Data module purpose | Suggested filename |
|---:|---|---|
| 040 | Air source and compressor inlet description | `DMC-AMPEL360E-EWTW-021-010-01A-040A-D_System-Description.xml` |
| 300 | General inspection / examination | `DMC-AMPEL360E-EWTW-021-010-01A-300A-D_General-Inspection.xml` |
| 310 | Operational or functional check | `DMC-AMPEL360E-EWTW-021-010-01A-310A-D_Functional-Check.xml` |
| 400 | Fault isolation introduction | `DMC-AMPEL360E-EWTW-021-010-01A-400A-D_Fault-Isolation.xml` |
| 420 | Fault isolation procedure | `DMC-AMPEL360E-EWTW-021-010-01A-420A-D_Fault-Isolation-Procedure.xml` |
| 520 | Disconnect, remove, or disassemble procedure | `DMC-AMPEL360E-EWTW-021-010-01A-520A-D_Remove.xml` |
| 720 | Assemble, install, or connect procedure | `DMC-AMPEL360E-EWTW-021-010-01A-720A-D_Install.xml` |
| 941 | Illustrated parts data | `DMC-AMPEL360E-EWTW-021-010-01A-941A-D_Illustrated-Parts-Data.xml` |

## Technical Boundaries

### Included

- inlet cowl;
- inlet lip;
- inlet protection screen;
- ram-air capture path;
- inlet anti-ice interface;
- inlet bleed / extraction interface, where applicable;
- variable inlet guide vane interface;
- active flow-control valve interface;
- total pressure probe;
- inlet temperature probe;
- downstream ACM inlet interface;
- control, sensor, and diagnostic interfaces.

### Excluded

- internal ACM compressor rotor and turbine-stage details;
- aftercooler internal design;
- downstream distribution manifold;
- cabin temperature-control algorithms;
- pressurization-control algorithms;
- full anti-ice system architecture outside the inlet interface;
- supplier-controlled proprietary design data unless released to the CSDB baseline.

## Traceability

| Trace item | Value |
|---|---|
| ATLAS branch | `000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/021-Conditioning-and-Pressurization` |
| Programme path | `Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family` |
| S1000D group path | `S1000D-CSDB/DMC/DMC-AMPEL360E-EWTW-021-010/01A_Air-Source-and-Compressor-Inlet` |
| Parent DMC group | `DMC-AMPEL360E-EWTW-021-010-00A` |
| SNS | `021-010-01A` |
| ATA reference | `ATA 21-10` |
| DMC prefix | `DMC-AMPEL360E-EWTW-021-010-01A` |
| Primary lifecycle use | LC05 Detailed Design / LC06 Verification Planning / LC11 Operation / LC12 Maintenance Support |

## Review and Governance

> Programme-controlled scaffold. Content is subject to BREX, SNS, applicability, DMRL, and CCB freeze before controlled release.

> **To be reviewed by system expert.**
