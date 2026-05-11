---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-020-HARDWARE-INSPECTION-REUSE-AND-REPLACEMENT-RULES"
title: "ATLAS 050-059 · 05.051.020 — Hardware Inspection, Reuse, and Replacement Rules"
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

# ATLAS 050-059 · 05.051.020 — Hardware Inspection, Reuse, and Replacement Rules

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Defines the inspection criteria, reuse limitations, and replacement rules for structural fasteners and hardware removed during maintenance, ensuring that reused hardware meets fitness-for-purpose requirements.

---

## 2. Scope

### 2.1 Context

Not all fasteners are eligible for reuse after removal. Self-locking nuts have a defined maximum reuse cycle; titanium bolts from interference-fit joints must be replaced; and fasteners from fatigue-critical locations require inspection before any reuse authorisation.

Replacement hardware must match the original specification or be covered by an approved substitute listing in the AMM or engineering order. Mixing of fastener grades, coatings, or material designations in the same joint is prohibited without engineering approval.

### 2.2 Scope Diagram

```mermaid
graph TD
    graph TD
        A[Fastener Removed] --> B[Visual Inspection]
        B --> C{Serviceability Check}
        C -- Scrap --> D[Discard — Replace New]
        C -- Marginal --> E[Dimensional Inspection]
        E --> F{Within Limits?}
        F -- Yes --> G[Reuse Authorised — Record]
        F -- No --> D
        C -- Serviceable --> G
        G --> H[Record Reuse Count if NAS21042 Nut]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Self-Lock Nut Max Reuse | 3 cycles — MS21042 |
| Titanium Bolt Reuse | Not permitted — interference fit |
| Inspection Method | Visual + dimensional + DPT if cracked |
| Replace Spec | Match OEM part number or approved sub |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-020-HARDWARE-INSPECTION-REUSE-AND-REPLACEMENT-RULES` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-020-Fasteners-Hardware-and-Joining-Practices/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| AMM 51-40-00 | Fastener Reuse Limitations |
| MS21042 | Self-Locking Nut — Reuse Cycle |
| EASA Part-145 Appendix II | Hardware Control |
| NAS Standards | Fastener Replacement Tables |
