---
document_id: DMC-AMPEL360E-EWTW-070-000-04A-README
title: "Hybrid Propulsion Control and Mode Management — S1000D Info Code Structure"
dmc_base: "DMC-AMPEL360E-EWTW-070-000-04A"
programme: "AMPEL360e-Wide-Tube-and-Wing-Family"
chapter: "ATLAS 070 — Hybrid-Electric Propulsion Architecture"
topic: "Hybrid Propulsion Control and Mode Management"
disassembly_code_variant: "04A"
status: "draft / scaffold"
standard: "S1000D Issue 4.2"
owner: "Amedeo Pelliccia / Q+"
primary_language: "en"
created: 2026-05-14
updated: 2026-05-15
no_aaa_rule: true
---

# Hybrid Propulsion Control and Mode Management — S1000D Info Code Structure

## Data Module Base

`DMC-AMPEL360E-EWTW-070-000-04A`

## Info Code Breakdown

| Folder | Info Codes | Description |
| ------ | ---------- | ----------- |
| `040_descriptive/` | 040–049 | System Description through Traceability and CSDB Mapping Description |
| `100_operation/` | 100–109 | Operation through Operational Limitations and Precautions |
| `300_examinations-tests-and-checks/` | 300–307, 310–317, 320–325, 330–331 | Inspection / Operational Check / Functional Test / Performance Check |
| `400_fault-reports-and-isolation-procedures/` | 400–408, 410–415, 420–424 | Fault Symptoms / Assessment / Isolation |
| `C00_computer-systems-software-and-data/` | C00, C10, C20 | Computer System Description / Software Configuration / Diagnostic Data |

## Summary of Data Modules

| Info Code | Variant | Title |
| --------- | ------- | ----- |
| 040 | A | System Description |
| 041 | A | Hybrid Propulsion Control Description |
| 042 | A | Mode Management Architecture Description |
| 043 | A | Control Law and Authority Boundary Description |
| 044 | A | Energy Command and Power Demand Description |
| 045 | A | Propulsive Channel Control Interface Description |
| 046 | A | Mode Transition and Arbitration Logic Description |
| 047 | A | Fault Tolerant Control and Degraded Mode Description |
| 048 | A | Safety Human Oversight and Certification Constraint Description |
| 049 | A | Traceability and CSDB Mapping Description |
| 100 | A | Operation |
| 101 | A | Hybrid Propulsion Control Normal Operation |
| 102 | A | Mode Management Operation |
| 103 | A | Control Law and Authority Boundary Operation |
| 104 | A | Energy Command and Power Demand Operation |
| 105 | A | Propulsive Channel Control Operation |
| 106 | A | Mode Transition and Arbitration Operation |
| 107 | A | Fault Tolerant Control Operation |
| 108 | A | Degraded Mode Control Operation |
| 109 | A | Operational Limitations and Precautions |
| 300 | A | General Inspection |
| 301 | A | Visual Inspection |
| 302 | A | Configuration Inspection |
| 303 | A | Control Interface Inspection |
| 304 | A | Mode Management Interface Inspection |
| 305 | A | Authority Boundary and Control Law Inspection |
| 306 | A | Energy Command and Power Demand Inspection |
| 307 | A | Fault Tolerant Control Path Inspection |
| 310 | A | Operational Check |
| 311 | A | Hybrid Propulsion Control Operational Check |
| 312 | A | Mode Management Operational Check |
| 313 | A | Control Law Authority Boundary Operational Check |
| 314 | A | Energy Command and Power Demand Operational Check |
| 315 | A | Mode Transition Operational Check |
| 316 | A | Fault Tolerant Control Operational Check |
| 317 | A | Degraded Mode Control Operational Check |
| 320 | A | Functional Test |
| 321 | A | Hybrid Propulsion Control Functional Test |
| 322 | A | Mode Management Functional Test |
| 323 | A | Control Law Authority Boundary Functional Test |
| 324 | A | Energy Command Functional Test |
| 325 | A | Mode Transition Functional Test |
| 330 | A | System Performance Check |
| 331 | A | Control and Mode Management Performance Check |
| 400 | A | Fault Reporting |
| 401 | A | Fault Code Classification |
| 402 | A | Hybrid Propulsion Control Fault Symptoms |
| 403 | A | Mode Management Fault Symptoms |
| 404 | A | Control Law Authority Boundary Fault Symptoms |
| 405 | A | Energy Command and Power Demand Fault Symptoms |
| 406 | A | Mode Transition Fault Symptoms |
| 407 | A | Fault Tolerant Control Fault Symptoms |
| 408 | A | Degraded Mode Control Fault Symptoms |
| 410 | A | Preliminary Fault Assessment |
| 411 | A | Hybrid Propulsion Control Fault Assessment |
| 412 | A | Mode Management Fault Assessment |
| 413 | A | Control Law Authority Boundary Fault Assessment |
| 414 | A | Mode Transition Fault Assessment |
| 415 | A | Degraded Mode Control Fault Assessment |
| 420 | A | Fault Isolation Procedure |
| 421 | A | Hybrid Propulsion Control Fault Isolation |
| 422 | A | Mode Management Fault Isolation |
| 423 | A | Control Law Authority Boundary Fault Isolation |
| 424 | A | Mode Transition and Degraded Mode Fault Isolation |
| C00 | A | Computer System Description |
| C10 | A | Software Configuration |
| C20 | A | Diagnostic Data |

## Status

```yaml
status:
  maturity: "draft / scaffold"
  content_ready: false
  next_steps:
    - "author XML content per S1000D Issue 4.2"
    - "validate against BREX-EWTW-070-v1"
    - "link ICN and illustrations"
    - "add to DMRL"
```
