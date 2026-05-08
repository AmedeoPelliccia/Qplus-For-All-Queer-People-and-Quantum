---
document_id: QATL-ATLAS1000-DTTA-200-209-00-203-009-LEGAL-ETHICAL-AND-RULES-OF-USE-CONSTRAINTS
title: "DTTA 200-209 · 00.203.009 — Legal, Ethical and Rules-of-Use Constraints"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: DTTA
architecture_name: "Defence Technology Type Architecture"
master_range: "200–299"
code_range: "200-209"
section: "00"
section_title: "Sistemas de Combate y Armamento"
subsection: "203"
subsection_title: "Sistemas de Control de Fuego No Operacional"
subsubject: "009"
subsubject_title: "Legal, Ethical and Rules-of-Use Constraints"
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

# DTTA 200-209 · Section 00 · Subsection 203 · Subsubject 009 — Legal, Ethical and Rules-of-Use Constraints

## 1. Purpose

This subsubject establishes the governance taxonomy of legal, ethical and rules-of-use constraints applicable to fire-control systems within the DTTA `200-209` subsection `203`. It maps International Humanitarian Law, human rights law, national legal frameworks and ethical principles to governance requirements at the taxonomy layer, for evidence-packaging and traceability purposes.

No operational Rules of Engagement, targeting law interpretation or specific legal advice is provided herein.

## 2. Scope

- Covers the *Legal, Ethical and Rules-of-Use Constraints* subsubject (`009`) of subsection `203`.
- Concepts in scope:
  - **IHL constraint taxonomy** — The governance classification of International Humanitarian Law principles (distinction, proportionality, precaution, humanity) as governance constraints on fire-control system taxonomy and evidence requirements.
  - **Human rights law governance hooks** — The governance requirement that human rights law instruments (ECHR Article 2, ICCPR Article 6) are mapped as governance constraints on any fire-control system human-authority interface.
  - **Ethical constraint governance** — The governance taxonomy of ethical constraints derived from international instruments and professional standards (ICRC LAWS guidance, UN GGE deliberations) applied as governance-layer requirements; not ethical certification or determination.
  - **Rules-of-Use governance boundary** — The governance concept of a rules-of-use boundary: the governance demarcation between permissible system use governed by IHL and prohibited system use; treated as a traceability construct only.
  - **Legal admissibility governance** — The governance requirements that fire-control system evidence packages must satisfy for legal admissibility review: chain of custody, human attribution, and IHL constraint traceability.
- Out of scope: specific Rules of Engagement text, legal advice on targeting or use of force, interpretation of IHL in specific operational contexts, ethical certification services, human rights assessments of specific systems and any operational deployment guidance.

## 3. Diagram — Legal and Ethical Governance Constraint Map

```mermaid
flowchart TD
    A["Legal & Ethical\nConstraint Taxonomy (009)"] --> B["IHL Principles\n(Distinction · Proportionality\nPrecaution · Humanity)"]
    A --> C["Human Rights Law\n(ECHR Art. 2\nICCPR Art. 6)"]
    A --> D["Ethical Constraints\n(ICRC LAWS Guidance\nUN GGE Deliberations)"]
    B --> E["Governance Hook:\nDistinction → 003_Sensor\n→ 004_Human-Authority"]
    B --> F["Governance Hook:\nProportionality → 005_Engagement-Chain"]
    C --> G["Governance Hook:\nRight-to-Life → 004_Human-Authority\n→ 010_Traceability"]
    D --> H["Governance Hook:\nEthical Constraint → 010_Traceability\nEvidence Package"]
    E --> I["Legal Admissibility\nGovernance Requirements"]
    F --> I
    G --> I
    H --> I
    style A fill:#1a3a5c,color:#fff
    style I fill:#1a3a5c,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `DTTA` — Defence Technology Type Architecture |
| Master range | `200–299` |
| Code range | `200-209` |
| Section | `00` — Sistemas de Combate y Armamento |
| Subsection | `203` — Sistemas de Control de Fuego No Operacional |
| Subsubject | `009` — Legal, Ethical and Rules-of-Use Constraints |
| Primary Q-Division | Q-DATAGOV |
| Support Q-Divisions | Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-LEG, ORB-PMO, ORB-FIN |
| Governance class | `restricted` |
| Document | `009_Legal-Ethical-and-Rules-of-Use-Constraints.md` (this file) |
| Subsection index | [`README.md`](./README.md) |
| Parent section | [`../README.md`](../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^geneva]: **Geneva Conventions (1949) and Additional Protocols I & II** — Fundamental IHL instruments; distinction (AP I Art. 48), proportionality (AP I Art. 51.5b), precaution (AP I Art. 57), and humanity principles are mapped as governance constraints.
[^echr]: **European Convention on Human Rights, Article 2** — Right to life; mapped as human rights law governance hook for human-authority interface requirements.
[^iccpr]: **International Covenant on Civil and Political Rights, Article 6** — Right to life; maps as human rights law governance constraint on fire-control authorization chains.
[^icrclaws]: **ICRC (2019) — Autonomy, artificial intelligence and robotics: Technical aspects of human control.** Provides ethical constraint taxonomy context for autonomous system governance hooks.
[^ungge]: **UN Group of Governmental Experts on LAWS (2021) — Report to the CCW.** Ethical principle guidance from GGE deliberations mapped as governance-layer ethical constraints.
[^n006]: **Note N-006 (Restricted bands)** — Defence-related (`200-299` DTTA) bands require additional governance, evidence packages and access controls. See [`organization/Q+ATLANTIDE.md` §5.3](../../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).
