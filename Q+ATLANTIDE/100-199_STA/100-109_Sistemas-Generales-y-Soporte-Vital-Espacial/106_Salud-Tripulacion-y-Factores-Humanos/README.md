---
document_id: QATL-ATLAS-1000-STA-100-109-00-106-README
title: "STA 100-109 · 00.106 — Salud Tripulación y Factores Humanos (Subsection Index)"
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
subsection: "106"
subsection_title: "Salud Tripulación y Factores Humanos"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "101_Habitabilidad"
  - "102_Soporte-Vital-ECLSS"
  - "104_Gestion-Termica-y-Control-Ambiental"
safety_boundary: "crew health critical; direct impact on mission success and crew survivability"
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · Section 00 · Subsection 106 — Salud Tripulación y Factores Humanos

## 1. Purpose

Subsection-level index for *Salud Tripulación y Factores Humanos* (`106`) within STA `100-109`. This subsection governs all crew health monitoring, medical support, radiation protection, countermeasures, human factors design, psychological support, and medical data management for Q+ATLANTIDE crewed missions[^baseline][^n001].

## 2. Scope

- Covers the subsubject namespace `000`–`090` (10 active) of subsection `106`; higher codes reserved.
- This subsection is designated **crew health critical**: degraded crew health directly impacts mission success and crew survivability on long-duration missions.
- All subsubjects inherit crew health and human factors requirements from NASA-STD-3001[^nastd3001] and the Human Integration Design Handbook[^nasahf].

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`106-000-General.md`](./106-000-General.md) | active |
| 010 | Crew Health Controlled Definition | [`106-010-Crew-Health-Controlled-Definition.md`](./106-010-Crew-Health-Controlled-Definition.md) | active |
| 020 | Medical Monitoring and Crew Status Assessment | [`106-020-Medical-Monitoring-and-Crew-Status-Assessment.md`](./106-020-Medical-Monitoring-and-Crew-Status-Assessment.md) | active |
| 030 | Radiation Exposure and Dosimetry | [`106-030-Radiation-Exposure-and-Dosimetry.md`](./106-030-Radiation-Exposure-and-Dosimetry.md) | active |
| 040 | Musculoskeletal Countermeasures and Exercise | [`106-040-Musculoskeletal-Countermeasures-and-Exercise.md`](./106-040-Musculoskeletal-Countermeasures-and-Exercise.md) | active |
| 050 | Nutrition Pharmacology and Metabolic Support | [`106-050-Nutrition-Pharmacology-and-Metabolic-Support.md`](./106-050-Nutrition-Pharmacology-and-Metabolic-Support.md) | active |
| 060 | Sleep Circadian Rhythms and Fatigue Management | [`106-060-Sleep-Circadian-Rhythms-and-Fatigue-Management.md`](./106-060-Sleep-Circadian-Rhythms-and-Fatigue-Management.md) | active |
| 070 | Human Factors Ergonomics and Cognitive Load | [`106-070-Human-Factors-Ergonomics-and-Cognitive-Load.md`](./106-070-Human-Factors-Ergonomics-and-Cognitive-Load.md) | active |
| 080 | Psychological Support and Crew Wellbeing | [`106-080-Psychological-Support-and-Crew-Wellbeing.md`](./106-080-Psychological-Support-and-Crew-Wellbeing.md) | active |
| 090 | Medical Data Management and CSDB Traceability | [`106-090-Medical-Data-Management-and-CSDB-Traceability.md`](./106-090-Medical-Data-Management-and-CSDB-Traceability.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `106` — Salud Tripulación y Factores Humanos |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/106_Salud-Tripulacion-y-Factores-Humanos/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. This subsection is designated **crew health critical**. All subsubjects require medical monitoring integration, countermeasure effectiveness evidence, and CSDB evidence traceability. The No-AAA Rule[^n004] applies.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).
[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).
[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).
[^gov]: **Governance class** — `baseline` denotes documents under controlled change management.
[^nastd3001]: **NASA-STD-3001 Vol.1 & Vol.2** — Human Integration Design Handbook.
[^nasahf]: **NASA/SP-2010-3407 — Human Integration Design Handbook (HIDH)** — Comprehensive human factors guidance.
[^n001]: **Note N-001** — Q+ATLANTIDE is a taxonomy and traceability ecosystem.
[^n004]: **Note N-004 (No-AAA Rule)** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
