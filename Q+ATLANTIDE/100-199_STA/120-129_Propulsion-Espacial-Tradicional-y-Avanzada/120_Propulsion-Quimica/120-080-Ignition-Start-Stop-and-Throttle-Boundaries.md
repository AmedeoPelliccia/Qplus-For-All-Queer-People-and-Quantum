---
document_id: QATL-ATLAS-1000-STA-120-129-02-120-080-IGNITION-START-STOP-AND-THROTTLE-BOUNDARIES
title: "STA 120-129 · 120-080 — Ignition Start Stop and Throttle Boundaries"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "120-129"
section: "02"
section_title: "Propulsión Espacial Tradicional y Avanzada"
subsection: "120"
subsection_title: "Propulsión Química"
subsubject: "080"
subsubject_title: "Ignition Start Stop and Throttle Boundaries"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · 120-080 — Ignition Start Stop and Throttle Boundaries

## 1. Purpose

Defines the **ignition system types, start/stop sequence logic, restart envelope, throttle boundaries, and minimum impulse bit (MIB)** constraints for liquid, solid, and hybrid propulsion, and their interface with avionics FDIR (→ `103`).

## 2. Scope

- Ignition methods: hypergolic self-ignition (NTO/MMH — no igniter required); spark igniter (LOX/LH₂ · LOX/RP-1); augmented spark igniter (ASI); catalytic bed (hydrazine decomposition); pyrotechnic initiator (solid/hybrid).
- Start sequence: pressurisation → valve open → ignition verify → thrust-OK flag; typical start transient ≤ 1 s.
- Stop sequence: propellant valve close → pressurant isolation → purge (if applicable); minimum off-time between restarts (thermal soak-back constraint).
- Throttle boundaries: minimum throttle level (min. stable combustion) ≥ 10% thrust; maximum throttle = 100% rated thrust; throttle ramp rate (% thrust/s) per structural loads (→ `110`).
- MIB: minimum impulse bit for RCS thrusters (pulse-mode operation ≥ 0.5 N·s).

## 3. Diagram — Ignition and Start Sequence

```mermaid
sequenceDiagram
    participant OBC as OBC / FDIR
    participant PRES as Pressurisation
    participant VALVE as Propellant Valves
    participant IGN as Igniter
    participant THRUST as Thrust Monitor
    OBC->>PRES: Open pressurant valve
    PRES-->>OBC: Pressure OK
    OBC->>VALVE: Open propellant valves
    VALVE-->>IGN: Propellant flow
    IGN-->>THRUST: Ignition confirmed
    THRUST-->>OBC: Thrust-OK flag
    OBC->>VALVE: Close valves (shutdown)
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `120` — Propulsión Química |
| Subsubject | `008` — Ignition, Start-Stop and Throttle Boundaries |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `120-080-Ignition-Start-Stop-and-Throttle-Boundaries.md` (this file) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-35C — Propulsion General Requirements
- NASA-STD-8719.15 — Safety Standard for Explosives, Propellants and Pyrotechnics
