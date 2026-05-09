---
document_id: QATL-ATLAS-1000-STA-140-149-04-140-030-NAVIGATION-SENSORS-STATE-ESTIMATION-AND-REFERENCE-FRAMES
title: "STA 140-149 · 140-030 — Navigation Sensors State Estimation and Reference Frames"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "140-149"
section: "04"
section_title: "Aviónica y Control de Misión Espacial"
subsection: "140"
subsection_title: "GNC — Guiado, Navegación y Control"
subsubject: "030"
subsubject_title: "Navigation Sensors State Estimation and Reference Frames"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HPC, Q-DATAGOV, Q-HORIZON, Q-AIR, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 140-149 · 140-030 — Navigation Sensors State Estimation and Reference Frames

## 1. Purpose

Defines the **navigation sensor suite, state estimation algorithms, and reference frame conventions** used by the GNC subsystem on Q+ATLANTIDE STA-band spacecraft.

## 2. Scope

- **Navigation sensor suite** — star trackers (attitude determination, arcsecond accuracy), fibre-optic and MEMS gyroscopes (angular rate), GPS/GNSS receivers (orbit position and velocity), LIDAR/RADAR (proximity operations ranging), accelerometers (non-gravitational force sensing); sensor redundancy and cross-check architecture.
- **State estimation** — Kalman filter (linear, applicable to near-nominal conditions), Extended Kalman Filter (EKF, nonlinear dynamics), Unscented Kalman Filter (UKF, strongly nonlinear regimes); state vector definition (position, velocity, attitude quaternion, angular rate, bias states); measurement model and process noise tuning.
- **Reference frame definitions** — Earth-Centred Inertial (ECI, J2000.0); Earth-Centred Earth-Fixed (ECEF, ITRF); spacecraft body frame; local vertical local horizontal (LVLH / Hill frame); orbit-relative rendezvous frame; sensor-fixed frames and alignment calibration.
- **Sensor data fusion** — multi-sensor fusion architecture, data-rate matching, fault detection and isolation per sensor channel, sensor handover procedures.
- **Navigation accuracy budget** — position knowledge error (PKE), velocity knowledge error (VKE), attitude knowledge error (AKE) allocations per mission phase.

## 3. Diagram — Navigation State Estimation Loop

```mermaid
flowchart TD
    A["Sensor Suite<br/>(Star Tracker · Gyro · GPS · LIDAR)"]
    A --> B["Measurement Pre-processing<br/>(data rate sync · validity check)"]
    B --> C["State Estimator<br/>(EKF / UKF)"]
    C --> D["State Vector<br/>(position · velocity · attitude · bias)"]
    D --> E["Guidance Law (002)"]
    D --> F["Control Law (004)"]
    G["Process Model<br/>(orbital dynamics · attitude kinematics)"] --> C
    style C fill:#1f3a93,color:#fff
    style D fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `140-149` |
| Section | `04` — Aviónica y Control de Misión Espacial |
| Subsection | `140` — GNC — Guiado, Navegación y Control |
| Subsubject | `003` — Navigation Sensors, State Estimation and Reference Frames |
| Primary Q-Division | Q-SPACE[^qdiv] |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Document | `140-030-Navigation-Sensors-State-Estimation-and-Reference-Frames.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`140-000-General.md`](./140-000-General.md) |

## 5. References & Citations

[^ecssest60c]: **ECSS-E-ST-60C — Control Engineering** — Navigation requirements for spacecraft GNC subsystems.

[^ccsds8710m1]: **CCSDS 871.0-M-1 — Navigation Data — Definitions and Conventions** — CCSDS standard for navigation data formats and reference frame conventions.

[^iso311]: **ISO 31-1 — Quantities and Units** — Reference standard for physical quantity definitions used in state estimation.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-60C — Control Engineering[^ecssest60c]
- CCSDS 871.0-M-1 — Navigation Data — Definitions and Conventions[^ccsds8710m1]
- ISO 31-1 — Quantities and Units[^iso311]
