---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-023-README
title: "ATLAS 020-029 · 02.023 — Communications (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "020-029"
section: "02"
section_title: "Sistemas Core de Aeronave"
subsection: "023"
subsection_title: "Communications"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-AIR, Q-HPC, Q-GROUND, Q-MECHANICS, Q-SPACE]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · Section 02 · Subsection 023 — Communications

## 1. Purpose

Subsection-level index for *Communications* (`023`) within ATLAS `020-029` — *Sistemas Core de Aeronave* — ATA 23.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Populates the ATA SNS-aligned section namespace `023-000`–`023-090` of subsection `023` *Communications* (ATA 23) — speech communications, data communications, passenger address, interphone, audio integration, static discharge, cabin monitoring, SATCOM/ACARS/CPDLC datalink, and S1000D traceability.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Sections `023-000` through `023-060` map directly to ATA 23-00-00 through 23-60-00. Sections `023-070` through `023-090` are programme-controlled extensions.
- Section naming pattern: `023-XXX-Title.md` where `XXX` is the three-digit local section code aligned to the ATA SNS (e.g., `023-010` → ATA `23-10-00`).

## 3. Section Index

| Section | ATA SNS | Title | Document | Status |
|---:|---|---|---|---|
| 023-000 | 23-00-00 | General | [`023-000-General.md`](./023-000-General.md) | active |
| 023-010 | 23-10-00 | Speech Communications | [`023-010-Speech-Communications.md`](./023-010-Speech-Communications.md) | active |
| 023-020 | 23-20-00 | Data Communications and Automatic Calling | [`023-020-Data-Communications-and-Automatic-Calling.md`](./023-020-Data-Communications-and-Automatic-Calling.md) | active |
| 023-030 | 23-30-00 | Passenger Address and Cabin Communications | [`023-030-Passenger-Address-and-Cabin-Communications.md`](./023-030-Passenger-Address-and-Cabin-Communications.md) | active |
| 023-040 | 23-40-00 | Interphone and Crew Communications | [`023-040-Interphone-and-Crew-Communications.md`](./023-040-Interphone-and-Crew-Communications.md) | active |
| 023-050 | 23-50-00 | Audio Integrating System | [`023-050-Audio-Integrating-System.md`](./023-050-Audio-Integrating-System.md) | active |
| 023-060 | 23-60-00 | Static Discharging and EMI Interfaces | [`023-060-Static-Discharging-and-EMI-Interfaces.md`](./023-060-Static-Discharging-and-EMI-Interfaces.md) | active |
| 023-070 | 23-70-00 | Audio-Video and Cabin Monitoring Interfaces | [`023-070-Audio-Video-and-Cabin-Monitoring-Interfaces.md`](./023-070-Audio-Video-and-Cabin-Monitoring-Interfaces.md) | programme-controlled-extension |
| 023-080 | 23-80-00 | SATCOM, ACARS, CPDLC and Datalink Interfaces | [`023-080-SATCOM-ACARS-CPDLC-and-Datalink-Interfaces.md`](./023-080-SATCOM-ACARS-CPDLC-and-Datalink-Interfaces.md) | programme-controlled-datalink-extension |
| 023-090 | 23-90-00 | S1000D CSDB Mapping and Traceability | [`023-090-S1000D-CSDB-Mapping-and-Traceability.md`](./023-090-S1000D-CSDB-Mapping-and-Traceability.md) | programme-controlled-publication-and-traceability-extension |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `023` — Communications |
| Subsubject namespace | `023-000`–`023-090` (10 sections active) |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-AIR, Q-HPC, Q-GROUND, Q-MECHANICS, Q-SPACE |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/023_Communications/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All sections under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-DATAGOV` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `023-000`–`023-090` shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
