---
document_id: QATL-ATLAS-1000-STA-100-109-00-101-README
title: "STA 100-109 · 00.101 — Habitabilidad (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "100-109"
section: "00"
section_title: "Sistemas Generales y Soporte Vital Espacial"
subsection: "101"
subsection_title: "Habitabilidad"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · Section 00 · Subsection 101 — Habitabilidad

## 1. Purpose

Subsection-level index for *Habitabilidad* (`101`) within STA `100-109` — *Sistemas Generales y Soporte Vital Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Populates the subsubject namespace `00`–`09` of subsection `101` *Habitability*; `10`–`99` remain reserved for future baseline extensions.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`101-000-General.md`](./101-000-General.md) | active |
| 010 | Habitability Controlled Definition | [`101-010-Habitability-Controlled-Definition.md`](./101-010-Habitability-Controlled-Definition.md) | active |
| 020 | Crew and Passenger Habitable Volume | [`101-020-Crew-and-Passenger-Habitable-Volume.md`](./101-020-Crew-and-Passenger-Habitable-Volume.md) | active |
| 030 | Environmental Comfort and Human Factors | [`101-030-Environmental-Comfort-and-Human-Factors.md`](./101-030-Environmental-Comfort-and-Human-Factors.md) | active |
| 040 | Radiation Shelter and Protected Zones | [`101-040-Radiation-Shelter-and-Protected-Zones.md`](./101-040-Radiation-Shelter-and-Protected-Zones.md) | active |
| 050 | Food Water Hygiene and Waste Interfaces | [`101-050-Food-Water-Hygiene-and-Waste-Interfaces.md`](./101-050-Food-Water-Hygiene-and-Waste-Interfaces.md) | active |
| 060 | Sleep Work and Private Volume Allocation | [`101-060-Sleep-Work-and-Private-Volume-Allocation.md`](./101-060-Sleep-Work-and-Private-Volume-Allocation.md) | active |
| 070 | Emergency Habitability and Safe Haven | [`101-070-Emergency-Habitability-and-Safe-Haven.md`](./101-070-Emergency-Habitability-and-Safe-Haven.md) | active |
| 080 | ECLSS Interfaces and Constraints | [`101-080-ECLSS-Interfaces-and-Constraints.md`](./101-080-ECLSS-Interfaces-and-Constraints.md) | active |
| 090 | Standards Traceability and Assurance Boundaries | [`101-090-Standards-Traceability-and-Assurance-Boundaries.md`](./101-090-Standards-Traceability-and-Assurance-Boundaries.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `101` — Habitabilidad |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/101_Habitabilidad/` |
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
