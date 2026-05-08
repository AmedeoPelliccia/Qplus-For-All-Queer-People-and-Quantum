---
document_id: QATL-ATLAS-1000-STA-150-159-05-152-000-OVERVIEW
title: "STA 150-159 · 05.152.000 — Overview"
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
subsection: "152"
subsection_title: "Redes Espaciales"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 150-159 · 05.152.000 — Overview

## §1 Purpose

This document is the entry-point overview for the **Redes Espaciales** (Space Networks) subsection within the Q+ATLANTIDE Space Technology Architecture (STA), code range 150-159, section 05 — Comunicaciones Espaciales.[^baseline] It provides navigational context, scope boundaries, and a consolidated footprint table for all ten subsubjects (001–010) contained in this subsection.[^archtable]

## §2 Scope

The following ten subsubjects are defined and governed within this subsection:

| ID | File | Brief Description |
|---|---|---|
| 001 | [001_Space-Networks-Controlled-Definition.md](./001_Space-Networks-Controlled-Definition.md) | Establishes the controlled Q+ATLANTIDE definition of "space network" and its protocol-layer taxonomy. |
| 002 | [002_Network-Architecture-and-Topology.md](./002_Network-Architecture-and-Topology.md) | Defines space network topology classes and architectural patterns including bent-pipe and OBP approaches. |
| 003 | [003_Routing-Switching-and-Store-and-Forward-Patterns.md](./003_Routing-Switching-and-Store-and-Forward-Patterns.md) | Covers routing and switching strategies including IP over satellite, CGR, and store-and-forward relay. |
| 004 | [004_Delay-Tolerant-Networking-DTN.md](./004_Delay-Tolerant-Networking-DTN.md) | Defines DTN architecture based on the CCSDS Bundle Protocol, including custody transfer and convergence layers. |
| 005 | [005_Ground-Space-and-Inter-Satellite-Network-Interfaces.md](./005_Ground-Space-and-Inter-Satellite-Network-Interfaces.md) | Defines network interface types and ICD requirements for ground-space and inter-satellite links. |
| 006 | [006_Network-Time-Synchronization-and-Reference-Frames.md](./006_Network-Time-Synchronization-and-Reference-Frames.md) | Defines time synchronization architecture including OBT, SCLK/SCET mapping, and PTP distribution. |
| 007 | [007_QoS-Priority-and-Mission-Traffic-Classes.md](./007_QoS-Priority-and-Mission-Traffic-Classes.md) | Defines the QoS framework, traffic classes, and bandwidth allocation schemes for mission networks. |
| 008 | [008_Cybersecurity-Resilience-and-Fault-Tolerance.md](./008_Cybersecurity-Resilience-and-Fault-Tolerance.md) | Defines the security and resilience architecture including threat model, encryption, and failover patterns. |
| 009 | [009_CCSDS-ECSS-ITU-and-NASA-Standards-Mapping.md](./009_CCSDS-ECSS-ITU-and-NASA-Standards-Mapping.md) | Maps each space-network function to its applicable CCSDS, ECSS, ITU-R, and NASA standard. |
| 010 | [010_Traceability-Evidence-and-Lifecycle-Governance.md](./010_Traceability-Evidence-and-Lifecycle-Governance.md) | Defines evidence package requirements, traceability records, and lifecycle review gates for space networks. |

## §3 Footprint

| Attribute | Value |
|---|---|
| Architecture | Space Technology Architecture (STA) |
| Master range | 100–199 |
| Code range | 150-159 |
| Section | 05 — Comunicaciones Espaciales |
| Subsection | 152 — Redes Espaciales |
| Subsubject | 000 — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | baseline[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/150-159_Comunicaciones-Espaciales/152_Redes-Espaciales/` |
| Document | `000_Overview.md` |
| Parent subsection | [README.md](./README.md) |
| Parent architecture | [../../README.md](../../README.md) |
| Parent baseline | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

## §4 References & Citations

[^baseline]: Q+ATLANTIDE controlled baseline (v1.0.0)
[^archtable]: §3 Architecture Table (parent)
[^qdiv]: Q-Division authority
[^gov]: Governance class — baseline
[^n001]: Note N-001 (Q+ATLANTIDE is a taxonomy/traceability ecosystem)

### Applicable industry standards

| Standard | Title |
|---|---|
| ECSS-E-ST-50C | Space engineering: Communications[^ecss50] |
| CCSDS 720.1-G | Delay-Tolerant Networking Architecture[^ccsds720] |
| CCSDS 702.1-B | IP over CCSDS Space Links[^ccsds702] |
| RFC 5050 | Bundle Protocol Specification[^rfc5050] |
| RFC 5326 | Licklider Transmission Protocol (LTP)[^rfc5326] |
| ITU-R S.1003 | Environmental protection of the geostationary-satellite orbit[^itur] |

[^ecss50]: ECSS-E-ST-50C — Space engineering: Communications
[^ccsds720]: CCSDS 720.1-G — Delay-Tolerant Networking Architecture
[^ccsds702]: CCSDS 702.1-B — IP over CCSDS Space Links
[^rfc5050]: RFC 5050 — Bundle Protocol Specification
[^rfc5326]: RFC 5326 — Licklider Transmission Protocol (LTP)
[^itur]: ITU-R S.1003 — Environmental protection of the geostationary-satellite orbit
