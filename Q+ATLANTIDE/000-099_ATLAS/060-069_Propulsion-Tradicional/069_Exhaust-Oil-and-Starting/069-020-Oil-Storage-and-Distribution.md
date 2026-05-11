---
document_id: "QATL-ATLAS-1000-ATLAS-060-069-069-020-OIL-STORAGE-AND-DISTRIBUTION"
register: ATLAS-1000
title: "Oil Storage and Distribution"
ata: "ATA 69"
sns: "069-020-00"
subsection: "069"
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
s1000d_dmc: "DMC-AMPEL360E-EWTW-0069-020"
---

# Oil Storage and Distribution

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![ATA: ATA 69](https://img.shields.io/badge/ATA-69-green)
![Q-Division: Q-MECHANICS](https://img.shields.io/badge/Q--Division-Q--MECHANICS-orange)

---

## §1 Purpose

Specifies the oil tank, supply pump, and distribution network for the AMPEL360E eWTW turbofan dry-sump oil system. Synthetic oil (MIL-PRF-23699) is stored in a gearbox-mounted tank and distributed under pressure to all bearing sumps.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA reference | ATA 69-020 |
| S1000D SNS | 069-020-00 |

---

## §3 Oil System Architecture ![DRAFT]

| Component | Specification | Location |
|---|---|---|
| Oil tank | 12 L capacity; aluminium alloy; pressurised headspace (2 kPa) | Accessory Gearbox (AGB) zone |
| Pressure pump | Gear-type; flow rate ![TBD] L/min at idle / max | AGB gear train |
| Scavenge pump | Multi-element gear-type; combined flow ≥ 2× pressure pump | AGB gear train |
| Oil filter | 15-micron bypass protected; differential pressure indicator (DPI) | AGB filter housing |
| Magnetic Chip Detector (MCD) | Fuzz burn-off circuit; FADEC-monitored | Main scavenge return line |
| Oil fill/drain point | External; cowl-accessible; level sight glass | AGB forward face |

---

## §4 Oil Distribution Schematic — Mermaid Diagram

```mermaid
flowchart LR
    TANK[Oil Tank 12 L] --> PRESS_PUMP[Pressure Pump AGB]
    PRESS_PUMP --> FILTER[15μ Filter]
    FILTER --> FAN_BRG[Fan Bearing Sump]
    FILTER --> INT_BRG[IGB Bearing Sump]
    FILTER --> HPC_BRG[HPC Bearing Sump]
    FILTER --> HPT_BRG[HPT Bearing Sump]
    FILTER --> LPT_BRG[LPT Bearing Sump]
    FILTER --> AGB_LUB[AGB Gearbox Lubrication]
    FAN_BRG & INT_BRG & HPC_BRG & HPT_BRG & LPT_BRG & AGB_LUB --> SCAV[Scavenge Pumps x5]
    SCAV --> DEAER[De-aerator]
    DEAER --> MCD[Magnetic Chip Detector]
    MCD --> FOHE[FOHE ATA 64]
    FOHE --> AOHE[AOHE Ram Air]
    AOHE --> TANK
```

---

## §5 Oil Specification

| Property | Value |
|---|---|
| Oil type | Synthetic turbine oil MIL-PRF-23699 Type II or equivalent |
| Viscosity (40 °C) | ~5 cSt |
| Flash point | > 250 °C |
| Auto-ignition temp | > 350 °C |
| Change interval | 3 000 FH or 2 years (whichever sooner) |

---

## §6 Interfaces

| Interface | Connected System | Data |
|---|---|---|
| Oil filter housing (ATA 69-030) | Cooling and filtration | Oil-out to coolers |
| FADEC (ATA 73) | Engine control | Oil pressure/temperature monitoring |
| FOHE (ATA 64) | Fuel–oil heat exchanger | Thermal load exchange |

---

## §7 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-069-020-001 | Confirm oil tank capacity (12 L) and scavenge-to-pressure pump ratio with OEM | Q-MECHANICS | 2026-Q4 |

---

## §8 Change Log

| Rev | Date | Author | Description |
|---|---|---|---|
| 0.1 | 2026-05-11 | @copilot | Initial DRAFT — AMPEL360E eWTW contextualization |
