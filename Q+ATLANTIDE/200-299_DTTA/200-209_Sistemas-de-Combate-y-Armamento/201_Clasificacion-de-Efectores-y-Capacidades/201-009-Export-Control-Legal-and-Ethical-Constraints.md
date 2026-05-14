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
document_id: QATL-ATLAS1000-DTTA-200-209-00-201-009-EXPORT-CONTROL-LEGAL-AND-ETHICAL-CONSTRAINTS
subsubject: "009"
subsubject_title: "Export Control, Legal and Ethical Constraints"
title: "DTTA 200-209 · 00.201.009 — Export Control, Legal and Ethical Constraints"
---

# DTTA 200-209 · 00.201.009 — Export Control, Legal and Ethical Constraints

## §1 Purpose

This document defines export control classification, legal boundary obligations, and ethical constraints for DTTA subsection 201 effector and capability taxonomy. Non-proliferation obligations are addressed at governance and taxonomy level only.

**Non-operational boundary:** This document addresses export control taxonomy, legal boundary obligations, and ethical constraint governance only. It does not reproduce classified control list items, country-specific export licence decisions, or specific product licence numbers. All export control taxonomy entries are abstract governance routing instruments referencing applicable regulatory frameworks by name only.

## §2 Scope

**In scope:**
- Export control taxonomy: ITAR Munitions List (ML) categories at abstract governance level, EAR Commerce Control List (CCL) taxonomy, Wassenaar Arrangement effector control list mapping at abstract level.
- IHL alignment requirements for effector classification labels.
- Ethical constraint framework: proportionality governance, discrimination governance, human dignity preservation taxonomy.
- Legal boundary declarations triggering ORB-LEG review.

**Out of scope:**
- Specific product licence numbers, export authorization codes, or classified control list line items.
- Country-specific trade decisions, individual export approvals, or denied-party determinations.
- Detailed ITAR/EAR compliance procedures (referenced by regulatory citation only).

## §3 Diagram

```mermaid
flowchart TD
    START([DTTA 201 Capability Label Assigned])

    START --> EC{Export Control\nReview Required?}

    EC -->|Kinetic / DE / EW class| ITAR[ITAR ML Check\n22 CFR 120-130\nORB-LEG required]
    EC -->|Dual-use class| EAR[EAR CCL Check\n15 CFR 730-774\nORB-LEG + Q-DATAGOV]
    EC -->|Support class| WASS[Wassenaar Check\nAbstract taxonomy only]
    EC -->|No export control trigger| CLEAR[Standard Governance Path]

    ITAR --> IHL[IHL Alignment Check\nAP-I Principles\nORB-LEG review]
    EAR --> EU[EU Dir 2009/43/EC\nIntra-EU transfer check]
    WASS --> ATT[UN ATT Review\nORB-LEG sign-off]
    CLEAR --> ETH[Ethical Constraint Review\nQ-DATAGOV]

    IHL --> EVP[Evidence Package\nUpdate]
    EU --> EVP
    ATT --> EVP
    ETH --> EVP

    EVP --> CLOSE([Governance Record Closed])

    style ITAR fill:#ffe0e0,stroke:#cc0000
    style IHL fill:#ffe0e0,stroke:#cc0000
    style ETH fill:#fff3cc,stroke:#cc8800
```

> **Note:** This diagram represents export control and legal boundary governance routing only. No specific licence decision, country determination, or classified control list item is defined or implied.

## §4 Footprint

| Field | Value |
|---|---|
| Architecture | Defence Technology Type Architecture (DTTA) |
| Master range | 200–299 |
| Code range | 200-209 |
| Section | 00 |
| Subsection | 201 |
| Subsubject | 009 |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-LEG, ORB-PMO, ORB-FIN |
| Governance class | restricted[^gov] |
| Restricted rule | N-006[^n006] |
| Folder path | `Q+ATLANTIDE/200-299_DTTA/200-209_Sistemas-de-Combate-y-Armamento/201_Clasificacion-de-Efectores-y-Capacidades/` |
| Document | `009_Export-Control-Legal-and-Ethical-Constraints.md` |
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
[^n004]: Note N-004 (No-AAA Rule).
[^n006]: Note N-006 (Restricted bands) — DTTA 200-299.

**Applicable standards:** ITAR (22 CFR 120-130) · EAR (15 CFR 730-774) · Wassenaar Arrangement · EU Directive 2009/43/EC · UN Arms Trade Treaty (ATT) · IHL Additional Protocol I (Geneva Conventions) · Convention on Certain Conventional Weapons (CCW).
