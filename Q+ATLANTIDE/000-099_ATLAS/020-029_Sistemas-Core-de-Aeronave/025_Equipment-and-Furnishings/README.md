---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-025-README
title: "ATLAS 020-029 · 02.025 — Equipment and Furnishings (Subsection Index)"
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
subsection: "025"
subsection_title: "Equipment and Furnishings"
ata_alignment: "ATA 25 — Equipment / Furnishings"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · Section 02 · Subsection 025 — Equipment and Furnishings

## 1. Purpose

Subsection-level index for *Equipment and Furnishings* (`025`) within ATLAS `020-029` — *Sistemas Core de Aeronave* — ATA 25.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Populates the ATA SNS-aligned section namespace `025-000`–`025-090` of subsection `025` *Equipment and Furnishings* (ATA 25) — flight compartment, passenger compartment, buffet/galley, lavatories, cargo compartments, emergency equipment, accessory compartments, cabin equipment monitoring, and S1000D traceability.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Sections `025-000` through `025-070` map directly to ATA 25-00-00 through 25-70-00. Sections `025-080` and `025-090` are programme-controlled extensions.
- Section naming pattern: `025-XXX-Title.md` where `XXX` is the three-digit local section code aligned to the ATA SNS (e.g., `025-010` → ATA `25-10-00`).

## 3. Section Index

| Section | ATA SNS | Title | Document | Status |
|---:|---|---|---|---|
| 025-000 | 25-00-00 | General | [`025-000-General.md`](./025-000-General.md) | active |
| 025-010 | 25-10-00 | Flight Compartment | [`025-010-Flight-Compartment.md`](./025-010-Flight-Compartment.md) | active |
| 025-020 | 25-20-00 | Passenger Compartment | [`025-020-Passenger-Compartment.md`](./025-020-Passenger-Compartment.md) | active |
| 025-030 | 25-30-00 | Buffet, Galley and Service Equipment | [`025-030-Buffet-Galley-and-Service-Equipment.md`](./025-030-Buffet-Galley-and-Service-Equipment.md) | active |
| 025-040 | 25-40-00 | Lavatories | [`025-040-Lavatories.md`](./025-040-Lavatories.md) | active |
| 025-050 | 25-50-00 | Cargo Compartments | [`025-050-Cargo-Compartments.md`](./025-050-Cargo-Compartments.md) | active |
| 025-060 | 25-60-00 | Emergency Equipment | [`025-060-Emergency-Equipment.md`](./025-060-Emergency-Equipment.md) | active |
| 025-070 | 25-70-00 | Accessory Compartments and Furnishing Interfaces | [`025-070-Accessory-Compartments-and-Furnishing-Interfaces.md`](./025-070-Accessory-Compartments-and-Furnishing-Interfaces.md) | active |
| 025-080 | 25-80-00 | Cabin Equipment Monitoring, Diagnostics and Control Interfaces | [`025-080-Cabin-Equipment-Monitoring-Diagnostics-and-Control-Interfaces.md`](./025-080-Cabin-Equipment-Monitoring-Diagnostics-and-Control-Interfaces.md) | programme-controlled-extension |
| 025-090 | 25-90-00 | S1000D CSDB Mapping and Traceability | [`025-090-S1000D-CSDB-Mapping-and-Traceability.md`](./025-090-S1000D-CSDB-Mapping-and-Traceability.md) | programme-controlled-publication-and-traceability-extension |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `025` — Equipment and Furnishings |
| Subsubject namespace | `025-000`–`025-090` (10 sections active) |
| Primary Q-Division | Q-AIR[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/025_Equipment-and-Furnishings/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All sections under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-AIR` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `025-000`–`025-090` shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
