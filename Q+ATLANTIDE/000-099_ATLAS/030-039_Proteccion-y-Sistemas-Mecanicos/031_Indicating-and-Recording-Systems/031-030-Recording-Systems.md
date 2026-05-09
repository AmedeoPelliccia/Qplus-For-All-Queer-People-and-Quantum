---
document_id: QATL-ATLAS-1000-ATLAS-030-039-03-031-030-RECORDING-SYSTEMS
title: "ATLAS 030-039 · 03.031.030 — Recording Systems"
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
subsection: "031"
subsection_title: "Indicating and Recording Systems"
subsubject: "030"
subsubject_title: "Recording Systems"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-AIR, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 030-039 · Section 03 · Subsection 031 · 030 — Recording Systems

## 1. Purpose

Defines Flight Data Recorder (FDR), Cockpit Voice Recorder (CVR), and Airborne Image Recorder (AIR) installation and integration, in compliance with EUROCAE ED-112A, ICAO Annex 6, and applicable TSO/ETSO.

## 2. Scope

- FDR — parameter list, sampling rates, data bus interfaces (ARINC 717/767).
- CVR — microphone placement, channel assignment, audio mixing.
- AIR (where fitted) — image sensor field-of-view, retention, and data link.
- Crash-survivability specifications (fire, impact, immersion) per ED-112A.
- Not in scope: QAR (Quick Access Recorder) ground-support infrastructure.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `030-039` |
| Section | `03` — Protección & Sistemas Mecánicos |
| Subsection | `031` — Indicating and Recording Systems |
| Subsubject | `030` — Recording Systems |
| Primary Q-Division | Q-MECHANICS[^qdiv] |
| Support Q-Divisions | Q-AIR, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/031_Indicating-and-Recording-Systems/` |
| Document | `031-030-Recording-Systems.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent section | [`../../README.md`](../../README.md) |
| Parent architecture | [`../../../README.md`](../../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../../organization/Q+ATLANTIDE.md#4-notes).
