---
document_id: QATL-ATLAS-1000-STA-130-139-03-133-007-EMC-GROUNDING-BONDING-AND-ISOLATION
title: "STA 130-139 · 03.133.007 — EMC, Grounding, Bonding and Isolation"
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
subsubject: "007"
subsubject_title: "EMC, Grounding, Bonding and Isolation"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-DATAGOV, Q-HPC, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · Section 03 · Subsection 133 · Subsubject 007 — EMC, Grounding, Bonding and Isolation

## 1. Purpose

Defines **EMC, grounding, bonding, and isolation architecture** requirements for Q+ATLANTIDE STA-band platforms.

## 2. Scope

- **Single-point ground (SPG)** — all chassis returns joined at one spacecraft structure reference node; prevents ground loops; DC common-mode noise < 50 mV.
- **Chassis bonding** — all structure-mounted units bonded with resistance ≤ 2.5 mΩ per ECSS-E-ST-20-07C; bond straps with cross-sectional area ≥ signal return wire area.
- **Isolation** — primary bus isolated from chassis by ≥ 1 MΩ; verified by isolation test; floating bus prevents galvanic corrosion on orbit.
- **Conducted emission (CE)** — per MIL-STD-461G CE101 (AC) / CE102 (DC); measured at power input ports of each unit.
- **Conducted susceptibility (CS)** — per MIL-STD-461G CS101/CS114; all units must pass bus ripple/surge injection.
- **Radiated emission (RE)** — per MIL-STD-461G RE102; cable shielding and chassis slot gasketing.

## 3. Diagram — EMC, Grounding, Bonding and Isolation

```mermaid
flowchart TD
    A["Power Source Input\n(→ 130 / 131 / 132)"] --> B["EMC, Grounding, Bonding and Isolation\n(STA-133-007)"]
    B --> C["Load Interfaces\n(→ 121 / 100 / Payload)"]
    B --> D["Fault Isolation\n(→ 005)"]
    style A fill:#1f3a93,color:#fff
    style C fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `133` — Distribución Eléctrica |
| Subsubject | `007` — EMC, Grounding, Bonding and Isolation |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |

## 5. References & Citations

[^ecssest20]: **ECSS-E-ST-20C — Electrical and Electronic**.
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards
- ECSS-E-ST-20C; MIL-STD-461G; ECSS-E-ST-20-07C
