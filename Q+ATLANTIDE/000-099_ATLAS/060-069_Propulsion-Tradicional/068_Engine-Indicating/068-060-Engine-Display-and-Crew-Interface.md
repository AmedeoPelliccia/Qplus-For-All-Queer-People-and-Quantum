---
document_id: "QATL-ATLAS-1000-ATLAS-060-069-068-060-ENGINE-DISPLAY-AND-CREW-INTERFACE"
register: ATLAS-1000
title: "Engine Display and Crew Interface"
ata: "ATA 68"
sns: "068-060-00"
subsection: "068"
subsubject_code: "060"
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
s1000d_dmc: "DMC-AMPEL360E-EWTW-0068-060"
---

# Engine Display and Crew Interface

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![ATA: ATA 68](https://img.shields.io/badge/ATA-68-green)
![Q-Division: Q-AIR](https://img.shields.io/badge/Q--Division-Q--AIR-blue)

---

## §1 Purpose

Defines the crew interface to engine indicating on the AMPEL360E eWTW, including ECAM page layout, display logic, control panel interface, and standby instrument provisions per CS-25 §25.1305 and §25.1321.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA reference | ATA 68-060 |
| S1000D SNS | 068-060-00 |

---

## §3 ECAM Engine Page Layout ![DRAFT]

**Upper ECAM (always displayed in flight):**
- Left engine column: N1 arc, EGT arc, digital FF, N2 digital, TLA position bar
- Right engine column: mirror layout
- Colour state: green (normal), amber (caution), red (warning)
- Max EGT line: fixed red arc boundary

**Lower ECAM (engine synoptic — displayed on demand or on engine alert):**
- Oil pressure gauges (both engines)
- Oil temperature
- Oil quantity
- Vibration trend bar (N1/N2)
- Fuel temperature advisory

---

## §4 Standby Engine Indication

Per CS-25 §25.1305, a standby independent N1 indicator is provided for each engine. The standby indicator is:
- Direct-driven from FADEC backup power (independent of AFDX IAS)
- Located on the centre instrument panel, below the main ECAM
- Colour LCD, 50 mm diameter, sunlight-readable

---

## §5 Display System Interface — Mermaid Diagram

```mermaid
flowchart LR
    FADEC --> AFDX --> IAS
    IAS --> UPPER_ECAM[Upper ECAM Display Unit]
    IAS --> LOWER_ECAM[Lower ECAM Display Unit]
    FADEC --> STANDBY_N1[Standby N1 Indicator CH-independent]
    IAS --> MFD[Multi-Function Display Engine Trend Page]
```

---

## §6 Interfaces

| Interface | Connected System | Data |
|---|---|---|
| IAS / ECAM (ATA 31) | Primary display | Engine parameter Virtual Links |
| FADEC (ATA 73) | Standby N1 source | Independent N1 backup channel |
| MFD (ATA 31) | EHM trend display | Performance trend pages |

---

## §7 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-068-060-001 | Complete CS-25 §25.1321 legibility analysis (luminance, contrast) | Q-AIR | 2026-Q4 |

---

## §8 Change Log

| Rev | Date | Author | Description |
|---|---|---|---|
| 0.1 | 2026-05-11 | @copilot | Initial DRAFT — AMPEL360E eWTW contextualization |
