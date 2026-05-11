---
document_id: QATL-ATLAS-1000-STA-150-159-05-153-000-GENERAL
title: "STA 150-159 · 153-000 — General"
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
subsection: "153"
subsection_title: "Comunicación Intersatélite"
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

# STA 150-159 · 153-000 — General

## §1 Purpose

This document is the controlled entry-point for the **Inter-Satellite Communication (ISL)** subsection within the Q+ATLANTIDE Space Technology Architecture (STA), covering code range 150-159, section 05, subsection 153.[^baseline] It provides navigational context, scope declarations, and footprint metadata for all ten subsubject files (001–010) that together constitute the ISL knowledge cluster.[^archtable] Readers should start here before consulting any individual subsubject file.

## §2 Scope

The subsection 153 covers the following ten subsubjects[^qdiv]:

| # | File | One-line description |
|---|------|----------------------|
| 010 | [153-010-Inter-Satellite-Communication-Controlled-Definition.md](./153-010-Inter-Satellite-Communication-Controlled-Definition.md) | Establishes the controlled Q+ATLANTIDE definition and taxonomy for inter-satellite links (ISL). |
| 020 | [153-020-ISL-Architecture-and-Link-Topology.md](./153-020-ISL-Architecture-and-Link-Topology.md) | Defines ISL architecture at constellation system level including topology patterns and feeder-link distinctions. |
| 030 | [153-030-RF-Optical-and-Hybrid-ISL-Classes.md](./153-030-RF-Optical-and-Hybrid-ISL-Classes.md) | Classifies ISL physical-layer technologies: RF (V/Ka-band), optical (1550/1064 nm), and hybrid variants. |
| 040 | [153-040-Crosslink-Pointing-Acquisition-and-Tracking.md](./153-040-Crosslink-Pointing-Acquisition-and-Tracking.md) | Specifies APT (Acquisition, Pointing and Tracking) requirements and control-loop architecture for ISL crosslinks. |
| 050 | [153-050-Routing-Relay-and-Mesh-Network-Patterns.md](./153-050-Routing-Relay-and-Mesh-Network-Patterns.md) | Defines constellation-level ISL routing patterns including contact-graph routing and mesh resilience policies. |
| 060 | [153-060-Time-Synchronization-and-Constellation-Coordination.md](./153-060-Time-Synchronization-and-Constellation-Coordination.md) | Specifies on-board time distribution, PTP-over-ISL, and GPS-free constellation synchronization architecture. |
| 070 | [153-070-Link-Budget-Latency-and-Data-Rate-Classes.md](./153-070-Link-Budget-Latency-and-Data-Rate-Classes.md) | Defines the ISL link-budget methodology, latency budget decomposition, and Q+ATLANTIDE data-rate class taxonomy. |
| 080 | [153-080-Security-Authentication-and-Resilience-Boundaries.md](./153-080-Security-Authentication-and-Resilience-Boundaries.md) | Defines the ISL security architecture, threat model, COMSEC boundary, and resilience policies. |
| 090 | [153-090-Traceability-Evidence-and-Lifecycle-Governance.md](./153-090-Traceability-Evidence-and-Lifecycle-Governance.md) | Maps ISL subsystem functions to applicable CCSDS, ECSS, ITU-R, and NASA standards. |
| 100 | [`153-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./153-090-Traceability-Evidence-and-Lifecycle-Governance.md) | Defines evidence-package requirements, ICD traceability, and review-gate governance across the ISL lifecycle. |

## §3 Footprint

| Field | Value |
|-------|-------|
| Architecture | Space Technology Architecture (STA) |
| Master range | 100–199 |
| Code range | 150-159 |
| Section | 05 — Comunicaciones Espaciales |
| Subsection | 153 — Comunicación Intersatélite |
| Subsubject | 000 — Overview |
| Primary Q-Division | Q-SPACE |
| Support Q-Divisions | Q-DATAGOV, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | baseline |
| Folder path | `Q+ATLANTIDE/100-199_STA/150-159_Comunicaciones-Espaciales/153_Comunicacion-Intersatelite/` |
| Document | `153-000-General.md` |
| Parent subsection | [README.md](./README.md) |
| Parent architecture | [../../README.md](../../README.md) |
| Parent baseline | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

## §4 References & Citations

[^baseline]: Q+ATLANTIDE controlled baseline (v1.0.0)
[^archtable]: §3 Architecture Table (parent)
[^qdiv]: Q-Division authority
[^gov]: Governance class — baseline
[^ecss50]: ECSS-E-ST-50C — Space engineering: Communications
[^ccsds401]: CCSDS 401.0-B — Radio Frequency and Modulation Systems
[^ccsds141]: CCSDS 141.0-B — Optical Communications
[^ccsds131]: CCSDS 131.0-B — TM Synchronization and Channel Coding
[^itur]: ITU-R F.1491 — Inter-satellite link characteristics
[^nasa4005]: NASA-STD-4005 — LEO Spacecraft Charging Design Standard
[^n001]: Note N-001 (Q+ATLANTIDE is a taxonomy/traceability ecosystem)

### Applicable industry standards

| Standard | Title | Relevance |
|----------|-------|-----------|
| ECSS-E-ST-50C | Space engineering: Communications | ISL communications framework |
| CCSDS 401.0-B | Radio Frequency and Modulation Systems | RF-ISL modulation and frequency |
| CCSDS 141.0-B | Optical Communications | Optical-ISL physical layer |
| CCSDS 131.0-B | TM Synchronization and Channel Coding | ISL channel coding |
| ITU-R F.1491 | Inter-satellite link characteristics | ISL frequency planning |
| NASA-STD-4005 | LEO Spacecraft Charging Design Standard | ISL hardware environment |
