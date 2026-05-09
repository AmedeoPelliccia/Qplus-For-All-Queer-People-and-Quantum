---
document_id: QATL-ATLAS-1000-STA-120-129-02-121-050-ELECTROMAGNETIC-PROPULSION-MPDT-AND-PULSED-PLASMA
title: "STA 120-129 · 121-050 — Electromagnetic Propulsion MPDT and Pulsed Plasma"
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
subsection: "121"
subsubject: "050"
subsubject_title: "Electromagnetic Propulsion MPDT and Pulsed Plasma"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-HPC, Q-DATAGOV, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · 121-050 — Electromagnetic Propulsion MPDT and Pulsed Plasma

## 1. Purpose

Defines **magnetoplasmadynamic (MPD) thruster and pulsed plasma thruster (PPT)** architectures, performance envelopes, and application boundaries.

## 2. Scope

- **MPD thrusters** — Lorentz force (J × B) accelerates propellant; applied-field MPD (AF-MPD) at low power, self-field MPD at high power (> 100 kW); Isp 1 000–8 000 s; thrust up to 200 N at MW power levels; propellants: Li, Ar, N₂, H₂; heritage: limited flight demonstration (Japan ETS-VI); largely TRL 4–5.
- **Pulsed plasma thrusters (PPT)** — Teflon® propellant ablated and accelerated by capacitor discharge arc; impulse bit 10–200 µNs; average thrust µN–mN; Isp 500–2 500 s; minimal power; heritage: EO-1, Zond-2; attitude control and small satellite applications.
- **Electromagnetic interactions** — EM noise from pulsed/high-current operation; EMC screening required per ECSS-E-ST-20-07C[^ecssemcc]; MPD magnetic field interaction with spacecraft magnetometers.
- **Thermal considerations** — AF-MPD cathode temperature > 3 000 K; radiative heat rejection to spacecraft thermal system; addressed in `009`.
- **Power requirements** — MPD: 10 kW–1 MW DC; PPT: 1–100 W average; capacitor bank sizing for PPT determines mass envelope.

## 3. Diagram — EM Propulsion Architecture

```mermaid
flowchart LR
    A["Power Supply<br/>(DC 10kW–1MW for MPD)"] --> B["Arc/Coil Driver"]
    B --> C["MPD Channel<br/>(J×B acceleration)"]
    D["Capacitor Bank<br/>(PPT)"] --> E["Arc Discharge<br/>(Teflon ablation)"]
    C --> F["High-Isp Thrust<br/>(MPD: kN class at MW)"]
    E --> G["µN–mN Thrust<br/>(PPT: attitude)"]
    style C fill:#1f3a93,color:#fff
    style E fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `121` — Propulsión Eléctrica |
| Subsubject | `005` — Electromagnetic Propulsion: MPDT and Pulsed Plasma |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `121-050-Electromagnetic-Propulsion-MPDT-and-Pulsed-Plasma.md` (this file) |

## 5. References & Citations

[^ecssest35]: **ECSS-E-ST-35C — Propulsion General Requirements**.

[^ecssemcc]: **ECSS-E-ST-20-07C — Electromagnetic Compatibility** — EMC requirements for space systems.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-35C — Propulsion General Requirements[^ecssest35]
- ECSS-E-ST-20-07C — Electromagnetic Compatibility[^ecssemcc]
