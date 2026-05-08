---
document_id: IDEALE-ESG-A-AEROSPACE-I-INFRASTRUCTURES-00-01-DEFINITIONS
title: "00-01-Definitions — Definitions"
canonical_path: "IDEALE-ESG/A-Aerospace/I-Infrastructures/00-General/00-01-Definitions.md"
parent_path: "IDEALE-ESG/A-Aerospace/I-Infrastructures/00-General/"
parent_document: "README.md"

domain: "A-Aerospace"
opt_in_axis: "I-Infrastructures"
section: "00-General"
node_code: "00-01"

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
  - ISO-9000
  - ISO-31000

tags:
  - IDEALE-ESG
  - A-Aerospace
  - OPT-IN
  - I-Infrastructures
  - General
  - Definitions
  - Controlled-Terminology
  - Infrastructure-Governance
---

# 00-01-Definitions — Definitions

## Purpose

Controlled terminology and definitions applicable across all `I-Infrastructures` sections.

This document defines the common vocabulary used to classify, govern, trace, and reference aerospace infrastructure assets, systems, facilities, data environments, and lifecycle-support environments under:

```text
IDEALE-ESG.panpara.eu/A-Aerospace/I-Infrastructures/00-General/
````

## Parent

[`README.md`](README.md) — `IDEALE-ESG/A-Aerospace/I-Infrastructures/00-General/`

---

# 1. Controlled Terminology

## 1.1 Infrastructure

An **infrastructure** is a physical, digital, industrial, operational, or organizational asset environment that enables a system, programme, facility, or service to function across its lifecycle.

In the `I-Infrastructures` axis, infrastructure includes:

* physical facilities;
* access and mobility systems;
* industrial production environments;
* test and certification environments;
* maintenance and support environments;
* energy and refuelling systems;
* digital operational systems;
* safety, security, and access-control systems.

## 1.2 Aerospace Infrastructure

An **aerospace infrastructure** is an infrastructure that enables the design, assembly, certification, operation, maintenance, servicing, launch, recovery, or lifecycle support of aircraft, spacecraft, launchers, aerospace systems, or aerospace services.

Aerospace infrastructure includes both:

* **physical infrastructure**, such as airports, vertiports, spaceports, hangars, launch pads, assembly buildings, test sites, and final assembly lines;
* **digital infrastructure**, such as CSDB, PLM, IETP, digital twins, operational-data platforms, ledgers, simulation environments, and controlled evidence repositories.

## 1.3 Infrastructure Class

An **infrastructure class** is a controlled category under the `I-Infrastructures` taxonomy.

The primary infrastructure classes are:

| Code | Infrastructure Class                  |
| ---: | ------------------------------------- |
| `01` | Airports                              |
| `02` | Vertiports                            |
| `03` | Spaceports and Launchers              |
| `04` | Maintenance Hangars                   |
| `05` | Assemblies and FAL                    |
| `06` | Test and Certification Infrastructure |
| `07` | Hydrogen and Energy Infrastructure    |
| `08` | Digital Operational Infrastructure    |
| `09` | Safety, Security and Access Control   |

## 1.4 Section

A **section** is a two-digit controlled subdivision under the `I-Infrastructures` axis.

Example:

```text
01-Airports/
02-Vertiports/
03-Spaceports-and-Launchers/
```

A section groups documents, references, footprints, and evidence related to one infrastructure class.

## 1.5 Node

A **node** is a controlled taxonomy element with an identifier, path, scope, parent relation, lifecycle marker, and traceability context.

Example:

```text
IDEALE-ESG.panpara.eu/A-Aerospace/I-Infrastructures/00-General/00-01-Definitions.md
```

## 1.6 Canonical Path

A **canonical path** is the controlled location of a taxonomy node, document, section, or infrastructure class.

Canonical paths shall be stable, human-readable, version-compatible, and traceable to parent nodes.

## 1.7 Parent Path

A **parent path** is the direct upstream path from which a document or node inherits scope, governance, naming logic, and classification context.

## 1.8 Controlled Candidate

A **controlled candidate** is a taxonomy element that has a structured document form, identifier, path, and governance context, but has not yet reached fully approved controlled-baseline status.

## 1.9 Controlled Baseline

A **controlled baseline** is an approved version of a document, taxonomy node, architecture element, or reference structure that is stable enough to be used for downstream authoring, validation, traceability, and governance.

## 1.10 Footprint

A **footprint** is a structured traceability mark that records why a document exists, where it belongs, what it covers, what it excludes, and what evidence or references support it.

Footprints may be:

* semantic;
* taxonomy-based;
* lifecycle-based;
* compliance-based;
* evidence-based;
* operational;
* digital;
* safety-related.

## 1.11 Evidence

**Evidence** is controlled information used to support a claim, classification, decision, requirement, interface, compliance statement, or lifecycle gate.

Evidence may include:

* source documents;
* standards references;
* certification records;
* engineering reports;
* test results;
* analysis files;
* inspection records;
* configuration records;
* digital signatures;
* lifecycle logs;
* traceability matrices.

## 1.12 Citation Key

A **citation key** is a controlled short identifier used to connect a taxonomy statement to an external standard, regulation, guidance document, or authoritative reference family.

Example:

```text
ICAO-ANNEX14
EASA-ADR
FAA-LAUNCH
ECSS
ISO-55000
```

## 1.13 Reference Family

A **reference family** is a group of external references used to support a taxonomy area.

Example:

| Reference Family                 | Typical Use                                   |
| -------------------------------- | --------------------------------------------- |
| Aerodrome references             | Airports                                      |
| Vertiport references             | Vertiports                                    |
| Launch and reentry references    | Spaceports and Launchers                      |
| Space standardization references | Space infrastructure and launch systems       |
| Quality-management references    | Industrial and aerospace lifecycle governance |
| Asset-management references      | Infrastructure lifecycle governance           |

---

# 2. Infrastructure Asset Definitions

## 2.1 Asset

An **asset** is an item, system, facility, dataset, platform, component, or environment that has value to an organization, programme, infrastructure operator, or lifecycle process.

In this taxonomy, assets may be physical, digital, operational, procedural, or organizational.

## 2.2 Physical Asset

A **physical asset** is a tangible infrastructure element such as a runway, hangar, launch pad, assembly jig, fuel-storage tank, cryogenic line, charging station, test rig, or access-control barrier.

## 2.3 Digital Asset

A **digital asset** is a controlled data, software, model, evidence, or information object used to support infrastructure operation, lifecycle management, certification, safety, or governance.

Examples:

* CSDB;
* PLM records;
* IETP packages;
* digital twins;
* operational datasets;
* inspection records;
* configuration baselines;
* ledger entries;
* simulation models.

## 2.4 Operational Asset

An **operational asset** is an infrastructure element used directly in operations, servicing, maintenance, assembly, test, certification, launch, recovery, turnaround, or support activities.

## 2.5 Critical Asset

A **critical asset** is an asset whose failure, degradation, misconfiguration, or unavailability can create significant safety, operational, certification, security, environmental, or business-continuity impact.

## 2.6 Lifecycle Asset

A **lifecycle asset** is an asset managed across phases such as concept, design, construction, commissioning, operation, maintenance, upgrade, decommissioning, and retirement.

---

# 3. Airport Definitions

## 3.1 Airport

An **airport** is an infrastructure environment supporting aircraft landing, take-off, taxiing, parking, servicing, passenger processing, cargo processing, ground handling, emergency response, and operational coordination.

## 3.2 Aerodrome

An **aerodrome** is a defined area intended for the arrival, departure, and surface movement of aircraft.

Within this taxonomy, `airport` is used for the broader operational infrastructure class, while `aerodrome` may be used when referring to regulatory, design, or standards terminology.

## 3.3 Runway

A **runway** is a defined surface prepared for aircraft landing and take-off.

## 3.4 Taxiway

A **taxiway** is a defined path used by aircraft to move between runways, aprons, stands, terminals, hangars, and other airport areas.

## 3.5 Apron

An **apron** is an airport area used for aircraft parking, loading, unloading, refuelling, servicing, boarding, disembarkation, and ground-support operations.

## 3.6 Aircraft Stand

An **aircraft stand** is a designated area on an apron where an aircraft may be parked for servicing, boarding, loading, or turnaround operations.

## 3.7 Ground Support Equipment

**Ground Support Equipment**, or **GSE**, is equipment used to service, move, support, power, cool, tow, load, unload, inspect, or maintain aircraft on the ground.

## 3.8 Turnaround

A **turnaround** is the set of ground operations performed between aircraft arrival and departure.

Turnaround may include:

* passenger disembarkation;
* baggage handling;
* refuelling or recharging;
* catering;
* cleaning;
* line maintenance;
* boarding;
* pushback preparation.

---

# 4. Vertiport Definitions

## 4.1 Vertiport

A **vertiport** is an infrastructure environment designed to support VTOL, eVTOL, and advanced air mobility operations, including take-off, landing, parking, charging, passenger processing, access control, emergency response, and digital traffic coordination.

## 4.2 VTOL

**VTOL** means **Vertical Take-Off and Landing**.

It refers to aircraft capable of taking off and landing vertically.

## 4.3 eVTOL

**eVTOL** means **electric Vertical Take-Off and Landing**.

It refers to electrically powered VTOL aircraft, including battery-electric, hybrid-electric, fuel-cell-electric, or other electric-propulsion configurations.

## 4.4 Advanced Air Mobility

**Advanced Air Mobility**, or **AAM**, is an aviation concept involving new aircraft, operational models, infrastructure, and digital coordination methods for air mobility services.

## 4.5 UAM

**Urban Air Mobility**, or **UAM**, is a subset of advanced air mobility focused on urban or metropolitan operations.

## 4.6 Final Approach and Take-Off Area

A **Final Approach and Take-Off Area**, or **FATO**, is a defined area over which the final phase of approach to hover or landing is completed and from which take-off is commenced.

## 4.7 Touchdown and Lift-Off Area

A **Touchdown and Lift-Off Area**, or **TLOF**, is a load-bearing area where a VTOL aircraft may touch down or lift off.

## 4.8 Vertiport Energy Interface

A **vertiport energy interface** is the infrastructure interface used to provide energy to VTOL or eVTOL aircraft.

It may include:

* electric charging;
* battery swapping;
* hydrogen refuelling;
* ground power;
* thermal conditioning;
* safety interlocks;
* metering and traceability systems.

---

# 5. Spaceport and Launcher Definitions

## 5.1 Spaceport

A **spaceport** is an infrastructure environment supporting launch, reentry, payload processing, launcher integration, propellant handling, range safety, mission operations, recovery, and space-access services.

## 5.2 Launcher

A **launcher** is a vehicle, system, or integrated launch architecture used to place payloads, spacecraft, or mission elements into a target trajectory, orbit, or flight path.

## 5.3 Launch Pad

A **launch pad** is a designated infrastructure area from which a launcher is prepared, supported, and launched.

## 5.4 Launch Complex

A **launch complex** is a group of facilities, systems, access routes, control systems, safety zones, propellant systems, and support areas associated with launch operations.

## 5.5 Payload Processing Facility

A **payload processing facility** is an infrastructure environment used to receive, inspect, test, configure, integrate, encapsulate, or prepare payloads before launch.

## 5.6 Launcher Integration Facility

A **launcher integration facility** is a building, bay, or infrastructure zone where launcher stages, payloads, fairings, adapters, or mission hardware are integrated before launch.

## 5.7 Range Safety

**Range safety** is the set of controls, systems, procedures, zones, analyses, and operational decisions used to protect people, property, airspace, maritime areas, and the environment during launch or reentry operations.

## 5.8 Flight Termination Interface

A **flight termination interface** is an infrastructure or system interface associated with the ability to terminate a launch vehicle flight when required by safety criteria.

## 5.9 Reentry Infrastructure

**Reentry infrastructure** is the infrastructure used to support controlled return, recovery, tracking, safety coordination, payload retrieval, vehicle processing, or post-flight handling after reentry.

---

# 6. Maintenance Hangar Definitions

## 6.1 Maintenance Hangar

A **maintenance hangar** is an infrastructure facility used for aircraft, spacecraft, launcher, or system inspection, maintenance, repair, modification, overhaul, testing, preservation, or return-to-service preparation.

## 6.2 MRO

**MRO** means **Maintenance, Repair, and Overhaul**.

It refers to the industrial and operational ecosystem used to inspect, maintain, repair, overhaul, modify, support, and return aerospace assets to service.

## 6.3 Line Maintenance

**Line maintenance** is maintenance performed in an operational context, typically to support dispatch, turnaround, short-duration inspection, defect rectification, or continued operation.

## 6.4 Base Maintenance

**Base maintenance** is deeper maintenance performed in dedicated facilities, typically involving scheduled inspections, structural access, component removal, major repairs, modifications, or extended downtime.

## 6.5 Maintenance Bay

A **maintenance bay** is a dedicated area inside a hangar or maintenance facility assigned to inspection, repair, servicing, overhaul, modification, or support tasks.

## 6.6 Access Platform

An **access platform** is infrastructure or equipment that provides safe physical access to aircraft, spacecraft, launcher, or component zones during maintenance, inspection, assembly, or test.

## 6.7 Tooling

**Tooling** refers to tools, fixtures, jigs, stands, lifting devices, measurement equipment, test equipment, and special-to-type equipment used in maintenance, assembly, inspection, repair, or production activities.

---

# 7. Assemblies and FAL Definitions

## 7.1 Assembly

An **assembly** is a controlled grouping of parts, components, structures, systems, or subassemblies integrated to form a larger aerospace product element.

## 7.2 Major Assembly

A **major assembly** is a large product element such as a wing, fuselage, centerbody, empennage, landing gear module, engine installation, tank module, cabin module, launcher stage, or spacecraft module.

## 7.3 Subassembly

A **subassembly** is a smaller controlled assembly integrated into a major assembly or final product.

## 7.4 FAL

**FAL** means **Final Assembly Line**.

A final assembly line is the industrial infrastructure where major assemblies, systems, equipment, interiors, software, tests, inspections, and delivery configurations are integrated into a complete aerospace product.

## 7.5 Station

A **station** is a controlled location in a production or assembly flow where defined operations, inspections, installations, tests, or configuration actions are performed.

## 7.6 Jig

A **jig** is a tool or fixture used to control position, orientation, geometry, repeatability, or assembly accuracy during manufacturing or integration.

## 7.7 Fixture

A **fixture** is a support or holding device used to locate, stabilize, position, or protect parts, assemblies, or components during manufacturing, assembly, test, inspection, or transport.

## 7.8 Major Join

A **major join** is an industrial operation where major assemblies are structurally or functionally integrated.

Examples:

* wing-to-centerbody join;
* fuselage-section join;
* engine-installation join;
* tank-module integration;
* launcher-stage mating;
* payload-adapter integration.

## 7.9 Industrial Flow

**Industrial flow** is the controlled sequence of production, assembly, inspection, test, rework, acceptance, and delivery activities within an industrial infrastructure.

---

# 8. Test and Certification Infrastructure Definitions

## 8.1 Test Infrastructure

**Test infrastructure** is the physical, digital, operational, and organizational environment used to perform controlled testing.

It may include:

* laboratories;
* test rigs;
* ground-test facilities;
* environmental chambers;
* structural-test frames;
* propulsion-test stands;
* instrumentation systems;
* data-acquisition systems;
* safety systems;
* evidence repositories.

## 8.2 Certification Infrastructure

**Certification infrastructure** is the set of facilities, systems, evidence environments, processes, records, and controls used to support certification demonstration, compliance substantiation, and regulatory review.

## 8.3 Test Rig

A **test rig** is a controlled setup used to test a component, subsystem, system, structure, assembly, or operational function.

## 8.4 Ground Test

A **ground test** is a test performed while the product, system, or test article remains on the ground or in a ground-based facility.

## 8.5 Environmental Test

An **environmental test** is a test used to evaluate behavior under environmental conditions such as temperature, humidity, vibration, shock, pressure, altitude, dust, corrosion, icing, electromagnetic exposure, or cryogenic conditions.

## 8.6 Structural Test

A **structural test** is a test used to verify structural strength, stiffness, damage tolerance, fatigue behavior, load paths, deformation, or failure margins.

## 8.7 Propulsion Test

A **propulsion test** is a test used to verify propulsion-system behavior, performance, safety, thermal behavior, integration, control, or endurance.

## 8.8 Certification Evidence

**Certification evidence** is controlled evidence used to support compliance demonstration against certification requirements, standards, rules, means of compliance, or approved certification plans.

---

# 9. Hydrogen and Energy Infrastructure Definitions

## 9.1 Energy Infrastructure

**Energy infrastructure** is the infrastructure used to produce, receive, store, convert, distribute, meter, control, or deliver energy to aerospace assets, facilities, or operations.

## 9.2 Hydrogen Infrastructure

**Hydrogen infrastructure** is the infrastructure used to receive, store, distribute, condition, refuel, vent, detect, isolate, or safely manage hydrogen.

## 9.3 LH2

**LH2** means **liquid hydrogen**.

Within this taxonomy, LH2 infrastructure includes cryogenic storage, transfer, refuelling, safety, thermal control, boil-off management, venting, leak detection, isolation, and emergency-response interfaces.

## 9.4 Cryogenic Infrastructure

**Cryogenic infrastructure** is infrastructure used to safely manage very-low-temperature fluids, materials, systems, equipment, insulation, transfer lines, tanks, valves, sensors, and safety controls.

## 9.5 Refuelling Interface

A **refuelling interface** is the physical, digital, safety, procedural, and metering interface between an infrastructure energy source and an aerospace vehicle or system.

## 9.6 Charging Infrastructure

**Charging infrastructure** is infrastructure used to provide electrical energy to electric or hybrid-electric aerospace systems, ground systems, support equipment, or facility assets.

## 9.7 Ground Power

**Ground power** is externally supplied electrical power used to support aircraft, spacecraft, launchers, support equipment, test systems, or facility systems while not relying on onboard power generation.

---

# 10. Digital Operational Infrastructure Definitions

## 10.1 Digital Operational Infrastructure

**Digital operational infrastructure** is the controlled digital environment used to manage operational data, technical information, configuration records, lifecycle evidence, digital twins, maintenance information, and decision-support systems.

## 10.2 CSDB

**CSDB** means **Common Source DataBase**.

A CSDB is a controlled repository used to manage structured technical-publication source data, including S1000D data modules, publication modules, illustrations, applicability, metadata, and publication outputs.

## 10.3 IETP

**IETP** means **Interactive Electronic Technical Publication**.

An IETP is an interactive digital publication environment used to deliver technical, maintenance, operational, procedural, or support information.

## 10.4 PLM

**PLM** means **Product Lifecycle Management**.

PLM is the system environment used to manage product configuration, lifecycle data, engineering changes, product structures, requirements, manufacturing data, and related evidence.

## 10.5 Digital Twin

A **digital twin** is a digital representation of a physical, operational, or lifecycle asset that is maintained through data, models, interfaces, and operational updates.

## 10.6 Operational Data Platform

An **operational data platform** is a digital platform used to collect, store, process, govern, analyze, and distribute data generated by infrastructure operations.

## 10.7 Ledger

A **ledger** is a controlled record system used to anchor, trace, timestamp, verify, or audit evidence, events, contributions, configuration states, approvals, or lifecycle transactions.

## 10.8 Configuration Baseline

A **configuration baseline** is an approved and controlled configuration state used as a reference for design, production, maintenance, certification, operation, or lifecycle governance.

---

# 11. Safety, Security, and Access-Control Definitions

## 11.1 Safety

**Safety** is the condition in which risks associated with hazards are identified, assessed, mitigated, and controlled to an acceptable level.

## 11.2 Security

**Security** is the protection of assets, people, data, systems, facilities, and operations against unauthorized access, interference, misuse, sabotage, theft, cyberattack, or hostile action.

## 11.3 Access Control

**Access control** is the set of physical, digital, procedural, and organizational controls used to determine who or what may access a facility, system, zone, asset, data object, or operational process.

## 11.4 Safety Zone

A **safety zone** is a defined area with controlled access, procedures, barriers, or restrictions used to protect people, assets, operations, and the environment from hazards.

## 11.5 Restricted Area

A **restricted area** is an area with limited access due to safety, security, operational, regulatory, or confidentiality requirements.

## 11.6 Hazard

A **hazard** is a condition, object, event, function, energy source, failure mode, or operational state with the potential to cause harm, damage, loss, non-compliance, or mission degradation.

## 11.7 Risk

**Risk** is the effect of uncertainty on objectives, generally expressed in terms of likelihood and consequence.

## 11.8 Emergency Response

**Emergency response** is the set of planned actions, resources, roles, systems, communications, and procedures used to respond to accidents, incidents, hazards, failures, security events, environmental events, or operational emergencies.

## 11.9 Cyber-Physical Protection

**Cyber-physical protection** is the integrated protection of digital systems and physical infrastructure where cyber events may affect physical operations, safety, security, access, energy, or lifecycle continuity.

---

# 12. Governance and Lifecycle Definitions

## 12.1 Governance

**Governance** is the set of rules, roles, authorities, processes, controls, and evidence mechanisms used to direct, validate, approve, monitor, and improve infrastructure taxonomy content.

## 12.2 Lifecycle

A **lifecycle** is the sequence of phases through which an infrastructure element, asset, system, document, facility, or digital object passes.

Typical lifecycle phases include:

* concept;
* definition;
* design;
* construction;
* integration;
* commissioning;
* operation;
* maintenance;
* upgrade;
* decommissioning;
* retirement.

## 12.3 Lifecycle Phase

A **lifecycle phase** is a controlled segment of the lifecycle used to organize evidence, maturity, decisions, gates, and responsibilities.

## 12.4 Gate

A **gate** is a controlled review or decision point where maturity, evidence, scope, risk, and readiness are assessed before progression.

## 12.5 Acceptance Criteria

**Acceptance criteria** are controlled conditions that must be satisfied before a document, node, system, asset, or process can be accepted, baselined, released, or used downstream.

## 12.6 Applicability

**Applicability** defines the conditions under which a document, rule, requirement, reference, procedure, or classification applies.

## 12.7 Effectivity

**Effectivity** defines the specific product, asset, configuration, serial number, batch, facility, timeframe, version, or operational condition to which a document, rule, or requirement applies.

## 12.8 Traceability

**Traceability** is the ability to link a statement, requirement, document, decision, asset, configuration, evidence item, or lifecycle event to its origin, rationale, parent, child, reference, and verification record.

## 12.9 Verification

**Verification** is confirmation that specified requirements have been fulfilled.

## 12.10 Validation

**Validation** is confirmation that the intended use, operational need, or stakeholder purpose has been satisfied.

---

# 13. OPT-IN Axis Definitions

## 13.1 OPT-IN

**OPT-IN** is the controlled five-axis structure used to organize IDEALE-ESG content.

The five axes are:

| Axis | Meaning         |
| ---- | --------------- |
| `O`  | Organizations   |
| `P`  | Programs        |
| `T`  | Technologies    |
| `I`  | Infrastructures |
| `N`  | Neural Networks |

## 13.2 O-Organizations

**O-Organizations** covers organizations, operators, authorities, suppliers, industrial actors, governance bodies, and institutional stakeholders.

## 13.3 P-Programs

**P-Programs** covers aerospace programmes, projects, campaigns, aircraft baselines, space missions, infrastructure initiatives, certification campaigns, and lifecycle programmes.

## 13.4 T-Technologies

**T-Technologies** covers technical systems, subsystems, equipment, materials, propulsion, energy, avionics, digital systems, sensors, manufacturing methods, and enabling technologies.

## 13.5 I-Infrastructures

**I-Infrastructures** covers physical, digital, industrial, operational, safety, and lifecycle-support infrastructure.

## 13.6 N-Neural-Networks

**N-Neural-Networks** covers neural-network systems, deterministic AI governance, model verification, synthetic data, digital-twin inference, predictive maintenance, autonomous operations, and AI-enabled infrastructure support.

---

# 14. Controlled Abbreviations

| Abbreviation | Meaning                                        |
| ------------ | ---------------------------------------------- |
| `AAM`        | Advanced Air Mobility                          |
| `ADR`        | Aerodrome Rules                                |
| `CSDB`       | Common Source DataBase                         |
| `ECSS`       | European Cooperation for Space Standardization |
| `eVTOL`      | electric Vertical Take-Off and Landing         |
| `FAL`        | Final Assembly Line                            |
| `FATO`       | Final Approach and Take-Off Area               |
| `GSE`        | Ground Support Equipment                       |
| `IETP`       | Interactive Electronic Technical Publication   |
| `LH2`        | Liquid Hydrogen                                |
| `MRO`        | Maintenance, Repair, and Overhaul              |
| `PLM`        | Product Lifecycle Management                   |
| `QMS`        | Quality Management System                      |
| `TLOF`       | Touchdown and Lift-Off Area                    |
| `UAM`        | Urban Air Mobility                             |
| `VTOL`       | Vertical Take-Off and Landing                  |

---

# Footprints

## Semantic Footprint

```yaml
semantic_footprint:
  id: FP-SEM-I-INFRA-00-01
  subject: "Controlled definitions for aerospace infrastructure taxonomy"
  meaning_boundary:
    includes:
      - controlled terminology
      - infrastructure definitions
      - asset definitions
      - airport definitions
      - vertiport definitions
      - spaceport and launcher definitions
      - maintenance hangar definitions
      - assemblies and FAL definitions
      - test and certification infrastructure definitions
      - hydrogen and energy infrastructure definitions
      - digital operational infrastructure definitions
      - safety security and access-control definitions
    excludes:
      - detailed engineering requirements
      - detailed regulatory compliance demonstrations
      - facility-specific procedures
      - programme-specific work instructions
```

## Taxonomy Footprint

```yaml
taxonomy_footprint:
  id: FP-TAX-I-INFRA-00-01
  hierarchy:
    root: "IDEALE-ESG"
    domain: "A-Aerospace"
    opt_in_axis: "I-Infrastructures"
    section: "00-General"
    document: "00-01-Definitions"
```

## Lifecycle Footprint

```yaml
lifecycle_footprint:
  id: FP-LC-I-INFRA-00-01
  lifecycle_phase: "LC01"
  lifecycle_role: "Terminology definition and vocabulary control"
  exit_criteria:
    - controlled terminology established
    - abbreviations listed
    - infrastructure classes defined
    - definitions aligned with section taxonomy
    - citation keys declared
```

## Compliance Footprint

```yaml
compliance_footprint:
  id: FP-COMP-I-INFRA-00-01
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
      - "ISO-9000"
    asset_and_risk_management:
      - "ISO-55000"
      - "ISO-31000"
```

## Evidence Footprint

```yaml
evidence_footprint:
  id: FP-EVD-I-INFRA-00-01
  expected_evidence:
    - controlled markdown document
    - YAML frontmatter
    - canonical path
    - parent path
    - controlled definitions
    - abbreviation table
    - citation keys
    - reference map
    - traceability links
```

---

# Citation Map

| Citation Key     | Applies To                     | Use in This Taxonomy                                                                  |
| ---------------- | ------------------------------ | ------------------------------------------------------------------------------------- |
| `ICAO-ANNEX14`   | Airports / Aerodromes          | Airport and aerodrome terminology reference family.                                   |
| `EASA-ADR`       | EU aerodrome infrastructure    | Aerodrome rules and administrative reference family.                                  |
| `EASA-VERTIPORT` | Vertiports                     | Vertiport terminology and prototype design reference family.                          |
| `FAA-LAUNCH`     | Spaceports / Launchers         | Launch, reentry, licensing, and range-safety reference family.                        |
| `ECSS`           | Space systems / Ground systems | European space infrastructure, engineering, and product-assurance reference family.   |
| `IAQG-9100`      | Aerospace quality management   | QMS terminology and aviation, space, and defense quality-governance reference family. |
| `ISO-9000`       | Quality management             | General quality-management terminology reference family.                              |
| `ISO-55000`      | Asset management               | Asset-management terminology and lifecycle reference family.                          |
| `ISO-31000`      | Risk management                | Risk-management terminology and governance reference family.                          |

---

# Controlled References

## [ICAO-ANNEX14]

**ICAO Annex 14 — Aerodromes, Volume I, Aerodrome Design and Operations.**

Used as the airport and aerodrome terminology reference family for `01-Airports`.

## [EASA-ADR]

**EASA Easy Access Rules for Aerodromes — Regulation (EU) No 139/2014.**

Used as the EU aerodrome regulatory and administrative terminology reference family for `01-Airports`.

## [EASA-VERTIPORT]

**EASA Prototype Technical Design Specifications for Vertiports.**

Used as the vertiport design and terminology reference family for `02-Vertiports`.

## [FAA-LAUNCH]

**14 CFR Part 450 — Launch and Reentry License Requirements.**

Used as the launch, reentry, licensing, safety, and spaceport terminology reference family for `03-Spaceports-and-Launchers`.

## [ECSS]

**European Cooperation for Space Standardization — ECSS Standards.**

Used as the European space standardization reference family for space infrastructure, ground systems, project management, product assurance, and engineering governance.

## [IAQG-9100]

**IAQG 9100 — Quality Management Systems Requirements for Aviation, Space and Defense Organizations.**

Used as the aerospace quality-management reference family for infrastructure suppliers, operators, production systems, maintenance systems, and lifecycle governance.

## [ISO-9000]

**ISO 9000 — Quality Management Systems, Fundamentals and Vocabulary.**

Used as the general quality-management vocabulary reference family.

## [ISO-55000]

**ISO 55000 — Asset Management, Vocabulary, Overview and Principles.**

Used as the asset-management reference family for infrastructure lifecycle, risk, value, and governance principles.

## [ISO-31000]

**ISO 31000 — Risk Management.**

Used as the risk-management reference family for hazard, risk, control, and governance terminology.

---

# Governance Rule

Any child document under `I-Infrastructures` shall use the definitions in this document unless a lower-level document declares a stricter, more specific, or programme-controlled definition.

If a child document introduces a new term, it shall include:

1. the term;
2. the definition;
3. the section where it applies;
4. the source or citation key, if externally derived;
5. the relation to existing controlled terminology;
6. the lifecycle status of the definition.

---

# Acceptance Criteria

This document is acceptable when:

* Core infrastructure terms are defined.
* Section-specific terminology is covered.
* Abbreviations are listed.
* Citation keys are declared.
* Definitions are reusable across child sections.
* No definition conflicts with the parent `00-00-Scope-and-Purpose`.
* The document can be used as the terminology baseline for `I-Infrastructures`.

---

# Summary

`00-01-Definitions` provides the controlled terminology baseline for the `I-Infrastructures` axis.

It defines infrastructure, assets, airports, vertiports, spaceports, launchers, maintenance hangars, assemblies, FAL, test infrastructure, hydrogen and energy infrastructure, digital operational infrastructure, safety, security, access control, lifecycle governance, and OPT-IN interfaces.

```
```
