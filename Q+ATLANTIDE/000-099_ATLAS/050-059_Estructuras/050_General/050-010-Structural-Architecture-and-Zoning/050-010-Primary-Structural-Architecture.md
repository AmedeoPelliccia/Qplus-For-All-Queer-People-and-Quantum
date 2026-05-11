---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-010-PRIMARY-STRUCTURAL-ARCHITECTURE"
title: "ATLAS 050-059 · 05.050.010 — Primary Structural Architecture"
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
subsubject: "010"
subsubject_title: "Primary Structural Architecture"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.050.010 — Primary Structural Architecture

## 1. Purpose

Describes the **primary structural architecture** of the AMPEL360 eWTW: the PSE network, principal load paths, key structural elements, and their architectural arrangement across the airframe.

## 2. Scope

### 2.1 Primary Load Paths

The AMPEL360 primary structural architecture is built around four principal load paths:

| Load path | Description | Key PSEs |
|---|---|---|
| **Wing bending** | Wing lift loads transferred inboard through spars to WFIJ | PSE-W01, PSE-W02, PSE-J01 |
| **Fuselage hoop** | Pressure vessel hoop stress in fuselage frames and skin | PSE-F01 |
| **Fuselage bending** | Fuselage bending carried by keel beam, crown beam, skin | PSE-F01 |
| **Empennage** | HTP/VTP loads transferred to rear fuselage via attach fittings | PSE-H01, PSE-V01 |

### 2.2 PSE Arrangement Diagram

```mermaid
graph TD
    WING_BENDING[Wing Bending LP] --> WFIJ[WFIJ PSE-J01]
    WFIJ --> CFUS[Centre Fuselage PSE-F01]
    PYLON[Pylon LP PSE-P01] --> WING_BOX[Wing Box PSE-W01/W02]
    WING_BOX --> WFIJ
    CFUS --> RFUS[Rear Fuselage PSE-F01]
    RFUS --> HTP_ATTACH[HTP Attach PSE-H01]
    RFUS --> VTP_ATTACH[VTP Attach PSE-V01]
```

### 2.3 Key Design Features

| Feature | AMPEL360 specific |
|---|---|
| Wing-fuselage joint | WFIJ — 4-bolt carbon/titanium joint; multi-load-path |
| Fuselage barrel | 6-barrel all-CFRP semi-monocoque; integral tear-straps |
| Wing box | 2-spar CFRP box with CFRP ribs; no hydraulic pump bay in wing |
| Centre box | Full-depth centre wing box integrated with fuselage floor beam grid |
| Pylon | Short, stiff titanium pylon; electric motor attachment loads |

### 2.4 CS-25 Compliance Basis

| PSE group | CS-25 basis |
|---|---|
| Wing, fuselage, WFIJ | §25.571(b) — Damage-tolerant design |
| Pylon main fittings | §25.571(b) + §25.581 lightning criteria |
| Landing gear attach | §25.571(c) — Safe-life (no damage-tolerant design possible) |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-010-PRIMARY-STRUCTURAL-ARCHITECTURE` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| CS-25.571 | Damage-tolerance and fatigue evaluation |
| CS-25.581 | Lightning protection — structures |
| [`./README.md`](./README.md) | Subsubject index |
