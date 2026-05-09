---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-021-README
title: "ATLAS 020-029 · 02.021 — Air Conditioning and Pressurization (Subsection Index)"
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
subsection: "021"
subsection_title: "Air Conditioning and Pressurization"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · Section 02 · Subsection 021 — Air Conditioning and Pressurization

## 1. Purpose

Subsection-level index for *Air Conditioning and Pressurization* (`021`) within ATLAS `020-029` — *Sistemas Core de Aeronave* — ATA 21.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Populates the ATA SNS-aligned section namespace `021-000`–`021-090` of subsection `021` *Air Conditioning and Pressurization* (ATA 21) — the Environmental Control System (ECS) functions for the aircraft.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Sections `021-000` through `021-070` map directly to ATA 21-00-00 through 21-70-00. Sections `021-080` and `021-090` are programme-controlled extensions covering ECS monitoring/diagnostics and S1000D/CSDB traceability respectively.
- Section naming pattern: `021-XXX-Title.md` where `XXX` is the three-digit local section code aligned to the ATA SNS (e.g., `021-010` → ATA `21-10-00`).

## 3. Section Index

| Section | ATA SNS | Title | Document | Status |
|---:|---|---|---|---|
| 021-000 | 21-00-00 | General | [`021-000-General.md`](./021-000-General.md) | active |
| 021-010 | 21-10-00 | Compression | [`021-010-Compression.md`](./021-010-Compression.md) | active |
| 021-020 | 21-20-00 | Distribution | [`021-020-Distribution.md`](./021-020-Distribution.md) | active |
| 021-030 | 21-30-00 | Pressurization Control | [`021-030-Pressurization-Control.md`](./021-030-Pressurization-Control.md) | active |
| 021-040 | 21-40-00 | Heating | [`021-040-Heating.md`](./021-040-Heating.md) | active |
| 021-050 | 21-50-00 | Cooling | [`021-050-Cooling.md`](./021-050-Cooling.md) | active |
| 021-060 | 21-60-00 | Temperature Control | [`021-060-Temperature-Control.md`](./021-060-Temperature-Control.md) | active |
| 021-070 | 21-70-00 | Moisture and Air Contaminant Control | [`021-070-Moisture-and-Air-Contaminant-Control.md`](./021-070-Moisture-and-Air-Contaminant-Control.md) | active |
| 021-080 | 21-80-00 | ECS Monitoring, Diagnostics and Control Interfaces | [`021-080-ECS-Monitoring-Diagnostics-and-Control-Interfaces.md`](./021-080-ECS-Monitoring-Diagnostics-and-Control-Interfaces.md) | programme-controlled-extension |
| 021-090 | 21-90-00 | S1000D CSDB Mapping and Traceability | [`021-090-S1000D-CSDB-Mapping-and-Traceability.md`](./021-090-S1000D-CSDB-Mapping-and-Traceability.md) | programme-controlled-publication-and-traceability-extension |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `021` — Air Conditioning and Pressurization |
| Subsubject namespace | `021-000`–`021-090` (10 sections: 021-000–021-090 active) |
| Primary Q-Division | Q-AIR[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/021_Air-Conditioning-and-Pressurization/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All sections under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-AIR` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `021-000`–`021-090` shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
