---
document_id: QATL-ATLAS-1000-STA-120-129-02-123-007-FIELD-EFFECT-AND-EXOTIC-PROPULSION-CLAIM-DISCIPLINE
title: "STA 120-129 · 02.123.007 — Field-Effect and Exotic Propulsion Claim Discipline"
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
subsection: "123"
subsubject: "007"
subsubject_title: "Field-Effect and Exotic Propulsion Claim Discipline"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · Section 02 · Subsection 123 · Subsubject 007 — Field-Effect and Exotic Propulsion Claim Discipline

## 1. Purpose

Establishes the **claim discipline protocol** for field-effect and exotic propulsion claims within the Q+ATLANTIDE STA band advanced propulsion framework.

## 2. Scope

- **Claim discipline requirement** — Extraordinary propulsion claims shall include: (a) a physics-grounded engineering model, (b) independent experimental verification, and (c) an explicit TRL statement. Claims of performance for concepts below TRL 3 are theoretical estimates only.
- **Excluded claims** — The following concepts have no credible independent verification of anomalous thrust and are excluded from Q+ATLANTIDE advanced propulsion roadmaps pending verified reproduction:
  - *EMDrive / RF resonant cavity thruster* — Multiple independent replications have not confirmed anomalous thrust above measurement artefacts (NASA, TU Dresden, 2021).
  - *Mach effect thruster* — Theoretical basis disputed; no independent confirmation of macroscopic propulsion effect.
  - *Inertial propulsion devices* — Violate conservation of momentum; excluded.
- **Included with claim discipline** — Concepts with theoretical basis and limited (not yet independently replicated) experimental evidence:
  - *Woodward effect (piezoelectric fluctuation)* — Theoretical basis in Mach effect; very low thrust measured; TRL 1–2; independent replication required before ATLAS inclusion.
  - *Photon rocket* — Theoretical; Isp = c/g₀ ≈ 3 × 10⁷ s; requires 100% efficiency radiation source; laser-propelled sails covered in `003`/`005`.
- **Verification protocol** — Independent verification = measurement at ≥ 2 independent facilities, vacuum chamber (< 10⁻⁵ Pa), with calibrated thrust balance (resolution < 1 µN), shielded from thermal/EMC artefacts.

## 3. Diagram — Claim Discipline Decision Tree

```mermaid
flowchart TD
    A["Exotic Propulsion Claim<br/>(007)"]
    A --> B{"Physics model<br/>consistent with<br/>known laws?"}
    B -->|No| C["Excluded<br/>(conservation law violation)"]
    B -->|Yes| D{"Independent<br/>experimental<br/>verification?"}
    D -->|No| E["TRL 1 — Theoretical<br/>claim discipline required"]
    D -->|Yes TRL≥3| F["Include with<br/>TRL statement"]
    style A fill:#1a472a,color:#fff
    style C fill:#7b0000,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `123` — Propulsión Avanzada |
| Subsubject | `007` — Field-Effect and Exotic Propulsion Claim Discipline |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Safety boundary | research and concept-screening only |
| Document | `007_Field-Effect-and-Exotic-Propulsion-Claim-Discipline.md` (this file) |

## 5. References & Citations

[^nasatrl]: **NASA TRL Definitions** — Technology Readiness Level scale.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- NASA TRL Definitions[^nasatrl]
- ECSS-E-ST-10C — System Engineering General Requirements
