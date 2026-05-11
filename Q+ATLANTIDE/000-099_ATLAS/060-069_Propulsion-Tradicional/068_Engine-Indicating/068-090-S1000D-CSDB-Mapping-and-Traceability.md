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
s1000d_dmc: "DMC-AMPEL360E-EWTW-0068-090"
---

# Engine Indicating — S1000D CSDB Mapping and Traceability

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![ATA: ATA 68](https://img.shields.io/badge/ATA-68-green)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-brightgreen)

---

## §1 Purpose

Provides the S1000D Data Module Code (DMC) mapping for all ATA 68 Engine Indicating content on the AMPEL360E eWTW and establishes traceability between ATLAS subsubject documents and S1000D CSDB data modules.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA reference | ATA 68-090 |
| S1000D SNS | 068-090-00 |
| S1000D Issue | 5.0 |

---

## §3 DMC Mapping Table

| ATLAS Document | Title | S1000D DMC | InfoCode | Status |
|---|---|---|---|---|
| 068-000 | Engine Indicating General | DMC-AMPEL360E-EWTW-0068-000-A-040A-A | 040A — Description | ![TBD] |
| 068-010 | Engine Parameter Indication | DMC-AMPEL360E-EWTW-0068-010-A-040A-A | 040A | ![TBD] |
| 068-020 | Engine Warning and Caution | DMC-AMPEL360E-EWTW-0068-020-A-040A-A | 040A | ![TBD] |
| 068-030 | Engine Sensors and Transducers | DMC-AMPEL360E-EWTW-0068-030-A-040A-A | 040A | ![TBD] |
| 068-040 | Engine Data Concentrators | DMC-AMPEL360E-EWTW-0068-040-A-040A-A | 040A | ![TBD] |
| 068-050 | Engine Health and Trend Monitoring | DMC-AMPEL360E-EWTW-0068-050-A-040A-A | 040A | ![TBD] |
| 068-060 | Engine Display and Crew Interface | DMC-AMPEL360E-EWTW-0068-060-A-040A-A | 040A | ![TBD] |
| 068-070 | Test and Maintenance | DMC-AMPEL360E-EWTW-0068-070-A-520-A | 520 — Removal/Installation | ![TBD] |
| 068-080 | Monitoring, Diagnostics, Interfaces | DMC-AMPEL360E-EWTW-0068-080-A-040A-A | 040A | ![TBD] |
| 068-090 | S1000D CSDB Mapping | DMC-AMPEL360E-EWTW-0068-090-A-040A-A | 040A | This document |

---

## §4 S1000D SNS Hierarchy

```
systemCode:    068     (Engine Indicating)
subSystemCode: 0       (General)
subSubSys:     00      (General overview)
assyCode:      00      (Top assembly)
disassyCode:   A       (Variant A — AMPEL360E eWTW)
infoCode:      040A    (Description)
```

---

## §5 CSDB Publication Applicability

All ATA 68 data modules are applicable to:
- **Aircraft Type:** AMPEL360E eWTW
- **Series:** All series (A1, A2 per AMPEL360E variant definition)
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
| 0.1 | 2026-05-11 | @copilot | Initial DRAFT — AMPEL360E eWTW contextualization |
