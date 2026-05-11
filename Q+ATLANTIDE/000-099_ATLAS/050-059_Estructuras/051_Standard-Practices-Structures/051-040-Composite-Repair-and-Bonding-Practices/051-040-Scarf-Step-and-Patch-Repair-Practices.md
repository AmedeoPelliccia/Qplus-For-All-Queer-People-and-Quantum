---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-040-SCARF-STEP-AND-PATCH-REPAIR-PRACTICES"
title: "ATLAS 050-059 · 05.051.040 — Scarf, Step and Patch Repair Practices"
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
subsubject: "040"
subsubject_title: "Composite Repair and Bonding Practices"
parent_subsubject_doc: ./README.md
---

# ATLAS 050-059 · 05.051.040 — Scarf, Step and Patch Repair Practices

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Defines the approved geometric configurations for composite structural repairs including scarf, step-lap, and external patch geometries, with dimensional requirements for each. Geometry selection is driven by structural zone criticality, aerodynamic surface requirements, and repair tooling capability.

---

## 2. Scope

### 2.1 Context

Scarf repairs provide the highest joint efficiency and are used for primary structure where aerodynamic smoothness is critical. A scarf joint gradually transfers load through the taper angle, minimising stress concentration. Step-lap repairs are easier to execute in the field and provide good load transfer through discrete overlap steps but are restricted to secondary structure. External patch repairs are the fastest to apply but introduce a step on the outer mold line.

Scarf ratio selection depends on the laminate thickness and structural zone. Primary structure typically requires a 1:50 scarf ratio or better (shallower taper). Step width must be sufficient to transfer the load carried by each ply. All repair geometries must be verified by the certifying staff before ply application begins.

### 2.2 Scope Diagram

```mermaid
graph TD
    A[Repair Type Selected] --> B{Structure Zone?}
    B -->|Primary| C[Scarf Repair — Taper 1:20 to 1:100]
    B -->|Secondary| D[Step-Lap Repair — Step ≥ 12 mm per ply]
    B -->|Tertiary/Fairing| E[External Patch — Taper min 30:1 aero surface]
    C --> F[Machine Cavity with Router/Sander to Scarf Angle]
    D --> F
    E --> F
    F --> G[Measure Taper/Step — Verify Ply Count]
    G --> H[Layup Repair Plies]
    H --> I[Cure and NDT]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Minimum Scarf Ratio | 1:20 (secondary), 1:50 typical primary structure |
| Step Width (Step-Lap) | ≥ 12 mm per ply — measured radially |
| External Patch Taper | Minimum 30:1 on aerodynamic surfaces |
| Overlap Margin | ≥ 25 mm beyond NDT-confirmed damage boundary |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-040-SCARF-STEP-AND-PATCH-REPAIR-PRACTICES` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-040-Composite-Repair-and-Bonding-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| SRM Chapter 51 | Scarf and Step-Lap Repair Geometry Requirements |
| AMM 51-70-00 | Repair Cavity Preparation and Geometry Inspection |
| ASTM D5656 | Standard Test Method for Thick-Adherend Metal Lap-Shear Joints |
| FAA AC 145-6 | Composite Repair Classification and Geometry |
