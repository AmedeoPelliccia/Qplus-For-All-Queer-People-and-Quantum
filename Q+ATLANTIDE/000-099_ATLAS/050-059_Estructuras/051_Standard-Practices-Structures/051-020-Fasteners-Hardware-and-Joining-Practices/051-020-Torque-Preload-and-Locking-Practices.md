---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-020-TORQUE-PRELOAD-AND-LOCKING-PRACTICES"
title: "ATLAS 050-059 · 05.051.020 — Torque, Preload, and Locking Practices"
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

# ATLAS 050-059 · 05.051.020 — Torque, Preload, and Locking Practices

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Establishes the torque application procedures, preload requirements, and locking methods for all threaded fasteners in structural applications on Q+ATLANTIDE aircraft.

---

## 2. Scope

### 2.1 Context

Correct preload is essential to fastener joint performance: insufficient preload permits fatigue-inducing slip under dynamic loads, while excessive preload can cause thread stripping or fastener fracture in high-tensile applications.

Locking features (self-locking nuts, lockwire, cotter pins, thread-locking compounds) prevent vibration loosening and are mandatory on all structural fasteners where the joint is subject to dynamic or vibration loading.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[Fastener Installation] --> B[Verify Fastener Condition & Lubrication]
        B --> C[Run Down by Hand]
        C --> D[Apply Torque — Calibrated Wrench]
        D --> E[Check Torque Value vs Table]
        E --> F{Correct Range?}
        F -- Yes --> G[Apply Locking Method]
        F -- No --> H[Remove — Investigate]
        G --> I[Record on Task Card]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Torque Tables | AMM 20-13-00 / Boeing BMS 8-8 |
| Torque Tool Cal | ISO 6789 — ±4% |
| Locking Types | Self-lock nut / lockwire / Loctite 243 |
| Nut Re-Use | Max 3 re-uses per MS21042 |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-020-TORQUE-PRELOAD-AND-LOCKING-PRACTICES` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-020-Fasteners-Hardware-and-Joining-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| AMM 20-13-00 | Torque Application Procedures |
| ISO 6789 | Torque Wrench Calibration |
| EASA CS-25.607 | Fastener Locking Requirements |
| MIL-PRF-8516 | Lockwire — Corrosion-Resistant Steel |
