---
document_id: "QATL-ATLAS-1000-ATLAS-070-079-070-050-PROPULSION-ENERGY-FLOW-ARCHITECTURE"
register: ATLAS-1000
title: "Propulsion Energy Flow Architecture"
ata: "ATA 70"
sns: "070-050-00"
subsection: "070"
subsubject_code: "050"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HPC, Q-MECHANICS, Q-AIR, Q-INDUSTRY]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-11"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
parent_subsubject_doc: "./README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0070-050"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-070-079-070-050-PROPULSION-ENERGY-FLOW-ARCHITECTURE
     ATA 70 · Propulsion Energy Flow Architecture
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Propulsion Energy Flow Architecture

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATA 70](https://img.shields.io/badge/ATA-70-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-GREENTECH](https://img.shields.io/badge/Q--Division-Q--GREENTECH-brightgreen)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden. Every linked document must exist in the Q+ATLANTIDE repository
> before the link is activated. Broken links are treated as open issues and must be resolved
> before the document is promoted from `DRAFT` to `APPROVED`.

---

## §1 Purpose

This document defines the energy flow paths across all propulsion-related components of the AMPEL360E eWTW — from fuel combustion through shaft power to electrical generation, HVDC distribution, battery storage, and electric propulsor drive — and quantifies the power and energy budgets for each path.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA reference | ATA 70-050 — Propulsion Energy Flow Architecture |
| Certification basis | EASA CS-25 Amdt 27 + SC-Hybrid-Electric |
| S1000D SNS | 070-050-00 |

---

## §3 Functional Description ![DRAFT]

**Primary Energy Flow — Combustion to Shaft Thrust**
Jet-A1/SAF fuel combustion in the turbofan core produces hot-gas energy. Approximately 36 % converts to useful shaft power (LP + HP turbines); the remainder is expelled as exhaust thrust and heat. LP shaft power drives the fan (primary thrust ~88 %) and through the reduction gearbox the PMSG (electrical energy ~12 %). Net turbofan cycle efficiency at cruise: ~38–40 %.

**Secondary Energy Flow — PMSG to EP Shaft**
PMSG converts LP shaft mechanical power to HVDC 540 V DC at ~96 % efficiency. HVDC bus carries the power through wing D-box cable trunking to the PDCU and onwards to each MDU. Each MDU (SiC inverter) converts HVDC DC to three-phase variable-frequency AC for the PMSM motor at ~98 % efficiency. PMSM motor converts electrical to mechanical shaft power at ~97 % efficiency. Combined PMSG→MDU→PMSM chain efficiency: ~91 %. Overall fuel→EP shaft efficiency: ~35 % (includes turbofan core losses).

**BESS Energy Flow — Storage to EP Shaft**
BESS DC stored energy → HV contactor → HVDC 540 V bus → MDU → PMSM. BESS discharge efficiency (contactor + bus losses): ~99 %. BESS charge efficiency (regen via MDU): ~98 %. Round-trip efficiency (BESS discharge + charge cycle): ~92 %.

**Regenerative Flow — EP Fan to BESS**
During RGD descent: EP fan windmills → mechanical torque → PMSM (acting as generator) → MDU (regenerative mode) → HVDC bus → BESS charging. Regen conversion efficiency (PMSM gen → BESS): ~95 %. Recoverable energy per descent: 30–50 kWh.

---

## §4 Functional Breakdown

| ID | Name | Description | Lead Division |
|---|---|---|---|
| F-001 | Combustion energy chain | Fuel → LP shaft → fan thrust + PMSG | Q-GREENTECH |
| F-002 | PMSG generation chain | LP shaft → PMSG → HVDC 540 V | Q-MECHANICS |
| F-003 | BESS discharge chain | BESS stored energy → HVDC bus → EP drive | Q-GREENTECH |
| F-004 | EP drive chain | HVDC bus → MDU → PMSM → fan thrust | Q-GREENTECH |
| F-005 | Regenerative capture chain | EP fan windmill → PMSM gen → MDU regen → BESS | Q-GREENTECH |

---

## §5 System Context — Mermaid Diagram

```mermaid
flowchart LR
    FUEL[Fuel Tank\nJet-A1 / SAF] --> TF_CORE[Turbofan Core\n38-40% cycle eff.]
    TF_CORE --> FAN[Fan Net Thrust\n~88% LP shaft]
    TF_CORE --> LP[LP Shaft ~12% to PMSG]
    LP --> PMSG[PMSG\n96% eff.]
    PMSG --> HVDC[HVDC 540 V Bus\nPDCU]
    BESS[BESS 800 kWh\nLi-S] --> HVDC
    HVDC --> MDU_P[MDU-PORT\n98% eff.]
    HVDC --> MDU_S[MDU-STBD\n98% eff.]
    MDU_P --> PMSM_P[PMSM-PORT\n97% eff.]
    MDU_S --> PMSM_S[PMSM-STBD\n97% eff.]
    PMSM_P --> EP_THRUST_P[EP-PORT Fan Thrust]
    PMSM_S --> EP_THRUST_S[EP-STBD Fan Thrust]
    EP_THRUST_P -.->|RGD regen| MDU_P
    MDU_P -.->|regen current| HVDC
    HVDC -.->|charge| BESS
```

---

## §6 Internal Architecture — Mermaid Diagram

```mermaid
flowchart TB
    subgraph THERMAL["Thermal Chain"]
        FUEL2[Fuel kJ/kg LHV] --> COMBUST[Combustion\n36% shaft eff.]
        COMBUST --> LP2[LP Shaft kW]
        LP2 -->|88%| FAN2[Fan Thrust kN]
        LP2 -->|12%| GBX2[Gearbox → PMSG\n96% eff.]
    end
    subgraph HVDC_BUS["HVDC 540 V Backbone"]
        GBX2 --> BUS[HVDC 540 V Bus]
        BESS2[BESS 800 kWh] -->|discharge 99%| BUS
    end
    subgraph EP_CHAIN["EP Drive Chain"]
        BUS -->|MDU 98%| PMSM2[PMSM Motor 97%]
        PMSM2 --> EP_SHAFT[EP Fan Shaft kW]
        EP_SHAFT -.->|regen 95%| BUS
    end
    EFFICIENCY["Overall fuel → EP shaft: ~35%\nBESS → EP shaft: ~94%\nRegen round-trip: ~92%"]
```

---

## §7 Components and LRUs

| Component | Part Number | Qty | Location | Maintenance Interval | Notes |
|---|---|---|---|---|---|
| PMSG (port/stbd) | PMSG-PN-TBD | 2 | Nacelle aft — LP shaft | On condition | 2.5 MW; 96 % efficiency |
| PDCU (Power Distribution & Control Unit) | PDCU-PN-TBD | 1 | EE bay / belly fairing | Functional test C-check | HVDC bus management |
| MDU (Motor Drive Unit, port/stbd) | MDU-PN-TBD | 2 | EP nacelle wingtip | Functional test C-check | SiC; 1.5 MW; 98 % efficiency |
| BESS Pack (A/B) | BESS-PN-TBD | 2 | Aft belly bays F-25/F-27 | Cap check 2 000 FH | 400 kWh each; 92 % round-trip |
| HVDC Cable Bundle (wing) | HVDC-CABLE-PN-TBD | 4 runs | Wing D-box conduit | Visual inspection A-check | 540 V; shielded; fire-rated |

---

## §8 Interfaces

| Interface Type | Connected System | Protocol / Medium | Data / Function |
|---|---|---|---|
| ATA 24 Electrical Power | HVDC bus, LVDC converters | HVDC cable | Energy flow backbone; non-propulsion loads shed in EE mode |
| ATA 28 Fuel System | Fuel tank quantity and feed | Discrete / AFDX | Fuel flow rate to TF → PMSG power calculation |
| ATA 79 EMS | Energy management targets | AFDX | EMS provides energy budget; energy flow monitored |
| ATA 45 CMS | Energy flow health monitoring | AFDX | PDCU and PMSG power anomalies logged |
| ATA 31 ECAM | Power flow synoptic | AFDX | HVDC bus voltage, PMSG output, BESS SoC, EP power |

---

## §9 Operating Modes

| Mode | Primary Energy Path | Secondary Path | Direction |
|---|---|---|---|
| AET | BESS → HVDC → MDU → EP | — | Discharge |
| BTO | PMSG → HVDC → MDU → EP + BESS → HVDC → MDU → EP | — | Discharge |
| Cruise | PMSG → HVDC → MDU → EP | — | Balanced / slight discharge |
| RGD | EP fan → PMSM gen → MDU regen → HVDC → BESS | — | Charge |
| EE | BESS → HVDC → MDU → EP | — | Full discharge |
| TF-Only | Fuel → TF → fan thrust | No electric EP | No HVDC propulsion flow |

---

## §10 Performance and Budgets ![DRAFT]

| Parameter | Requirement | Target / Design Value | Status |
|---|---|---|---|
| PMSG efficiency | ≥ 95 % | 96 % | ![TBD] |
| MDU (SiC inverter) efficiency | ≥ 97 % | 98 % | ![TBD] |
| PMSM motor efficiency | ≥ 96 % | 97 % | ![TBD] |
| PMSG→EP shaft chain efficiency | ≥ 88 % | 91 % | ![TBD] |
| BESS round-trip efficiency | ≥ 90 % | 92 % | ![TBD] |
| BESS→EP shaft efficiency | ≥ 92 % | 94 % | ![TBD] |
| Regen capture efficiency (EP→BESS) | ≥ 90 % | 95 % | ![TBD] |

---

## §11 Safety, Redundancy and Fault Tolerance

- HVDC bus over-voltage protection in PDCU: trips bus within 5 ms if > 600 V (HVDC rated limit 560 V).
- PMSG over-speed (LP shaft runaway) protection: PMSG disconnected via contactor within 50 ms of over-speed signal.
- BESS thermal runaway: energy flow path isolated by BMS contactors within 100 ms; HVDC rerouted to remaining pack.
- Regenerative over-charge: MDU regen mode limited by BMS maximum charge current; MDU inhibits regen if BESS at 90 % SoC.
- Fuel flow anomaly: FADEC handles independently; PMSG output drops are absorbed by BESS with PDCU prioritisation.

---

## §12 Maintenance and Diagnostics

| Task | Interval | Access | Special Tools |
|---|---|---|---|
| HVDC cable insulation resistance test (wing D-box) | C-check | Wing access panels | HVDC IR tester (1 kV) |
| PMSG power output calibration (kW vs N1 curve) | C-check | Nacelle; PMSG GSE | PMSG GSE terminal |
| MDU efficiency measurement (kW in vs kW out) | C-check | EP nacelle | MDU GSE terminal + power analyser |
| BESS round-trip efficiency test | 2 000 FH | Belly fairing | BMS GSE terminal |

---

## §13 Footprint — Physical, Electrical, Maintenance, Data ![TBD]

| Footprint Type | Parameter | Value | Notes |
|---|---|---|---|
| Electrical | Peak HVDC bus current (BTO) | ~5 600 A (3 MW / 540 V) | Both EPs + PMSG + BESS parallel |
| Electrical | HVDC cable cross-section | ![TBD] | Per current density and voltage drop spec |
| Data | PDCU power monitoring rate | 100 Hz | HVDC voltage / current telemetry |
| Physical | Wing D-box cable conduit length | ~22 m each side | PMSG nacelle to PDCU |

---

## §14 Safety and Certification References ![DRAFT]

| Standard / Document | Title | Issuing Body | Applicability |
|---|---|---|---|
| SAE AS6019 | HVDC Arc-Fault Detection | SAE | HVDC bus arc protection |
| SAE AS5780 | HV Interconnect for Hybrid-Electric | SAE | HVDC cable sizing and routing |
| RTCA DO-311A | MOPS — Rechargeable Lithium Battery | RTCA | BESS energy flow safety |
| EASA AMC 25.1353 | Electrical Equipment and Installations | EASA | HVDC bus protection requirements |

---

## §15 V&V Approach ![TBD]

| Phase | Method | Acceptance Criterion | Status |
|---|---|---|---|
| Design | Power flow simulation (Modelica / MATLAB) | All efficiency targets met; HVDC voltage within ±5 % at bus | ![TBD] |
| Integration | Ground power-on test (PMSG → HVDC → MDU → EP) | Energy flow correct; no bus voltage exceedances | ![TBD] |
| Qualification | DO-160G EMI test on HVDC cable runs | No interference with avionics | ![TBD] |
| Certification | Flight test power flow measurement | PMSG output, BESS SoC, EP input within spec | ![TBD] |

---

## §16 Glossary

| Term | Definition |
|---|---|
| **Energy flow** | The path and conversion chain of energy from fuel to final propulsive thrust. |
| **HVDC PDU** | HVDC Power Distribution Unit — manages bus sources, loads, and protection. |
| **Bus bar** | Conductor connecting multiple sources and loads at a common voltage point. |
| **Round-trip efficiency** | Ratio of energy recovered from BESS (discharge) to energy stored (charge), typically 90–95 %. |
| **Thermal efficiency** | Ratio of shaft power output to fuel chemical energy input; 36–40 % for turbofan at cruise. |
| **Regen mode** | MDU operation as a generator-rectifier, converting EP fan windmill energy to HVDC DC. |
| **SiC inverter** | Silicon Carbide power electronic device enabling high-frequency, high-efficiency DC/AC conversion. |

---

## §17 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-070-050-001 | Finalise HVDC cable cross-section sizing (peak 5 600 A at BTO vs weight budget) | Q-MECHANICS | 2026-Q4 |
| OI-070-050-002 | Validate PMSG→EP chain efficiency 91 % with component-level test data from OEMs | Q-GREENTECH | 2027-Q1 |

---

## §18 Status Legend

| Badge | Meaning |
|---|---|
| `![DRAFT]` | Section is drafted but not yet reviewed |
| `![TBD]` | Content not yet started — to be defined |
| `![To Be Completed]` | Partially complete — needs additional content |
| `![APPROVED]` | Reviewed and formally approved |

---

## §19 Related Documents (Siblings in this Subsection)

- [070-000](./070-000-Hybrid-Electric-Architecture-Overview-General.md)
- [070-010](./070-010-Propulsion-System-Topology.md)
- [070-020](./070-020-Electric-and-Thermal-Propulsion-Allocation.md)
- [070-030](./070-030-Hybrid-Electric-Operating-Modes.md)
- [070-040](./070-040-Propulsion-Redundancy-and-Degraded-Modes.md)
- [070-060](./070-060-Propulsion-Safety-and-Isolation-Zones.md)
- [070-070](./070-070-Propulsion-Integration-and-Airframe-Interfaces.md)
- [070-080](./070-080-Hybrid-Electric-Monitoring-Diagnostics-and-Control-Interfaces.md)
- [070-090](./070-090-S1000D-CSDB-Mapping-and-Traceability.md)

---

## §20 Change Log

| Rev | Date | Author | Description |
|---|---|---|---|
| 0.1 | 2026-05-11 | @copilot | Initial DRAFT — contextualized content per AMPEL360E eWTW architecture |
