---
document_id: QATL-ATLAS-1000-STA-120-129-02-122-090-ASSURANCE-EVIDENCE-AND-NON-DEPLOYMENT-BOUNDARIES
title: "STA 120-129 · 122-090 — Assurance Evidence and Non Deployment Boundaries"
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
subsection: "122"
subsubject: "090"
subsubject_title: "Assurance Evidence and Non Deployment Boundaries"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · 122-090 — Assurance Evidence and Non Deployment Boundaries

## 1. Purpose

Defines **assurance evidence requirements and non-deployment boundary conditions** for conceptual nuclear propulsion within the Q+ATLANTIDE STA band.

## 2. Scope

- **Non-deployment boundary declaration** — This subsection (`122`) is designated **conceptual-only**. No system in this subsection shall advance to design, manufacture, flight hardware assembly, launch integration, or flight operation without:
  1. Separate programme authority with lawful mandate.
  2. Completed Nuclear Launch Safety Approval (NLSA) per NASA-NSS 1676.1[^nasanss16761].
  3. Environmental Impact Statement (EIS) and safety analysis report (SAR) signed by competent authority.
  4. Applicable IAEA and treaty compliance documentation.
  5. Explicit safety boundary upgrade in this registry from `conceptual-only` to `qualified for [phase]`.
- **Assurance evidence package** — For any future conceptual-to-design transition, the following evidence package is required:
  - Mission safety analysis (hazard identification and risk classification per `103_Seguridad-de-Mision`).
  - Radiation environment and shielding verification evidence (ref `006`).
  - Power conversion qualification evidence (ref `005`).
  - Regulatory approvals (NLSA, EIS, IAEA, treaty compliance).
- **Lifecycle traceability** — All conceptual studies archived per ECSS-Q-ST-20C[^ecssqst20c]; document_ids registered in this STA-122 namespace; change log maintained.

## 3. Diagram — Assurance Gate for Conceptual-to-Design Transition

```mermaid
flowchart LR
    A["STA-122<br/>Conceptual-Only Status"] --> B["Programme Authority<br/>(lawful mandate)"]
    B --> C["NLSA · EIS · SAR<br/>(NASA-NSS 1676.1)"]
    C --> D["IAEA / Treaty<br/>(compliance docs)"]
    D --> E["Safety Boundary Upgrade<br/>(registry update)"]
    E --> F["Design Phase<br/>(authorised)"]
    style A fill:#7b0000,color:#fff
    style F fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `122` — Propulsión Nuclear Conceptual |
| Subsubject | `010` — Assurance Evidence and Non-Deployment Boundaries |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Safety boundary | conceptual-only |
| Document | `122-090-Assurance-Evidence-and-Non-Deployment-Boundaries.md` (this file) |

## 5. References & Citations

[^nasanss16761]: **NASA-NSS 1676.1 — Nuclear Safety Policy**.

[^ecssqst20c]: **ECSS-Q-ST-20C — Quality Assurance**.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- NASA-NSS 1676.1 — Nuclear Safety Policy[^nasanss16761]
- ECSS-Q-ST-20C — Quality Assurance[^ecssqst20c]
- IAEA Safety Framework for Nuclear Power Source Applications in Outer Space (2009)
