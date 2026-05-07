---
document_id: QATL-ATLAS-1000-STA-140-149-04-144-README
title: "STA 140-149 · 04.144 — Autonomía (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "140-149"
section: "04"
section_title: "Aviónica y Control de Misión Espacial"
subsection: "144"
subsection_title: "Autonomía"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "103_Seguridad-de-Mision"
  - "140_GNC-Guiado-Navegacion-y-Control"
  - "141_Avionica-Espacial"
  - "142_Software-de-Vuelo"
  - "143_Control-de-Mision"
safety_boundary: "mission-autonomy critical; requires explicit authority boundaries, deterministic supervision logic, FDIR integration, safe-mode transitions, human/ground override interfaces, AI/ML admission discipline, V&V evidence, HIL testing and lifecycle traceability"
no_aaa_rule: true
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 140-149 · Section 04 · Subsection 144 — Autonomía

## 1. Purpose

Subsection-level index for *Autonomía* (`144`) within STA `140-149` — *Aviónica y Control de Misión Espacial*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is designated **mission-autonomy critical**: all subsubjects require explicit authority boundaries, deterministic supervision logic, FDIR integration, safe-mode transitions, human/ground override interfaces, AI/ML admission discipline, V&V evidence, HIL testing, and lifecycle traceability.

## 2. Scope

- Populates the subsubject namespace `000`–`010` of subsection `144` *Autonomy*; subsubjects `011`–`099` remain reserved.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Linked nodes: `100_Arquitectura-General-Espacial`, `103_Seguridad-de-Mision`, `140_GNC-Guiado-Navegacion-y-Control`, `141_Avionica-Espacial`, `142_Software-de-Vuelo`, `143_Control-de-Mision`.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](000_Overview.md) | active |
| 001 | Autonomy Controlled Definition | [`001_Autonomy-Controlled-Definition.md`](001_Autonomy-Controlled-Definition.md) | active |
| 002 | Autonomous Modes and Authority Boundaries | [`002_Autonomous-Modes-and-Authority-Boundaries.md`](002_Autonomous-Modes-and-Authority-Boundaries.md) | active |
| 003 | Onboard Decision Logic and Supervision | [`003_Onboard-Decision-Logic-and-Supervision.md`](003_Onboard-Decision-Logic-and-Supervision.md) | active |
| 004 | FDIR Autonomy and Contingency Response | [`004_FDIR-Autonomy-and-Contingency-Response.md`](004_FDIR-Autonomy-and-Contingency-Response.md) | active |
| 005 | AI/ML Autonomy Admission and Assurance Boundaries | [`005_AI-ML-Autonomy-Admission-and-Assurance-Boundaries.md`](005_AI-ML-Autonomy-Admission-and-Assurance-Boundaries.md) | active |
| 006 | Human-in-the-Loop and Ground Override Interfaces | [`006_Human-in-the-Loop-and-Ground-Override-Interfaces.md`](006_Human-in-the-Loop-and-Ground-Override-Interfaces.md) | active |
| 007 | Safe-Mode Transition and Recovery Logic | [`007_Safe-Mode-Transition-and-Recovery-Logic.md`](007_Safe-Mode-Transition-and-Recovery-Logic.md) | active |
| 008 | Verification, Validation, Simulation and HIL Testing | [`008_Verification-Validation-Simulation-and-HIL-Testing.md`](008_Verification-Validation-Simulation-and-HIL-Testing.md) | active |
| 009 | ECSS-NASA Autonomy Standards Mapping | [`009_ECSS-NASA-Autonomy-Standards-Mapping.md`](009_ECSS-NASA-Autonomy-Standards-Mapping.md) | active |
| 010 | Traceability, Evidence and Lifecycle Governance | [`010_Traceability-Evidence-and-Lifecycle-Governance.md`](010_Traceability-Evidence-and-Lifecycle-Governance.md) | active |
| 011–099 | *(reserved)* | — | reserved |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `140-149` |
| Section | `04` — Aviónica y Control de Misión Espacial |
| Subsection | `144` — Autonomía |
| Subsubject namespace | `000`–`010` active / `011`–`099` reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Safety boundary | mission-autonomy critical |
| Folder path | `Q+ATLANTIDE/100-199_STA/140-149_Avionica-y-Control-de-Mision-Espacial/144_Autonomia/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = STA`, `primary_q_division = Q-SPACE`, `support_q_divisions = [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH]`, and `governance_class = baseline` from the parent STA section. Extensions added under `011`–`099` shall preserve those header fields, declare the `safety_boundary`, and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
