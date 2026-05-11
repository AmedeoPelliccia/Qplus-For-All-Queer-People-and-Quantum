---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-051-060-SURFACE-CLEANING-AND-PREPARATION"
title: "ATLAS 050-059 · 05.051.060 — Surface Cleaning and Preparation"
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

# ATLAS 050-059 · 05.051.060 — Surface Cleaning and Preparation

> **ATLAS-1000** · Q+ATLANTIDE Baseline · Section 05.051 Standard Practices — Structures

---

## 1. Purpose

Defines approved methods for cleaning and preparing metallic and composite aircraft surfaces prior to surface treatment, priming, painting, or bonding operations. Surface cleanliness is the fundamental prerequisite for adhesion of all protective coatings and bonded repairs.

---

## 2. Scope

### 2.1 Context

Surface cleanliness directly determines the adhesion quality of primers, topcoats, and bonded repairs. Contamination from hydraulic fluid, lubricating oils, and release agents must be fully removed before any coating or bonding operation proceeds. Solvent cleaning is followed by mechanical abrasion or chemical conversion to create a chemically active, high surface energy substrate.

Different preparation sequences apply to different substrates: aluminium alloys require degreasing, abrasion, and chemical conversion (alodine or phosphoric acid anodise); titanium requires degreasing and passivation; steel requires degreasing, abrasion, and phosphate treatment or primer direct; composite surfaces require peel-ply removal or controlled abrasion followed by primer. The correct sequence for each substrate is specified in the applicable AMM task or BMS specification.

### 2.2 Scope Diagram

```mermaid
graph TD
    A[Surface to Prepare] --> B[Remove Old Coating if Required]
    B --> C[Degrease: Solvent Wipe with MEK or IPA]
    C --> D[Mechanical Abrasion: 180-grit Scotch-Brite or equivalent]
    D --> E[Re-degrease with Clean Solvent]
    E --> F[Chemical Conversion Coating: Alodine or Phosphoric Acid Anodise]
    F --> G[Inspect Water-Break-Free — ≥ 30 sec continuous sheet]
    G --> H[Apply Primer Within Open Time]
    H --> I[Document Process Parameters]
```

### 2.3 Key Parameters

| Parameter | Value |
|-----------|-------|
| Degreasing Solvent | MEK (ASTM D740) or IPA (MIL-I-6702) |
| Abrasive Grade | 120–220 grit aluminium oxide or 180-grit Scotch-Brite |
| Alodine Specification | MIL-DTL-5541 Type 1 or Type 2 |
| Water-Break-Free Duration | ≥ 30 sec continuous water sheet required |

---

## 3. Footprint

| Field | Value |
|-------|-------|
| **Document ID** | `QATL-ATLAS-1000-ATLAS-050-059-05-051-060-SURFACE-CLEANING-AND-PREPARATION` |
| **Status** | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| **Folder Path** | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/051_Standard-Practices-Structures/051-060-Corrosion-Protection-Sealing-and-Surface-Treatment/` |

---

## 4. References

> [^1]: All references below are applicable at the revision level current at the time of document release. Superseded revisions must be assessed for impact before continued use.

| Reference | Description |
|-----------|-------------|
| MIL-DTL-5541 | Chemical Conversion Coating for Aluminium Alloys |
| ASTM B449 | Chemical Film on Aluminium — Quality and Verification |
| AMM Chapter 51 | Surface Preparation Procedures |
| BMS 10-11 | Primer Application Process Specification |
