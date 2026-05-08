---
document_id: QATL-ATLAS1000-DTTA-200-209-00-202-000-OVERVIEW
title: "DTTA 202 · 000 — Overview"
subsubject: "000"
subsubject_title: "Overview"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: DTTA
architecture_name: "Defence Technology Type Architecture"
master_range: "200–299"
code_range: "200-209"
section: "00"
section_title: "Sistemas de Combate y Armamento"
subsection: "202"
subsection_title: "Armamento Convencional: Clasificacion y Control"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY]
orb_function_support: [ORB-LEG, ORB-PMO, ORB-FIN]
governance_class: restricted
restricted_rule: N-006
evidence_package_id: PENDING
access_control_profile: QATL-ACP-DTTA-RESTRICTED
version: 1.0.0
status: active
language: en
---

# DTTA 202 · Subsubject 000 — Overview

## §1 Purpose

This document is the entry-point for **Armamento Convencional: Clasificación y Control** (DTTA 202). It provides controlled vocabulary, scope boundaries, and a navigational index for all subsubjects 001–010.

**Non-operational boundary:** This subsection is restricted to classification, governance, custody, safety, accountability and legal-control taxonomy. It does not define construction details, deployment methods, targeting logic, tactical employment, optimization for harm, performance enhancement or operational weapon procedures.

Subsection 202 exists within Q+ATLANTIDE[^baseline] to fulfil the following governance functions:

- Establish a controlled, legally reviewable taxonomy of conventional armament classifications for DTTA traceability.
- Provide the authorization and human-control framework required for responsible custody and governance.
- Map applicable legal obligations across Wassenaar, ITAR, EAR, UN ATT and non-proliferation regimes.
- Define lifecycle evidence and audit requirements from acquisition classification to decommissioning.

All content is issued under governance class `restricted`[^gov] per N-006[^n006].

### Applicable Standards

| Standard | Scope |
|---|---|
| STANAG 4187 | NATO Ammunition Safety — storage, handling, safety governance |
| MIL-STD-882E | System Safety — risk classification and hazard prevention |
| ITAR (22 CFR 121) | Export control — abstract category alignment |
| EAR (15 CFR 774) | Export control — Commerce Control List alignment |
| Wassenaar Arrangement | Multilateral export control — ML-category abstract taxonomy |
| UN ATT | Arms Trade Treaty — legal obligation taxonomy |
| IEC 60079 | Explosive atmospheres — storage environmental control |
| OSCE Handbook | Best Practices for Conventional Ammunition — governance reference |

## §2 Scope

Navigational index of subsubjects 001–010:

| NNN | Title | One-line description |
|---:|---|---|
| 001 | Conventional Armament Controlled Definition | Establishes Q+ATLANTIDE normative definition and disambiguation from non-conventional/CBRN systems |
| 002 | Conventional Armament Classes, Non-Operational Taxonomy | Non-operational class hierarchy: light weapons, heavy weapons, support weapons — abstract labels only |
| 003 | Platform Compatibility and Integration Boundaries | Taxonomy of platform-armament interface boundaries (mechanical, electrical, data, authorization) |
| 004 | Storage, Handling and Safety Governance | Safety governance framework, storage classification taxonomy, handling control requirements |
| 005 | Inventory Accountability and Chain of Custody | Inventory taxonomy, serial/lot traceability, custodian chain and transfer authorization governance |
| 006 | Authorization, Rules-of-Use and Human Control | Authorization taxonomy, command authority levels, mandatory HITL/supervisory human control requirements |
| 007 | Risk Classification and Hazard Prevention | Risk and hazard taxonomy: hazard classes, SIL triggers, prevention framework hierarchy |
| 008 | Export Control, Legal and Non-Proliferation Mapping | Regime mapping: Wassenaar, ITAR, EAR, EU Directive 2009/43/EC, UN ATT, UN PoA SALW |
| 009 | Evidence, Audit and Compliance Records | Evidence record taxonomy, audit trail requirements, compliance and non-conformance record structure |
| 010 | Traceability, Evidence and Lifecycle Governance | Lifecycle phases, evidence gates from acquisition classification to decommissioning and disposal |

## §3 Footprint

| Field | Value |
|---|---|
| Architecture | Defence Technology Type Architecture (DTTA) |
| Master range | 200–299 |
| Code range | 200-209 |
| Section | 00 |
| Subsection | 202 |
| Subsubject | 000 |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-LEG, ORB-PMO, ORB-FIN |
| Governance class | restricted[^gov] |
| Restricted rule | N-006[^n006] |
| Folder path | `Q+ATLANTIDE/200-299_DTTA/200-209_Sistemas-de-Combate-y-Armamento/202_Armamento-Convencional-Clasificacion-y-Control/` |
| Document | `000_Overview.md` |
| Parent subsection | [README.md](./README.md) |
| Parent section | [../README.md](../README.md) |
| Parent architecture | [../../README.md](../../README.md) |
| Parent baseline | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

## §4 References

[^baseline]: Q+ATLANTIDE controlled baseline — [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md)
[^archtable]: §3 Architecture Table (parent) — [../../README.md](../../README.md)
[^qdiv]: Q-DATAGOV primary; Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY support.
[^gov]: Governance class `restricted` per N-006.
[^n001]: Note N-001: taxonomy/traceability ecosystem only — no operational, construction or performance content.
[^n004]: Note N-004 (No-AAA Rule): No autonomous armament activation, targeting or engagement logic permitted.
[^n006]: Note N-006 (Restricted bands) — DTTA 200-299.
