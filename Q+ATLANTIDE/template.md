---
document_id: "QATL-ATLAS-<BAND>-<NODE>-<SECTION>-<SUBJECT>"
title: "<CODE> — <Controlled Title>"
short_title: "<Short Controlled Title>"

programme: "AMPEL360e Wide Tube-and-Wing Family"
programme_link: "../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/"
short_code: "eWTW"

register: "Q+ATLANTIDE"
register_link: "../../../../Q+ATLANTIDE/"
architecture_band: "000-099_ATLAS"
architecture_band_link: "../../"
architecture_band_title: "New Commercial Aircraft Architectures"

code_range: "<040-049_Avionica-Informacion-y-APU>"
code_range_link: "../"
code_range_title: "<Controlled Range Title>"

node_code: "<CODE>"
node_title: "<Controlled Node Title>"
node_link: "./"

parent_path: "Q+ATLANTIDE/000-099_ATLAS/<CODE-RANGE>/<NODE>/"
parent_path_link: "./"
file_name: "<CODE>-<SECTION>-<Controlled-File-Name>.md"

ata_reference: "ATA <XX>"
ata_reference_link: "#20-references"

s1000d_applicability: "S1000D-CSDB-compatible"
s1000d_link: "https://s1000d.org/"

sns_reference: "<SNS if applicable>"
dmc_prefix: "DMC-AMPEL360E-EWTW-<SNS>"
csdb_path: "<S1000D-CSDB path if applicable>"
csdb_path_link: "<relative-link-to-csdb-path-or-TBD>"

domain: "A-Aerospace"
domain_link: "../../../../IDEALE-ESG/A-Aerospace/"

primary_q_division: "<Q-DATAGOV>"
primary_q_division_link: "../../../../Q-Divisions/Q-DATAGOV/"

support_q_divisions:
  - name: "<Q-AIR>"
    link: "../../../../Q-Divisions/Q-AIR/"
  - name: "<Q-HPC>"
    link: "../../../../Q-Divisions/Q-HPC/"
  - name: "<Q-INDUSTRY>"
    link: "../../../../Q-Divisions/Q-INDUSTRY/"

orb_functions:
  - name: "ORB-PMO"
    link: "../../../../ORB-Functions/ORB-PMO/"
  - name: "ORB-LEG"
    link: "../../../../ORB-Functions/ORB-LEG/"

lifecycle_phase:
  - code: "LC02"
    title: "Requirements Definition"
    link: "../../../../Governance/Lifecycle/LC02-Requirements-Definition.md"
  - code: "LC03"
    title: "Architecture Definition"
    link: "../../../../Governance/Lifecycle/LC03-Architecture-Definition.md"
  - code: "LC05"
    title: "Detailed Design"
    link: "../../../../Governance/Lifecycle/LC05-Detailed-Design.md"
  - code: "LC06"
    title: "Verification Planning"
    link: "../../../../Governance/Lifecycle/LC06-Verification-Planning.md"
  - code: "LC10"
    title: "Certification / Approval"
    link: "../../../../Governance/Lifecycle/LC10-Certification-Approval.md"
  - code: "LC11"
    title: "Operation"
    link: "../../../../Governance/Lifecycle/LC11-Operation.md"
  - code: "LC12"
    title: "Maintenance / Support"
    link: "../../../../Governance/Lifecycle/LC12-Maintenance-Support.md"

classification: "open-technical-scaffold"
status: "programme-controlled-scaffold-placeholder"
revision: "0.1.0"
created: "2026-05-09"
updated: "2026-05-09"
authoring_mode: "deterministic-technical-publication"
review_status: "to-be-reviewed-by-system-expert"

traceability:
  atlas_node: "<CODE>_<NODE-TITLE>"
  atlas_node_link: "./"
  parent_branch: "<Parent branch path>"
  parent_branch_link: "../"
  programme_path: "Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family"
  programme_path_link: "../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/"
  csdb_path: "<S1000D-CSDB path if applicable>"
  csdb_path_link: "<relative-link-to-csdb-path-or-TBD>"
  evidence_status: "draft"
  brex_status: "not-yet-validated"
  brex_link: "<relative-link-to-brex-or-TBD>"
  dmrl_status: "not-yet-frozen"
  dmrl_link: "<relative-link-to-dmrl-or-TBD>"

keywords:
  - "Q+ATLANTIDE"
  - "ATLAS"
  - "AMPEL360e"
  - "S1000D"
  - "CSDB"
  - "<system keyword>"
---

# <CODE> — <Controlled Title>

## 0. Hyperlink Policy

All linkable content in this file shall be expressed as Markdown links where a stable target exists.

Use:

- relative links for repository-internal content;
- anchor links for headings, figures, diagrams, glossary terms, citations, references, and open issues;
- stable external links only for public standards or authoritative sources;
- `TBD` or `<relative-link-or-TBD>` where no stable target exists.

Do not invent links.

---

## 1. Purpose

This document defines the controlled technical scope for **<Controlled Title>** within the [Q+ATLANTIDE](../../../../Q+ATLANTIDE/) / [ATLAS 000-099](../../) architecture branch.

The objective is to provide a deterministic, [S1000D](https://s1000d.org/)-compatible technical baseline for [system architecture definition](#5-architecture-description), [maintenance documentation](#13-maintenance-concept), [configuration control](#14-s1000d--csdb-mapping), [verification planning](#17-verification-and-validation), and [lifecycle traceability](#9-mermaid--lifecycle-traceability).

This file belongs to:

[`Q+ATLANTIDE/000-099_ATLAS/<CODE-RANGE>/<NODE>/<FILE>`](./)

---

## 2. Applicability

This document applies to the [AMPEL360e Wide Tube-and-Wing Family](../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/) programme and the **eWTW** configuration.

| Applicability Item | Value |
|---|---|
| Programme | [AMPEL360e Wide Tube-and-Wing Family](../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/) |
| Short code | [eWTW](#glossary-ewtw) |
| Architecture register | [Q+ATLANTIDE](../../../../Q+ATLANTIDE/) |
| ATLAS band | [000-099_ATLAS](../../) |
| ATA reference | [ATA <XX>](#ref-ata) |
| S1000D compatibility | [S1000D-CSDB-compatible](https://s1000d.org/) |
| Lifecycle use | [LC03](../../../../Governance/Lifecycle/LC03-Architecture-Definition.md) / [LC05](../../../../Governance/Lifecycle/LC05-Detailed-Design.md) / [LC06](../../../../Governance/Lifecycle/LC06-Verification-Planning.md) / [LC11](../../../../Governance/Lifecycle/LC11-Operation.md) / [LC12](../../../../Governance/Lifecycle/LC12-Maintenance-Support.md) |

---

## 3. System / Function Overview

The **<Controlled Title>** node covers the architecture, interfaces, operational logic, maintenance boundaries, and traceability requirements associated with this system or function.

For the [AMPEL360e](#glossary-ampel360e) configuration, the node shall be treated as part of a full-electric, medium-range, approximately 100-passenger aircraft architecture. Where conventional aircraft assumptions rely on engine bleed, hydraulic supply, pneumatic supply, or legacy equipment, the AMPEL360e implementation shall be explicitly reviewed for electric, distributed, or digitally controlled alternatives.

This document does not freeze the final certified design. It establishes a controlled scaffold for downstream engineering, [S1000D](#glossary-s1000d) data-module planning, [CSDB](#glossary-csdb) integration, and evidence capture.

---

## 4. Scope

### 4.1 Included

This document includes:

- controlled definition of the system or function;
- architecture boundaries;
- major equipment and component classes;
- operating modes;
- interfaces with adjacent aircraft systems;
- monitoring and diagnostics;
- maintenance and inspection implications;
- [S1000D / CSDB](#14-s1000d--csdb-mapping) mapping logic;
- lifecycle evidence requirements.

### 4.2 Excluded

This document excludes:

- supplier-proprietary internal design data unless released to the programme baseline;
- final certification compliance statements;
- detailed maintenance procedures unless assigned by the [DMRL](#glossary-dmrl);
- final illustrated parts data unless released through the [CSDB](#glossary-csdb);
- production-level configuration until [CCB](#glossary-ccb) freeze.

---

## 5. Architecture Description

The **<Controlled Title>** architecture is organized around controlled interfaces, deterministic function allocation, and maintainable component boundaries.

At architecture level, the system shall be described in terms of:

1. **Function** — what the system does.
2. **Equipment** — which [LRUs](#glossary-lru), assemblies, panels, modules, or components implement the function.
3. **Interfaces** — how the system exchanges power, data, fluid, air, signal, force, or commands.
4. **Control logic** — how the system is commanded, monitored, degraded, isolated, or reset.
5. **Maintenance boundary** — what a technician can inspect, test, remove, install, or replace.
6. **Evidence boundary** — which requirements, tests, inspections, and records prove compliance.

---

## 6. Functional Breakdown

| Ref | Function | Description | Primary Interface |
|---:|---|---|---|
| [F-001](#f-001) | <a id="f-001"></a><Function 1> | <Describe the first controlled function.> | [Interface](#10-interfaces) |
| [F-002](#f-002) | <a id="f-002"></a><Function 2> | <Describe the second controlled function.> | [Interface](#10-interfaces) |
| [F-003](#f-003) | <a id="f-003"></a><Function 3> | <Describe the third controlled function.> | [Interface](#10-interfaces) |
| [F-004](#f-004) | <a id="f-004"></a>Monitoring | Captures status, failures, degradation, and maintenance data. | [CMS / BITE](#12-monitoring-and-diagnostics) |
| [F-005](#f-005) | <a id="f-005"></a>Traceability | Links architecture, requirements, evidence, and S1000D content. | [CSDB / DMRL / BREX](#14-s1000d--csdb-mapping) |

---

## 7. Mermaid — System Context Diagram

<a id="diagram-system-context"></a>

```mermaid
flowchart LR
    A[Aircraft-Level Function] --> B[<Controlled Node>]
    B --> C[Power Interface]
    B --> D[Data / Control Interface]
    B --> E[Mechanical / Fluid / Air Interface]
    B --> F[Monitoring and Diagnostics]
    F --> G[Central Maintenance System]
    G --> H[S1000D / CSDB Evidence]
````

***[Diagram 1](#diagram-system-context) — System context diagram for <Controlled Title>. Related sections: [Interfaces](#10-interfaces), [Monitoring and Diagnostics](#12-monitoring-and-diagnostics), [S1000D / CSDB Mapping](#14-s1000d--csdb-mapping).***

---

## 8. Mermaid — Internal Functional Architecture

<a id="diagram-internal-functional-architecture"></a>

```mermaid
flowchart TB
    SYS[<Controlled Title>] --> F1[Function 1]
    SYS --> F2[Function 2]
    SYS --> F3[Function 3]
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

## 10. Interfaces

| Interface Type        | Connected System                                      | Description                                                   | Evidence Required                        |
| --------------------- | ----------------------------------------------------- | ------------------------------------------------------------- | ---------------------------------------- |
| Electrical power      | [<ATA / ATLAS node>](relative-link-or-TBD)            | <Describe power interface.>                                   | [Wiring / load analysis](#20-references) |
| Data / control        | [IMA / CMS / controller](relative-link-or-TBD)        | <Describe command and monitoring interface.>                  | [ICD / data dictionary](#20-references)  |
| Mechanical            | [Structure / installation zone](relative-link-or-TBD) | <Describe mounting, access, or load path.>                    | [Installation drawing](#20-references)   |
| Fluid / air / thermal | [Adjacent system](relative-link-or-TBD)               | <Describe flow, pressure, temperature, or thermal interface.> | [Test report](#20-references)            |
| Maintenance           | [CSDB / IETP](relative-link-or-TBD)                   | <Describe technician-facing access and procedure boundary.>   | [DMRL / BREX](#14-s1000d--csdb-mapping)  |

---

## 11. Operating Modes

| Mode                                             | Description                                                                                                  | Entry Condition                             | Exit Condition                                    |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------- | ------------------------------------------------- |
| [Normal](#mode-normal)                           | <a id="mode-normal"></a>System operates within nominal limits.                                               | Aircraft powered and system enabled.        | Shutdown, fault, or mode change.                  |
| [Degraded](#mode-degraded)                       | <a id="mode-degraded"></a>System operates with reduced function or redundancy.                               | Fault detected or partial loss of function. | Recovery, isolation, or maintenance action.       |
| [Maintenance](#mode-maintenance)                 | <a id="mode-maintenance"></a>System is configured for inspection, test, removal, installation, or servicing. | Authorized maintenance action.              | Maintenance close-up and operational check.       |
| [Failure / Safe State](#mode-failure-safe-state) | <a id="mode-failure-safe-state"></a>System enters protective state to prevent unsafe operation.              | Fault threshold exceeded.                   | Reset, repair, replacement, or dispatch decision. |

---

## 12. Monitoring and Diagnostics

The system shall provide sufficient monitoring to support safe operation, maintenance troubleshooting, and lifecycle evidence capture.

Monitoring may include:

* status indication;
* fault detection;
* [BITE](#glossary-bite) results;
* sensor plausibility checks;
* degraded-mode reporting;
* maintenance messages;
* event recording;
* configuration status;
* software or hardware part-number reporting where applicable.

Diagnostic data shall be mapped to the relevant [S1000D / CSDB](#14-s1000d--csdb-mapping) fault isolation and maintenance data modules.

---

## 13. Maintenance Concept

The maintenance concept shall support modular inspection, fault isolation, removal, installation, and return-to-service verification.

Maintenance content should be structured around:

* access requirements;
* safety precautions;
* isolation conditions;
* required tools and test equipment;
* inspection criteria;
* functional test criteria;
* fault isolation logic;
* replacement boundaries;
* close-up and return-to-service checks.

Maintenance procedures shall remain provisional until validated against the applicable [DMRL](#glossary-dmrl), [BREX](#glossary-brex), and task validation records.

---

## 14. S1000D / CSDB Mapping

| S1000D Element      | Controlled Value                                                |
| ------------------- | --------------------------------------------------------------- |
| Model ident code    | `AMPEL360E`                                                     |
| System diff code    | `EWTW`                                                          |
| System code         | `<XXX>`                                                         |
| Sub-system code     | `<X>`                                                           |
| Sub-sub-system code | `<XX>`                                                          |
| Assy code           | `<XXA>`                                                         |
| Info code           | `<040 / 300 / 400 / 520 / 720 / 941>`                           |
| Item location code  | `D`                                                             |
| DMC prefix          | [`DMC-AMPEL360E-EWTW-<SNS>`](relative-link-to-csdb-path-or-TBD) |

### Recommended Data Module Set

|      Info code | Data module purpose                                 | Suggested filename                                                                   |
| -------------: | --------------------------------------------------- | ------------------------------------------------------------------------------------ |
| [040](#dm-040) | <a id="dm-040"></a>Descriptive information          | [`DMC-AMPEL360E-EWTW-<SNS>-040A-D_System-Description.xml`](relative-link-or-TBD)     |
| [300](#dm-300) | <a id="dm-300"></a>Examination / inspection / check | [`DMC-AMPEL360E-EWTW-<SNS>-300A-D_Inspection.xml`](relative-link-or-TBD)             |
| [400](#dm-400) | <a id="dm-400"></a>Fault isolation                  | [`DMC-AMPEL360E-EWTW-<SNS>-400A-D_Fault-Isolation.xml`](relative-link-or-TBD)        |
| [520](#dm-520) | <a id="dm-520"></a>Remove / disassemble             | [`DMC-AMPEL360E-EWTW-<SNS>-520A-D_Remove.xml`](relative-link-or-TBD)                 |
| [720](#dm-720) | <a id="dm-720"></a>Install / assemble / connect     | [`DMC-AMPEL360E-EWTW-<SNS>-720A-D_Install.xml`](relative-link-or-TBD)                |
| [941](#dm-941) | <a id="dm-941"></a>Illustrated parts data           | [`DMC-AMPEL360E-EWTW-<SNS>-941A-D_Illustrated-Parts-Data.xml`](relative-link-or-TBD) |

---

## 15. Footprints

### 15.1 Physical Footprint

| Footprint Item        | Description                                    | Status |
| --------------------- | ---------------------------------------------- | ------ |
| Installation zone     | <Aircraft zone or compartment.>                | TBD    |
| Access panels         | <Relevant access points.>                      | TBD    |
| Mounting provisions   | <Rack, bracket, panel, structural attachment.> | TBD    |
| Clearance envelope    | <Required removal / installation clearance.>   | TBD    |
| Cooling / ventilation | <Thermal management interface.>                | TBD    |
| Drainage / leak path  | <If applicable.>                               | TBD    |

### 15.2 Electrical / Data Footprint

| Footprint Item      | Description                                              | Status |
| ------------------- | -------------------------------------------------------- | ------ |
| Power supply        | <Voltage / phase / bus source.>                          | TBD    |
| Protection          | <Circuit breaker / SSPC / fuse / electronic protection.> | TBD    |
| Data buses          | <ARINC / AFDX / CAN / discrete / optical / other.>       | TBD    |
| Connectors          | <Connector families or interface references.>            | TBD    |
| Bonding / grounding | <Bonding and grounding provision.>                       | TBD    |
| EMC / EMI controls  | <Shielding, segregation, filtering.>                     | TBD    |

### 15.3 Maintenance Footprint

| Footprint Item          | Description                                  | Status |
| ----------------------- | -------------------------------------------- | ------ |
| Access level            | Line / base / shop                           | TBD    |
| Replaceable unit        | LRU / SRU / assembly / panel                 | TBD    |
| Removal time            | Estimated or controlled maintenance interval | TBD    |
| Required tools          | Standard / special tools                     | TBD    |
| Required GSE            | Ground support equipment                     | TBD    |
| Return-to-service check | Operational / functional / BITE check        | TBD    |

### 15.4 Data Footprint

| Footprint Item        | Description                                            | Status |
| --------------------- | ------------------------------------------------------ | ------ |
| Configuration records | Part number, serial number, software load, effectivity | TBD    |
| Evidence records      | Test, inspection, compliance, review records           | TBD    |
| CSDB records          | DMCs, ICNs, BREX, applicability                        | TBD    |
| Maintenance data      | Fault history, BITE, removal/installation records      | TBD    |
| Cybersecurity records | Access, load authorization, integrity checks           | TBD    |

---

## 16. Safety and Certification Considerations

The system shall be assessed according to its aircraft-level function, failure effects, operational criticality, and integration dependencies.

The certification and safety analysis shall consider:

* functional hazard assessment;
* failure modes and effects;
* common-cause failures;
* degraded-mode behavior;
* latent failures;
* maintenance-induced failures;
* incorrect installation;
* incorrect configuration;
* loss of indication or misleading indication;
* software and hardware assurance levels where applicable;
* environmental qualification;
* electromagnetic compatibility;
* continued airworthiness impact.

Final safety classification shall remain **TBD** until reviewed against the applicable [FHA](#glossary-fha), [PSSA](#glossary-pssa), [SSA](#glossary-ssa), and certification basis.

---

## 17. Verification and Validation

Verification shall demonstrate that the system satisfies its requirements under nominal, degraded, maintenance, and failure conditions.

| Verification Method                          | Description                                                                                                          | Evidence                               |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| [Analysis](#verification-analysis)           | <a id="verification-analysis"></a>Engineering calculation, modelling, simulation, or safety analysis.                | [Analysis report](#20-references)      |
| [Inspection](#verification-inspection)       | <a id="verification-inspection"></a>Physical or visual verification of installation, marking, routing, or condition. | [Inspection record](#20-references)    |
| [Test](#verification-test)                   | <a id="verification-test"></a>Functional, environmental, integration, or system test.                                | [Test report](#20-references)          |
| [Demonstration](#verification-demonstration) | <a id="verification-demonstration"></a>Operational demonstration under controlled conditions.                        | [Demonstration record](#20-references) |
| [Similarity](#verification-similarity)       | <a id="verification-similarity"></a>Justified reuse of existing certified design evidence.                           | [Similarity report](#20-references)    |

---

## 18. Glossary of Terms and Acronyms

| Term / Acronym                           | Meaning                                                                                | Link                                                                                 |
| ---------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| <a id="glossary-ampel360e"></a>AMPEL360e | Electrified aircraft programme family used as the programme example.                   | [Programme](../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/) |
| <a id="glossary-atlas"></a>ATLAS         | Aircraft Top Level Architecture Schema/System.                                         | [ATLAS 000-099](../../)                                                              |
| <a id="glossary-bite"></a>BITE           | Built-In Test Equipment.                                                               | [Monitoring and Diagnostics](#12-monitoring-and-diagnostics)                         |
| <a id="glossary-brex"></a>BREX           | Business Rules Exchange; S1000D rule set used to validate data-module content.         | [BREX](relative-link-or-TBD)                                                         |
| <a id="glossary-ccb"></a>CCB             | Configuration Control Board.                                                           | [Governance](../../../../Governance/)                                                |
| <a id="glossary-csdb"></a>CSDB           | Common Source DataBase.                                                                | [S1000D / CSDB Mapping](#14-s1000d--csdb-mapping)                                    |
| <a id="glossary-dmc"></a>DMC             | Data Module Code.                                                                      | [S1000D DMC Mapping](#14-s1000d--csdb-mapping)                                       |
| <a id="glossary-dmrl"></a>DMRL           | Data Module Requirement List.                                                          | [DMRL](relative-link-or-TBD)                                                         |
| <a id="glossary-ewtw"></a>eWTW           | Electric Wide Tube-and-Wing.                                                           | [Programme](../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/) |
| <a id="glossary-fha"></a>FHA             | Functional Hazard Assessment.                                                          | [Safety and Certification](#16-safety-and-certification-considerations)              |
| <a id="glossary-ietp"></a>IETP           | Interactive Electronic Technical Publication.                                          | [S1000D](https://s1000d.org/)                                                        |
| <a id="glossary-lc"></a>LC               | Lifecycle phase code.                                                                  | [Lifecycle Governance](../../../../Governance/Lifecycle/)                            |
| <a id="glossary-lru"></a>LRU             | Line Replaceable Unit.                                                                 | [Maintenance Concept](#13-maintenance-concept)                                       |
| <a id="glossary-pssa"></a>PSSA           | Preliminary System Safety Assessment.                                                  | [Safety and Certification](#16-safety-and-certification-considerations)              |
| <a id="glossary-qdatagov"></a>Q-DATAGOV  | Q-Division responsible for data governance, digital architecture, and traceability.    | [Q-DATAGOV](../../../../Q-Divisions/Q-DATAGOV/)                                      |
| <a id="glossary-s1000d"></a>S1000D       | International specification for technical publications using a common source database. | [S1000D](https://s1000d.org/)                                                        |
| <a id="glossary-sns"></a>SNS             | Standard Numbering System.                                                             | [S1000D / CSDB Mapping](#14-s1000d--csdb-mapping)                                    |
| <a id="glossary-ssa"></a>SSA             | System Safety Assessment.                                                              | [Safety and Certification](#16-safety-and-certification-considerations)              |
| <a id="glossary-tbc"></a>TBC             | To Be Confirmed.                                                                       | [Open Issues](#21-open-issues)                                                       |
| <a id="glossary-tbd"></a>TBD             | To Be Determined.                                                                      | [Open Issues](#21-open-issues)                                                       |

---

## 19. Citations

| Ref                 | Citation                                                                | Use                            | Link                                                                                          |
| ------------------- | ----------------------------------------------------------------------- | ------------------------------ | --------------------------------------------------------------------------------------------- |
| [CIT-001](#cit-001) | <a id="cit-001"></a>`<Standard or source title>, <edition>, <section>.` | Architecture / terminology     | [Source](stable-link-or-TBD)                                                                  |
| [CIT-002](#cit-002) | <a id="cit-002"></a>`<Regulatory source>, <paragraph>.`                 | Certification basis            | [Source](stable-link-or-TBD)                                                                  |
| [CIT-003](#cit-003) | <a id="cit-003"></a>`<Programme document>, <revision>.`                 | Programme-specific requirement | [Programme baseline](../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/) |
| [CIT-004](#cit-004) | <a id="cit-004"></a>`<Supplier document>, <revision>.`                  | Equipment-specific data        | [Supplier evidence](relative-link-or-TBD)                                                     |
| [CIT-005](#cit-005) | <a id="cit-005"></a>`<Test or analysis report>, <revision>.`            | Verification evidence          | [Evidence record](relative-link-or-TBD)                                                       |

---

## 20. References

| Ref                 | Document                                                      |                  Identifier | Revision | Status            | Link                                                                            |
| ------------------- | ------------------------------------------------------------- | --------------------------: | -------: | ----------------- | ------------------------------------------------------------------------------- |
| [REF-001](#ref-001) | <a id="ref-001"></a>Q+ATLANTIDE ATLAS master index            |        `QATL-ATLAS-000-099` |      TBD | Draft             | [Open](../../)                                                                  |
| [REF-002](#ref-002) | <a id="ref-002"></a>AMPEL360e programme architecture baseline |     `AMP360E-ARCH-BASELINE` |      TBD | Draft             | [Open](../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/) |
| [REF-003](#ref-003) | <a id="ref-003"></a>S1000D project BREX                       |       `BREX-AMPEL360E-EWTW` |      TBD | Draft             | [Open](relative-link-or-TBD)                                                    |
| [REF-004](#ref-004) | <a id="ref-004"></a>DMRL for applicable system                | `DMRL-AMPEL360E-EWTW-<SNS>` |      TBD | Draft             | [Open](relative-link-or-TBD)                                                    |
| [REF-005](#ref-005) | <a id="ref-005"></a>System safety assessment                  |    `SSA-AMPEL360E-<SYSTEM>` |      TBD | Planned           | [Open](relative-link-or-TBD)                                                    |
| [REF-ATA](#ref-ata) | <a id="ref-ata"></a>ATA iSpec 2200 reference                  |            `ATA-ISPEC-2200` |      TBD | External standard | [Source](stable-link-or-TBD)                                                    |

---

## 21. Open Issues

| ID                | Issue                                                                     | Owner              | Status | Link                                                                    |
| ----------------- | ------------------------------------------------------------------------- | ------------------ | ------ | ----------------------------------------------------------------------- |
| [OI-001](#oi-001) | <a id="oi-001"></a>Confirm final system boundary.                         | System expert      | Open   | [Architecture Description](#5-architecture-description)                 |
| [OI-002](#oi-002) | <a id="oi-002"></a>Confirm S1000D SNS allocation.                         | Q-DATAGOV          | Open   | [S1000D / CSDB Mapping](#14-s1000d--csdb-mapping)                       |
| [OI-003](#oi-003) | <a id="oi-003"></a>Confirm certification basis and safety classification. | Certification lead | Open   | [Safety and Certification](#16-safety-and-certification-considerations) |
| [OI-004](#oi-004) | <a id="oi-004"></a>Confirm maintenance task allocation in DMRL.           | Tech pubs lead     | Open   | [Maintenance Concept](#13-maintenance-concept)                          |

---

## 22. Change Log

| Revision          | Date                           | Author                | Change                                 | Link                                     |
| ----------------- | ------------------------------ | --------------------- | -------------------------------------- | ---------------------------------------- |
| [0.1.0](#chg-010) | <a id="chg-010"></a>2026-05-09 | GAIA-QAO / IDEALE-ESG | Initial programme-controlled scaffold. | [Document root](#code--controlled-title) |

---

> Programme-controlled scaffold. Content is subject to [BREX](#glossary-brex), [SNS](#glossary-sns), applicability, [DMRL](#glossary-dmrl), evidence review, and [CCB](#glossary-ccb) freeze before controlled release.

> **To be reviewed by system expert.**

```
```
