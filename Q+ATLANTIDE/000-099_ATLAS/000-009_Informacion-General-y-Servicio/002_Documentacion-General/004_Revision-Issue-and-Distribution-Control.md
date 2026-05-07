---
document_id: QATL-ATLAS-1000-ATLAS-000-009-00-002-004-REVISION-ISSUE-DISTRIBUTION-CONTROL
title: "ATLAS 000-009 · 00.002.004 — Revision, Issue and Distribution Control"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "000-009"
section: "00"
section_title: "Información General y Servicio"
subsection: "002"
subsection_title: "Documentación General"
subsubject: "004"
subsubject_title: "Revision, Issue and Distribution Control"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-GROUND, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 000-009 · 00.002.004 — Revision, Issue and Distribution Control

## 1. Purpose

Defines the **issue numbering scheme**, revision policy (types of revisions), release authority and signoff procedure, distribution control (operator subscription, regulatory submission), change history and traceability across issues, and the relationship to configuration baseline freeze events.

This document links to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4.

## 2. Scope

### 2.1 Issue numbering

Every delivered manual has an **Issue Number** that identifies the complete revision state of that manual at a point in time.

Issue numbering convention: `Issue N` where N is a positive integer starting at 1.

| Milestone | Issue number | Description |
|---|---|---|
| First type-certificate delivery | Issue 1 | Initial certified content |
| First major revision | Issue 2 | Following content update after certification |
| Subsequent major revisions | Issue 3, 4, … | Sequential; no gaps allowed |
| Draft / in-work state | Issue N — inWork XX | CSDB `inWork` attribute; not distributed externally |

**Rules**:
- Issue numbers are manual-specific: AMM Issue 3 and IPC Issue 3 are independent; they are not required to be synchronised.
- The CSDB PM `issueNumber` attribute is the machine-readable issue identifier.
- Human-readable issue dates appear on the title page of every distributed manual.
- Superseded issues are archived in the CSDB and remain accessible for historical traceability; they are never deleted.

### 2.2 Revision policy

Three types of revisions are recognised:

| Revision type | Trigger | Distribution | Incorporation into manual |
|---|---|---|---|
| **Full Revision (FR)** | Significant content change (new system, regulatory change, structural repair scheme update) | All operators on distribution list | Full re-issue of the manual (new Issue N) |
| **Temporary Revision (TR)** | Urgent safety or operational information requiring immediate distribution before full revision cycle | All operators on distribution list (priority) | Inserted physically (paper) or electronically as overlay; incorporated at next FR |
| **Technical Newsletter (TN)** | Minor clarification, editorial correction, non-safety-critical information | All operators (advisory) | Incorporated at next FR; TNs do not change Issue N |

**Additional rule — Service Bulletins (SBs)**: SBs are not revisions of the AMM; they are standalone documents. However, when an SB is incorporated into an aircraft, the AMM and IPC shall be revised at the next FR cycle to reflect the post-SB configuration. SB status tracking is part of the change history (§2.5).

### 2.3 Release authority and signoff procedure

Every issue of a manual (FR or TR) requires formal release authority before distribution:

| Role | Responsibility |
|---|---|
| **Data Module Author** | Produces DM content; marks `inWork = 00` when ready for review |
| **Technical Reviewer (Q-DATAGOV)** | Reviews technical accuracy against ATLAS source data; approves or returns |
| **Verification Reviewer (Q-AIR / Q-GROUND)** | Verifies operational applicability and safety impact |
| **Release Authority (ORB-PMO)** | Final signoff; promotes CSDB PM from `inWork` to official Issue N |
| **Regulatory Submission (ORB-LEG)** | For AFM, AWL, and MMEL: submits to EASA/FAA before distribution |

Signoff evidence is retained in the CSDB as DM status attributes (`reasonForUpdate`, `security`, `qa`) and in the programme ECO (Engineering Change Order) register maintained by ORB-PMO.

### 2.4 Distribution control

#### 2.4.1 Operator subscription

Operators receive manuals according to their subscription level, which is tied to their Operator Agreement with P&L.inc:

| Subscription level | Manuals included |
|---|---|
| Standard | AMM, IPC, WDM, TSM, MPD |
| Structural | + SRM, NDT Manual |
| Full | All manuals including CMM, FCOM, MMEL/MEL |
| Regulatory only | AFM, MMEL (required by all operators by regulation) |

Distribution is managed via the operator portal (authenticated access). Physical distribution (CD/USB/paper) is available on request for operators without portal access.

#### 2.4.2 Regulatory submission

| Manual | Regulatory authority | Submission trigger |
|---|---|---|
| AFM | EASA (primary); FAA (validation) | Every FR; before entry into service of new variant |
| AWL (AMM §4) | EASA / FAA | Every change to life limits or inspection intervals |
| MMEL | EASA (master); operator submits derived MEL to local authority | Every FR affecting dispatch items |
| SB (safety-critical) | EASA via Mandatory Service Bulletin (MSB) mechanism | Before operator distribution |

#### 2.4.3 Confidentiality

Manuals are classified as **Proprietary — Commercial Confidence** unless declared otherwise. The following classifications are used:

| Classification | Distribution |
|---|---|
| `Unrestricted` | AFM performance sections (public); regulatory submissions |
| `Operator Restricted` | All standard manuals; operators only |
| `Programme Restricted` | CMM of advanced systems (propulsion, quantum); controlled release |
| `Regulatory Only` | Submitted to EASA/FAA only |

### 2.5 Change history and traceability across issues

Every FR produces a **Highlights of Changes** document that lists, for each changed DM, the reason for change, the issue number affected, and the BREX rule or regulatory reference that drove the change.

Change traceability chain:

```
Configuration Baseline Freeze Event (001_Configuracion/001_)
  → Engineering Change Order (ECO)
  → CSDB DM update (changeType + reasonForUpdate attributes)
  → PM rebuild → Issue N
  → Highlights of Changes document
  → Distribution to operators
```

All CSDB DM changes carry `changeType` attributes (`add`, `delete`, `modify`) and `reasonForUpdate` free-text at the DM level. The CSDB version history (Git log) provides the full audit trail.

### 2.6 Relationship to configuration baseline freeze events

Configuration baseline freeze events — defined in `001_Configuracion/001_Configuration-Baseline.md`[^sub001baseline] — are the external triggers that initiate a Full Revision cycle. When the configuration baseline is frozen for a new variant or at a programme milestone (e.g. first flight, type certificate, Entry Into Service), a FR of all affected manuals is initiated.

Alignment rule: the Issue N of a manual issued at a baseline freeze event shall explicitly declare the configuration baseline version it was compiled against (e.g. `AMM Issue 3 — compiled against Configuration Baseline CB-003 (EIS)` in the manual title page and in the CSDB PM `reasonForUpdate` field).

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `000-009` |
| Section | `00` — Información General y Servicio |
| Subsection | `002` — Documentación General |
| Subsubject | `004` — Revision, Issue and Distribution Control |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-GROUND, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/000-009_Informacion-General-y-Servicio/002_Documentacion-General/` |
| Document | `004_Revision-Issue-and-Distribution-Control.md` (this file) |
| Parent subsection index | [`README.md`](./README.md) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^s1000d60]: **S1000D Issue 6.0 — International specification for technical publications** — ASD/AIA/ATA, 2022. Issue numbering and revision mark conventions are defined in Chapters 3 and 6.

[^easacs25]: **EASA CS-25 — Certification Specifications for Large Aeroplanes** — Regulatory basis for AFM (CS-25.1581), AWL (CS-25.1529), and MMEL distribution requirements.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for release authority and change control procedures.

[^sub001baseline]: **`001_Configuracion/001_Configuration-Baseline.md`** — [`../001_Configuracion/`](../001_Configuracion/). Configuration baseline freeze events that trigger FR cycles.

### Applicable industry standards

- S1000D Issue 6.0 — International specification for technical publications[^s1000d60]
- EASA CS-25 — Certification Specifications for Large Aeroplanes[^easacs25]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
