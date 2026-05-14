---
document_id: QATL-ATLAS1000-DTTA-200-209-00-200-006-SAFETY-INTERLOCKS-RULES-OF-USE-AND-AUTHORIZATION-GATES
title: "DTTA 200-209 · 00.200.006 — Safety Interlocks, Rules-of-Use and Authorization Gates"
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
subsection: "200"
subsection_title: "Arquitectura de Sistemas de Combate"
subsubject: "006"
subsubject_title: "Safety Interlocks, Rules-of-Use and Authorization Gates"
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

# DTTA 200-209 · 00.200.006 — Safety Interlocks, Rules-of-Use and Authorization Gates

---

> **⚠ NON-OPERATIONAL BOUNDARY NOTICE**
> This document is a **restricted taxonomy and governance framework** within the Q+ATLANTIDE ATLAS-1000 register.
> It does **not** define specific hardware interlock designs, classified authorization criteria, operational safety procedures, or operational combat procedures.
> All content is normative exclusively within the Q+ATLANTIDE taxonomy and traceability ecosystem.[^n001][^n006]
> The **No-AAA Rule** applies.[^n004]
> Documents in this band are classified `governance_class: restricted` per N-006.[^n006] Explicit human authority, rules-of-use governance, safety interlocks, legal admissibility, export-control review, independent assurance, and lifecycle traceability are **required**.

---

## §1 Purpose

This document defines the **taxonomy and governance framework** for safety interlocks, rules-of-use (ROU) declarations, and authorization gates for DTTA 200 systems within the Q+ATLANTIDE ATLAS-1000 register.[^baseline]

The framework establishes mandatory safety classes and authorization structures that all DTTA 200 subsubject artefacts must declare. Three primary taxonomy categories are defined:

**Safety Interlock Taxonomy**
- *Hardware interlocks* — physical mechanisms that prevent unauthorised or unsafe state transitions, classified by function (enable, inhibit, emergency-stop).
- *Software interlocks* — software logic gates that enforce pre-conditions before state transitions, classified by safety integrity level (SIL) per IEC 61508.
- *Procedural interlocks* — documented human-operator steps that must be completed before system state transitions, classified by authority level.

**Rules-of-Use (ROU) Classification Framework**
- *Enabling conditions* — conditions that must be satisfied before a system or function class may be activated; declared abstractly for taxonomy purposes.
- *Use restrictions* — conditions that constrain the operational envelope of a system or function class; declared for export-control and assurance scoping.
- *Override and emergency procedures* — human-authority override taxonomy for exceptional situations.

**Authorization Gate Structure**
- *Enabling gate* — confirms satisfaction of enabling conditions (human sign-off required).
- *Legal review gate* — confirms legal and export-control review has been completed.
- *Safety case gate* — confirms safety case evidence package is current and approved.
- *Command authority gate* — confirms appropriate human authority level (HITL/HOTL per subsubject 004) is active.

All categories are **taxonomy classifications only**. Specific hardware designs, software implementations, and operational authorization criteria are outside scope.

---

## §2 Scope

### In Scope

- Safety interlock taxonomy: hardware, software, and procedural classes
- Rules-of-use (ROU) classification framework: enabling conditions, use restrictions, override taxonomy
- Authorization gate structure: enabling gate, legal review gate, safety case gate, command authority gate
- SIL classification references per IEC 61508 for safety interlock taxonomy alignment
- Mandatory declaration requirements for all DTTA 200 artefacts

### Out of Scope

- Specific hardware interlock designs or engineering specifications
- Software source code or firmware for safety functions
- Classified authorization criteria or programme-specific enabling conditions
- Operational safety procedures or standing operating procedures
- Operational combat procedures or tactical employment guidance

---

## §3 Diagram

```mermaid
flowchart TD
    subgraph SIF ["Safety Interlock & Authorization Gate Framework — Taxonomy (Q+ATLANTIDE · Non-Operational)"]
        HWI["Hardware Interlock\n─────────────\nEnable / Inhibit / E-Stop\nTaxonomy class only\nRef: IEC 61508"]
        SWI["Software Interlock\n─────────────\nSIL-classified logic gate\nPre-condition enforcement\nRef: IEC 61508"]
        PRI["Procedural Interlock\n─────────────\nHuman-operator step\nAuthority level declared\nRef: IEC 62061"]
    end

    subgraph AGS ["Authorization Gate Sequence"]
        EG["Enabling Gate\n─────────────\nEnabling conditions met?\nHuman sign-off required"]
        LG["Legal Review Gate\n─────────────\nLegal + export-control\nreview completed?"]
        SCG["Safety Case Gate\n─────────────\nSafety case evidence\npackage current + approved?"]
        CAG["Command Authority Gate\n─────────────\nHITL/HOTL active?\n(subsubject 004)"]
    end

    HWI -->|"Interlock satisfied"| EG
    SWI -->|"Interlock satisfied"| EG
    PRI -->|"Interlock satisfied"| EG
    EG -->|"Gate passed"| LG
    LG -->|"Gate passed"| SCG
    SCG -->|"Gate passed"| CAG
    CAG -->|"All gates passed\nAction permitted"| OUT["Authorised\nSystem Action\n(taxonomy)"]

    style HWI fill:#eafaf1,stroke:#27ae60
    style SWI fill:#e8f4f8,stroke:#2c7bb6
    style PRI fill:#fef9e7,stroke:#f39c12
    style EG fill:#fdf2f8,stroke:#8e44ad
    style LG fill:#fadbd8,stroke:#c0392b
    style SCG fill:#d5f5e3,stroke:#1e8449
    style CAG fill:#d6eaf8,stroke:#1a5276
    style OUT fill:#f9f9f9,stroke:#555555
    style SIF fill:#f8f9fa,stroke:#6c757d
    style AGS fill:#f0f0f0,stroke:#aaaaaa
```

> **Diagram note:** This is a governance taxonomy diagram. No specific hardware, software, or operational criteria are depicted.

---

## §4 Footprint

| Attribute | Value |
|---|---|
| Architecture | Defence Technology Type Architecture (DTTA) |
| Master range | 200–299 |
| Code range | 200-209 |
| Section | 00 |
| Subsection | 200 |
| Subsubject | 006 |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-LEG, ORB-PMO, ORB-FIN |
| Governance class | restricted[^gov] |
| Restricted rule | N-006[^n006] |
| Folder path | `Q+ATLANTIDE/200-299_DTTA/200-209_Sistemas-de-Combate-y-Armamento/200_Arquitectura-de-Sistemas-de-Combate/` |
| Document | `006_Safety-Interlocks-Rules-of-Use-and-Authorization-Gates.md` |
| Parent subsection | [README.md](./README.md) · [000_Overview.md](./000_Overview.md) |
| Parent section | [../README.md](../README.md) |
| Parent architecture | [../../README.md](../../README.md) |
| Parent baseline | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

### Applicable Standards

| Standard | Issuing Body | Applicability |
|---|---|---|
| IEC 61508 | IEC | Functional Safety of E/E/PE Safety-related Systems — SIL classification taxonomy for hardware and software interlocks |
| IEC 62061 | IEC | Safety of Machinery — safety integrity requirements for procedural interlock taxonomy |
| IEC 61511 | IEC | Functional Safety for the Process Industry Sector — process-safety interlock taxonomy alignment |
| NATO STANAG 4187 | NATO | Fuze Safety Design — safety interlock taxonomy reference for fuze-related systems |
| MIL-STD-882E | US DoD | System Safety — system safety taxonomy and hazard classification reference |

---

## §5 References & Citations

[^baseline]: Q+ATLANTIDE controlled baseline — authoritative taxonomy and traceability ecosystem governing all DTTA documents. See [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md).
[^archtable]: §3 Architecture Table (parent) — see [../../README.md](../../README.md).
[^qdiv]: Q-Division authority — Q-DATAGOV is the primary authority for governance and data taxonomy within Q+ATLANTIDE DTTA band; Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY provide technical domain support.
[^gov]: Governance class `restricted` — documents in this class require formal evidence packages, export-control review, and access controls per N-006.
[^n001]: Note N-001: Q+ATLANTIDE is a taxonomy and traceability ecosystem, not an operational programme; definitions herein are normative within the Q+ATLANTIDE register only.
[^n004]: Note N-004 (No-AAA Rule) — "AAA" is not a valid domain, division, architecture, interface or function in this baseline.
[^n006]: Note N-006 (Restricted bands) — Defence-related (200-299 DTTA) bands require additional governance, evidence packages and access controls. See [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) §5.3.
