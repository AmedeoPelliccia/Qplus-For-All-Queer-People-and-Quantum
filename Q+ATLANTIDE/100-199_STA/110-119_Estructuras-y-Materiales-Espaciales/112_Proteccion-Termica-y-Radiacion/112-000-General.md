---
document_id: QATL-ATLAS-1000-STA-110-119-01-112-000-GENERAL
title: "STA 110-119 · 112-000 — General"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "110-119"
section: "01"
section_title: "Estructuras y Materiales Espaciales"
subsection: "112"
subsection_title: "Protección Térmica y Radiación"
subsubject: "000"
subsubject_title: "General"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-GREENTECH, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 110-119 · 112-000 — General

## 1. Purpose

Overview entry-point for the *Protección Térmica y Radiación* subsection within the `110-119` code range (Section `01` — *Estructuras y Materiales Espaciales*) of the **STA** architecture band.

This subsubject (`000 Overview`) introduces the STA 110-119.112 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the thermal and radiation protection framework governing controlled definitions, thermal control boundaries, passive TPS materials, active thermal control interfaces, radiation environment characterisation, shielding architectures, electronics/payload/crew protection zones, degradation and lifetime effects, and lifecycle governance for Q+ATLANTIDE space systems. This subsection is designated **thermal and radiation protection critical**.

## 2. Scope

- Covers the *Protección Térmica y Radiación* slice of the parent code range `110-119`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`001`–`010`) extend this Overview; the populated set in this baseline is `001`–`010`, indexed in [`README.md`](./README.md).
- Concepts in scope across the subsection:
  - **Thermal and Radiation Protection Controlled Definition** (`001`) — normative definition, scope, and applicability per ECSS-E-ST-31C[^ecssest31].
  - **Thermal Control Boundaries and Protection Functions** (`002`) — thermal balance, hot/cold case analysis, temperature limits.
  - **Passive Thermal Protection Materials and Coatings** (`003`) — MLI, OSR, black/white paint, foam insulation, ablatives.
  - **Active Thermal Control Interfaces** (`004`) — heaters, heat pipes, louvers, radiators, fluid loops.
  - **Radiation Environment and Exposure Regimes** (`005`) — GEO/LEO/deep-space TID, SEE, proton/electron belt fluence.
  - **Radiation Shielding Materials and Architectures** (`006`) — Al shielding, polyethylene, spot shielding, hydrogenous materials.
  - **Electronics, Payload and Crew Protection Zones** (`007`) — dose-depth curves, electronics derating, crew dose limits.
  - **Thermal Cycling, Degradation and Lifetime Effects** (`008`) — thermal fatigue, material property degradation, end-of-life margins.
  - **ECSS / NASA Thermal and Radiation Standards Mapping** (`009`) — normative standards cross-reference for all `112` subsubjects.
  - **Traceability, Evidence and Lifecycle Governance** (`010`) — compliance evidence package and lifecycle change authority.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `112` — Protección Térmica y Radiación |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-GREENTECH, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/112_Proteccion-Termica-y-Radiacion/` |
| Document | `112-000-General.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ecssest31]: **ECSS-E-ST-31C — Thermal Control** — European standard for spacecraft thermal control design, analysis, and verification requirements.

[^ecssest1004]: **ECSS-E-ST-10-04C — Space Environment** — European standard defining the natural space environment for spacecraft design.

[^nasastd5020]: **NASA-STD-5020 — Requirements for Threaded Fastening Systems in Spaceflight Hardware** — referenced here for structural thermal interface requirements.

[^nasahdbk4001]: **NASA-HDBK-4001 — Electrical Grounding Architecture for Unmanned Spacecraft** — guidance on shielding and grounding for radiation protection of electronics.

### Applicable industry standards

- ECSS-E-ST-31C — Thermal Control[^ecssest31]
- ECSS-E-ST-10-04C — Space Environment[^ecssest1004]
- NASA-STD-5020 — Requirements for Threaded Fastening Systems[^nasastd5020]
- NASA-HDBK-4001 — Electrical Grounding for Unmanned Spacecraft[^nasahdbk4001]
