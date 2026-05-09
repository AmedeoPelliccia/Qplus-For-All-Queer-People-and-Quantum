---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-026-README
title: "ATLAS 020-029 · 02.026 — Fire Protection (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "020-029"
section: "02"
section_title: "Sistemas Core de Aeronave"
subsection: "026"
subsection_title: "Fire Protection"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · Section 02 · Subsection 026 — Fire Protection

## 1. Purpose

Subsection-level index for *Fire Protection* (`026`) within ATLAS `020-029` — *Sistemas Core de Aeronave* — ATA 26.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Defines the section namespace `026-000` through `026-090` of subsection `026` *Fire Protection*, aligned to ATA Chapter 26.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- `primary_q_division: Q-AIR` — fire protection is a safety-of-flight system authority. Q-MECHANICS covers engine/APU bay interfaces; Q-GREENTECH covers hydrogen and electric propulsion fire safety; Q-DATAGOV governs publication and CSDB traceability; Q-GROUND and Q-INDUSTRY cover airport/ground infrastructure and manufacturing interfaces.

## 3. Section Index

| Section | ATA SNS | Title | Status |
|---|---|---|---|
| 026-000 | 26-00-00 | General | baseline |
| 026-010 | 26-10-00 | Fire and Smoke Detection | baseline |
| 026-020 | 26-20-00 | Fire Extinguishing | baseline |
| 026-030 | 26-30-00 | Explosion Suppression | baseline |
| 026-040 | 26-40-00 | Engine, APU and Nacelle Fire Protection | programme-controlled-extension |
| 026-050 | 26-50-00 | Cargo and Baggage Compartment Fire Protection | baseline |
| 026-060 | 26-60-00 | Cabin, Lavatory and Equipment Bay Fire Protection | baseline |
| 026-070 | 26-70-00 | Hydrogen and Electric Propulsion Fire Safety Interfaces | programme-controlled-extension |
| 026-080 | 26-80-00 | Fire Protection Monitoring, Diagnostics and Control Interfaces | programme-controlled-diagnostics-extension |
| 026-090 | 26-90-00 | S1000D CSDB Mapping and Traceability | programme-controlled-publication-and-traceability-extension |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `026` — Fire Protection |
| Section namespace | `026-000`–`026-090` |
| Primary Q-Division | Q-AIR[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/026_Fire-Protection/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All sections under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-AIR` and `governance_class = baseline` from the parent ATLAS section. Programme-controlled extensions (`026-040`, `026-070`, `026-080`, `026-090`) require programme authority before population of detailed design data modules.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
