---
document_id: QATL-ATLAS-1000-STA-130-139-03-133-006-LOAD-MANAGEMENT-AND-PRIORITY-SHEDDING
title: "STA 130-139 · 03.133.006 — Load Management and Priority Shedding"
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
subsubject: "006"
subsubject_title: "Load Management and Priority Shedding"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-DATAGOV, Q-HPC, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · Section 03 · Subsection 133 · Subsubject 006 — Load Management and Priority Shedding

## 1. Purpose

Establishes **load management and priority load-shedding** requirements for Q+ATLANTIDE STA-band platforms.

## 2. Scope

- **Load priority tiers** — Tier 1 (safety-critical): OBDH, attitude control actuators, crew safety systems (→ `103_Seguridad-de-Mision`), minimum thermal; Tier 2 (mission-critical): primary payload, comms; Tier 3 (non-essential): auxiliary payload, logging, non-critical heating.
- **Automatic load shedding** — triggered by bus undervoltage threshold (V_bus < 90% nominal); shed Tier 3 first, then Tier 2 if V_bus < 85%; preserve Tier 1 always.
- **Telecommand load shedding** — ground-commanded shedding for planned orbit maintenance or contingency.
- **Safe-mode power floor** — Tier 1 loads must be powered continuously from battery during safe-mode, worst-case eclipse, for minimum 72 h (crewed) / 24 h (robotic).
- **Load model** — detailed load current profile (on/off timeline, transient peaks) required in power budget at PDR/CDR.

## 3. Diagram — Load Management and Priority Shedding

```mermaid
flowchart TD
    A["Power Source Input\n(→ 130 / 131 / 132)"] --> B["Load Management and Priority Shedding\n(STA-133-006)"]
    B --> C["Load Interfaces\n(→ 121 / 100 / Payload)"]
    B --> D["Fault Isolation\n(→ 005)"]
    style A fill:#1f3a93,color:#fff
    style C fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `133` — Distribución Eléctrica |
| Subsubject | `006` — Load Management and Priority Shedding |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |

## 5. References & Citations

[^ecssest20]: **ECSS-E-ST-20C — Electrical and Electronic**.
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards
- ECSS-E-ST-20C — Electrical and Electronic
