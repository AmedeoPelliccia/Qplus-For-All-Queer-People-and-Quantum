---
document_id: DMC-AMPEL360E-EWTW-021-010-00A-GROUP-README
title: "DMC Group — DMC-AMPEL360E-EWTW-021-010-00A"
programme: "AMPEL360e Wide Tube-and-Wing Family"
short_code: "eWTW"
system: "021 — Conditioning and Pressurization"
sub_system: "021-010 — Compression Subsystem"
component: "Compression Subsystem — General"
sns: "021-010-00A"
ata_reference: "ATA 21-10"
model_ident_code: "AMPEL360E"
system_diff_code: "EWTW"
system_code: "021"
sub_system_code: "0"
sub_sub_system_code: "10"
assy_code: "00A"
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
---

# DMC Group: DMC-AMPEL360E-EWTW-021-010-00A

<img width="1536" height="1024" alt="AMPEL360e EWTW 021-010 / 00A Compression Subsystem General — detailed ACM isometric technical illustration" src="https://github.com/user-attachments/assets/fc2d5c8c-283f-40a8-a0ff-3da359577f8b" />

***Figure 1 — Compression Subsystem General, detailed Air Cycle Machine internal view.***

## Identification

**Programme:** AMPEL360e Wide Tube-and-Wing Family  
**Short code:** eWTW  
**System:** 021 — Conditioning and Pressurization  
**Sub-system:** 021-010 — Compression Subsystem  
**Component:** Compression Subsystem — General  
**SNS node:** 021-010-00A  
**ATA reference:** ATA 21-10  
**DMC group:** DMC-AMPEL360E-EWTW-021-010-00A  

## Purpose

This DMC group contains the S1000D/CSDB scaffold for the **021-010 / 00A Compression Subsystem General** node of the AMPEL360e EWTW conditioning and pressurization system.

The group covers the descriptive, operational, test, fault isolation, and illustrated-parts data modules required to describe and support the compression subsystem at general assembly level.

## System Scope

The compression subsystem includes the controlled compression, conditioning, regulation, and delivery of air used by downstream aircraft systems, including:

- air conditioning packs;
- pressurization supply;
- anti-ice system interfaces, where applicable;
- system monitoring and diagnostic interfaces;
- maintenance and fault isolation data capture.

For the AMPEL360e EWTW configuration, the subsystem is treated as part of an electrically driven or electrically supported environmental control architecture, rather than a conventional engine-bleed-only architecture.

## Info-Code Folder Index

| Folder | Info Code(s) | Use |
|---|---:|---|
| `040_descriptive/` | 040 | System description / descriptive data module |
| `100_operation/` | 100 | Operation data module |
| `300_examinations-tests-and-checks/` | 300 | Inspection, operational checks, and functional tests |
| `400_fault-reports-and-isolation-procedures/` | 400 | Fault reporting and fault isolation procedures |
| `941_illustrated-parts-data/` | 941 | Illustrated parts data |

## Recommended Data Module Set

| Info code | Data module purpose | Suggested filename |
|---:|---|---|
| 040 | Compression subsystem general description | `DMC-AMPEL360E-EWTW-021-010-00A-040A-D_System-Description.xml` |
| 100 | Compression subsystem operation | `DMC-AMPEL360E-EWTW-021-010-00A-100A-D_Operation.xml` |
| 300 | Compression subsystem operational check | `DMC-AMPEL360E-EWTW-021-010-00A-300A-D_Operational-Check.xml` |
| 400 | Compression subsystem fault isolation | `DMC-AMPEL360E-EWTW-021-010-00A-400A-D_Fault-Isolation.xml` |
| 941 | Compression subsystem illustrated parts data | `DMC-AMPEL360E-EWTW-021-010-00A-941A-D_Illustrated-Parts-Data.xml` |

## Technical Boundaries

### Included

- compression subsystem general architecture;
- Air Cycle Machine general description;
- pressure regulation and shutoff interfaces;
- aftercooler interface;
- distribution manifold interface;
- control electronics interface;
- sensors, monitoring, and diagnostic interfaces;
- S1000D/CSDB traceability for the 021-010 / 00A node.

### Excluded

- downstream air distribution detailed routing;
- cabin temperature-control logic;
- full pressurization-control algorithms;
- detailed anti-ice system design;
- component-level repair procedures unless assigned by programme DMRL;
- supplier-controlled proprietary internal design data unless released to the CSDB baseline.

## Traceability

| Trace item | Value |
|---|---|
| ATLAS branch | `000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/021-Conditioning-and-Pressurization` |
| Programme path | `Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family` |
| S1000D group path | `S1000D-CSDB/DMC/DMC-AMPEL360E-EWTW-021-010/00A_Compression-Subsystem-General` |
| SNS | `021-010-00A` |
| DMC prefix | `DMC-AMPEL360E-EWTW-021-010-00A` |
| Primary lifecycle use | LC05 Detailed Design / LC06 Verification Planning / LC11 Operation / LC12 Maintenance Support |

## Governance Note

> Programme-controlled scaffold. Content is subject to BREX, SNS, applicability, DMRL, and CCB freeze before controlled release.
