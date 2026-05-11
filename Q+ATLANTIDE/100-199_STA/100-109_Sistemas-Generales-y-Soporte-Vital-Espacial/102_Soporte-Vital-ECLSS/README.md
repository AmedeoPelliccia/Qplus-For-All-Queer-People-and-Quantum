---
document_id: QATL-ATLAS-1000-STA-100-109-00-102-README
title: "STA 100-109 · 00.102 — Soporte Vital ECLSS (Subsection Index)"
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
subsection: "102"
subsection_title: "Soporte Vital ECLSS"
acronym:
  ECLSS: "Environmental Control and Life Support System"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "101_Habitabilidad"
  - "103_Seguridad-de-Mision"
safety_boundary: "life-support critical; requires explicit assurance, redundancy, fault detection, contingency modes and mission-risk governance"
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · Section 00 · Subsection 102 — Soporte Vital ECLSS

## 1. Purpose

Subsection-level index for *Soporte Vital ECLSS* (`102`) within STA `100-109` — *Sistemas Generales y Soporte Vital Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Covers the subsubject namespace `00`–`10` (11 active) of subsection `102` *Environmental Control and Life Support System (ECLSS)*; `11`–`99` reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- This subsection is designated **life-support critical**; all subsubjects require explicit assurance, redundancy, fault detection, contingency modes, and mission-risk governance.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`102-000-General.md`](./102-000-General.md) | active |
| 010 | ECLSS Controlled Definition | [`102-010-ECLSS-Controlled-Definition.md`](./102-010-ECLSS-Controlled-Definition.md) | active |
| 020 | Atmosphere Generation and Revitalization | [`102-020-Atmosphere-Generation-and-Revitalization.md`](./102-020-Atmosphere-Generation-and-Revitalization.md) | active |
| 030 | Oxygen Supply and CO2 Removal | [`102-030-Oxygen-Supply-and-CO2-Removal.md`](./102-030-Oxygen-Supply-and-CO2-Removal.md) | active |
| 040 | Pressure Control and Cabin Atmosphere Monitoring | [`102-040-Pressure-Control-and-Cabin-Atmosphere-Monitoring.md`](./102-040-Pressure-Control-and-Cabin-Atmosphere-Monitoring.md) | active |
| 050 | Thermal Humidity and Condensate Control | [`102-050-Thermal-Humidity-and-Condensate-Control.md`](./102-050-Thermal-Humidity-and-Condensate-Control.md) | active |
| 060 | Water Recovery and Management | [`102-060-Water-Recovery-and-Management.md`](./102-060-Water-Recovery-and-Management.md) | active |
| 070 | Waste Management and Containment | [`102-070-Waste-Management-and-Containment.md`](./102-070-Waste-Management-and-Containment.md) | active |
| 080 | Emergency Life Support and Contingency Modes | [`102-080-Emergency-Life-Support-and-Contingency-Modes.md`](./102-080-Emergency-Life-Support-and-Contingency-Modes.md) | active |
| 090 | ECLSS Sensors Automation and Fault Detection | [`102-090-ECLSS-Sensors-Automation-and-Fault-Detection.md`](./102-090-ECLSS-Sensors-Automation-and-Fault-Detection.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `102` — Soporte Vital ECLSS |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/102_Soporte-Vital-ECLSS/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE` and `governance_class = baseline` from the parent STA section. This subsection is designated **life-support critical**; all subsubjects require explicit assurance, redundancy, fault detection, contingency modes and mission-risk governance. Extensions added under `11`–`99` shall preserve those header fields, carry the `safety_boundary` declaration, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
