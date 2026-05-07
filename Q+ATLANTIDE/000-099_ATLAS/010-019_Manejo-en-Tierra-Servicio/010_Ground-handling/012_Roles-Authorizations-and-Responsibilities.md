---
document_id: QATL-ATLAS-1000-ATLAS-010-019-01-010-012-ROLES-AUTHORIZATIONS-AND-RESPONSIBILITIES
title: "ATLAS 010-019 · 01.010.012 — Roles, Authorizations and Responsibilities"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top-Level Architecture System"
master_range: "000–099"
code_range: "010-019"
section: "01"
section_title: "Manejo en Tierra & Servicio"
subject: "00"
subject_title: "General Information"
subsection: "010"
subsection_title: "Ground handling"
subsubject: "012"
subsubject_title: "Roles, Authorizations and Responsibilities"
primary_q_division: Q-GROUND
support_q_divisions: [Q-MECHANICS, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# ATLAS 010-019 · Section 01 · Subsection 010 · Subsubject 012 — Roles, Authorizations and Responsibilities

## 1. Purpose

Defines the **role catalogue**, **authorization grants** and **responsibility matrix** (RACI) governing the *Ground handling* of an airframe instance under ATLAS `010-019.010` *Ground handling*: which actor (operator, supervisor, marshaller, GSE driver, mechanic-on-call, duty engineer) is *Responsible*, *Accountable*, *Consulted* or *Informed* for each handling phase identified in subsubject `011`. Authorizations are issued against the controlled Q+ATLANTIDE baseline[^baseline], surfaced as S1000D applicability conditions on the ATA iSpec 2200 / Spec 100 information set[^ata2200][^ataspec100][^s1000d] and audited per AS9100D[^as9100d].

## 2. Scope

- Covers the *Roles, Authorizations and Responsibilities* subsubject (`012`) of subsection `010` *Ground handling* within section `01` *Manejo en Tierra & Servicio*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable]; Q-GROUND is the issuing authority for ground-handling authorizations, with Q-MECHANICS and Q-INDUSTRY consulted for GSE-side qualifications.
- Artefact classes in scope: **Role definition card**, **Authorization grant** (named individual ↔ role ↔ validity window), **RACI matrix** (role × handling phase), **competency record** and **delegation log**.
- Authorizations are surfaced as S1000D `applic` properties (e.g. `operator`, `lcPhase`) on the ATA iSpec 2200 information set[^ata2200][^s1000d] so that data modules render only for the actors entitled to consume them.

## 3. Diagram

The diagram below shows how a **named individual** is bound to a **role** through an **authorization grant**, and how that grant projects onto the **RACI matrix** that drives phase-by-phase responsibility during ground handling.

```mermaid
flowchart LR
    IND[Named Individual] --> AUTH[Authorization Grant\nrole · validity window]
    ROLE[Role Definition\noperator · supervisor · marshaller · GSE driver] --> AUTH
    COMP[Competency Record] --> AUTH
    AUTH --> RACI{{RACI Matrix\nrole × phase}}
    RACI --> R[(Responsible)]
    RACI --> A[(Accountable)]
    RACI --> C[(Consulted)]
    RACI --> I[(Informed)]
    AUTH --> DEL[Delegation Log]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top-Level Architecture System |
| Master range | `000–099` |
| Code range | `010-019` |
| Section | `01` — Manejo en Tierra & Servicio |
| Subject | `00` — General Information |
| Subsection | `010` — Ground handling |
| Subsubject | `012` — Roles, Authorizations and Responsibilities |
| Primary Q-Division | Q-GROUND[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/010-019_Manejo-en-Tierra-Servicio/010_Ground-handling/` |
| Document | `012_Roles-Authorizations-and-Responsibilities.md` (this file) |
| Parent subsection | [`010_Overview.md`](./010_Overview.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **ATLAS §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `010-019` row (Section `01` — Manejo en Tierra & Servicio, Primary Q-Division Q-GROUND).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — Bands are classified as `baseline` or `restricted` per Q+ATLANTIDE §4 governance rules.

[^ata2200]: **ATA iSpec 2200 — Information Standards for Aviation Maintenance** — Industry standard for digital aircraft maintenance information; governs chapter / section / subject numbering inherited by ATLAS `000-099`.

[^ataspec100]: **ATA Spec 100 — Manufacturers' Technical Data** — Predecessor numbering scheme that established the 00–99 chapter map mirrored by ATLAS sub-ranges.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used across ATLAS technical publications.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

### Applicable industry standards

The following ATA-family and industry standards apply to this subsubject in addition to the cross-cutting Q+ATLANTIDE governance:

- ATA iSpec 2200 — Information Standards for Aviation Maintenance[^ata2200]
- ATA Spec 100 — Manufacturers' Technical Data[^ataspec100]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
