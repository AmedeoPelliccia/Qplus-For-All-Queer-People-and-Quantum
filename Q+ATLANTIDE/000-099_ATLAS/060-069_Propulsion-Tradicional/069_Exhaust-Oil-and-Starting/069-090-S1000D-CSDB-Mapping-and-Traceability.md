---
document_id: "QATL-ATLAS-1000-ATLAS-060-069-069-090-S1000D-CSDB-MAPPING"
register: ATLAS-1000
title: "Exhaust, Oil and Starting — S1000D CSDB Mapping and Traceability"
ata: "ATA 69"
sns: "069-090-00"
subsection: "069"
subsubject_code: "090"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-MECHANICS, Q-AIR, Q-INDUSTRY]
status: active
scope: agnostic-standard
governance_class: baseline
revision: "0.1"
date: "2026-05-11"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
parent_subsubject_doc: "./README.md"
s1000d_dmc: "DMC-<MODEL>-<SYSTEMDIFF>-069-090"
---

# Exhaust, Oil and Starting — S1000D CSDB Mapping and Traceability

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![ATA: ATA 69](https://img.shields.io/badge/ATA-69-green)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-brightgreen)

---

## §1 Purpose

Provides the S1000D Data Module Code (DMC) mapping for all ATA 69 Exhaust, Oil and Starting content on the <PROGRAMME> and establishes traceability between ATLAS subsubject documents and S1000D CSDB data modules.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Programme | (defined in programme implementation branch) |
| ATA reference | ATA 69-090 |
| S1000D SNS | 069-090-00 |
| S1000D Issue | 5.0 |

---

## §3 DMC Mapping Table

| ATLAS Document | Title | S1000D DMC | InfoCode | Status |
|---|---|---|---|---|
| 069-000 | Exhaust, Oil and Starting General | DMC-<MODEL>-<SYSTEMDIFF>-0069-000-A-040A-A | 040A — Description | ![TBD] |
| 069-010 | Exhaust System | DMC-<MODEL>-<SYSTEMDIFF>-0069-010-A-040A-A | 040A | ![TBD] |
| 069-020 | Oil Storage and Distribution | DMC-<MODEL>-<SYSTEMDIFF>-0069-020-A-040A-A | 040A | ![TBD] |
| 069-030 | Oil Cooling, Filtration and Conditioning | DMC-<MODEL>-<SYSTEMDIFF>-0069-030-A-040A-A | 040A | ![TBD] |
| 069-040 | Oil Indication and Monitoring | DMC-<MODEL>-<SYSTEMDIFF>-0069-040-A-040A-A | 040A | ![TBD] |
| 069-050 | Engine Starting System | DMC-<MODEL>-<SYSTEMDIFF>-0069-050-A-040A-A | 040A | ![TBD] |
| 069-060 | Starter Electric and Control Interfaces | DMC-<MODEL>-<SYSTEMDIFF>-0069-060-A-040A-A | 040A | ![TBD] |
| 069-070 | Inspection and Maintenance | DMC-<MODEL>-<SYSTEMDIFF>-0069-070-A-520-A | 520 — Removal/Installation | ![TBD] |
| 069-080 | Monitoring, Diagnostics, Interfaces | DMC-<MODEL>-<SYSTEMDIFF>-0069-080-A-040A-A | 040A | ![TBD] |
| 069-090 | S1000D CSDB Mapping | DMC-<MODEL>-<SYSTEMDIFF>-0069-090-A-040A-A | 040A | This document |

---

## §4 S1000D SNS Hierarchy

```
systemCode:    069     (Exhaust, Oil and Starting)
subSystemCode: 0       (General)
subSubSys:     00      (General overview)
assyCode:      00      (Top assembly)
disassyCode:   A       (Variant A — <PROGRAMME>)
infoCode:      040A    (Description)
```

---

## §5 CSDB Publication Applicability

All ATA 69 data modules are applicable to:
- **Aircraft Type:** <PROGRAMME>
- **Series:** All series (A1, A2 per programme variant definition)
- **Effectivity:** MSN 001 onwards

---

## §6 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-069-090-001 | Create S1000D XML shells for all 10 ATA 69 DMCs in CSDB | Q-INDUSTRY | 2027-Q1 |

---

## §7 Change Log

| Rev | Date | Author | Description |
|---|---|---|---|
| 0.1 | 2026-05-11 | @copilot | Initial DRAFT — <PROGRAMME> contextualization |
