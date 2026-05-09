---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-027-README
title: "ATLAS 020-029 · 02.027 — Flight Controls (Subsection Index)"
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
subsection: "027"
subsection_title: "Flight Controls"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · Section 02 · Subsection 027 — Flight Controls

## 1. Purpose

Subsection-level index for *Flight Controls* (`027`) within ATLAS `020-029` — *Sistemas Core de Aeronave* — ATA 27.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Covers the full section namespace `027-000`–`027-090` of subsection `027` *Flight Controls* (ATA 27), including primary flight control surfaces, actuation, fly-by-wire systems, and publication traceability.
- `primary_q_division: Q-AIR` holds system authority over all flight control sections as safety-of-flight functions. Q-MECHANICS covers structural actuation and mechanical rigging interfaces; Q-DATAGOV governs publication traceability; Q-GREENTECH covers electric actuation and energy-efficient control surface architectures; Q-HPC supports fly-by-wire computation and control law simulation; Q-INDUSTRY covers manufacturing and integration of control surface assemblies.
- Sections `027-080` (Fly-by-Wire Monitoring, Diagnostics and Control Interfaces) and `027-090` (S1000D CSDB Mapping and Traceability) are programme-controlled extensions activated under programme authority.
- Does not replace certified ATA/S1000D task-specific maintenance, troubleshooting, operational, or software assurance data modules.

## 3. Section Index

| Section | ATA SNS | Title | Status |
|---|---|---|---|
| 027-000 | 27-00-00 | General | baseline |
| 027-010 | 27-10-00 | Aileron, Elevon and Roll Control | baseline |
| 027-020 | 27-20-00 | Rudder, Yaw Control and Directional Control | baseline |
| 027-030 | 27-30-00 | Elevator, Pitch Control and Trim | baseline |
| 027-040 | 27-40-00 | Stabilizer and Pitch Trim | baseline |
| 027-050 | 27-50-00 | Flaps, High Lift and Lift Augmentation | baseline |
| 027-060 | 27-60-00 | Spoilers, Speedbrakes and Ground Spoilers | baseline |
| 027-070 | 27-70-00 | Control Actuation, Feel, Centering and Gust Lock | baseline |
| 027-080 | 27-80-00 | Fly-by-Wire Monitoring, Diagnostics and Control Interfaces | programme-controlled-diagnostics-extension |
| 027-090 | 27-90-00 | S1000D CSDB Mapping and Traceability | programme-controlled-publication-and-traceability-extension |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `027` — Flight Controls |
| Section namespace | `027-000`–`027-090` |
| Primary Q-Division | Q-AIR[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/027_Flight-Controls/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All sections under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-AIR` and `governance_class = baseline` from the parent ATLAS section. Sections `027-080` (Fly-by-Wire Monitoring, Diagnostics and Control Interfaces) and `027-090` (S1000D CSDB Mapping and Traceability) are programme-controlled extensions; activation requires programme authority and is controlled by Q-AIR. All other sections (`027-000` through `027-070`) are baseline and shall preserve those header fields and reuse the footnote set declared here.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
