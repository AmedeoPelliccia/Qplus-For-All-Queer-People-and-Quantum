---
document_id: QATL-ATLAS-1000-ATLAS-030-039-03-032-040-WHEELS-TIRES-AND-BRAKES
title: "ATLAS 030-039 · 03.032.040 — Wheels, Tires and Brakes"
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
subsection: "032"
subsection_title: "Landing Gear"
subsubject: "040"
subsubject_title: "Wheels, Tires and Brakes"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-AIR, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 030-039 · Section 03 · Subsection 032 · 040 — Wheels, Tires and Brakes

## 1. Purpose

Documents carbon or steel brake assemblies, anti-skid systems, wheel and tire specifications, tire pressure monitoring (TPMS), and brake temperature/fuse-plug management.

## 2. Scope

- Brake assembly type (carbon/steel), stack configuration, and wear limits.
- Anti-skid control unit (ASCU) logic: slip-ratio control, locked-wheel protection, touchdown protection.
- Brake-by-wire and normal/alternate/parking brake system.
- Tire type, ply rating, inflation pressure, and speed/load limits.
- TPMS sensor installation, data bus, and crew/maintenance alerting.
- Fuse plug design, melting threshold, and ground-cooling requirements.
- Not in scope: steering (subsubject 050) or gear position indication (subsubject 060).

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `030-039` |
| Section | `03` — Protección & Sistemas Mecánicos |
| Subsection | `032` — Landing Gear |
| Subsubject | `040` — Wheels, Tires and Brakes |
| Primary Q-Division | Q-MECHANICS[^qdiv] |
| Support Q-Divisions | Q-AIR, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/032_Landing-Gear/` |
| Document | `032-040-Wheels-Tires-and-Brakes.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent section | [`../../README.md`](../../README.md) |
| Parent architecture | [`../../../README.md`](../../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../../organization/Q+ATLANTIDE.md#4-notes).
