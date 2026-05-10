---
document_id: QATL-ATLAS-1000-STA-130-139-03-130-050-SUN-POINTING-TRACKING-AND-ATTITUDE-CONSTRAINTS
title: "STA 130-139 · 130-050 — Sun Pointing Tracking and Attitude Constraints"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "130-139"
section: "03"
subsection: "130"
subsubject: "050"
subsubject_title: "Sun Pointing Tracking and Attitude Constraints"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · 130-050 — Sun Pointing Tracking and Attitude Constraints

## 1. Purpose

Establishes **sun-pointing, SADM tracking and attitude constraint requirements** for solar arrays on Q+ATLANTIDE STA-band platforms.

## 2. Scope

- **SADM tracking** — 1-axis rotation about yoke axis; tracking accuracy ≤ ±2° for multi-junction cells (cosine-loss ≤ 0.06%); drive rate and duty cycle allocation.
- **Solar incidence angle** — cosine factor (P = P₀·cos θ); mispointing allocation in power budget; worst-case attitude scenarios.
- **Attitude constraints** — sun-keep-in (SKI) and sun-keep-out (SKO) zones for payload/star tracker exclusion; solar array slew rate limits imposed on attitude control.
- **Sunrise/sunset transitions** — array current surges; inrush current limiting; MPPT transient management.
- **Tumbling/safe-mode** — minimum power generation in safe mode (spinning or gravity-gradient stabilised); battery discharge margins.

## 3. Diagram — Sun-Pointing and Attitude Interface

```mermaid
flowchart TD
    A["Orbital Geometry<br/>(Sun vector, β angle)"]
    A --> B["SADM Drive Rate<br/>+ Tracking Accuracy"]
    A --> C["Cosine Factor<br/>in Power Budget (→ 008)"]
    B --> D["SKI/SKO Constraints<br/>→ AOCS Allocation"]
    C --> E["Eclipse Transitions<br/>(→ 008)"]
    D --> F["Safe-Mode<br/>Minimum Power"]
    style A fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `130` — Energía Solar |
| Subsubject | `005` — Sun-Pointing, Tracking and Attitude Constraints |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |

## 5. References & Citations

[^ecssest20]: **ECSS-E-ST-20C — Electrical and Electronic**.
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards
- ECSS-E-ST-20C — Electrical and Electronic[^ecssest20]
