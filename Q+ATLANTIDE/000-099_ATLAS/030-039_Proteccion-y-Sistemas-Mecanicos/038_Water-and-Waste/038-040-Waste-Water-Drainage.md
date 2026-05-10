---
document_id: "QATL-ATLAS-000099-ATLAS-030039-038-040"
title: "038-040 — Waste Water Drainage"
short_title: "Waste Water Drainage"
subsubject: "040"
subsubject_title: "Waste Water Drainage"
file_name: "038-040-Waste-Water-Drainage.md"
sns_reference: "038-04"
dmc_prefix: "DMC-AMPEL360E-EWTW-038-04"
programme: "AMPEL360e Wide Tube-and-Wing Family"
programme_link: "../../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/"
short_code: "eWTW"
register: "Q+ATLANTIDE"
register_link: "../../../../../Q+ATLANTIDE/"
architecture_band: "000-099_ATLAS"
architecture_band_link: "../../../"
architecture_band_title: "New Commercial Aircraft Architectures"
code_range: "030-039_Proteccion-y-Sistemas-Mecanicos"
code_range_link: "../../"
code_range_title: "Protección & Sistemas Mecánicos"
node_code: "038"
node_title: "Water and Waste"
node_link: "./"
parent_path: "Q+ATLANTIDE/000-099_ATLAS/030-039_Proteccion-y-Sistemas-Mecanicos/038_Water-and-Waste/"
parent_path_link: "./"
ata_reference: "ATA 38"
ata_reference_link: "#20-references"
s1000d_applicability: "S1000D-CSDB-compatible"
s1000d_link: "https://s1000d.org/"
domain: "A-Aerospace"
domain_link: "../../../../../IDEALE-ESG/A-Aerospace/"
primary_q_division: "Q-AIR"
primary_q_division_link: "../../../../../Q-Divisions/Q-AIR/"
support_q_divisions:
  - name: "Q-MECHANICS"
    link: "../../../../../Q-Divisions/Q-MECHANICS/"
  - name: "Q-DATAGOV"
    link: "../../../../../Q-Divisions/Q-DATAGOV/"
  - name: "Q-GREENTECH"
    link: "../../../../../Q-Divisions/Q-GREENTECH/"
  - name: "Q-GROUND"
    link: "../../../../../Q-Divisions/Q-GROUND/"
orb_functions:
  - name: "ORB-PMO"
    link: "../../../../../ORB-Functions/ORB-PMO/"
  - name: "ORB-LEG"
    link: "../../../../../ORB-Functions/ORB-LEG/"
classification: "open-technical-scaffold"
status: "programme-controlled-scaffold"
revision: "0.1.0"
created: "2026-05-10"
updated: "2026-05-10"
authoring_mode: "deterministic-technical-publication"
review_status: "to-be-reviewed-by-system-expert"
lifecycle_phase:
  - code: "LC02"
    title: "Requirements Definition"
  - code: "LC03"
    title: "Architecture Definition"
  - code: "LC05"
    title: "Detailed Design"
  - code: "LC06"
    title: "Verification Planning"
  - code: "LC10"
    title: "Certification / Approval"
  - code: "LC11"
    title: "Operation"
  - code: "LC12"
    title: "Maintenance / Support"
traceability:
  atlas_node: "038_Water-and-Waste"
  atlas_node_link: "./"
  parent_branch: "030-039_Proteccion-y-Sistemas-Mecanicos"
  parent_branch_link: "../../"
  csdb_path: "TBD"
  evidence_status: "draft"
  brex_status: "not-yet-validated"
  dmrl_status: "not-yet-frozen"
keywords:
  - "Q+ATLANTIDE"
  - "ATLAS"
  - "AMPEL360e"
  - "S1000D"
  - "ATA 38"
  - "Water and Waste"
  - "Waste Water Drainage"
  - "grey water"
  - "mast drain"
  - "EMH"
  - "Electric Mast Heater"
  - "gravity drain"
  - "PTFE drain line"
  - "p-trap"
  - "overboard drain"
---

# 038-040 — Waste Water Drainage
### AMPEL360e eWTW · ATA 38 · Q+ATLANTIDE ATLAS Scaffold

**Status:** <img src="https://img.shields.io/badge/DRAFT-yellow">  
**Revision:** 0.1.0 — 2026-05-10  
**Classification:** Q-AIR Primary | Q-MECHANICS / Q-DATAGOV / Q-GREENTECH / Q-GROUND Support

---

## §0 Hyperlink Policy

All cross-references within this document use relative Markdown links anchored to section headings within the Q+ATLANTIDE ATLAS repository. External regulatory references are cited by document identifier only. Internal DMC cross-references follow the pattern `DMC-AMPEL360E-EWTW-038-04-YYYY-A`. Where a parameter is not yet determined, the badge <img src="https://img.shields.io/badge/TBD-red"> is used inline.

---

## §1 Purpose

This document describes the **Waste Water Drainage** (grey water) subsystem of ATA 38 for the **AMPEL360e eWTW**. It covers:

1. Grey water sources: galley sinks and lavatory sinks (not toilet waste — that is ATA 38-050).
2. Gravity drain line routing from each sink to mast drain nozzles on the lower fuselage.
3. Mast drain nozzle design: overboard drain, electrically heated (EMH — Electric Mast Heater) to prevent ice blockage.
4. Drain line materials: PTFE-lined or polyethylene, slopes, supports, and p-trap cleanouts.
5. Galley waste condensate routing TBD (potential routing to grey drain).
6. Grey water retention requirement: regulatory review pending (OI-038-004).
7. Separation from black water (toilet waste) circuit: physical separation maintained at all points.
8. EMH monitoring: continuity check, CMC "DRAIN HTR FAULT" alert.

---

## §2 Applicability

| Item | Value |
|---|---|
| Aircraft Programme | AMPEL360e eWTW |
| Variant | All variants (unless noted) |
| ATA Chapter/Subsubject | 38-040 — Waste Water Drainage |
| Document Tier | Level 2 — SDD |
| Effectivity | MSN 0001 onwards <img src="https://img.shields.io/badge/TBD-red"> |
| Parent Document | [038-000](./038-000-Water-and-Waste-General.md) |

---

## §3 System/Function Overview

### 3.1 Grey Water Sources

Grey water on the eWTW originates from:

| Source | Location | Qty |
|---|---|---|
| Galley FWD sink | Forward galley area | 1 |
| Galley AFT sink | Aft galley area | 1 |
| Lavatory-1 sink | Lavatory-1 | 1 |
| Lavatory-2 sink | Lavatory-2 | 1 |
| Lavatory-3 sink | Lavatory-3 (TBD) | 1 (TBD) |
| Galley cooling condensate | Galley equipment drain | TBD |

**Total grey water drain points:** TBD (~4–5 sinks plus condensate TBD).

Grey water does **not** include toilet waste (black water). The toilet waste circuit is entirely separate and described in [038-050](./038-050-Toilet-and-Vacuum-Waste-System.md).

### 3.2 Drain System Overview

- **Principle:** Gravity drain — sloped drain lines (minimum slope: TBD, typically ≥ 1° / 17 mm per metre) routing downward from each sink p-trap through the bilge to the mast drain exit fittings on the lower fuselage.
- **Mast drain nozzles:** Overboard nozzles with electrically heated shrouds (EMH) to prevent ice formation at the drain outlet during flight in icing conditions. Drain overboard during flight; no grey water retention tank (TBD — OI-038-004).
- **Line material:** PTFE-lined stainless or polyethylene; food/grey-water compatible; easy to inspect and clean.
- **P-traps:** At each sink drain outlet; removable cleanout plugs for maintenance.

### 3.3 Grey Water Retention Option (OI-038-004)

Current baseline: grey water drains overboard via mast drains (no retention tank). Regulatory review in progress (OI-038-004). If regulations require grey water retention (e.g. port environmental rules), a grey water retention tank would be added aft of the bilge drain system. This document will be updated once OI-038-004 is resolved.

---

## §4 Scope

### 4.1 In-Scope

- Sink drain fittings (drain outlet at each galley and lavatory sink)
- P-trap assemblies (removable, at each sink)
- Grey water drain lines: PTFE-lined or PE; from p-trap to mast drain manifold
- Drain line supports and clamps (minimum slope maintained)
- Drain line cleanout access points (bilge access panels)
- Mast drain nozzle assemblies (drain nozzle + EMH heating element)
- Electric Mast Heater (EMH) units — resistance elements, power connection
- EMH monitoring: continuity (current/resistance monitor), CMC interface
- Grey water retention tank (if required by OI-038-004 — TBD)
- Separation from black water system (physical; no shared pipework)

### 4.2 Out-of-Scope

- Toilet waste system (black water): → [038-050](./038-050-Toilet-and-Vacuum-Waste-System.md)
- Potable water system: → [038-010](./038-010-Potable-Water-System.md)
- Galley sink fixtures (above drain outlet): → ATA 25
- Cabin condensate drain (if separate from grey drain): → ATA 21

---

## §5 Architecture Description

### 5.1 Drain Routing

```
[Galley FWD sink] ──[p-trap G1]──┐
[Galley AFT sink] ──[p-trap G2]──┤
                                  ├──[Grey drain collector line — bilge route]──→ [Mast Drain-1] → Overboard
[Lav-1 sink] ──[p-trap L1]───────┤
[Lav-2 sink] ──[p-trap L2]───────┤──[Grey drain line — bilge route]──────────→ [Mast Drain-2] → Overboard
[Lav-3 sink] ──[p-trap L3 TBD]──┘
[Galley condensate TBD] ──────────── route to grey drain TBD
```

**Mast drain count:** <img src="https://img.shields.io/badge/TBD-red"> (~2–4, OI-038-008). Each mast drain fitted with EMH.

### 5.2 Mast Drain Nozzle

The mast drain nozzle protrudes through the lower fuselage skin. It incorporates:
- **Drain channel:** PTFE-lined bore; drain opens downward/rearward.
- **EMH element:** Resistance heater bonded to nozzle body; keeps nozzle above freezing during flight.
- **Seal:** Sealed penetration through fuselage skin with aerodynamic fairing TBD.
- **Drain cover:** Open drain (no valve); gravity drains continuously during flight.

### 5.3 Drain Line Material and Slope

| Parameter | Requirement |
|---|---|
| Drain line material | PTFE-lined stainless steel or polyethylene (PE) TBD |
| Line OD | <img src="https://img.shields.io/badge/TBD-red"> (typical ~25–38 mm for gravity drain) |
| Minimum slope | <img src="https://img.shields.io/badge/TBD-red"> (typically ≥ 1°, ~17 mm/m) |
| Joints | Push-fit or flanged; cleanable TBD |
| Colour coding | Grey or clear (distinct from potable water) TBD |
| Insulation | Not required (ambient temp drain) unless routed through cold zone |

---

## §6 Functional Breakdown

| Component | Function | Qty | Status |
|---|---|---|---|
| Sink drain fitting (G1, G2) | Outlet fitting at galley sink | 2 | <img src="https://img.shields.io/badge/TBD-red"> |
| Sink drain fitting (L1, L2, L3) | Outlet fitting at lav sink | 3 (TBD) | <img src="https://img.shields.io/badge/TBD-red"> |
| P-trap (G1, G2, L1–L3) | Odour barrier; cleanout | TBD (1 per sink) | Removable |
| Grey drain lines | Gravity drain from p-trap to mast | TBD m | PTFE/PE |
| Drain line supports | Slope-maintaining clamps | TBD | Structural |
| Cleanout access panels | Bilge access for drain maintenance | TBD | Per design |
| Mast drain nozzles (MD-1, MD-2, etc.) | Overboard drain; aerodynamic | TBD (~2–4) | OI-038-008 |
| EMH units (EMH-1, EMH-2, etc.) | Prevent ice at mast drain | TBD (1 per mast) | TBD ~20–50 W each |
| EMH power connections | Low-voltage DC from ATA 24 | TBD | TBD |
| EMH monitoring (current/resist.) | Detect open-circuit heater fault | TBD (1 per EMH) | AFDX to CMC |
| Grey water retention tank (TBD) | Store grey water if regulations require | 0 (TBD if OI-038-004) | OI-038-004 |

---

## §7 System Context Diagram

```mermaid
flowchart LR
    ATA24["ATA 24\nElectrical Power\n(low-voltage DC for EMH)"]
    ATA25["ATA 25\nGalley / Lavatory\n(sink fixtures above drain)"]
    ATA21["ATA 21\nCabin\n(condensate TBD)"]
    CMC["CMC / ATA 45"]
    OB["Overboard\n(atmosphere)"]

    SINK_G1["Galley FWD\nSink"]
    SINK_G2["Galley AFT\nSink"]
    SINK_L1["Lav-1 Sink"]
    SINK_L2["Lav-2 Sink"]
    SINK_L3["Lav-3 Sink TBD"]
    PTRAP["P-Traps\n(at each sink)"]
    LINES["Grey Drain Lines\n(PTFE/PE, gravity slope)"]
    MD1["Mast Drain-1\n+ EMH-1"]
    MD2["Mast Drain-2\n+ EMH-2 TBD"]
    RTNK["Grey Water\nRetention Tank\n(TBD — OI-038-004)"]

    SINK_G1 --> PTRAP
    SINK_G2 --> PTRAP
    SINK_L1 --> PTRAP
    SINK_L2 --> PTRAP
    SINK_L3 --> PTRAP
    PTRAP --> LINES --> MD1 --> OB
    LINES --> MD2 --> OB
    LINES -.-> RTNK
    ATA24 -->|"DC power"| MD1
    ATA24 -->|"DC power"| MD2
    ATA25 -.->|"sink outlets"| SINK_G1
    ATA25 -.->|"sink outlets"| SINK_L1
    ATA21 -.->|"condensate TBD"| LINES
    MD1 -->|"EMH continuity"| CMC
    MD2 -->|"EMH continuity"| CMC
```

---

## §8 Internal Functional Architecture

```mermaid
flowchart TB
    SOURCES["Grey Water Sources\n(galley + lav sinks)"]
    PTRAP["P-Trap Assembly\n(odour seal + cleanout)"]
    LINES["Gravity Drain Lines\n(PTFE/PE, ≥1° slope)\nBilge route"]
    COLL["Drain Collector\n(bilge manifold TBD)"]
    MD["Mast Drain Nozzle\n(MD-1 ... MD-N)"]
    EMH["EMH Unit\n(resistance heater, ~20–50 W TBD)"]
    PWR["DC Power In\n(from ATA 24)"]
    MON["Continuity Monitor\n(current/resistance)"]
    CMC["CMC Alert\n('DRAIN HTR FAULT')"]
    OB["Overboard Discharge"]
    RTNK["Grey Water Retention\nTank (TBD — OI-038-004)"]

    SOURCES --> PTRAP --> LINES --> COLL
    COLL --> MD --> OB
    COLL -.-> RTNK
    PWR --> EMH --> MD
    MON --> EMH
    MON -->|"fault signal"| CMC
```

---

## §9 Lifecycle Traceability

```mermaid
flowchart LR
    REQ["Requirements\n(CS-25.1419 freeze,\nOI-038-004 grey water regs,\nCS-25.1301)"]
    SRD["System Requirements\nDocument"]
    SDD["SDD 038-040\nWaste Water Drainage"]
    ICD["ICDs\n(ATA 24 power,\nATA 25 sink fittings)"]
    COMP["Component Specs\n(mast drain, EMH,\nPTFE lines, p-traps)"]
    VTP["V&V Plan (§17)"]
    TEST["Test Reports\n(drain flow, EMH continuity,\nmast drain freeze test)"]
    CERT["EASA/FAA Certification"]
    EIS["Entry Into Service"]
    MAINT["AMM / S1000D DMs"]

    REQ --> SRD --> SDD --> ICD --> COMP
    SDD --> VTP --> TEST --> CERT --> EIS --> MAINT
```

---

## §10 Interfaces

| Interface | ATA Chapter | Direction | Signal/Medium | Notes |
|---|---|---|---|---|
| EMH electrical power | ATA 24 | In | Low-voltage DC TBD | EMH heater elements |
| Sink drain connections | ATA 25 | In | Grey water (fluid) | Galley and lavatory sink outlets |
| Galley condensate drain | ATA 25 | In | Condensate fluid (TBD) | Routing to grey drain TBD |
| Cabin condensate | ATA 21 | In | Condensate (TBD) | Potential routing to grey drain |
| EMH status to CMC | ATA 45 | Out | Digital/AFDX | Continuity/fault signal |
| Grey water retention (if OI-038-004) | ATA 38-070 | Out | Grey water | Retention tank service point TBD |

---

## §11 Operating Modes

| Mode | Drain Line State | EMH State | Notes |
|---|---|---|---|
| Normal Flight (all altitudes) | Gravity draining continuously | Active (icing conditions) | EMH on when temp sensor < threshold TBD |
| Ground — Hot day | Gravity draining | EMH off | No ice risk |
| Ground — Cold weather | Gravity draining | EMH may be active | Prevent nozzle freeze on ground |
| Icing conditions in flight | Gravity draining | EMH active | Critical — EMH prevents exit ice |
| Maintenance | Lines depressurised; accessible | Off | P-trap removal; line inspection |
| EMH Fault | Drain continues (gravity) | Off (fault) | "DRAIN HTR FAULT" caution; monitor for ice |

---

## §12 Monitoring and Diagnostics

| Parameter | Sensor | CMC Signal | Alert |
|---|---|---|---|
| EMH-1 continuity | Current/resistance monitor (CMH-1) | AFDX | "DRAIN HTR FAULT" (caution) |
| EMH-2 continuity | Current/resistance monitor (CMH-2) | AFDX | "DRAIN HTR FAULT" (caution) |
| EMH temperature (TBD) | NTC at nozzle (TBD) | AFDX | Advisory if below threshold |
| Grey water line blockage | None (gravity; no active sensor) | N/A | Detected by inspection only |

Note: Grey water drain lines do not carry active flow sensors. Blockage is detected by periodic maintenance inspection. EMH fault is the primary airworthiness-relevant alert for this subsystem.

---

## §13 Maintenance Concept

| Task | Access | Interval | Skill |
|---|---|---|---|
| P-trap inspection and clean | Galley/lav under-counter | A-check or per catering clean | Line |
| Grey drain line visual inspection | Bilge access panels | C-check TBD | Line/base |
| Mast drain nozzle inspection | Lower fuselage belly | C-check TBD | Base |
| Mast drain nozzle clean (scale/residue) | Mast drain access | C-check TBD | Base |
| EMH continuity test | Resistance measurement at access | A-check TBD | Line |
| EMH R&R | Mast drain removal access | On condition | Base |
| Drain line blockage clearance | Bilge access / p-trap | On condition | Line/base |
| Grey water retention tank drain (if fitted) | Service panel | Per turn / OI-038-004 | Line |

---

## §14 S1000D/CSDB Mapping

| Document | DMC Pattern | Info Code | Status |
|---|---|---|---|
| System description — grey water drainage | DMC-AMPEL360E-EWTW-038-04-00A-040A-A | 040 | <img src="https://img.shields.io/badge/DRAFT-yellow"> |
| Mast drain description | DMC-AMPEL360E-EWTW-038-04-10A-040A-A | 040 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Mast drain inspection | DMC-AMPEL360E-EWTW-038-04-10A-300A-A | 300 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| EMH removal | DMC-AMPEL360E-EWTW-038-04-20A-520A-A | 520 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| P-trap clean | DMC-AMPEL360E-EWTW-038-04-30A-810A-A | 810 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Fault isolation — grey water drain | DMC-AMPEL360E-EWTW-038-04-00A-400A-A | 400 | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §15 Footprints

| Parameter | Value |
|---|---|
| Mast drain count | <img src="https://img.shields.io/badge/TBD-red"> (~2–4, OI-038-008) |
| EMH power per unit | <img src="https://img.shields.io/badge/TBD-red"> (~20–50 W) |
| Total EMH power | <img src="https://img.shields.io/badge/TBD-red"> |
| Grey drain line length (total) | <img src="https://img.shields.io/badge/TBD-red"> m |
| Line diameter | <img src="https://img.shields.io/badge/TBD-red"> (typical ~25–38 mm) |
| Minimum slope | <img src="https://img.shields.io/badge/TBD-red"> (≥ 1°) |
| System mass (grey drain) | <img src="https://img.shields.io/badge/TBD-red"> kg |

---

## §16 Safety and Certification

| Requirement | Standard | Application |
|---|---|---|
| Freeze protection — mast drain | CS-25.1419 | EMH prevents ice blockage of overboard drain |
| Equipment installation | CS-25.1301 | Mast drain nozzle, EMH installation |
| System safety | CS-25.1309 | EMH failure mode; drain blockage consequence |
| Material flammability | CS-25.853 | Drain line material in cabin/bilge zones |
| Grey water disposal (regulatory) | OI-038-004 — regulatory review pending | Overboard drain vs. retention tank |
| Separation from potable water | NRV and physical separation | Grey circuit never contacts clean circuit |
| EMC | CS-25.1353 | EMH power connections |

---

## §17 Verification and Validation

| Test | Method | Acceptance Criterion | Status |
|---|---|---|---|
| EWP flow test | Bench/rig | ≥ TBD L/min | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Tank leak test | Hydrostatic 1.5× WP | No leakage TBD min | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| EWH thermal test | Bench thermostat | Outlet ≥ 60°C; TMV ≤ 43°C TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| UV steriliser output test | UV intensity + log-reduction | ≥ 4-log TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Mast heater continuity test | Resistance at installation | Within rated tolerance | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Flush cycle test | Functional rig | Waste ≤ 1.5 s TBD | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Fill-level sensor accuracy | Cal 0/50/100% | ± TBD % | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Overflow sensor function | Simulated overfill | Alert within TBD s | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Grey water drain flow test | Max simultaneous sink load | All drains clear within TBD s | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Potable water quality test | Sample analysis | Meets WHO/FAA standard | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |
| Freeze protection activation test | Cold chamber −40°C TBD | THC / EMH activate; no ice | <img src="https://img.shields.io/badge/To_Be_Completed-orange"> |

---

## §18 Glossary

| Term | Definition |
|---|---|
| PWS | Potable Water System |
| EWP | Electric Water Pump |
| EWH | Electric Water Heater |
| VWS | Vacuum Waste System |
| EFV | Electric Flush Valve |
| WIV | Waste Inlet Valve |
| Mast drain | Overboard grey water drain nozzle on lower fuselage |
| EMH | Electric Mast Heater — resistance heater on mast drain nozzle |
| UV sterilisation | UV-C inline potable water treatment |
| Activated carbon filter | Filter at potable water fill point |
| LLDPE | Linear Low-Density Polyethylene tubing |
| PEX | Cross-linked Polyethylene tubing |
| Capacitive level sensor | Non-contact level sensor |
| NRV | Non-Return Valve |
| TMV | Thermostatic Mixing Valve |
| Grey water | Sink drainage (not toilet waste) |
| Black water | Toilet waste |
| Waste tank | Toilet waste storage vessel |
| Freeze protection | Trace/mast heating system preventing ice |
| Trace heating | Resistance elements on water/drain lines |
| THC | Trace Heater Controller |
| CMC | Central Maintenance Computer |
| P-trap | Sink drain trap providing odour barrier; removable for cleaning |
| PTFE | Polytetrafluoroethylene — drain line liner material |

---

## §19 Citations

1. EASA CS-25.1419 — Ice protection.
2. EASA CS-25.1301 — Function and installation.
3. EASA CS-25.1309 — System safety.
4. EASA CS-25.853 — Material flammability.
5. OI-038-004 — Grey water retention regulatory review.
6. [038-000 General](./038-000-Water-and-Waste-General.md).
7. [038-050 Toilet and Vacuum Waste System](./038-050-Toilet-and-Vacuum-Waste-System.md) — black water system.
8. [038-060 Indication and Warning](./038-060-Water-and-Waste-Indication-and-Warning.md).
9. [038-070 Servicing and Ground Interfaces](./038-070-Water-and-Waste-Servicing-and-Ground-Interfaces.md).

---

## §20 References

| Ref | Document | Notes |
|---|---|---|
| [R1] | CS-25.1419 | Freeze protection (EMH) |
| [R2] | CS-25.1301 | Installation |
| [R3] | CS-25.1309 | System safety |
| [R4] | CS-25.853 | Flammability |
| [R5] | OI-038-004 | Grey water retention review |
| [R6] | [038-000](./038-000-Water-and-Waste-General.md) | ATA 38 General |
| [R7] | [038-050](./038-050-Toilet-and-Vacuum-Waste-System.md) | Black water system |
| [R8] | [038-060](./038-060-Water-and-Waste-Indication-and-Warning.md) | Indication |
| [R9] | [038-070](./038-070-Water-and-Waste-Servicing-and-Ground-Interfaces.md) | Ground servicing |

---

## §21 Open Issues

| ID | Description | Owner | Status |
|---|---|---|---|
| OI-038-001 | Tank capacity and material | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-002 | Tank pressurisation method | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-003 | EWH count, placement, power budget | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-004 | Grey water retention regulatory review (overboard drain vs. retention tank) | Q-AIR / ORB-LEG | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-005 | Waste tank count and capacity | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-006 | Freeze protection strategy (trace heat vs. routing) | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-007 | UV sterilisation certification and interval | Q-AIR / ORB-LEG | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-008 | Mast drain count and location | Q-AIR / Q-MECHANICS | <img src="https://img.shields.io/badge/TBD-red"> |
| OI-038-009 | Single-point servicing panel location | Q-AIR / Q-GROUND | <img src="https://img.shields.io/badge/TBD-red"> |

---

## §22 Change Log

| Revision | Date | Author | Description |
|---|---|---|---|
| 0.1.0 | 2026-05-10 | Q+ATLANTIDE ATLAS Working Group | Initial full-template draft; all 23 sections; grey water drain, mast drain, EMH |
| 0.0.0 | 2026-05-10 | Q+ATLANTIDE ATLAS Working Group | Scaffold stub created |
