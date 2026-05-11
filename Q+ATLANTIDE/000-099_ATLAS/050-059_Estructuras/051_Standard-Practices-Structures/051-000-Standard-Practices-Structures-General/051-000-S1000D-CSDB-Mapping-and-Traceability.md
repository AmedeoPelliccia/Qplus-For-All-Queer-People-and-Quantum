---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-000-S1000D-CSDB-MAPPING-AND-TRACEABILITY"
title: "ATLAS 050-059 · 05.051.000 — S1000D CSDB Mapping and Traceability"
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
subsection: "051"
subsection_title: "Standard Practices — Structures"
subsubject: "000"
subsubject_title: "Standard Practices Structures General"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.051.000 — S1000D CSDB Mapping and Traceability

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Provides the S1000D Data Module Code (DMC) mapping and Common Source Data Base (CSDB) traceability matrix for all documents within the 051-000 Standard Practices Structures General subsubject.

---

## 2. Scope

### 2.1 Context

Each document in this subsubject is assigned a unique S1000D DMC that anchors it within the CSDB hierarchy. The DMC structure follows ATLAS-1000 BREX rules and the Q+ATLANTIDE information set taxonomy.

Traceability ensures that every ATLAS document can be traced forward to publication modules (PMs) and backward to source requirements, supporting configuration management, export control, and regulatory audit.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[ATLAS-1000 CSDB] --> B[051-000 Subsubject]
        B --> C[DMC Assignment]
        C --> D[Data Module Status List]
        D --> E[Publication Module Mapping]
        E --> F[AMM / CMM / IPC]
        B --> G[Applicability Cross-Ref]
        G --> H[BREX Rule Validation]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| DMC Model ID | QATL |
| SNS | 050-059 Structures |
| Disassembly Code | 051-000 |
| Issue Date | Per CSDB commit log |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-000-S1000D-CSDB-MAPPING-AND-TRACEABILITY` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-000-Standard-Practices-Structures-General/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| S1000D Issue 5.0 | Data Module Coding Rules |
| ASD SX000i | Integrated Technical Publication Framework |
| ATLAS BREX | Q+ATLANTIDE Business Rules Exchange |
| CSDB Config Plan | ATLAS-1000 CSDB Configuration Management Plan |
