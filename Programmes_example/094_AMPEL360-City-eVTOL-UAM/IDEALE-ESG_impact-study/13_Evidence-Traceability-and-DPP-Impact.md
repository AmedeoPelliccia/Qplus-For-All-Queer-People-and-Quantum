---
document_id: AMPEL360-CITY-EVTOL-IDEALE-ESG-13-EVIDENCE-TRACEABILITY-DPP
title: "Evidence Traceability and DPP Impact — AMPEL360 City eVTOL — UAM (City-eVTOL)"
programme: "AMPEL360 City eVTOL — UAM"
framework: "IDEALE-ESG"
file: "13_Evidence-Traceability-and-DPP-Impact"
status: "draft / programme-impact-study"
classification: "open-technical-programme-study"
owner: "Amedeo Pelliccia / Q+"
primary_language: "en"
created: 2026-05-09
no_aaa_rule: true
---

# Evidence Traceability and DPP Impact — AMPEL360 City eVTOL — UAM (City-eVTOL)

## 1. Purpose

Defines the evidence traceability requirements and Digital Product Passport (DPP) impact for the **AMPEL360 City eVTOL — UAM** programme across all IDEALE-ESG axes.

## 2. Evidence Requirements by Axis

```yaml
evidence_requirements:
  A_Aerospace:
    - requirements traceability
    - system decomposition and interface definitions
    - configuration baselines

  E_Energy:
    - propulsion system architecture evidence
    - energy safety assumptions
    - thermal management evidence

  E3_Environments:
    - LCA evidence
    - emissions measurement and monitoring evidence

  G_Governance:
    - Q-Division authority records
    - lifecycle gate evidence packages
    - ORB-Function decision records

  I_Information:
    - S1000D data module mapping
    - CSDB structure
    - PLM configuration records
    - DPP records

  L_Logistics:
    - GSE and supply chain qualification evidence
    - MRO strategy evidence

  S_Social:
    - safety culture evidence
    - worker rights compliance evidence
    - accessibility assessment

  D_Defense:
    - dual-use screening records
    - export-control classification evidence
```

## 3. DPP Interface

```yaml
dpp_interface:
  standard: "EU DPP / EASA Digital Twin Framework"
  programme: "AMPEL360 City eVTOL — UAM"
  dpp_scope:
    - materials traceability
    - energy carrier lifecycle data
    - maintenance and repair records
    - end-of-life circularity data
  controlled_by: "Q-DATAGOV / PLM / digital-thread"
```

## 4. Lifecycle Evidence Packages

| Gate | Evidence Package | Required Axes | Status |
|---|---|---|---|
| Gate 1 — Concept | Concept Evidence Package | A, E, G | TBD |
| Gate 2 — Preliminary Design | PD Evidence Package | A, E, E3, G, I | TBD |
| Gate 3 — Detailed Design | DD Evidence Package | A, E, E2, E3, G, I, L | TBD |
| Gate 4 — Certification Basis | Cert Evidence Package | A, E, G, S | TBD |
| Gate 5 — Entry Into Service | EIS Evidence Package | All axes | TBD |
