---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-050-AIRCRAFT-EFFECTIVITY-AND-CONFIGURATION-BASELINES"
title: "ATLAS 050-059 · 05.050.050 — Aircraft Effectivity and Configuration Baselines"
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
subsubject: "050"
subsubject_title: "Aircraft Effectivity and Configuration Baselines"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
standard_scope: agnostic
programme_specific: false
---

# ATLAS 050-059 · 05.050.050 — Aircraft Effectivity and Configuration Baselines

## 1. Purpose

Defines the **aircraft effectivity and configuration baselines** used to bound the structural documentation set: the structural configuration baseline (SCB) identifiers, their scope relative to production lots and design changes, and how configuration baselines are referenced in maintenance and repair documentation.

## 2. Scope

### 2.1 Context

A structural configuration baseline (SCB) is a formally controlled snapshot of the [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT] structural definition at a given programme phase or production lot boundary. SCBs are issued at first-flight, type-certification, entry-into-service, and after each major structural modification campaign. All structural ATLAS documents carry a `baseline_ref` indicating the SCB under which their content was validated.

Effectivity within an SCB is further resolved by the PDCM master aircraft register, which maps each aircraft serial number (SN) to the SCB applicable at delivery and records all subsequent SB incorporations. Maintenance documentation applicability is filtered against the current SCB + SB-incorporation state of the specific aircraft.

### 2.2 Configuration Baseline Lifecycle

```mermaid
stateDiagram-v2
    [*] --> SCB_PDR: Programme launch
    SCB_PDR --> SCB_CDR: Critical design review
    SCB_CDR --> SCB_FF: First flight
    SCB_FF --> SCB_TC: Type certification
    SCB_TC --> SCB_EIS: Entry into service
    SCB_EIS --> SCB_MOD1: Major modification SB-001
    SCB_MOD1 --> SCB_MOD2: Subsequent modification
```

### 2.3 Structural Configuration Baseline Register

| SCB ID | Milestone | SN Range | Structural Scope |
|---|---|---|---|
| SCB-01 | PDR | — | Pre-design baseline |
| SCB-02 | CDR | — | Frozen design baseline |
| SCB-03 | First Flight | SN 001 | Flight-test configuration |
| SCB-04 | Type Cert | SN 001–010 | Certification baseline |
| SCB-05 | EIS | SN 001–050 | Delivery baseline |
| SCB-06 | SB-001 retrofit | SN 001–050 post-SB | Post-modification baseline |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-050-AIRCRAFT-EFFECTIVITY-AND-CONFIGURATION-BASELINES` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/050_General/050-050-Applicability-and-Effectivity/` |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| S1000D Issue 5.0 | Configuration baseline management |
| ATA iSpec 2200 | Aircraft effectivity chapter |
| PDCM-[PROGRAMME-AIRCRAFT]-001 | Product Definition and Configuration Management Plan |
| [`./README.md`](./README.md) | Subsubject 050 index |
| [`../README.md`](../README.md) | 050_General subsection index |
