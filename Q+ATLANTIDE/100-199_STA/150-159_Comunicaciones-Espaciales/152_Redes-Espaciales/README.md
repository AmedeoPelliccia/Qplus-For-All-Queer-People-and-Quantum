---
document_id: QATL-ATLAS-1000-STA-150-159-05-152-README
title: "STA 150-159 · 05.152 — Redes Espaciales (Subsection Index)"
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
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 150-159 · Section 05 · Subsection 152 — Redes Espaciales

## 1. Purpose

Subsection-level index for *Redes Espaciales* (`152`) within STA `150-159` — *Comunicaciones Espaciales*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Reserves the subsubject namespace `00`–`99` of subsection `152` *Space Networks*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Subsubjects `00`–`99` are reserved for future baseline extensions per the parent section's authorisation.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`152-000-General.md`](./152-000-General.md) | active |
| 010 | Space Networks Controlled Definition | [`152-010-Space-Networks-Controlled-Definition.md`](./152-010-Space-Networks-Controlled-Definition.md) | active |
| 020 | Network Architecture and Topology | [`152-020-Network-Architecture-and-Topology.md`](./152-020-Network-Architecture-and-Topology.md) | active |
| 030 | Routing Switching and Store and Forward Patterns | [`152-030-Routing-Switching-and-Store-and-Forward-Patterns.md`](./152-030-Routing-Switching-and-Store-and-Forward-Patterns.md) | active |
| 040 | Delay Tolerant Networking DTN | [`152-040-Delay-Tolerant-Networking-DTN.md`](./152-040-Delay-Tolerant-Networking-DTN.md) | active |
| 050 | Ground Space and Inter Satellite Network Interfaces | [`152-050-Ground-Space-and-Inter-Satellite-Network-Interfaces.md`](./152-050-Ground-Space-and-Inter-Satellite-Network-Interfaces.md) | active |
| 060 | Network Time Synchronization and Reference Frames | [`152-060-Network-Time-Synchronization-and-Reference-Frames.md`](./152-060-Network-Time-Synchronization-and-Reference-Frames.md) | active |
| 070 | QoS Priority and Mission Traffic Classes | [`152-070-QoS-Priority-and-Mission-Traffic-Classes.md`](./152-070-QoS-Priority-and-Mission-Traffic-Classes.md) | active |
| 080 | Cybersecurity Resilience and Fault Tolerance | [`152-080-Cybersecurity-Resilience-and-Fault-Tolerance.md`](./152-080-Cybersecurity-Resilience-and-Fault-Tolerance.md) | active |
| 090 | Traceability Evidence and Lifecycle Governance | [`152-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./152-090-Traceability-Evidence-and-Lifecycle-Governance.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `150-159` |
| Section | `05` — Comunicaciones Espaciales |
| Subsection | `152` — Redes Espaciales |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/150-159_Comunicaciones-Espaciales/152_Redes-Espaciales/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE` and `governance_class = baseline` from the parent STA section. Extensions added under `00`–`99` shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
