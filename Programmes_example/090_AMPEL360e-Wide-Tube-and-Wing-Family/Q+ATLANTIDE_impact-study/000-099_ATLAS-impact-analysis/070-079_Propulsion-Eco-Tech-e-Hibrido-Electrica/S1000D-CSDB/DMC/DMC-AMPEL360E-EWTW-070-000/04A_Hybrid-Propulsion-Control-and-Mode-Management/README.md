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
| `500_disconnect-remove-and-disassembly-procedures/` | 500–509, 510–513, 520–526, 530–534, 540–541, 590 | Disconnect / Access / Remove / Disassembly / Post-Removal / Records |
| `700_assemble-install-and-connect-procedures/` | 700–708, 710–713, 720–726, 730–737, 740–746, 750–752, 790 | Assemble / Access / Install / Connect / Verify / Restore / Records |
| `941_illustrated-parts-data/` | 941A–941Z | Illustrated Parts Data (all modules and hardware) |
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
| 500 | A | Disconnect |
| 501 | A | Pre-Removal Safety Preparation |
| 502 | A | Electrical Isolation and Lockout |
| 503 | A | Control System Isolation |
| 504 | A | Mode Management Isolation |
| 505 | A | Energy Command and Power Demand Interface Safing |
| 506 | A | Propulsive Channel Control Interface Safing |
| 507 | A | Data Control and Signal Interface Disconnect |
| 508 | A | High Voltage and Low Voltage Control Power Disconnect |
| 509 | A | Fault Tolerant Control Path Safing |
| 510 | A | Access and Preparation for Removal |
| 511 | A | Remove Access Panels and Protective Covers |
| 512 | A | Label Tag and Protect Control Interfaces |
| 513 | A | Install Temporary Protection Caps and Blanks |
| 520 | A | Remove |
| 521 | A | Remove Hybrid Propulsion Control Unit |
| 522 | A | Remove Mode Management Control Module |
| 523 | A | Remove Control Law and Authority Boundary Module |
| 524 | A | Remove Energy Command and Power Demand Module |
| 525 | A | Remove Propulsive Channel Control Interface Module |
| 526 | A | Remove Fault Tolerant Control and Degraded Mode Module |
| 530 | A | Disassembly |
| 531 | A | Disassemble Control Unit Mounting Hardware |
| 532 | A | Disassemble Control Interface Connector and Harness Supports |
| 533 | A | Disassemble Mode Management Interface Hardware |
| 534 | A | Disassemble Control Path Isolation Hardware |
| 540 | A | Post-Removal Inspection and Quarantine |
| 541 | A | Removed Item Preservation and Packaging |
| 590 | A | Removal Records and Evidence Capture |
| 700 | A | Assemble |
| 701 | A | Pre-Installation Safety Preparation |
| 702 | A | Installation Configuration Verification |
| 703 | A | Control Unit Hardware Preparation |
| 704 | A | Control Unit Mounting Hardware Assembly |
| 705 | A | Mode Management Interface Preparation |
| 706 | A | Energy Command Interface Preparation |
| 707 | A | Propulsive Channel Control Interface Preparation |
| 708 | A | Fault Tolerant Control Path Preparation |
| 710 | A | Access and Preparation for Installation |
| 711 | A | Prepare Access Panels and Protective Covers |
| 712 | A | Prepare Tagged Control Interfaces for Reconnection |
| 713 | A | Remove Temporary Protection Caps and Blanks |
| 720 | A | Install |
| 721 | A | Install Hybrid Propulsion Control Unit |
| 722 | A | Install Mode Management Control Module |
| 723 | A | Install Control Law and Authority Boundary Module |
| 724 | A | Install Energy Command and Power Demand Module |
| 725 | A | Install Propulsive Channel Control Interface Module |
| 726 | A | Install Fault Tolerant Control and Degraded Mode Module |
| 730 | A | Connect |
| 731 | A | Connect Data Control and Signal Interfaces |
| 732 | A | Connect High Voltage and Low Voltage Control Power |
| 733 | A | Connect Mode Management Interfaces |
| 734 | A | Connect Energy Command and Power Demand Interfaces |
| 735 | A | Connect Propulsive Channel Control Interfaces |
| 736 | A | Connect Control Law and Authority Boundary Interfaces |
| 737 | A | Connect Fault Tolerant Control Path Interfaces |
| 740 | A | Post-Installation Inspection |
| 741 | A | Installation Torque and Locking Verification |
| 742 | A | Continuity Insulation and Bonding Verification |
| 743 | A | Control Interface Verification |
| 744 | A | Mode Management Interface Verification |
| 745 | A | Energy Command and Power Demand Interface Verification |
| 746 | A | Fault Tolerant Control Path Verification |
| 750 | A | Restore System to Test Configuration |
| 751 | A | Restore Access Panels and Protective Covers |
| 752 | A | Enable Safe Test Power Configuration |
| 790 | A | Installation Records and Evidence Capture |
| 941 | A | Illustrated Parts Data |
| 941 | B | Hybrid Propulsion Control Parts Index |
| 941 | C | Hybrid Propulsion Control Unit Illustrated Parts Data |
| 941 | D | Mode Management Control Module Illustrated Parts Data |
| 941 | E | Control Law and Authority Boundary Module Illustrated Parts Data |
| 941 | F | Energy Command and Power Demand Module Illustrated Parts Data |
| 941 | G | Propulsive Channel Control Interface Module Illustrated Parts Data |
| 941 | H | Fault Tolerant Control and Degraded Mode Module Illustrated Parts Data |
| 941 | J | Data Control and Signal Harness Illustrated Parts Data |
| 941 | K | High Voltage and Low Voltage Control Power Harness Illustrated Parts Data |
| 941 | L | Mode Management Connector and Switching Hardware Illustrated Parts Data |
| 941 | M | Energy Command Interface Hardware Illustrated Parts Data |
| 941 | N | Control Path Isolation Hardware Illustrated Parts Data |
| 941 | P | Mounting Brackets Supports and Fasteners Illustrated Parts Data |
| 941 | Q | Labels Tags and Identification Plates Illustrated Parts Data |
| 941 | R | Seals Caps Blanks and Protective Items Illustrated Parts Data |
| 941 | S | Consumables and Standard Parts Illustrated Parts Data |
| 941 | Z | Illustrated Parts Data Traceability and Effectivity |

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
