---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-030-REPAIR-INSPECTION-VERIFICATION-AND-RELEASE"
title: "ATLAS 050-059 · 05.051.030 — Repair Inspection, Verification and Release"
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
subsubject: "030"
subsubject_title: "Structural Repair General Practices"
parent_subsubject_doc: ./README.md
---

# ATLAS 050-059 · 05.051.030 — Repair Inspection, Verification and Release

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Defines the inspection steps, acceptance criteria, and airworthiness release requirements for structural repairs prior to return to service. The release process ensures that each repair is fully verified and that the certifying staff confirms compliance with all applicable requirements.

---

## 2. Scope

### 2.1 Context

All structural repairs must undergo a documented inspection sequence covering workmanship, dimensional conformance, NDT acceptance, and final sign-off by an authorised certifying staff. The release must reference the applicable SRM scheme number or engineering order, the certifying staff's Part-66 licence number, and the date and aircraft registration.

Independent inspection (duplicate inspection) is required for structural repairs involving primary flight controls, primary load-bearing frames, or any repair designated as requiring two-person verification in the AMM. The independent inspector must confirm that the repair is complete and conforms to the approved data before the certifying staff issues the CRS.

### 2.2 Scope Diagram

```mermaid
graph TD
    A[Repair Completed] --> B[Workmanship Visual Inspection]
    B --> C[Dimensional Check vs Repair Drawing]
    C --> D[NDT — UT/Tap Test as Required by SRM]
    D --> E{Meets Acceptance Criteria?}
    E -->|Yes| F[Complete Repair Record]
    F --> G[Certifying Staff Sign-Off — EASA Form 1 / CRS]
    G --> H[Return to Service]
    E -->|No| I[Rework and Re-inspect]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Inspection Authority | EASA Part-145 Certifying Staff (Category B) |
| CRS Requirements | EASA Part-145.A.50 — statement of compliance |
| NDT Certification | EN 4179 / NAS 410 Level 2 minimum |
| Record Retention | Per Part-M / Part-CAMO — minimum aircraft life |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-030-REPAIR-INSPECTION-VERIFICATION-AND-RELEASE` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-030-Structural-Repair-General-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| EASA Part-145.A.50 | Certification of Maintenance — Release to Service |
| EN 4179 | Qualification and Approval of Personnel for NDT |
| AMM 51-70-00 | Repair Release and Inspection Procedures |
| SRM Chapter 51 | Repair Acceptance Criteria by Repair Type |
