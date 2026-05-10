---
document_id: AMPEL360-CITY-EVTOL-UAM-QATLANTIDE-IMPACT-STUDY-README
title: "Q+ATLANTIDE Impact Study — AMPEL360 City eVTOL — UAM"
programme: "AMPEL360-City-eVTOL-UAM"
configuration: "Electric Vertical Take-Off and Landing — Urban Air Mobility"
framework: "Q+ATLANTIDE"
register: "Q+ATLANTIDE1000"
status: "draft / programme-impact-study"
classification: "open-technical-programme-study"
owner: "Amedeo Pelliccia / Q+"
primary_language: "en"
created: 2026-05-09
no_aaa_rule: true
---

# Q+ATLANTIDE Impact Study — AMPEL360 City eVTOL — UAM

## 1. Purpose

This README defines the controlled entry point for the **Q+ATLANTIDE Impact Study** of **AMPEL360-City-eVTOL-UAM**, a hybrid electric vertical take-off and landing aircraft designed for **Urban Air Mobility (UAM)** applications.

The study evaluates how **Q+ATLANTIDE** and **Q+ATLANTIDE1000** affect the programme across architecture classification, lifecycle evidence, S1000D / CSDB, PLM / DPP traceability, certification readiness, safety governance, cybersecurity, energy, materials, ground operations and long-horizon technology boundaries.

This document is a programme-impact and governance artefact. It is not a certified aircraft design, production approval, operational approval or compliance finding.

---

## 2. Repository Position

```text
Programmes_example/
└── 094_AMPEL360-City-eVTOL-UAM/
    └── Q+ATLANTIDE_impact-study/
        ├── README.md
        ├── 000-Overview.md
        ├── 010-Architecture-Band-Impact-Matrix.md
        ├── 020-ATLAS-Aircraft-Architecture-Impact.md
        ├── 030-EPTA-Energy-and-Propulsion-Impact.md
        ├── 040-AMTA-Materials-and-Structures-Impact.md
        ├── 050-DTCEC-Digital-Twin-Cloud-Edge-AI-Impact.md
        ├── 060-CYB-Cybersecurity-and-Data-Protection-Impact.md
        ├── 070-QCSAA-Quantum-and-Sentient-Agency-Boundary-Impact.md
        ├── 080-STA-Space-Derivative-and-Long-Horizon-Impact.md
        ├── 090-DTTA-Restricted-Defence-Boundary-Impact.md
        ├── 100-OGATA-Ground-Automation-and-GSE-Impact.md
        ├── 110-ACV-UAM-Vertiport-and-Urban-Interface-Impact.md
        ├── 120-Q-Division-and-ORB-Function-Impact.md
        ├── 130-S1000D-CSDB-and-Technical-Publications-Impact.md
        ├── 140-PLM-DPP-Digital-Thread-and-Evidence-Impact.md
        ├── 150-Safety-Certification-and-Lifecycle-Gate-Impact.md
        ├── 160-ESG-Civilisational-and-Governance-Impact.md
        ├── 170-Risk-Opportunity-and-Trade-Space.md
        ├── 180-Impact-Scoring-Model.md
        └── 190-Conclusions-and-Programme-Recommendations.md
```

---

## 3. Controlled Reading

```yaml
controlled_reading:
  framework: "Q+ATLANTIDE"
  register: "Q+ATLANTIDE1000"
  use_case: "programme-impact assessment"
  programme: "AMPEL360-City-eVTOL-UAM"
  aircraft_type: "electric vertical take-off and landing urban air mobility aircraft"
  baseline_energy_carrier: "battery-electric / hybrid-electric"
  operations: "vertiport-based urban and suburban UAM"
  primary_architecture_band: "ATLAS 000-099 / ACV 700-799"
  documentation_logic: "S1000D / CSDB compatible"
  evidence_logic: "PLM / DPP / digital-thread traceability"
  governance_logic: "deterministic, auditable, lifecycle-gated"
```

---

## 4. Architecture Band Impact Matrix

| Architecture Band | Name | City eVTOL Impact Area | Primary Concern |
| ----------------- | ---- | ---------------------- | --------------- |
| ATLAS 000-099 | Aircraft Top-Level Architecture Schema/System | eVTOL aircraft architecture, DEP systems, airworthiness | Certifiable eVTOL aircraft baseline |
| STA 100-199 | Space Technology Architecture | Space-derived navigation and communications for urban ops | Urban airspace communications |
| DTTA 200-299 | Defence Technology Type Architecture | Autonomous flight dual-use boundary review | Non-operational defence screening only |
| DTCEC 300-399 | Digital Twin, Cloud, Edge & AI Architecture | Urban flight management AI, digital twin, autonomous systems | Controlled AI governance for autonomous UAM |
| EPTA 400-499 | Energy & Propulsion Technology Architecture | Battery-electric / hybrid-electric DEP, charging | Safe electric propulsion architecture |
| AMTA 500-599 | Advanced Material, Bio & Nanotechnology Architecture | Lightweight urban-aircraft structures, battery materials | Materials qualification and circularity |
| OGATA 600-699 | On-Ground Automation Technology Architecture | Vertiport automation, charging logistics, ground robotics | Urban operational supportability |
| ACV 700-799 | Aerial City Viability / UAM Architecture | Vertiports, urban airspace, passenger flow, community | Urban infrastructure and social compatibility |
| CYB 800-899 | Cybersecurity Architecture | Autonomous flight cybersecurity, urban data protection | Safety-relevant cyber resilience for UAM |
| QCSAA 900-999 | Quantum Computing & Sentient Agency Architecture | AI/autonomous-system sentient-agency governance boundary | Non-operational autonomy boundary governance |

---

## 5. Q-Division and ORB Impact

```yaml
primary_q_divisions:
  - Q-AIR
  - Q-GREENTECH
  - Q-DATAGOV

support_q_divisions:
  - Q-STRUCTURES
  - Q-MECHANICS
  - Q-GROUND
  - Q-INDUSTRY
  - Q-HPC
  - Q-HORIZON

support_orb_functions:
  - ORB-PMO
  - ORB-LEG
  - ORB-FIN
  - ORB-HR
  - ORB-CSR
  - ORB-MKTG
```

---

## 6. Governance Boundary

```yaml
governance_boundary:
  study_type: "Q+ATLANTIDE impact study"
  not_certification: true
  not_type_design_approval: true
  not_production_approval: true
  not_operational_approval: true
  not_supplier_release: true
  not_final_safety_case: true

  required_for_programme_use:
    - technical authority review
    - safety review
    - legal review where applicable
    - lifecycle gate acceptance
    - configuration control
    - evidence traceability
```

---

## 7. No-AAA Rule

`AAA` is not a valid domain, division, architecture, interface or enterprise function.

---

## 8. Status

```yaml
status:
  maturity: "draft / programme-impact-study"
  release_status: "README-ready"
  next_steps:
    - "complete 000-Overview.md"
    - "complete 010-Architecture-Band-Impact-Matrix.md"
    - "draft one impact file per architecture band"
    - "define scoring model"
    - "connect evidence to PLM / DPP / S1000D-CSDB maps"
```
