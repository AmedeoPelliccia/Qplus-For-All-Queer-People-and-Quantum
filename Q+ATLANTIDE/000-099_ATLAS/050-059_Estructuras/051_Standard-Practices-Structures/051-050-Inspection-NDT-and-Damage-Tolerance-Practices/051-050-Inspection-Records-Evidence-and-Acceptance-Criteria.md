---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-050-INSPECTION-RECORDS-EVIDENCE-AND-ACCEPTANCE-CRITERIA"
title: "ATLAS 050-059 · 05.051.050 — Inspection Records, Evidence and Acceptance Criteria"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../../README.md
parent_section_doc: ../../README.md
parent_subsection_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "050-059"
section: "05"
section_title: "Estructuras"
subsection: "051"
subsection_title: "Standard Practices — Structures"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
subsubject: "050"
subsubject_title: "Inspection, NDT and Damage-Tolerance Practices"
parent_subsubject_doc: ./README.md
---

# ATLAS 050-059 · 05.051.050 — Inspection Records, Evidence and Acceptance Criteria

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Defines the documentation requirements, evidence standards, and acceptance criteria for structural inspections and NDT findings. Comprehensive and traceable inspection records are a regulatory requirement and a key element of the aircraft continuing airworthiness data package.

---

## 2. Scope

### 2.1 Context

Inspection records must capture the task reference, date, aircraft registration, inspector identity, access achieved, findings, and disposition. For NDT tasks, additional evidence includes calibration records, scan data files, and certified personnel qualification. Records form part of the aircraft continuing airworthiness data package and must be retained for the life of the aircraft plus the period specified by the national authority.

Electronic records stored in CSDB-linked maintenance management systems must be protected against unauthorised modification and must provide an audit trail showing the creation, amendment, and approval history of each record. Paper records must be legible, indelible, and stored in a controlled environment to prevent deterioration.

### 2.2 Scope Diagram

```mermaid
graph TD
    A[Inspection Completed] --> B[Complete Maintenance Record]
    B --> C[Record: AMM Task Ref, Date, Reg, Inspector ID]
    C --> D[NDT Evidence: Scan Data, Calibration Sheet, Level 2 Cert]
    D --> E[Document All Findings with Measurements]
    E --> F[Disposition Each Finding: Repair/Accept/Monitor]
    F --> G[CRS Issued by Certifying Staff]
    G --> H[Record Archived with CAMO/Part-M System]
    H --> I[Retain for Aircraft Life]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Record Retention Period | Aircraft life or per national authority minimum |
| Inspector Identity Requirement | Part-66 AME licence category and authorisation |
| NDT Evidence Format | Scan data archived in CSDB-compatible format |
| Calibration Traceability | UKAS-accredited or national metrology standard |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-050-INSPECTION-RECORDS-EVIDENCE-AND-ACCEPTANCE-CRITERIA` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-050-Inspection-NDT-and-Damage-Tolerance-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| EASA Part-145.A.55 | Maintenance Records Requirements |
| EASA Part-M.A.306 | Technical Log and Continuing Airworthiness Records |
| EN 4179 | NDT Record Requirements and Personnel Certification |
| ATA Spec 2200 | Documentation Standard for Aviation Maintenance |
