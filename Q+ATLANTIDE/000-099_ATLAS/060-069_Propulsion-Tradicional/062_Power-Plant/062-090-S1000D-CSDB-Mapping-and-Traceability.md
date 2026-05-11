---
document_id: "QATL-ATLAS-1000-ATLAS-060-069-062-090-S1000D---CSDB-MAPPING-AND-TRACEABILITY"
register: ATLAS-1000
title: "S1000D / CSDB Mapping and Traceability"
ata: "ATA 62"
sns: "062-090-00"
subsection: "062"
subsubject_code: "090"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-MECHANICS, Q-AIR, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-11"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
parent_subsubject_doc: "./README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0062-090"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-060-069-062-090-S1000D---CSDB-MAPPING-AND-TRACEABILITY
     ATA 62 · S1000D / CSDB Mapping and Traceability
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# S1000D / CSDB Mapping and Traceability

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATA 62](https://img.shields.io/badge/ATA-62-green)
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

ATA 62 S1000D DMRL: 36 data modules. DMC scheme `AMPEL360E-EWTW-062-{NNN}-00A-EN-US`. BREX `AMPEL360E-BREX-062-v1` enforces: (1) no bleed-air pneumatic interface DMs; (2) fire zone DMs must cite CS-25 §25.1181; (3) mount bolt torque DMs must cite calibrated-tool requirement. Q-DATAGOV manages CSDB; Q-MECHANICS is technical review authority.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA reference | ATA 62-090 — S1000D / CSDB Mapping and Traceability |
| Certification basis | EASA CS-25 Amdt 27+ |
| S1000D SNS | 062-090-00 |

---

## §3 Functional Description ![DRAFT]

System description for S1000D / CSDB Mapping and Traceability within the AMPEL360E eWTW Power Plant architecture. See §3 Functional Description for technical detail.

---

## §4 Functional Breakdown

| ID | Name | Description | Lead Division |
|---|---|---|---|
| F-001 | S1000D / CSDB Mapping and Traceability Function 1 | Primary system function | Q-GREENTECH |
| F-002 | S1000D / CSDB Mapping and Traceability Function 2 | Secondary function | Q-MECHANICS |
| F-003 | Interface Management | Manage all system interfaces at QEC split plane | Q-MECHANICS / Q-AIR |

---

## §5 System Context — Mermaid Diagram

```mermaid
flowchart LR
    A[Power Plant Level] --> B[S1000D / CSDB Mapping and Traceability]
    B --> C[Primary Function]
    B --> D[Interface]
    B --> E[Monitoring]
    E --> F[CMS ATA 45]
```

---

## §6 Internal Architecture — Mermaid Diagram

```mermaid
flowchart TB
    SYS[S1000D / CSDB Mappin] --> F1[Function A]
    SYS --> F2[Function B]
    SYS --> MON[Monitoring BITE]
    MON --> CMS[CMS AFDX]
```

---

## §7 Components and LRUs

| Component | Part Number | Qty | Location | Maintenance Interval | Notes |
|---|---|---|---|---|---|
| S1000D Issue 5.0 schema | S1000D.org | CSDB authoring platform | IT | Per schema release | XML authoring base |
| BREX-062-v1 | Programme document | CSDB | CSDB validator | Per BREX revision | Three domain-specific constraints |
| DMRL tracker — 36 DMs | Q-DATAGOV | PMO | PMO tool | Continuously maintained | Monthly review |
| ICN registry ATA 62 | Q-DATAGOV | CSDB | IT | Continuously maintained | Illustration traceability |
| CSDB authoring tool | Approved tool | CSDB | IT | Per update | DM authoring and validation |

---

## §8 Interfaces

| Interface Type | Connected System | Protocol / Medium | Data / Function |
|---|---|---|---|
| ATA 45 CMS | Central Maintenance | AFDX | Health data and BITE fault codes |
| ATA 24 Electrical | Power distribution | HVDC / 28 V DC | LRU power supply |
| ATA 26 Fire Protection | Fire zone | Fire detector loop | Fire monitoring |

---

## §9 Operating Modes

| Mode | Trigger | System State | Actions / Consequences |
|---|---|---|---|
| Normal operation | All systems powered | Nominal | Full function active |
| Maintenance | Systems isolated | Aircraft grounded | LOTO active; task in progress |
| Engine change (QEC) | Engine removal/installation | Heavy maintenance | QEC split plane open |

---

## §10 Performance and Budgets ![DRAFT]

| Parameter | Requirement | Target / Design Value | Status |
|---|---|---|---|
| System availability | ≥ 99.9 % dispatch reliability | RAMS analysis | TBD |
| Maintenance access time | < 5 min to first access | Maintainability analysis | TBD |

---

## §11 Safety, Redundancy and Fault Tolerance

- All work in the S1000D / CSDB Mapping and Traceability area requires FADEC isolation and fuel system isolation before starting.
- Fire-zone materials in ATA 62 must meet CS-25 §25.1185 requirements; standard aircraft materials not permitted.
- Dual sign-off required for all engine mount and QEC tasks.

---

## §12 Maintenance and Diagnostics

| Task | Interval | Access | Special Tools |
|---|---|---|---|
| Scheduled inspection of S1000D / CSDB Mapping and Traceability | C-check | Nacelle access | Inspection kit per AMM |
| BITE download for S1000D / CSDB Mapping and Traceability | A-check | Maintenance terminal | CMS terminal |

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
| EASA CS-25 §25.1181 | Designated fire zones | EASA | Fire zone requirement |
| ATA iSpec 2200 | Chapter 62 — Power Plant | ATA | Chapter scope |
| DO-160G | Environmental conditions | RTCA | LRU environmental qualification |
| SAE AS7114 | Propulsion System Installation | SAE | Engine installation reference |
| ARINC 664 P7 | AFDX network | ARINC | Data bus standard |

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
| **QEC** | Quick Engine Change — the defined split plane for engine removal and installation. |
| **FADEC** | Full Authority Digital Engine Control — the engine computer governing all fuel and control functions. |
| **Fire zone** | Engine compartment area treated to CS-25 §25.1181 fire-resistance standards. |
| **CS-25 §25.1185** | EASA standard for fuel lines in fire zones. |
| **BREX** | Business Rules eXchange — project-specific S1000D rules. |
| **BITE** | Built-In Test Equipment — self-test functionality within an LRU. |
| **ACMF** | Aircraft Condition Monitoring Function — FADEC data recorder for in-service trending. |
| **EDIU** | Engine Data Interface Unit — gateway between engine FADEC bus and aircraft AFDX. |
| **LRU** | Line Replaceable Unit — a module designed for rapid removal and replacement. |
| **NPN** | Not Part Number — placeholder for components whose part numbers are not yet assigned. |

---

## §17 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-062-090-001 | Finalise S1000D / CSDB Mapping and Traceability design for AMPEL360E baseline (OEM data pending) | Q-MECHANICS | 2026-Q4 |

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

- [062-000](./062-000.md)
- [062-010](./062-010.md)
- [062-020](./062-020.md)
- [062-030](./062-030.md)
- [062-040](./062-040.md)
- [062-050](./062-050.md)
- [062-060](./062-060.md)
- [062-070](./062-070.md)
- [062-080](./062-080.md)

---

## §20 Change Log

| Rev | Date | Author | Description |
|---|---|---|---|
| 0.1 | 2026-05-11 | @copilot | Initial DRAFT — contextualized content per AMPEL360E eWTW architecture |
