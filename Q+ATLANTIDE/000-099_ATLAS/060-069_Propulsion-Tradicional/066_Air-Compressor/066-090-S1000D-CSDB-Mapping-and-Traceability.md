---
document_id: "QATL-ATLAS-1000-ATLAS-060-069-06-066-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY"
title: "ATLAS 060-069 · 06.066.090 — S1000D / CSDB Mapping and Traceability"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../../README.md
parent_section_doc: ../../README.md
parent_subsection_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "060-069"
section: "06"
section_title: "Propulsión Tradicional"
subsection: "066"
subsection_title: "Air Compressor"
subsubject: "090"
subsubject_title: "S1000D / CSDB Mapping and Traceability"
subsubject_file: "066-090-S1000D-CSDB-Mapping-and-Traceability.md"
subsubject_link: "./066-090-S1000D-CSDB-Mapping-and-Traceability.md"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-MECHANICS, Q-AIR, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
s1000d_applicability: "S1000D-CSDB-compatible"
ata_reference: "ATA 66"
created: "2026-05-11"
updated: "2026-05-11"
review_status: "to-be-reviewed-by-system-expert"
---

![DRAFT](https://img.shields.io/badge/DRAFT-yellow)
![TBD](https://img.shields.io/badge/TBD-red)
![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)

# ATLAS 060-069 · Section 06 · Subsection 066 · 090 — S1000D / CSDB Mapping and Traceability

## 0. Hyperlink Policy

All linkable content in this file shall be expressed as Markdown links where a stable target exists.

Use:

- relative links for repository-internal content;
- anchor links for headings, figures, diagrams, glossary terms, citations, references, open issues, and lifecycle sections;
- stable external links only for public standards or authoritative sources;
- `TBD` or `<relative-link-or-TBD>` where no stable target exists.

Do not invent links.

Every table containing a document, path, code, reference, acronym, figure, diagram, lifecycle phase, Q-Division, ORB-Function, DMC, BREX, DMRL, evidence record, or issue shall include either a direct link or an explicit `TBD` target.

---

## 1. Purpose

This document defines the controlled technical scope for **S1000D / CSDB Mapping and Traceability** (`066-090`) within the [Q+ATLANTIDE](../../../../../Q+ATLANTIDE/) / [ATLAS 000-099](../../../) architecture branch, section [060-069 Propulsión Tradicional](../../).

The objective is to provide a deterministic, [S1000D](https://s1000d.org/)-compatible technical baseline covering the S1000D CSDB mapping, DMC structure, BREX applicability, and traceability for all ATA 66 Air Compressor data modules.

This file belongs to:

[`Q+ATLANTIDE/000-099_ATLAS/060-069_Propulsion-Tradicional/066_Air-Compressor/066-090-S1000D-CSDB-Mapping-and-Traceability.md`](./)

---

## 2. Applicability

This document applies to the [AMPEL360e Wide Tube-and-Wing Family](../../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/) programme and the **eWTW** configuration.

| Applicability Item | Value | Status |
|---|---|---|
| Programme | [AMPEL360e Wide Tube-and-Wing Family](../../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| Short code | eWTW | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| Architecture register | [Q+ATLANTIDE](../../../../../Q+ATLANTIDE/) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| ATLAS band | [000-099_ATLAS](../../../) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| Section | [060-069 Propulsión Tradicional](../../) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| Subsection | [066 Air Compressor](../) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| ATA reference | [ATA 66](#ref-ata) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| S1000D compatibility | [S1000D-CSDB-compatible](https://s1000d.org/) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| Lifecycle use | [LC03](../../../../../Governance/Lifecycle/LC03-Architecture-Definition.md) / [LC05](../../../../../Governance/Lifecycle/LC05-Detailed-Design.md) / [LC06](../../../../../Governance/Lifecycle/LC06-Verification-Planning.md) / [LC11](../../../../../Governance/Lifecycle/LC11-Operation.md) / [LC12](../../../../../Governance/Lifecycle/LC12-Maintenance-Support.md) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |

---

## 3. System / Function Overview

The **S1000D / CSDB Mapping and Traceability** node covers the S1000D CSDB mapping, DMC structure, BREX applicability, and traceability for all ATA 66 Air Compressor data modules.

For the [AMPEL360e](#glossary-ampel360e) configuration, this node shall be treated as part of a full-electric, medium-range, approximately 100-passenger aircraft architecture. Where conventional aircraft assumptions rely on engine bleed, hydraulic supply, pneumatic supply, or legacy equipment, the AMPEL360e implementation shall be explicitly reviewed for electric, distributed, or digitally controlled alternatives.

This document does not freeze the final certified design. It establishes a controlled scaffold for downstream engineering, [S1000D](#glossary-s1000d) data-module planning, [CSDB](#glossary-csdb) integration, and evidence capture.

---

## 4. Scope

### 4.1 Included

This document includes:
- Define DMC structure for ATA 66
- Map all subsubject topics to data module types
- Document BREX rules for air compressor DMs
- Define DMRL entries and evidence requirements
- Establish traceability to Q+ATLANTIDE ATLAS architecture

### 4.2 Excluded

This document excludes:

- supplier-proprietary internal design data unless released to the programme baseline;
- final certification compliance statements;
- detailed maintenance procedures unless assigned by the [DMRL](#glossary-dmrl);
- final illustrated parts data unless released through the [CSDB](#glossary-csdb);
- production-level configuration until [CCB](#glossary-ccb) freeze.

---

## 5. Architecture Description ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)

The **S1000D / CSDB Mapping and Traceability** architecture is organized around controlled interfaces, deterministic function allocation, and maintainable component boundaries.

At architecture level, the system shall be described in terms of:

1. **Function** — what the system does.
2. **Equipment** — which [LRUs](#glossary-lru), assemblies, panels, modules, or components implement the function.
3. **Interfaces** — how the system exchanges power, data, fluid, air, signal, force, or commands.
4. **Control logic** — how the system is commanded, monitored, degraded, isolated, or reset.
5. **Maintenance boundary** — what a technician can inspect, test, remove, install, or replace.
6. **Evidence boundary** — which requirements, tests, inspections, and records prove compliance.

---

## 6. Functional Breakdown ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)

| Ref | Function | Description | Primary Interface | Status |
|---:|---|---|---|---|
| [F-001](#f-001) | <a id="f-001"></a>Define DMC structure for ATA 66 | TBD — to be completed. | [Interface](#10-interfaces) | ![TBD](https://img.shields.io/badge/TBD-red) |
| [F-002](#f-002) | <a id="f-002"></a>Map all subsubject topics to data module types | TBD — to be completed. | [Interface](#10-interfaces) | ![TBD](https://img.shields.io/badge/TBD-red) |
| [F-003](#f-003) | <a id="f-003"></a>Document BREX rules for air compressor DMs | TBD — to be completed. | [Interface](#10-interfaces) | ![TBD](https://img.shields.io/badge/TBD-red) |
| [F-004](#f-004) | <a id="f-004"></a>Monitoring | Captures status, failures, degradation, and maintenance data. | [CMS / BITE](#12-monitoring-and-diagnostics) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| [F-005](#f-005) | <a id="f-005"></a>Traceability | Links architecture, requirements, evidence, and S1000D content. | [CSDB / DMRL / BREX](#14-s1000d--csdb-mapping) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |

---

## 7. Mermaid — System Context Diagram

<a id="diagram-system-context"></a>

```mermaid
flowchart LR
    A[Aircraft-Level Function] --> B[066 Air Compressor]
    B --> C[Power Interface]
    B --> D[Data / Control Interface]
    B --> E[Mechanical / Fluid / Air Interface]
    B --> F[Monitoring and Diagnostics]
    F --> G[Central Maintenance System]
    G --> H[S1000D / CSDB Evidence]
```

***[Diagram 1](#diagram-system-context) — System context diagram for S1000D / CSDB Mapping and Traceability. Related sections: [Interfaces](#10-interfaces), [Monitoring and Diagnostics](#12-monitoring-and-diagnostics), [S1000D / CSDB Mapping](#14-s1000d--csdb-mapping).***

---

## 8. Mermaid — Internal Functional Architecture

<a id="diagram-internal-functional-architecture"></a>

```mermaid
flowchart TB
    SYS[066-090 S1000D / CSDB Mapping and Traceabil] --> F1[Define DMC structure for ATA 66]
    SYS --> F2[Map all subsubject topics to data module types]
    SYS --> CTRL[Control Logic]
    SYS --> MON[Monitoring and Diagnostics]
    SYS --> MAINT[Maintenance Boundary]
    CTRL --> IMA[IMA / Controller Interface]
    MON --> CMS[CMS / BITE]
    MAINT --> CSDB[S1000D Data Modules]
```

***[Diagram 2](#diagram-internal-functional-architecture) — Internal functional architecture. Related sections: [Functional Breakdown](#6-functional-breakdown), [Maintenance Concept](#13-maintenance-concept), [Footprints](#15-footprints).***

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

## 10. Interfaces ![TBD](https://img.shields.io/badge/TBD-red)

| Interface Type | Connected System | Description | Evidence Required | Status |
|---|---|---|---|---|
| Electrical power | [ATA 24 Power](TBD) | TBD — power supply interface. | [Wiring / load analysis](#20-references) | ![TBD](https://img.shields.io/badge/TBD-red) |
| Data / control | [FADEC / CMS / IMA](TBD) | TBD — command and monitoring interface. | [ICD / data dictionary](#20-references) | ![TBD](https://img.shields.io/badge/TBD-red) |
| Mechanical | [Structure / installation zone](TBD) | TBD — mounting, access, or load path. | [Installation drawing](#20-references) | ![TBD](https://img.shields.io/badge/TBD-red) |
| Fluid / air / thermal | [Adjacent propulsion system](TBD) | TBD — flow, pressure, temperature, or thermal interface. | [Test report](#20-references) | ![TBD](https://img.shields.io/badge/TBD-red) |
| Maintenance | [CSDB / IETP](TBD) | TBD — technician-facing access and procedure boundary. | [DMRL / BREX](#14-s1000d--csdb-mapping) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |

---

## 11. Operating Modes ![DRAFT](https://img.shields.io/badge/DRAFT-yellow)

| Mode | Description | Entry Condition | Exit Condition | Status |
|---|---|---|---|---|
| [Normal](#mode-normal) | <a id="mode-normal"></a>System operates within nominal limits. | Aircraft powered and system enabled. | Shutdown, fault, or mode change. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| [Degraded](#mode-degraded) | <a id="mode-degraded"></a>System operates with reduced function or redundancy. | Fault detected or partial loss of function. | Recovery, isolation, or maintenance action. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| [Maintenance](#mode-maintenance) | <a id="mode-maintenance"></a>System is configured for inspection, test, removal, installation, or servicing. | Authorized maintenance action. | Maintenance close-up and operational check. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| [Failure / Safe State](#mode-failure-safe-state) | <a id="mode-failure-safe-state"></a>System enters protective state to prevent unsafe operation. | Fault threshold exceeded. | Reset, repair, replacement, or dispatch decision. | ![TBD](https://img.shields.io/badge/TBD-red) |

---

## 12. Monitoring and Diagnostics ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)

The system shall provide sufficient monitoring to support safe operation, maintenance troubleshooting, and lifecycle evidence capture.

Monitoring may include:

- status indication;
- fault detection;
- [BITE](#glossary-bite) results;
- sensor plausibility checks;
- degraded-mode reporting;
- maintenance messages;
- event recording;
- configuration status;
- software or hardware part-number reporting where applicable.

Diagnostic data shall be mapped to the relevant [S1000D / CSDB](#14-s1000d--csdb-mapping) fault isolation and maintenance data modules.

---

## 13. Maintenance Concept ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)

The maintenance concept shall support modular inspection, fault isolation, removal, installation, and return-to-service verification.

Maintenance content should be structured around:

- access requirements;
- safety precautions;
- isolation conditions;
- required tools and test equipment;
- inspection criteria;
- functional test criteria;
- fault isolation logic;
- replacement boundaries;
- close-up and return-to-service checks.

Maintenance procedures shall remain provisional until validated against the applicable [DMRL](#glossary-dmrl), [BREX](#glossary-brex), and task validation records.

---

## 14. S1000D / CSDB Mapping ![TBD](https://img.shields.io/badge/TBD-red)

| S1000D Element | Controlled Value | Status |
|---|---|---|
| Model ident code | `AMPEL360E` | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| System diff code | `EWTW` | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| System code | `066` | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| Sub-system code | `0` | ![TBD](https://img.shields.io/badge/TBD-red) |
| Sub-sub-system code | `90` | ![TBD](https://img.shields.io/badge/TBD-red) |
| Assy code | `00A` | ![TBD](https://img.shields.io/badge/TBD-red) |
| Info code | `040 / 300 / 400 / 520 / 720 / 941` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| Item location code | `D` | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| DMC prefix | [`DMC-AMPEL360E-EWTW-066-090`](TBD) | ![TBD](https://img.shields.io/badge/TBD-red) |

### Recommended Data Module Set

| Info code | Data module purpose | Suggested filename | Status |
|---:|---|---|---|
| [040](#dm-040) | <a id="dm-040"></a>Descriptive information | [`DMC-AMPEL360E-EWTW-066-090-040A-D_System-Description.xml`](TBD) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| [300](#dm-300) | <a id="dm-300"></a>Examination / inspection / check | [`DMC-AMPEL360E-EWTW-066-090-300A-D_Inspection.xml`](TBD) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| [400](#dm-400) | <a id="dm-400"></a>Fault isolation | [`DMC-AMPEL360E-EWTW-066-090-400A-D_Fault-Isolation.xml`](TBD) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| [520](#dm-520) | <a id="dm-520"></a>Remove / disassemble | [`DMC-AMPEL360E-EWTW-066-090-520A-D_Remove.xml`](TBD) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| [720](#dm-720) | <a id="dm-720"></a>Install / assemble / connect | [`DMC-AMPEL360E-EWTW-066-090-720A-D_Install.xml`](TBD) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| [941](#dm-941) | <a id="dm-941"></a>Illustrated parts data | [`DMC-AMPEL360E-EWTW-066-090-941A-D_Illustrated-Parts-Data.xml`](TBD) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |

---

## 15. Footprints ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)

### 15.1 Physical Footprint

| Footprint Item | Description | Status |
|---|---|---|
| Installation zone | TBD — aircraft zone or compartment. | ![TBD](https://img.shields.io/badge/TBD-red) |
| Access panels | TBD — relevant access points. | ![TBD](https://img.shields.io/badge/TBD-red) |
| Mounting provisions | TBD — rack, bracket, panel, structural attachment. | ![TBD](https://img.shields.io/badge/TBD-red) |
| Clearance envelope | TBD — required removal / installation clearance. | ![TBD](https://img.shields.io/badge/TBD-red) |
| Cooling / ventilation | TBD — thermal management interface. | ![TBD](https://img.shields.io/badge/TBD-red) |
| Drainage / leak path | TBD — if applicable. | ![TBD](https://img.shields.io/badge/TBD-red) |

### 15.2 Electrical / Data Footprint

| Footprint Item | Description | Status |
|---|---|---|
| Power supply | TBD — voltage / phase / bus source. | ![TBD](https://img.shields.io/badge/TBD-red) |
| Protection | TBD — circuit breaker / SSPC / fuse / electronic protection. | ![TBD](https://img.shields.io/badge/TBD-red) |
| Data buses | TBD — ARINC / AFDX / CAN / discrete / optical / other. | ![TBD](https://img.shields.io/badge/TBD-red) |
| Connectors | TBD — connector families or interface references. | ![TBD](https://img.shields.io/badge/TBD-red) |
| Bonding / grounding | TBD — bonding and grounding provision. | ![TBD](https://img.shields.io/badge/TBD-red) |
| EMC / EMI controls | TBD — shielding, segregation, filtering. | ![TBD](https://img.shields.io/badge/TBD-red) |

### 15.3 Maintenance Footprint

| Footprint Item | Description | Status |
|---|---|---|
| Access level | Line / base / shop | ![TBD](https://img.shields.io/badge/TBD-red) |
| Replaceable unit | LRU / SRU / assembly / panel | ![TBD](https://img.shields.io/badge/TBD-red) |
| Removal time | Estimated or controlled maintenance interval | ![TBD](https://img.shields.io/badge/TBD-red) |
| Required tools | Standard / special tools | ![TBD](https://img.shields.io/badge/TBD-red) |
| Required GSE | Ground support equipment | ![TBD](https://img.shields.io/badge/TBD-red) |
| Return-to-service check | Operational / functional / BITE check | ![TBD](https://img.shields.io/badge/TBD-red) |

### 15.4 Data Footprint

| Footprint Item | Description | Status |
|---|---|---|
| Configuration records | Part number, serial number, software load, effectivity | ![TBD](https://img.shields.io/badge/TBD-red) |
| Evidence records | Test, inspection, compliance, review records | ![TBD](https://img.shields.io/badge/TBD-red) |
| CSDB records | DMCs, ICNs, BREX, applicability | ![TBD](https://img.shields.io/badge/TBD-red) |
| Maintenance data | Fault history, BITE, removal/installation records | ![TBD](https://img.shields.io/badge/TBD-red) |
| Cybersecurity records | Access, load authorization, integrity checks | ![TBD](https://img.shields.io/badge/TBD-red) |

---

## 16. Safety and Certification Considerations ![TBD](https://img.shields.io/badge/TBD-red)

The system shall be assessed according to its aircraft-level function, failure effects, operational criticality, and integration dependencies.

The certification and safety analysis shall consider:

- functional hazard assessment;
- failure modes and effects;
- common-cause failures;
- degraded-mode behavior;
- latent failures;
- maintenance-induced failures;
- incorrect installation;
- incorrect configuration;
- loss of indication or misleading indication;
- software and hardware assurance levels where applicable;
- environmental qualification;
- electromagnetic compatibility;
- continued airworthiness impact.

Final safety classification shall remain **TBD** ![TBD](https://img.shields.io/badge/TBD-red) until reviewed against the applicable [FHA](#glossary-fha), [PSSA](#glossary-pssa), [SSA](#glossary-ssa), and certification basis.

---

## 17. Verification and Validation ![DRAFT](https://img.shields.io/badge/DRAFT-yellow)

Verification shall demonstrate that the system satisfies its requirements under nominal, degraded, maintenance, and failure conditions.

| Verification Method | Description | Evidence | Status |
|---|---|---|---|
| [Analysis](#verification-analysis) | <a id="verification-analysis"></a>Engineering calculation, modelling, simulation, or safety analysis. | [Analysis report](#20-references) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| [Inspection](#verification-inspection) | <a id="verification-inspection"></a>Physical or visual verification of installation, marking, routing, or condition. | [Inspection record](#20-references) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| [Test](#verification-test) | <a id="verification-test"></a>Functional, environmental, integration, or system test. | [Test report](#20-references) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| [Demonstration](#verification-demonstration) | <a id="verification-demonstration"></a>Operational demonstration under controlled conditions. | [Demonstration record](#20-references) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| [Similarity](#verification-similarity) | <a id="verification-similarity"></a>Justified reuse of existing certified design evidence. | [Similarity report](#20-references) | ![TBD](https://img.shields.io/badge/TBD-red) |

---

## 18. Glossary of Terms and Acronyms

| Term / Acronym | Meaning | Link | Status |
|---|---|---|---|
| <a id="glossary-ampel360e"></a>AMPEL360e | Electrified aircraft programme family used as the programme example. | [Programme](../../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| <a id="glossary-atlas"></a>ATLAS | Aircraft Top Level Architecture Schema/System. | [ATLAS 000-099](../../../) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| <a id="glossary-bite"></a>BITE | Built-In Test Equipment. | [Monitoring and Diagnostics](#12-monitoring-and-diagnostics) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| <a id="glossary-brex"></a>BREX | Business Rules Exchange; S1000D rule set used to validate data-module content. | TBD | ![TBD](https://img.shields.io/badge/TBD-red) |
| <a id="glossary-ccb"></a>CCB | Configuration Control Board. | [Governance](../../../../../Governance/) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| <a id="glossary-csdb"></a>CSDB | Common Source DataBase. | [S1000D / CSDB Mapping](#14-s1000d--csdb-mapping) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| <a id="glossary-dmc"></a>DMC | Data Module Code. | [S1000D DMC Mapping](#14-s1000d--csdb-mapping) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| <a id="glossary-dmrl"></a>DMRL | Data Module Requirement List. | TBD | ![TBD](https://img.shields.io/badge/TBD-red) |
| <a id="glossary-ewtw"></a>eWTW | Electric Wide Tube-and-Wing. | [Programme](../../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| <a id="glossary-fadec"></a>FADEC | Full Authority Digital Engine Control. | [Engine Controls](../067_Engine-Controls/) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| <a id="glossary-fha"></a>FHA | Functional Hazard Assessment. | [Safety and Certification](#16-safety-and-certification-considerations) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| <a id="glossary-lru"></a>LRU | Line Replaceable Unit. | [Maintenance Concept](#13-maintenance-concept) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| <a id="glossary-pssa"></a>PSSA | Preliminary System Safety Assessment. | [Safety and Certification](#16-safety-and-certification-considerations) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| <a id="glossary-s1000d"></a>S1000D | International specification for technical publications using a common source database. | [S1000D](https://s1000d.org/) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| <a id="glossary-sns"></a>SNS | Standard Numbering System. | [S1000D / CSDB Mapping](#14-s1000d--csdb-mapping) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| <a id="glossary-ssa"></a>SSA | System Safety Assessment. | [Safety and Certification](#16-safety-and-certification-considerations) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| <a id="glossary-tbd"></a>TBD | To Be Determined. | [Open Issues](#21-open-issues) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |

---

## 19. Citations ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)

| Ref | Citation | Use | Link | Status |
|---|---|---|---|---|
| [CIT-001](#cit-001) | <a id="cit-001"></a>`S1000D Issue 5.0, Part I — Introduction and overview.` | Architecture / terminology | [S1000D](https://s1000d.org/) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| [CIT-002](#cit-002) | <a id="cit-002"></a>`EASA CS-25, Amendment 27 — Airworthiness Standards: Large Aeroplanes.` | Certification basis | [EASA](https://www.easa.europa.eu/) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| [CIT-003](#cit-003) | <a id="cit-003"></a>`AMPEL360e Programme Architecture Baseline, Rev TBD.` | Programme-specific requirement | [Programme baseline](../../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/) | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| [CIT-004](#cit-004) | <a id="cit-004"></a>`ATA iSpec 2200, Chapter 66 — Air Compressor.` | ATA reference | TBD | ![TBD](https://img.shields.io/badge/TBD-red) |
| [CIT-005](#cit-005) | <a id="cit-005"></a>`DO-160G — Environmental Conditions and Test Procedures for Airborne Equipment.` | Environmental qualification | TBD | ![TBD](https://img.shields.io/badge/TBD-red) |

---

## 20. References ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)

| Ref | Document | Identifier | Revision | Status | Link |
|---|---|---|---:|---|---|
| [REF-001](#ref-001) | <a id="ref-001"></a>Q+ATLANTIDE ATLAS master index | `QATL-ATLAS-000-099` | TBD | ![TBD](https://img.shields.io/badge/TBD-red) | [Open](../../../) |
| [REF-002](#ref-002) | <a id="ref-002"></a>AMPEL360e programme architecture baseline | `AMP360E-ARCH-BASELINE` | TBD | ![TBD](https://img.shields.io/badge/TBD-red) | [Open](../../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/) |
| [REF-003](#ref-003) | <a id="ref-003"></a>060-069 Propulsión Tradicional section index | `QATL-ATLAS-060-069` | TBD | ![TBD](https://img.shields.io/badge/TBD-red) | [Open](../../) |
| [REF-004](#ref-004) | <a id="ref-004"></a>066 Air Compressor subsection index | `QATL-ATLAS-060-069-066` | TBD | ![TBD](https://img.shields.io/badge/TBD-red) | [Open](../) |
| [REF-005](#ref-005) | <a id="ref-005"></a>S1000D project BREX | `BREX-AMPEL360E-EWTW` | TBD | ![TBD](https://img.shields.io/badge/TBD-red) | TBD |
| [REF-ATA](#ref-ata) | <a id="ref-ata"></a>ATA iSpec 2200 — Chapter 66 | `ATA-ISPEC-2200-66` | TBD | ![TBD](https://img.shields.io/badge/TBD-red) | TBD |

---

## 21. Open Issues

| ID | Issue | Owner | Status | Badge | Link |
|---|---|---|---|---|---|
| [OI-001](#oi-001) | <a id="oi-001"></a>Confirm final system boundary for S1000D / CSDB Mapping and Traceability. | System expert | TBD | ![TBD](https://img.shields.io/badge/TBD-red) | [Architecture Description](#5-architecture-description) |
| [OI-002](#oi-002) | <a id="oi-002"></a>Complete S1000D SNS allocation for 066-090. | Q-DATAGOV | To Be Completed | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) | [S1000D / CSDB Mapping](#14-s1000d--csdb-mapping) |
| [OI-003](#oi-003) | <a id="oi-003"></a>Confirm certification basis and safety classification. | Certification lead | TBD | ![TBD](https://img.shields.io/badge/TBD-red) | [Safety and Certification](#16-safety-and-certification-considerations) |
| [OI-004](#oi-004) | <a id="oi-004"></a>Confirm maintenance task allocation in DMRL. | Tech pubs lead | To Be Completed | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) | [Maintenance Concept](#13-maintenance-concept) |

---

## 22. Status Legend

| Badge | Meaning | Use |
|---|---|---|
| ![TBD](https://img.shields.io/badge/TBD-red) | To Be Determined | Required value, source, boundary, interface, requirement, or evidence is not yet determined. |
| ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) | To Be Completed | Section exists but content is intentionally incomplete. |
| ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) | Draft | Content exists but is not yet reviewed, frozen, or baselined. |
| ![DONE](https://img.shields.io/badge/DONE-brightgreen) | Done | Content has been reviewed and is complete for the current baseline. |

---

## 23. Change Log

| Revision | Date | Author | Change | Link | Status |
|---|---|---|---|---|---|
| [0.1.0](#chg-010) | <a id="chg-010"></a>2026-05-11 | Q+ Team / Amedeo Pelliccia + AI | Initial programme-controlled scaffold. | [Document root](#atlas-060-069--section-06--subsection-066--090--s1000d---csdb-mapping-and-traceability) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |

---

> Programme-controlled scaffold. Content is subject to [BREX](#glossary-brex), [SNS](#glossary-sns), applicability, [DMRL](#glossary-dmrl), evidence review, and [CCB](#glossary-ccb) freeze before controlled release.

> **To be reviewed by system expert.**
