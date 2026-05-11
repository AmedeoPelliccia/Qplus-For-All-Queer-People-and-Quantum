---
document_id: QATL-ATLAS-1000-STA-150-159-05-150-README
title: "STA 150-159 · 05.150 — SATCOM (Subsection Index)"
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
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 150-159 · Section 05 · Subsection 150 — SATCOM

## 1. Purpose

Subsection-level index for *SATCOM* (`150`) within STA `150-159` — *Comunicaciones Espaciales*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Reserves the subsubject namespace `00`–`99` of subsection `150` *SATCOM*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Subsubjects `00`–`99` are reserved for future baseline extensions per the parent section's authorisation.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`150-000-General.md`](./150-000-General.md) | active |
| 010 | SATCOM Controlled Definition | [`150-010-SATCOM-Controlled-Definition.md`](./150-010-SATCOM-Controlled-Definition.md) | active |
| 020 | Satellite Communication Architecture | [`150-020-Satellite-Communication-Architecture.md`](./150-020-Satellite-Communication-Architecture.md) | active |
| 030 | Link Budget Frequency Bands and Modulation | [`150-030-Link-Budget-Frequency-Bands-and-Modulation.md`](./150-030-Link-Budget-Frequency-Bands-and-Modulation.md) | active |
| 040 | Antennas Terminals and RF Interfaces | [`150-040-Antennas-Terminals-and-RF-Interfaces.md`](./150-040-Antennas-Terminals-and-RF-Interfaces.md) | active |
| 050 | Telecommand Telemetry and Payload Data Links | [`150-050-Telecommand-Telemetry-and-Payload-Data-Links.md`](./150-050-Telecommand-Telemetry-and-Payload-Data-Links.md) | active |
| 060 | Ground Station and Network Interfaces | [`150-060-Ground-Station-and-Network-Interfaces.md`](./150-060-Ground-Station-and-Network-Interfaces.md) | active |
| 070 | Encryption Authentication and COMSEC Boundaries | [`150-070-Encryption-Authentication-and-COMSEC-Boundaries.md`](./150-070-Encryption-Authentication-and-COMSEC-Boundaries.md) | active |
| 080 | Interference Spectrum and Regulatory Constraints | [`150-080-Interference-Spectrum-and-Regulatory-Constraints.md`](./150-080-Interference-Spectrum-and-Regulatory-Constraints.md) | active |
| 090 | Traceability Evidence and Lifecycle Governance | [`150-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./150-090-Traceability-Evidence-and-Lifecycle-Governance.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `150-159` |
| Section | `05` — Comunicaciones Espaciales |
| Subsection | `150` — SATCOM |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/150-159_Comunicaciones-Espaciales/150_SATCOM/` |
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
