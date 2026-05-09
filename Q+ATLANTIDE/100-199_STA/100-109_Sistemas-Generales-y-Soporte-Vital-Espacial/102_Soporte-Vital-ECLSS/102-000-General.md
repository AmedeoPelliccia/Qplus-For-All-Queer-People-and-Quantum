---
document_id: QATL-ATLAS-1000-STA-100-109-00-102-000-GENERAL
title: "STA 100-109 · 102-000 — General"
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
subsection: "102"
subsection_title: "Soporte Vital ECLSS"
subsubject: "000"
subsubject_title: "General"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · 102-000 — General

## 1. Purpose

Overview entry-point for the *Soporte Vital ECLSS* subsection within the `100-109` code range (Section `00` — *Sistemas Generales y Soporte Vital Espacial*) of the **STA** architecture band (*Space Technology Architecture*, master range `100–199`).

This subsubject (`000 Overview`) introduces the STA 100-109.102 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the ECLSS framework — controlled definition, atmosphere generation, oxygen/CO₂ management, pressure control, thermal/humidity control, water recovery, waste management, emergency life support, sensor/automation/fault detection, and standards traceability — governing all ECLSS design activities within the Q+ATLANTIDE crewed-space programme.

## 2. Scope

- Covers the *Soporte Vital ECLSS* slice of the parent code range `100-109`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`001`–`010`) extend this Overview; the populated set in this baseline is `001`–`010`, indexed in [`README.md`](./README.md).
- Concepts in scope across the subsection:
  - **ECLSS Controlled Definition** (`001`) — normative ECLSS definition and acronym controlled vocabulary per ECSS-E-ST-34C[^ecsse34].
  - **Atmosphere Generation and Revitalization** (`002`) — O₂ generation, CO₂ removal, and cabin air quality maintenance.
  - **Oxygen Supply and CO₂ Removal** (`003`) — on-board O₂ generation systems (OGS/SFOG) and CO₂ removal assemblies (CDRA/Sabatier).
  - **Pressure Control and Cabin Atmosphere Monitoring** (`004`) — pressure regulator design, leak detection, and sensor network.
  - **Thermal, Humidity and Condensate Control** (`005`) — ATCS temperature and humidity management, condensate collection.
  - **Water Recovery and Management** (`006`) — urine processor assembly (UPA), water recovery system (WRS), and potable water certification.
  - **Waste Management and Containment** (`007`) — faecal waste containment, trash management, and hazardous waste segregation.
  - **Emergency Life Support and Contingency Modes** (`008`) — emergency O₂ reserves, contingency atmosphere modes, and crew safe-haven support.
  - **ECLSS Sensors, Automation and Fault Detection** (`009`) — sensor network, automation logic, and FDIR interfaces.
  - **Standards Traceability and Assurance Boundaries** (`010`) — cross-map to ECSS/NASA/ISO and product-assurance evidence requirements.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `102` — Soporte Vital ECLSS |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/102_Soporte-Vital-ECLSS/` |
| Document | `102-000-General.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `100-109` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ecsse34]: **ECSS-E-ST-34C Rev.1 — Space Engineering: Environmental Control and Life Support** — European standard for ECLSS design, subsystem interfaces, and test criteria.

[^nasajsc]: **NASA/JSC-65591 — ECLSS Design and Performance Requirements** — NASA design specification for ISS-class ECLSS subsystems, used as the baseline engineering reference.

[^nastd3001v2]: **NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health** — Atmosphere and water quality requirements that ECLSS must satisfy.

[^iso14644]: **ISO 14644-1:2015 — Cleanrooms and Associated Controlled Environments** — Applied to atmosphere quality monitoring and contamination control requirements.

[^nasacp]: **NASA/CP-2008-214304 — ECLSS Development and Testing** — ECLSS hardware development and qualification test reference covering all subsystems.

### Applicable industry standards

- ECSS-E-ST-34C Rev.1 — Space Engineering: Environmental Control and Life Support[^ecsse34]
- NASA/JSC-65591 — ECLSS Design and Performance Requirements[^nasajsc]
- NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health[^nastd3001v2]
- ISO 14644-1:2015 — Cleanrooms and Associated Controlled Environments[^iso14644]
- NASA/CP-2008-214304 — ECLSS Development and Testing[^nasacp]
