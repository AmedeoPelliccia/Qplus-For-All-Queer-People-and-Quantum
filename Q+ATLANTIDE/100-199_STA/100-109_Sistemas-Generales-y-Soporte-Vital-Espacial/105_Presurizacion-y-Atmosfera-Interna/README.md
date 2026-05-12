---
document_id: QATL-ATLAS-1000-STA-100-109-00-105-README
title: "STA 100-109 · 00.105 — Presurización y Atmósfera Interna (Subsection Index)"
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
subsection: "105"
subsection_title: "Presurización y Atmósfera Interna"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "102_Soporte-Vital-ECLSS"
  - "103_Seguridad-de-Mision"
  - "104_Gestion-Termica-y-Control-Ambiental"
safety_boundary: "pressurization critical; failure may result in hypoxia or rapid decompression"
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · Section 00 · Subsection 105 — Presurización y Atmósfera Interna

## 1. Purpose

Subsection-level index for *Presurización y Atmósfera Interna* (`105`) within STA `100-109` — *Sistemas Generales y Soporte Vital Espacial*.

This subsection governs all pressurization system design, cabin atmosphere management, and atmospheric safety for Q+ATLANTIDE crewed modules[^baseline][^n001], under the **ATLAS-1000** register. It is designated **pressurization critical**: loss of pressurization integrity can result in rapid decompression and crew fatality within minutes.

## 2. Scope

- Covers the subsubject namespace `000`–`090` (10 active) of subsection `105`; higher codes reserved.
- All subsubjects require pressurization failure mode analysis, leak detection verification, redundant pressure control paths, and crew emergency procedure validation per ECSS-E-ST-34C[^ecsse34] and NASA-STD-3001[^nastd3001].

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`105-000-General.md`](./105-000-General.md) | active |
| 010 | Pressurization Controlled Definition | [`105-010-Pressurization-Controlled-Definition.md`](./105-010-Pressurization-Controlled-Definition.md) | active |
| 020 | Cabin Pressure Regulation and Altitude Profile | [`105-020-Cabin-Pressure-Regulation-and-Altitude-Profile.md`](./105-020-Cabin-Pressure-Regulation-and-Altitude-Profile.md) | active |
| 030 | Atmospheric Composition and Partial Pressures | [`105-030-Atmospheric-Composition-and-Partial-Pressures.md`](./105-030-Atmospheric-Composition-and-Partial-Pressures.md) | active |
| 040 | Pressurization Valves and Outflow Control | [`105-040-Pressurization-Valves-and-Outflow-Control.md`](./105-040-Pressurization-Valves-and-Outflow-Control.md) | active |
| 050 | Leak Detection and Seal Integrity | [`105-050-Leak-Detection-and-Seal-Integrity.md`](./105-050-Leak-Detection-and-Seal-Integrity.md) | active |
| 060 | Depressurization Control and Emergency Procedures | [`105-060-Depressurization-Control-and-Emergency-Procedures.md`](./105-060-Depressurization-Control-and-Emergency-Procedures.md) | active |
| 070 | Atmospheric Monitoring and Contaminant Detection | [`105-070-Atmospheric-Monitoring-and-Contaminant-Detection.md`](./105-070-Atmospheric-Monitoring-and-Contaminant-Detection.md) | active |
| 080 | Redundancy and Fail-Safe Architecture | [`105-080-Redundancy-and-Fail-Safe-Architecture.md`](./105-080-Redundancy-and-Fail-Safe-Architecture.md) | active |
| 090 | Standards Traceability and CSDB Evidence | [`105-090-Standards-Traceability-and-CSDB-Evidence.md`](./105-090-Standards-Traceability-and-CSDB-Evidence.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `105` — Presurización y Atmósfera Interna |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/105_Presurizacion-y-Atmosfera-Interna/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. This subsection is designated **pressurization critical**; all subsubjects require dual-redundant pressure control, leak detection, emergency procedures, and mission-risk governance per ECSS-E-ST-34C. The No-AAA Rule[^n004] applies.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).
[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).
[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).
[^gov]: **Governance class** — `baseline` denotes documents under controlled change management.
[^ecsse34]: **ECSS-E-ST-34C Rev.1 — Space Engineering: Environmental Control and Life Support** — Pressurization design and verification requirements.
[^nastd3001]: **NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health** — Cabin pressure and atmospheric composition crew health requirements.
[^n001]: **Note N-001** — Q+ATLANTIDE is a taxonomy and traceability ecosystem. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^n004]: **Note N-004 (No-AAA Rule)** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
