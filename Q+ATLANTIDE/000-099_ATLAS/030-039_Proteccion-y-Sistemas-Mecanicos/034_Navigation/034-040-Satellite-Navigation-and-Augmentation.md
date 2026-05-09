---
document_id: QATL-ATLAS-1000-ATLAS-030-039-03-034-040-SATELLITE-NAVIGATION-AND-AUGMENTATION
title: "ATLAS 030-039 · 03.034.040 — Satellite Navigation and Augmentation"
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
subsubject: "040"
subsubject_title: "Satellite Navigation and Augmentation"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-AIR, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 030-039 · Section 03 · Subsection 034 · 040 — Satellite Navigation and Augmentation

## 1. Purpose

Documents Multi-Mode Receiver (MMR) GNSS functions, SBAS (WAAS/EGNOS), GBAS, dual-constellation GPS/GALILEO positioning, and receiver autonomous integrity monitoring (RAIM).

## 2. Scope

- MMR GPS/GNSS receiver architecture, antenna placement, and RNP output quality.
- SBAS signal processing: WAAS (Americas), EGNOS (Europe), MSAS (Japan).
- GBAS Category III approach architecture and VDB data-link interface.
- RAIM / ARAIM algorithm requirements and integrity levels per ED-75D.
- ARINC 743A interface and ARINC 429 label assignments for lat/lon, altitude, integrity.
- Not in scope: FMS position computation (ATA 34 is sensor-only) or ADS-B out (ATA 34-050).

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `030-039` |
| Section | `03` — Protección & Sistemas Mecánicos |
| Subsection | `034` — Navigation |
| Subsubject | `040` — Satellite Navigation and Augmentation |
| Primary Q-Division | Q-MECHANICS[^qdiv] |
| Support Q-Divisions | Q-AIR, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/034_Navigation/` |
| Document | `034-040-Satellite-Navigation-and-Augmentation.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent section | [`../../README.md`](../../README.md) |
| Parent architecture | [`../../../README.md`](../../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../../organization/Q+ATLANTIDE.md#4-notes).
