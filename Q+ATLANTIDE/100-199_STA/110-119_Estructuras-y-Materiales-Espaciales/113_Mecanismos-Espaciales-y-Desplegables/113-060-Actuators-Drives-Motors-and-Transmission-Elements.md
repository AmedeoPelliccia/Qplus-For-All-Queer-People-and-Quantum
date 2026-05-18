---
document_id: QATL-ATLAS-1000-STA-110-119-01-113-060-ACTUATORS-DRIVES-MOTORS-AND-TRANSMISSION-ELEMENTS
title: "STA 110-119 · 113-060 — Actuators Drives Motors and Transmission Elements"
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
subsection: "113"
subsection_title: "Mecanismos Espaciales y Desplegables"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
subsubject: "060"
subsubject_title: "Actuators Drives Motors and Transmission Elements"
---
# STA 110-119 · 113-060 — Actuators Drives Motors and Transmission Elements

## 1. Purpose

Defines the **design and verification requirements** for actuators, drive assemblies, motors, and transmission elements used in Q+ATLANTIDE space mechanisms, covering motor selection, gear train design, position-feedback architectures, and drive-train life budgets per ECSS-E-ST-33-01C[^ecsse3301] and NASA-STD-5017A[^nasastd5017].

## 2. Scope

- Covers the *Actuators, Drives, Motors and Transmission Elements* subsubject (`006`) of subsection `113`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Motor types** — brushless DC (BLDC), stepper, permanent-magnet synchronous (PMSM), and voice-coil actuators; torque-speed characteristics and derating for vacuum/temperature.
  - **Gear trains** — spur/helical gear trains, harmonic (strain-wave) drives, planetary gearboxes, and worm drives; gear ratio selection for output torque and deployment speed.
  - **Lead screws and linear actuators** — acme/ball-screw actuators, recirculating ball nuts, and linear voice-coil actuators; efficiency, backdriving prevention, and stroke limits.
  - **Position-feedback architectures** — resolvers, encoders (optical/magnetic), potentiometers, and limit switches; redundancy requirements for mechanism critical items.
  - **Drive electronics** — motor driver topology (H-bridge / 3-phase inverter), current-limiting protection, telemetry monitoring, and fault-isolation design.
  - **Transmission life budget** — gear mesh cycles, bearing revolutions, lubrication replenishment intervals, and end-of-life torque margin re-assessment.

## 3. Diagram — Actuator and Drive Train Architecture

```mermaid
flowchart TB
    CTRL["Drive Electronics<br/>(H-bridge · 3-phase inverter · CL protection)"]
    CTRL --> MTR["Motor<br/>(BLDC · stepper · PMSM · voice-coil)"]
    MTR --> GEAR["Gear Train<br/>(harmonic · planetary · spur · worm)"]
    GEAR --> OUT["Output Element<br/>(lead screw · rotary joint · linear actuator)"]
    OUT --> FB["Position Feedback<br/>(resolver · encoder · potentiometer · limit switch)"]
    FB --> CTRL
    OUT --> LBG["Life Budget<br/>(mesh cycles · bearing revolutions · lube intervals)"]
    style CTRL fill:#1f3a93,color:#fff
    style LBG fill:#2c82c9,color:#fff
```

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `113` — Mecanismos Espaciales y Desplegables |
| Subsubject | `060` — Actuators Drives Motors and Transmission Elements |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/113_Mecanismos-Espaciales-y-Desplegables/` |
| Document | `113-060-Actuators-Drives-Motors-and-Transmission-Elements.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`113-000-General.md`](./113-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `110-119` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ecsse3301]: **ECSS-E-ST-33-01C Rev.2 — Space Engineering: Mechanisms** — European standard governing design, development, qualification and acceptance of space mechanisms including release devices, hinges, latches, drives and deployable systems.

[^ecsse33]: **ECSS-E-ST-33C — Space Engineering: Mechanisms General Requirements** — European standard defining general requirements for space mechanism design, analysis, testing, and documentation.

[^nasastd5017]: **NASA-STD-5017A — Design, Development, and Test Standard for Mechanisms** — NASA standard for mechanism design, development, qualification and acceptance testing.

[^nasahdbk7005]: **NASA-HDBK-7005 — Dynamic Environmental Criteria** — NASA handbook providing dynamic environmental criteria applicable to mechanism qualification testing.

[^iso9283]: **ISO 9283:1998 — Manipulating Industrial Robots: Performance Criteria and Related Test Methods** — Applicable to robotic deployment and drive systems performance characterisation.

### Applicable industry standards

- ECSS-E-ST-33-01C Rev.2 — Space Engineering: Mechanisms[^ecsse3301]
- ECSS-E-ST-33C — Space Engineering: Mechanisms General Requirements[^ecsse33]
- NASA-STD-5017A — Design, Development, and Test Standard for Mechanisms[^nasastd5017]
- NASA-HDBK-7005 — Dynamic Environmental Criteria[^nasahdbk7005]
- ISO 9283:1998 — Manipulating Industrial Robots: Performance Criteria and Related Test Methods[^iso9283]
