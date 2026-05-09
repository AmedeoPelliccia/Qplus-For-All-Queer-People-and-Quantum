---
document_id: QATL-ATLAS-1000-ATLAS-030-039-03-034-050-TRAFFIC-SURVEILLANCE-AND-COLLISION-AVOIDANCE
title: "ATLAS 030-039 · 03.034.050 — Traffic Surveillance and Collision Avoidance"
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
subsubject: "050"
subsubject_title: "Traffic Surveillance and Collision Avoidance"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-AIR, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 030-039 · Section 03 · Subsection 034 · 050 — Traffic Surveillance and Collision Avoidance

## 1. Purpose

Documents TCAS II (v7.1) / ACAS X, ADS-B In/Out (1090 ES), ATCRBS/Mode-S transponder, and Traffic Advisory System (TAS) installations and data bus interfaces.

## 2. Scope

- Mode-S transponder: Extended Squitter (ES) 1090 MHz, ARINC 718A interface.
- ADS-B Out: DO-260B / ED-102A compliance, SIL/SDA levels, and position source requirements.
- ADS-B In: traffic display integration with ND/MFD.
- TCAS II v7.1 / ACAS Xa: hybrid surveillance, RA generation, and RA downlink.
- ARINC 429 label assignments for traffic, RA commands, and transponder status.
- Not in scope: traffic display symbology (ATA 31) or ATC voice communication (ATA 23).

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `030-039` |
| Section | `03` — Protección & Sistemas Mecánicos |
| Subsection | `034` — Navigation |
| Subsubject | `050` — Traffic Surveillance and Collision Avoidance |
| Primary Q-Division | Q-MECHANICS[^qdiv] |
| Support Q-Divisions | Q-AIR, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/034_Navigation/` |
| Document | `034-050-Traffic-Surveillance-and-Collision-Avoidance.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent section | [`../../README.md`](../../README.md) |
| Parent architecture | [`../../../README.md`](../../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../../organization/Q+ATLANTIDE.md#4-notes).
