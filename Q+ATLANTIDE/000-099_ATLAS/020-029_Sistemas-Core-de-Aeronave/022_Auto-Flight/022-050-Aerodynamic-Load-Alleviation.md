---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-022-050-AERODYNAMIC-LOAD-ALLEVIATION
title: "ATLAS 020-029 · 02.022 — Auto Flight · 022-050 Aerodynamic Load Alleviation"
ata_chapter: "22"
ata_sns: "22-50-00"
local_section_code: "022-050"
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
subsection: "022"
subsection_title: "Auto Flight"
primary_q_division: Q-AIR
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-MECHANICS, Q-GROUND, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# ATLAS 020-029 · 02.022 — Auto Flight · 022-050 Aerodynamic Load Alleviation

## 1. Purpose

Defines the **aerodynamic load alleviation (ALA) system architecture and functional requirements** for the *Auto Flight* subsystem (ATA 22-50-00) within the Q+ATLANTIDE programme. Covers gust load alleviation (GLA) and manoeuvre load alleviation (MLA) functions that use active control surface deflections to reduce wing-bending moments and structural loads during gusts and manoeuvres, extending structural fatigue life and enabling airframe mass optimisation.

## 2. Scope

- Covers the *Aerodynamic Load Alleviation* section (`022-050`, ATA SNS 22-50-00) of subsection `022` *Auto Flight*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Gust Load Alleviation (GLA)** — accelerometer-based gust detection; aileron and spoiler deflection commands to counteract wing bending from vertical gusts; GLA gain scheduling with airspeed, altitude, and aircraft weight.
  - **Manoeuvre Load Alleviation (MLA)** — reduction of wing-root bending moment during roll manoeuvres; outboard aileron deflection combined with spoiler scheduling; integration with flight-control system (ATA 27).
  - **Sensor architecture** — accelerometer suite (centre of gravity, wing tip) used for GLA; inertial reference system (IRS) interface for roll rate and normal acceleration signals.
  - **Authority and limits** — ALA surface deflection limits; interaction with flight-control surface envelope protection; rate and position limits.
  - **Structural interface** — load-alleviation effectiveness envelope definition; fatigue life credit methodology interface with structures (ATA 51/57); interaction with flutter clearance.
  - **Failure modes** — GLA/MLA failure detection; deselection on failure; structural load monitoring without alleviation fallback.
- Out of scope: autopilot modes (022-010), flight director (022-060), aeroelastic flutter analysis (ATA 57/structures domain).

## 3. Diagram — Aerodynamic Load Alleviation Functional Architecture

Gust and manoeuvre load signals drive surface commands via the ALA law; limits and failure monitoring constrain authority; structural benefits feed fatigue credit.

```mermaid
flowchart TD
    ACC["Accelerometer Suite<br/>(CoG · wing tip<br/>normal acceleration)"]:::sensor
    IRS["IRS<br/>(roll rate · pitch rate)"]:::sensor
    ALA["ALA Control Law<br/>(GLA · MLA<br/>gain-scheduled)"]:::ctrl
    ACC & IRS --> ALA
    SCHED["Gain Scheduler<br/>(airspeed · altitude<br/>gross weight)"]:::sched
    SCHED --> ALA
    ALA --> AIL["Outboard Aileron<br/>Deflection Command"]:::act
    ALA --> SPOIL["Spoiler Deflection<br/>Command"]:::act
    AIL & SPOIL --> FCS["Flight Control System<br/>(ATA 27 — surface limits)"]:::out
    MON["Failure Monitor<br/>(ALA deselection on fault)"]:::safety
    MON --> ALA
    STRUCT["Structural Fatigue<br/>Credit Interface<br/>(ATA 51/57)"]:::trace
    FCS --> STRUCT

    classDef sensor fill:#1f3a93,stroke:#0b1d4a,color:#fff
    classDef ctrl fill:#2c82c9,stroke:#0b1d4a,color:#fff
    classDef sched fill:#eaf3fb,stroke:#2c82c9,color:#0b1d4a
    classDef act fill:#f6e6ff,stroke:#7d3c98,color:#3b1f4d
    classDef out fill:#f0f9e8,stroke:#27ae60,color:#145a32
    classDef safety fill:#c0392b,stroke:#7b241c,color:#fff
    classDef trace fill:#fff4dd,stroke:#b9770e,color:#5a3b00
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `022` — Auto Flight |
| Local section code | `022-050` — Aerodynamic Load Alleviation |
| ATA chapter | 22 |
| ATA SNS | 22-50-00 |
| Primary Q-Division | Q-AIR[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC, Q-MECHANICS, Q-GROUND, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/022_Auto-Flight/` |
| Document | `022-050-Aerodynamic-Load-Alleviation.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`022-000-General.md`](./022-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **ATLAS §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management.

[^cs25]: **EASA CS-25** — CS 25.341 (gust and turbulence loads), CS 25.349 (rolling conditions), and AMC covering active load alleviation system design and failure condition classification.

[^ata2200]: **ATA iSpec 2200** — Section 22-50 naming and data-module scope for aerodynamic load alleviation subsystems.

### Applicable standards

- EASA CS-25[^cs25]
- ATA iSpec 2200[^ata2200]
