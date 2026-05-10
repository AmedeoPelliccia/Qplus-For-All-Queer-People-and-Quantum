---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-024-README
title: "ATLAS 020-029 · 02.024 — Electrical Power (Subsection Index)"
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
subsection: "024"
subsection_title: "Electrical Power"
ata_alignment: "ATA 24 — Electrical Power"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · Section 02 · Subsection 024 — Electrical Power

## 1. Purpose

Subsection-level index for *Electrical Power* (`024`) within ATLAS `020-029` — *Sistemas Core de Aeronave* — ATA 24.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Populates the ATA SNS-aligned section namespace `024-000`–`024-090` of subsection `024` *Electrical Power* (ATA 24) — generator drive, AC/DC generation, external power, electrical load distribution, emergency and standby power, monitoring and diagnostics, and S1000D traceability.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Sections `024-000` through `024-070` map directly to ATA 24-00-00 through 24-70-00. Sections `024-080` and `024-090` are programme-controlled extensions.
- Section naming pattern: `024-XXX-Title.md` where `XXX` is the three-digit local section code aligned to the ATA SNS (e.g., `024-010` → ATA `24-10-00`).

## 3. Section Index

| Section | ATA SNS | Title | Document | Status |
|---:|---|---|---|---|
| 024-000 | 24-00-00 | General | [`024-000-General.md`](./024-000-General.md) | active |
| 024-010 | 24-10-00 | Generator Drive | [`024-010-Generator-Drive.md`](./024-010-Generator-Drive.md) | active |
| 024-020 | 24-20-00 | AC Generation | [`024-020-AC-Generation.md`](./024-020-AC-Generation.md) | active |
| 024-030 | 24-30-00 | DC Generation | [`024-030-DC-Generation.md`](./024-030-DC-Generation.md) | active |
| 024-040 | 24-40-00 | External Power | [`024-040-External-Power.md`](./024-040-External-Power.md) | active |
| 024-050 | 24-50-00 | AC Electrical Load Distribution | [`024-050-AC-Electrical-Load-Distribution.md`](./024-050-AC-Electrical-Load-Distribution.md) | active |
| 024-060 | 24-60-00 | DC Electrical Load Distribution | [`024-060-DC-Electrical-Load-Distribution.md`](./024-060-DC-Electrical-Load-Distribution.md) | active |
| 024-070 | 24-70-00 | Emergency, Standby and Essential Power | [`024-070-Emergency-Standby-and-Essential-Power.md`](./024-070-Emergency-Standby-and-Essential-Power.md) | active |
| 024-080 | 24-80-00 | Electrical Power Monitoring, Diagnostics and Control Interfaces | [`024-080-Electrical-Power-Monitoring-Diagnostics-and-Control-Interfaces.md`](./024-080-Electrical-Power-Monitoring-Diagnostics-and-Control-Interfaces.md) | programme-controlled-diagnostics-extension |
| 024-090 | 24-90-00 | S1000D CSDB Mapping and Traceability | [`024-090-S1000D-CSDB-Mapping-and-Traceability.md`](./024-090-S1000D-CSDB-Mapping-and-Traceability.md) | programme-controlled-publication-and-traceability-extension |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `024` — Electrical Power |
| Subsubject namespace | `024-000`–`024-090` (10 sections active) |
| Primary Q-Division | Q-MECHANICS[^qdiv] |
| Support Q-Divisions | Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/024_Electrical-Power/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All sections under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-MECHANICS` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `024-000`–`024-090` shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
