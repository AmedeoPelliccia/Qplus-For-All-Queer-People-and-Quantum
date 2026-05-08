---
document_id: IDEALE-ESG-A-AEROSPACE-I-INFRASTRUCTURES-00-00-SCOPE-PURPOSE
title: "00-00-Scope-and-Purpose — Scope and Purpose"
canonical_path: "IDEALE-ESG/A-Aerospace/I-Infrastructures/00-General/00-00-Scope-and-Purpose.md"
parent_path: "IDEALE-ESG/A-Aerospace/I-Infrastructures/00-General/"
parent_document: "README.md"

domain: "A-Aerospace"
opt_in_axis: "I-Infrastructures"
section: "00-General"
node_code: "00-00"

status: "controlled-candidate"
version: "0.1.0"
revision: "A"
date: "2026-05-08"
language: "en"
classification: "open-technical-taxonomy"

owner: "Q-DATAGOV"
lifecycle_phase: "LC01"
maturity: "taxonomy-definition"

citation_keys:
  - ICAO-ANNEX14
  - EASA-ADR
  - EASA-VERTIPORT
  - FAA-LAUNCH
  - ECSS
  - IAQG-9100
  - ISO-55000

tags:
  - IDEALE-ESG
  - A-Aerospace
  - OPT-IN
  - I-Infrastructures
  - General
  - Scope
  - Purpose
  - Infrastructure-Governance
---

# 00-00-Scope-and-Purpose — Scope and Purpose

## Purpose

Defines the scope and purpose of the `00-General` section within `I-Infrastructures`.

This document establishes the controlled entry point for:

```text
IDEALE-ESG.panpara.eu/A-Aerospace/I-Infrastructures/00-General/
````

It defines what the `I-Infrastructures` axis covers, how infrastructure sections are interpreted, and how references, citations, lifecycle markers, and traceability footprints are applied.

## Parent

[`README.md`](README.md) — `IDEALE-ESG/A-Aerospace/I-Infrastructures/00-General/`

## Scope Statement

`00-General` covers the common governance layer for the `I-Infrastructures` axis within `A-Aerospace`.

It provides:

1. Infrastructure classification rules.
2. Controlled naming conventions.
3. Parent-child path logic.
4. Applicability and effectivity logic.
5. Reference and citation conventions.
6. Lifecycle governance.
7. Traceability and evidence footprints.
8. Interfaces with the other OPT-IN axes.

## Infrastructure Classes Covered

| Code | Section                               | Scope                                                                                                             |
| ---: | ------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `01` | Airports                              | Airport infrastructure for aircraft operation, ground handling, servicing, compatibility, safety, and turnaround. |
| `02` | Vertiports                            | Infrastructure for VTOL, eVTOL, and advanced air mobility operations.                                             |
| `03` | Spaceports and Launchers              | Launch-site, launcher-integration, payload-processing, range-safety, and space-access infrastructure.             |
| `04` | Maintenance Hangars                   | MRO, inspection, tooling, repair, maintenance-access, and airline-support infrastructure.                         |
| `05` | Assemblies and FAL                    | Industrial assembly, major joins, jigs, fixtures, station flow, and final assembly line infrastructure.           |
| `06` | Test and Certification Infrastructure | Ground-test, lab-test, environmental-test, propulsion-test, and certification-evidence infrastructure.            |
| `07` | Hydrogen and Energy Infrastructure    | LH2, cryogenic, refuelling, charging, electrical, and energy-interface infrastructure.                            |
| `08` | Digital Operational Infrastructure    | CSDB, PLM, IETP, digital twin, operational data, ledger, and infrastructure-data governance.                      |
| `09` | Safety, Security and Access Control   | Safety zones, access control, emergency response, physical security, and cyber-physical protection.               |

## Boundary Definition

### Included

This document includes:

* Taxonomy-level scope.
* Infrastructure definitions.
* Classification rules.
* Applicability logic.
* Footprints.
* Citation keys.
* Reference families.
* Lifecycle and governance rules.

### Excluded

This document does not include:

* Detailed civil engineering design.
* Detailed airport master planning.
* Detailed vertiport drawings.
* Detailed launchpad engineering.
* Detailed aircraft or spacecraft product design.
* Maintenance work instructions.
* Production work orders.
* Certification compliance reports.

Those belong in lower-level infrastructure, programme, facility, or certification documents.

## Controlled Definition

For this taxonomy, an aerospace infrastructure is:

> A physical, digital, industrial, or operational asset environment that enables the design, assembly, certification, operation, maintenance, servicing, launch, recovery, or lifecycle support of aerospace systems.

This includes physical assets such as airports, vertiports, spaceports, hangars, launchpads, and final assembly lines, as well as digital assets such as CSDB, PLM, IETP, digital twins, ledgers, and operational data platforms.

---

# Footprints

## Semantic Footprint

```yaml
semantic_footprint:
  id: FP-SEM-I-INFRA-00-00
  subject: "Scope and purpose of aerospace infrastructure taxonomy"
  meaning_boundary:
    includes:
      - infrastructure classification
      - taxonomy governance
      - lifecycle traceability
      - standards mapping
      - evidence architecture
    excludes:
      - detailed engineering design
      - detailed operational procedures
      - product-specific certification data
```

## Taxonomy Footprint

```yaml
taxonomy_footprint:
  id: FP-TAX-I-INFRA-00-00
  hierarchy:
    root: "IDEALE-ESG"
    domain: "A-Aerospace"
    opt_in_axis: "I-Infrastructures"
    section: "00-General"
    document: "00-00-Scope-and-Purpose"
```

## Lifecycle Footprint

```yaml
lifecycle_footprint:
  id: FP-LC-I-INFRA-00-00
  lifecycle_phase: "LC01"
  lifecycle_role: "Concept definition and taxonomy boundary control"
  exit_criteria:
    - scope statement approved
    - parent-child path confirmed
    - infrastructure classes identified
    - reference families mapped
    - traceability convention defined
```

## Compliance Footprint

```yaml
compliance_footprint:
  id: FP-COMP-I-INFRA-00-00
  reference_families:
    aerodromes:
      - "ICAO-ANNEX14"
      - "EASA-ADR"
    vertiports:
      - "EASA-VERTIPORT"
    launch_and_reentry:
      - "FAA-LAUNCH"
      - "ECSS"
    quality_management:
      - "IAQG-9100"
    asset_management:
      - "ISO-55000"
```

## Evidence Footprint

```yaml
evidence_footprint:
  id: FP-EVD-I-INFRA-00-00
  expected_evidence:
    - controlled markdown document
    - YAML frontmatter
    - canonical path
    - parent path
    - scope statement
    - boundary definition
    - references
    - citation keys
    - traceability links
```

---

# OPT-IN Interfaces

| OPT-IN Axis         | Interface with `I-Infrastructures`                                                                                         |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `O-Organizations`   | Infrastructure ownership, operators, authorities, suppliers, maintainers, airport/spaceport/vertiport stakeholders.        |
| `P-Programs`        | Programme-specific infrastructure needs, certification campaigns, FAL planning, MRO deployment, airport compatibility.     |
| `T-Technologies`    | Propulsion, hydrogen, energy, GSE, digital twin, PLM, CSDB, sensor systems, safety systems.                                |
| `I-Infrastructures` | Physical, digital, industrial, and operational asset environments.                                                         |
| `N-Neural-Networks` | Predictive maintenance, operational optimization, digital twin inference, safety monitoring, infrastructure AI governance. |

---

# Citation Map

| Citation Key     | Applies To                                   | Use in This Taxonomy                                                                             |
| ---------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `ICAO-ANNEX14`   | Airports / Aerodromes                        | Aerodrome design and operations baseline.                                                        |
| `EASA-ADR`       | Airports / EU Aerodromes                     | EU aerodrome requirements and administrative procedures.                                         |
| `EASA-VERTIPORT` | Vertiports                                   | Prototype design guidance for VTOL/eVTOL vertiport infrastructure.                               |
| `FAA-LAUNCH`     | Spaceports / Launchers                       | Launch and reentry licensing, safety coordination, and site-interface reference.                 |
| `ECSS`           | Space systems / Launchers / Ground equipment | European space project management, product assurance, and engineering standardization framework. |
| `IAQG-9100`      | Aerospace quality management                 | QMS alignment for aviation, space, and defense organizations.                                    |
| `ISO-55000`      | Asset lifecycle management                   | Infrastructure asset lifecycle, value, risk, and governance principles.                          |

---

# Controlled References

## [ICAO-ANNEX14]

**ICAO Annex 14 — Aerodromes, Volume I, Aerodrome Design and Operations.**

Used as the airport and aerodrome infrastructure reference family for `01-Airports`. ICAO identifies Annex 14 Volume I as covering aerodrome design and operations. ([ICAO Store][1])

## [EASA-ADR]

**EASA Easy Access Rules for Aerodromes — Regulation (EU) No 139/2014.**

Used as the EU aerodrome regulatory and administrative reference family for `01-Airports`. EASA identifies the Easy Access Rules for Aerodromes as the consolidated rule set for aerodromes under Regulation (EU) No 139/2014. ([EASA][2])

## [EASA-VERTIPORT]

**EASA Prototype Technical Design Specifications for Vertiports.**

Used as the vertiport design guidance reference family for `02-Vertiports`. EASA describes the PTS for Vertiports as guidance for safe design of vertiports serving VTOL aircraft. ([EASA][3])

## [FAA-LAUNCH]

**14 CFR Part 450 — Launch and Reentry License Requirements.**

Used as the launch, reentry, licensing, safety, and site-interface reference family for `03-Spaceports-and-Launchers`. The eCFR identifies Part 450 as covering launch and reentry license requirements. ([eCFR][4])

## [ECSS]

**European Cooperation for Space Standardization — ECSS Standards.**

Used as the European space standardization reference family for space infrastructure, launcher interfaces, ground systems, project management, product assurance, and engineering governance. ECSS describes its purpose as developing a coherent set of standards for European space activities. ([Ecss][5])

## [IAQG-9100]

**IAQG 9100 — Quality Management Systems Requirements for Aviation, Space and Defense Organizations.**

Used as the aerospace quality-management reference family for infrastructure suppliers, operators, production systems, maintenance systems, and lifecycle governance. IAQG states that 9100 standardizes QMS requirements across the aviation, space, and defense supply chain. ([IAQG][6])

## [ISO-55000]

**ISO 55000:2024 — Asset Management, Vocabulary, Overview and Principles.**

Used as the asset-management reference family for infrastructure lifecycle, risk, value, and governance principles. ISO identifies ISO 55000:2024 as providing terminology, overview, and principles for asset management. ([ISO][7])

---

# Governance Rule

Any child document under `I-Infrastructures` shall preserve:

1. The parent path.
2. The section code.
3. A controlled YAML frontmatter block.
4. A scope and boundary statement.
5. At least one footprint block.
6. Citation keys when external standards or regulatory references are invoked.
7. Traceability to upstream and downstream taxonomy nodes.

---

# Acceptance Criteria

This document is acceptable when:

* The canonical path is stable.
* The parent-child relation is unambiguous.
* Scope and exclusions are stated.
* Infrastructure classes are enumerated.
* Footprints are present.
* Citation keys are declared.
* References are mapped to their relevant infrastructure classes.
* The document can be reused as a template for lower-level `00-General` files.

---

# Summary

`00-00-Scope-and-Purpose` defines the controlled entry point for the `00-General` section of `I-Infrastructures`.

Its role is not to design the infrastructure directly, but to govern how infrastructure knowledge is classified, referenced, traced, and reused across the IDEALE-ESG / A-Aerospace taxonomy.

```
::contentReference[oaicite:7]{index=7}
```

[1]: https://store.icao.int/en/annex-14-aerodromes?utm_source=chatgpt.com "Annex 14 - Aerodromes - Volume I"
[2]: https://www.easa.europa.eu/en/document-library/easy-access-rules/online-publications/easy-access-rules-aerodromes-regulation-eu?utm_source=chatgpt.com "Easy Access Rules for Aerodromes (Regulation (EU) No 139 ..."
[3]: https://www.easa.europa.eu/en/document-library/general-publications/prototype-technical-design-specifications-vertiports?utm_source=chatgpt.com "Prototype Technical Design Specifications for Vertiports - EASA"
[4]: https://www.ecfr.gov/current/title-14/chapter-III/subchapter-C/part-450?utm_source=chatgpt.com "14 CFR Part 450 -- Launch and Reentry License ..."
[5]: https://ecss.nl/?utm_source=chatgpt.com "| European Cooperation for Space Standardization"
[6]: https://iaqg.org/standard/9100-qms-requirements-for-aviation-space-and-defense-organizations/?utm_source=chatgpt.com "9100 Quality Management Systems – Requirements for ..."
[7]: https://www.iso.org/standard/83053.html?utm_source=chatgpt.com "Asset management - ISO 55000:2024"
