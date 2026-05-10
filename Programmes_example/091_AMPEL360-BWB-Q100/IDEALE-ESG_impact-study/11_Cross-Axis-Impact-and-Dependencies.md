---
document_id: AMPEL360-BWB-Q100-IDEALE-ESG-11-CROSS-AXIS-IMPACT
title: "Cross-Axis Impact and Dependencies — AMPEL360 BWB Q100 (BWB-Q100)"
programme: "AMPEL360 BWB Q100"
framework: "IDEALE-ESG"
file: "11_Cross-Axis-Impact-and-Dependencies"
status: "draft / programme-impact-study"
classification: "open-technical-programme-study"
owner: "Amedeo Pelliccia / Q+"
primary_language: "en"
created: 2026-05-09
no_aaa_rule: true
---

# Cross-Axis Impact and Dependencies — AMPEL360 BWB Q100 (BWB-Q100)

## 1. Purpose

Identifies compound risks and cross-axis dependencies where impacts in one IDEALE-ESG axis create or amplify impacts in another axis for the **AMPEL360 BWB Q100** programme.

## 2. Dependency Map

```yaml
cross_axis_dependencies:
  A_Aerospace:
    depends_on: [E-Energy, I-Information, G-Governance, L-Logistics]
    driven_by: []
  E_Energy:
    depends_on: [A-Aerospace, E3-Environments, L-Logistics, G-Governance]
    driven_by: [A-Aerospace]
  E3_Environments:
    depends_on: [E-Energy, A-Aerospace, G-Governance]
    driven_by: []
  I_Information:
    depends_on: [G-Governance, A-Aerospace, L-Logistics]
    driven_by: [A-Aerospace]
  L_Logistics:
    depends_on: [E-Energy, A-Aerospace, I-Information]
    driven_by: [A-Aerospace, E-Energy]
  S_Social:
    depends_on: [A-Aerospace, E3-Environments, G-Governance, L-Logistics]
    driven_by: []
  E2_Economics:
    depends_on: [L-Logistics, E-Energy, S-Social, A-Aerospace]
    driven_by: []
  G_Governance:
    depends_on: []
    driven_by: [A-Aerospace, E-Energy, I-Information, L-Logistics, S-Social]
  D_Defense:
    depends_on: [G-Governance, I-Information]
    driven_by: []
```

## 3. Compound Risk Register

> **Status:** ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) — ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange).

| Risk ID | Primary Axis | Secondary Axis | Compound Risk Description | Combined Impact Score |
|---|---|---|---|:---:|
| CX-001 | A | E | ![TBD](https://img.shields.io/badge/TBD-red) | ![TBD](https://img.shields.io/badge/TBD-red) |
| CX-002 | E | L | ![TBD](https://img.shields.io/badge/TBD-red) | ![TBD](https://img.shields.io/badge/TBD-red) |
| CX-003 | I | G | ![TBD](https://img.shields.io/badge/TBD-red) | ![TBD](https://img.shields.io/badge/TBD-red) |

## 4. Mitigation Priorities

_To be completed after individual axis assessments. Prioritise compound risks by combined impact score._
