---
document_id: QATL-ATLAS-1000-STA-130-139-03-133-001-ELECTRICAL-DISTRIBUTION-CONTROLLED-DEFINITION
title: "STA 130-139 · 03.133.001 — Electrical Distribution Controlled Definition"
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
subsubject: "001"
subsubject_title: "Electrical Distribution Controlled Definition"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-DATAGOV, Q-HPC, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · Section 03 · Subsection 133 · Subsubject 001 — Electrical Distribution Controlled Definition

## 1. Purpose

Establishes the **normative definition and controlled scope** of electrical distribution within Q+ATLANTIDE STA-band platforms.

## 2. Scope

- **Controlled definition** — Electrical distribution systems transfer and regulate electrical power from primary sources (solar, battery, nuclear) to all spacecraft loads via a controlled bus topology, including power conditioning, protection, harness routing, and load management.
- **Applicability boundary** — STA `133` covers all power distribution from the primary bus output to load terminals; excludes power generation (→ `130`, `131`, `132`) and propulsion power processing units (→ `121`).
- **Controlled vocabulary** — *regulated bus*, *unregulated bus*, *remote power controller (RPC)*, *latching current limiter (LCL)*, *inrush current*, *voltage ripple*, *conducted emission*, *single-point ground (SPG)*, *return current*.
- **Safety classification** — mission-power critical; distribution fault isolation must prevent single-point failures from propagating to safety-critical loads.

## 3. Diagram — Electrical Distribution Controlled Definition

```mermaid
flowchart TD
    A["Power Source Input\n(→ 130 / 131 / 132)"] --> B["Electrical Distribution Controlled Definition\n(STA-133-001)"]
    B --> C["Load Interfaces\n(→ 121 / 100 / Payload)"]
    B --> D["Fault Isolation\n(→ 005)"]
    style A fill:#1f3a93,color:#fff
    style C fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `133` — Distribución Eléctrica |
| Subsubject | `001` — Electrical Distribution Controlled Definition |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |

## 5. References & Citations

[^ecssest20]: **ECSS-E-ST-20C — Electrical and Electronic**.
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards
- ECSS-E-ST-20C — Electrical and Electronic
