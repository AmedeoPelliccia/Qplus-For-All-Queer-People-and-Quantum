---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-083-040-POWER-CONDITIONING-AND-DISTRIBUTION-INTERFACES"
register: ATLAS-1000
title: "Power Conditioning and Distribution Interfaces"
ata: "ATLAS-083 (Solar-Electric Auxiliary)"
sns: "083-040-00"
subsection: "083"
subsubject_code: "040"
primary_q_division: Q-INDUSTRY
support_q_divisions: [Q-GREENTECH, Q-HPC, Q-STRUCTURES]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0083-040"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-083-040-POWER-CONDITIONING-AND-DISTRIBUTION-INTERFACES
     ATLAS-083 (Solar-Electric Auxiliary) · Power Conditioning and Distribution
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# Power Conditioning and Distribution Interfaces

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-083 Solar-Electric](https://img.shields.io/badge/ATLAS--083-Solar--Electric%20Auxiliary-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-INDUSTRY](https://img.shields.io/badge/Q--Division-Q--INDUSTRY-purple)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `Power Conditioning and Distribution Interfaces`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.
## §2 Applicability

| Applicability Level | Rule |
|---|---|
| Standard taxonomy | Applies to the ATLAS node `083` |
| Programme implementation | Conditional; determined by programme architecture, trade studies, certification basis, and applicability model |
| Product configuration | Defined in the programme-specific configuration baseline |
| Effectivity | Defined in the programme CSDB / applicability layer |
| Non-applicability | Must be explicitly stated in the programme impact-study branch when excluded |
## §3 SEACU Internal Power Architecture

```
PV Arrays (6 zones) ──→ 6× MPPT Boost Converters ──→ 700 V DC Link
SCAP Bank ─────────── ↕ Bidirectional DC/DC (200 kW peak) ──→ 700 V DC Link
Li-Ion Battery ─────── ↕ Bidirectional DC/DC (80 kW) ──→ HVDC 270 V Bus Tie
HVDC 270 V Bus ─────── ↕ Bidirectional Bus Tie Converter ──→ 700 V DC Link (via boost)
700 V DC Link ─────────→ 4× SiC Propulsor Inverters ──→ 3-phase AC (Propulsor Motors)
```

---

## §4 MPPT Boost Converter Stages (6×)

| Parameter | Value |
|---|---|
| Topology | Interleaved synchronous boost (4-phase interleaved) |
| Input voltage range | 40–120 V DC (PV string Vmpp range) |
| Output voltage | 700 V DC regulated |
| Rated power | 20 kW per converter (10 kW for CH-6 winglet) |
| Switching frequency | 100 kHz |
| Semiconductor | SiC MOSFET (Wolfspeed C3M or equivalent), 1 200 V, 40 A |
| Efficiency | ≥ 98 % at full load |
| Input filter | Pi-filter; CM choke 2.2 mH; DM capacitor 100 µF; limits conducted EMI to DO-160G Cat B |
| Overcurrent protection | Cycle-by-cycle current limit; 150 % rated → converter fault and latch-off within 100 µs |
| Input isolation | No galvanic isolation (MPPT boost); galvanic isolation provided at SEACU input (Y-capacitor bonding to airframe) |
| Cooling | Aluminium cold plate; forced air 40 CFM per converter; SEACU bay temperature monitored |

---

## §5 SCAP Bidirectional DC/DC Converter

| Parameter | Value |
|---|---|
| Topology | Half-bridge bidirectional DC/DC (non-isolated) |
| SCAP port voltage | 350–700 V DC (SCAP SoE 25–100 %) |
| DC link port voltage | 700 V DC |
| Peak power (charge / discharge) | 200 kW for ≤ 0.5 s |
| Continuous power | 50 kW |
| Switching frequency | 50 kHz |
| Semiconductor | SiC MOSFET 1 200 V, 100 A (paralleled pairs) |
| Efficiency | ≥ 97 % at 50 kW continuous |
| Control mode | Current-controlled; SEACU arbitrator commands current setpoint (A) to SCAP converter |
| Protection | Over-voltage (730 V); under-voltage (330 V); over-current (220 kW); shoot-through interlocked |

---

## §6 Battery Bidirectional DC/DC Converter

| Parameter | Value |
|---|---|
| Topology | Isolated bidirectional LLC resonant converter |
| Battery port | 520–740 V DC (<BATTERY-CHEMISTRY> SoC 20–90 %) |
| DC link / HVDC 270 V bus port | 270 V DC (isolated; ratio 2.7:1) |
| Rated continuous power | 40 kW (charge and discharge) |
| Peak power | 80 kW for ≤ 10 s |
| Galvanic isolation | 4 kV (battery side to HVDC 270 V bus); required for HVDC bus safety |
| Switching frequency | 200 kHz (resonant LLC) |
| Efficiency | ≥ 96 % at full load |
| Control | Dual-active bridge (DAB) control; SEACU BMS SoC feedback |

---

## §7 SiC Propulsor Inverters (4×)

| Parameter | Value |
|---|---|
| Topology | 3-phase 2-level voltage source inverter (VSI) |
| DC link input | 700 V DC |
| AC output | 0–500 V line-to-line RMS; 0–800 Hz (PMSM drive) |
| Rated power | 50 kW per inverter |
| Semiconductor | SiC MOSFET 1 200 V, 80 A; 6-switch bridge |
| Switching frequency | 20 kHz (audible noise out of range; efficient for PMSM) |
| Motor control algorithm | Field-Oriented Control (FOC); MTPA (Maximum Torque Per Ampere) for PMSM |
| Torque ripple | < 2 % at rated speed (FOC with harmonic injection) |
| DC link capacitor | 5 mF film capacitor per inverter (shared DC link capacitor bank) |
| Protection | Overcurrent (hardware latch, < 2 µs); desaturation detection; ground fault |
| Cooling | SiC module baseplate → copper cold plate → EGW coolant (ATLAS 074) |
| Gate drive | 2-level gate drive; +15 V / −4 V; dV/dt controlled 10 V/ns to limit CMV |

---

## §8 HVDC 270 V Bus Tie

| Parameter | Value |
|---|---|
| Topology | Bidirectional non-isolated boost/buck converter |
| DC link port | 700 V DC |
| HVDC 270 V bus port | 270 V DC |
| Rated power | ±80 kW (positive = export from SEA to bus; negative = import from bus to SEA) |
| IRM protection | IRM (Inrush Resistance Module) on HVDC 270 V port; 50 ms precharge before contactor close |
| SSPC on bus tie | 100 A SSPC (Q-INDUSTRY standard; trip time < 1 ms at 200 % overload) |
| Fault isolation | SEACU fault → bus tie SSPC opens within 5 ms; HVDC 270 V bus unaffected |
| EMC filter | Common-mode choke + X/Y capacitors; DO-160G Cat B |

---

## §9 SSPCs and Protection Architecture

| SSPC | Rating | Protected Circuit | Trip Time (Overload) | Trip Time (Short) |
|---|---|---|---|---|
| SSPC-083-01 | 100 A / 700 V | DC link to propulsor inverter A (CH-1) | 100 ms at 120 % | < 1 ms at 500 % |
| SSPC-083-02 | 100 A / 700 V | DC link to propulsor inverter B (CH-2) | 100 ms at 120 % | < 1 ms at 500 % |
| SSPC-083-03 | 100 A / 700 V | DC link to propulsor inverter C (CH-3) | 100 ms at 120 % | < 1 ms at 500 % |
| SSPC-083-04 | 100 A / 700 V | DC link to propulsor inverter D (CH-4) | 100 ms at 120 % | < 1 ms at 500 % |
| SSPC-083-05 | 200 A / 700 V | SCAP DC/DC to DC link | 50 ms at 130 % | < 500 µs at 500 % |
| SSPC-083-06 | 100 A / 270 V | HVDC 270 V bus tie | 100 ms at 120 % | < 1 ms at 500 % |
| SSPC-083-07 | 50 A / 700 V | DC link to SEACU control electronics | 200 ms at 110 % | < 2 ms at 500 % |

**Insulation Monitoring Device (IMD):** Bender ISOMETER IR155 or equivalent; monitors isolation resistance between DC link (700 V) and airframe ground continuously; alarm at < 100 kΩ·kW (per IEC 61557-8 / DO-160G).

---

## §10 Cable Sizing

| Cable | Route | AWG | Current (A) | Voltage (V) | Insulation |
|---|---|---|---|---|---|
| PV string to MPPT input | Panel to junction box | 14 AWG | 5 A max per string | 600 V | Silicone, 125 °C |
| MPPT input trunk to SEACU | Junction box to SEACU bay | 10 AWG | 15 A per channel | 600 V | PTFE, 200 °C |
| MPPT output / DC link | Internal SEACU bus bar | 4 AWG Cu bar | 200 A | 700 V | Bus bar insulation, 125 °C |
| SCAP to DC/DC | SCAP bay to SEACU | 4/0 AWG | 300 A peak | 700 V | XLPE, 125 °C |
| Propulsor inverter to motor | SEACU bay to aft BLI duct | 2/0 AWG | 80 A per phase | 500 V AC | XLPE, 150 °C |
| HVDC 270 V bus tie | SEACU to HVDC 270 V bus bar | 2/0 AWG | 200 A | 270 V | XLPE, 125 °C |

---

## §11 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-083-040-001 | EMC conducted emission test (DO-160G Section 21) for SEACU MPPT switching at 100 kHz — filter design validation | Q-INDUSTRY | CDR |
| OI-083-040-002 | Ground fault detection sensitivity for 700 V DC link — IMD threshold vs. Y-capacitor leakage budget | Q-INDUSTRY | PDR |
| OI-083-040-003 | SiC gate drive dV/dt limit impact on common-mode voltage at propulsor motor bearings — bearing current analysis | Q-HPC | CDR |
| OI-083-040-004 | Cable derating for XLPE in SEACU bay at elevated ambient (55 °C) — thermal analysis | Q-STRUCTURES | PDR |
