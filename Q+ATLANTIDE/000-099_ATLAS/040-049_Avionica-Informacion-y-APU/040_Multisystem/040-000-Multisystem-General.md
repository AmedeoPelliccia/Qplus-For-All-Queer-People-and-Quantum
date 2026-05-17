---
document_id: QATL-ATLAS-1000-ATLAS-040-049-04-040-000-MULTISYSTEM-GENERAL
title: "ATLAS 040-049 · 04.040.000 — Multisystem General"
register: "ATLAS-1000"
register_link: "../../../README.md"

parent_baseline: "Q+ATLANTIDE"
parent_baseline_doc: "../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "./README.md"

architecture_code: "ATLAS"
architecture_name: "Aircraft Top Level Architecture Schema/System"
architecture_link: "../../../README.md"

master_range: "000–099"
master_range_title: "New Commercial Aircraft Architectures"
master_range_link: "../../../README.md"

code_range: "040-049"
code_range_title: "Aviónica, Información & APU"
code_range_link: "../../README.md"

section: "04"
section_title: "Aviónica, Información & APU"
section_link: "../../README.md"

subsection: "040"
subsection_title: "Multisystem"
subsection_link: "./README.md"

subsubject: "000"
subsubject_title: "Multisystem General"
subsubject_file: "040-000-Multisystem-General.md"
subsubject_link: "./040-000-Multisystem-General.md"

primary_q_division: "Q-DATAGOV"
primary_q_division_link: "../../../../organization/Q-Divisions/Q-DATAGOV.md"

support_q_divisions:
  - name: "Q-AIR"
    link: "../../../../organization/Q-Divisions/Q-AIR.md"
  - name: "Q-SPACE"
    link: "../../../../organization/Q-Divisions/Q-SPACE.md"
  - name: "Q-HPC"
    link: "../../../../organization/Q-Divisions/Q-HPC.md"

orb_function_support:
  - name: "ORB-PMO"
    link: "../../../../organization/ORB-Functions/ORB-PMO.md"
  - name: "ORB-LEG"
    link: "../../../../organization/ORB-Functions/ORB-LEG.md"

governance_class: "baseline"
governance_class_link: "#ref-gov"
version: "1.0.0"
status: "active"
language: "en"

s1000d_applicability: "S1000D-CSDB-compatible"
s1000d_reference_link: "#ref-s1000d"
ata_reference: "ATA iSpec 2200"
ata_reference_link: "#ref-ata-ispec-2200"

created: "2026-05-09"
updated: "2026-05-09"
review_status: "to-be-reviewed-by-system-expert"
standard_scope: agnostic
programme_specific: false
---

# ATLAS 040-049 · Section 04 · Subsection 040 · 000 — Multisystem General

## 0. Hyperlink Policy

All linkable content in this file shall be expressed as Markdown links where a stable target exists.

Use:

- relative links for repository-internal content;
- anchor links for headings, diagrams, glossary terms, citations, references, and footprint entries;
- stable external links only for public standards or authoritative sources;
- `TBD` where no stable target exists.

Do not invent links.

---

## 1. Purpose

This document establishes the general architectural description, scope boundary, and governing principles for the **[Multisystem](#glossary-multisystem)** subsection, **[ATLAS 040](./README.md)**, within the **[Q+ATLANTIDE](../../../../organization/Q+ATLANTIDE.md)** controlled baseline.

It provides the authoritative entry point for all subsubject documents within subsection **[040_Multisystem](./README.md)**, defining how cross-system avionics functions are structured, classified, and managed under the **[ATLAS](#glossary-atlas)** taxonomy.

The **[Multisystem](#glossary-multisystem)** concept recognises that modern aircraft avionics architectures are no longer composed only of isolated, federated black boxes. Instead, resources such as computing hardware, avionics data networks, power, cooling, timing references, configuration data, and diagnostic services are shared among multiple hosted applications through rigorously partitioned platforms.

This document anchors that conceptual shift within the **[ATLAS](../../../README.md)** framework and maps it to applicable industry standards and reference frameworks, including **[ATA iSpec 2200](#ref-ata-ispec-2200)**, **[ARINC 653](#ref-arinc-653)**, **[RTCA DO-178C](#ref-do-178c)**, **[RTCA DO-254](#ref-do-254)**, and **[S1000D](#ref-s1000d)**.

---

## 2. Applicability

| Applicability Item | Value |
|---|---|
| Architecture register | [Q+ATLANTIDE](../../../../organization/Q+ATLANTIDE.md) |
| ATLAS band | [000-099_ATLAS](../../../README.md) |
| ATA reference | [ATA iSpec 2200](#ref-ata-ispec-2200) |
| S1000D compatibility | [S1000D-CSDB-compatible](https://s1000d.org/) |
| Lifecycle use | LC03 Architecture Definition / LC05 Detailed Design / LC06 Verification Planning / LC11 Operation / LC12 Maintenance & Support |

---

## 3. System / Function Overview

The **[Multisystem](#glossary-multisystem)** node covers cross-functional avionics architecture elements shared across two or more aircraft systems or hosted functions.

For modern aircraft, the node addresses the shift from federated, single-function boxes to integrated platforms where computing resources, data networks, timing infrastructure, and diagnostic services are shared. Architecture drivers include weight reduction, volume efficiency, power savings, and simplified certification through consolidated hardware platforms governed by **[ARINC 653](#ref-arinc-653)** partitioning and **[DO-297](#ref-do-297)** IMA guidance.

This document does not freeze the final certified design. It establishes a controlled scaffold for downstream engineering, **[S1000D](#glossary-s1000d)** data-module planning, **[CSDB](#glossary-csdb)** integration, and evidence capture.

---

## 4. Scope

### 4.1 Included

- Controlled definition of the cross-system avionics architecture;
- **[Integrated Modular Avionics](#glossary-ima)** platforms hosting multiple avionics applications on shared computing resources;
- **[Avionics data networks](#glossary-avionics-data-network)** providing deterministic interconnectivity across subsystems;
- Shared services such as **[BITE](#glossary-bite)**, time synchronisation, bay-level power distribution, and configuration data loading;
- System integration and **[ICD](#glossary-icd)** management;
- Monitoring, diagnostics, and health-management aggregation across avionics domains;
- **[S1000D](#glossary-s1000d)** data-module and **[CSDB](#glossary-csdb)** traceability.

### 4.2 Excluded

- System-specific functions covered under dedicated ATLAS sections;
- Supplier-proprietary internal design data unless released to the programme baseline;
- Final certification compliance statements;
- Detailed maintenance procedures unless assigned by the [DMRL](#glossary-dmrl);
- Production-level configuration until CCB freeze.

---

## 5. Architecture Description

The **[Multisystem](#glossary-multisystem)** architecture is organised around controlled interfaces, deterministic function allocation, and maintainable component boundaries.

At architecture level, the system shall be described in terms of:

1. **Function** — what the system does.
2. **Equipment** — which [LRUs](#glossary-lru), assemblies, modules, or components implement the function.
3. **Interfaces** — how the system exchanges power, data, signal, or commands.
4. **Control logic** — how the system is commanded, monitored, degraded, isolated, or reset.
5. **Maintenance boundary** — what a technician can inspect, test, remove, install, or replace.
6. **Evidence boundary** — which requirements, tests, inspections, and records prove compliance.

---

## 6. Functional Breakdown

| Ref | Function | Description | Primary Interface |
|---:|---|---|---|
| [F-001](#f-001) | <a id="f-001"></a>Shared Computing | Provides partitioned compute resources for multiple hosted avionics applications. | [040-010](./040-010-Integrated-Modular-Avionics-IMA.md) |
| [F-002](#f-002) | <a id="f-002"></a>Avionics Networking | Supports deterministic data exchange across all avionics subsystems. | [040-030](./040-030-Avionics-Networks-and-Data-Buses.md) |
| [F-003](#f-003) | <a id="f-003"></a>Shared Services | Delivers platform-level BITE, power, cooling, and timing services. | [040-050](./040-050-Shared-Avionics-Resources-and-Services.md) |
| [F-004](#f-004) | <a id="f-004"></a>Monitoring | Captures status, failures, degradation, and maintenance data. | [040-080](./040-080-Multisystem-Monitoring-Diagnostics-and-Control-Interfaces.md) |
| [F-005](#f-005) | <a id="f-005"></a>Traceability | Links architecture, requirements, evidence, and S1000D content. | [040-090](./040-090-S1000D-CSDB-Mapping-and-Traceability.md) |

---

## 7. Mermaid — Subsection Structure

<a id="diagram-subsection-structure"></a>

```mermaid
flowchart TD
    A["ATLAS 040 — Multisystem<br/>(Subsection Root)"] --> B["040-000<br/>General & Architecture Concept"]
    A --> C["040-010<br/>Integrated Modular Avionics (IMA)"]
    A --> D["040-020<br/>Core Processing & Computing Platforms"]
    A --> E["040-030<br/>Avionics Networks & Data Buses"]
    A --> F["040-040<br/>System Integration & Interface Mgmt"]
    A --> G["040-050<br/>Shared Resources & Services"]
    A --> H["040-060<br/>Time Synchronisation & Data Integrity"]
    A --> I["040-070<br/>Configuration, Software & Data Loading"]
    A --> J["040-080<br/>Monitoring, Diagnostics & Control"]
    A --> K["040-090<br/>S1000D / CSDB Mapping & Traceability"]

    B:::root

    classDef root fill:#1a3c5e,color:#fff,stroke:#0d2137
```

***[Diagram 1](#diagram-subsection-structure) — Controlled subsection structure for [ATLAS 040 — Multisystem](./README.md). Related sections: [Functional Breakdown](#6-functional-breakdown), [Footprint](#15-footprints), and [References & Citations](#8-references--citations).***

---

## 8. Mermaid — Multisystem Context

<a id="diagram-multisystem-context"></a>

```mermaid
flowchart LR
    IMA["IMA / Shared Computing"] --> NET["Avionics Networks"]
    NET --> NAV["Navigation"]
    NET --> ECS["Conditioning and Pressurization"]
    NET --> CMS["Central Maintenance"]
    NET --> ELEC["Electrical Power"]
    NET --> PROP["Propulsion Interfaces"]

    IMA --> SWLOAD["Software / Data Loading"]
    IMA --> TIME["Time Synchronisation"]
    IMA --> BITE["BITE / Diagnostics"]
    BITE --> CSDB["S1000D / CSDB Evidence"]
```

***[Diagram 2](#diagram-multisystem-context) — Multisystem avionics context showing shared computing, networking, timing, software-loading, diagnostics, and CSDB evidence flow. Related sections: [Scope](#4-scope), [Architecture Principles](#architecture-principles), and [Glossary](#18-glossary).***

---

## 9. Mermaid — Lifecycle Traceability

<a id="diagram-lifecycle-traceability"></a>

```mermaid
flowchart LR
    LC02[LC02 Requirements] --> LC03[LC03 Architecture]
    LC03 --> LC05[LC05 Detailed Design]
    LC05 --> LC06[LC06 Verification Planning]
    LC06 --> LC10[LC10 Certification / Approval]
    LC10 --> LC11[LC11 Operation]
    LC11 --> LC12[LC12 Maintenance / Support]

    LC03 --> CSDB[S1000D / CSDB]
    LC05 --> DMRL[DMRL]
    LC06 --> EVID[Evidence Records]
    LC12 --> FEEDBACK[In-Service Feedback]
    FEEDBACK --> LC13[LC13 Upgrade / Modification]
```

***[Diagram 3](#diagram-lifecycle-traceability) — Lifecycle traceability from requirements to maintenance feedback. Related sections: [Verification and Validation](#17-verification-and-validation), [References](#20-references), [Open Issues](#21-open-issues).***

---

## 10. Interfaces

| Interface Type | Connected System | Description | Evidence Required |
|---|---|---|---|
| Data / control | [IMA / CMS / controller](./040-010-Integrated-Modular-Avionics-IMA.md) | Inter-system command and monitoring via AFDX/ARINC 664 and ARINC 429 buses. | ICD / data dictionary |
| Electrical power | [Electrical Power (023)](../../../020-029_Sistemas-Core-de-Aeronave/023_Electrical-Power/README.md) | 28 VDC / 115 VAC supply to IMA cabinets and avionics bays. | Wiring / load analysis |
| Mechanical | [Structure / avionics bay](TBD) | Rack mounting, cooling, access panels, bonding. | Installation drawing |
| Maintenance | [CSDB / IETP](./040-090-S1000D-CSDB-Mapping-and-Traceability.md) | Technician-facing BITE and CMC diagnostic interface. | [DMRL / BREX](#glossary-dmrl) |

---

## 11. Operating Modes

| Mode | Description | Entry Condition | Exit Condition |
|---|---|---|---|
| [Normal](#mode-normal) | <a id="mode-normal"></a>All partitions and networks operating within nominal limits. | Aircraft powered and avionics enabled. | Shutdown, fault, or mode change. |
| [Degraded](#mode-degraded) | <a id="mode-degraded"></a>One or more shared resources operating at reduced capacity or failed; hosted applications continue via redundancy. | Fault detected or partial resource loss. | Recovery, isolation, or maintenance action. |
| [Maintenance](#mode-maintenance) | <a id="mode-maintenance"></a>System configured for inspection, software load, test, or LRU exchange. | Authorized maintenance action. | Maintenance close-up and operational check. |
| [Failure / Safe State](#mode-failure-safe-state) | <a id="mode-failure-safe-state"></a>Shared platform enters protective isolation to prevent cascade failure. | Fault threshold exceeded. | Reset, repair, replacement, or dispatch decision. |

---

## 12. Monitoring and Diagnostics

The Multisystem shall provide sufficient monitoring to support safe operation, maintenance troubleshooting, and lifecycle evidence capture, including:

- Partition and resource health status;
- Network error counters (VL utilisation, latency, error frames);
- Power and thermal status of IMA cabinets;
- Time synchronisation accuracy and holdover status;
- Configuration and software load verification status;
- [BITE](#glossary-bite) results aggregated to [CMS](#glossary-cms);
- Maintenance messages routed through [ARINC 429](#ref-arinc-429) / [AFDX](#glossary-afdx) to the [Central Maintenance System](./040-080-Multisystem-Monitoring-Diagnostics-and-Control-Interfaces.md).

---

## 13. Maintenance Concept

Maintenance shall support modular inspection, fault isolation, LRU removal, installation, and return-to-service verification.

Content is structured around:

- avionics bay access requirements;
- safety precautions (power isolation, ESD, software load control);
- replacement boundaries (LRU / LRM level);
- functional and BITE verification after installation;
- controlled post-load configuration verification.

Maintenance procedures shall remain provisional until validated against the applicable [DMRL](#glossary-dmrl), [BREX](#glossary-brex), and task validation records.

---

## 14. S1000D / CSDB Mapping

| S1000D Element | Controlled Value |
|---|---|
| Model ident code | `[PROGRAMME-AIRCRAFT]` |
| System diff code | `[PROGRAMME-VARIANT]` |
| System code | `040` |
| Sub-system code | `0` |
| Sub-sub-system code | `00` |
| Assy code | `00A` |
| Info code | `040 / 300 / 400 / 520 / 720 / 941` |
| Item location code | `D` |
| DMC prefix | `DMC-<PROGRAMME>-<VARIANT>-040` |

### Recommended Data Module Set

| Info code | Data module purpose | Suggested filename |
|---:|---|---|
| [040](#dm-040) | <a id="dm-040"></a>Descriptive information | `DMC-<PROGRAMME>-<VARIANT>-040-000-00A-040A-D_System-Description.xml` |
| [300](#dm-300) | <a id="dm-300"></a>Examination / inspection / check | `DMC-<PROGRAMME>-<VARIANT>-040-000-00A-300A-D_Inspection.xml` |
| [400](#dm-400) | <a id="dm-400"></a>Fault isolation | `DMC-<PROGRAMME>-<VARIANT>-040-000-00A-400A-D_Fault-Isolation.xml` |
| [520](#dm-520) | <a id="dm-520"></a>Remove / disassemble | `DMC-<PROGRAMME>-<VARIANT>-040-000-00A-520A-D_Remove.xml` |
| [720](#dm-720) | <a id="dm-720"></a>Install / assemble / connect | `DMC-<PROGRAMME>-<VARIANT>-040-000-00A-720A-D_Install.xml` |
| [941](#dm-941) | <a id="dm-941"></a>Illustrated parts data | `DMC-<PROGRAMME>-<VARIANT>-040-000-00A-941A-D_Illustrated-Parts-Data.xml` |

---

## 15. Footprints

### 15.1 Physical Footprint

| Footprint Item | Description | Status |
|---|---|---|
| Installation zone | Avionics bay (forward / main equipment centre) | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Access panels | Dedicated avionics bay access doors | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Mounting provisions | ARINC 600 rack / cabinet provisions | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Clearance envelope | Per LRU removal envelope | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Cooling / ventilation | Forced-air cooling via avionics bay ventilation | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Drainage / leak path | N/A (electronic equipment) | N/A |

### 15.2 Electrical / Data Footprint

| Footprint Item | Description | Status |
|---|---|---|
| Power supply | 28 VDC and 115 VAC from primary electrical buses | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Protection | SSPCs / circuit breakers per electrical load analysis | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Data buses | AFDX (ARINC 664), ARINC 429, discrete signals | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Connectors | ARINC 600 Series I / MIL-C-38999 | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Bonding / grounding | Avionics bay structural bonding per DO-160G Section 16 | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| EMC / EMI controls | Shielding, segregation, filtering per DO-160G | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |

### 15.3 Maintenance Footprint

| Footprint Item | Description | Status |
|---|---|---|
| Access level | Line / Base | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Replaceable unit | LRU (cabinet level) / LRM (module level) | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Removal time | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Required tools | Standard avionics tools; ESD precautions | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Required GSE | Avionics test set; data loader | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Return-to-service check | BITE / operational check per applicable CMM | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |

### 15.4 Data Footprint

| Footprint Item | Description | Status |
|---|---|---|
| Configuration records | Part number, serial number, software load, effectivity | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Evidence records | Test, inspection, compliance, review records | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| CSDB records | DMCs, ICNs, BREX, applicability | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Maintenance data | Fault history, BITE, removal / installation records | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| Cybersecurity records | Access, load authorisation, integrity checks | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |

---

## 16. Safety and Certification Considerations

The Multisystem shared platform shall be assessed in terms of its aircraft-level failure effects and integration dependencies.

Considerations include:

- Common-cause failures in shared computing or networking resources;
- Partition containment failures (spatial or temporal);
- Loss of shared timing reference (timing integrity monitoring);
- Misleading diagnostic indication through shared BITE bus;
- Software and hardware assurance levels per [DO-178C](#ref-do-178c) / [DO-254](#ref-do-254);
- Environmental qualification per [DO-160G](#ref-do-160g);
- Electromagnetic compatibility.

Final safety classification shall remain <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> until reviewed against the applicable FHA, PSSA, SSA, and certification basis.

---

## 17. Verification and Validation

| Verification Method | Description | Evidence |
|---|---|---|
| [Analysis](#verification-analysis) | <a id="verification-analysis"></a>Partition analysis, timing analysis, FMEA, worst-case execution time. | Analysis report |
| [Inspection](#verification-inspection) | <a id="verification-inspection"></a>Physical and visual verification of installation, marking, routing. | Inspection record |
| [Test](#verification-test) | <a id="verification-test"></a>Functional, environmental, integration, and system test. | Test report |
| [Demonstration](#verification-demonstration) | <a id="verification-demonstration"></a>Operational demonstration under controlled conditions. | Demonstration record |
| [Similarity](#verification-similarity) | <a id="verification-similarity"></a>Justified reuse of existing certified design evidence. | Similarity report |

---

## 18. Glossary

| Term / Acronym | Definition | Link |
|---|---|---|
| <a id="glossary-afdx"></a>AFDX | Avionics Full-Duplex Switched Ethernet; deterministic switched Ethernet defined by ARINC 664 Part 7. | [ARINC 664](#ref-arinc-664) |
| <a id="glossary-atlas"></a>ATLAS | Aircraft Top Level Architecture Schema/System — Q+ATLANTIDE taxonomic framework. | [ATLAS architecture](../../../README.md) |
| <a id="glossary-avionics-data-network"></a>Avionics Data Network | Controlled aircraft data-network infrastructure supporting deterministic communication. | [040-030](./040-030-Avionics-Networks-and-Data-Buses.md) |
| <a id="glossary-bite"></a>BITE | Built-In Test Equipment; on-board self-test capability for fault detection, isolation, and reporting. | [040-080](./040-080-Multisystem-Monitoring-Diagnostics-and-Control-Interfaces.md) |
| <a id="glossary-brex"></a>BREX | Business Rules Exchange; S1000D rule set used to validate data-module content. | [040-090](./040-090-S1000D-CSDB-Mapping-and-Traceability.md) |
| <a id="glossary-cms"></a>CMS | Central Maintenance System; aircraft maintenance computer aggregating fault and diagnostic data. | [040-080](./040-080-Multisystem-Monitoring-Diagnostics-and-Control-Interfaces.md) |
| <a id="glossary-csdb"></a>CSDB | Common Source DataBase; S1000D repository for controlled data modules. | [040-090](./040-090-S1000D-CSDB-Mapping-and-Traceability.md) |
| <a id="glossary-dmrl"></a>DMRL | Data Module Requirement List; controlled list of required S1000D data modules. | [040-090](./040-090-S1000D-CSDB-Mapping-and-Traceability.md) |
| <a id="glossary-icd"></a>ICD | Interface Control Document; formally managed interface specification between system elements. | [040-040](./040-040-System-Integration-and-Interface-Management.md) |
| <a id="glossary-ima"></a>IMA | Integrated Modular Avionics; shared, partitioned computing platform hosting multiple applications. | [040-010](./040-010-Integrated-Modular-Avionics-IMA.md) |
| <a id="glossary-lru"></a>LRU | Line-Replaceable Unit; modular assembly designed for rapid removal and replacement on the flight line. | [Maintenance Concept](#13-maintenance-concept) |
| <a id="glossary-multisystem"></a>Multisystem | Cross-functional aircraft architecture domain covering shared avionics resources, networks, timing, configuration, diagnostics, and traceability. | [040_Multisystem](./README.md) |
| <a id="glossary-q-atlantide"></a>Q+ATLANTIDE | Quantum and Aerospace Top-Level Architectures and Novel Technologies Identification Data Ecosystem. | [Parent baseline](../../../../organization/Q+ATLANTIDE.md) |
| <a id="glossary-s1000d"></a>S1000D | International specification for technical publications using a Common Source DataBase. | [S1000D reference](#ref-s1000d) |
| <a id="glossary-sns"></a>SNS | Standard Numbering System; hierarchical coding logic for aircraft system documentation. | [ATA iSpec 2200](#ref-ata-ispec-2200) |

---

## 19. Citations

| Ref | Citation | Use | Link |
|---|---|---|---|
| [CIT-001](#cit-001) | <a id="cit-001"></a>`ATA iSpec 2200, Edition 2022, Chapter 4.` | SNS logic and chapter numbering | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| [CIT-002](#cit-002) | <a id="cit-002"></a>`RTCA DO-297, Integrated Modular Avionics (IMA) Development Guidance and Certification Considerations, 2005.` | IMA architecture and certification | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| [CIT-003](#cit-003) | <a id="cit-003"></a>`ARINC 653, Avionics Application Software Standard Interface, Part 1–4.` | Partitioning and APEX interface | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| [CIT-004](#cit-004) | <a id="cit-004"></a>`RTCA DO-178C, Software Considerations in Airborne Systems, 2011.` | Software assurance levels | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| [CIT-005](#cit-005) | <a id="cit-005"></a>`RTCA DO-254, Design Assurance Guidance for Airborne Electronic Hardware, 2000.` | Hardware assurance levels | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |

---

## 20. References

| Ref | Document | Identifier | Revision | Status | Link |
|---|---|---:|---:|---|---|
| [REF-001](#ref-001) | <a id="ref-001"></a>Q+ATLANTIDE baseline | `QATL-ATLAS-000-099` | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> | Draft | [Open](../../../../organization/Q+ATLANTIDE.md) |
| [REF-ATA-ISPEC-2200](#ref-ata-ispec-2200) | <a id="ref-ata-ispec-2200"></a>ATA iSpec 2200 | `ATA-ISPEC-2200` | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> | External standard | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| [REF-ARINC-653](#ref-arinc-653) | <a id="ref-arinc-653"></a>ARINC 653 | `ARINC-653` | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> | External standard | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| [REF-ARINC-664](#ref-arinc-664) | <a id="ref-arinc-664"></a>ARINC 664 / AFDX | `ARINC-664` | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> | External standard | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| [REF-ARINC-429](#ref-arinc-429) | <a id="ref-arinc-429"></a>ARINC 429 | `ARINC-429` | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> | External standard | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| [REF-DO-178C](#ref-do-178c) | <a id="ref-do-178c"></a>RTCA DO-178C | `DO-178C` | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> | External standard | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| [REF-DO-254](#ref-do-254) | <a id="ref-do-254"></a>RTCA DO-254 | `DO-254` | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> | External standard | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| [REF-DO-297](#ref-do-297) | <a id="ref-do-297"></a>RTCA DO-297 | `DO-297` | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> | External standard | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| [REF-DO-160G](#ref-do-160g) | <a id="ref-do-160g"></a>RTCA DO-160G | `DO-160G` | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> | External standard | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| [REF-MIL-STD-1553](#ref-mil-std-1553) | <a id="ref-mil-std-1553"></a>MIL-STD-1553 | `MIL-STD-1553` | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> | External standard | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| [REF-S1000D](#ref-s1000d) | <a id="ref-s1000d"></a>S1000D | `S1000D-ISS5` | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> | External standard | [https://s1000d.org/](https://s1000d.org/) |
| [REF-GOV](#ref-gov) | <a id="ref-gov"></a>Governance class — baseline | `QATL-GOV-BASELINE` | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> | Controlled | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

---

## 21. Open Issues

| ID | Issue | Owner | Status | Link |
|---|---|---|---|---|
| [OI-001](#oi-001) | <a id="oi-001"></a>Confirm whether ATLAS 040 and ATLAS 042 should remain separated between general multisystem and IMA-specific content. | Q-DATAGOV | Open | [Functional Breakdown](#6-functional-breakdown) |
| [OI-002](#oi-002) | <a id="oi-002"></a>Confirm final repository targets for external standards references. | ORB-LEG | Open | [References](#20-references) |
| [OI-003](#oi-003) | <a id="oi-003"></a>Confirm [PROGRAMME-AIRCRAFT]-specific applicability for hosted avionics functions. | Q-AIR | Open | [Scope](#4-scope) |
| [OI-004](#oi-004) | <a id="oi-004"></a>Confirm S1000D DMRL allocation for ATLAS 040 multisystem documents. | Q-DATAGOV | Open | [Glossary — DMRL](#glossary-dmrl) |

---

## 22. Change Log

| Version | Date | Author | Change | Link |
|---|---|---|---|---|
| [1.0.0](#chg-100) | <a id="chg-100"></a>2026-05-09 | Q+ Team/Amedeo Pelliccia + AI | Initial active baseline for ATLAS 040-049 · 04.040.000 — Multisystem General. | [Document root](#atlas-040-049--section-04--subsection-040--000--multisystem-general) |

---

> Programme-controlled baseline. Content is subject to [Q+ATLANTIDE](../../../../organization/Q+ATLANTIDE.md), [Q-DATAGOV](../../../../organization/Q-Divisions/Q-DATAGOV.md), [S1000D / CSDB traceability](./040-090-S1000D-CSDB-Mapping-and-Traceability.md), and controlled change management before downstream programme release.

> **To be reviewed by system expert.**
