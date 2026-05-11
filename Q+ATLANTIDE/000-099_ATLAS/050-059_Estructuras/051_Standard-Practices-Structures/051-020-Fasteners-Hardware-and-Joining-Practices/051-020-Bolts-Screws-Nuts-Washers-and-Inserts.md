---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-020-BOLTS-SCREWS-NUTS-WASHERS-AND-INSERTS"
title: "ATLAS 050-059 · 05.051.020 — Bolts, Screws, Nuts, Washers, and Inserts"
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

# ATLAS 050-059 · 05.051.020 — Bolts, Screws, Nuts, Washers, and Inserts

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Defines selection, installation, and torque application requirements for bolts, screws, nuts, washers, and thread inserts used in structural applications on Q+ATLANTIDE aircraft.

---

## 2. Scope

### 2.1 Context

Bolted joints form the primary disassemble-and-re-assemble structural joining method for major structural components. Correct selection of bolt grade, nut type, and washer stack is critical to achieving the design preload and preventing fretting corrosion.

Thread inserts (e.g., Heli-Coil®, Keensert®) are approved for use in parent material where thread damage has occurred or where a replaceable thread interface is required in composite or thin-wall metallic structure.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[Bolted Joint Design] --> B[Select Bolt — NAS/AN/MS]
        B --> C[Select Nut — Self-Locking/Hex]
        C --> D[Select Washer Stack]
        D --> E[Apply Corrosion-Inhibiting Sealant if Required]
        E --> F[Install and Apply Torque]
        F --> G[Torque Check & Record]
        G --> H[Apply Lockwire / Cotter Pin if Required]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Bolt Standard | NAS6204–NAS6220 / AN3–AN20 |
| Nut Standard | MS21042 Self-Locking / AN365 |
| Washer | AN960 / NAS1149 |
| Torque Tables | AMM 20-13 / Boeing BMS 8-8 |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-020-BOLTS-SCREWS-NUTS-WASHERS-AND-INSERTS` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-020-Fasteners-Hardware-and-Joining-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| AMM 20-13-00 | Torque Application |
| AN Standards | Air Force-Navy Aeronautical Standards |
| NAS Standards | National Aerospace Standards |
| EASA CS-25.607 | Fastener Provisions — Locking |
