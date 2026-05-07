---
document_id: QATL-ATLAS-1000-STA-130-139-03-133-008-REDUNDANCY-CROSS-STRAPPING-AND-SAFE-MODES
title: "STA 130-139 · 03.133.008 — Redundancy, Cross-Strapping and Safe Modes"
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
subsection: "133"
subsubject: "008"
subsubject_title: "Redundancy, Cross-Strapping and Safe Modes"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-DATAGOV, Q-HPC, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · Section 03 · Subsection 133 · Subsubject 008 — Redundancy, Cross-Strapping and Safe Modes

## 1. Purpose

Establishes **redundancy, bus cross-strapping, and safe-mode power architecture** for Q+ATLANTIDE STA-band platforms.

## 2. Scope

- **Dual-bus architecture** — Bus A and Bus B; fully independent in normal ops; cross-strap relays allow either bus to power safety-critical loads.
- **Cross-strapping logic** — automatic cross-strap on Bus A undervoltage (V < 85%) or commanded; cross-strap not latching; reverts on bus recovery.
- **Safe-mode minimum set** — defined set of loads powered on Bus A or B regardless of fault; includes OBDH, attitude sensors, basic telecommand receiver, heaters, minimal EPS monitoring.
- **Battery autonomy** — safe-mode minimum set must be sustained by battery alone for ≥ 72 h (crewed platform) / ≥ 24 h (robotic) from worst-case eclipse DOD.
- **Failure mode analysis** — FMEA/FMECA for all distribution units; single-point failures that could lead to mission loss or safety event shall be eliminated.

## 3. Diagram — Redundancy, Cross-Strapping and Safe Modes

```mermaid
flowchart TD
    A["Power Source Input\n(→ 130 / 131 / 132)"] --> B["Redundancy, Cross-Strapping and Safe Modes\n(STA-133-008)"]
    B --> C["Load Interfaces\n(→ 121 / 100 / Payload)"]
    B --> D["Fault Isolation\n(→ 005)"]
    style A fill:#1f3a93,color:#fff
    style C fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `133` — Distribución Eléctrica |
| Subsubject | `008` — Redundancy, Cross-Strapping and Safe Modes |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |

## 5. References & Citations

[^ecssest20]: **ECSS-E-ST-20C — Electrical and Electronic**.
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards
- ECSS-E-ST-20C — Electrical and Electronic; ECSS-Q-ST-30-02C — FMEA/FMECA
