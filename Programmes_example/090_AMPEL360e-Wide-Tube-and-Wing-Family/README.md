---
document_id: AMPEL360e-eWTW-PROGRAMME-README
title: "Programme Example — AMPEL360e Wide Tube-and-Wing Family (eWTW)"
programme: "AMPEL360e-eWTW"
programme_code: "090"
configuration: "Wide-Body Tube-and-Wing Electric/Hybrid Family"
abbreviation: "eWTW"
status: "draft / programme-impact-study"
classification: "open-technical-programme-study"
owner: "Amedeo Pelliccia / Q+"
primary_language: "en"
created: 2026-05-09
no_aaa_rule: true
---

# Programme Example — AMPEL360e Wide Tube-and-Wing Family (eWTW)

## Overview

The **AMPEL360e Wide Tube-and-Wing Family (eWTW)** is the Gen 1 baseline commercial aircraft programme: a family of conventional wide-body tube-and-wing aircraft incorporating electric and hybrid-electric propulsion, SAF compatibility, and hydrogen-readiness across multiple variants.

## Repository Structure

```text
Programmes_example/
└── 090_AMPEL360e-Wide-Tube-and-Wing-Family/
    ├── README.md  ← this file
    ├── IDEALE-ESG_impact-study/
    │   └── README.md
    └── Q+ATLANTIDE_impact-study/        ← impact analysis layer
        ├── README.md
        └── 000-099_ATLAS-impact-analysis/
            ├── README.md
            └── 020-029_Sistemas-Core-de-Aeronave/
                └── 020_Air-Conditioning-and-Pressurization/
                    ├── README.md
                    └── S1000D-CSDB/     ← technical publication layer
                        ├── README.md
                        ├── BREX/
                        │   └── README.md
                        ├── SNS/
                        │   └── README.md
                        └── DMC/
                            ├── README.md
                            └── DMC-AMPEL360E-EWTW-020-{NNN}-00A-040A-D_*.xml  (10 DMs)
```

### Production Layer Separation

| Layer | Role | Location |
|---|---|---|
| Q+ATLANTIDE impact study | Impact analysis, architecture effect, ESG, Q-Division ownership | `Q+ATLANTIDE_impact-study/` |
| S1000D CSDB | Authoritative descriptive data modules (system descriptions) | `Q+ATLANTIDE_impact-study/.../020_Air-Conditioning-and-Pressurization/S1000D-CSDB/` |

System descriptions are **Descriptive Data Modules** in the S1000D CSDB — not `Impact.md` files.

## Programme Reference

| Field | Value |
|---|---|
| Programme code | `090` |
| Programme name | AMPEL360e Wide Tube-and-Wing Family |
| Abbreviation | eWTW |
| Generation | Gen 1 baseline |
| Propulsion | Hybrid-electric / SAF / H₂-ready |
| ATLAS section | `090` — AMPEL360e Tube-and-Wing Family |
| Primary Q-Division | Q-AIR |
| Governance | Q+ATLANTIDE baseline |

## Governance Boundary

This document is a programme-impact and governance artefact. It is not a certified aircraft design, production approval, operational approval or legal compliance finding.
