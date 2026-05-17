---
document_id: "QATL-ATLAS-1000-ATLAS-060-069-068-090-S1000D-CSDB-MAPPING"
register: ATLAS-1000
title: "Engine Indicating — S1000D CSDB Mapping and Traceability"
ata: "ATA 68"
sns: "068-090-00"
subsection: "068"
subsubject_code: "090"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-MECHANICS, Q-AIR, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-11"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
parent_subsubject_doc: "./README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0068-090"
standard_scope: agnostic
programme_specific: false
---

# Engine Indicating — S1000D CSDB Mapping and Traceability

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![ATA: ATA 68](https://img.shields.io/badge/ATA-68-green)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-brightgreen)

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Engine Indicating — S1000D CSDB Mapping and Traceability`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 Applicability

| Applicability Level | Rule |
|---|---|
| Standard taxonomy | Applies to the ATLAS node `068` |
| Programme implementation | Conditional; determined by programme architecture, trade studies, certification basis, and applicability model |
| Product configuration | Defined in the programme-specific configuration baseline |
| Effectivity | Defined in the programme CSDB / applicability layer |
| Non-applicability | Must be explicitly stated in the programme impact-study branch when excluded |
## §3 DMC Mapping Table

| ATLAS Document | Title | S1000D DMC | InfoCode | Status |
|---|---|---|---|---|
| 068-000 | Engine Indicating General | DMC-<PROGRAMME>-<VARIANT>-0068-000-A-040A-A | 040A — Description | ![TBD] |
| 068-010 | Engine Parameter Indication | DMC-<PROGRAMME>-<VARIANT>-0068-010-A-040A-A | 040A | ![TBD] |
| 068-020 | Engine Warning and Caution | DMC-<PROGRAMME>-<VARIANT>-0068-020-A-040A-A | 040A | ![TBD] |
| 068-030 | Engine Sensors and Transducers | DMC-<PROGRAMME>-<VARIANT>-0068-030-A-040A-A | 040A | ![TBD] |
| 068-040 | Engine Data Concentrators | DMC-<PROGRAMME>-<VARIANT>-0068-040-A-040A-A | 040A | ![TBD] |
| 068-050 | Engine Health and Trend Monitoring | DMC-<PROGRAMME>-<VARIANT>-0068-050-A-040A-A | 040A | ![TBD] |
| 068-060 | Engine Display and Crew Interface | DMC-<PROGRAMME>-<VARIANT>-0068-060-A-040A-A | 040A | ![TBD] |
| 068-070 | Test and Maintenance | DMC-<PROGRAMME>-<VARIANT>-0068-070-A-520-A | 520 — Removal/Installation | ![TBD] |
| 068-080 | Monitoring, Diagnostics, Interfaces | DMC-<PROGRAMME>-<VARIANT>-0068-080-A-040A-A | 040A | ![TBD] |
| 068-090 | S1000D CSDB Mapping | DMC-<PROGRAMME>-<VARIANT>-0068-090-A-040A-A | 040A | This document |

---

## §4 S1000D SNS Hierarchy

```
systemCode:    068     (Engine Indicating)
subSystemCode: 0       (General)
subSubSys:     00      (General overview)
assyCode:      00      (Top assembly)
disassyCode:   A       (Variant A — programme-defined aircraft type)
infoCode:      040A    (Description)
```

---

## §5 CSDB Publication Applicability

All ATA 68 data modules are applicable to:
- **Aircraft Type:** programme-defined aircraft type
- **Series:** All series (A1, A2 per [PROGRAMME-AIRCRAFT] variant definition)
- **Effectivity:** MSN 001 onwards

---

## §6 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-068-090-001 | Create S1000D XML shells for all 10 ATA 68 DMCs in CSDB | Q-INDUSTRY | 2027-Q1 |

---

## §7 Change Log

| Rev | Date | Author | Description |
|---|---|---|---|
| 0.1 | 2026-05-11 | @copilot | Initial DRAFT — programme-defined aircraft type contextualization |
