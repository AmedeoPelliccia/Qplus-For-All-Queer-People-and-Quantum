---
document_id: QATL-ATLAS1000-DTTA-200-209-00-200-README
title: "DTTA 200-209 · 00.200 — Arquitectura de Sistemas de Combate (Subsection Index)"
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

# DTTA 200-209 · Section 00 · Subsection 200 — Arquitectura de Sistemas de Combate

---

> **⚠ NON-OPERATIONAL BOUNDARY NOTICE**
> This document is a **restricted taxonomy and governance index** within the Q+ATLANTIDE ATLAS-1000 register.
> It does **not** define targeting logic, weapon construction, deployment methods, tactical employment, performance optimisation for harm, or operational combat procedures.
> All content is normative exclusively within the Q+ATLANTIDE taxonomy and traceability ecosystem.[^n001][^n006]

---

## §1 Purpose

This README is the subsection-level index for **Arquitectura de Sistemas de Combate** (subsection 200), part of the DTTA 200-209 code range within the ATLAS-1000 register under the **Q+ATLANTIDE** controlled baseline.[^baseline]

The subsection establishes a governed vocabulary and traceability structure for combat systems architecture **taxonomy and governance** only. It reserves subsubject namespace `000`–`999` under subsection 200, allocating the first eleven positions (`000`–`010`) to the documents listed in §3.

Documents in this subsection are classified `governance_class: restricted` per **N-006**[^n006] and must satisfy the following requirements:

- Explicit human authority and rules-of-use declarations
- Safety interlock taxonomy compliance
- Legal admissibility and export-control review
- Independent assurance and lifecycle traceability
- Evidence package declaration (or `PENDING` acknowledgement with remediation plan)

The **No-AAA Rule** applies throughout this subsection.[^n004] No document, diagram, or reference in this subsection may designate any domain, division, architecture, interface, or function using the identifier "AAA".

All content is bounded by the non-operational constraint: governance, taxonomy, and traceability purposes only. References to combat systems architecture concepts do not constitute authorisation, specification, or guidance for the construction, deployment, or employment of weapon systems.[^n006][^n004]

---

## §2 Scope

This subsection reserves the subsubject namespace `000`–`999` under subsection 200. Authority derives from Q-Division governance inherited from the Q+ATLANTIDE baseline.[^qdiv]

Each subsubject listed in §3 inherits:

- All shared YAML frontmatter fields from this README
- Restricted governance classification per N-006
- Non-operational boundary constraint
- No-AAA Rule

No subsubject in this namespace may address operational combat procedures, targeting logic, weapon construction, deployment instructions, or performance optimisation for harm.

---

## §3 Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 001 | Combat Systems Architecture Controlled Definition | [`001_Combat-Systems-Architecture-Controlled-Definition.md`](./001_Combat-Systems-Architecture-Controlled-Definition.md) | active |
| 002 | Defensive System Classes and Boundaries | [`002_Defensive-System-Classes-and-Boundaries.md`](./002_Defensive-System-Classes-and-Boundaries.md) | active |
| 003 | Platform System Integration Architecture | [`003_Platform-System-Integration-Architecture.md`](./003_Platform-System-Integration-Architecture.md) | active |
| 004 | Command, Control and Human Authority Interfaces | [`004_Command-Control-and-Human-Authority-Interfaces.md`](./004_Command-Control-and-Human-Authority-Interfaces.md) | active |
| 005 | Sensor, Effector and Decision-Chain Abstraction | [`005_Sensor-Effector-and-Decision-Chain-Abstraction.md`](./005_Sensor-Effector-and-Decision-Chain-Abstraction.md) | active |
| 006 | Safety Interlocks, Rules-of-Use and Authorization Gates | [`006_Safety-Interlocks-Rules-of-Use-and-Authorization-Gates.md`](./006_Safety-Interlocks-Rules-of-Use-and-Authorization-Gates.md) | active |
| 007 | Interoperability, NATO, EU and Standards Mapping | [`007_Interoperability-NATO-EU-and-Standards-Mapping.md`](./007_Interoperability-NATO-EU-and-Standards-Mapping.md) | active |
| 008 | Assurance, Verification and Non-Operational Evidence | [`008_Assurance-Verification-and-Non-Operational-Evidence.md`](./008_Assurance-Verification-and-Non-Operational-Evidence.md) | active |
| 009 | Export Control, Legal and Ethical Boundaries | [`009_Export-Control-Legal-and-Ethical-Boundaries.md`](./009_Export-Control-Legal-and-Ethical-Boundaries.md) | active |
| 010 | Traceability, Evidence and Lifecycle Governance | [`010_Traceability-Evidence-and-Lifecycle-Governance.md`](./010_Traceability-Evidence-and-Lifecycle-Governance.md) | active |

---

## §4 Footprint

| Attribute | Value |
|---|---|
| Architecture | Defence Technology Type Architecture (DTTA) |
| Master range | 200–299 |
| Code range | 200-209 |
| Section | 00 |
| Subsection | 200 |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-LEG, ORB-PMO, ORB-FIN |
| Governance class | restricted[^gov] |
| Restricted rule | N-006[^n006] |
| Folder path | `Q+ATLANTIDE/200-299_DTTA/200-209_Sistemas-de-Combate-y-Armamento/200_Arquitectura-de-Sistemas-de-Combate/` |
| Document (this file) | `README.md` |
| Parent section | [../README.md](../README.md) |
| Parent architecture | [../../README.md](../../README.md) |
| Parent baseline | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

---

## § Governance

This subsection is governed by the Q+ATLANTIDE baseline ([organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md)). All subsubjects (`000`–`010`) inherit `governance_class: restricted` and must individually:

1. Declare a valid `evidence_package_id` (or formally register `PENDING` with a remediation schedule) per N-006.
2. Declare a valid `access_control_profile` per N-006.
3. Comply with the No-AAA Rule (N-004).[^n004]
4. Maintain the non-operational boundary: taxonomy and governance only — no targeting logic, no weapon construction, no deployment methods, no tactical employment, no operational combat procedures.
5. Include applicable standards traceability and export-control review status.

Any amendment to this index must be reviewed by Q-DATAGOV and ORB-LEG before publication. Changes affecting the standards mapping (subsubject 007) additionally require ORB-FIN assessment for export-control implications.

---

## §5 References & Citations

[^baseline]: Q+ATLANTIDE controlled baseline — authoritative taxonomy and traceability ecosystem governing all DTTA documents. See [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md).
[^archtable]: §3 Architecture Table (parent) — see [../../README.md](../../README.md).
[^qdiv]: Q-Division authority — Q-DATAGOV is the primary authority for governance and data taxonomy within Q+ATLANTIDE DTTA band; Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY provide technical domain support.
[^gov]: Governance class `restricted` — documents in this class require formal evidence packages, export-control review, and access controls per N-006.
[^n001]: Note N-001: Q+ATLANTIDE is a taxonomy and traceability ecosystem, not an operational programme; definitions herein are normative within the Q+ATLANTIDE register only.
[^n002]: Note N-002: Document identifiers and codes in this register are internal taxonomy references and do not correspond to or disclose any classified programme, system, or capability.
[^n004]: Note N-004 (No-AAA Rule) — "AAA" is not a valid domain, division, architecture, interface or function in this baseline.
[^n006]: Note N-006 (Restricted bands) — Defence-related (200-299 DTTA) bands require additional governance, evidence packages and access controls. See [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) §5.3.
