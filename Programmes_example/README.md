---
document_id: PROGRAMMES-EXAMPLE-README
title: "Programmes_example — Programme Impact Study Index"
framework: "IDEALE-ESG / Q+ATLANTIDE"
status: "active"
classification: "open-technical-programme-study"
owner: "Amedeo Pelliccia / Q+"
primary_language: "en"
created: 2026-05-09
no_aaa_rule: true
---

# Programmes_example — Programme Impact Study Index

This directory contains **programme example studies** for the AMPEL360 and GAIA-AIR aircraft family, each mapped against the **IDEALE-ESG** framework and the **Q+ATLANTIDE** architecture baseline.

Each programme example includes:

- `IDEALE-ESG_impact-study/` — impact assessment across the nine IDEALE-ESG axes (A, D, E, E2, E3, G, I, L, S)
- `Q+ATLANTIDE_impact-study/` — impact assessment across all Q+ATLANTIDE architecture bands (ATLAS, STA, DTTA, DTCEC, EPTA, AMTA, OGATA, ACV, CYB, QCSAA)

---

## Programme Index

| Code | Programme | Abbreviation | Folder |
|---:|---|---|---|
| `090` | AMPEL360e Wide Tube-and-Wing Family | eWTW | [`090_AMPEL360e-Wide-Tube-and-Wing-Family/`](./090_AMPEL360e-Wide-Tube-and-Wing-Family/) |
| `091` | AMPEL360 BWB Q100 | BWB-Q100 | [`091_AMPEL360-BWB-Q100/`](./091_AMPEL360-BWB-Q100/) |
| `092` | AMPEL360 BWB H₂ Demonstrator | H2-DEMO | [`092_AMPEL360-BWB-H2-Demonstrator/`](./092_AMPEL360-BWB-H2-Demonstrator/) |
| `093` | AMPEL360 MRTT Q300 | MRTT-Q300 | [`093_AMPEL360-MRTT-Q300/`](./093_AMPEL360-MRTT-Q300/) |
| `094` | AMPEL360 City eVTOL — UAM | City-eVTOL | [`094_AMPEL360-City-eVTOL-UAM/`](./094_AMPEL360-City-eVTOL-UAM/) |
| `095` | GAIA-AIR Sky Cleaner Environmental | GAIA-AIR-SCE | [`095_GAIA-AIR-Sky-Cleaner-Environmental/`](./095_GAIA-AIR-Sky-Cleaner-Environmental/) |

---

## Legacy Programme Examples

| Programme | Folder |
|---|---|
| AMPEL360-Q100 (BWB H2 Hy-E Q100 INTEGRA) | [`AMPEL360-Q100/`](./AMPEL360-Q100/) |

---

## Governance Boundary

All programme examples in this directory are **programme-impact and governance artefacts**. They are not certified aircraft designs, production approvals, operational approvals or legal compliance findings.

```yaml
governance_boundary:
  study_type: "programme-impact study"
  not_certification: true
  not_type_design_approval: true
  not_production_approval: true
  not_operational_approval: true
  not_supplier_release: true
  not_final_safety_case: true
```

## No-AAA Rule

`AAA` is not a valid domain, division, architecture, interface or enterprise function in this baseline.
