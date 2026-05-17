---
document_id: "QATL-ATLAS-000099-ATLAS-030039-038-090"
title: "038-090 — S1000D CSDB Mapping and Traceability"
short_title: "S1000D CSDB Mapping and Traceability"
subsubject: "090"
subsubject_title: "S1000D CSDB Mapping and Traceability"
file_name: "038-090-S1000D-CSDB-Mapping-and-Traceability.md"
sns_reference: "038-09"
dmc_prefix: "DMC-<MODEL>-<SYSTEMDIFF>-038-09"
programme_link: "../../../../../<programme-implementation-branch>
register: "Q+ATLANTIDE"
register_link: "../../../../../Q+ATLANTIDE/"
architecture_band: "000-099_ATLAS"
architecture_band_link: "../../../"
architecture_band_title: "New Commercial Aircraft Architectures"
code_range: "030-039_Proteccion-y-Sistemas-Mecanicos"
code_range_link: "../../"
code_range_title: "Protección & Sistemas Mecánicos"
node_code: "038"
node_title: "Water and Waste"
node_link: "./"
parent_path: "Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/038_Water-and-Waste/"
parent_path_link: "./"
ata_reference: "ATA 38"
ata_reference_link: "#20-references"
s1000d_applicability: "S1000D-CSDB-compatible"
s1000d_link: "https://s1000d.org/"
domain: "A-Aerospace"
domain_link: "../../../../../IDEALE-ESG/A-Aerospace/"
primary_q_division: "Q-AIR"
primary_q_division_link: "../../../../../Q-Divisions/Q-AIR/"
support_q_divisions:
  - name: "Q-DATAGOV"
    link: "../../../../../Q-Divisions/Q-DATAGOV/"
  - name: "Q-DIGITAL"
    link: "../../../../../Q-Divisions/Q-DIGITAL/"
  - name: "Q-MECHANICS"
    link: "../../../../../Q-Divisions/Q-MECHANICS/"
orb_functions:
  - name: "ORB-PMO"
    link: "../../../../../ORB-Functions/ORB-PMO/"
  - name: "ORB-LEG"
    link: "../../../../../ORB-Functions/ORB-LEG/"
classification: "open-technical-scaffold"
status: "programme-controlled-scaffold"
scope: agnostic-standard
revision: "0.1.0"
created: "2026-05-10"
updated: "2026-05-10"
authoring_mode: "deterministic-technical-publication"
review_status: "to-be-reviewed-by-system-expert"
lifecycle_phase:
  - code: "LC02"
    title: "Requirements Definition"
  - code: "LC03"
    title: "Architecture Definition"
  - code: "LC05"
    title: "Detailed Design"
  - code: "LC06"
    title: "Verification Planning"
  - code: "LC10"
    title: "Certification / Approval"
  - code: "LC11"
    title: "Operation"
  - code: "LC12"
    title: "Maintenance / Support"
traceability:
  atlas_node: "038_Water-and-Waste"
  atlas_node_link: "./"
  parent_branch: "030-039_Proteccion-y-Sistemas-Mecanicos"
  parent_branch_link: "../../"
  csdb_path: "TBD"
  evidence_status: "draft"
  brex_status: "not-yet-validated"
  dmrl_status: "not-yet-frozen"
keywords:
  - "Q+ATLANTIDE"
  - "ATLAS"
  - "AMPEL360e"
  - "S1000D"
  - "ATA 38"
  - "Water and Waste"
  - "CSDB"
  - "DMRL"
  - "DMC"
  - "info code"
  - "traceability"
  - "AMM"
  - "IPC"
  - "BREX"
  - "data module"
---

# 038-090 — S1000D CSDB Mapping and Traceability
### <PROGRAMME> · ATA 38 · Q+ATLANTIDE ATLAS Scaffold

**Status:** <img src="https://img.shields.io/badge/DRAFT-yellow">  
**Revision:** 0.1.0 — 2026-05-10  
**Classification:** Q-AIR Primary | Q-DATAGOV / Q-DIGITAL / Q-MECHANICS Support

---

## §0 Hyperlink Policy

All cross-references within this document use relative Markdown links anchored to section headings within the Q+ATLANTIDE ATLAS repository. External regulatory references are cited by document identifier only. Internal DMC cross-references follow the pattern `DMC-<MODEL>-<SYSTEMDIFF>-038-NN-NNA-XXXXA-A`. Where a parameter is not yet determined, the badge <img src="https://img.shields.io/badge/TBD-red"> is used inline.

---

## §1 Purpose

This document defines the **S1000D CSDB Mapping and Traceability** for ATA 38 Water and Waste on the **<PROGRAMME>**. It provides:

1. Data Module Requirements List (DMRL): all 10 ATA 38 subsubjects × applicable info codes; estimated total DM count.
2. Info code definitions: the S1000D info codes used for ATA 38 documentation.
3. CSDB structure: SNS coding, BREX/DMRL status, CSDB address.
4. AMM chapter list: correspondence between ATA 38 subsubjects and AMM task numbers.
5. ATA 37 cross-references: boundary at EFV inlet; shared data modules.
6. Traceability matrix: ATLAS document → DMRL DM → AMM task → regulatory requirement.

---

> **Agnostic standard.** This file defines the S1000D/CSDB mapping rule for this ATLAS node. It does not instantiate programme-specific DMCs, model identifiers, or system-difference codes. Programme-specific content belongs in the programme implementation branch.

## §2 Applicability

| Item | Value |
|---|---|
| Aircraft Programme | <PROGRAMME> |
| Variant | All variants |
| ATA Chapter/Subsubject | 038-090 — S1000D CSDB Mapping and Traceability |
| Document Tier | Level 2 — SDD |
| Effectivity | MSN 0001 onwards <img src="https://img.shields.io/badge/TBD-red"> |
| Parent Document | [038-000](./038-000-Water-and-Waste-General.md) |
| S1000D Issue | 5.0 TBD <img src="https://img.shields.io/badge/TBD-red"> |
| CSDB Status | Not yet created <img src="https://img.shields.io/badge/TBD-red"> |

---

## §3 System/Function Overview

### 3.1 S1000D Documentation Framework

The <PROGRAMME> uses S1000D Issue TBD for all technical publications. ATA 38 documentation is structured as follows:

| Publication | ATA 38 Content | S1000D Pub Module |
|---|---|---|
| Aircraft Maintenance Manual (AMM) | All ATA 38 maintenance tasks (remove, install, test, service) | ATA 38 AMM publication module |
| Illustrated Parts Catalog (IPC) | All ATA 38 line-replaceable units and parts | ATA 38 IPC publication module |
| System Description Document (SDD) | System description DMs (info code 040) | ATA 38 SDD publication module |
| Fault Isolation Manual (FIM) | Fault isolation DMs (info code 400) | ATA 38 FIM publication module |
| Component Maintenance Manual (CMM) | Shop-level tasks for ATA 38 LRUs | Vendor-supplied TBD |
| Wiring Diagram Manual (WDM) | Electrical schematics for ATA 38 | ATA 38 WDM publication module |

### 3.2 SNS Reference Structure

| Level | Pattern | Example |
|---|---|---|
| System | ATA 38 | Water and Waste |
| Subsystem | ATA 38-0X | 038-00 to 038-09 |
| Sub-subsystem | ATA 38-0X0 | 038-000 to 038-090 |
| S1000D SNS | 038-0X-00A | 038-07-10A (fill servicing) |

DMC pattern: `DMC-<MODEL>-<SYSTEMDIFF>-038-NN-NNA-XXXXA-A`

Where:
- `038` = ATA chapter
- `NN` = subsubject (00–09)
- `NNA` = sub-subsubject + variant (00A = first variant)
- `XXXX` = info code (4 characters)
- `A` = language/country code
- `A` = issue number

---

## §4 Scope

### 4.1 In-Scope

- DMRL table for all 10 ATA 38 subsubjects
- Info code list and definitions
- Total DM count estimate per subsubject
- AMM chapter / task number list
- ATA 37 cross-reference DMCs
- CSDB address, BREX, DMRL status fields
- Traceability: ATLAS doc → DM → AMM task → certification requirement

### 4.2 Out-of-Scope

- Content of individual data modules (written as separate CSDB documents)
- CSDB database administration: → Q-DATAGOV
- S1000D BREX development: → Q-DATAGOV / Q-DIGITAL
- Vendor CMMs: → individual suppliers

---

## §5 Architecture Description

### 5.1 ATA 38 Document Hierarchy

```
ATA 38 Water and Waste
│
├── 038-000  General ─────────────────────► SDD (040) + WDM refs
│
├── 038-010  Potable Water System ─────────► SDD + AMM (300/300) + IPC + FIM
│
├── 038-020  Water Storage and Distribution ► SDD + AMM (300/300) + IPC + FIM
│
├── 038-030  Water Heaters & Service I/F ──► SDD + AMM (300/300) + IPC + FIM
│
├── 038-040  Waste Water Drainage ─────────► SDD + AMM (300/300) + IPC + FIM
│
├── 038-050  Toilet & Vacuum Waste System ─► SDD + AMM (300/300) + IPC + FIM
│
├── 038-060  Indication and Warning ───────► SDD + FIM + CMC listing (720)
│
├── 038-070  Servicing & Ground I/F ───────► SDD + Servicing (910) + AMM
│
├── 038-080  Monitoring, Diag & Control ──► SDD + BITE (300) + FIM + CMC (720)
│
└── 038-090  S1000D CSDB Mapping ──────────► DMRL + Traceability (this document)

Cross-reference: ATA 37 Vacuum → EFV boundary DMC-<MODEL>-<SYSTEMDIFF>-037-038-00A-040A-A TBD
```

---

## §6 Functional Breakdown

### 6.1 Info Code Definitions Used in ATA 38

| Info Code | S1000D Type | Description | Used in ATA 38 |
|---|---|---|---|
| 040 | Descriptive | System description | All subsubjects |
| 300 | Procedural | Maintenance procedure (test, inspect, check) | 010–080 |
| 400 | Fault | Fault isolation | 000, 010, 020, 030, 040, 050, 060, 080 |
| 520 | Parts | IPD (Illustrated Parts Data) | 010–070 |
| 720 | CMC/OMS data | Onboard maintenance system data listing | 060, 080 |
| 810 | Wiring | Wiring data | 010, 020, 030, 040, 050, 060, 080 |
| 910 | Servicing | Servicing procedure | 020, 070 |
| 941 | External | CSDB administration data | 090 |

### 6.2 DMRL — Data Module Requirements List

**Estimated total DM count: 46–62 DMs** (TBD pending DMRL freeze — Q-DATAGOV).

| Subsubject | ATLAS Document | Estimated DMs | Info Codes Covered | DMRL Status |
|---|---|---|---|---|
| 038-000 | [038-000-Water-and-Waste-General.md](./038-000-Water-and-Waste-General.md) | 4–6 | 040, 400, 810, 941 | <img src="https://img.shields.io/badge/TBD-red"> |
| 038-010 | [038-010-Potable-Water-System.md](./038-010-Potable-Water-System.md) | 5–7 | 040, 300, 400, 520, 810 | <img src="https://img.shields.io/badge/TBD-red"> |
| 038-020 | [038-020-Water-Storage-and-Distribution.md](./038-020-Water-Storage-and-Distribution.md) | 5–7 | 040, 300, 400, 520, 810, 910 | <img src="https://img.shields.io/badge/TBD-red"> |
| 038-030 | [038-030-Water-Heaters-and-Service-Interfaces.md](./038-030-Water-Heaters-and-Service-Interfaces.md) | 5–6 | 040, 300, 400, 520, 810 | <img src="https://img.shields.io/badge/TBD-red"> |
| 038-040 | [038-040-Waste-Water-Drainage.md](./038-040-Waste-Water-Drainage.md) | 4–6 | 040, 300, 400, 520, 810 | <img src="https://img.shields.io/badge/TBD-red"> |
| 038-050 | [038-050-Toilet-and-Vacuum-Waste-System.md](./038-050-Toilet-and-Vacuum-Waste-System.md) | 6–8 | 040, 300, 400, 520, 810 | <img src="https://img.shields.io/badge/TBD-red"> |
| 038-060 | [038-060-Water-and-Waste-Indication-and-Warning.md](./038-060-Water-and-Waste-Indication-and-Warning.md) | 4–5 | 040, 400, 720, 810 | <img src="https://img.shields.io/badge/TBD-red"> |
| 038-070 | [038-070-Water-and-Waste-Servicing-and-Ground-Interfaces.md](./038-070-Water-and-Waste-Servicing-and-Ground-Interfaces.md) | 5–7 | 040, 300, 520, 810, 910 | <img src="https://img.shields.io/badge/TBD-red"> |
| 038-080 | [038-080-Water-and-Waste-Monitoring-Diagnostics-and-Control-Interfaces.md](./038-080-Water-and-Waste-Monitoring-Diagnostics-and-Control-Interfaces.md) | 6–8 | 040, 300, 400, 720, 810 | <img src="https://img.shields.io/badge/TBD-red"> |
| 038-090 | [038-090-S1000D-CSDB-Mapping-and-Traceability.md](./038-090-S1000D-CSDB-Mapping-and-Traceability.md) | 2–2 | 040, 941 | <img src="https://img.shields.io/badge/TBD-red"> |
| **Total** | | **46–62 DMs** | | <img src="https://img.shields.io/badge/TBD-red"> |

### 6.3 Detailed DMRL — Per-Subsubject

#### 038-000 — General

| DMC | Title | Info Code | Priority | Status |
|---|---|---|---|---|
| DMC-<MODEL>-<SYSTEMDIFF>-038-00-00A-040A-A | ATA 38 Water and Waste — System Description | 040 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-00-00A-400A-A | ATA 38 Water and Waste — Fault Isolation | 400 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-00-00A-810A-A | ATA 38 Water and Waste — Wiring Diagram | 810 | Medium | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-00-00A-941A-A | ATA 38 DMRL and CSDB Mapping | 941 | Medium | <img src="https://img.shields.io/badge/DRAFT-yellow"> |

#### 038-010 — Potable Water System

| DMC | Title | Info Code | Priority | Status |
|---|---|---|---|---|
| DMC-<MODEL>-<SYSTEMDIFF>-038-01-00A-040A-A | Potable Water System — Description | 040 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-01-10A-300A-A | Potable Water System — EWP Removal/Installation | 300 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-01-20A-300A-A | UV Steriliser Unit — Removal/Installation | 300 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-01-00A-400A-A | Potable Water System — Fault Isolation | 400 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-01-00A-520A-A | Potable Water System — Illustrated Parts Data | 520 | Medium | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-01-00A-810A-A | Potable Water System — Wiring Diagram | 810 | Medium | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

#### 038-020 — Water Storage and Distribution

| DMC | Title | Info Code | Priority | Status |
|---|---|---|---|---|
| DMC-<MODEL>-<SYSTEMDIFF>-038-02-00A-040A-A | Water Storage and Distribution — Description | 040 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-02-10A-300A-A | Water Tank — Removal/Installation | 300 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-02-20A-300A-A | Water Distribution — Leak Check | 300 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-02-00A-400A-A | Water Storage — Fault Isolation | 400 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-02-00A-520A-A | Water Storage and Distribution — Illustrated Parts Data | 520 | Medium | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-02-10A-910A-A | Water Tank — Drain and Fill Servicing | 910 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

#### 038-030 — Water Heaters and Service Interfaces

| DMC | Title | Info Code | Priority | Status |
|---|---|---|---|---|
| DMC-<MODEL>-<SYSTEMDIFF>-038-03-00A-040A-A | Water Heaters — Description | 040 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-03-10A-300A-A | EWH — Removal/Installation | 300 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-03-20A-300A-A | TMV — Removal/Installation | 300 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-03-00A-400A-A | Water Heaters — Fault Isolation | 400 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-03-00A-520A-A | Water Heaters — Illustrated Parts Data | 520 | Medium | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

#### 038-040 — Waste Water Drainage

| DMC | Title | Info Code | Priority | Status |
|---|---|---|---|---|
| DMC-<MODEL>-<SYSTEMDIFF>-038-04-00A-040A-A | Waste Water Drainage — Description | 040 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-04-10A-300A-A | Mast Drain Nozzle — Removal/Installation | 300 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-04-00A-400A-A | Waste Water Drainage — Fault Isolation | 400 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-04-00A-520A-A | Waste Water Drainage — Illustrated Parts Data | 520 | Medium | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

#### 038-050 — Toilet and Vacuum Waste System

| DMC | Title | Info Code | Priority | Status |
|---|---|---|---|---|
| DMC-<MODEL>-<SYSTEMDIFF>-038-05-00A-040A-A | Toilet and Vacuum Waste System — Description | 040 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-05-10A-300A-A | EFV — Removal/Installation | 300 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-05-20A-300A-A | WIV — Removal/Installation | 300 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-05-30A-300A-A | Waste Tank — Removal/Installation | 300 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-05-00A-400A-A | Vacuum Waste System — Fault Isolation | 400 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-05-00A-520A-A | Vacuum Waste System — Illustrated Parts Data | 520 | Medium | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-05-00A-810A-A | Vacuum Waste System — Wiring Diagram | 810 | Medium | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

#### 038-060 — Indication and Warning

| DMC | Title | Info Code | Priority | Status |
|---|---|---|---|---|
| DMC-<MODEL>-<SYSTEMDIFF>-038-06-00A-040A-A | Indication and Warning — Description | 040 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-06-00A-400A-A | Indication and Warning — Fault Isolation | 400 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-06-00A-720A-A | CMC Parameter List — ATA 38 | 720 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-06-00A-810A-A | Indication and Warning — Wiring Diagram | 810 | Medium | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

#### 038-070 — Servicing and Ground Interfaces

| DMC | Title | Info Code | Priority | Status |
|---|---|---|---|---|
| DMC-<MODEL>-<SYSTEMDIFF>-038-07-00A-040A-A | Servicing and Ground Interfaces — Description | 040 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-07-10A-910A-A | Potable Water Fill — Servicing Procedure | 910 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-07-20A-910A-A | Waste Tank Drain — Servicing Procedure | 910 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-07-30A-300A-A | Water Quality Sample — Procedure | 300 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-07-40A-300A-A | UV Lamp Check — Procedure | 300 | Medium | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-07-00A-520A-A | Service Panel — Illustrated Parts Data | 520 | Medium | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

#### 038-080 — Monitoring, Diagnostics and Control Interfaces

| DMC | Title | Info Code | Priority | Status |
|---|---|---|---|---|
| DMC-<MODEL>-<SYSTEMDIFF>-038-08-00A-040A-A | Monitoring and Control — System Description | 040 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-08-10A-040A-A | BITE — Description | 040 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-08-10A-300A-A | BITE Power-Up — Procedure | 300 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-08-20A-040A-A | THC Freeze Protection — Description | 040 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-08-30A-300A-A | Maintenance Terminal Commands — Procedure | 300 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-08-00A-400A-A | Monitoring System — Fault Isolation | 400 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-08-40A-720A-A | CMC Parameter List — ATA 38 Monitoring | 720 | High | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

#### 038-090 — S1000D CSDB Mapping

| DMC | Title | Info Code | Priority | Status |
|---|---|---|---|---|
| DMC-<MODEL>-<SYSTEMDIFF>-038-09-00A-040A-A | S1000D CSDB Mapping — Description | 040 | Medium | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-09-00A-941A-A | ATA 38 DMRL — CSDB Administration | 941 | High | <img src="https://img.shields.io/badge/DRAFT-yellow"> |

---

## §7 System Context Diagram

```mermaid
flowchart LR
    ATLAS["Q+ATLANTIDE ATLAS\n(10 × 038-0XX.md)"]
    DMRL["DMRL\n(038-090)\n~46–62 DMs"]
    CSDB["CSDB\n(S1000D database\nTBD)"]
    AMM["AMM\n(ATA 38 tasks)"]
    IPC["IPC\n(ATA 38 parts)"]
    FIM["FIM\n(ATA 38 faults)"]
    CMC_PUB["CMC Data\n(720 DMs)"]
    ATA37["ATA 37\n(Vacuum)\ncross-refs"]
    REG["Regulatory\n(CS-25, WHO,\n14 CFR 121)"]
    CERT["Certification\nDossier"]

    ATLAS -->|"source"| DMRL
    DMRL -->|"populates"| CSDB
    CSDB --> AMM
    CSDB --> IPC
    CSDB --> FIM
    CSDB --> CMC_PUB
    DMRL -.->|"cross-ref"| ATA37
    AMM --> CERT
    REG --> CERT
```

---

## §8 Internal Functional Architecture

```mermaid
flowchart TB
    subgraph ATLAS_DOCS["Q+ATLANTIDE ATLAS (038-000 to 038-090)"]
        D000["038-000 General"]
        D010["038-010 Potable Water"]
        D020["038-020 Storage/Distrib"]
        D030["038-030 Heaters"]
        D040["038-040 Drainage"]
        D050["038-050 Vacuum Waste"]
        D060["038-060 Indication"]
        D070["038-070 Servicing"]
        D080["038-080 Monitoring"]
        D090["038-090 Mapping (this)"]
    end

    subgraph DMRL_SET["DMRL (§6.3)"]
        DM_040["040 Descriptions\n(10–12 DMs)"]
        DM_300["300 Procedures\n(12–14 DMs)"]
        DM_400["400 Fault Isolation\n(8–10 DMs)"]
        DM_520["520 IPD Parts\n(6–7 DMs)"]
        DM_720["720 CMC Data\n(2 DMs)"]
        DM_810["810 Wiring\n(5–6 DMs)"]
        DM_910["910 Servicing\n(3 DMs)"]
        DM_941["941 CSDB Admin\n(2 DMs)"]
    end

    ATLAS_DOCS --> DMRL_SET
    DMRL_SET -->|"loaded to CSDB"| CSDB_BOX["CSDB"]
```

---

## §9 Lifecycle Traceability

```mermaid
flowchart LR
    REQ["Requirements\n(CS-25, WHO/FAA water quality,\nS1000D documentation standard)"]
    SRD["System Requirements\nDocument"]
    SDD["SDD 038-090\nS1000D CSDB Mapping\nand Traceability"]
    DMRL_DOC["DMRL\n(this document §6.3)"]
    CSDB_POP["CSDB Population\n(all ATA 38 DMs)"]
    AMM_PUB["AMM Publication\n(ATA 38 chapters)"]
    CERT["Certification Dossier\n(ATA 38 compliance)"]
    EIS["Entry Into Service"]
    MOD["Modifications\n(revision control)"]

    REQ --> SRD --> SDD --> DMRL_DOC
    DMRL_DOC --> CSDB_POP --> AMM_PUB
    AMM_PUB --> CERT --> EIS --> MOD --> DMRL_DOC
```

---

## §10 Interfaces

| Interface | System | Direction | Medium | Notes |
|---|---|---|---|---|
| ATLAS document input | All 038-0XX ATLAS docs | In | Markdown / YAML | Source material for CSDB content |
| CSDB | S1000D CSDB system | Out | S1000D XML | Populated from DMRL |
| AMM publication | ATA 38 AMM module | Out | S1000D publication | Maintenance tasks |
| IPC publication | ATA 38 IPC module | Out | S1000D publication | Parts data |
| FIM publication | ATA 38 FIM module | Out | S1000D publication | Fault isolation |
| CMC data | ATA 38 720 DMs | Out | S1000D publication | Onboard maintenance |
| ATA 37 cross-reference | ATA 37 CSDB | Bi-directional | CSDB cross-reference | EFV boundary DMs |
| BREX | BREX document | In | S1000D BREX | Business rules for CSDB |

---

## §11 Operating Modes

| Mode | Description |
|---|---|
| DMRL Draft | DMRL under development; DM list TBD |
| DMRL Frozen | DMRL approved; no new DMs without change control |
| CSDB Population | DMs authored and loaded to CSDB |
| Publication Build | AMM/IPC/FIM publication modules built from CSDB |
| Revision | DM updated; revision level incremented; change log updated |

---

## §12 Monitoring and Diagnostics

| Metric | Tool | Target | Notes |
|---|---|---|---|
| DMRL completeness | Q-DATAGOV CSDB reports | 100% DMs assigned before EIS | TBD |
| DM authoring status | CSDB workflow status | 100% DMs in "reviewed" before EIS | TBD |
| BREX validation | CSDB BREX checker | 0 BREX errors | TBD |
| ATA 37 cross-reference validation | Cross-reference check tool | All xrefs resolve | TBD |

---

## §13 Maintenance Concept

S1000D data modules for ATA 38 are maintained in the CSDB. All changes follow the programme change control procedure. Key governance rules:

- DMRL changes require Q-DATAGOV / Q-AIR approval.
- DM revision level incremented for all substantive changes.
- Change log (§22 of each ATLAS document) maintained in parallel with CSDB revision history.
- BREX validation mandatory before DM approval.
- ATA 37 cross-reference DMCs must be validated against ATA 37 DMRL before approval.

---

## §14 S1000D/CSDB Mapping

This section is itself the CSDB mapping for ATA 38. The master DMRL is provided in §6.3.

| CSDB Administration DM | Status |
|---|---|
| DMC-<MODEL>-<SYSTEMDIFF>-038-09-00A-941A-A | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| DMC-<MODEL>-<SYSTEMDIFF>-038-09-00A-040A-A | <img src="https://img.shields.io/badge/DRAFT-yellow"> |

---

## §15 Footprints

| Parameter | Value |
|---|---|
| Total estimated ATA 38 DMs | 46–62 <img src="https://img.shields.io/badge/TBD-red"> |
| S1000D issue | TBD <img src="https://img.shields.io/badge/TBD-red"> |
| CSDB system | TBD <img src="https://img.shields.io/badge/TBD-red"> |
| BREX identifier | TBD <img src="https://img.shields.io/badge/TBD-red"> |
| AMM chapter count (ATA 38) | 10 subsubjects |
| ATA 37 cross-reference DMs | TBD <img src="https://img.shields.io/badge/TBD-red"> |

---

## §16 Safety and Certification

| Requirement | Standard | Application |
|---|---|---|
| Technical publication accuracy | CS-25.1529 | Instructions for Continued Airworthiness (ICA) |
| S1000D compliance | S1000D Issue TBD | All DMs must conform to S1000D specification |
| AMM task accuracy | CS-25.1529 + EASA Part 145 | All maintenance tasks must be validated against design |
| CSDB data integrity | Q-DATAGOV procedures | CSDB access control; revision control |
| Water quality procedure accuracy | WHO / 14 CFR Part 121 App A | Water servicing AMM tasks must support operator compliance |

---

## §17 Verification and Validation

| Test | Method | Acceptance Criterion | Status |
|---|---|---|---|
| EWP flow test | Bench/rig | ≥ TBD L/min | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Tank leak test | Hydrostatic 1.5× WP | No leakage TBD min | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| EWH thermal test | Bench | Outlet ≥ 60°C; TMV ≤ 43°C TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| UV steriliser output test | UV intensity + log-reduction | ≥ 4-log TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Mast heater continuity test | Resistance at install | Within tolerance | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Flush cycle test | Functional rig | Waste ≤ 1.5 s TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Fill-level sensor accuracy | Cal 0/50/100% | ± TBD % | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Overflow sensor function | Simulated overfill | Alert within TBD s | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Grey water drain flow test | Max load | Clear within TBD s | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Potable water quality test | Sample analysis | Meets WHO/FAA standard | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Freeze protection activation test | Cold chamber | THC/EMH activate; no freeze | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMRL completeness check | CSDB report | 100% DMs authored before EIS | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| BREX validation | CSDB BREX tool | 0 BREX errors | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| ATA 37 cross-reference validation | Cross-ref tool | All xrefs resolve | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §18 Glossary

| Term | Definition |
|---|---|
| PWS | Potable Water System |
| EWP | Electric Water Pump |
| EWH | Electric Water Heater |
| VWS | Vacuum Waste System |
| EFV | Electric Flush Valve |
| WIV | Waste Inlet Valve |
| Mast drain | Heated overboard grey drain nozzle |
| EMH | Electric Mast Heater |
| UV sterilisation | UV-C inline water treatment |
| Activated carbon filter | Filter at fill point |
| LLDPE | Linear Low-Density Polyethylene |
| PEX | Cross-linked Polyethylene |
| Capacitive level sensor | Non-contact fluid level sensor |
| NRV | Non-Return Valve |
| TMV | Thermostatic Mixing Valve |
| Grey water | Sink drainage |
| Black water | Toilet waste |
| Waste tank | Toilet waste storage vessel |
| Freeze protection | Trace/mast heating |
| Trace heating | Resistance elements on water lines |
| THC | Trace Heater Controller |
| CMC | Central Maintenance Computer |
| S1000D | International specification for technical publications |
| CSDB | Common Source DataBase — S1000D content repository |
| DMRL | Data Module Requirements List |
| DMC | Data Module Code |
| DM | Data Module |
| Info Code | S1000D category code defining content type (040, 300, 400, etc.) |
| SNS | Standard Numbering System |
| BREX | Business Rules eXchange — S1000D rule set |
| AMM | Aircraft Maintenance Manual |
| IPC | Illustrated Parts Catalog |
| FIM | Fault Isolation Manual |
| IPD | Illustrated Parts Data |
| ICA | Instructions for Continued Airworthiness |
| WDM | Wiring Diagram Manual |
| CMM | Component Maintenance Manual |

---

## §19 Citations

1. S1000D International Specification, Issue TBD. <https://s1000d.org/>
2. EASA CS-25.1529 — Instructions for Continued Airworthiness.
3. OI-038-009 — DMRL freeze pending open issues resolution.
4. [038-000 General](./038-000-Water-and-Waste-General.md).
5. [038-010 Potable Water](./038-010-Potable-Water-System.md).
6. [038-020 Storage](./038-020-Water-Storage-and-Distribution.md).
7. [038-030 Heaters](./038-030-Water-Heaters-and-Service-Interfaces.md).
8. [038-040 Drainage](./038-040-Waste-Water-Drainage.md).
9. [038-050 Vacuum Waste](./038-050-Toilet-and-Vacuum-Waste-System.md).
10. [038-060 Indication](./038-060-Water-and-Waste-Indication-and-Warning.md).
11. [038-070 Servicing](./038-070-Water-and-Waste-Servicing-and-Ground-Interfaces.md).
12. [038-080 Monitoring](./038-080-Water-and-Waste-Monitoring-Diagnostics-and-Control-Interfaces.md).

---

## §20 References

| Ref | Document | Notes |
|---|---|---|
| [R1] | S1000D Issue TBD | Technical publications specification |
| [R2] | CS-25.1529 | ICA |
| [R3] | EASA Part 145 | Maintenance organisation |
| [R4] | [038-000](./038-000-Water-and-Waste-General.md) | ATA 38 General |
| [R5] | ATA 37 DMRL TBD | Vacuum system cross-reference |
| [R6] | Q-DATAGOV CSDB procedures | CSDB administration |

---

## §21 Open Issues

| ID | Description | Owner | Status |
|---|---|---|---|
| OI-038-001 | Tank capacity and material | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-002 | Tank pressurisation method | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-003 | EWH count, placement, power budget | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-004 | Grey water retention regulatory review | Q-AIR / ORB-LEG | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-005 | Waste tank count and capacity | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-006 | Freeze protection strategy | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-007 | UV sterilisation certification and interval | Q-AIR / ORB-LEG | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-008 | Mast drain count and location | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-009 | Single-point servicing panel — DMRL freeze pending | Q-AIR / Q-DATAGOV | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §22 Change Log

| Revision | Date | Author | Description |
|---|---|---|---|
| 0.1.0 | 2026-05-10 | Q+ATLANTIDE ATLAS Working Group | Initial full-template draft; DMRL for all 10 subsubjects; ~46–62 DMs; info codes; AMM mapping; ATA 37 cross-refs; all 23 sections |
| 0.0.0 | 2026-05-10 | Q+ATLANTIDE ATLAS Working Group | Scaffold stub created |
