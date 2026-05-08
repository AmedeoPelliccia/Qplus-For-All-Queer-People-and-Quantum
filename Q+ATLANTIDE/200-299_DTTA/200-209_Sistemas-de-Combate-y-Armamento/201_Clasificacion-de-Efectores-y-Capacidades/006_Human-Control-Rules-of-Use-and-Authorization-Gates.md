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
document_id: QATL-ATLAS1000-DTTA-200-209-00-201-006-HUMAN-CONTROL-RULES-OF-USE-AND-AUTHORIZATION-GATES
subsubject: "006"
subsubject_title: "Human Control, Rules-of-Use and Authorization Gates"
title: "DTTA 201 · 006 — Human Control, Rules-of-Use and Authorization Gates"
---

# DTTA 201 · 006 — Human Control, Rules-of-Use and Authorization Gates

## §1 Purpose

This document defines the human control framework, rules-of-use taxonomy, and authorization gate structure for effector capabilities within DTTA subsection 201. Mandatory human authority at all engagement-relevant decision points is a non-negotiable governance constraint. All definitions are at governance and taxonomy level only.

**Non-operational boundary:** This document defines human control and authorization gate taxonomy for governance purposes only. It does not define specific rules of engagement (ROE), operational authorization decisions, targeting authority chains, or operational command procedures. All human control taxonomy entries are governance instruments.

## §2 Scope

**In scope:**
- Human control taxonomy: Human-In-The-Loop (HITL), Human-On-The-Loop (HOTL), supervisory control classifications.
- Rules-of-use declaration framework for effector capability labelling.
- Authorization gate structure: legal review gate, command authority gate, proportionality check gate.
- ROE interface taxonomy at abstract level (governance boundary only; no specific ROE content).

**Out of scope:**
- Specific rules of engagement content, classified or otherwise.
- Operational authorization decisions, mission-specific authority chains.
- Targeting authority structures, fire control procedures.

## §3 Diagram

```mermaid
flowchart TD
    START([Effector Capability Action Request])

    START --> G1[Gate 1: Legal Review\nORB-LEG authorization]
    G1 -->|Approved| G2[Gate 2: Command Authority\nHuman commander decision]
    G1 -->|Rejected| STOP1([Action Blocked — Legal])

    G2 -->|Authorized| G3[Gate 3: Proportionality Check\nHuman proportionality assessment]
    G2 -->|Not Authorized| STOP2([Action Blocked — Command])

    G3 -->|Proportionate| G4[Gate 4: Human Engagement Authorization\nHITL mandatory confirmation]
    G3 -->|Disproportionate| STOP3([Action Blocked — Proportionality])

    G4 -->|Confirmed by Human| ACTION([Action Proceeds under Human Authority])
    G4 -->|Not Confirmed| STOP4([Action Blocked — Human Control])

    style G1 fill:#fff3cc,stroke:#cc8800
    style G2 fill:#ffe0e0,stroke:#cc0000
    style G3 fill:#ffe0e0,stroke:#cc0000
    style G4 fill:#ffe0e0,stroke:#cc0000
    style ACTION fill:#e8ffe8,stroke:#007700
    style STOP1 fill:#cccccc,stroke:#666666
    style STOP2 fill:#cccccc,stroke:#666666
    style STOP3 fill:#cccccc,stroke:#666666
    style STOP4 fill:#cccccc,stroke:#666666
```

> **Note:** This diagram represents governance authorization gate taxonomy only. All gate nodes require human decision-making authority. No autonomous, automated, or algorithmic engagement authorization is defined, implied, or permitted[^n004].

## §4 Footprint

| Field | Value |
|---|---|
| Architecture | Defence Technology Type Architecture (DTTA) |
| Master range | 200–299 |
| Code range | 200-209 |
| Section | 00 |
| Subsection | 201 |
| Subsubject | 006 |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-LEG, ORB-PMO, ORB-FIN |
| Governance class | restricted[^gov] |
| Restricted rule | N-006[^n006] |
| Folder path | `Q+ATLANTIDE/200-299_DTTA/200-209_Sistemas-de-Combate-y-Armamento/201_Clasificacion-de-Efectores-y-Capacidades/` |
| Document | `006_Human-Control-Rules-of-Use-and-Authorization-Gates.md` |
| Parent subsection | [README.md](./README.md) · [000_Overview.md](./000_Overview.md) |
| Parent section | [../README.md](../README.md) |
| Parent architecture | [../../README.md](../../README.md) |
| Parent baseline | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

## §5 References

[^baseline]: Q+ATLANTIDE controlled baseline — [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md)
[^archtable]: §3 Architecture Table — parent architecture index [../../README.md](../../README.md)
[^qdiv]: Q-DATAGOV primary authority; Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY support.
[^gov]: Governance class `restricted` per N-006 for DTTA band documents.
[^n001]: Note N-001: taxonomy/traceability ecosystem only.
[^n004]: Note N-004 (No-AAA Rule) — No autonomous, automated, or algorithmic attack authorization is defined, implied, or permitted within this subsection.
[^n006]: Note N-006 (Restricted bands) — DTTA 200-299.

**Applicable standards:** UN CCW Group of Governmental Experts on LAWS · NATO AJP-01 · STANAG 4586 · IEC 61508 · IHL principles (Additional Protocol I) · NATO AAP-06.
