---
document_id: QATL-ATLAS-1000-ATLAS-030-039-03-033-070-LIGHTING-CONTROL-DIMMING-AND-POWER-INTERFACES
title: "ATLAS 030-039 · 03.033.070 — Lighting Control, Dimming and Power Interfaces"
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
subsection: "033"
subsection_title: "Lights"
subsubject: "070"
subsubject_title: "Lighting Control, Dimming and Power Interfaces"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-AIR, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 030-039 · Section 03 · Subsection 033 · 070 — Lighting Control, Dimming and Power Interfaces

## 1. Purpose

Documents the Cabin Lighting Control System (CLCS), dimmer control units, LED driver specifications, and 28 VDC / 115 VAC power distribution to lighting zones.

## 2. Scope

- CLCS architecture: centralised controller, zone modules, and bus topology.
- Dimmer circuit types (0–10 V, DALI, PWM) and output characteristics.
- Power distribution: 28 VDC circuit breaker allocation and 115 VAC conversion.
- Crew interface: overhead panel switches, cabin management system (CMS) integration.
- Not in scope: primary AC electrical power generation (ATA 24).

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `030-039` |
| Section | `03` — Protección & Sistemas Mecánicos |
| Subsection | `033` — Lights |
| Subsubject | `070` — Lighting Control, Dimming and Power Interfaces |
| Primary Q-Division | Q-MECHANICS[^qdiv] |
| Support Q-Divisions | Q-AIR, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/033_Lights/` |
| Document | `033-070-Lighting-Control-Dimming-and-Power-Interfaces.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent section | [`../../README.md`](../../README.md) |
| Parent architecture | [`../../../README.md`](../../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../../organization/Q+ATLANTIDE.md#4-notes).
