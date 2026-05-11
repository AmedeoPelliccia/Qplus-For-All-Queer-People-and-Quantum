---
document_id: QATL-ATLAS-1000-STA-150-159-05-150-000-GENERAL
title: "STA 150-159 · 150-000 — General"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "150-159"
section: "05"
section_title: "Comunicaciones Espaciales"
subsection: "150"
subsection_title: "SATCOM"
subsubject: "000"
subsubject_title: "General"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 150-159 · 150-000 — General

## §1 Purpose

This document is the controlled entry-point for the **SATCOM** subsection (`150`) within the *Comunicaciones Espaciales* code range (`150-159`) of the Space Technology Architecture (STA) master range `100–199`.[^baseline] It establishes the shared vocabulary, scope boundaries, and navigational index for all satellite-communication topics governed under Q+ATLANTIDE.[^n001]

The Overview anchors the eleven subsubject files that together constitute the complete SATCOM knowledge domain: from controlled terminology and link architecture through encryption, interference, standards mapping, and lifecycle governance. All child documents derive their authority from this entry-point and from the parent-section README.[^archtable]

## §2 Scope

The following ten subsubjects are defined within subsection `150`:[^qdiv]

| ID | File | One-line description |
|-----|------|----------------------|
| 010 | [150-010-SATCOM-Controlled-Definition.md](./150-010-SATCOM-Controlled-Definition.md) | Establishes the Q+ATLANTIDE controlled definition of SATCOM and its taxonomy of orbit types and frequency bands. |
| 020 | [150-020-Satellite-Communication-Architecture.md](./150-020-Satellite-Communication-Architecture.md) | Defines the complete three-segment link architecture: space, ground, and user segments. |
| 030 | [150-030-Link-Budget-Frequency-Bands-and-Modulation.md](./150-030-Link-Budget-Frequency-Bands-and-Modulation.md) | Specifies the link-budget methodology, frequency band assignments, modulation schemes, and coding standards. |
| 040 | [150-040-Antennas-Terminals-and-RF-Interfaces.md](./150-040-Antennas-Terminals-and-RF-Interfaces.md) | Defines antenna types, terminal classes, and RF interface specifications from terminal to satellite. |
| 050 | [150-050-Telecommand-Telemetry-and-Payload-Data-Links.md](./150-050-Telecommand-Telemetry-and-Payload-Data-Links.md) | Defines TC/TM/payload data-link classes and CCSDS protocol assignments. |
| 060 | [150-060-Ground-Station-and-Network-Interfaces.md](./150-060-Ground-Station-and-Network-Interfaces.md) | Defines ground-station functional elements and network interfaces to IP/MPLS backbones. |
| 070 | [150-070-Encryption-Authentication-and-COMSEC-Boundaries.md](./150-070-Encryption-Authentication-and-COMSEC-Boundaries.md) | Defines the COMSEC architecture, key management, and Q+ATLANTIDE boundary declarations. |
| 080 | [150-080-Interference-Spectrum-and-Regulatory-Constraints.md](./150-080-Interference-Spectrum-and-Regulatory-Constraints.md) | Classifies interference types, spectrum-coordination obligations, and mitigation techniques. |
| 090 | [150-090-Traceability-Evidence-and-Lifecycle-Governance.md](./150-090-Traceability-Evidence-and-Lifecycle-Governance.md) | Maps each SATCOM function to the applicable normative standard. |
| 100 | [`150-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./150-090-Traceability-Evidence-and-Lifecycle-Governance.md) | Defines evidence-package requirements, review gates, and end-of-life decommissioning records. |

## §3 Footprint

| Attribute | Value |
|-----------|-------|
| Architecture | Space Technology Architecture (STA) |
| Master range | 100–199 |
| Code range | 150-159 |
| Section | 05 |
| Subsection | 150 |
| Subsubject | 000 |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | baseline[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/150-159_Comunicaciones-Espaciales/150_SATCOM/` |
| Document | `150-000-General.md` |
| Parent subsection | [../README.md](../README.md) |
| Parent architecture | [../../README.md](../../README.md) |
| Parent baseline | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

## §4 References & Citations

[^baseline]: Q+ATLANTIDE controlled baseline — the authoritative taxonomy and traceability ecosystem governing all Space Technology Architecture documents.
[^archtable]: §3 Architecture Table (parent) — see [../../README.md](../../README.md) for the master architecture index.
[^qdiv]: Q-Division authority — Q-SPACE is the primary authority for all space-segment and satellite communication standards within Q+ATLANTIDE; Q-DATAGOV and Q-HPC provide supporting governance for data handling and computation.
[^gov]: Governance class `baseline` — documents in this class are subject to formal change control under ORB-PMO and ORB-LEG review gates.
[^n001]: Note N-001: Q+ATLANTIDE is a taxonomy and traceability ecosystem, not an operational programme; all definitions herein are normative within the Q+ATLANTIDE register only.
[^ecss50]: ECSS-E-ST-50C — *Space engineering: Communications*, European Cooperation for Space Standardization, 31 July 2008.
[^ccsds401]: CCSDS 401.0-B — *Radio Frequency and Modulation Systems*, Consultative Committee for Space Data Systems, Blue Book.
[^itur]: ITU-R S.1003 — *Environmental protection of the geostationary-satellite orbit*, International Telecommunication Union Radiocommunication Sector.
[^nasa4005]: NASA-STD-4005 — *Low Earth Orbit Spacecraft Charging Design Standard*, NASA Technical Standards Program.
[^ccsds131]: CCSDS 131.0-B — *TM Synchronization and Channel Coding*, Consultative Committee for Space Data Systems, Blue Book.
[^ccsds132]: CCSDS 132.0-B — *TM Space Data Link Protocol*, Consultative Committee for Space Data Systems, Blue Book.
[^ccsds133]: CCSDS 133.0-B — *Encapsulation Service*, Consultative Committee for Space Data Systems, Blue Book.

### Applicable industry standards

| Standard | Title | Body |
|----------|-------|------|
| ECSS-E-ST-50C | Space engineering: Communications | ECSS |
| CCSDS 401.0-B | Radio Frequency and Modulation Systems | CCSDS |
| CCSDS 131.0-B | TM Synchronization and Channel Coding | CCSDS |
| CCSDS 132.0-B | TM Space Data Link Protocol | CCSDS |
| CCSDS 133.0-B | Encapsulation Service | CCSDS |
| ITU-R S.1003 | Environmental protection of the geostationary-satellite orbit | ITU-R |
| NASA-STD-4005 | Low Earth Orbit Spacecraft Charging Design Standard | NASA |
