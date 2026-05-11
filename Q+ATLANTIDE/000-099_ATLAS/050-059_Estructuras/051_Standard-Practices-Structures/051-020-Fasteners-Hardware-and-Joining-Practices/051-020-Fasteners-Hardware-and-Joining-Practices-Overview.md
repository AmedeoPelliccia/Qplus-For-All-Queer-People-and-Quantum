---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-020-FASTENERS-HARDWARE-AND-JOINING-PRACTICES-OVERVIEW"
title: "ATLAS 050-059 · 05.051.020 — Fasteners, Hardware, and Joining Practices — Overview"
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

# ATLAS 050-059 · 05.051.020 — Fasteners, Hardware, and Joining Practices — Overview

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Provides an overview of the fasteners, hardware types, and joining practices used in Q+ATLANTIDE aircraft structures, covering mechanical fastening, bonded joining, and hybrid joining methods.

---

## 2. Scope

### 2.1 Context

Fasteners and joining hardware are critical structural elements that transfer loads between structural members. This subsubject covers classification, selection, installation, inspection, and traceability of all fastener and joining systems used in ATLAS-registered aircraft.

Joining practices include torque application, interference fit installation, rivet driving, bonded joint preparation, and hybrid mechanically fastened/bonded assemblies, each governed by specific approved process instructions.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[Joining Requirement] --> B[Mechanical Fastening]
        A --> C[Bonded Joining]
        A --> D[Hybrid Joining]
        B --> E[Bolts / Screws / Rivets]
        C --> F[Adhesive Film / Paste]
        D --> G[Fastened + Bonded]
        E & F & G --> H[Installation Process]
        H --> I[Inspection & Record]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Fastener Types | Bolts, screws, rivets, blind fasteners |
| Joining Methods | Mechanical, bonded, hybrid |
| Installation Authority | LAE structural authorisation |
| Traceability | Batch/lot per AMS spec |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-020-FASTENERS-HARDWARE-AND-JOINING-PRACTICES-OVERVIEW` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-020-Fasteners-Hardware-and-Joining-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| AMM 51-40-00 | Fastener Installation — General |
| NAS Standards | National Aerospace Standards — Fasteners |
| MIL-HDBK-5 | Metallic Materials and Elements |
| EASA CS-25.607 | Fastener Provisions |
