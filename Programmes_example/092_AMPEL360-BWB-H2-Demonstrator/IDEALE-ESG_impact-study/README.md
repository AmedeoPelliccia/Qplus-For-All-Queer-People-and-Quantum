---
document_id: AMPEL360-BWB-H2-DEMO-IDEALE-ESG-IMPACT-STUDY-README
title: "IDEALE-ESG Impact Study — AMPEL360 BWB H2 Demonstrator (H2-DEMO)"
programme: "AMPEL360-BWB-H2-Demonstrator"
configuration: "BWB Hydrogen Demonstrator Aircraft"
framework: "IDEALE-ESG"
status: "draft / programme-impact-study"
classification: "open-technical-programme-study"
owner: "Amedeo Pelliccia / Q+"
primary_language: "en"
created: 2026-05-09
no_aaa_rule: true
---

# IDEALE-ESG Impact Study — AMPEL360 BWB H2 Demonstrator (H2-DEMO)

## 1. Purpose

This README defines the controlled entry point for the **IDEALE-ESG Impact Study** of **AMPEL360-BWB-H2-Demonstrator**, a scaled technology demonstrator for the **BWB hydrogen-electric aircraft** family targeting TRL 5–6 maturation.

The study evaluates how the H2-DEMO programme is affected across the IDEALE-ESG axes:

```text
A  — Aerospace
D  — Defense
E  — Energy
E2 — Economics
E3 — Environments
G  — Governance
I  — Information
L  — Logistics
S  — Social
```

This document is a programme-impact and governance artefact. It is not a certified aircraft design, production approval, operational approval or legal compliance finding.

---

## 2. Repository Position

```text
Programmes_example/
└── 092_AMPEL360-BWB-H2-Demonstrator/
    └── IDEALE-ESG_impact-study/
        ├── README.md
        ├── 00_Overview.md
        ├── 01_IDEALE-ESG-Axis-Impact-Matrix.md
        ├── 02_A-Aerospace-Impact.md
        ├── 03_D-Defense-Restricted-Boundary-Impact.md
        ├── 04_E-Energy-Impact.md
        ├── 05_E2-Economics-Impact.md
        ├── 06_E3-Environments-Impact.md
        ├── 07_G-Governance-Impact.md
        ├── 08_I-Information-Impact.md
        ├── 09_L-Logistics-Impact.md
        ├── 10_S-Social-Impact.md
        ├── 11_Cross-Axis-Impact-and-Dependencies.md
        ├── 12_Risk-Opportunity-and-Mitigation-Register.md
        ├── 13_Evidence-Traceability-and-DPP-Impact.md
        ├── 14_Safety-Certification-and-Lifecycle-Gate-Impact.md
        └── 15_Conclusions-and-Programme-Recommendations.md
```

---

## 3. Controlled Reading

```yaml
controlled_reading:
  framework: "IDEALE-ESG"
  use_case: "programme-impact assessment"
  programme: "AMPEL360-BWB-H2-Demonstrator"
  aircraft_type: "BWB hydrogen-electric technology demonstrator"
  baseline_energy_carrier: "LH2"
  trl_target: "TRL 5-6"
  documentation_logic: "S1000D / CSDB compatible"
  evidence_logic: "PLM / DPP / digital-thread traceability"
  governance_logic: "deterministic, auditable, lifecycle-gated"
```

---

## 4. Axis Impact Matrix

| Axis | Name | H2-DEMO Impact Area | Primary Concern |
| ---- | ---- | ------------------- | --------------- |
| A | Aerospace | BWB demonstrator architecture, scaled flight test, airworthiness | Airworthy demonstrator baseline and test programme |
| D | Defense | Restricted dual-use and resilience boundary | Non-operational defence screening only |
| E | Energy | LH₂ demonstrator propulsion, cryogenic storage, fuel-cell integration | Safe hydrogen demonstrator architecture |
| E2 | Economics | Research funding, demonstrator economics, industrial readiness | Demonstrator return on investment |
| E3 | Environments | Demonstrator emissions footprint, hydrogen production, LCA | Environmental evidence for scaling |
| G | Governance | Q-Divisions, ORB-Functions, TRL gates, research governance | Accountable research programme control |
| I | Information | PLM, test data management, DPP, traceability for scaling | Controlled technical data for production transition |
| L | Logistics | Test facility operations, cryogenic GSE, demonstration logistics | Test campaign supportability |
| S | Social | Research team safety, public demonstration acceptance | Safety culture and public value |

---

## 5. Axis Files

### 5.1 A — Aerospace

Assesses BWB demonstrator configuration, scaled aerodynamic validation, aircraft systems at demonstrator TRL, flight test programme assumptions, and S1000D / CSDB implications for test documentation.

### 5.2 D — Defense

Assesses restricted boundary screening, dual-use risk, resilience, and export-control awareness. Excludes weaponization, targeting and offensive procedures.

### 5.3 E — Energy

Assesses LH₂ demonstrator propulsion, cryogenic storage systems, fuel-cell integration at demonstrator scale, thermal management, and test energy infrastructure.

### 5.4 E2 — Economics

Assesses demonstrator programme funding, research return-on-investment, cost-to-TRL model, industrial readiness assessment, and transition economics to production programme.

### 5.5 E3 — Environments

Assesses demonstrator lifecycle emissions, hydrogen production footprint, test campaign environmental impact, and lifecycle analysis evidence for programme scaling.

### 5.6 G — Governance

Assesses Q-Division authority over demonstrator research, ORB-Function support, TRL gate framework, decision rights, and research auditability.

### 5.7 I — Information

Assesses test data management, PLM for demonstrator configuration, S1000D / CSDB for test publications, DPP, and digital thread supporting transition to production.

### 5.8 L — Logistics

Assesses test facility support, cryogenic GSE at demonstrator scale, campaign logistics, and lessons for operational scaling.

### 5.9 S — Social

Assesses research team safety, public demonstration acceptance, regulatory engagement, and civilisational benefit of demonstrator as technology bridge.

---

## 6. Cross-Axis Dependencies

```yaml
cross_axis_dependencies:
  A_Aerospace:
    depends_on: [E-Energy, I-Information, G-Governance, L-Logistics]
  E_Energy:
    depends_on: [A-Aerospace, E3-Environments, L-Logistics, G-Governance]
  I_Information:
    depends_on: [G-Governance, A-Aerospace, L-Logistics]
  L_Logistics:
    depends_on: [E-Energy, A-Aerospace, I-Information]
  S_Social:
    depends_on: [A-Aerospace, E3-Environments, G-Governance, L-Logistics]
```

---

## 7. Impact Scoring Model

| Score | Meaning |
| ----: | ------- |
| 0 | No material impact |
| 1 | Low impact; documentation only |
| 2 | Moderate impact; architecture or governance adjustment required |
| 3 | High impact; programme-level mitigation required |
| 4 | Critical impact; lifecycle gate cannot close without resolution |
| 5 | Blocking impact; programme baseline cannot proceed without redesign or authority decision |

---

## 8. Controlled Conclusion Format

```yaml
impact_summary:
  ideale_esg_axis:
  affected_programme_area:
  impact_score:
  positive_impacts:
  negative_impacts:
  risks:
  mitigations:
  evidence_required:
  lifecycle_gate_relevance:
  q_division_ownership:
  orb_function_support:
  recommendation:
```

---

## 9. Status

```yaml
status:
  maturity: "draft / programme-impact-study"
  release_status: "README-ready"
  next_steps:
    - "complete 00_Overview.md"
    - "complete 01_IDEALE-ESG-Axis-Impact-Matrix.md"
    - "draft one impact file per IDEALE-ESG axis"
    - "define scoring model"
    - "connect evidence to PLM / DPP / S1000D-CSDB maps"
```
