---
document_id: AMPEL360e-eWTW-S1000D-CSDB-ROOT-README
title: "S1000D CSDB — AMPEL360e Wide Tube-and-Wing Family (eWTW)"
programme: "AMPEL360e Wide Tube-and-Wing Family"
programme_code: "090"
short_code: "eWTW"
framework: "S1000D"
csdb_root: "Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/S1000D-CSDB/"
status: "draft / programme-controlled-placeholder"
classification: "open-technical-programme-study"
owner: "Amedeo Pelliccia / Q+"
primary_language: "en"
created: 2026-05-09
no_aaa_rule: true
---

# S1000D CSDB — AMPEL360e Wide Tube-and-Wing Family (eWTW)

## 1. Purpose

This directory is the **Common Source Data Base (CSDB)** root for the **AMPEL360e Wide Tube-and-Wing Family (eWTW)** programme, structured according to the **S1000D** technical publication standard.

The CSDB is the **authoritative technical publication production layer** for the eWTW programme. It is distinct from — and complementary to — the Q+ATLANTIDE impact study:

| Layer | Role |
|---|---|
| Q+ATLANTIDE / ATLAS | Architecture classification, SNS alignment, impact analysis |
| S1000D / CSDB (this directory) | Technical publication content: descriptive data modules, procedures, illustrated parts |
| System Description | Descriptive Data Module (DM), not an impact analysis file |

---

## 2. Repository Position

```text
Programmes_example/
└── 090_AMPEL360e-Wide-Tube-and-Wing-Family/
    ├── README.md
    ├── IDEALE-ESG_impact-study/
    ├── Q+ATLANTIDE_impact-study/         ← impact analysis layer
    └── S1000D-CSDB/                      ← this directory (publication layer)
        ├── README.md
        ├── BREX/
        │   └── README.md
        ├── SNS/
        │   └── ATLAS-020_Air-Conditioning-and-Pressurization/
        │       └── README.md
        └── DMC/
            └── ATLAS-020_Air-Conditioning-and-Pressurization/
                ├── README.md
                └── DMC-AMPEL360E-EWTW-020-{NNN}-00A-040A-D_*.xml
```

---

## 3. Controlled Reading

```yaml
controlled_reading:
  programme: "AMPEL360e Wide Tube-and-Wing Family"
  short_code: "eWTW"
  s1000d_issue: "4.x (programme-controlled)"
  csdb_role: "controlled storage, retrieval, issue control and reuse of data modules"
  document_scope: "technical publication placeholder — not certified design or approved procedure"
  brex_status: "pending — BREX freeze required before production release"
  dmrl_status: "draft — data module requirement list subject to programme review"
```

---

## 4. CSDB Structure

| Folder | Content |
|---|---|
| `BREX/` | Business Rules EXchange documents controlling schema, SNS and info code usage |
| `SNS/` | Standard Numbering System mapping: ATLAS node to ATA/SNS alignment |
| `DMC/` | Data Module Code directories containing S1000D XML data modules |

---

## 5. Responsibility Split

```yaml
responsibility_split:
  q_atlantide_impact_study:
    purpose:
      - "programme impact analysis"
      - "architecture-band effect"
      - "risk / opportunity / ESG / lifecycle impact"
      - "Q-Division and ORB ownership"
    not_for:
      - "system descriptions"
      - "technical publication content"
      - "certified design data"

  s1000d_csdb:
    purpose:
      - "authoritative technical publication content"
      - "descriptive, procedural and operational data modules"
      - "CSDB-controlled retrieval and issue management"
      - "reuse across maintenance manuals, IPC, crew procedures"
    governed_by:
      - "BREX rules"
      - "DMRL (Data Module Requirement List)"
      - "SNS alignment"
      - "project configuration control"
```

---

## 6. Current ATLAS-020 Implementation

The first CSDB node implemented is **ATLAS 020 — Air Conditioning and Pressurization** (ATA 21 alignment), consisting of 10 descriptive data modules. See `DMC/ATLAS-020_Air-Conditioning-and-Pressurization/README.md` for the full DMRL-style register.

---

## 7. Governance Boundary

This CSDB directory contains programme-controlled **placeholder** data modules. All content is subject to:

- BREX rule freeze by the programme Configuration Control Board (CCB)
- SNS alignment review by Q-DATAGOV and Q-AIR
- DMRL approval before production release
- Airworthiness authority review for any certified content

This is not a certified publication and must not be used operationally.
