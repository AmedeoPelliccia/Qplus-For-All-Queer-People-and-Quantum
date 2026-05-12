---
document_id: QATL-ATLAS-1000-STA-100-109-00-107-README
title: "STA 100-109 · 00.107 — Supervivencia, Emergencia y Aborto (Subsection Index)"
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
subsection: "107"
subsection_title: "Supervivencia, Emergencia y Aborto"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
linked_nodes:
  - "100_Arquitectura-General-Espacial"
  - "102_Soporte-Vital-ECLSS"
  - "103_Seguridad-de-Mision"
  - "105_Presurizacion-y-Atmosfera-Interna"
safety_boundary: "emergency/abort critical; life-safety systems with highest assurance requirement"
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · Section 00 · Subsection 107 — Supervivencia, Emergencia y Aborto

## 1. Purpose

Subsection-level index for *Supervivencia, Emergencia y Aborto* (`107`) within STA `100-109`. This subsection governs abort modes, emergency egress, survival equipment, fire and toxic atmosphere response, crew rescue, and emergency communications for Q+ATLANTIDE crewed missions[^baseline][^n001].

## 2. Scope

- Covers the subsubject namespace `000`–`090` (10 active) of subsection `107`; higher codes reserved.
- This subsection is designated **emergency/abort critical** with the highest assurance requirement of any crew safety subsystem.
- All subsubjects inherit requirements from ECSS-Q-ST-40C[^ecssq40], MIL-STD-882E[^milstd882], and ISO 14620-1[^iso14620].

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | General | [`107-000-General.md`](./107-000-General.md) | active |
| 010 | Emergency Abort Controlled Definition | [`107-010-Emergency-Abort-Controlled-Definition.md`](./107-010-Emergency-Abort-Controlled-Definition.md) | active |
| 020 | Abort Modes and Abort Logic Architecture | [`107-020-Abort-Modes-and-Abort-Logic-Architecture.md`](./107-020-Abort-Modes-and-Abort-Logic-Architecture.md) | active |
| 030 | Emergency Egress and Escape | [`107-030-Emergency-Egress-and-Escape.md`](./107-030-Emergency-Egress-and-Escape.md) | active |
| 040 | Survival Equipment and Personnel Equipment | [`107-040-Survival-Equipment-and-Personnel-Equipment.md`](./107-040-Survival-Equipment-and-Personnel-Equipment.md) | active |
| 050 | Fire Detection and Suppression | [`107-050-Fire-Detection-and-Suppression.md`](./107-050-Fire-Detection-and-Suppression.md) | active |
| 060 | Toxic Atmosphere Response and NBC Protection | [`107-060-Toxic-Atmosphere-Response-and-NBC-Protection.md`](./107-060-Toxic-Atmosphere-Response-and-NBC-Protection.md) | active |
| 070 | Crew Rescue Recovery and Search-and-Rescue | [`107-070-Crew-Rescue-Recovery-and-Search-and-Rescue.md`](./107-070-Crew-Rescue-Recovery-and-Search-and-Rescue.md) | active |
| 080 | Emergency Communications and Distress Signalling | [`107-080-Emergency-Communications-and-Distress-Signalling.md`](./107-080-Emergency-Communications-and-Distress-Signalling.md) | active |
| 090 | Emergency Procedures Evidence and CSDB Traceability | [`107-090-Emergency-Procedures-Evidence-and-CSDB-Traceability.md`](./107-090-Emergency-Procedures-Evidence-and-CSDB-Traceability.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `107` — Supervivencia, Emergencia y Aborto |
| Subsubject namespace | `000`–`090` (10 active); higher reserved |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/107_Supervivencia-Emergencia-y-Aborto/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. This subsection carries the highest assurance classification in `100-109`. All subsubjects require formal hazard analysis (MIL-STD-882E SHA/SSHA[^milstd882]), failure mode analysis, and independent safety review. The No-AAA Rule[^n004] applies.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).
[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).
[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).
[^gov]: **Governance class** — `baseline` denotes documents under controlled change management.
[^ecssq40]: **ECSS-Q-ST-40C — Safety** — ESA safety standards.
[^iso14620]: **ISO 14620-1:2018 — Space Systems Safety Requirements**.
[^milstd882]: **MIL-STD-882E — System Safety** — Hazard analysis and risk acceptance.
[^n001]: **Note N-001** — Q+ATLANTIDE is a taxonomy and traceability ecosystem.
[^n004]: **Note N-004 (No-AAA Rule)** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
