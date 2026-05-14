---
document_id: QATL-ATLAS1000-DTTA-200-209-00-200-009-EXPORT-CONTROL-LEGAL-AND-ETHICAL-BOUNDARIES
title: "DTTA 200-209 · 00.200.009 — Export Control, Legal and Ethical Boundaries"
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
subsubject: "009"
subsubject_title: "Export Control, Legal and Ethical Boundaries"
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

# DTTA 200-209 · 00.200.009 — Export Control, Legal and Ethical Boundaries

---

> **⚠ NON-OPERATIONAL BOUNDARY NOTICE**
> This document is a **restricted taxonomy and governance classification** within the Q+ATLANTIDE ATLAS-1000 register.
> It does **not** provide specific product classifications (classified), operational legal opinions, country-specific export licences, or operational combat procedures.
> All content is normative exclusively within the Q+ATLANTIDE taxonomy and traceability ecosystem.[^n001][^n006]
> The **No-AAA Rule** applies.[^n004]
> Documents in this band are classified `governance_class: restricted` per N-006.[^n006] Explicit human authority, rules-of-use governance, safety interlocks, legal admissibility, export-control review, independent assurance, and lifecycle traceability are **required**.

---

## §1 Purpose

This document defines the **export control classification framework**, **legal boundaries**, and **ethical constraints** applicable to DTTA 200 combat systems architecture taxonomy within the Q+ATLANTIDE ATLAS-1000 register.[^baseline]

The framework serves three governance functions:

1. **Export Control Classification Taxonomy** — establishes the classification framework vocabulary (ITAR, EAR, EU ML/CCL, Wassenaar Arrangement) for use in evidence packages and assurance reviews. Does not perform product-level classification — that requires a qualified export-control counsel review.

2. **Legal Boundary Declaration** — establishes the non-proliferation and international law obligations that all DTTA 200 artefacts must acknowledge and to which they must be traceable.

3. **Ethical Constraint Taxonomy** — establishes the International Humanitarian Law (IHL) alignment requirements and ethical constraint taxonomy at an abstract governance level. The principles of **proportionality** and **distinction** (IHL) are declared as mandatory governance references for all DTTA 200 systems, at the taxonomy level.

This document explicitly does **not** provide:
- Specific export classification determinations (requires qualified counsel)
- Operational legal opinions or legal advice
- Country-specific export licence guidance
- Classified export control data

---

## §2 Scope

### In Scope

- Export control classification taxonomy vocabulary: ITAR (22 CFR 120-130), EAR (15 CFR 730-774), EU Military List / Commerce Control List (ML/CCL), Wassenaar Arrangement
- Legal review requirement declarations for DTTA 200 artefacts
- International Humanitarian Law (IHL) alignment requirements: proportionality, distinction, precaution principles — abstract governance level only
- Ethical constraint taxonomy: proportionality, discrimination, precaution, human dignity — governance vocabulary
- Non-proliferation obligation acknowledgements: UN Arms Trade Treaty, CCW Convention

### Out of Scope

- Specific product-level export classification determinations
- Classified export control data or jurisdiction-specific rulings
- Operational legal opinions, compliance certificates, or export licences
- Country-specific regulatory interpretations or case-specific advice
- Operational combat procedures, targeting authority, or rules of engagement

---

## §3 Diagram

```mermaid
flowchart TD
    subgraph ECF ["Export Control & Legal Review Framework — Taxonomy (Q+ATLANTIDE · Non-Operational)"]
        ITAR["ITAR Classification Taxonomy\n─────────────────────\n22 CFR 120-130\nUS Munitions List (USML)\nRequires: Legal review\nStatus: PENDING"]
        EAR["EAR Classification Taxonomy\n─────────────────────\n15 CFR 730-774\nCommerce Control List (CCL)\nRequires: Legal review\nStatus: PENDING"]
        EUML["EU ML/CCL Taxonomy\n─────────────────────\nEU Military List\nDirective 2009/43/EC\nRequires: Legal review\nStatus: PENDING"]
        WA["Wassenaar Arrangement\n─────────────────────\nDual-use & munitions lists\nMultilateral framework\nRequires: Legal review\nStatus: PENDING"]
    end

    subgraph IHL ["IHL & Ethical Constraint Taxonomy"]
        PROP["Proportionality\n─────────────────────\nAP I to Geneva Conventions\nAbstract governance ref only"]
        DIST["Distinction\n─────────────────────\nAP I to Geneva Conventions\nAbstract governance ref only"]
        PREC["Precaution\n─────────────────────\nAP I to Geneva Conventions\nAbstract governance ref only"]
        ATT["UN Arms Trade Treaty\n─────────────────────\nNon-proliferation obligation\nGovernance acknowledgement"]
    end

    ECF -->|"Export-control gate\n(subsubject 006)"| LRG["Legal Review Gate\n(mandatory)"]
    IHL -->|"IHL compliance gate\n(mandatory)"| LRG
    LRG -->|"Gate passed"| EPS["Evidence Package\n(subsubject 008)"]

    style ITAR fill:#fadbd8,stroke:#c0392b
    style EAR fill:#fdf2f8,stroke:#8e44ad
    style EUML fill:#e8f4f8,stroke:#2c7bb6
    style WA fill:#eafaf1,stroke:#27ae60
    style PROP fill:#fef9e7,stroke:#f39c12
    style DIST fill:#fef9e7,stroke:#f39c12
    style PREC fill:#fef9e7,stroke:#f39c12
    style ATT fill:#d5f5e3,stroke:#1e8449
    style LRG fill:#d6eaf8,stroke:#1a5276
    style EPS fill:#ecf0f1,stroke:#95a5a6
    style ECF fill:#f8f9fa,stroke:#6c757d
    style IHL fill:#f0f0f0,stroke:#aaaaaa
```

---

## §4 Footprint

| Attribute | Value |
|---|---|
| Architecture | Defence Technology Type Architecture (DTTA) |
| Master range | 200–299 |
| Code range | 200-209 |
| Section | 00 |
| Subsection | 200 |
| Subsubject | 009 |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-LEG, ORB-PMO, ORB-FIN |
| Governance class | restricted[^gov] |
| Restricted rule | N-006[^n006] |
| Folder path | `Q+ATLANTIDE/200-299_DTTA/200-209_Sistemas-de-Combate-y-Armamento/200_Arquitectura-de-Sistemas-de-Combate/` |
| Document | `009_Export-Control-Legal-and-Ethical-Boundaries.md` |
| Parent subsection | [README.md](./README.md) · [000_Overview.md](./000_Overview.md) |
| Parent section | [../README.md](../README.md) |
| Parent architecture | [../../README.md](../../README.md) |
| Parent baseline | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

### Applicable Standards and Legal Instruments

| Instrument | Issuing Body | Applicability |
|---|---|---|
| ITAR (22 CFR 120-130) | US Government | International Traffic in Arms Regulations — US Munitions List classification taxonomy reference |
| EAR (15 CFR 730-774) | US Government | Export Administration Regulations — Commerce Control List classification taxonomy reference |
| EU Directive 2009/43/EC | EU | Intra-EU transfers of defence-related products — EU Military List classification reference |
| Wassenaar Arrangement | Multilateral | Dual-use goods and munitions — multilateral export control classification reference |
| UN Arms Trade Treaty | UN | Non-proliferation obligations — governance acknowledgement reference |
| Additional Protocol I to Geneva Conventions | ICRC/UN | IHL proportionality and distinction principles — abstract ethical governance reference |
| CCW Convention | UN | Convention on Certain Conventional Weapons — IHL compliance governance reference |

---

## §5 References & Citations

[^baseline]: Q+ATLANTIDE controlled baseline — authoritative taxonomy and traceability ecosystem governing all DTTA documents. See [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md).
[^archtable]: §3 Architecture Table (parent) — see [../../README.md](../../README.md).
[^qdiv]: Q-Division authority — Q-DATAGOV is the primary authority for governance and data taxonomy within Q+ATLANTIDE DTTA band; Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY provide technical domain support.
[^gov]: Governance class `restricted` — documents in this class require formal evidence packages, export-control review, and access controls per N-006.
[^n001]: Note N-001: Q+ATLANTIDE is a taxonomy and traceability ecosystem, not an operational programme; definitions herein are normative within the Q+ATLANTIDE register only.
[^n004]: Note N-004 (No-AAA Rule) — "AAA" is not a valid domain, division, architecture, interface or function in this baseline.
[^n006]: Note N-006 (Restricted bands) — Defence-related (200-299 DTTA) bands require additional governance, evidence packages and access controls. See [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) §5.3.
