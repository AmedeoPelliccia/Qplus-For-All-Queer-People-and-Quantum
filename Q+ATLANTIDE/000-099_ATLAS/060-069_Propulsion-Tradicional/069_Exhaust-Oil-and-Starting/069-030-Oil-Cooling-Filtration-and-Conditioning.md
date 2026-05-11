---
document_id: "QATL-ATLAS-1000-ATLAS-060-069-069-030-OIL-COOLING-FILTRATION-AND-CONDITIONING"
register: ATLAS-1000
title: "Oil Cooling, Filtration and Conditioning"
ata: "ATA 69"
sns: "069-030-00"
subsection: "069"
subsubject_code: "030"
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
s1000d_dmc: "DMC-AMPEL360E-EWTW-0069-030"
---

# Oil Cooling, Filtration and Conditioning

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![ATA: ATA 69](https://img.shields.io/badge/ATA-69-green)
![Q-Division: Q-MECHANICS](https://img.shields.io/badge/Q--Division-Q--MECHANICS-orange)

---

## §1 Purpose

Specifies the oil cooling, filtration, and conditioning subsystems for the AMPEL360E eWTW engine oil circuit. Two heat exchangers in series — FOHE (fuel–oil) and AOHE (air–oil) — maintain oil temperature within operating limits, while the 15-micron filter protects all rotating components.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA reference | ATA 69-030 |
| S1000D SNS | 069-030-00 |

---

## §3 Oil Cooling Architecture ![DRAFT]

### Primary Cooler — FOHE (Fuel–Oil Heat Exchanger)
The FOHE is a shell-and-tube aluminium heat exchanger mounted in the engine fuel supply line (ATA 64). Engine fuel acts as the cold-side fluid, cooling the hot scavenge oil and simultaneously preheating fuel to prevent fuel filter icing. The FOHE contributes approximately 70 % of total oil heat rejection at cruise.

### Secondary Cooler — AOHE (Air–Oil Heat Exchanger)
The AOHE is a plate-fin heat exchanger cooled by ram air drawn from the nacelle inlet. It provides overflow cooling capacity when fuel flow is insufficient (e.g., at low thrust / descent). The AOHE bypass valve (thermostatic) modulates airflow to maintain oil temperature between 80 °C and 130 °C.

### Oil De-aerator
A centrifugal de-aerator removes entrained air from the scavenge stream before the oil enters the cooler train. This prevents oil foaming and ensures accurate oil quantity sensing.

---

## §4 Oil Thermal Budget ![TBD]

| Operating Point | Oil Inlet Temp | Oil Outlet Temp (target) | FOHE Duty | AOHE Duty |
|---|---|---|---|---|
| Take-off ISA SL | 100 °C | 115 °C | ![TBD] kW | ![TBD] kW |
| Cruise FL350 ISA | 90 °C | 110 °C | ![TBD] kW | ![TBD] kW |
| Descent idle | 80 °C | 85 °C | ![TBD] kW | Minimal |

---

## §5 Interfaces

| Interface | Connected System | Data |
|---|---|---|
| FOHE hot-side (ATA 64) | Engine fuel system | Oil heat → fuel pre-heat |
| AOHE ram air (nacelle inlet) | Nacelle aerodynamics | Air-side cooling flow |
| Oil filter assembly (ATA 69-020) | Oil distribution | Filtered oil supply |
| FADEC (ATA 73) | Engine control | Oil temperature monitoring |

---

## §6 Maintenance

| Task | Interval | Notes |
|---|---|---|
| Oil filter element replacement | 3 000 FH | Differential pressure indicator check at each A-check |
| FOHE external inspection | C-check | Leak check; fouling inspection |
| AOHE bypass valve functional test | B-check | Confirm thermostatic valve operation 80–130 °C |

---

## §7 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-069-030-001 | Confirm FOHE and AOHE thermal capacities with OEM heat exchanger sizing | Q-MECHANICS | 2026-Q4 |

---

## §8 Change Log

| Rev | Date | Author | Description |
|---|---|---|---|
| 0.1 | 2026-05-11 | @copilot | Initial DRAFT — AMPEL360E eWTW contextualization |
