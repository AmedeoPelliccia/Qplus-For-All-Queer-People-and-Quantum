---
document_id: QATL-ATLAS-1000-ATLAS-030-039-03-034-070-WEATHER-RADAR-AND-NAVIGATION-SENSOR-FUSION
title: "ATLAS 030-039 · 03.034.070 — Weather Radar and Navigation Sensor Fusion"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../../README.md
parent_section_doc: ../../README.md
parent_subsection_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "030-039"
section: "03"
section_title: "Protección & Sistemas Mecánicos"
subsection: "034"
subsection_title: "Navigation"
subsubject: "070"
subsubject_title: "Weather Radar and Navigation Sensor Fusion"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-AIR, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 030-039 · Section 03 · Subsection 034 · 070 — Weather Radar and Navigation Sensor Fusion

## 1. Purpose

Documents airborne weather radar (predictive windshear, turbulence, precipitation), radar altimeter, multi-sensor navigation fusion (IRS+GPS+VOR+DME), and FMS position selection logic.

## 2. Scope

- Weather radar antenna, transceiver, scan patterns, and tilt control.
- Predictive Windshear System (PWS) detection and alert criteria.
- Radar altimeter (RALT) antenna installation, data bus, and alert thresholds.
- Multi-sensor navigation filter: IRS/GPS/DME-DME/VOR-DME position computation.
- FMS navigation sensor priority and integrity voting.
- Not in scope: weather display on ND/MFD (ATA 31) or pilot advisory for turbulence avoidance (procedure).

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `030-039` |
| Section | `03` — Protección & Sistemas Mecánicos |
| Subsection | `034` — Navigation |
| Subsubject | `070` — Weather Radar and Navigation Sensor Fusion |
| Primary Q-Division | Q-MECHANICS[^qdiv] |
| Support Q-Divisions | Q-AIR, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/034_Navigation/` |
| Document | `034-070-Weather-Radar-and-Navigation-Sensor-Fusion.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent section | [`../../README.md`](../../README.md) |
| Parent architecture | [`../../../README.md`](../../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../../organization/Q+ATLANTIDE.md#4-notes).
