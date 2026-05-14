---
document_id: QATL-ATLAS1000-DTTA-200-209-00-200-002-DEFENSIVE-SYSTEM-CLASSES-AND-BOUNDARIES
title: "DTTA 200-209 · 00.200.002 — Defensive System Classes and Boundaries"
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
subsubject: "002"
subsubject_title: "Defensive System Classes and Boundaries"
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

# DTTA 200-209 · 00.200.002 — Defensive System Classes and Boundaries

---

> **⚠ NON-OPERATIONAL BOUNDARY NOTICE**
> This document is a **restricted taxonomy and governance classification** within the Q+ATLANTIDE ATLAS-1000 register.
> It does **not** define weapon construction, deployment methods, tactical employment, performance optimisation for harm, offensive applications, or operational combat procedures.
> All content is normative exclusively within the Q+ATLANTIDE taxonomy and traceability ecosystem.[^n001][^n006]
> The **No-AAA Rule** applies.[^n004]
> Documents in this band are classified `governance_class: restricted` per N-006.[^n006] Explicit human authority, rules-of-use governance, safety interlocks, legal admissibility, export-control review, independent assurance, and lifecycle traceability are **required**.

---

## §1 Purpose

This document defines the **Q+ATLANTIDE taxonomy of defensive system classes** and their governance boundaries within the DTTA 200 subsection.[^baseline]

The taxonomy identifies four primary defensive system classes for classification and governance purposes:

1. **Active Protection Systems (APS)** — systems classified as providing kinetic or non-kinetic countermeasures against inbound threats, for taxonomy and governance classification only.
2. **Passive Protection Systems (PPS)** — systems classified as providing structural, material, or signature-reduction protection, for taxonomy classification only.
3. **C2/ISR-Support Systems** — systems classified as providing command, control, intelligence, surveillance, and reconnaissance support functions, for taxonomy classification only.
4. **Logistical and Support Systems** — systems classified as providing sustainment, maintenance, and logistical support, for taxonomy classification only.

All class definitions are **classification taxonomy only**. They do not constitute construction specifications, performance requirements, or operational employment guidance. The boundary between classes is a governance boundary, not a physical design boundary.

No content in this document addresses offensive applications, targeting, weapon construction, or performance optimisation. The classification taxonomy is designed to support export-control review, assurance scoping, and standards applicability mapping only.

---

## §2 Scope

### In Scope

- Classification taxonomy of defensive system classes (APS, PPS, C2/ISR-Support, Logistical/Support)
- Boundary definitions between classes for governance and export-control purposes
- Declarations of interface boundaries between defensive class taxonomy and other taxonomy layers defined in subsubject 001
- Mapping of defensive classes to applicable governance requirements (safety, assurance, export-control)
- Disambiguation of defensive vs. non-defensive categories within Q+ATLANTIDE taxonomy

### Out of Scope

- Construction details, materials specifications, or hardware design for any class
- Offensive applications, offensive-defensive hybrid systems performance parameters
- Lethality, range, or performance parameters of any system class
- Classified system specifications or programme-specific data
- Operational employment guidance or tactical procedures for any class

---

## §3 Diagram

```mermaid
flowchart TD
    subgraph DSC ["Defensive System Classes — Taxonomy (Q+ATLANTIDE · Non-Operational)"]
        APS["Active Protection Systems (APS)\n─────────────────────────────\nClass: Active countermeasure taxonomy\nGovernance boundary: N-006\nExport-control review: Required\nSafety: IEC 61508 SIL applicable"]
        PPS["Passive Protection Systems (PPS)\n─────────────────────────────\nClass: Structural/signature protection\nGovernance boundary: N-006\nExport-control review: Required\nSafety: IEC 62443 applicable"]
        C2ISR["C2/ISR-Support Systems\n─────────────────────────────\nClass: C&C / intelligence / surveillance\nGovernance boundary: N-006\nHuman authority: Mandatory\nStandards: STANAG 4586"]
        LOG["Logistical & Support Systems\n─────────────────────────────\nClass: Sustainment / maintenance\nGovernance boundary: N-006\nExport-control review: Required\nStandards: STANAG 2490"]
    end

    PLAT["Platform Layer\n(subsubject 001 taxonomy)"]

    PLAT -->|"Integration boundary"| APS
    PLAT -->|"Integration boundary"| PPS
    PLAT -->|"Integration boundary"| C2ISR
    PLAT -->|"Integration boundary"| LOG

    APS <-->|"Class boundary\n(governance)"| PPS
    C2ISR <-->|"Authority interface\n(taxonomy)"| APS
    C2ISR <-->|"Authority interface\n(taxonomy)"| PPS

    style APS fill:#fdf2f8,stroke:#8e44ad
    style PPS fill:#eafaf1,stroke:#27ae60
    style C2ISR fill:#fef9e7,stroke:#f39c12
    style LOG fill:#e8f4f8,stroke:#2c7bb6
    style DSC fill:#f8f9fa,stroke:#6c757d
    style PLAT fill:#ecf0f1,stroke:#95a5a6
```

> **Diagram note:** All class names and boundary labels are Q+ATLANTIDE governance taxonomy identifiers. This diagram does not represent any specific system, programme, or operational design.

---

## §4 Footprint

| Attribute | Value |
|---|---|
| Architecture | Defence Technology Type Architecture (DTTA) |
| Master range | 200–299 |
| Code range | 200-209 |
| Section | 00 |
| Subsection | 200 |
| Subsubject | 002 |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-LEG, ORB-PMO, ORB-FIN |
| Governance class | restricted[^gov] |
| Restricted rule | N-006[^n006] |
| Folder path | `Q+ATLANTIDE/200-299_DTTA/200-209_Sistemas-de-Combate-y-Armamento/200_Arquitectura-de-Sistemas-de-Combate/` |
| Document | `002_Defensive-System-Classes-and-Boundaries.md` |
| Parent subsection | [README.md](./README.md) · [000_Overview.md](./000_Overview.md) |
| Parent section | [../README.md](../README.md) |
| Parent architecture | [../../README.md](../../README.md) |
| Parent baseline | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

### Applicable Standards

| Standard | Issuing Body | Applicability |
|---|---|---|
| IEC 61508 | IEC | Functional Safety — SIL classification applicable to APS class taxonomy |
| IEC 62443 | IEC | Industrial Automation Security — applicable to PPS and C2/ISR class taxonomy |
| STANAG 4586 | NATO | UAV Control System Interoperability — C2/ISR-Support class taxonomy reference |
| STANAG 2490 | NATO | Defence Platform Integration — Logistical/Support class integration boundary reference |
| STANAG 4569 | NATO | Protection Levels for Armoured Vehicles — PPS class taxonomy reference |

---

## §5 References & Citations

[^baseline]: Q+ATLANTIDE controlled baseline — authoritative taxonomy and traceability ecosystem governing all DTTA documents. See [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md).
[^archtable]: §3 Architecture Table (parent) — see [../../README.md](../../README.md).
[^qdiv]: Q-Division authority — Q-DATAGOV is the primary authority for governance and data taxonomy within Q+ATLANTIDE DTTA band; Q-SPACE, Q-HORIZON, Q-HPC, Q-STRUCTURES, Q-INDUSTRY provide technical domain support.
[^gov]: Governance class `restricted` — documents in this class require formal evidence packages, export-control review, and access controls per N-006.
[^n001]: Note N-001: Q+ATLANTIDE is a taxonomy and traceability ecosystem, not an operational programme; definitions herein are normative within the Q+ATLANTIDE register only.
[^n004]: Note N-004 (No-AAA Rule) — "AAA" is not a valid domain, division, architecture, interface or function in this baseline.
[^n006]: Note N-006 (Restricted bands) — Defence-related (200-299 DTTA) bands require additional governance, evidence packages and access controls. See [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) §5.3.
