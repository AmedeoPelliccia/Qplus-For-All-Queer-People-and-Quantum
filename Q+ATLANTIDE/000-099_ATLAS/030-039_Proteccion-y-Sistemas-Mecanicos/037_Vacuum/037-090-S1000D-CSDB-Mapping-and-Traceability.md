---
document_id: "QATL-ATLAS-000099-ATLAS-030039-037-090"
title: "037-090 — S1000D / CSDB Mapping and Traceability"
short_title: "S1000D CSDB Mapping"
subsubject: "090"
subsubject_title: "S1000D / CSDB Mapping and Traceability"
file_name: "037-090-S1000D-CSDB-Mapping-and-Traceability.md"
sns_reference: "037-90"
dmc_prefix: "DMC-<MODEL>-<SYSTEMDIFF>-037-90"
programme_link: "../../../../../<programme-implementation-branch>
register: "Q+ATLANTIDE ATLAS"
register_link: "../../../../../Q+ATLANTIDE/"
architecture_band: "030-039 Protection and Mechanical Systems"
architecture_band_link: "../../../"
architecture_band_title: "Protection and Mechanical Systems"
code_range: "037"
code_range_link: "../../"
code_range_title: "Vacuum"
node_code: "037"
node_title: "Vacuum"
node_link: "./"
parent_path: "Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/037_Vacuum/"
parent_path_link: "./"
ata_reference: "ATA 37"
ata_reference_link: "https://www.airlines.org/dataset/ata-spec-2200/"
s1000d_applicability: "S1000D Issue 5.0"
s1000d_link: "https://www.s1000d.org/"
domain: "Airworthiness / Aircraft Systems / Technical Publications"
domain_link: "https://www.easa.europa.eu/en/document-library/easy-access-rules/easy-access-rules-large-aeroplanes-cs-25"
primary_q_division: "Q-DIGITAL"
primary_q_division_link: "../../../../../Q-DIGITAL/"
support_q_divisions: ["Q-SYSTEMS", "Q-SAFETY", "Q-CERTIFICATION"]
orb_functions: ["FUNCTION-S1000D-MAPPING", "FUNCTION-DMRL", "FUNCTION-CSDB-TRACEABILITY", "FUNCTION-AMM"]
classification: "UNCLASSIFIED — ENGINEERING SCAFFOLD"
status: "DRAFT"
scope: agnostic-standard
revision: "0.1.0"
created: "2025-07-14"
updated: "2025-07-14"
authoring_mode: "AI-assisted scaffold"
review_status: "PENDING"
lifecycle_phase: "LC02 — System Definition"
traceability: ["CS-25.1438", "CS-25.1301", "CS-25.1309", "AMC 25.831", "S1000D Issue 5.0"]
keywords: ["ATA 37", "Vacuum", "S1000D", "CSDB", "DMRL", "data module", "traceability", "DMC", "SNS", "info code", "BREX", "AMM"]
---

# 037-090 — S1000D / CSDB Mapping and Traceability
### <PROGRAMME> · ATA 37 · Q+ATLANTIDE ATLAS Scaffold

**Status:** <img src="https://img.shields.io/badge/DRAFT-yellow">
**Revision:** 0.1.0 | **Created:** 2025-07-14 | **Updated:** 2025-07-14

---

## §0 Hyperlink Policy

All links in this document are relative within the Q+ATLANTIDE ATLAS repository unless explicitly marked as external. External links reference publicly available standards only. The S1000D standard link points to the public S1000D website. Internal cross-references use relative paths from the `037_Vacuum/` node.

---

## §1 Purpose

This document defines the **S1000D Data Module Requirements List (DMRL)** and **CSDB mapping** for the complete ATA 37 Vacuum chapter of the <PROGRAMME> aircraft. It provides traceability from the Q+ATLANTIDE ATLAS scaffold nodes (037-000 through 037-090) to the planned S1000D Data Modules (DMs) for the <PROGRAMME> Aircraft Maintenance Manual (AMM) CSDB volume.

**Key context:** ATA 37 on the <PROGRAMME-SHORT> is a **highly reduced chapter** compared to conventional aircraft. Estimated DM count: ~20–30 DMs (vs. ~60–80 for a conventional aircraft). The reduction is because:
- No engine vacuum pump DMs (no vacuum engine pump — electric EVG only)
- No gyroscopic instrument vacuum DMs (ADIRU solid-state — ATA 34)
- No vacuum autopilot servo DMs (FBW electric — ATA 22)
- No bleed-air venturi DMs (no bleed system — ATA 36)
- Only consumer is the vacuum waste toilet system (~3 toilets)

---

> **Agnostic standard.** This file defines the S1000D/CSDB mapping rule for this ATLAS node. It does not instantiate programme-specific DMCs, model identifiers, or system-difference codes. Programme-specific content belongs in the programme implementation branch.

## §2 Applicability

| Item | Value |
|------|-------|
| Aircraft Programme | <PROGRAMME> |
| ATA Chapter | 37 — Vacuum |
| Subsubject | 037-90 — S1000D / CSDB Mapping |
| S1000D Version | Issue 5.0 |
| CSDB Platform | <img src="https://img.shields.io/badge/TBD-red"> (CSDB path TBD) |
| BREX Document | <img src="https://img.shields.io/badge/TBD-red"> (<PROGRAMME-SHORT> BREX TBD) |
| DMRL Status | Not-yet-frozen |
| Publication | <PROGRAMME> AMM — Chapter 37 |
| Certification Basis | CS-25 Amendment 27 (TBD) |

---

## §3 System / Function Overview — DMRL Summary

### 3.1 Subsubject DMRL Overview

| SNS (ATA) | Subsubject Title | ATLAS Node | Planned DM Count | Info Codes Planned | DMRL Status |
|-----------|-----------------|------------|------------------|--------------------|-------------|
| 037-00 | Vacuum General | 037-000 | 2–3 | 040 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-10 | Vacuum Sources (EVG) | 037-010 | 4–6 | 040, 520, 720, 300 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-20 | Vacuum Distribution | 037-020 | 3–4 | 040, 300 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-30 | Regulation and Shutoff | 037-030 | 4–5 | 040, 520, 720, 300 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-40 | Pumps, Ejectors, Valves, Lines | 037-040 | 4–6 | 040, 520, 720, 300, 400 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-50 | Vacuum Consumers and Interfaces | 037-050 | 3–5 | 040, 300, 520, 720, 400 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-60 | Indication and Warning | 037-060 | 2–3 | 040, 300, 400 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-70 | Ground Service and Test | 037-070 | 5–7 | 040, 300, 400 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-80 | Monitoring and Diagnostics | 037-080 | 3–5 | 040, 300, 400 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-90 | S1000D / CSDB Mapping | 037-090 | 1 | 040 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| **TOTAL** | | | **~31–45 DMs** | | Not-yet-frozen |

> **Reduction note:** A conventional aircraft ATA 37 DMRL would contain ~60–80 DMs. The <PROGRAMME-SHORT> DMRL is approximately half that due to the elimination of vacuum gyro instruments and autopilot vacuum servos. If OI-037-002 resolves to **dry-flush toilets**, the DMRL count drops further to ~2–5 DMs (general description + confirmed eliminations only).

---

## §4 Scope

This document covers:
- DMRL for all 10 ATA 37 subsubjects (037-00 through 037-90)
- Individual planned DM list per subsubject with info codes
- S1000D DMC format specification for <PROGRAMME-SHORT> ATA 37
- CSDB path, BREX reference, publication structure
- Traceability from ATLAS scaffold to S1000D DMs
- Lifecycle traceability from requirements to DM authoring to certification
- V&V for S1000D/CSDB deliverables

---

## §5 Architecture Description — S1000D for ATA 37

### 5.1 DMC Format

All ATA 37 <PROGRAMME-SHORT> data modules follow this DMC format:

```
DMC-<MODEL>-<SYSTEMDIFF>-037-{NN}-{AA}-00{infoCode}{variant}-{lang}.xml
```

Where:
| Field | Description | Example |
|-------|-------------|---------|
| `<MODEL>-<SYSTEMDIFF>` | Model identification code | Fixed |
| `037` | System code (ATA 37 — Vacuum) | Fixed |
| `{NN}` | Subsubject (ATA subsubject, 2-digit) | `10`, `50`, `70` |
| `{AA}` | Sub-subsubject (00 for general, `A`–`Z` for variants) | `00` |
| `{infoCode}` | S1000D information code | `040`, `300`, `400`, `520`, `720` |
| `{variant}` | DM variant letter | `A` (primary), `B`, `C` as needed |
| `{lang}` | Language code | `A` (English) |

### 5.2 Information Code Reference

| Info Code | S1000D Type | Use in ATA 37 |
|-----------|-------------|---------------|
| 040 | Descriptive — system description and operation | System description DMs for all subsubjects |
| 300 | Procedures — inspection/check | Functional tests, inspections, VRV test, decay test |
| 400 | Fault isolation | EVG, EFV, SOV, transducer fault isolation |
| 520 | Removal | EVG, EFV, NRV, SOV, VRV, odour filter removal |
| 720 | Installation | EVG, EFV, NRV, SOV, VRV, odour filter installation |

### 5.3 CSDB Architecture

| CSDB Element | Value | Status |
|-------------|-------|--------|
| CSDB platform | <img src="https://img.shields.io/badge/TBD-red"> | Not selected |
| CSDB path | <img src="https://img.shields.io/badge/TBD-red"> | Not assigned |
| BREX document | <img src="https://img.shields.io/badge/TBD-red"> <PROGRAMME-SHORT>-BREX-001 TBD | Not frozen |
| Publication | <PROGRAMME> AMM — Chapter 37 | Planned |
| AMM format | S1000D Publication Module (PM) | Planned |
| Output formats | PDF, IETP (Interactive Electronic Technical Publication) TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

### 5.4 Reduced Chapter Rationale — Explicit Elimination Table

The following conventional ATA 37 DM categories are **explicitly eliminated** from the <PROGRAMME-SHORT> DMRL:

| Eliminated DM Category | Conventional ATA 37 Count (est.) | Reason Eliminated | <PROGRAMME-SHORT> Replacement |
|------------------------|----------------------------------|-------------------|-----------------|
| Engine vacuum pump removal/installation | 4–6 DMs | No engine vacuum pump | EVG (electric) |
| Vacuum pump inspection | 2–3 DMs | No engine vacuum pump | EVG BITE + CMC |
| Gyro instrument vacuum supply | 6–10 DMs | No vacuum gyros | ADIRU (ATA 34) |
| Autopilot vacuum servo supply | 4–6 DMs | No vacuum servos | FBW electric (ATA 22) |
| Vacuum regulator (engine-side) | 2–3 DMs | No engine vacuum | EVG controller |
| Bleed venturi vacuum | 2–4 DMs | No bleed system | N/A |
| **Total eliminated** | **~20–32 DMs** | | |

---

## §6 Functional Breakdown — Detailed DM Plan per Subsubject

### 6.1 SNS 037-00 — Vacuum General

| Planned DM Code | Info Code | Title | Priority | Status |
|----------------|-----------|-------|----------|--------|
| DMC-<MODEL>-<SYSTEMDIFF>-037-00-00-00A-040A-A | 040 | Vacuum System — General Description and Operation | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-00-00-00A-040B-A | 040 | Vacuum System — <PROGRAMME-SHORT> Design Philosophy and ATA 37 Scope Reduction | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

### 6.2 SNS 037-10 — Vacuum Sources (EVG)

| Planned DM Code | Info Code | Title | Priority | Status |
|----------------|-----------|-------|----------|--------|
| DMC-<MODEL>-<SYSTEMDIFF>-037-10-00-00A-040A-A | 040 | Electric Vacuum Generator (EVG) — Description and Operation | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-10-00-00A-300A-A | 300 | EVG — Functional Test | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-10-00-00A-520A-A | 520 | EVG — Removal | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-10-00-00A-720A-A | 720 | EVG — Installation | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-10-00-00A-400A-A | 400 | EVG — Fault Isolation | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

### 6.3 SNS 037-20 — Vacuum Distribution

| Planned DM Code | Info Code | Title | Priority | Status |
|----------------|-----------|-------|----------|--------|
| DMC-<MODEL>-<SYSTEMDIFF>-037-20-00-00A-040A-A | 040 | Vacuum Distribution Manifold — Description | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-20-00-00A-300A-A | 300 | Vacuum Manifold — Inspection and Leak Check | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-20-00-00A-300B-A | 300 | Vacuum Line — Inspection and Leak Test (Decay Method) | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

### 6.4 SNS 037-30 — Regulation and Shutoff

| Planned DM Code | Info Code | Title | Priority | Status |
|----------------|-----------|-------|----------|--------|
| DMC-<MODEL>-<SYSTEMDIFF>-037-30-00-00A-040A-A | 040 | Vacuum Relief Valve (VRV) — Description | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-30-00-00A-040B-A | 040 | Shutoff Valve (SOV) — Description | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-30-00-00A-300A-A | 300 | VRV — Pop-Test Procedure | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-30-00-00A-520A-A | 520 | VRV — Removal | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-30-00-00A-720A-A | 720 | VRV — Installation | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

### 6.5 SNS 037-40 — Pumps, Ejectors, Valves, and Lines

| Planned DM Code | Info Code | Title | Priority | Status |
|----------------|-----------|-------|----------|--------|
| DMC-<MODEL>-<SYSTEMDIFF>-037-40-00-00A-040A-A | 040 | Non-Return Valve (NRV) — Description | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-40-00-00A-300A-A | 300 | NRV — Inspection and Leak Test | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-40-00-00A-520A-A | 520 | NRV — Removal | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-40-00-00A-720A-A | 720 | NRV — Installation | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-40-00-00A-400A-A | 400 | Vacuum Line — Fault Isolation (leak, blockage) | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

### 6.6 SNS 037-50 — Vacuum Consumers and Interfaces

| Planned DM Code | Info Code | Title | Priority | Status |
|----------------|-----------|-------|----------|--------|
| DMC-<MODEL>-<SYSTEMDIFF>-037-50-00-00A-040A-A | 040 | Vacuum Consumers and System Interfaces — Description | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-50-00-00A-300A-A | 300 | EFV — Inspection | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-50-00-00A-520A-A | 520 | EFV — Removal | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-50-00-00A-720A-A | 720 | EFV — Installation | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-50-00-00A-400A-A | 400 | EFV — Fault Isolation | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

### 6.7 SNS 037-60 — Indication and Warning

| Planned DM Code | Info Code | Title | Priority | Status |
|----------------|-----------|-------|----------|--------|
| DMC-<MODEL>-<SYSTEMDIFF>-037-60-00-00A-040A-A | 040 | Vacuum Indication and Warning — Description | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-60-00-00A-300A-A | 300 | CAS Alert Functional Check | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-60-00-00A-400A-A | 400 | Vacuum CAS Alert — Fault Isolation | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

### 6.8 SNS 037-70 — Ground Service and Test

| Planned DM Code | Info Code | Title | Priority | Status |
|----------------|-----------|-------|----------|--------|
| DMC-<MODEL>-<SYSTEMDIFF>-037-70-00-00A-040A-A | 040 | Ground Service and Test — Description | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-70-00-00A-300A-A | 300 | Waste Drain and Line Rinse Procedure | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-70-00-00A-300B-A | 300 | Vacuum System Functional Test | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-70-00-00A-300C-A | 300 | VRV Pop-Test | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-70-00-00A-300D-A | 300 | Vacuum Decay Leak Test | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-70-00-00A-400A-A | 400 | Vacuum System Ground Fault Isolation | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

### 6.9 SNS 037-80 — Monitoring and Diagnostics

| Planned DM Code | Info Code | Title | Priority | Status |
|----------------|-----------|-------|----------|--------|
| DMC-<MODEL>-<SYSTEMDIFF>-037-80-00-00A-040A-A | 040 | Monitoring and Diagnostics — Description | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-80-00-00A-300A-A | 300 | CMC / OMS Monitoring Check | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-80-00-00A-400A-A | 400 | Fault Isolation — EVG Fault | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-80-00-00A-400B-A | 400 | Fault Isolation — EFV Fault | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMC-<MODEL>-<SYSTEMDIFF>-037-80-00-00A-400C-A | 400 | Fault Isolation — Transducer Fault | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

### 6.10 SNS 037-90 — S1000D / CSDB Mapping

| Planned DM Code | Info Code | Title | Priority | Status |
|----------------|-----------|-------|----------|--------|
| DMC-<MODEL>-<SYSTEMDIFF>-037-90-00-00A-040A-A | 040 | S1000D / CSDB Mapping and Traceability — Description | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §7 System Context Diagram

```mermaid
flowchart LR
    ATLAS[ATLAS Node 037\nQ+ATLANTIDE] --> DMRL[DMRL\nATA 37\n~31–45 DMs]
    DMRL --> DM00[SNS 037-00\n040 ×2]
    DMRL --> DM10[SNS 037-10\n040/300/520/720/400 ×5]
    DMRL --> DM20[SNS 037-20\n040/300 ×3]
    DMRL --> DM30[SNS 037-30\n040/300/520/720 ×5]
    DMRL --> DM40[SNS 037-40\n040/300/520/720/400 ×5]
    DMRL --> DM50[SNS 037-50\n040/300/520/720/400 ×5]
    DMRL --> DM60[SNS 037-60\n040/300/400 ×3]
    DMRL --> DM70[SNS 037-70\n040/300×4/400 ×6]
    DMRL --> DM80[SNS 037-80\n040/300/400×3 ×5]
    DMRL --> DM90[SNS 037-90\n040 ×1]

    DM00 & DM10 & DM20 & DM30 & DM40 --> CSDB[CSDB\nAMM Volume\nChapter 37]
    DM50 & DM60 & DM70 & DM80 & DM90 --> CSDB

    CSDB -->|BREX validation| BREX[<PROGRAMME-SHORT> BREX TBD]
    CSDB -->|Publication| AMM[<PROGRAMME>\nAMM Chapter 37\nPDF / IETP TBD]
    AMM -->|Certification evidence| CERT[CS-25 Certification\nCompliance]
```

---

## §8 Internal Functional Architecture

```mermaid
flowchart TB
    REQ[Regulatory Requirements\nCS-25.1438\nCS-25.1309\nAMC 25.831] --> ATLAS_SCAF[Q+ATLANTIDE ATLAS\nScaffold\n037-000 to 037-090]
    ATLAS_SCAF --> DMRL_AUTH[DMRL Authoring\nSNS assignment\nInfo code selection\nDM count estimate]
    DMRL_AUTH --> BREX_REF[BREX Reference\nprogramme BREX TBD]
    BREX_REF --> DM_AUTH[Data Module\nAuthoring\nXML S1000D\nper DM plan]
    DM_AUTH --> CSDB_ING[CSDB Ingestion\nDM validation\nCross-reference check]
    CSDB_ING --> BREX_VAL[BREX Validation\nAutomated check\nagainst <PROGRAMME-SHORT> BREX]
    BREX_VAL -->|Pass| PUB[Publication Build\nAMM Chapter 37\nPDF / IETP]
    BREX_VAL -->|Fail| DM_CORR[DM Correction\nand re-submission]
    DM_CORR --> CSDB_ING
    PUB --> CERT_EV[Certification Evidence\nMaintenance DM coverage\nCS-25.1309 compliance]
    CERT_EV --> CS25_CERT[CS-25\nType Certificate]
```

---

## §9 Lifecycle Traceability

```mermaid
flowchart LR
    LC01[LC01\nConcept\nATA 37 scope\ndecision] --> LC02[LC02\nRequirements\nCS-25\napplicability]
    LC02 --> LC03[LC03\nDMRL Freeze\nTarget: TBD date\nOI: DMRL freeze TBD]
    LC03 --> LC05[LC05\nDM Authoring\nXML production\nAll SNS 037-00\nto 037-90]
    LC05 --> LC06[LC06\nBREX Validation\nCSDB ingestion\nCross-reference\nchecks]
    LC06 --> LC08[LC08\nGround Test\nAMM procedure\nvalidation against\nactual system]
    LC08 --> LC09[LC09\nFlight Test\nAMM accuracy\ncheck]
    LC09 --> LC10[LC10\nCertification\nCS-25 compliance\nMaintenance\ndocumentation]
    LC10 --> LC11[LC11\nIn-Service\nAMM Chapter 37\nlive CSDB]
    LC11 --> LC12[LC12\nPost-Service\nRevision process\nCSDB update]
```

---

## §10 Interfaces

| Interface ID | System | Direction | Description | Status |
|-------------|--------|-----------|-------------|--------|
| IF-037-090-001 | CSDB platform | ATLAS → CSDB | DMRL ingested into CSDB; DMs authored in XML per DMC format | <img src="https://img.shields.io/badge/TBD-red"> |
| IF-037-090-002 | BREX | CSDB ↔ BREX | All DMs validated against <PROGRAMME-SHORT> BREX before publication | <img src="https://img.shields.io/badge/TBD-red"> |
| IF-037-090-003 | AMM Publication | CSDB → AMM | Chapter 37 published as AMM chapter from CSDB PM | <img src="https://img.shields.io/badge/TBD-red"> |
| IF-037-090-004 | Certification | AMM → EASA | AMM Chapter 37 DMs provided as maintenance documentation for TC | <img src="https://img.shields.io/badge/TBD-red"> |
| IF-037-090-005 | ATA 38 CSDB | Cross-reference | ATA 37 DMs cross-reference ATA 38 DMs (waste tank, drain valve) | <img src="https://img.shields.io/badge/TBD-red"> |
| IF-037-090-006 | ATA 45 CSDB | Cross-reference | ATA 37 FI DMs cross-reference ATA 45 CMC/OMS DMs | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §11 Operating Modes

> **Note:** This subsubject (037-90) is a documentation and traceability node — it does not define operational modes of the vacuum system. The following modes relate to the CSDB/DMRL workflow:

| Mode | Description | Status |
|------|-------------|--------|
| DMRL DRAFT | DMRL not frozen; DM count and codes subject to change | Current |
| DMRL FREEZE | DMRL frozen; no new DMs added without CCB approval | <img src="https://img.shields.io/badge/TBD-red"> |
| DM AUTHORING | Individual DMs being authored in XML per frozen DMRL | <img src="https://img.shields.io/badge/TBD-red"> |
| CSDB VALIDATION | DMs ingested into CSDB; BREX validation running | <img src="https://img.shields.io/badge/TBD-red"> |
| PUBLICATION | AMM Chapter 37 published and available | <img src="https://img.shields.io/badge/TBD-red"> |
| IN-SERVICE | AMM live; revision process operational | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §12 Monitoring and Diagnostics

### 12.1 DMRL Completeness Metrics

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Total planned DMs | ~31–45 | ~40 (this scaffold) | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| DMs with info code 040 (descriptive) | ≥1 per SNS | 10 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| DMs with info code 400 (FI) | ≥1 per LRU type | 5 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| DMs with info codes 520/720 (R/I) | Per each replaceable component | ~8 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| BREX validation pass rate | 100% | N/A (authoring not started) | <img src="https://img.shields.io/badge/TBD-red"> |
| Cross-reference integrity | 100% valid links | N/A | <img src="https://img.shields.io/badge/TBD-red"> |
| Coverage of open OIs | Tracked in §21 | 7 OIs + 4 DMRL OIs | Active |

---

## §13 Maintenance Concept

- **DMRL maintenance:** DMRL is a living document until freeze date (TBD). Changes require CCB (Configuration Control Board) approval.
- **DM revision process:** Post-freeze changes follow S1000D change management (revision code increment, reason-for-change entry).
- **BREX enforcement:** All DMs validated against <PROGRAMME-SHORT> BREX before CSDB ingestion (automated tooling TBD).
- **Cross-reference management:** CSDB platform maintains applicability cross-references between ATA 37 and ATA 38, ATA 45 DMs.
- **Translation:** English (language A) primary. Additional languages TBD per operator requirements.

---

## §14 S1000D / CSDB Mapping — Comprehensive DMRL Table

| DMC (abbreviated) | SNS | Info Code | Title (abbreviated) | Priority | Status |
|-------------------|-----|-----------|---------------------|----------|--------|
| 037-00-…-040A | 037-00 | 040 | General Description | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-00-…-040B | 037-00 | 040 | <PROGRAMME-SHORT> Scope Reduction | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-10-…-040A | 037-10 | 040 | EVG Description | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-10-…-300A | 037-10 | 300 | EVG Functional Test | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-10-…-520A | 037-10 | 520 | EVG Removal | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-10-…-720A | 037-10 | 720 | EVG Installation | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-10-…-400A | 037-10 | 400 | EVG Fault Isolation | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-20-…-040A | 037-20 | 040 | Distribution Manifold | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-20-…-300A | 037-20 | 300 | Manifold Inspection | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-20-…-300B | 037-20 | 300 | Decay Leak Test | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-30-…-040A | 037-30 | 040 | VRV Description | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-30-…-040B | 037-30 | 040 | SOV Description | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-30-…-300A | 037-30 | 300 | VRV Pop-Test | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-30-…-520A | 037-30 | 520 | VRV Removal | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-30-…-720A | 037-30 | 720 | VRV Installation | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-40-…-040A | 037-40 | 040 | NRV Description | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-40-…-300A | 037-40 | 300 | NRV Inspection | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-40-…-520A | 037-40 | 520 | NRV Removal | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-40-…-720A | 037-40 | 720 | NRV Installation | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-40-…-400A | 037-40 | 400 | Line Fault Isolation | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-50-…-040A | 037-50 | 040 | Consumers + Interfaces | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-50-…-300A | 037-50 | 300 | EFV Inspection | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-50-…-520A | 037-50 | 520 | EFV Removal | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-50-…-720A | 037-50 | 720 | EFV Installation | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-50-…-400A | 037-50 | 400 | EFV Fault Isolation | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-60-…-040A | 037-60 | 040 | Indication Description | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-60-…-300A | 037-60 | 300 | CAS Functional Check | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-60-…-400A | 037-60 | 400 | CAS Fault Isolation | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-70-…-040A | 037-70 | 040 | Ground Service Descr. | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-70-…-300A | 037-70 | 300 | Drain and Rinse Proc. | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-70-…-300B | 037-70 | 300 | Functional Test | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-70-…-300C | 037-70 | 300 | VRV Pop-Test | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-70-…-300D | 037-70 | 300 | Decay Leak Test | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-70-…-400A | 037-70 | 400 | Ground Fault Isolation | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-80-…-040A | 037-80 | 040 | Monitoring Descr. | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-80-…-300A | 037-80 | 300 | CMC / OMS Check | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-80-…-400A | 037-80 | 400 | EVG Fault Isolation | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-80-…-400B | 037-80 | 400 | EFV Fault Isolation | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-80-…-400C | 037-80 | 400 | Transducer FI | P2 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| 037-90-…-040A | 037-90 | 040 | S1000D Mapping | P1 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

**Total planned DMs: 40** (DMRL not frozen — count may change pending OI resolution, particularly OI-037-002)

---

## §15 Footprints

| Item | Value |
|------|-------|
| Total planned DMs | ~40 (not-yet-frozen) |
| Estimated XML file size per DM | 50–200 kB TBD |
| Total estimated CSDB volume (ATA 37) | ~4–8 MB XML TBD |
| AMM Chapter 37 PDF page count (est.) | ~80–120 pages TBD |
| Languages | English (primary); others TBD |
| CSDB path | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §16 Safety and Certification

| Requirement | Reference | Compliance Method | Status |
|-------------|-----------|-------------------|--------|
| Maintenance documentation adequacy | CS-25.1529 (Instructions for CAS) | DM completeness per DMRL | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| AMM procedure accuracy | CS-25.1309 (safety process) | Procedure validation in ground test | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| DMRL coverage of all LRUs | Maintenance programme requirements | DMRL completeness review | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| S1000D BREX compliance | <PROGRAMME-SHORT> BREX TBD | Automated BREX validation | <img src="https://img.shields.io/badge/TBD-red"> |
| Regulatory language requirements | EASA Part-21 / CS-25 | Language and clarity review | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §17 Verification and Validation

| V&V ID | Activity | Method | Acceptance Criteria | Status |
|--------|----------|--------|---------------------|--------|
| VV-037-090-001 | DMRL completeness review | Document review | All SNS have ≥1 DM with info code 040; all LRUs have 520/720 pair | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| VV-037-090-002 | BREX validation | Automated tool | 100% BREX pass rate | <img src="https://img.shields.io/badge/TBD-red"> |
| VV-037-090-003 | Cross-reference integrity check | CSDB report | No broken DM-to-DM references | <img src="https://img.shields.io/badge/TBD-red"> |
| VV-037-090-004 | ATLAS-to-DMRL traceability | Manual review | Each ATLAS scaffold node maps to ≥1 DM | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| VV-037-090-005 | AMM procedure validation | Ground test | Each AMM 300-series procedure executable as written | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| VV-037-090-006 | DM count vs. conventional reduction rationale | Design review | Elimination table accepted by certification authority | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §18 Glossary

| Term | Definition |
|------|-----------|
| ADIRU | Air Data Inertial Reference Unit — solid-state; gyro vacuum DMs eliminated on <PROGRAMME-SHORT> |
| AMM | Aircraft Maintenance Manual — primary publication using ATA 37 S1000D DMs |
| ATA 37 | Air Transport Association chapter for Vacuum systems |
| BREX | Business Rules Exchange — S1000D document defining project-specific authoring rules |
| CCB | Configuration Control Board — governs DMRL changes after freeze |
| CMC | Central Maintenance Computer |
| CSDB | Common Source Data Base — S1000D DM repository and publication management system |
| CS-25.1438 | EASA CS for vacuum/pneumatic plumbing integrity |
| DMC | Data Module Code — unique identifier for each S1000D data module |
| DMRL | Data Module Requirements List — master list of all required DMs for a publication |
| EFV | Electrically actuated Flush Valve |
| EVG | Electric Vacuum Generator |
| Freeze protection | OI-037-005 — thermal protection for vacuum lines |
| Gyroscopic instruments | Vacuum-driven AI, DI, TC — **eliminated on <PROGRAMME-SHORT>**; no gyro vacuum DMs in DMRL |
| Info code | S1000D code indicating DM type (040 descriptive, 300 procedure, 400 FI, 520 removal, 720 installation) |
| IETP | Interactive Electronic Technical Publication — electronic AMM format |
| Manifold | Vacuum distribution header |
| NRV | Non-Return Valve |
| Odour filter | Activated carbon filter — replacement tracked by CMC (OI-037-006) |
| PTFE | Polytetrafluoroethylene — vacuum line material |
| S1000D | International specification for technical publications using an SGML/XML architecture |
| SNS | System / Sub-system / Sub-sub-system — S1000D hierarchical classification aligning with ATA |
| SOV | Shutoff Valve |
| Vacuum transducer | Manifold pressure sensor |
| VRV | Vacuum Relief Valve |
| VWS | Vacuum Waste System |
| Waste tank | ATA 38 scope waste collection vessel |

---

## §19 Citations

1. EASA CS-25 Amendment 27 (TBD), §25.1529 — Instructions for Continued Airworthiness
2. EASA CS-25 §25.1438, §25.1309, §25.1301
3. S1000D Issue 5.0 — International specification for technical publications
4. ATA iSpec 2200 — Air Transport Association specification for aviation maintenance documentation
5. EASA Part-21 — Certification of Aircraft and Related Products

---

## §20 References

| Ref | Document | Link |
|-----|----------|------|
| R-090-001 | 037-000 Vacuum General | [037-000](./037-000-Vacuum-General.md) |
| R-090-002 | 037-010 Vacuum Sources | [037-010](./037-010-Vacuum-Sources.md) |
| R-090-003 | 037-020 Vacuum Distribution | [037-020](./037-020-Vacuum-Distribution.md) |
| R-090-004 | 037-030 Regulation and Shutoff | [037-030](./037-030-Vacuum-Regulation-and-Shutoff.md) |
| R-090-005 | 037-040 Valves and Lines | [037-040](./037-040-Vacuum-Pumps-Ejectors-Valves-and-Lines.md) |
| R-090-006 | 037-050 Consumers and Interfaces | [037-050](./037-050-Vacuum-Consumers-and-System-Interfaces.md) |
| R-090-007 | 037-060 Indication and Warning | [037-060](./037-060-Vacuum-System-Indication-and-Warning.md) |
| R-090-008 | 037-070 Ground Service and Test | [037-070](./037-070-Vacuum-Ground-Service-and-Test-Interfaces.md) |
| R-090-009 | 037-080 Monitoring and Diagnostics | [037-080](./037-080-Vacuum-Monitoring-Diagnostics-and-Control-Interfaces.md) |
| R-090-010 | S1000D Issue 5.0 | [s1000d.org](https://www.s1000d.org/) |

---

## §21 Open Issues

| OI ID | Description | Owner | Priority | Status |
|-------|-------------|-------|----------|--------|
| OI-037-001 | EVG count and sizing — affects DMRL DM count (EVG-2 may require additional 520/720 DMs) | Systems Eng | HIGH | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-037-002 | **Dry-flush vs. vacuum toilet decision** — if dry-flush selected, DMRL reduced to ~2–5 DMs; vacuum system eliminated | Chief Architect | CRITICAL | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-037-003 | Waste tank material and capacity — may require ATA 38 DMRL DMs; ATA 37/38 boundary TBD | Structures | MEDIUM | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-037-004 | Vacuum line routing — affects DM count for line inspection procedures | Structures | HIGH | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-037-005 | Freeze protection — if heater tapes added, requires additional DMs (520/720/300 for heater) | Systems Eng | MEDIUM | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-037-006 | Odour filter certification — requires dedicated 520/720 DMs if scheduled replacement | Certification | MEDIUM | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-037-007 | Ground service panel location — affects 037-70 DM descriptions and access illustrations | Ground Ops | LOW | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-DMRL-001 | **DMRL freeze date TBD** — required before DM authoring can begin | Programme | HIGH | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-DMRL-002 | **BREX document TBD** — <PROGRAMME-SHORT> BREX not yet created; required for CSDB validation | Tech Pubs | HIGH | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-DMRL-003 | **CSDB path TBD** — CSDB platform not yet selected; affects all DM delivery | Tech Pubs | HIGH | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-DMRL-004 | **DM count may reduce to ~2–5 if OI-037-002 resolves to dry-flush** — entire VWS vacuum DM scope eliminated | Chief Architect | CRITICAL | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §22 Change Log

| Rev | Date | Author | Description |
|-----|------|--------|-------------|
| 0.1.0 | 2025-07-14 | AI-assisted scaffold | Initial scaffold — §0–§22; full DMRL planned; 40 DMs defined across all 10 SNS; BREX, CSDB path, freeze date all TBD; 4 DMRL-specific OIs added |

---
*Q+ATLANTIDE ATLAS — ATA 37 Vacuum — 037-090 S1000D / CSDB Mapping and Traceability — <PROGRAMME>*
*Classification: UNCLASSIFIED — ENGINEERING SCAFFOLD*
