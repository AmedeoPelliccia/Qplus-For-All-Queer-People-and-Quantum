---
document_id: QATL-ATLAS-1000-STA-100-109-00-104-README
title: "STA 100-109 · 00.104 — Gestión Térmica y Control Ambiental (Subsection Index)"
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
subsection: "104"
subsection_title: "Gestión Térmica y Control Ambiental"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "101_Habitabilidad"
  - "102_Soporte-Vital-ECLSS"
  - "103_Seguridad-de-Mision"
  - "105_Presurizacion-y-Atmosfera-Interna"
safety_boundary: "thermal control critical; failure may result in equipment damage or crew safety risk"
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · Section 00 · Subsection 104 — Gestión Térmica y Control Ambiental

## 1. Purpose

Subsection-level index for *Gestión Térmica y Control Ambiental* (`104`) within STA `100-109` — *Sistemas Generales y Soporte Vital Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It governs all thermal control design, analysis, and verification activities for crewed and uncrewed spacecraft within the Q+ATLANTIDE programme.

## 2. Scope

- Covers the subsubject namespace `000`–`090` (10 active) of subsection `104` *Thermal Control and Environmental Management*; higher codes reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- This subsection is designated **thermal control critical**; all subsubjects require thermal analysis verification, redundancy for active components, failure-mode assessment, and mission-risk governance aligned with ECSS-E-ST-31C[^ecsse31].

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`104-000-General.md`](./104-000-General.md) | active |
| 010 | Thermal Control Controlled Definition | [`104-010-Thermal-Control-Controlled-Definition.md`](./104-010-Thermal-Control-Controlled-Definition.md) | active |
| 020 | External Thermal Environment and Solar Flux | [`104-020-External-Thermal-Environment-and-Solar-Flux.md`](./104-020-External-Thermal-Environment-and-Solar-Flux.md) | active |
| 030 | Passive Thermal Control MLI and Surface Coatings | [`104-030-Passive-Thermal-Control-MLI-and-Surface-Coatings.md`](./104-030-Passive-Thermal-Control-MLI-and-Surface-Coatings.md) | active |
| 040 | Active Thermal Control ATCS Loops | [`104-040-Active-Thermal-Control-ATCS-Loops.md`](./104-040-Active-Thermal-Control-ATCS-Loops.md) | active |
| 050 | Heat Rejection Radiators and Heat Pipes | [`104-050-Heat-Rejection-Radiators-and-Heat-Pipes.md`](./104-050-Heat-Rejection-Radiators-and-Heat-Pipes.md) | active |
| 060 | Cabin HVAC and Temperature Distribution | [`104-060-Cabin-HVAC-and-Temperature-Distribution.md`](./104-060-Cabin-HVAC-and-Temperature-Distribution.md) | active |
| 070 | Electronics Thermal Dissipation and Cold Plates | [`104-070-Electronics-Thermal-Dissipation-and-Cold-Plates.md`](./104-070-Electronics-Thermal-Dissipation-and-Cold-Plates.md) | active |
| 080 | Cryogenic and Low Temperature Thermal Management | [`104-080-Cryogenic-and-Low-Temperature-Thermal-Management.md`](./104-080-Cryogenic-and-Low-Temperature-Thermal-Management.md) | active |
| 090 | Thermal Monitoring Alarms and CSDB Traceability | [`104-090-Thermal-Monitoring-Alarms-and-CSDB-Traceability.md`](./104-090-Thermal-Monitoring-Alarms-and-CSDB-Traceability.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `104` — Gestión Térmica y Control Ambiental |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/104_Gestion-Termica-y-Control-Ambiental/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE` and `governance_class = baseline` from the parent STA section. This subsection is designated **thermal control critical**; all subsubjects require thermal analysis, active-component redundancy, FMEA coverage, and mission-risk governance. Extensions added under higher codes shall preserve those header fields, carry the `safety_boundary` declaration, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ecsse31]: **ECSS-E-ST-31C — Space Engineering: Thermal Control** — European standard for spacecraft thermal control design, analysis, and verification.

[^n001]: **Note N-001** — Q+ATLANTIDE is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
