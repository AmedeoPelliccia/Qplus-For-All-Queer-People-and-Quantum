---
document_id: "QATL-ATLAS-1000-ATLAS-060-069-068-020-ENGINE-WARNING-AND-CAUTION-INDICATION"
register: ATLAS-1000
title: "Engine Warning and Caution Indication"
ata: "ATA 68"
sns: "068-020-00"
subsection: "068"
subsubject_code: "020"
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
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0068-020"
standard_scope: agnostic
programme_specific: false
---

# Engine Warning and Caution Indication

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![ATA: ATA 68](https://img.shields.io/badge/ATA-68-green)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-brightgreen)

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Engine Warning and Caution Indication`.

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
## §3 Alert Classification ![DRAFT]

| Level | Colour | Audio | Crew Action |
|---|---|---|---|
| Warning (L3) | Red | Continuous chime | Immediate action per QRH |
| Caution (L2) | Amber | Single chime | Timely action per QRH |
| Advisory (L1) | Amber (advisory colour) | No audio | Monitor; log for maintenance |

---

## §4 Engine ECAM Alert Catalogue (Primary) ![DRAFT]

| ECAM Message | Trigger | Level | Crew Action |
|---|---|---|---|
| ENG 1 (2) EGT OVERLIMIT | EGT > 960 °C for > 1 s | Warning | FADEC auto-derate; QRH engine overlimit procedure |
| ENG 1 (2) OIL LO PR | Oil pressure < 1.0 bar | Warning | Monitor RPM reduction; if confirmed: engine shutdown |
| ENG 1 (2) VIB HI | VIB > 6 mm/s | Warning | Reduce thrust; QRH vibration procedure |
| ENG 1 (2) N1 OVERLIMIT | N1 > 105 % | Warning | FADEC protection; QRH overlimit procedure |
| ENG 1 (2) FAIL | FADEC detects engine flame-out | Warning | Engine restart or shutdown per QRH |
| ENG 1 (2) OIL LO QTY | OQ < 20 % | Caution | Monitor; land at nearest suitable airport |
| ENG 1 (2) EGT HI | EGT 900–960 °C sustained | Caution | Monitor; FADEC derate advisory |
| ENG 1 (2) FADEC FAULT | FADEC CH-A or CH-B fail | Caution | Confirm thrust available; QRH FADEC fault procedure |

---

## §5 Alert Generation Flow — Mermaid Diagram

```mermaid
flowchart LR
    FADEC[FADEC EEC — Parameter Monitor] -->|Limit breach detected| AFDX_ALERT[AFDX Alert Message]
    AFDX_ALERT --> IAS[Integrated Avionics System]
    IAS --> ECAM[ECAM Alert Page]
    IAS --> MWL[Master Warning Light]
    IAS --> AUDIO[Audio Warning Chime]
    ECAM --> QRH_LINK[QRH Action Procedure Link]
```

---

## §6 Interfaces

| Interface | Connected System | Data |
|---|---|---|
| FADEC (ATA 73) | Alert source | Limit breach flags |
| ECAM / IAS (ATA 31) | Alert display | Level/colour/audio outputs |
| MWS (ATA 31) | Crew attention | Master warning/caution light activation |
| CMS (ATA 45) | Maintenance log | Alert event timestamps |

---

## §7 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-068-020-001 | Finalise full ECAM alert catalogue (50+ engine messages) | Q-AIR / safety | 2027-Q1 |

---

## §8 Change Log

| Rev | Date | Author | Description |
|---|---|---|---|
| 0.1 | 2026-05-11 | @copilot | Initial DRAFT — programme-defined aircraft type contextualization |
