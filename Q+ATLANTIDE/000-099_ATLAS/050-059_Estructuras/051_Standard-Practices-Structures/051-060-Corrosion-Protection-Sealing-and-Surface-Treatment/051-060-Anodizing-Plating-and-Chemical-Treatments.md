---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-060-ANODIZING-PLATING-AND-CHEMICAL-TREATMENTS"
title: "ATLAS 050-059 · 05.051.060 — Anodizing, Plating and Chemical Treatments"
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
subsubject: "060"
subsubject_title: "Corrosion Protection, Sealing and Surface Treatment"
parent_subsubject_doc: ./README.md
---

# ATLAS 050-059 · 05.051.060 — Anodizing, Plating and Chemical Treatments

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Defines the approved anodising, plating, and chemical conversion coating treatments for corrosion protection of metallic aircraft structure. These electrochemical and chemical processes form the base protection layer upon which subsequent primer and topcoat systems are applied.

---

## 2. Scope

### 2.1 Context

Anodising produces an oxide layer on aluminium that provides corrosion resistance and significantly improves adhesion for subsequent primers. Type II sulphuric acid anodising is the standard process for aluminium structural components. Type III hard anodising provides a thicker, harder oxide for wear-resistant surfaces such as hinges and sliding contacts. Chromic acid anodising (Type I) provides thin films with minimal dimensional change, used where close tolerances are critical.

Cadmium plating provides galvanically compatible, lubricious protection for steel fasteners and hardware. Alternatives to cadmium (zinc-nickel, aluminium-slurry) are increasingly required due to environmental restrictions on cadmium use in certain jurisdictions. All plating processes must be performed by qualified processors to the applicable AMS specification, with certification to accompany each batch.

### 2.2 Scope Diagram

```mermaid
graph TD
    A[Component Material Identified] --> B{Material?}
    B -->|Aluminium| C[Select Anodise Type]
    C --> D[Type I — Chromic Acid BAC 5765 — tight tolerance parts]
    C --> E[Type II — Sulphuric Acid AMS 2470 — standard structural]
    C --> F[Type III — Hard Anodise AMS 2469 — wear surfaces]
    B -->|Steel| G[Cadmium Plate AMS 2400 / Zinc-Nickel alternative]
    B -->|Titanium| H[Passivate AMS 2816]
    D --> I[Seal and Apply Primer]
    E --> I
    F --> I
    G --> I
    H --> I
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Type II Anodise Thickness | 18–25 µm per AMS 2470 |
| Type III Hard Anodise Thickness | 25–75 µm per AMS 2469 |
| Cadmium Plate Thickness | 5–13 µm per AMS 2400 |
| Alodine Touch-Up Thickness | 0.1–1.0 µm per MIL-DTL-5541 |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-060-ANODIZING-PLATING-AND-CHEMICAL-TREATMENTS` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-060-Corrosion-Protection-Sealing-and-Surface-Treatment/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| AMS 2470 | Sulphuric Acid Anodic Coating of Aluminium Alloys |
| AMS 2469 | Hard Anodic Coating of Aluminium Alloys |
| AMS 2400 | Cadmium Plating |
| MIL-DTL-5541 | Chemical Conversion Coatings on Aluminium |
