---
document_id: AMPEL360-CITY-EVTOL-UAM-IDEALE-ESG-IMPACT-STUDY-README
title: "IDEALE-ESG Impact Study — AMPEL360 City eVTOL — UAM"
programme: "AMPEL360-City-eVTOL-UAM"
configuration: "Electric Vertical Take-Off and Landing — Urban Air Mobility"
framework: "IDEALE-ESG"
status: "draft / programme-impact-study"
classification: "open-technical-programme-study"
owner: "Amedeo Pelliccia / Q+"
primary_language: "en"
created: 2026-05-09
no_aaa_rule: true
---

# IDEALE-ESG Impact Study — AMPEL360 City eVTOL — UAM

## 1. Purpose

This README defines the controlled entry point for the **IDEALE-ESG Impact Study** of **AMPEL360-City-eVTOL-UAM**, a hybrid electric vertical take-off and landing aircraft designed for **Urban Air Mobility (UAM)** applications.

The study evaluates how the City eVTOL programme is affected across the IDEALE-ESG axes:

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
└── 094_AMPEL360-City-eVTOL-UAM/
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
  programme: "AMPEL360-City-eVTOL-UAM"
  aircraft_type: "electric vertical take-off and landing urban air mobility aircraft"
  baseline_energy_carrier: "battery-electric / hybrid-electric"
  operations: "vertiport-based urban and suburban UAM"
  documentation_logic: "S1000D / CSDB compatible"
  evidence_logic: "PLM / DPP / digital-thread traceability"
  governance_logic: "deterministic, auditable, lifecycle-gated"
```

---

## 4. Axis Impact Matrix

| Axis | Name | City eVTOL Impact Area | Primary Concern |
| ---- | ---- | ---------------------- | --------------- |
| A | Aerospace | eVTOL aircraft architecture, distributed electric propulsion, urban operations | Certifiable eVTOL aircraft baseline |
| D | Defense | Restricted dual-use and resilience boundary | Non-operational defence screening only |
| E | Energy | Battery-electric / hybrid propulsion, charging infrastructure, energy density | Safe electric propulsion architecture |
| E2 | Economics | UAM market economics, route viability, vertiport investment, lifecycle cost | Commercial UAM viability |
| E3 | Environments | Zero in-flight emissions, urban noise, battery lifecycle, circularity | Urban environmental admissibility |
| G | Governance | Q-Divisions, ORB-Functions, UAM regulatory framework, lifecycle gates | Accountable UAM programme control |
| I | Information | S1000D, PLM, DPP, autonomous/pilot-assisted flight software governance | Controlled technical and flight data |
| L | Logistics | Vertiport operations, charging logistics, MRO in urban environment | Urban operational supportability |
| S | Social | Passenger safety, urban community acceptance, accessibility, noise impact | Urban public value and dignity |

---

## 5. Axis Files

### 5.1 A — Aerospace

Assesses eVTOL aircraft architecture, distributed electric propulsion, multi-rotor or tilt-rotor configuration, urban airspace integration, airworthiness assumptions under emerging UAM regulations, and S1000D / CSDB implications.

### 5.2 D — Defense

Assesses restricted boundary screening, dual-use risk for autonomous flight systems, resilience, and export-control awareness. Excludes weaponization, targeting and offensive procedures.

### 5.3 E — Energy

Assesses battery-electric or hybrid-electric propulsion, charging infrastructure compatibility, energy density evolution roadmap, electric distribution, thermal management, and vertiport energy interface.

### 5.4 E2 — Economics

Assesses UAM market economics, route and vertiport investment viability, seat-mile cost, fleet scaling economics, infrastructure funding model, and sustainable competitiveness.

### 5.5 E3 — Environments

Assesses zero in-flight emissions, urban noise footprint, battery lifecycle and recycling, materials circularity, and urban infrastructure environmental impact.

### 5.6 G — Governance

Assesses Q-Division authority, ORB-Function support, UAM regulatory framework alignment, lifecycle gates, decision rights, auditability, and safety-first governance for autonomous systems.

### 5.7 I — Information

Assesses PLM, S1000D, CSDB, IETP, DPP, digital thread, autonomous/pilot-assisted flight software governance, cybersecurity, and flight-data traceability.

### 5.8 L — Logistics

Assesses vertiport operational logistics, charging infrastructure, urban MRO constraints, spares philosophy for distributed propulsion, and emergency response protocols.

### 5.9 S — Social

Assesses passenger safety, urban community noise and visual acceptance, accessibility for diverse urban populations, worker rights in UAM operations, and civilisational benefit of urban mobility.

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
  E2_Economics:
    depends_on: [L-Logistics, E-Energy, S-Social, A-Aerospace]
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
