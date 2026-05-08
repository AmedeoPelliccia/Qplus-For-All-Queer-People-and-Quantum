---
document_id: QATL-ATLAS1000-DTTA-200-209-00-200-000-OVERVIEW
title: "DTTA 200-209 · 00.200.000 — Overview"
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
subsubject: "000"
subsubject_title: "Overview"
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

# DTTA 200-209 · 00.200.000 — Overview

---

> **⚠ NON-OPERATIONAL BOUNDARY NOTICE**
> This document is a **restricted taxonomy and governance overview** within the Q+ATLANTIDE ATLAS-1000 register.
> It does **not** define targeting logic, weapon construction, deployment methods, tactical employment, performance optimisation for harm, or operational combat procedures.
> All content is normative exclusively within the Q+ATLANTIDE taxonomy and traceability ecosystem.[^n001][^n006]
> The **No-AAA Rule** applies.[^n004]

---

## §1 Purpose

This document is the entry-point for the **Arquitectura de Sistemas de Combate** subsection (200) of the DTTA 200-209 code range within the ATLAS-1000 register under the **Q+ATLANTIDE** controlled baseline.[^baseline]

The Overview establishes:

- **Shared vocabulary** — controlled terminology for combat systems architecture as used across all subsubjects 001–010 of this subsection.
- **Scope boundaries** — explicit delineation of what is and is not addressed within this taxonomy (non-operational governance only).
- **Navigational index** — a structured table linking all ten subsubject documents (001–010) with one-line scope descriptions.

All child documents (subsubjects 001–010) derive their authority from this entry-point and from the parent-section README ([../README.md](../README.md)). Any conflict between a child document and this Overview must be resolved by escalation to Q-DATAGOV with ORB-LEG review.

Documents in this subsection are classified `governance_class: restricted` per **N-006**.[^n006] Explicit human authority, rules-of-use governance, safety interlocks, legal admissibility, export-control review, independent assurance, and lifecycle traceability are **mandatory** for all subsubjects in this band.

The No-AAA Rule applies throughout this subsection.[^n004]

---

## §2 Scope

The following table provides a navigational index to all ten subsubject documents. Each entry includes a one-line description of scope.

| NNN | Title | Document | One-Line Scope |
|---:|---|---|---|
| 001 | Combat Systems Architecture Controlled Definition | [`001_Combat-Systems-Architecture-Controlled-Definition.md`](./001_Combat-Systems-Architecture-Controlled-Definition.md) | Normative Q+ATLANTIDE definition of "Combat Systems Architecture" and its taxonomy layers. |
| 002 | Defensive System Classes and Boundaries | [`002_Defensive-System-Classes-and-Boundaries.md`](./002_Defensive-System-Classes-and-Boundaries.md) | Classification taxonomy of defensive system classes and boundary declarations. |
| 003 | Platform System Integration Architecture | [`003_Platform-System-Integration-Architecture.md`](./003_Platform-System-Integration-Architecture.md) | Integration architecture taxonomy for combat platforms (physical, data, software, HMI layers). |
| 004 | Command, Control and Human Authority Interfaces | [`004_Command-Control-and-Human-Authority-Interfaces.md`](./004_Command-Control-and-Human-Authority-Interfaces.md) | C2 interface taxonomy and mandatory human authority levels (HITL/HOTL). |
| 005 | Sensor, Effector and Decision-Chain Abstraction | [`005_Sensor-Effector-and-Decision-Chain-Abstraction.md`](./005_Sensor-Effector-and-Decision-Chain-Abstraction.md) | Abstract taxonomy of sensor-effector relationships and OODA-loop decision-chain governance model. |
| 006 | Safety Interlocks, Rules-of-Use and Authorization Gates | [`006_Safety-Interlocks-Rules-of-Use-and-Authorization-Gates.md`](./006_Safety-Interlocks-Rules-of-Use-and-Authorization-Gates.md) | Taxonomy and governance framework for safety interlocks, ROU declarations, and authorization gates. |
| 007 | Interoperability, NATO, EU and Standards Mapping | [`007_Interoperability-NATO-EU-and-Standards-Mapping.md`](./007_Interoperability-NATO-EU-and-Standards-Mapping.md) | Applicability matrix mapping subsection functions to NATO, EU, and international standards. |
| 008 | Assurance, Verification and Non-Operational Evidence | [`008_Assurance-Verification-and-Non-Operational-Evidence.md`](./008_Assurance-Verification-and-Non-Operational-Evidence.md) | Assurance framework, verification taxonomy, and evidence package requirements. |
| 009 | Export Control, Legal and Ethical Boundaries | [`009_Export-Control-Legal-and-Ethical-Boundaries.md`](./009_Export-Control-Legal-and-Ethical-Boundaries.md) | Export control classification taxonomy, legal boundaries, and ethical constraints. |
| 010 | Traceability, Evidence and Lifecycle Governance | [`010_Traceability-Evidence-and-Lifecycle-Governance.md`](./010_Traceability-Evidence-and-Lifecycle-Governance.md) | Lifecycle governance, evidence package requirements, and traceability obligations for the full subsection. |

---

## §3 Footprint

| Attribute | Value |
|---|---|
| Architecture | Defence Technology Type Architecture (DTTA) |
| Master range | 200–299 |
| Code range | 200-209 |
| Section | 00 |
| Subsection | 200 |
| Subsubject | 000 |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-LEG, ORB-PMO, ORB-FIN |
| Governance class | restricted[^gov] |
| Restricted rule | N-006[^n006] |
| Folder path | `Q+ATLANTIDE/200-299_DTTA/200-209_Sistemas-de-Combate-y-Armamento/200_Arquitectura-de-Sistemas-de-Combate/` |
| Document | `000_Overview.md` |
| Parent subsection | [README.md](./README.md) |
| Parent section | [../README.md](../README.md) |
| Parent architecture | [../../README.md](../../README.md) |
| Parent baseline | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

---

### Applicable Standards

| Standard | Issuing Body | Applicability |
|---|---|---|
| STANAG 4586 | NATO | UAV Control System Interoperability — platform interface taxonomy reference |
| STANAG 2490 | NATO | Defence Platform Integration — integration boundary reference |
| IEC 62443 | IEC | Industrial Automation Security — cybersecurity taxonomy for integrated systems |
| ISO/IEC 27001 | ISO/IEC | Information Security Management — access control and governance framework |
| ARP4754A | SAE | Development of Civil Aircraft and Systems — assurance taxonomy reference |
| STANAG 4569 | NATO | Protection Levels for Armoured Vehicles — defensive system classification reference |

---

## §4 References & Citations

[^baseline]: Q+ATLANTIDE controlled baseline — authoritative taxonomy and traceability ecosystem governing all DTTA documents. See [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md).
[^archtable]: §3 Architecture Table (parent) — see [../../README.md](../../README.md).
[^qdiv]: Q-Division authority — Q-DATAGOV is the primary authority for governance and data taxonomy within Q+ATLANTIDE DTTA band; Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY provide technical domain support.
[^gov]: Governance class `restricted` — documents in this class require formal evidence packages, export-control review, and access controls per N-006.
[^n001]: Note N-001: Q+ATLANTIDE is a taxonomy and traceability ecosystem, not an operational programme; definitions herein are normative within the Q+ATLANTIDE register only.
[^n004]: Note N-004 (No-AAA Rule) — "AAA" is not a valid domain, division, architecture, interface or function in this baseline.
[^n006]: Note N-006 (Restricted bands) — Defence-related (200-299 DTTA) bands require additional governance, evidence packages and access controls. See [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) §5.3.
