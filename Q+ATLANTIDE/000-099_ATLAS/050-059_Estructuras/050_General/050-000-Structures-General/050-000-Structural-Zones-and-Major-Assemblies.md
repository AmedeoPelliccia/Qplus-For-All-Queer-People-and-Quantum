---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-000-STRUCTURAL-ZONES-AND-MAJOR-ASSEMBLIES"
title: "ATLAS 050-059 · 05.050.000 — Structural Zones and Major Assemblies"
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
subsubject_title: "Structural Zones and Major Assemblies"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.050.000 — Structural Zones and Major Assemblies

## 1. Purpose

Defines the **structural zone map** and **major assembly list** for the AMPEL360 eWTW, providing the reference coordinate system, zone identifiers, and major assembly part-number families used across all structural documentation.

## 2. Scope

### 2.1 Coordinate System and Station Reference

- **FS** (Fuselage Station): measured aft from datum FS 0.000 at nose reference plane, in mm.
- **WS** (Wing Station): measured outboard from aircraft centreline, in mm.
- **WL** (Water Line): measured upward from ground datum, in mm.
- **BL** (Buttock Line): measured laterally from aircraft centreline, in mm.

### 2.2 Zone Map Summary

| Zone | Description | FS range (approx.) | ATLAS subsection |
|---|---|---|---|
| Z100 | Forward fuselage (nose to fwd pressure bulkhead) | 0–2500 | 053_Fuselage |
| Z200 | Forward cabin (fwd bulkhead to wing leading edge) | 2500–7000 | 053_Fuselage |
| Z300 | Centre wing box / cabin intersection | 7000–11000 | 053_Fuselage + 057_Wings |
| Z400 | Rear cabin (wing TE to aft pressure bulkhead) | 11000–17500 | 053_Fuselage |
| Z500 | Tail cone and empennage attach | 17500–21000 | 053_Fuselage + 055_Stabilizers |
| Z600 | Wing — inboard box | WS 0–4500 | 057_Wings |
| Z700 | Wing — outboard box | WS 4500–16000 | 057_Wings |
| Z800 | Pylons and nacelles | — | 054_Nacelles-and-Pylons |
| Z900 | Doors and frames | Multiple FS | 052_Doors |

### 2.3 Major Structural Assemblies

| Assembly | Designation | Material | Supplier class |
|---|---|---|---|
| Forward fuselage section | SEC-100 | CFRP (IM7/8552) | TBD |
| Centre fuselage section | SEC-200 | CFRP (IM7/8552) | TBD |
| Rear fuselage section | SEC-300 | CFRP (IM7/8552) | TBD |
| Wing box — LH | WB-L | CFRP (IM7/977-3) | TBD |
| Wing box — RH | WB-R | CFRP (IM7/977-3) | TBD |
| Wing-fuselage interface joint | WFIJ | Ti-6Al-4V + CFRP | TBD |
| HTP primary structure | HTP-PRIM | CFRP | TBD |
| VTP primary structure | VTP-PRIM | CFRP | TBD |
| Pylon — LH | PYL-L | Ti-6Al-4V primary | TBD |
| Pylon — RH | PYL-R | Ti-6Al-4V primary | TBD |

### 2.4 Assembly Interface Diagram

```mermaid
graph TD
    SEC100[SEC-100 Forward Fuselage] --> SEC200[SEC-200 Centre Fuselage]
    SEC200 --> SEC300[SEC-300 Rear Fuselage]
    SEC200 --> WBL[WB-L Wing Box LH]
    SEC200 --> WBR[WB-R Wing Box RH]
    WBL --> PULL[PYL-L Pylon LH]
    WBR --> PYLR[PYL-R Pylon RH]
    SEC300 --> HTP[HTP Primary]
    SEC300 --> VTP[VTP Primary]
```

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-000-STRUCTURAL-ZONES-AND-MAJOR-ASSEMBLIES` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| CS-25.301 | Loads — structural zone applicability |
| [`./README.md`](./README.md) | Subsubject index |
| [`../README.md`](../README.md) | 050_General subsection index |
