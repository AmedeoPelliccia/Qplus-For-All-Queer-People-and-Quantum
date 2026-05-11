---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-055-README"
title: "ATLAS 050-059 · 05.055 — Stabilizers (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "050-059"
section: "05"
section_title: "Estructuras"
subsection: "055"
subsection_title: "Stabilizers"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · Section 05 · Subsection 055 — Stabilizers

## 1. Purpose

Subsection-level index for *Stabilizers* (`055`) within ATLAS `050-059` — *Estructuras* — ATA 55.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Reserves the subsubject namespace `00`–`99` of subsection `055` *Stabilizers*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- The Overview and detailed subsubjects (`00`–`99`) will be populated in subsequent baseline releases per the parent section's authorisation.

## 3. Subsubject Index

| NN | Folder | Title | Status |
|---:|---|---|---|
| 000 | [055-000-Stabilizers-General](./055-000-Stabilizers-General/README.md) | Stabilizers — General | draft |
| 010 | [055-010-Horizontal-Stabilizer](./055-010-Horizontal-Stabilizer/README.md) | Horizontal Stabilizer | draft |
| 020 | [055-020-Vertical-Stabilizer](./055-020-Vertical-Stabilizer/README.md) | Vertical Stabilizer | draft |
| 030 | [055-030-Stabilizer-Control-Surfaces](./055-030-Stabilizer-Control-Surfaces/README.md) | Stabilizer Control Surfaces | draft |
| 040 | [055-040-Stabilizer-Attachment-and-Actuation-Interfaces](./055-040-Stabilizer-Attachment-and-Actuation-Interfaces/README.md) | Stabilizer Attachment and Actuation Interfaces | draft |
| 050 | [055-050-Stabilizer-Loads-and-Aeroelastic-Interfaces](./055-050-Stabilizer-Loads-and-Aeroelastic-Interfaces/README.md) | Stabilizer Loads and Aeroelastic Interfaces | draft |
| 060 | [055-060-Stabilizer-Fairings-Tips-and-Access-Panels](./055-060-Stabilizer-Fairings-Tips-and-Access-Panels/README.md) | Stabilizer Fairings, Tips and Access Panels | draft |
| 070 | [055-070-Stabilizer-Repairs-and-NDT](./055-070-Stabilizer-Repairs-and-NDT/README.md) | Stabilizer Repairs and NDT | draft |
| 080 | [055-080-Stabilizer-Monitoring-Diagnostics-and-Control-Interfaces](./055-080-Stabilizer-Monitoring-Diagnostics-and-Control-Interfaces/README.md) | Stabilizer Monitoring, Diagnostics and Control Interfaces | draft |
| 090 | [055-090-S1000D-CSDB-Mapping-and-Traceability](./055-090-S1000D-CSDB-Mapping-and-Traceability/README.md) | S1000D CSDB Mapping and Traceability | draft |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `050-059` |
| Section | `05` — Estructuras |
| Subsection | `055` — Stabilizers |
| Subsubject namespace | `000`–`090` (10 subsubjects, draft) |
| Primary Q-Division | Q-STRUCTURES[^qdiv] |
| Support Q-Divisions | Q-AIR, Q-INDUSTRY, Q-HPC |
| ORB support | ORB-PMO, ORB-FIN, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/055_Stabilizers/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-STRUCTURES` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `00`–`99` shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
