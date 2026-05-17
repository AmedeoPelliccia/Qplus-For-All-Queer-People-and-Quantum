---
document_id: "QATL-ATLAS-1000-ATLAS-060-069-068-070-ENGINE-INDICATING-TEST-AND-MAINTENANCE"
register: ATLAS-1000
title: "Engine Indicating Test and Maintenance"
ata: "ATA 68"
sns: "068-070-00"
subsection: "068"
subsubject_code: "070"
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
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0068-070"
standard_scope: agnostic
programme_specific: false
---

# Engine Indicating Test and Maintenance

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![ATA: ATA 68](https://img.shields.io/badge/ATA-68-green)
![Q-Division: Q-MECHANICS](https://img.shields.io/badge/Q--Division-Q--MECHANICS-orange)

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Engine Indicating Test and Maintenance`.

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
## §3 Scheduled Maintenance Tasks ![DRAFT]

| Task | Task Type | Interval | Man-Hours | Access |
|---|---|---|---|---|
| BITE download and review (EDC + FADEC) | Inspection | A-check (500 FH) | 0.5 h | CMS terminal |
| EGT thermocouple continuity check | Inspection | 6 000 FH | 1.0 h/engine | Engine cowl open |
| Vibration sensor calibration (N1/N2) | Calibration | 12 000 FH | 2.0 h/engine | Fan cowl open; calibration shaker |
| N1/N2 speed sensor check | Functional | 12 000 FH | 1.0 h/engine | Fan/HPC access |
| EDC LRU replacement | On condition | As required | 2.0 h | Pylon forward zone |
| EGT harness replacement | On condition | As required | 4.0 h | Engine cowl removal |
| Standby N1 indicator functional test | Functional | B-check | 0.25 h | Cockpit centre panel |

---

## §4 BITE Test Procedure

1. Connect CMS terminal to aircraft maintenance port.
2. Select `ENGINE INDICATING → BITE TEST → ALL SENSORS`.
3. BITE automatically injects known test signals into all EDC input channels.
4. Review PASS/FAIL results for each sensor channel.
5. Download NVM snapshot for off-aircraft analysis if any FAIL result is detected.

---

## §5 Special Tools

| Tool | Part Number | Purpose |
|---|---|---|
| TC Continuity Tester | TCT-PN-TBD | EGT harness open-circuit check |
| Calibration Shaker | SHAKER-PN-TBD | Vibration sensor calibration |
| EDC GSE Interface | EDC-GSE-TBD | EDC configuration and BITE |
| CMS Ground Terminal | CMS-GT-TBD | BITE download and maintenance reporting |

---

## §6 Interfaces

| Interface | Connected System | Data |
|---|---|---|
| CMS (ATA 45) | Maintenance ground system | BITE results, NVM download |
| FADEC GSE (ATA 73) | Engine test equipment | FADEC configuration and test |

---

## §7 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-068-070-001 | Finalise EGT harness replacement man-hour estimate with OEM | Q-MECHANICS | 2026-Q4 |

---

## §8 Change Log

| Rev | Date | Author | Description |
|---|---|---|---|
| 0.1 | 2026-05-11 | @copilot | Initial DRAFT — programme-defined aircraft type contextualization |
