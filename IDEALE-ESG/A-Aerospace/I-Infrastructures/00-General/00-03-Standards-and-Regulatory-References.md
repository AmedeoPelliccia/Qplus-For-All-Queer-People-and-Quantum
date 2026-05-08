---
document_id: IDEALE-ESG-A-AEROSPACE-I-INFRASTRUCTURES-00-03-STANDARDS-AND-REGULATORY-REFERENCES
title: "00-03-Standards-and-Regulatory-References — Standards and Regulatory References"
canonical_path: "IDEALE-ESG/A-Aerospace/I-Infrastructures/00-General/00-03-Standards-and-Regulatory-References.md"
parent_path: "IDEALE-ESG/A-Aerospace/I-Infrastructures/00-General/"
parent_document: "README.md"

domain: "A-Aerospace"
opt_in_axis: "I-Infrastructures"
section: "00-General"
node_code: "00-03"

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
  - EASA-CS-ADR-DSN
  - EASA-VERTIPORT
  - FAA-PART-450
  - FAA-PART-139
  - ECSS
  - IAQG-9100
  - ISO-9001
  - ISO-55000
  - ISO-31000
  - ISO-19880-1
  - NFPA-2
  - ISO-IEC-IEEE-15288

tags:
  - IDEALE-ESG
  - A-Aerospace
  - OPT-IN
  - I-Infrastructures
  - General
  - Standards
  - Regulatory-References
  - Compliance
  - Infrastructure-Governance
---
---

# 00-03-Standards-and-Regulatory-References — Standards and Regulatory References

## Purpose

Applicable standards, regulations, and normative references for aerospace infrastructure.

This document establishes the controlled standards and regulatory reference map for the `I-Infrastructures` taxonomy under:

```text
IDEALE-ESG/A-Aerospace/I-Infrastructures/00-General/
```

## Parent

[`README.md`](README.md) — `IDEALE-ESG/A-Aerospace/I-Infrastructures/00-General/`

---

# 1. Reference Scope

This document identifies external standards, regulations, guidance documents, and normative reference families applicable to aerospace infrastructure classification.

It supports the following infrastructure sections:

| Code | Section                               | Reference Scope                                                                                                                      |
| ---: | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `01` | Airports                              | Aerodrome design, airport certification, operations, safety, and infrastructure compatibility.                                       |
| `02` | Vertiports                            | VTOL/eVTOL vertiport design, safe layout, passenger interfaces, and energy interfaces.                                               |
| `03` | Spaceports and Launchers              | Launch/reentry licensing, launch-site safety, space systems standards, payload processing, range safety, and mission infrastructure. |
| `04` | Maintenance Hangars                   | MRO infrastructure, safety, quality, tooling, access control, and maintenance-support environments.                                  |
| `05` | Assemblies and FAL                    | Industrial production infrastructure, quality management, assembly flow, configuration control, and lifecycle evidence.              |
| `06` | Test and Certification Infrastructure | Ground test, certification evidence, verification, validation, qualification, and compliance substantiation.                         |
| `07` | Hydrogen and Energy Infrastructure    | Hydrogen storage, cryogenic systems, refuelling, charging, safety, emergency response, and energy delivery.                          |
| `08` | Digital Operational Infrastructure    | CSDB, PLM, IETP, digital twin, system lifecycle, data governance, and evidence repositories.                                         |
| `09` | Safety, Security and Access Control   | Hazard control, emergency response, risk management, physical security, cyber-physical protection, and restricted areas.             |

---

# 2. Reference Classification Rules

## RULE-I-INFRA-REF-001 — Authoritative Source Rule

Regulatory and standards references shall be taken from authoritative sources whenever possible.

Preferred source hierarchy:

1. regulatory authority;
2. standardization body;
3. official publisher;
4. recognized industry body;
5. secondary explanatory source.

## RULE-I-INFRA-REF-002 — Citation Key Rule

Every external reference used in this taxonomy shall be assigned a controlled citation key.

Example:

```yaml
citation_key: "EASA-ADR"
reference_family: "Aerodromes"
applies_to:
  - "01-Airports"
```

## RULE-I-INFRA-REF-003 — Reference Family Rule

References shall be grouped by reference family.

Reference families include:

* aerodrome references;
* vertiport references;
* launch and reentry references;
* space standardization references;
* quality-management references;
* asset-management references;
* risk-management references;
* hydrogen and energy references;
* systems lifecycle references;
* digital-operational references.

## RULE-I-INFRA-REF-004 — Applicability Rule

A reference shall not be treated as universally applicable.

Each reference shall declare:

1. applicable infrastructure section;
2. reference role;
3. regulatory or non-regulatory status;
4. jurisdiction, if applicable;
5. lifecycle relevance;
6. limitations.

## RULE-I-INFRA-REF-005 — No False Compliance Rule

A taxonomy reference shall not imply compliance by itself.

Classification under this taxonomy does not mean that a facility, asset, programme, or operator is compliant with the referenced regulation or standard.

Compliance requires programme-specific evidence, authority engagement, and applicable means of compliance.

## RULE-I-INFRA-REF-006 — Current-Version Awareness Rule

Standards and regulations may change.

Each controlled document shall record the date of reference review and avoid hard-coding obsolete revision assumptions unless the programme explicitly baselines a specific edition.

---

# 3. Controlled Reference Families

## 3.1 Aerodrome and Airport References

| Citation Key      | Reference                                                                    | Primary Use                                                                                    |
| ----------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `ICAO-ANNEX14`    | ICAO Annex 14 — Aerodromes, Volume I, Aerodrome Design and Operations        | Baseline aerodrome design and operations reference family.                                     |
| `EASA-ADR`        | EASA Easy Access Rules for Aerodromes, Regulation (EU) No 139/2014           | EU aerodrome rules, administrative procedures, certification, and operations reference family. |
| `EASA-CS-ADR-DSN` | EASA Certification Specifications and Guidance Material for Aerodrome Design | Aerodrome design certification specification reference family.                                 |
| `FAA-PART-139`    | 14 CFR Part 139 — Certification of Airports                                  | US airport certification reference family.                                                     |

## 3.2 Vertiport References

| Citation Key     | Reference                                                     | Primary Use                                                                       |
| ---------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `EASA-VERTIPORT` | EASA Prototype Technical Design Specifications for Vertiports | Prototype technical design guidance for vertiports serving VTOL-capable aircraft. |

## 3.3 Spaceport, Launcher, and Space Infrastructure References

| Citation Key   | Reference                                                 | Primary Use                                                                                                           |
| -------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `FAA-PART-450` | 14 CFR Part 450 — Launch and Reentry License Requirements | Launch and reentry licensing, safety, and operational-control reference family.                                       |
| `ECSS`         | European Cooperation for Space Standardization standards  | European space systems engineering, product assurance, project management, and space infrastructure reference family. |

## 3.4 Quality and Industrial Infrastructure References

| Citation Key | Reference                                                                  | Primary Use                                           |
| ------------ | -------------------------------------------------------------------------- | ----------------------------------------------------- |
| `IAQG-9100`  | IAQG 9100 — QMS Requirements for Aviation, Space and Defense Organizations | Aerospace quality-management system reference family. |
| `ISO-9001`   | ISO 9001 — Quality Management Systems Requirements                         | General quality-management system reference family.   |

## 3.5 Asset, Risk, and Lifecycle References

| Citation Key         | Reference                                                                          | Primary Use                                                                   |
| -------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `ISO-55000`          | ISO 55000:2024 — Asset Management, Vocabulary, Overview and Principles             | Infrastructure asset lifecycle, value, risk, and governance reference family. |
| `ISO-31000`          | ISO 31000:2018 — Risk Management Guidelines                                        | Risk-management and hazard-control reference family.                          |
| `ISO-IEC-IEEE-15288` | ISO/IEC/IEEE 15288 — Systems and Software Engineering, System Life Cycle Processes | System lifecycle and process reference family.                                |

## 3.6 Hydrogen and Energy Infrastructure References

| Citation Key  | Reference                                        | Primary Use                                                                                                             |
| ------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `ISO-19880-1` | ISO 19880-1 — Gaseous Hydrogen Fuelling Stations | Hydrogen fuelling-station design, installation, commissioning, operation, inspection, and maintenance reference family. |
| `NFPA-2`      | NFPA 2 — Hydrogen Technologies Code              | Hydrogen generation, installation, storage, piping, use, and handling safety reference family.                          |

---

# 4. Section-to-Reference Matrix

| Section | Infrastructure Class                  | Primary References                                            | Supporting References                                       |
| ------: | ------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------- |
|    `01` | Airports                              | `ICAO-ANNEX14`, `EASA-ADR`, `EASA-CS-ADR-DSN`, `FAA-PART-139` | `ISO-55000`, `ISO-31000`, `IAQG-9100`                       |
|    `02` | Vertiports                            | `EASA-VERTIPORT`                                              | `ISO-55000`, `ISO-31000`, `ISO-19880-1`, `NFPA-2`           |
|    `03` | Spaceports and Launchers              | `FAA-PART-450`, `ECSS`                                        | `ISO-31000`, `ISO-55000`, `ISO-IEC-IEEE-15288`, `IAQG-9100` |
|    `04` | Maintenance Hangars                   | `IAQG-9100`, `ISO-9001`                                       | `ISO-55000`, `ISO-31000`, `ISO-IEC-IEEE-15288`              |
|    `05` | Assemblies and FAL                    | `IAQG-9100`, `ISO-9001`                                       | `ISO-55000`, `ISO-IEC-IEEE-15288`, `ISO-31000`              |
|    `06` | Test and Certification Infrastructure | `ECSS`, `IAQG-9100`, `ISO-IEC-IEEE-15288`                     | `ISO-9001`, `ISO-31000`, `ISO-55000`                        |
|    `07` | Hydrogen and Energy Infrastructure    | `ISO-19880-1`, `NFPA-2`                                       | `ISO-31000`, `ISO-55000`, `EASA-ADR`, `EASA-VERTIPORT`      |
|    `08` | Digital Operational Infrastructure    | `ISO-IEC-IEEE-15288`, `IAQG-9100`, `ISO-9001`                 | `ISO-55000`, `ISO-31000`                                    |
|    `09` | Safety, Security and Access Control   | `ISO-31000`, `NFPA-2`, `FAA-PART-450`, `EASA-ADR`             | `ISO-55000`, `ISO-IEC-IEEE-15288`                           |

---

# 5. Controlled References

## [ICAO-ANNEX14]

**Reference:** ICAO Annex 14 — Aerodromes, Volume I, Aerodrome Design and Operations.

**Type:** International civil aviation standard and recommended practices reference family.

**Primary Section:** `01-Airports`

**Use in this taxonomy:** Used as the baseline reference family for airport and aerodrome infrastructure classification, including aerodrome design and operational infrastructure. ICAO identifies Annex 14 Volume I as addressing aerodrome design and operations. ([store.icao.int][1])

**Reference Role:**

```yaml
reference_role:
  citation_key: "ICAO-ANNEX14"
  applies_to:
    - "01-Airports"
  role:
    - "aerodrome design reference"
    - "aerodrome operations reference"
    - "airport infrastructure classification support"
  regulatory_status: "ICAO reference family; local legal applicability depends on national implementation"
```

## [EASA-ADR]

**Reference:** EASA Easy Access Rules for Aerodromes — Regulation (EU) No 139/2014.

**Type:** EU aerodrome regulatory reference family.

**Primary Section:** `01-Airports`

**Use in this taxonomy:** Used for EU airport and aerodrome infrastructure governance, aerodrome operator requirements, certification logic, and administrative procedures. EASA describes the Easy Access Rules for Aerodromes as containing applicable aerodrome rules in a consolidated, easy-to-read format; the March 2026 revision is identified by EASA as the current published revision. ([EASA][2])

**Reference Role:**

```yaml
reference_role:
  citation_key: "EASA-ADR"
  applies_to:
    - "01-Airports"
    - "09-Safety-Security-and-Access-Control"
  role:
    - "EU aerodrome rule reference"
    - "aerodrome certification support"
    - "aerodrome operations governance"
  jurisdiction: "European Union / EASA system"
```

## [EASA-CS-ADR-DSN]

**Reference:** EASA Certification Specifications and Guidance Material for Aerodrome Design.

**Type:** Aerodrome design certification specification reference family.

**Primary Section:** `01-Airports`

**Use in this taxonomy:** Used as an aerodrome design reference family for infrastructure elements such as runways, taxiways, aprons, obstacle environments, physical characteristics, and related aerodrome infrastructure design controls.

**Reference Role:**

```yaml
reference_role:
  citation_key: "EASA-CS-ADR-DSN"
  applies_to:
    - "01-Airports"
  role:
    - "aerodrome design specification support"
    - "airport physical infrastructure classification"
    - "design certification support"
  jurisdiction: "European Union / EASA system"
```

## [EASA-VERTIPORT]

**Reference:** EASA Prototype Technical Design Specifications for Vertiports.

**Type:** Non-regulatory prototype technical design guidance.

**Primary Section:** `02-Vertiports`

**Use in this taxonomy:** Used as the primary vertiport infrastructure reference family for safe VTOL/eVTOL vertiport design classification. EASA describes the document as guidance for urban planners, local decision-makers, and industry to enable safe design of vertiports for vertical take-off and landing aircraft. ([EASA][3])

**Reference Role:**

```yaml
reference_role:
  citation_key: "EASA-VERTIPORT"
  applies_to:
    - "02-Vertiports"
  role:
    - "vertiport design guidance"
    - "VTOL/eVTOL infrastructure classification"
    - "advanced air mobility infrastructure support"
  regulatory_status: "prototype technical design specification; non-regulatory unless adopted by authority or programme"
```

## [FAA-PART-139]

**Reference:** 14 CFR Part 139 — Certification of Airports.

**Type:** US airport certification regulation.

**Primary Section:** `01-Airports`

**Use in this taxonomy:** Used as a US airport certification reference family for airport infrastructure, airport operating certificates, safety, and operational controls.

**Reference Role:**

```yaml
reference_role:
  citation_key: "FAA-PART-139"
  applies_to:
    - "01-Airports"
  role:
    - "US airport certification reference"
    - "airport operations and safety classification"
    - "airport infrastructure governance support"
  jurisdiction: "United States / FAA"
```

## [FAA-PART-450]

**Reference:** 14 CFR Part 450 — Launch and Reentry License Requirements.

**Type:** US commercial space launch and reentry regulation.

**Primary Section:** `03-Spaceports-and-Launchers`

**Use in this taxonomy:** Used as the launch and reentry reference family for spaceport, launcher, launch-site safety, operational readiness, and reentry infrastructure classification. The eCFR states that Part 450 prescribes requirements for obtaining and maintaining a license to launch, reenter, or both launch and reenter a launch or reentry vehicle. ([ecfr.gov][4])

**Reference Role:**

```yaml
reference_role:
  citation_key: "FAA-PART-450"
  applies_to:
    - "03-Spaceports-and-Launchers"
    - "09-Safety-Security-and-Access-Control"
  role:
    - "launch licensing reference"
    - "reentry licensing reference"
    - "range safety and operational control support"
  jurisdiction: "United States / FAA Commercial Space Transportation"
```

## [ECSS]

**Reference:** European Cooperation for Space Standardization standards.

**Type:** European space standardization reference family.

**Primary Section:** `03-Spaceports-and-Launchers`

**Use in this taxonomy:** Used as the European reference family for space project management, product assurance, engineering, ground systems, and space infrastructure governance. ECSS describes itself as developing a coherent set of user-friendly standards for use in European space activities. ([ecss.nl][5])

**Reference Role:**

```yaml
reference_role:
  citation_key: "ECSS"
  applies_to:
    - "03-Spaceports-and-Launchers"
    - "06-Test-and-Certification-Infrastructure"
    - "08-Digital-Operational-Infrastructure"
  role:
    - "space systems engineering reference"
    - "space product assurance reference"
    - "space project management reference"
    - "ground systems and launch infrastructure support"
  jurisdiction: "European space standardization framework"
```

## [IAQG-9100]

**Reference:** IAQG 9100 — Quality Management Systems Requirements for Aviation, Space and Defense Organizations.

**Type:** Aerospace quality-management system standard.

**Primary Sections:** `04-Maintenance-Hangars`, `05-Assemblies-and-FAL`, `06-Test-and-Certification-Infrastructure`

**Use in this taxonomy:** Used as the aviation, space, and defense QMS reference family for infrastructure suppliers, operators, production systems, maintenance systems, assembly systems, test infrastructure, and lifecycle quality governance. IAQG describes 9100 as standardizing QMS requirements across the supply chain for aviation, space, and defense organizations. ([iaqg.org][6])

**Reference Role:**

```yaml
reference_role:
  citation_key: "IAQG-9100"
  applies_to:
    - "04-Maintenance-Hangars"
    - "05-Assemblies-and-FAL"
    - "06-Test-and-Certification-Infrastructure"
    - "08-Digital-Operational-Infrastructure"
  role:
    - "aerospace QMS reference"
    - "production infrastructure governance"
    - "maintenance infrastructure governance"
    - "supplier quality infrastructure support"
```

## [ISO-9001]

**Reference:** ISO 9001 — Quality Management Systems Requirements.

**Type:** General quality-management system standard.

**Primary Sections:** `04-Maintenance-Hangars`, `05-Assemblies-and-FAL`, `08-Digital-Operational-Infrastructure`

**Use in this taxonomy:** Used as a general QMS reference family for infrastructure organizations, suppliers, operators, maintainers, and support functions. ISO describes ISO 9001 as defining requirements to establish, implement, maintain, and continually improve a quality management system. ([ISO][7])

**Reference Role:**

```yaml
reference_role:
  citation_key: "ISO-9001"
  applies_to:
    - "04-Maintenance-Hangars"
    - "05-Assemblies-and-FAL"
    - "06-Test-and-Certification-Infrastructure"
    - "08-Digital-Operational-Infrastructure"
  role:
    - "general QMS reference"
    - "organizational process control"
    - "continuous improvement support"
```

## [ISO-55000]

**Reference:** ISO 55000:2024 — Asset Management, Vocabulary, Overview and Principles.

**Type:** Asset-management standard.

**Primary Sections:** All `I-Infrastructures` sections.

**Use in this taxonomy:** Used as the asset-management reference family for infrastructure lifecycle governance, asset value, risk, and asset-management principles. ISO describes ISO 55000:2024 as providing overview, terminology, and principles for asset management. ([ISO][8])

**Reference Role:**

```yaml
reference_role:
  citation_key: "ISO-55000"
  applies_to:
    - "01-Airports"
    - "02-Vertiports"
    - "03-Spaceports-and-Launchers"
    - "04-Maintenance-Hangars"
    - "05-Assemblies-and-FAL"
    - "06-Test-and-Certification-Infrastructure"
    - "07-Hydrogen-and-Energy-Infrastructure"
    - "08-Digital-Operational-Infrastructure"
    - "09-Safety-Security-and-Access-Control"
  role:
    - "asset lifecycle governance"
    - "infrastructure value management"
    - "asset-management principles"
```

## [ISO-31000]

**Reference:** ISO 31000:2018 — Risk Management Guidelines.

**Type:** Risk-management standard.

**Primary Sections:** `09-Safety-Security-and-Access-Control`, all safety-relevant infrastructure sections.

**Use in this taxonomy:** Used as the risk-management reference family for hazard identification, risk evaluation, treatment, monitoring, and governance. ISO identifies ISO 31000 as providing principles and guidelines for risk management. ([ISO][9])

**Reference Role:**

```yaml
reference_role:
  citation_key: "ISO-31000"
  applies_to:
    - "01-Airports"
    - "02-Vertiports"
    - "03-Spaceports-and-Launchers"
    - "04-Maintenance-Hangars"
    - "05-Assemblies-and-FAL"
    - "06-Test-and-Certification-Infrastructure"
    - "07-Hydrogen-and-Energy-Infrastructure"
    - "08-Digital-Operational-Infrastructure"
    - "09-Safety-Security-and-Access-Control"
  role:
    - "risk-management reference"
    - "hazard-control support"
    - "safety and security governance"
```

## [ISO-19880-1]

**Reference:** ISO 19880-1 — Gaseous Hydrogen Fuelling Stations.

**Type:** Hydrogen fuelling-station standard.

**Primary Section:** `07-Hydrogen-and-Energy-Infrastructure`

**Use in this taxonomy:** Used as a hydrogen fuelling-station reference family for design, installation, commissioning, operation, inspection, and maintenance considerations. ISO describes ISO 19880-1 as defining minimum requirements for safety and, where appropriate, performance of hydrogen fuelling stations. ([ISO][10])

**Reference Role:**

```yaml
reference_role:
  citation_key: "ISO-19880-1"
  applies_to:
    - "07-Hydrogen-and-Energy-Infrastructure"
    - "09-Safety-Security-and-Access-Control"
  role:
    - "hydrogen fuelling-station reference"
    - "hydrogen safety support"
    - "energy infrastructure classification"
  limitation: "Primarily targeted to gaseous hydrogen fuelling stations; LH2 aerospace applications require programme-specific assessment."
```

## [NFPA-2]

**Reference:** NFPA 2 — Hydrogen Technologies Code.

**Type:** Hydrogen safety code.

**Primary Section:** `07-Hydrogen-and-Energy-Infrastructure`

**Use in this taxonomy:** Used as a hydrogen safety reference family for generation, installation, storage, piping, use, and handling of hydrogen. NFPA describes NFPA 2 as providing safeguards for hydrogen in compressed gas and cryogenic liquid forms. ([NFPA][11])

**Reference Role:**

```yaml
reference_role:
  citation_key: "NFPA-2"
  applies_to:
    - "07-Hydrogen-and-Energy-Infrastructure"
    - "09-Safety-Security-and-Access-Control"
  role:
    - "hydrogen safety code"
    - "compressed hydrogen safeguard reference"
    - "cryogenic liquid hydrogen safeguard reference"
    - "hazard zoning support"
  jurisdiction: "Code applicability depends on local adoption and authority having jurisdiction."
```

## [ISO-IEC-IEEE-15288]

**Reference:** ISO/IEC/IEEE 15288 — Systems and Software Engineering, System Life Cycle Processes.

**Type:** Systems lifecycle standard.

**Primary Sections:** `06-Test-and-Certification-Infrastructure`, `08-Digital-Operational-Infrastructure`

**Use in this taxonomy:** Used as the lifecycle-process reference family for infrastructure systems, digital systems, evidence systems, systems-of-interest, and lifecycle-controlled engineering processes. ISO describes ISO/IEC/IEEE 15288 as establishing a common framework of process descriptions for systems created by humans. ([ISO][12])

**Reference Role:**

```yaml
reference_role:
  citation_key: "ISO-IEC-IEEE-15288"
  applies_to:
    - "06-Test-and-Certification-Infrastructure"
    - "08-Digital-Operational-Infrastructure"
    - "05-Assemblies-and-FAL"
  role:
    - "system lifecycle process reference"
    - "verification and validation lifecycle support"
    - "digital operational infrastructure process support"
```

---

# 6. Regulatory Applicability Notes

## 6.1 Jurisdiction Control

A reference shall be treated as jurisdiction-specific when issued by a regulatory authority.

Examples:

| Reference      | Jurisdiction                                               |
| -------------- | ---------------------------------------------------------- |
| `EASA-ADR`     | European Union / EASA system                               |
| `FAA-PART-139` | United States / FAA airport certification system           |
| `FAA-PART-450` | United States / FAA commercial space transportation system |

## 6.2 Standards vs Regulations

This taxonomy distinguishes between:

| Type                        | Meaning                                                                                                                                   |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Regulation                  | Legally enforceable when applicable in the relevant jurisdiction.                                                                         |
| Certification Specification | Technical specification used for compliance demonstration or accepted design basis within a regulatory system.                            |
| Standard                    | Consensus or organizational standard that may become mandatory through contract, certification basis, procurement, or authority adoption. |
| Guidance                    | Non-binding material unless adopted by a programme, authority, contract, or internal governance rule.                                     |
| Reference Family            | A controlled group of references used to support taxonomy classification, not automatic compliance.                                       |

## 6.3 Programme-Specific Compliance

Programme-specific compliance shall be established outside this taxonomy document.

Required compliance evidence may include:

* certification basis;
* means of compliance;
* issue papers;
* special conditions;
* authority correspondence;
* test plans;
* safety assessments;
* conformity records;
* inspection records;
* verification matrices;
* quality records;
* operational approvals.

---

# 7. Reference Record Template

Each future infrastructure document should use the following reference record pattern when invoking external references:

```yaml
reference_record:
  citation_key: ""
  reference_title: ""
  reference_type: ""
  issuing_body: ""
  jurisdiction: ""
  applicable_sections:
    - ""
  reference_role:
    - ""
  regulatory_status: ""
  lifecycle_relevance:
    - ""
  limitation: ""
  reviewed_on: "2026-05-08"
```

---

# 8. Applicability Template

Each child document may include the following applicability block:

```yaml
applicability:
  infrastructure_section: ""
  infrastructure_asset_type: ""
  jurisdiction:
    - ""
  reference_families:
    - citation_key: ""
      applicability: ""
      status: ""
  compliance_note: >
    The reference is used for taxonomy classification and standards mapping.
    It does not, by itself, constitute compliance demonstration.
```

---

# 9. Footprints

## Semantic Footprint

```yaml
semantic_footprint:
  id: FP-SEM-I-INFRA-00-03
  subject: "Standards and regulatory references for aerospace infrastructure taxonomy"
  meaning_boundary:
    includes:
      - standards mapping
      - regulatory reference mapping
      - citation keys
      - reference families
      - applicability notes
      - jurisdiction logic
    excludes:
      - full compliance demonstration
      - legal interpretation
      - authority-approved certification basis
      - programme-specific means of compliance
```

## Taxonomy Footprint

```yaml
taxonomy_footprint:
  id: FP-TAX-I-INFRA-00-03
  hierarchy:
    root: "IDEALE-ESG"
    domain: "A-Aerospace"
    opt_in_axis: "I-Infrastructures"
    section: "00-General"
    document: "00-03-Standards-and-Regulatory-References"
```

## Lifecycle Footprint

```yaml
lifecycle_footprint:
  id: FP-LC-I-INFRA-00-03
  lifecycle_phase: "LC01"
  lifecycle_role: "Standards and regulatory reference mapping"
  exit_criteria:
    - reference families identified
    - citation keys declared
    - section-to-reference matrix established
    - regulatory applicability notes included
    - reference record template provided
```

## Compliance Footprint

```yaml
compliance_footprint:
  id: FP-COMP-I-INFRA-00-03
  reference_families:
    aerodromes:
      - "ICAO-ANNEX14"
      - "EASA-ADR"
      - "EASA-CS-ADR-DSN"
      - "FAA-PART-139"
    vertiports:
      - "EASA-VERTIPORT"
    launch_and_reentry:
      - "FAA-PART-450"
      - "ECSS"
    quality_management:
      - "IAQG-9100"
      - "ISO-9001"
    asset_management:
      - "ISO-55000"
    risk_management:
      - "ISO-31000"
    hydrogen_and_energy:
      - "ISO-19880-1"
      - "NFPA-2"
    system_lifecycle:
      - "ISO-IEC-IEEE-15288"
```

## Evidence Footprint

```yaml
evidence_footprint:
  id: FP-EVD-I-INFRA-00-03
  expected_evidence:
    - controlled markdown document
    - YAML frontmatter
    - canonical path
    - parent path
    - citation keys
    - standards map
    - regulatory reference map
    - section-to-reference matrix
    - applicability notes
    - reference record template
```

---

# 10. Citation Map

| Citation Key         | Applies To                                                                                                         | Use in This Taxonomy                                               |
| -------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `ICAO-ANNEX14`       | `01-Airports`                                                                                                      | Aerodrome design and operations reference family.                  |
| `EASA-ADR`           | `01-Airports`, `09-Safety-Security-and-Access-Control`                                                             | EU aerodrome rules and administrative procedures reference family. |
| `EASA-CS-ADR-DSN`    | `01-Airports`                                                                                                      | Aerodrome design certification specification reference family.     |
| `EASA-VERTIPORT`     | `02-Vertiports`                                                                                                    | Vertiport design guidance reference family.                        |
| `FAA-PART-139`       | `01-Airports`                                                                                                      | US airport certification reference family.                         |
| `FAA-PART-450`       | `03-Spaceports-and-Launchers`, `09-Safety-Security-and-Access-Control`                                             | Launch and reentry licensing reference family.                     |
| `ECSS`               | `03-Spaceports-and-Launchers`, `06-Test-and-Certification-Infrastructure`, `08-Digital-Operational-Infrastructure` | European space standardization reference family.                   |
| `IAQG-9100`          | `04-Maintenance-Hangars`, `05-Assemblies-and-FAL`, `06-Test-and-Certification-Infrastructure`                      | Aerospace QMS reference family.                                    |
| `ISO-9001`           | `04-Maintenance-Hangars`, `05-Assemblies-and-FAL`, `08-Digital-Operational-Infrastructure`                         | General QMS reference family.                                      |
| `ISO-55000`          | All sections                                                                                                       | Asset-management reference family.                                 |
| `ISO-31000`          | All safety-relevant sections                                                                                       | Risk-management reference family.                                  |
| `ISO-19880-1`        | `07-Hydrogen-and-Energy-Infrastructure`                                                                            | Hydrogen fuelling-station reference family.                        |
| `NFPA-2`             | `07-Hydrogen-and-Energy-Infrastructure`, `09-Safety-Security-and-Access-Control`                                   | Hydrogen safety-code reference family.                             |
| `ISO-IEC-IEEE-15288` | `06-Test-and-Certification-Infrastructure`, `08-Digital-Operational-Infrastructure`                                | System lifecycle-process reference family.                         |

---

# 11. Governance Rule

Any child document under `I-Infrastructures` that invokes external standards or regulations shall include:

1. citation key;
2. reference title;
3. reference family;
4. applicable infrastructure section;
5. jurisdiction, if applicable;
6. reference role;
7. regulatory or non-regulatory status;
8. limitation statement;
9. review date;
10. traceability to this document.

No child document shall claim regulatory compliance solely because a reference appears in this taxonomy.

---

# 12. Acceptance Criteria

This document is acceptable when:

* standards and regulatory references are grouped by reference family;
* citation keys are declared;
* each reference has a controlled role;
* jurisdiction-specific references are identified;
* section-to-reference mapping is established;
* applicability limitations are stated;
* compliance is not overstated;
* child documents can reuse the citation keys without redefining the reference family.

---

# 13. Summary

`00-03-Standards-and-Regulatory-References` defines the controlled standards and regulatory reference map for the `I-Infrastructures` axis.

It supports consistent classification, citation, applicability control, and lifecycle governance across airports, vertiports, spaceports, launchers, maintenance hangars, assemblies, FAL environments, test infrastructure, hydrogen and energy systems, digital operational infrastructure, and safety/security infrastructure.

[1]: https://store.icao.int/en/annex-14-aerodromes?utm_source=chatgpt.com "Annex 14 - Aerodromes - Volume I"
[2]: https://www.easa.europa.eu/en/document-library/easy-access-rules/easy-access-rules-aerodromes?utm_source=chatgpt.com "Easy Access Rules for Aerodromes - Revision from March 2026"
[3]: https://www.easa.europa.eu/en/document-library/general-publications/prototype-technical-design-specifications-vertiports?utm_source=chatgpt.com "Prototype Technical Design Specifications for Vertiports - EASA"
[4]: https://www.ecfr.gov/current/title-14/chapter-III/subchapter-C/part-450?utm_source=chatgpt.com "14 CFR Part 450 -- Launch and Reentry License ..."
[5]: https://ecss.nl/?utm_source=chatgpt.com "| European Cooperation for Space Standardization"
[6]: https://iaqg.org/standard/9100-qms-requirements-for-aviation-space-and-defense-organizations/?utm_source=chatgpt.com "9100 Quality Management Systems – Requirements for ..."
[7]: https://www.iso.org/standard/62085.html?utm_source=chatgpt.com "ISO 9001:2015 - Quality management systems"
[8]: https://www.iso.org/standard/83053.html?utm_source=chatgpt.com "Asset management - ISO 55000:2024"
[9]: https://www.iso.org/standard/65694.html?utm_source=chatgpt.com "ISO 31000:2018 - Risk management — Guidelines"
[10]: https://www.iso.org/obp/ui/es/?utm_source=chatgpt.com "ISO 19880-1:2020(en), Gaseous hydrogen"
[11]: https://www.nfpa.org/product/nfpa-2-hydrogen-technologies-code/p0002code?utm_source=chatgpt.com "NFPA 2, Hydrogen Technologies Code (2026)"
[12]: https://www.iso.org/standard/63711.html?utm_source=chatgpt.com "ISO/IEC/IEEE 15288:2015 - Systems and software ..."
