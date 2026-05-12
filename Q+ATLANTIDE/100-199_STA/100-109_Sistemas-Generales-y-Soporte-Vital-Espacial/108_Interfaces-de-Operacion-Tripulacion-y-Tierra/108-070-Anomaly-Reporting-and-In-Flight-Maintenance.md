---
document_id: QATL-ATLAS-1000-STA-100-109-00-108-070-ANOMALY-REPORTING-AND-IN-FLIGHT-MAINTENANCE
title: "STA 100-109 · 108-070 — Anomaly-Reporting-and-In-Flight-Maintenance"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "100-109"
section: "00"
section_title: "Sistemas Generales y Soporte Vital Espacial"
subsection: "108"
subsection_title: "Interfaces de Operación Tripulación y Tierra"
subsubject: "070"
subsubject_title: "Anomaly-Reporting-and-In-Flight-Maintenance"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 108-070 — Anomaly-Reporting-and-In-Flight-Maintenance

## 1. Purpose

Defines the **anomaly reporting and in-flight maintenance** architecture for Q+ATLANTIDE missions, specifying the on-board discrepancy reporting system, fault isolation, repair procedures, and evidence collection per MIL-STD-1472G[^milstd1472].

Anomaly reporting: crew initiates anomaly report (HANA) via dedicated MFD interface; report includes: system ID, observation time, description, severity classification (1=safety risk, 2=mission risk, 3=operational impact), initial crew assessment, and supporting telemetry snapshot. Anomaly database: stored in encrypted CSDB data module with automatic telemetry correlation; downlinked to MCC for ground analysis within next communication window. In-flight maintenance: on-board maintenance procedures (ORU — orbital replacement unit concept) for all field-replaceable components; tool kit for minor maintenance; maintenance access panels per ergonomic requirements (≤ 111 N removal force; ≤ 23 N routine force); maintenance log entries in CSDB.

## 2. Scope

- Covers the *Anomaly-Reporting-and-In-Flight-Maintenance* subsubject (`070`) of subsection `108`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All HMI designs require human factors evaluation per MIL-STD-1472G[^milstd1472] and NASA-STD-3001 Vol.2[^nastd3001v2].

## 3. Diagram — Anomaly-Reporting-and-In-Flight-Maintenance

```mermaid
flowchart TB
    CREW_OBS["Crew Observation<br/>(anomaly detected)"]
    CREW_OBS --> HANA["HANA Report<br/>(system · time · severity 1–3)"]
    HANA --> TM_SNAP["Telemetry Snapshot<br/>(automated correlation)"]
    HANA & TM_SNAP --> CSDB_AN["CSDB Anomaly DM<br/>(encrypted · stored)"]
    CSDB_AN --> DOWNLINK["MCC Downlink<br/>(next comm window)"]
    CSDB_AN --> MX_PROC["Maintenance Procedure<br/>(ORU · CSDB S1000D)"]
    MX_PROC --> MX_LOG["Maintenance Log<br/>(CSDB evidence)"]
    style CSDB_AN fill:#2c82c9,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `108` — Interfaces de Operación Tripulación y Tierra |
| Subsubject | `070` — Anomaly-Reporting-and-In-Flight-Maintenance |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/108_Interfaces-de-Operacion-Tripulacion-y-Tierra/` |
| Document | `108-070-Anomaly-Reporting-and-In-Flight-Maintenance.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`108-000-General.md`](./108-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management.

[^ecsse1011]: **ECSS-E-ST-10-11C — Spacecraft Environment Interaction** — Applied here for operations interface monitoring standards.

[^nastd3001v2]: **NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health** — Display, control, and HMI design requirements for crewed spacecraft operations.

[^milstd1472]: **MIL-STD-1472G — Human Engineering** — Anthropometric, display, control-force, and cognitive load requirements.

[^ccsds]: **CCSDS 401.0-B — Radio Frequency and Modulation Systems; CCSDS 131.0-B — TM Synchronization and Channel Coding** — Uplink/downlink communications standards.

### Applicable industry standards

- ECSS-E-ST-10-11C — Spacecraft Environment Interaction[^ecsse1011]
- NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health[^nastd3001v2]
- MIL-STD-1472G — Human Engineering[^milstd1472]
- CCSDS — Radio Frequency and Modulation Systems[^ccsds]
