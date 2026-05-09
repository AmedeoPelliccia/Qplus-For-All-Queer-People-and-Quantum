---
document_id: QATL-ATLAS-1000-STA-130-139-03-133-050-SWITCHING-PROTECTION-AND-FAULT-ISOLATION
title: "STA 130-139 · 133-050 — Switching Protection and Fault Isolation"
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
subsubject: "050"
subsubject_title: "Switching Protection and Fault Isolation"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-DATAGOV, Q-HPC, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · 133-050 — Switching Protection and Fault Isolation

## 1. Purpose

Defines **load switching, protection, and fault isolation architecture** for electrical distribution on Q+ATLANTIDE STA-band platforms.

## 2. Scope

- **Remote power controllers (RPCs)** — solid-state switching; programmable current limits; latch-off on fault; telemetry-readable status; preferred for non-explosive pyro loads.
- **Latching current limiters (LCLs)** — active current limiting with latch-off; protects bus from load short-circuit; reset via telecommand.
- **Fuses** — passive protection (last resort); selected per ECSS-E-ST-20C Table B; not re-settable; used for high-reliability irreversible protection.
- **Fault isolation** — single-fault tolerance: any single short-circuit on a load must not propagate to adjacent bus; verified by worst-case fault analysis.
- **Pyrotechnic switching** — squib drivers for one-shot deployment/separation events; firing capacitor bank; inhibit plug for ground operations.

## 3. Diagram — Switching, Protection and Fault Isolation

```mermaid
flowchart TD
    A["Power Source Input\n(→ 130 / 131 / 132)"] --> B["Switching, Protection and Fault Isolation\n(STA-133-005)"]
    B --> C["Load Interfaces\n(→ 121 / 100 / Payload)"]
    B --> D["Fault Isolation\n(→ 005)"]
    style A fill:#1f3a93,color:#fff
    style C fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `133` — Distribución Eléctrica |
| Subsubject | `005` — Switching, Protection and Fault Isolation |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |

## 5. References & Citations

[^ecssest20]: **ECSS-E-ST-20C — Electrical and Electronic**.
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards
- ECSS-E-ST-20C — Electrical and Electronic
