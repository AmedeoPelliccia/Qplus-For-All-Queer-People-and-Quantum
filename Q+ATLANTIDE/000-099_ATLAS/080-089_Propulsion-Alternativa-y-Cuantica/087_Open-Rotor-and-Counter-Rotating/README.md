---
document_id: QATL-ATLAS-1000-ATLAS-080-089-08-087-README
title: "ATLAS 080-089 · 08.087 — Open Rotor and Counter-Rotating (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "080-089"
section: "08"
section_title: "Propulsión Alternativa & Cuántica"
subsection: "087"
subsection_title: "Open Rotor and Counter-Rotating"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HORIZON, Q-HPC, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG, ORB-FIN]
governance_class: baseline
version: 1.1.0
status: active
language: en
standard_scope: agnostic
programme_specific: false
---

# ATLAS 080-089 · Section 08 · Subsection 087 — Open Rotor and Counter-Rotating

## 1. Purpose

Subsection-level index for *Open Rotor and Counter-Rotating* (`087`) within ATLAS `080-089` — *Propulsión Alternativa & Cuántica*.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Documents the **ORCR (Open Rotor and Counter-Rotating)** propulsor subsystem for the programme-defined aircraft type, covering the contra-rotating unducted fan (CRUF) configuration with 12-blade Forward Rotor (FR), 10-blade Aft Rotor (AR), Differential Planetary Gearbox (DPGB), and Open-Rotor Supervisory Control Unit (ORSCU DAL B).
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- All ten subsubject documents (`00`–`90`) are now populated and active.

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 00 | Open Rotor and Counter-Rotating — General | [087-000-Open-Rotor-and-Counter-Rotating-General.md](087-000-Open-Rotor-and-Counter-Rotating-General.md) | active |
| 10 | Open Rotor Baseline and Scope | [087-010-Open-Rotor-Baseline-and-Scope.md](087-010-Open-Rotor-Baseline-and-Scope.md) | active |
| 20 | Counter-Rotating Propulsor Architecture | [087-020-Counter-Rotating-Propulsor-Architecture.md](087-020-Counter-Rotating-Propulsor-Architecture.md) | active |
| 30 | Rotor Blade Design and Aeroacoustics | [087-030-Rotor-Blade-Design-and-Aeroacoustics.md](087-030-Rotor-Blade-Design-and-Aeroacoustics.md) | active |
| 40 | Gearbox Drive and Torque-Transfer Interfaces | [087-040-Gearbox-Drive-and-Torque-Transfer-Interfaces.md](087-040-Gearbox-Drive-and-Torque-Transfer-Interfaces.md) | active |
| 50 | Propulsor Airframe Integration and Clearance Zones | [087-050-Propulsor-Airframe-Integration-and-Clearance-Zones.md](087-050-Propulsor-Airframe-Integration-and-Clearance-Zones.md) | active |
| 60 | Noise, Vibration and Cabin Comfort Constraints | [087-060-Noise-Vibration-and-Cabin-Comfort-Constraints.md](087-060-Noise-Vibration-and-Cabin-Comfort-Constraints.md) | active |
| 70 | Safety, Containment and Blade-Off Risk Management | [087-070-Safety-Containment-and-Blade-Off-Risk-Management.md](087-070-Safety-Containment-and-Blade-Off-Risk-Management.md) | active |
| 80 | Open Rotor Monitoring, Diagnostics and Control Interfaces | [087-080-Open-Rotor-Monitoring-Diagnostics-and-Control-Interfaces.md](087-080-Open-Rotor-Monitoring-Diagnostics-and-Control-Interfaces.md) | active |
| 90 | S1000D CSDB Mapping and Traceability | [087-090-S1000D-CSDB-Mapping-and-Traceability.md](087-090-S1000D-CSDB-Mapping-and-Traceability.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `080-089` |
| Section | `08` — Propulsión Alternativa & Cuántica |
| Subsection | `087` — Open Rotor and Counter-Rotating |
| Subsubject namespace | `00`–`99` (active — 10 documents) |
| Primary Q-Division | Q-GREENTECH[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-HPC, Q-STRUCTURES |
| ORB support | ORB-PMO, ORB-LEG, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/080-089_Propulsion-Alternativa-y-Cuantica/087_Open-Rotor-and-Counter-Rotating/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |
| DMRL | BREX-087-v1; 30 Data Modules |
| S1000D SNS pattern | `087-{NNN}-00` |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-GREENTECH` and `governance_class = baseline` from the parent ATLAS section.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
