---
document_id: "QATL-ATLAS-1000-ATLAS-050-059-05-050-060-STRUCTURAL-LRU-SRU-AND-ASSEMBLY-REPLACEMENT-BOUNDARIES"
title: "ATLAS 050-059 · 05.050.060 — Structural LRU, SRU and Assembly Replacement Boundaries"
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
subsection: "050"
subsection_title: "General"
subsubject: "060"
subsubject_title: "Structural LRU, SRU and Assembly Replacement Boundaries"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
standard_scope: agnostic
programme_specific: false
---

# ATLAS 050-059 · 05.050.060 — Structural LRU, SRU and Assembly Replacement Boundaries

## 1. Purpose

Defines the **Line Replaceable Unit (LRU), Shop Replaceable Unit (SRU), and structural assembly replacement boundaries** for the [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT], identifying which structural components are designed for removal and replacement at line or base maintenance, and which require depot-level disassembly or permanent bonded/fastened repair schemes.

## 2. Scope

### 2.1 Context

The [PROGRAMME-AIRCRAFT] [PROGRAMME-VARIANT] structural design maximises replaceability of access panels, secondary fairings, and modular structural attachments to minimise aircraft on-ground (AOG) time. Primary structural elements (wing spar, centre-wing box, main frames) are not LRUs — they are repaired in-situ via SRM or MRA schemes. However, the LH₂ tank assembly is designed as a depot-replaceable unit due to cryogenic seal integrity requirements, and the modular DEP nacelle attachment frames are base-maintainable LRU-level assemblies.

The LRU/SRU classification defines the spares inventory requirements, the RSPL (Recommended Spare Parts List), and the skill and tooling requirements at each maintenance level. It also drives the S1000D data module scope (procedure DMs for LRU removal/installation vs. repair DMs for non-replaceable structure).

### 2.2 Replacement Boundary Classification

```mermaid
flowchart LR
    A[Structural Element] --> B{Replaceable?}
    B -->|Yes, line| C[LRU: Line Replaceable Unit]
    B -->|Yes, base or depot shop| D[SRU: Shop Replaceable Unit]
    B -->|No, repair in situ| E[Non-Replaceable: SRM or MRA repair]
    C --> F[Removal and installation AMM procedure]
    D --> G[Shop maintenance manual SMM procedure]
    E --> H[SRM repair or MRA engineering disposition]
```

### 2.3 Structural LRU / SRU Register (Top Level)

| Item | Classification | Level | Replacement Driver |
|---|---|---|---|
| Access and inspection panels | LRU | Line | Damage or scheduled removal |
| Trailing-edge flap track assembly | LRU | Base | Wear, corrosion, damage |
| DEP nacelle attachment frame | LRU | Base | Fatigue life, damage |
| LH₂ tank assembly | SRU | Depot | Seal integrity, corrosion, life limit |
| Main gear primary fitting | SRU | Depot | Safe-life limit |
| Wing spar cap | Non-replaceable | Depot repair (SRM/MRA) | Damage beyond ADL |
| Centre-wing box lower panel | Non-replaceable | Depot repair (SRM/MRA) | Fatigue or damage |

## 3. Footprint

| Metric | Value |
|---|---|
| Document ID | `QATL-ATLAS-1000-ATLAS-050-059-05-050-060-STRUCTURAL-LRU-SRU-AND-ASSEMBLY-REPLACEMENT-BOUNDARIES` |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/050_General/050-060-Maintenance-Concept-General/` |

## 4. References

[^baseline]: Q+ATLANTIDE Baseline — [`organization/Q+ATLANTIDE.md`](../../../../../organization/Q+ATLANTIDE.md)

| Ref | Document |
|---|---|
| ATA iSpec 2200 | LRU and SRU classification |
| AMM-[PROGRAMME-AIRCRAFT]-050 | Aircraft Maintenance Manual — Structures |
| RSPL-[PROGRAMME-AIRCRAFT]-001 | Recommended Spare Parts List |
| SRM-[PROGRAMME-AIRCRAFT]-050 | Structural Repair Manual |
| [`./README.md`](./README.md) | Subsubject 060 index |
| [`../README.md`](../README.md) | 050_General subsection index |
