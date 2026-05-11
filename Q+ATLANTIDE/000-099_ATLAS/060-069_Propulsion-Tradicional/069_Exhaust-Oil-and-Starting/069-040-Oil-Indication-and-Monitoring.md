---
document_id: "QATL-ATLAS-1000-ATLAS-060-069-069-040-OIL-INDICATION-AND-MONITORING"
register: ATLAS-1000
title: "Oil Indication and Monitoring"
ata: "ATA 69"
sns: "069-040-00"
subsection: "069"
subsubject_code: "040"
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
s1000d_dmc: "DMC-AMPEL360E-EWTW-0069-040"
---

# Oil Indication and Monitoring

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![ATA: ATA 69](https://img.shields.io/badge/ATA-69-green)
![Q-Division: Q-AIR](https://img.shields.io/badge/Q--Division-Q--AIR-blue)

---

## §1 Purpose

Specifies the oil monitoring and indication functions for the AMPEL360E eWTW engine oil system. Continuous FADEC monitoring of oil pressure, temperature, and quantity provides crew alerting and maintenance health data via ECAM and CMS.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA reference | ATA 69-040 |
| S1000D SNS | 069-040-00 |

---

## §3 Monitored Parameters and Limits ![DRAFT]

| Parameter | Normal Range | Caution | Warning | Sensor Type |
|---|---|---|---|---|
| Oil Pressure (OP) | 1.5–8 bar | 1.0–1.5 bar | < 1.0 bar | 4–20 mA transducer |
| Oil Temperature (OT) | 60–130 °C | 130–163 °C | > 163 °C | Pt100 RTD |
| Oil Quantity (OQ) | 30–100 % | 20–30 % | < 20 % | Capacitive sensor |
| Chip Detection (MCD) | No chips | Chip detected | N/A — fuzz burn-off | Magnetic pickup with burn-off |

---

## §4 ECAM Oil Synoptic Display

Lower ECAM Engine Synoptic page shows for each engine:
- Oil pressure gauge (analogue arc with digital readout)
- Oil temperature digital readout
- Oil quantity percentage bar
- Chip detection annunciator (amber lamp)

All values colour-coded per §3 limits (green / amber / red).

---

## §5 FADEC Oil Health Monitoring

FADEC monitors oil system trends over time and performs the following automated actions:
- **Low oil pressure warning:** Triggers ECAM Warning `ENG x OIL LO PR`; FADEC records in NVM.
- **High oil temperature warning:** Triggers ECAM Caution `ENG x OIL HI TEMP`; FADEC adjusts AOHE bypass valve.
- **Chip detection:** Triggers ECAM Advisory `ENG x OIL CHIP`; FADEC activates fuzz burn-off circuit; if re-trip occurs in < 5 minutes, triggers Caution for crew action.
- **Oil consumption rate tracking:** FADEC calculates OQ consumption per flight hour for EHM trending (ATA 68-050).

---

## §6 Interfaces

| Interface | Connected System | Data |
|---|---|---|
| FADEC (ATA 73) | Engine controller | Oil parameter acquisition |
| ECAM (ATA 31) | Crew display | Oil synoptic page data |
| CMS (ATA 45) | Maintenance | Oil exceedance logs; chip detection events |
| EHM (ATA 68-050) | Health monitoring | Oil consumption trend data |

---

## §7 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-069-040-001 | Confirm MCD fuzz burn-off circuit qualification test plan | Q-MECHANICS | 2026-Q4 |

---

## §8 Change Log

| Rev | Date | Author | Description |
|---|---|---|---|
| 0.1 | 2026-05-11 | @copilot | Initial DRAFT — AMPEL360E eWTW contextualization |
