---
document_id: QATL-ATLAS-1000-STA-190-199-09-190-000-OVERVIEW
title: "STA 190-199 · 09.190.000 — Overview"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "190-199"
section: "09"
section_title: "Sistemas Avanzados, Conceptos y Futuro Espacial"
subsection: "190"
subsection_title: "Arquitecturas Interplanetarias"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-DATAGOV, Q-HPC, Q-GREENTECH, Q-STRUCTURES, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 190-199 · 09.190.000 — Overview

## §1 Purpose

This document is the controlled entry-point for the **Arquitecturas Interplanetarias** subsection (`190`) within the *Sistemas Avanzados, Conceptos y Futuro Espacial* code range (`190-199`) of the Space Technology Architecture (STA) master range `100–199`.[^baseline] It establishes the shared vocabulary, scope boundaries, and navigational index for all interplanetary architecture topics governed under Q+ATLANTIDE.[^n001]

The Overview anchors eleven subsubject files that together constitute the complete Interplanetary Architecture knowledge domain: from controlled definitions and mission-class taxonomy through trajectory design, propulsion interfaces, communications, surface/orbital infrastructure, autonomy, human factors, standards mapping, and lifecycle governance. All child documents derive their authority from this entry-point and from the parent-section README.[^archtable]

**Safety boundary:** This subsection is classified *interplanetary-architecture critical*. All documents require explicit mission-class definition, trajectory assumptions, deep-space communication and navigation constraints, autonomy boundaries, radiation and life-support analysis, infrastructure interface declarations, and full lifecycle traceability before any claim of compliance with this baseline may be made.[^qdiv]

## §2 Scope

The following ten subsubjects are defined within subsection `190`:[^qdiv]

| ID | File | One-line description |
|----|------|----------------------|
| 001 | [001_Interplanetary-Architecture-Controlled-Definition.md](./001_Interplanetary-Architecture-Controlled-Definition.md) | Establishes the Q+ATLANTIDE controlled definition of "Interplanetary Architecture" and its regime taxonomy. |
| 002 | [002_Mission-Classes-and-Interplanetary-Regimes.md](./002_Mission-Classes-and-Interplanetary-Regimes.md) | Defines the formal mission-class taxonomy (flyby through crewed surface) and all regime boundary conditions. |
| 003 | [003_Trajectory-Architecture-and-Transfer-Windows.md](./003_Trajectory-Architecture-and-Transfer-Windows.md) | Specifies trajectory architecture requirements — transfers, gravity assists, launch windows, and delta-V budgets. |
| 004 | [004_Deep-Space-Transport-and-Propulsion-Interfaces.md](./004_Deep-Space-Transport-and-Propulsion-Interfaces.md) | Architecture-level interface control between the transport vehicle and its propulsion system across all propulsion classes. |
| 005 | [005_Communication-Navigation-and-Time-Reference-Boundaries.md](./005_Communication-Navigation-and-Time-Reference-Boundaries.md) | Defines deep-space link architecture, navigation reference frames, light-time constraints, and time-system boundaries. |
| 006 | [006_Surface-Orbital-and-Transit-Infrastructure-Interfaces.md](./006_Surface-Orbital-and-Transit-Infrastructure-Interfaces.md) | Specifies interfaces between transit vehicle and surface, orbital, and in-space infrastructure elements. |
| 007 | [007_Autonomy-Safe-Modes-and-Long-Duration-Operations.md](./007_Autonomy-Safe-Modes-and-Long-Duration-Operations.md) | Classifies autonomy tiers, safe-mode hierarchies, FDIR architecture, and long-duration operations protocols. |
| 008 | [008_Radiation-Life-Support-and-Human-Factors-Boundaries.md](./008_Radiation-Life-Support-and-Human-Factors-Boundaries.md) | Characterises the radiation environment, ECLSS boundary requirements, and human-factors constraints for crewed missions. |
| 009 | [009_ECSS-NASA-CCSDS-Deep-Space-Standards-Mapping.md](./009_ECSS-NASA-CCSDS-Deep-Space-Standards-Mapping.md) | Maps each interplanetary architecture function to the applicable normative ECSS, NASA, and CCSDS standard. |
| 010 | [010_Traceability-Evidence-and-Lifecycle-Governance.md](./010_Traceability-Evidence-and-Lifecycle-Governance.md) | Defines evidence-package requirements, review gates (MDR through ORR), and mission-archive closure records. |

## §3 Footprint

| Attribute | Value |
|-----------|-------|
| Architecture | Space Technology Architecture (STA) |
| Master range | 100–199 |
| Code range | 190-199 |
| Section | 09 |
| Subsection | 190 |
| Subsubject | 000 |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-DATAGOV, Q-HPC, Q-GREENTECH, Q-STRUCTURES, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | baseline[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/190-199_Sistemas-Avanzados-Conceptos-y-Futuro-Espacial/190_Arquitecturas-Interplanetarias/` |
| Document | `000_Overview.md` |
| Parent subsection | [../README.md](../README.md) |
| Parent architecture | [../../README.md](../../README.md) |
| Parent baseline | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

## §4 References & Citations

[^baseline]: Q+ATLANTIDE controlled baseline — the authoritative taxonomy and traceability ecosystem governing all Space Technology Architecture documents.
[^archtable]: §3 Architecture Table (parent) — see [../../README.md](../../README.md) for the master architecture index.
[^qdiv]: Q-Division authority — Q-SPACE is the primary authority for all interplanetary architecture standards within Q+ATLANTIDE; Q-HORIZON, Q-DATAGOV, Q-HPC, Q-GREENTECH, Q-STRUCTURES, and Q-INDUSTRY provide supporting governance.
[^gov]: Governance class `baseline` — documents in this class are subject to formal change control under ORB-PMO and ORB-LEG review gates.
[^n001]: Note N-001: Q+ATLANTIDE is a taxonomy and traceability ecosystem; definitions herein are normative within the Q+ATLANTIDE register only.
[^ecss1002]: ECSS-E-ST-10-02C — *Space engineering: Verification*, European Cooperation for Space Standardization, 6 March 2009.
[^ecssm10]: ECSS-M-ST-10C — *Space project management: Project planning and implementation*, European Cooperation for Space Standardization, 6 March 2009.
[^nasa7009]: NASA/SP-2016-6105 — *NASA Systems Engineering Handbook*, Rev. 2, National Aeronautics and Space Administration, 2016.
[^ccsds401]: CCSDS 401.0-B — *Radio Frequency and Modulation Systems*, Consultative Committee for Space Data Systems, Blue Book.
[^ecss50]: ECSS-E-ST-50C — *Space engineering: Communications*, European Cooperation for Space Standardization, 31 July 2008.

### Applicable industry standards

| Standard | Title | Body |
|----------|-------|------|
| ECSS-E-ST-10-02C | Space engineering: Verification | ECSS |
| ECSS-M-ST-10C | Space project management: Project planning and implementation | ECSS |
| NASA/SP-2016-6105 | NASA Systems Engineering Handbook | NASA |
| CCSDS 401.0-B | Radio Frequency and Modulation Systems | CCSDS |
| ECSS-E-ST-50C | Space engineering: Communications | ECSS |
