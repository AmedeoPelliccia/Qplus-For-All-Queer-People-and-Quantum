---
document_id: QATL-ATLAS-1000-STA-130-139-03-133-002-POWER-ARCHITECTURE-AND-BUS-TOPOLOGY
title: "STA 130-139 · 03.133.002 — Power Architecture and Bus Topology"
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
subsubject: "002"
subsubject_title: "Power Architecture and Bus Topology"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-DATAGOV, Q-HPC, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · Section 03 · Subsection 133 · Subsubject 002 — Power Architecture and Bus Topology

## 1. Purpose

Defines **power bus architecture and topology options** for Q+ATLANTIDE STA-band platforms.

## 2. Scope

- **Regulated bus** — constant voltage (28 V ± 2%, 50 V ± 2%, 100 V ± 2%); S3R or MPPT-based regulation; low-noise; preferred for sensitive payloads.
- **Unregulated bus** — battery-dominated bus; voltage varies with battery SOC (typically 24–34 V for Li-ion 28 V nominal); lower mass; used on heritage small-sat.
- **Dual bus architecture** — redundant A/B buses with cross-strapping relays; essential bus + non-essential bus; shedding hierarchy in safe-mode.
- **Voltage standards** — 28 V (small/medium platforms), 50 V (medium/large), 100 V (large LEO), 120/160 V (ISS-class/HEO large).
- **Bus capacitor sizing** — holdup time during bus fault < 1 ms; inrush limiting for capacitive loads.

## 3. Diagram — Power Architecture and Bus Topology

```mermaid
flowchart TD
    A["Power Source Input\n(→ 130 / 131 / 132)"] --> B["Power Architecture and Bus Topology\n(STA-133-002)"]
    B --> C["Load Interfaces\n(→ 121 / 100 / Payload)"]
    B --> D["Fault Isolation\n(→ 005)"]
    style A fill:#1f3a93,color:#fff
    style C fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `133` — Distribución Eléctrica |
| Subsubject | `002` — Power Architecture and Bus Topology |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |

## 5. References & Citations

[^ecssest20]: **ECSS-E-ST-20C — Electrical and Electronic**.
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards
- ECSS-E-ST-20C — Electrical and Electronic
