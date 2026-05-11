---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-000-STRUCTURAL-MONITORING-DIAGNOSTICS-AND-EVIDENCE-GENERAL"
title: "ATLAS 050-059 · 05.050.000 — Structural Monitoring, Diagnostics and Evidence General"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../../README.md
parent_section_doc: ../../README.md
parent_subsection_doc: ../README.md
parent_subsubject_doc: ./README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "050-059"
section: "05"
section_title: "Estructuras"
subsection: "050"
subsection_title: "General"
subsubject: "000"
subsubject_title: "Structural Monitoring Diagnostics and Evidence General"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.050.000 — Structural Monitoring, Diagnostics and Evidence General

## 1. Purpose

Defines the **Structural Health Monitoring (SHM) architecture** for the AMPEL360 eWTW: sensor types, data acquisition, on-board processing, ground-station synchronisation, PHM credit, and regulatory evidence pathway under CS-25 AMC 20-29A.

## 2. Scope

### 2.1 SHM Sensor Architecture

| Sensor type | Acronym | Application | Quantity (est.) |
|---|---|---|---|
| Fibre Bragg Grating | FBG | Strain, temperature — fuselage + wing skin | ~2,400 nodes |
| Piezoelectric wafer active sensor | PWAS | Lamb-wave damage detection — PSE zones | ~800 nodes |
| Acoustic emission sensor | AE | Crack initiation monitoring — WFIJ/pylon | ~120 nodes |
| Eddy-current film sensor | ECFS | Corrosion monitoring — lap-joint zones | ~400 nodes |

### 2.2 Data Acquisition and Processing

```mermaid
graph LR
    S1[FBG Array] --> DAU[Structural Data Acquisition Unit SDAU]
    S2[PWAS Array] --> DAU
    S3[AE Sensors] --> DAU
    S4[ECFS] --> DAU
    DAU --> SCU[SHM Central Unit SCU - AFDX connected]
    SCU --> PHM[PHM / RUL Engine]
    SCU --> DST[Digital Structural Twin DST]
    DST --> GND[Ground Station / MCC]
```

### 2.3 PHM Credit Pathway

SHM data may be used to extend inspection intervals subject to regulatory credit per CS-25 AMC 20-29A (onboard maintenance systems). The credit pathway requires:

1. **Sensor qualification** — DO-160G environmental; DO-254 hardware; sensor accuracy characterisation.
2. **Algorithm qualification** — DO-178C DAL C for damage-state classifier; uncertainty quantification report.
3. **Regulatory submission** — Special Condition or AMC letter to EASA SA/FAA ACO covering SHM credit.
4. **Fleet demonstration** — minimum 500 aircraft-flights with validated sensor performance prior to interval extension.

### 2.4 Evidence and Traceability

All SHM findings are recorded in the S1000D CSDB as:
- **Event DMs** (info-code 012) — sensor alert events.
- **Inspection DMs** (info-code 300) — correlated visual/NDT findings.
- **Maintenance DMs** (info-code 200) — follow-on maintenance actions.

Digital twin correlation results are stored in the **Fleet Health Management System (FHMS)** and linked to individual aircraft serial numbers.

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-000-STRUCTURAL-MONITORING-DIAGNOSTICS-AND-EVIDENCE-GENERAL` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| CS-25 AMC 20-29A | Onboard maintenance systems |
| DO-160G | Environmental conditions and test procedures |
| DO-178C | Software considerations in airborne systems |
| DO-254 | Design assurance guidance for airborne electronic hardware |
| [`./README.md`](./README.md) | Subsubject index |
