---
document_id: QATL-ATLAS-1000-STA-100-109-00-108-010-OPERATIONS-INTERFACES-CONTROLLED-DEFINITION
title: "STA 100-109 · 108-010 — Operations-Interfaces-Controlled-Definition"
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
subsubject: "010"
subsubject_title: "Operations-Interfaces-Controlled-Definition"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 108-010 — Operations-Interfaces-Controlled-Definition

## 1. Purpose

Establishes the **controlled normative definition** of the Operations Interfaces subsystem, fixing controlled vocabulary, scope boundaries, and authority hierarchy per MIL-STD-1472G[^milstd1472] and NASA-STD-3001 Vol.2[^nastd3001v2].

Controlled terms: **HMI** (Human-Machine Interface); **CDU** (Control Display Unit); **MFD** (Multi-Function Display); **CWS** (Caution and Warning System); **MON** (Mission Operations Network); **Uplink** (ground-to-spacecraft command path); **Downlink** (spacecraft-to-ground telemetry path); **HANA** (Hardcopy Anomaly and Non-Conformance Analysis); **GPC** (General Purpose Computer). Authority hierarchy: ground override capability is retained for safety-critical systems; crew has local authority for habitability and non-safety systems; crew autonomy level increases with communication delay per the Automation and Crew Autonomy Framework.

## 2. Scope

- Covers the *Operations-Interfaces-Controlled-Definition* subsubject (`010`) of subsection `108`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All HMI designs require human factors evaluation per MIL-STD-1472G[^milstd1472] and NASA-STD-3001 Vol.2[^nastd3001v2].

## 3. Diagram — Operations-Interfaces-Controlled-Definition

```mermaid
flowchart TB
    subgraph AUTH["Authority Hierarchy"]
        GROUND["Ground Override<br/>(safety-critical)"]
        CREW_AUTH["Crew Authority<br/>(local · habitability)"]
        AUTO_AUTH["Autonomous Ops<br/>(comm delay > threshold)"]
    end
    COMM_DELAY["Communication Delay<br/>(0 s → 40 min one-way)"] --> AUTO_AUTH
    style AUTH fill:#eaf3fb,stroke:#2c82c9
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `108` — Interfaces de Operación Tripulación y Tierra |
| Subsubject | `010` — Operations-Interfaces-Controlled-Definition |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/108_Interfaces-de-Operacion-Tripulacion-y-Tierra/` |
| Document | `108-010-Operations-Interfaces-Controlled-Definition.md` (this file) |
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
