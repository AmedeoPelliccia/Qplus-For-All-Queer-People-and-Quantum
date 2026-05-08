---
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
subsection: "201"
subsection_title: "Clasificacion de Efectores y Capacidades"
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
document_id: QATL-ATLAS1000-DTTA-200-209-00-201-010-TRACEABILITY-EVIDENCE-AND-LIFECYCLE-GOVERNANCE
subsubject: "010"
subsubject_title: "Traceability, Evidence and Lifecycle Governance"
title: "DTTA 201 · 010 — Traceability, Evidence and Lifecycle Governance"
---

# DTTA 201 · 010 — Traceability, Evidence and Lifecycle Governance

## §1 Purpose

This document defines evidence package requirements, traceability obligations, and lifecycle governance for the entire Clasificación de Efectores y Capacidades subsection (201). It is the authoritative governance reference for evidence integrity, review gate obligations, and archive closure requirements for all subsubjects 000–009.

**Non-operational boundary:** This document defines lifecycle governance and evidence traceability taxonomy only. It does not contain operational mission evidence, classified test data, mission-specific safety cases, or operational deployment records. All lifecycle stages and evidence requirements are governance instruments for programme and classification management.

## §2 Scope

**In scope:**
- Lifecycle taxonomy for DTTA 201: concept, classification, verification, certification, operational-support, decommission.
- Evidence package structure requirements per lifecycle stage.
- Review gate obligations: PDR (Preliminary Design Review), CDR (Critical Design Review), export-control review, safety case review, legal review.
- Traceability matrix structure linking subsubjects 000–009 to governance obligations.
- Archive closure requirements and document status lifecycle.

**Out of scope:**
- Operational mission evidence, classified test data, or live system performance records.
- System-level safety cases, qualified data packages, or airworthiness certification data.

## §3 Diagram

```mermaid
flowchart LR
    LC1([Concept Stage])
    LC2([Classification Stage])
    LC3([Verification Stage])
    LC4([Certification Stage])
    LC5([Operational-Support Stage])
    LC6([Decommission Stage])

    LC1 -->|Evidence: scope declaration,\ntaxonomy draft| LC2
    LC2 -->|Gate: PDR\nEvidence: taxonomy baseline,\nexport-control trigger check| LC3
    LC3 -->|Gate: CDR\nEvidence: standards mapping,\nhuman-control verification| LC4
    LC4 -->|Gate: Safety case review\nLegal review\nExport-control review\nEvidence: full evidence package| LC5
    LC5 -->|Evidence: change records,\nlegal compliance updates| LC6
    LC6 -->|Gate: Archive closure\nEvidence: final archive package| END([Archive Closed])

    style LC4 fill:#ffe0e0,stroke:#cc0000
    style LC6 fill:#cccccc,stroke:#666666
    style END fill:#cccccc,stroke:#666666
```

> **Note:** This diagram represents governance lifecycle flow for DTTA 201 documentation only. Lifecycle stages are governance instruments; they do not represent physical system development milestones or operational deployment events.

## §4 Traceability Matrix

| Subsubject | Title | Lifecycle Coverage | Review Gates | Standards |
|---:|---|---|---|---|
| 000 | Overview | Concept, Classification | PDR | AAP-06 |
| 001 | Controlled Definitions | Concept, Classification | PDR | AAP-06, STANAG 4586 |
| 002 | Effector Class Taxonomy | Classification, Verification | PDR, CDR | STANAG 4586, IEC 61508 |
| 003 | Defensive Capability Categories | Classification, Verification | PDR, CDR | STANAG 4569, IEC 61508 |
| 004 | Kinetic/Non-Kinetic Boundaries | Classification, Certification | CDR, Legal | ATT, AP-I |
| 005 | Platform Integration Taxonomy | Verification, Certification | CDR, Safety | STANAG 4586, IEC 61508 |
| 006 | Human Control & Auth Gates | Verification, Certification | CDR, Legal | CCW GGE, IEC 61508 |
| 007 | Safety, Risk & Harm Prevention | Verification, Certification | Safety Case, Legal | IEC 61508, MIL-STD-882E |
| 008 | Standards Mapping | Classification, Operational-Support | PDR | All applicable |
| 009 | Export Control & Legal | Certification, Operational-Support | Export Control, Legal | ITAR, EAR, Wassenaar |

## §5 Footprint

| Field | Value |
|---|---|
| Architecture | Defence Technology Type Architecture (DTTA) |
| Master range | 200–299 |
| Code range | 200-209 |
| Section | 00 |
| Subsection | 201 |
| Subsubject | 010 |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-LEG, ORB-PMO, ORB-FIN |
| Governance class | restricted[^gov] |
| Restricted rule | N-006[^n006] |
| Folder path | `Q+ATLANTIDE/200-299_DTTA/200-209_Sistemas-de-Combate-y-Armamento/201_Clasificacion-de-Efectores-y-Capacidades/` |
| Document | `010_Traceability-Evidence-and-Lifecycle-Governance.md` |
| Parent subsection | [README.md](./README.md) · [000_Overview.md](./000_Overview.md) |
| Parent section | [../README.md](../README.md) |
| Parent architecture | [../../README.md](../../README.md) |
| Parent baseline | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

## §6 References

[^baseline]: Q+ATLANTIDE controlled baseline — [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md)
[^archtable]: §3 Architecture Table — parent architecture index [../../README.md](../../README.md)
[^qdiv]: Q-DATAGOV primary authority; Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY support.
[^gov]: Governance class `restricted` per N-006 for DTTA band documents.
[^n001]: Note N-001: taxonomy/traceability ecosystem only.
[^n004]: Note N-004 (No-AAA Rule).
[^n006]: Note N-006 (Restricted bands) — DTTA 200-299.

**Applicable standards:** AS9100D · MIL-STD-882E · IEC 61508 · IEC 62443 · NATO STANAG 4187 · ISO/IEC 15026 · EU Directive 2009/43/EC.
