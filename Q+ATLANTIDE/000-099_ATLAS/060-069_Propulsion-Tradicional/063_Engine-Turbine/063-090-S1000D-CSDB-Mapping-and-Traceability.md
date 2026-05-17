---
document_id: "QATL-ATLAS-1000-ATLAS-060-069-063-090-S1000D---CSDB-MAPPING-AND-TRACEABILITY"
register: ATLAS-1000
title: "S1000D / CSDB Mapping and Traceability"
ata: "ATA 63"
sns: "063-090-00"
subsection: "063"
subsubject_code: "090"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-MECHANICS, Q-AIR, Q-INDUSTRY]
status: active
scope: agnostic-standard
governance_class: baseline
revision: "0.1"
date: "2026-05-11"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
parent_subsubject_doc: "./README.md"
s1000d_dmc: "DMC-<MODEL>-<SYSTEMDIFF>-063-090"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-060-069-063-090-S1000D---CSDB-MAPPING-AND-TRACEABILITY
     ATA 63 · S1000D / CSDB Mapping and Traceability
────────────────────────────────────────────────────────────────────────────── -->

# S1000D / CSDB Mapping and Traceability

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATA 63](https://img.shields.io/badge/ATA-63-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-DATAGOV](https://img.shields.io/badge/Q--Division-Q-DATAGOV-brightgreen)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden. Every linked document must exist in the Q+ATLANTIDE repository
> before the link is activated. Broken links are treated as open issues and must be resolved
> before the document is promoted from `DRAFT` to `APPROVED`.

---

## §1 Purpose

ATA 63 DMRL: 36 data modules. DMC `DMC-<MODEL>-<SYSTEMDIFF>-063-{NNN}-00A-EN-US`. BREX `BREX-063-v1` enforces: (1) all LLP DMs must cite engine TC and LLP life value; (2) HSI DMs must cite OEM-approved borescope procedure; (3) no DM may reference engine bleed air as aircraft pneumatic supply.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Programme | (defined in programme implementation branch) |
| ATA reference | ATA 63-090 — S1000D / CSDB Mapping and Traceability |
| Certification basis | EASA CS-25 Amdt 27+ |
| S1000D SNS | 063-090-00 |

---

## §3 Functional Description ![DRAFT]

ATA 63 DMRL: 36 data modules. DMC `DMC-<MODEL>-<SYSTEMDIFF>-063-{NNN}-00A-EN-US`. BREX `BREX-063-v1` enforces: (1) all LLP DMs must cite engine TC and LLP life value; (2) HSI DMs must cite OEM-approved borescope procedure; (3) no DM may reference engine bleed air as aircraft pneumatic supply.

---

## §4 Functional Breakdown

| ID | Name | Description | Lead Division |
|---|---|---|---|
| F-001 | S1000D Issue 5.0 | Primary function | Q-GREENTECH |
| F-002 | System integration | Interface management | Q-MECHANICS |
| F-003 | Monitoring | BITE and health data | Q-AIR |

---

## §5 System Context — Mermaid Diagram

```mermaid
flowchart LR
    A[Aircraft Level] --> B[S1000D / CSDB Mapping and Trac]
    B --> C[Primary Function]
    B --> D[Interfaces]
    B --> E[Monitoring]
    E --> F[CMS ATA 45]
```

---

## §6 Internal Architecture — Mermaid Diagram

```mermaid
flowchart TB
    SYS[S1000D / CSDB Mapping and] --> F1[Function 1]
    SYS --> F2[Function 2]
    SYS --> CTRL[Control]
    SYS --> MON[BITE Diagnostics]
    MON --> CMS[CMS AFDX]
```

---

## §7 Components and LRUs

| Component | Part Number | Qty | Location | Maintenance Interval | Notes |
|---|---|---|---|---|---|
| S1000D Issue 5.0 | S1000D.org | CSDB | IT | Per release | XML authoring standard |
| BREX-063-v1 | Programme doc | CSDB validator | IT | Per revision | Three domain constraints enforced |
| DMRL — 36 DMs | Q-DATAGOV tracker | PMO | PMO tool | Monthly status review | All 36 DMs tracked |
| ICN registry ATA 63 | Q-DATAGOV database | CSDB | IT | Continuous | Illustration traceability |
| ELM-DB + CSDB LLP evidence link | ELM-DB + CSDB | Q-DATAGOV + CAMO | IT | Continuous | LLP life evidence DMs |

---

## §8 Interfaces

| Interface Type | Connected System | Protocol / Medium | Data / Function |
|---|---|---|---|
| ATA 45 CMS | Central Maintenance System | AFDX ARINC 664 P7 | BITE faults and health data |
| ATA 24 Electrical Power | Power distribution | HVDC / 28 V DC | LRU power supply |
| ATA 67 Engine Controls | FADEC | ARINC 429 / AFDX | Control commands and feedback |
| ATA 31 ECAM | Cockpit display | AFDX | Crew indication and alerts |

---

## §9 Operating Modes

| Mode | Trigger | System State | Actions / Consequences |
|---|---|---|---|
| Normal operation | Aircraft/engine powered | Nominal | Full function active |
| Engine shutdown | Commanded or fault | FADEC stops fuel | System de-energised |
| Maintenance | Isolated | Aircraft grounded | LOTO active |
| Ground test | Post-maintenance | Engine on ground | Test pass before service |

---

## §10 Performance and Budgets ![DRAFT]

| Parameter | Requirement | Target / Design Value | Status |
|---|---|---|---|
| System availability | ≥ 99.9 % dispatch | RAMS analysis | TBD |
| BITE fault detection | ≥ 80 % coverage | BITE design analysis | TBD |

---

## §11 Safety, Redundancy and Fault Tolerance

- All S1000D / CSDB Mapping and Traceability maintenance requires FADEC and fuel system isolation before starting.
- Safety-critical fastener torques require calibrated tooling and dual sign-off.
- BITE failures affecting S1000D / CSDB Mapping and Traceability dispatch must be resolved or deferred per approved MEL.

---

## §12 Maintenance and Diagnostics

| Task | Interval | Access | Special Tools |
|---|---|---|---|
| Scheduled S1000D / CSDB Mapping and Traceability inspection | C-check | Per AMM access | NDT and inspection kit |
| BITE log review and download | A-check | Maintenance terminal | CMS terminal |
| S1000D / CSDB Mapping and Traceability functional test after LRU replacement | After LRU change | Ground run | FADEC GSE |

---

## §13 Footprint — Physical, Electrical, Maintenance, Data ![TBD]

| Footprint Type | Parameter | Value | Notes |
|---|---|---|---|
| Physical | Mass (system total) | ![TBD] | Pending OEM data |
| Physical | Envelope (max) | ![TBD] | Pending detailed design |
| Electrical | Peak power (W) | ![TBD] | To be defined |
| Maintenance | Access category | Standard line maintenance | Per AMM |
| Data | AFDX bandwidth | ![TBD] | Per AFDX bus load analysis |

---

## §14 Safety and Certification References ![DRAFT]

| Standard / Document | Title | Issuing Body | Applicability |
|---|---|---|---|
| S1000D Issue 5.0 | Technical Publications Standard | S1000D.org | Authoring standard |
| ATA iSpec 2200 | Chapter 63 | ATA | ATA SNS reference |
| EASA CS-E §515 | Engine life limits | EASA | LLP TC reference requirement in DMs |
| <MODEL>-GP-CSDB-001 | CSDB Governance Procedure | Q-DATAGOV | CSDB workflow |
| DO-178C | Software Considerations | RTCA | FADEC DM software content requirements |

---

## §15 V&V Approach ![TBD]

| Phase | Method | Acceptance Criterion | Status |
|---|---|---|---|
| Design | Analysis and simulation | Meets all §10 performance requirements | ![TBD] |
| Integration | Ground functional test | All BITE tests pass; interfaces verified | ![TBD] |
| Qualification | DO-160G environmental test | All applicable tests pass | ![TBD] |
| Certification | EASA CS-25 / CS-E compliance demonstration | Type Certificate / STC approval | ![TBD] |

---

## §16 Glossary

| Term | Definition |
|---|---|
| **DMC** | Data Module Code — unique S1000D identifier for each data module. |
| **DMRL** | Data Module Requirement List — master list of all required DMs. |
| **BREX** | Business Rules eXchange — project-specific S1000D rules enforced at ingestion. |
| **LLP** | Life-Limited Part — mandatory retirement life defined in engine TC. |
| **CSDB** | Common Source DataBase — controlled S1000D data module repository. |
| **SNS** | Standard Numbering System — hierarchical system/sub-system numbering in DMCs. |
| **IETP** | Interactive Electronic Technical Publication — rendered from CSDB DMs. |
| **DM-040** | Descriptive data module (system description). |
| **DM-300** | Inspection/examination data module. |
| **DM-941** | Illustrated parts data module. |

---

## §17 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-063-090-001 | Finalise S1000D / CSDB Mapping and Traceability design with engine OEM | Q-MECHANICS | 2026-Q4 |
| OI-063-090-002 | Define BITE coverage for S1000D / CSDB Mapping and Traceability | Q-AIR / safety | 2027-Q1 |

---

## §18 Status Legend

| Badge | Meaning |
|---|---|
| `![DRAFT]` | Section is drafted but not yet reviewed |
| `![TBD]` | Content not yet started — to be defined |
| `![To Be Completed]` | Partially complete — needs additional content |
| `![APPROVED]` | Reviewed and formally approved |

---

## §19 Related Documents (Siblings in this Subsection)

- [063-000](./063-000.md)
- [063-010](./063-010.md)
- [063-020](./063-020.md)
- [063-030](./063-030.md)
- [063-040](./063-040.md)
- [063-050](./063-050.md)
- [063-060](./063-060.md)
- [063-070](./063-070.md)
- [063-080](./063-080.md)

---

## §20 Change Log

| Rev | Date | Author | Description |
|---|---|---|---|
| 0.1 | 2026-05-11 | @copilot | Initial DRAFT — contextualized content per <PROGRAMME> architecture |
