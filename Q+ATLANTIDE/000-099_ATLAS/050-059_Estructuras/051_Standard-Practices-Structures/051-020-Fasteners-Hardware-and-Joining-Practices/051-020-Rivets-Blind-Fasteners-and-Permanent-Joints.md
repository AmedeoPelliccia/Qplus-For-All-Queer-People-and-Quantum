---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-020-RIVETS-BLIND-FASTENERS-AND-PERMANENT-JOINTS"
title: "ATLAS 050-059 · 05.051.020 — Rivets, Blind Fasteners, and Permanent Joints"
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
subsubject: "020"
subsubject_title: "Fasteners, Hardware and Joining Practices"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
---

# ATLAS 050-059 · 05.051.020 — Rivets, Blind Fasteners, and Permanent Joints

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Specifies the types, installation methods, and acceptance criteria for solid rivets, blind rivets, and lockbolts used to create permanent structural joints in Q+ATLANTIDE aircraft.

---

## 2. Scope

### 2.1 Context

Solid rivets driven in interference are the classic permanent structural fastener for aluminium aircraft structure, providing excellent fatigue performance when properly installed with correct driven-head dimensions and shop-head geometry.

Blind fasteners (e.g., Cherry® MAXIBOLT®, Huck BOM®) provide permanent one-sided access installation capability for closed-section structures and remote fastening applications where a bucking bar cannot reach.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[Permanent Joint Requirement] --> B{Access Type?}
        B -- Two-Sided --> C[Solid Rivet]
        B -- One-Sided --> D[Blind Fastener]
        C --> E[Drill, Deburr, Countersink]
        C --> F[Insert Rivet / Drive / Buck]
        D --> E
        D --> G[Insert Blind Fastener / Pull Tool]
        E & F & G --> H[Inspect Driven Head / Set]
        H --> I[Accept / Replace]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Solid Rivet Std | AN426 / AN470 / MS20427 |
| Blind Fastener | Cherry MAXIBOLT / Huck BOM |
| Hole Size Tolerance | H7 or per fastener spec |
| Driven Head | Diameter ≥1.4× shank, height per spec |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-020-RIVETS-BLIND-FASTENERS-AND-PERMANENT-JOINTS` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-020-Fasteners-Hardware-and-Joining-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| AMM 51-43-00 | Rivet Installation and Inspection |
| AN426 | 100° Countersunk Head Rivets |
| AN470 | Universal Head Rivets |
| EASA CS-25.607 | Permanent Fastener Requirements |
