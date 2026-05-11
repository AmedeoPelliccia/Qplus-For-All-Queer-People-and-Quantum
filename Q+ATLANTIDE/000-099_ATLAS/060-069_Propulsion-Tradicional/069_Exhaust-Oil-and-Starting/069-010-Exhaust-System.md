---
document_id: "QATL-ATLAS-1000-ATLAS-060-069-069-010-EXHAUST-SYSTEM"
register: ATLAS-1000
title: "Exhaust System"
ata: "ATA 69"
sns: "069-010-00"
subsection: "069"
subsubject_code: "010"
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
s1000d_dmc: "DMC-AMPEL360E-EWTW-0069-010"
---

# Exhaust System

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![ATA: ATA 69](https://img.shields.io/badge/ATA-69-green)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-brightgreen)

---

## §1 Purpose

Specifies the exhaust system of the AMPEL360E eWTW turbofan installation. The fixed convergent exhaust nozzle discharges both the core (hot) and fan (cold) streams through a mixer nozzle arrangement to minimise jet noise. No thrust reverser is installed on the eWTW baseline.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA reference | ATA 69-010 |
| S1000D SNS | 069-010-00 |

---

## §3 Exhaust System Architecture ![DRAFT]

| Component | Material | Function |
|---|---|---|
| Core exhaust duct (inner) | Inconel 625 | Channels hot gas from LPT exit to nozzle |
| Fan duct (outer annulus) | Titanium alloy Ti-6Al-4V | Channels fan bypass stream |
| Mixer nozzle | Inconel 625 + Ti fairings | Merges core + fan streams; reduces jet shear noise |
| Acoustic liner panels (x4) | Aluminium honeycomb + CFRP face sheet | Attenuates LPT noise in aft duct |
| Exhaust nozzle plug (centerbody) | Inconel 718 | Shapes jet profile; reduces core exhaust noise |
| Nozzle exit flange | Inconel 625 | Structural attachment to nacelle aft frame |

---

## §4 Key Parameters ![TBD]

| Parameter | Value | Status |
|---|---|---|
| Nozzle throat area (core) | ![TBD] m² | ![TBD] |
| Bypass nozzle exit area | ![TBD] m² | ![TBD] |
| Max core exhaust temperature | 630 °C (continuous), 660 °C (T/O 5 min) | Pending OEM confirmation |
| Nozzle Cv (velocity coefficient) | ≥ 0.99 | ![TBD] |
| Acoustic liner insertion loss | ≥ 3 dB at 3.15 kHz 1/3-octave | ![TBD] |

---

## §5 Interfaces

| Interface | Connected System | Data |
|---|---|---|
| LPT exit (ATA 63) | Engine turbine | Hot gas stream |
| Fan duct (ATA 62) | Bypass stream | Cold fan air |
| Nacelle aft frame (ATA 54) | Structural | Nozzle attachment |
| FADEC (ATA 73) | Engine control | EGT sensor input from exhaust frame |

---

## §6 Maintenance

| Task | Interval | Notes |
|---|---|---|
| Exhaust nozzle visual inspection | C-check | Check for cracks, delamination of liner panels |
| Acoustic liner bond check | C-check | Tap test per NDT AMM procedure |
| Nozzle exit geometry measurement | 12 000 FH | Confirm throat area within ±1 % |

---

## §7 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-069-010-001 | Confirm nozzle throat area from OEM final aero design | Q-GREENTECH | 2026-Q4 |

---

## §8 Change Log

| Rev | Date | Author | Description |
|---|---|---|---|
| 0.1 | 2026-05-11 | @copilot | Initial DRAFT — AMPEL360E eWTW contextualization |
