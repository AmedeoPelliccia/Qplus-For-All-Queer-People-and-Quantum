---
document_id: IDEALE-ESG-A-AEROSPACE-I-INFRASTRUCTURES-00-04-APPLICABILITY-AND-EFFECTIVITY
title: "00-04-Applicability-and-Effectivity — Applicability and Effectivity"
canonical_path: "IDEALE-ESG/A-Aerospace/I-Infrastructures/00-General/00-04-Applicability-and-Effectivity.md"
parent_path: "IDEALE-ESG/A-Aerospace/I-Infrastructures/00-General/"
parent_document: "README.md"

domain: "A-Aerospace"
opt_in_axis: "I-Infrastructures"
section: "00-General"
node_code: "00-04"

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
  - FAA-PART-139
  - FAA-PART-450
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
  - Applicability
  - Effectivity
  - Infrastructure-Governance
  - Asset-Scope
  - Programme-Scope
---

# 00-04-Applicability-and-Effectivity — Applicability and Effectivity

## Purpose

Applicability matrix and effectivity rules governing which assets and programmes are in scope.

This document defines how applicability and effectivity shall be assigned, controlled, and traced across the `I-Infrastructures` taxonomy under:

```text
IDEALE-ESG/A-Aerospace/I-Infrastructures/00-General/
```

## Parent

[`README.md`](README.md) — `IDEALE-ESG/A-Aerospace/I-Infrastructures/00-General/`

---

# 1. Applicability and Effectivity Principle

Applicability defines **where a document, rule, reference, classification, or infrastructure element applies**.

Effectivity defines **the exact asset, configuration, programme, facility, version, timeframe, jurisdiction, or operational condition to which it applies**.

Applicability answers:

```text
Does this taxonomy item apply?
```

Effectivity answers:

```text
To which exact item, configuration, period, or condition does it apply?
```

---

# 2. Controlled Definitions

## 2.1 Applicability

**Applicability** is the set of conditions under which a taxonomy document, classification rule, reference, standard, infrastructure asset, or lifecycle control is valid for use.

Applicability may be defined by:

- infrastructure section;
- asset type;
- programme;
- facility;
- jurisdiction;
- lifecycle phase;
- operational context;
- technology interface;
- digital system;
- safety or security condition.

## 2.2 Effectivity

**Effectivity** is the controlled identification of the specific asset, configuration, programme, facility, version, serial number, date range, operational condition, or jurisdiction to which a document, rule, reference, or infrastructure classification applies.

Effectivity may be defined by:

- asset ID;
- facility ID;
- programme ID;
- configuration baseline;
- lifecycle phase;
- date range;
- version;
- jurisdiction;
- operator;
- infrastructure class;
- operational state.

## 2.3 Applicability Matrix

An **applicability matrix** is a controlled table that maps infrastructure sections, assets, programmes, references, lifecycle phases, and jurisdictions to their applicable scope.

## 2.4 Effectivity Record

An **effectivity record** is a controlled data block that states the exact effectivity conditions for a document, asset, infrastructure element, reference, or classification decision.

---

# 3. Applicability Classes

Applicability shall be classified using the following classes:

| Applicability Class | Meaning |
|---|---|
| `GLOBAL-INFRA` | Applies across all `I-Infrastructures` sections. |
| `SECTION-SPECIFIC` | Applies only to one infrastructure section. |
| `ASSET-SPECIFIC` | Applies only to identified infrastructure assets. |
| `PROGRAMME-SPECIFIC` | Applies only to one or more programmes. |
| `FACILITY-SPECIFIC` | Applies only to one or more physical facilities. |
| `JURISDICTION-SPECIFIC` | Applies only within a defined regulatory or national jurisdiction. |
| `TECHNOLOGY-SPECIFIC` | Applies only when a given technology is present. |
| `DIGITAL-SYSTEM-SPECIFIC` | Applies only to a digital infrastructure system or data environment. |
| `LIFECYCLE-SPECIFIC` | Applies only during defined lifecycle phases. |
| `CONFIGURATION-SPECIFIC` | Applies only to a defined configuration baseline. |
| `OPERATIONAL-CONDITION-SPECIFIC` | Applies only under defined operating states or conditions. |

---

# 4. Infrastructure Applicability Matrix

| Section | Infrastructure Class | Default Applicability |
|---:|---|---|
| `00` | General | Applies to all `I-Infrastructures` sections unless explicitly limited. |
| `01` | Airports | Applies to airport, aerodrome, runway, taxiway, apron, terminal, stand, GSE, and airport-side operational infrastructure. |
| `02` | Vertiports | Applies to VTOL/eVTOL, AAM, UAM, vertiport pad, FATO, TLOF, charging, passenger-access, and urban air mobility infrastructure. |
| `03` | Spaceports and Launchers | Applies to launch pads, launch complexes, launcher integration, payload processing, range safety, reentry, recovery, and mission-support infrastructure. |
| `04` | Maintenance Hangars | Applies to MRO, inspection, maintenance bays, repair cells, tooling, access platforms, hangar support, and return-to-service infrastructure. |
| `05` | Assemblies and FAL | Applies to industrial assembly, major joins, jigging, fixtures, production stations, station flow, and final assembly line infrastructure. |
| `06` | Test and Certification Infrastructure | Applies to test rigs, laboratories, ground-test sites, environmental-test facilities, certification evidence environments, and verification infrastructure. |
| `07` | Hydrogen and Energy Infrastructure | Applies to LH2, hydrogen, cryogenic, charging, electrical, ground-power, refuelling, storage, energy-distribution, and isolation infrastructure. |
| `08` | Digital Operational Infrastructure | Applies to CSDB, PLM, IETP, digital twin, operational data, ledgers, evidence repositories, and lifecycle-data platforms. |
| `09` | Safety, Security and Access Control | Applies to safety zones, emergency response, hazard control, restricted areas, access control, physical security, and cyber-physical protection infrastructure. |

---

# 5. Programme Applicability

## 5.1 Programme Scope

A programme shall be in scope when its infrastructure assets, systems, facilities, or operational environments belong to the `A-Aerospace` domain and support one or more `I-Infrastructures` sections.

Programme applicability may include:

- aircraft programmes;
- space programmes;
- launcher programmes;
- airport infrastructure programmes;
- vertiport programmes;
- MRO programmes;
- FAL industrialization programmes;
- hydrogen airport-readiness programmes;
- digital infrastructure programmes;
- test and certification campaigns.

## 5.2 Programme Applicability Record

```yaml
programme_applicability:
  programme_id: ""
  programme_name: ""
  domain: "A-Aerospace"
  applicable_infrastructure_sections:
    - section_code: ""
      section_name: ""
      applicability_basis: ""
  lifecycle_phase: ""
  applicability_status: "candidate"
```

## 5.3 Programme Applicability Rule

A programme shall not be considered globally applicable to all infrastructure sections unless explicitly declared.

Each programme shall state:

1. applicable infrastructure sections;
2. excluded infrastructure sections;
3. relevant assets or facilities;
4. lifecycle phase;
5. governing references;
6. traceability to programme-level documents.

---

# 6. Asset Applicability

## 6.1 Asset Scope

An infrastructure asset is in scope when it supports one or more aerospace lifecycle activities.

These activities may include:

- design;
- assembly;
- production;
- certification;
- testing;
- operation;
- servicing;
- maintenance;
- launch;
- reentry;
- recovery;
- digital support;
- safety management;
- security control;
- lifecycle governance.

## 6.2 Asset Applicability Record

```yaml
asset_applicability:
  asset_id: ""
  asset_name: ""
  asset_type: ""
  infrastructure_section:
    section_code: ""
    section_name: ""
  applicability_basis: ""
  effectivity:
    asset_effectivity: ""
    configuration_effectivity: ""
    date_effectivity: ""
    jurisdiction_effectivity: ""
  status: "controlled-candidate"
```

## 6.3 Asset Applicability Rule

An asset shall be applicable to the section where its primary lifecycle function is classified.

Secondary applicability may be declared when the asset also supports:

- safety;
- energy;
- digital operations;
- certification evidence;
- programme-specific operations;
- cross-facility workflows.

---

# 7. Facility Applicability

## 7.1 Facility Scope

A facility is in scope when it physically or digitally supports an aerospace infrastructure function.

Facility examples:

- airport terminal;
- runway;
- apron;
- vertiport pad;
- launch pad;
- launch integration building;
- maintenance hangar;
- FAL station;
- test laboratory;
- hydrogen storage farm;
- CSDB environment;
- operational control room.

## 7.2 Facility Applicability Record

```yaml
facility_applicability:
  facility_id: ""
  facility_name: ""
  facility_type: ""
  location: ""
  jurisdiction: ""
  applicable_sections:
    - section_code: ""
      section_name: ""
      applicability_basis: ""
  facility_effectivity:
    active_from: ""
    active_until: ""
    configuration: ""
    operational_status: ""
```

## 7.3 Facility Applicability Rule

A facility shall be classified by its primary infrastructure function.

Physical location alone shall not define applicability.

Example:

```yaml
example:
  asset_name: "LH2 Airport Refuelling Station"
  physical_location: "Airport"
  primary_applicability: "07-Hydrogen-and-Energy-Infrastructure"
  secondary_applicability:
    - "01-Airports"
    - "09-Safety-Security-and-Access-Control"
  rationale: "Primary function is hydrogen storage, transfer, refuelling, and safety-controlled energy delivery."
```

---

# 8. Jurisdiction Applicability

## 8.1 Jurisdiction Scope

Jurisdiction applicability defines where a regulatory or standards reference may be relevant.

Examples:

| Reference | Jurisdiction Applicability |
|---|---|
| `ICAO-ANNEX14` | International reference family; implementation depends on state adoption. |
| `EASA-ADR` | European Union / EASA aerodrome regulatory system. |
| `EASA-CS-ADR-DSN` | European Union / EASA aerodrome design certification specification context. |
| `EASA-VERTIPORT` | EASA prototype guidance; not automatically regulatory unless adopted. |
| `FAA-PART-139` | United States airport certification system. |
| `FAA-PART-450` | United States commercial launch and reentry licensing system. |
| `ECSS` | European space-sector standardization framework. |
| `NFPA-2` | Hydrogen safety code; applicability depends on local adoption and authority having jurisdiction. |

## 8.2 Jurisdiction Applicability Rule

A regulatory reference shall only be treated as applicable when:

1. the infrastructure asset is located in the relevant jurisdiction;
2. the programme has adopted the reference contractually;
3. the authority has defined it as applicable;
4. the certification basis or approval path invokes it;
5. an internal governance baseline adopts it.

---

# 9. Lifecycle Applicability

## 9.1 Lifecycle Phases

Applicability shall identify the lifecycle phase where the rule, reference, document, or asset applies.

| Lifecycle Phase | Description |
|---|---|
| `LC01` | Concept Definition |
| `LC02` | Requirements Definition |
| `LC03` | Architecture Definition |
| `LC04` | Preliminary Design |
| `LC05` | Detailed Design |
| `LC06` | Verification Planning |
| `LC07` | Construction / Implementation |
| `LC08` | Integration |
| `LC09` | Commissioning |
| `LC10` | Certification / Approval |
| `LC11` | Operation |
| `LC12` | Maintenance / Support |
| `LC13` | Upgrade / Modification |
| `LC14` | Decommissioning / Retirement |

## 9.2 Lifecycle Applicability Rule

A document or reference may apply to one or more lifecycle phases.

Example:

```yaml
lifecycle_applicability:
  applies_to:
    - "LC01"
    - "LC02"
    - "LC03"
  does_not_apply_to:
    - "LC11"
    - "LC12"
  rationale: "Document defines taxonomy scope and applicability before operational use."
```

---

# 10. Configuration Effectivity

## 10.1 Configuration Scope

Configuration effectivity defines the exact configuration baseline to which a document, rule, reference, or infrastructure asset applies.

Configuration effectivity may include:

- baseline ID;
- version;
- revision;
- facility configuration;
- asset configuration;
- system configuration;
- equipment configuration;
- software version;
- digital model version;
- certification baseline.

## 10.2 Configuration Effectivity Record

```yaml
configuration_effectivity:
  baseline_id: ""
  baseline_name: ""
  baseline_version: ""
  revision: ""
  valid_from: ""
  valid_until: ""
  supersedes: ""
  superseded_by: ""
  applicability_condition: ""
```

## 10.3 Configuration Effectivity Rule

A document shall not claim applicability to all configurations unless explicitly declared.

If a document applies only to a defined baseline, the configuration effectivity shall be stated.

---

# 11. Temporal Effectivity

## 11.1 Temporal Scope

Temporal effectivity defines when a document, rule, reference, configuration, or infrastructure classification is valid.

Temporal effectivity may include:

- effective date;
- expiration date;
- review date;
- supersession date;
- commissioning date;
- operational start date;
- retirement date.

## 11.2 Temporal Effectivity Record

```yaml
temporal_effectivity:
  effective_from: "2026-05-08"
  effective_until: ""
  review_due: ""
  superseded_on: ""
  superseded_by: ""
```

## 11.3 Temporal Effectivity Rule

If no `effective_until` date is declared, the item remains valid until:

1. superseded;
2. withdrawn;
3. revised;
4. invalidated by authority or programme decision;
5. replaced by a new controlled baseline.

---

# 12. Digital Effectivity

## 12.1 Digital Scope

Digital effectivity applies to digital operational infrastructure and data-driven infrastructure assets.

It may include:

- CSDB version;
- PLM baseline;
- IETP release;
- digital twin model version;
- ledger version;
- dataset version;
- software version;
- schema version;
- API version.

## 12.2 Digital Effectivity Record

```yaml
digital_effectivity:
  digital_system: ""
  system_type: ""
  version: ""
  schema_version: ""
  data_baseline: ""
  release_status: ""
  valid_from: ""
  valid_until: ""
```

## 12.3 Digital Effectivity Rule

Digital infrastructure shall declare effectivity at the level required to preserve traceability.

If a document depends on a digital model, dataset, ledger, CSDB, PLM, or IETP release, the relevant version or baseline shall be stated.

---

# 13. Applicability Decision Tree

```text
START
 |
 |-- Does the item belong to A-Aerospace?
 |       |-- NO → Out of scope
 |       |-- YES
 |
 |-- Does the item support infrastructure functions?
 |       |-- NO → Classify under another OPT-IN axis
 |       |-- YES
 |
 |-- Is the item general taxonomy governance?
 |       |-- YES → 00-General
 |
 |-- Does the item support airport operations?
 |       |-- YES → 01-Airports
 |
 |-- Does the item support VTOL/eVTOL/AAM/UAM operations?
 |       |-- YES → 02-Vertiports
 |
 |-- Does the item support launch, reentry, or launcher integration?
 |       |-- YES → 03-Spaceports-and-Launchers
 |
 |-- Does the item support maintenance, repair, inspection, or overhaul?
 |       |-- YES → 04-Maintenance-Hangars
 |
 |-- Does the item support assembly, production, major joins, or FAL?
 |       |-- YES → 05-Assemblies-and-FAL
 |
 |-- Does the item support test, qualification, or certification evidence?
 |       |-- YES → 06-Test-and-Certification-Infrastructure
 |
 |-- Does the item support hydrogen, energy, charging, refuelling, or cryogenics?
 |       |-- YES → 07-Hydrogen-and-Energy-Infrastructure
 |
 |-- Does the item support digital operations, data, CSDB, PLM, IETP, or digital twin?
 |       |-- YES → 08-Digital-Operational-Infrastructure
 |
 |-- Does the item support safety, security, access control, or emergency response?
 |       |-- YES → 09-Safety-Security-and-Access-Control
 |
END
```

---

# 14. Applicability Matrix Template

```yaml
applicability_matrix:
  document_id: ""
  title: ""
  applies_to:
    infrastructure_sections:
      - section_code: ""
        section_name: ""
        applicability_basis: ""
    programmes:
      - programme_id: ""
        programme_name: ""
        applicability_basis: ""
    assets:
      - asset_id: ""
        asset_name: ""
        applicability_basis: ""
    facilities:
      - facility_id: ""
        facility_name: ""
        applicability_basis: ""
    jurisdictions:
      - jurisdiction: ""
        applicability_basis: ""
    lifecycle_phases:
      - phase: ""
        applicability_basis: ""
  does_not_apply_to:
    infrastructure_sections: []
    programmes: []
    assets: []
    facilities: []
    jurisdictions: []
  applicability_notes: ""
```

---

# 15. Effectivity Record Template

```yaml
effectivity_record:
  document_id: ""
  effectivity_type:
    - "asset"
    - "programme"
    - "facility"
    - "configuration"
    - "temporal"
    - "jurisdiction"
    - "digital"
  asset_effectivity:
    asset_id: ""
    asset_name: ""
    asset_type: ""
  programme_effectivity:
    programme_id: ""
    programme_name: ""
  facility_effectivity:
    facility_id: ""
    facility_name: ""
    location: ""
  configuration_effectivity:
    baseline_id: ""
    baseline_version: ""
    revision: ""
  temporal_effectivity:
    effective_from: ""
    effective_until: ""
    review_due: ""
  jurisdiction_effectivity:
    jurisdiction: ""
    authority: ""
    applicability_basis: ""
  digital_effectivity:
    system_name: ""
    system_version: ""
    data_baseline: ""
  effectivity_status: "controlled-candidate"
```

---

# 16. Applicability to OPT-IN Axes

| OPT-IN Axis | Applicability Relation |
|---|---|
| `O-Organizations` | Applies when infrastructure ownership, operation, certification, maintenance, or governance bodies must be identified. |
| `P-Programs` | Applies when infrastructure supports a specific aircraft, space, launcher, MRO, FAL, hydrogen, or digital programme. |
| `T-Technologies` | Applies when infrastructure is driven by a specific technology such as LH2, charging, GSE, digital twin, propulsion test, or cryogenic systems. |
| `I-Infrastructures` | Primary axis for physical, digital, industrial, operational, safety, and lifecycle-support infrastructure. |
| `N-Neural-Networks` | Applies when infrastructure supports AI inference, predictive maintenance, digital twin inference, monitoring, optimization, or deterministic AI governance. |

---

# 17. Exclusion Rules

## RULE-I-INFRA-APP-001 — Non-Aerospace Exclusion Rule

An asset, facility, document, or programme shall be excluded if it has no aerospace-domain relevance.

## RULE-I-INFRA-APP-002 — Product-Design Exclusion Rule

Aircraft, spacecraft, or launcher product-design data shall not be classified as infrastructure unless the document specifically addresses the infrastructure enabling design, assembly, operation, maintenance, test, certification, or support.

## RULE-I-INFRA-APP-003 — Procedure Exclusion Rule

Operational, maintenance, production, or test procedures shall not be classified as infrastructure unless the document governs the infrastructure environment where those procedures occur.

## RULE-I-INFRA-APP-004 — Non-Applicable Reference Rule

A standard or regulation shall not be treated as applicable unless the infrastructure section, jurisdiction, programme, contract, or internal governance baseline invokes it.

## RULE-I-INFRA-APP-005 — Superseded Baseline Rule

A superseded document, configuration, or reference shall not be used as active effectivity unless explicitly retained as a historical or legacy baseline.

---

# 18. Applicability Rules

## RULE-I-INFRA-APP-006 — Explicit Applicability Rule

Each child document shall explicitly state its applicability.

Minimum fields:

```yaml
minimum_applicability:
  applies_to:
    - ""
  does_not_apply_to:
    - ""
  applicability_basis: ""
```

## RULE-I-INFRA-APP-007 — Effectivity Declaration Rule

Each child document shall declare effectivity when it applies to a specific asset, programme, facility, configuration, jurisdiction, lifecycle phase, or digital system.

## RULE-I-INFRA-APP-008 — Multi-Section Applicability Rule

If a document applies to multiple infrastructure sections, it shall state:

1. primary applicable section;
2. secondary applicable sections;
3. classification basis;
4. traceability links;
5. duplication-control statement.

## RULE-I-INFRA-APP-009 — Jurisdiction Control Rule

Regulatory applicability shall be declared separately from technical applicability.

A reference may be technically useful without being legally applicable.

## RULE-I-INFRA-APP-010 — Programme Adoption Rule

A reference, standard, method, or infrastructure rule becomes programme-applicable only when adopted by:

1. programme baseline;
2. contract;
3. certification plan;
4. authority agreement;
5. internal governance rule.

---

# 19. Traceability Requirements

Each applicability or effectivity decision shall be traceable to:

1. document ID;
2. infrastructure section;
3. asset or programme ID;
4. classification rule;
5. applicability basis;
6. effectivity basis;
7. reference family, if applicable;
8. lifecycle phase;
9. owner;
10. evidence item.

Required traceability pattern:

```yaml
traceability:
  upstream:
    - document_id: "IDEALE-ESG-A-AEROSPACE-I-INFRASTRUCTURES-00-00-SCOPE-PURPOSE"
    - document_id: "IDEALE-ESG-A-AEROSPACE-I-INFRASTRUCTURES-00-01-DEFINITIONS"
    - document_id: "IDEALE-ESG-A-AEROSPACE-I-INFRASTRUCTURES-00-02-INFRASTRUCTURE-CLASSIFICATION-RULES"
    - document_id: "IDEALE-ESG-A-AEROSPACE-I-INFRASTRUCTURES-00-03-STANDARDS-AND-REGULATORY-REFERENCES"
  applicability_basis:
    - rule_id: ""
      rationale: ""
  effectivity_basis:
    - effectivity_type: ""
      rationale: ""
  evidence:
    - evidence_id: ""
      evidence_type: ""
      evidence_status: ""
```

---

# 20. Footprints

## Semantic Footprint

```yaml
semantic_footprint:
  id: FP-SEM-I-INFRA-00-04
  subject: "Applicability and effectivity rules for aerospace infrastructure taxonomy"
  meaning_boundary:
    includes:
      - applicability rules
      - effectivity rules
      - asset scope
      - programme scope
      - facility scope
      - jurisdiction scope
      - lifecycle scope
      - configuration scope
      - digital effectivity
    excludes:
      - full regulatory compliance demonstration
      - detailed legal interpretation
      - programme-specific certification basis
      - facility-specific engineering design
```

## Taxonomy Footprint

```yaml
taxonomy_footprint:
  id: FP-TAX-I-INFRA-00-04
  hierarchy:
    root: "IDEALE-ESG"
    domain: "A-Aerospace"
    opt_in_axis: "I-Infrastructures"
    section: "00-General"
    document: "00-04-Applicability-and-Effectivity"
```

## Lifecycle Footprint

```yaml
lifecycle_footprint:
  id: FP-LC-I-INFRA-00-04
  lifecycle_phase: "LC01"
  lifecycle_role: "Applicability and effectivity control definition"
  exit_criteria:
    - applicability classes defined
    - effectivity types defined
    - applicability matrix provided
    - effectivity record template provided
    - jurisdiction rules defined
    - lifecycle applicability rules defined
    - traceability requirements defined
```

## Compliance Footprint

```yaml
compliance_footprint:
  id: FP-COMP-I-INFRA-00-04
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
  id: FP-EVD-I-INFRA-00-04
  expected_evidence:
    - controlled markdown document
    - YAML frontmatter
    - canonical path
    - parent path
    - applicability classes
    - effectivity rules
    - applicability matrix
    - effectivity record template
    - exclusion rules
    - traceability requirements
```

---

# 21. Citation Map

| Citation Key | Applies To | Use in This Taxonomy |
|---|---|---|
| `ICAO-ANNEX14` | `01-Airports` | Supports airport and aerodrome applicability context. |
| `EASA-ADR` | `01-Airports`, `09-Safety-Security-and-Access-Control` | Supports EU aerodrome applicability and jurisdiction control. |
| `EASA-CS-ADR-DSN` | `01-Airports` | Supports aerodrome design applicability and design effectivity. |
| `EASA-VERTIPORT` | `02-Vertiports` | Supports vertiport applicability and VTOL/eVTOL infrastructure scope. |
| `FAA-PART-139` | `01-Airports` | Supports US airport certification applicability. |
| `FAA-PART-450` | `03-Spaceports-and-Launchers` | Supports launch, reentry, and spaceport jurisdiction applicability. |
| `ECSS` | `03-Spaceports-and-Launchers`, `06-Test-and-Certification-Infrastructure`, `08-Digital-Operational-Infrastructure` | Supports space-sector lifecycle and systems applicability. |
| `IAQG-9100` | `04-Maintenance-Hangars`, `05-Assemblies-and-FAL`, `06-Test-and-Certification-Infrastructure` | Supports aerospace quality-management applicability. |
| `ISO-9001` | `04-Maintenance-Hangars`, `05-Assemblies-and-FAL`, `08-Digital-Operational-Infrastructure` | Supports general QMS applicability. |
| `ISO-55000` | All sections | Supports asset-management applicability and lifecycle effectivity. |
| `ISO-31000` | All safety-relevant sections | Supports risk-based applicability and hazard-control effectivity. |
| `ISO-19880-1` | `07-Hydrogen-and-Energy-Infrastructure` | Supports hydrogen fuelling infrastructure applicability. |
| `NFPA-2` | `07-Hydrogen-and-Energy-Infrastructure`, `09-Safety-Security-and-Access-Control` | Supports hydrogen safety applicability. |
| `ISO-IEC-IEEE-15288` | `06-Test-and-Certification-Infrastructure`, `08-Digital-Operational-Infrastructure` | Supports systems lifecycle applicability and effectivity. |

---

# 22. Controlled References

## [ICAO-ANNEX14]

**ICAO Annex 14 — Aerodromes, Volume I, Aerodrome Design and Operations.**

Used as an airport and aerodrome reference family for applicability and effectivity decisions related to `01-Airports`.

## [EASA-ADR]

**EASA Easy Access Rules for Aerodromes — Regulation (EU) No 139/2014.**

Used as the EU aerodrome regulatory reference family for applicability and jurisdiction control related to airport infrastructure.

## [EASA-CS-ADR-DSN]

**EASA Certification Specifications and Guidance Material for Aerodrome Design.**

Used as an aerodrome design reference family for applicability and effectivity of airport physical infrastructure.

## [EASA-VERTIPORT]

**EASA Prototype Technical Design Specifications for Vertiports.**

Used as the vertiport design reference family for applicability of VTOL/eVTOL infrastructure.

## [FAA-PART-139]

**14 CFR Part 139 — Certification of Airports.**

Used as the US airport certification reference family for jurisdiction-specific applicability.

## [FAA-PART-450]

**14 CFR Part 450 — Launch and Reentry License Requirements.**

Used as the launch and reentry reference family for spaceport, launcher, range-safety, and reentry infrastructure applicability.

## [ECSS]

**European Cooperation for Space Standardization — ECSS Standards.**

Used as the European space reference family for lifecycle applicability in space infrastructure, launch support, ground systems, engineering, and product assurance.

## [IAQG-9100]

**IAQG 9100 — Quality Management Systems Requirements for Aviation, Space and Defense Organizations.**

Used as the aviation, space, and defense QMS reference family for maintenance, production, assembly, FAL, test, and lifecycle infrastructure.

## [ISO-9001]

**ISO 9001 — Quality Management Systems Requirements.**

Used as the general QMS reference family for organizational process applicability and infrastructure quality governance.

## [ISO-55000]

**ISO 55000 — Asset Management, Vocabulary, Overview and Principles.**

Used as the asset-management reference family for asset lifecycle applicability and effectivity.

## [ISO-31000]

**ISO 31000 — Risk Management Guidelines.**

Used as the risk-management reference family for risk-based applicability, hazard-control effectivity, and safety-governance scope.

## [ISO-19880-1]

**ISO 19880-1 — Gaseous Hydrogen Fuelling Stations.**

Used as the hydrogen fuelling-station reference family for hydrogen infrastructure applicability. Programme-specific assessment is required for LH2 aerospace applications.

## [NFPA-2]

**NFPA 2 — Hydrogen Technologies Code.**

Used as the hydrogen safety-code reference family for hydrogen storage, handling, installation, and safety-control applicability.

## [ISO-IEC-IEEE-15288]

**ISO/IEC/IEEE 15288 — Systems and Software Engineering, System Life Cycle Processes.**

Used as the systems lifecycle reference family for test, certification, digital operational infrastructure, and lifecycle-process effectivity.

---

# 23. Governance Rule

Any child document under `I-Infrastructures` shall include applicability and effectivity statements when the document is limited by asset, programme, facility, jurisdiction, lifecycle phase, configuration, digital system, or operational condition.

No document shall imply universal applicability unless explicitly declared.

No regulatory reference shall be treated as legally applicable without jurisdictional, contractual, programme, or authority basis.

---

# 24. Acceptance Criteria

This document is acceptable when:

- applicability and effectivity are clearly distinguished;
- applicability classes are defined;
- infrastructure-section applicability is mapped;
- asset, programme, facility, jurisdiction, lifecycle, configuration, temporal, and digital effectivity are addressed;
- templates are provided;
- exclusion rules are stated;
- traceability requirements are defined;
- child documents can reuse the applicability and effectivity logic without reinterpretation.

---

# 25. Summary

`00-04-Applicability-and-Effectivity` defines the controlled applicability and effectivity rules for the `I-Infrastructures` taxonomy.

It governs which assets, programmes, facilities, configurations, lifecycle phases, jurisdictions, digital systems, and operational conditions are in scope for each infrastructure document.
````
