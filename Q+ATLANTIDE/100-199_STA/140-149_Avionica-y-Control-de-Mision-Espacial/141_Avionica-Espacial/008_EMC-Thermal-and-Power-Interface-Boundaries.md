---
document_id: QATL-ATLAS-1000-STA-140-149-04-141-008-EMC-THERMAL-AND-POWER-INTERFACE-BOUNDARIES
title: "STA 140-149 · 04.141.008 — EMC, Thermal and Power Interface Boundaries"
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
subsection: "141"
subsection_title: "Aviónica Espacial"
subsubject: "008"
subsubject_title: "EMC, Thermal and Power Interface Boundaries"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 140-149 · Section 04 · Subsection 141 · Subsubject 008 — EMC, Thermal and Power Interface Boundaries

## 1. Purpose

Defines the **EMC design rules, thermal dissipation boundaries, and power interface constraints** for Q+ATLANTIDE STA-band spacecraft avionics in its operational environment.

## 2. Scope

- **EMC design rules — conducted emissions** — power supply ripple and noise limits on DC bus input; inrush current limits; EMI filter requirements at avionics unit power input; conducted susceptibility limits for avionics immunity to power bus disturbances per ECSS-E-ST-20-07C[^ecssest2007c].
- **EMC design rules — radiated emissions** — avionics clock frequency harmonics management; PCB layout rules for EMC (ground planes, decoupling, signal return paths); chassis shielding effectiveness requirements; radiated emission limits for compatibility with sensitive sensors (star trackers, magnetometers).
- **EMC susceptibility** — avionics immunity to RF environment (transponder transmit power, inter-unit electromagnetic coupling); susceptibility test levels per ECSS-E-ST-20-07C; worst-case RF environment definition.
- **Thermal dissipation boundaries** — avionics unit-level power dissipation budget (W); thermal interface resistance to mounting panel; permitted component junction temperature range; thermal cycling range and number of cycles to qualification; heater power budget for cold survival case; interface with thermal subsystem (→ ECSS-E-ST-31C[^ecssest31c]).
- **Power consumption budget** — unit-level power consumption in each operational mode (peak, nominal, standby, safe mode); power consumption measurement tolerance; interface with power distribution subsystem (→ `133`); over-current protection coordination.
- **Power interface** — supply voltage range (nominal, minimum, maximum transient); input capacitance limit; hold-up time requirement; power bus isolation switch coordination; connector and harness requirements for power lines.

## 3. Diagram — EMC, Thermal and Power Interface Boundaries

```mermaid
flowchart TD
    A["Power Distribution (133)"] -->|"regulated DC bus"| B["Avionics Unit<br/>(OBC / DHU)"]
    B -->|"heat dissipation"| C["Thermal Subsystem<br/>(ECSS-E-ST-31C)"]
    B -->|"EMI filter + shielding"| D["EMC Compliance<br/>(ECSS-E-ST-20-07C)"]
    D --> E["Sensitive Sensors<br/>(star tracker · magnetometer)"]
    B -->|"power telemetry"| F["Power Monitor → 003 TM"]
    style B fill:#1f3a93,color:#fff
    style D fill:#0f4c8a,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `140-149` |
| Section | `04` — Aviónica y Control de Misión Espacial |
| Subsection | `141` — Aviónica Espacial |
| Subsubject | `008` — EMC, Thermal and Power Interface Boundaries |
| Primary Q-Division | Q-SPACE[^qdiv] |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Document | `008_EMC-Thermal-and-Power-Interface-Boundaries.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |

## 5. References & Citations

[^ecssest2007c]: **ECSS-E-ST-20-07C — Electromagnetic Compatibility** — Spacecraft EMC design requirements and test methods.

[^ecssest31c]: **ECSS-E-ST-31C — Thermal Control** — Thermal interface requirements between avionics and thermal control subsystem.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-20-07C — Electromagnetic Compatibility[^ecssest2007c]
- ECSS-E-ST-31C — Thermal Control[^ecssest31c]
