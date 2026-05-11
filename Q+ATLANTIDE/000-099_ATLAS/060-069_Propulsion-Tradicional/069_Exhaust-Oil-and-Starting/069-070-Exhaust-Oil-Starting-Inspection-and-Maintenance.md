---
document_id: "QATL-ATLAS-1000-ATLAS-060-069-069-070-EXHAUST-OIL-STARTING-INSPECTION-MAINTENANCE"
register: ATLAS-1000
title: "Exhaust, Oil and Starting — Inspection and Maintenance"
ata: "ATA 69"
sns: "069-070-00"
subsection: "069"
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
s1000d_dmc: "DMC-AMPEL360E-EWTW-0069-070"
---

# Exhaust, Oil and Starting — Inspection and Maintenance

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![ATA: ATA 69](https://img.shields.io/badge/ATA-69-green)
![Q-Division: Q-MECHANICS](https://img.shields.io/badge/Q--Division-Q--MECHANICS-orange)

---

## §1 Purpose

Consolidates scheduled and unscheduled maintenance tasks for the ATA 69 Exhaust System, Oil System, and Starting System on the AMPEL360E eWTW.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA reference | ATA 69-070 |
| S1000D SNS | 069-070-00 |

---

## §3 Scheduled Maintenance Task List ![DRAFT]

| Task | Subsystem | Task Type | Interval | Man-Hours | Access |
|---|---|---|---|---|---|
| Oil quantity and quality check | Oil | Service | 500 FH / transit | 0.25 h | Cowl fill point |
| Magnetic chip detector inspection | Oil | Inspection | A-check | 0.5 h | Scavenge line access |
| Oil filter element replacement | Oil | Replacement | 3 000 FH | 1.0 h | AGB filter housing |
| FOHE external leak check | Oil / Fuel | Inspection | C-check | 1.0 h | Pylon access |
| AOHE bypass valve functional test | Oil | Functional | B-check | 0.5 h | Nacelle inlet zone |
| Exhaust nozzle visual inspection | Exhaust | Inspection | C-check | 1.5 h | Aft nacelle access |
| Acoustic liner bond check (tap test) | Exhaust | NDT | C-check | 2.0 h | Aft nacelle |
| SPEC BITE download | Starting | Inspection | A-check | 0.25 h | CMS terminal |
| PMSG oil lubrication check (AGB) | Starting | Service | 3 000 FH | 0.5 h | AGB access |
| PMSG service life status check | Starting | Record check | 25 000 FH | 0.1 h | FADEC / CMS |

---

## §4 Unscheduled / Conditional Tasks

| Condition | Task | Man-Hours |
|---|---|---|
| MCD chip detection (single trip) | Oil analysis sample; inspect MCD plug | 1.0 h |
| MCD chip detection (re-trip < 5 min) | Engine borescope inspection — all bearing sumps | 6.0 h |
| Hot start event (EGT > start limit) | EGT harness inspection; FADEC NVM download | 2.0 h |
| Exhaust nozzle crack indication | Eddy current NDT + engineering disposition | 4.0 h |
| SPEC/PMSG fault code logged | SPEC BITE isolation; LRU replace if BER | 3.0 h |

---

## §5 Special Tools

| Tool | Part Number | Purpose |
|---|---|---|
| Oil analysis kit | OA-KIT-TBD | In-situ oil quality analysis at fill point |
| MCD extraction tool | MCD-XT-TBD | Chip detector removal without oil spillage |
| Tap test hammer + calibration standard | TAP-TBD | Acoustic liner disbond detection |
| SPEC GSE interface | SPEC-GSE-TBD | BITE download and SPEC configuration |
| CMS ground terminal | CMS-GT-TBD | Maintenance data download |

---

## §6 Interfaces

| Interface | Connected System | Data |
|---|---|---|
| CMS (ATA 45) | Maintenance ground | BITE results, fault codes, event logs |
| FADEC GSE (ATA 73) | Engine test | Engine ground runs and post-maintenance tests |

---

## §7 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-069-070-001 | Finalise exhaust nozzle NDT procedure for crack detection with DT engineering | Q-MECHANICS | 2027-Q1 |

---

## §8 Change Log

| Rev | Date | Author | Description |
|---|---|---|---|
| 0.1 | 2026-05-11 | @copilot | Initial DRAFT — AMPEL360E eWTW contextualization |
