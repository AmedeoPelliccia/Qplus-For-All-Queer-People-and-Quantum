---
document_id: QATL-ATLAS-1000-STA-110-119-01-111-000-OVERVIEW
title: "STA 110-119 · 01.111.000 — Overview"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "110-119"
section: "01"
section_title: "Estructuras y Materiales Espaciales"
subsection: "111"
subsection_title: "Materiales Espaciales"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 110-119 · Section 01 · Subsection 111 — Materiales Espaciales

## 1. Purpose

Overview entry-point for the *Materiales Espaciales* subsection within the `110-119` code range (Section `01` — *Estructuras y Materiales Espaciales*) of the **STA** architecture band.

This subsubject (`000 Overview`) introduces the STA 110-119.111 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline]. It establishes the materials engineering framework governing controlled definitions, material family taxonomy and selection criteria, metals/alloys, composites/ceramics/hybrid materials, polymers/elastomers/sealants, outgassing/contamination control, radiation/thermal/atomic-oxygen degradation effects, qualification testing and allowables, and lifecycle governance for Q+ATLANTIDE space-system structural and mechanical elements. This subsection is designated **space-materials critical**.

## 2. Scope

- Covers the *Materiales Espaciales* slice of the parent code range `110-119`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`001`–`010`) extend this Overview; the populated set in this baseline is `001`–`010`, indexed in [`README.md`](./README.md).
- Concepts in scope across the subsection:
  - **Space Materials Controlled Definition** (`001`) — normative definition, scope, and applicability per ECSS-Q-ST-70C[^ecssqst70].
  - **Material Families and Selection Criteria** (`002`) — taxonomy of space-qualified material families and selection methodology.
  - **Metals, Alloys and Superalloys** (`003`) — aluminium, titanium, stainless steel, Inconel, and other space-heritage metallic materials.
  - **Composites, Ceramics and Hybrid Materials** (`004`) — CFRP, GFRP, SiC, Al₂O₃, and hybrid sandwich systems.
  - **Polymers, Elastomers and Sealants** (`005`) — Kapton®, PTFE, silicone, polyimide foam, and pressure-seal compounds.
  - **Outgassing, Vacuum and Contamination Control** (`006`) — TML/CVCM limits, vacuum bake-out, and contamination control zones.
  - **Radiation, Thermal Cycling and Atomic Oxygen Effects** (`007`) — degradation mechanisms and design margins for the space environment.
  - **Qualification Testing and Material Allowables** (`008`) — coupon and element test programme; allowables database management.
  - **ECSS / NASA Materials Standards Mapping** (`009`) — normative standards cross-reference for all `111` subsubjects.
  - **Traceability, Evidence and Lifecycle Governance** (`010`) — materials compliance evidence package and lifecycle change authority.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `111` — Materiales Espaciales |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/111_Materiales-Espaciales/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `110-119` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ecssqst70]: **ECSS-Q-ST-70C — Space Product Assurance: Materials, Mechanical Parts and their Data** — European standard for space materials qualification, controlled substances, outgassing, and materials data management.

[^ecssqst7001]: **ECSS-Q-ST-70-01C — Cleanliness and Contamination Control** — European standard for contamination control on spacecraft hardware.

[^nasastd6016]: **NASA-STD-6016A — Standard Materials and Processes Requirements for Spacecraft** — NASA standard governing material selection, prohibited materials, contamination and outgassing requirements.

[^nasarpd7901]: **NASA-RP-1401 — Outgassing Data for Selecting Spacecraft Materials** — NASA reference publication providing outgassing TML and CVCM data for spacecraft material selection.

[^iso11357]: **ISO 11357-1:2023 — Plastics: Differential Scanning Calorimetry (DSC)** — thermal characterisation standard used for polymer and composite material qualification in the space environment.

### Applicable industry standards

- ECSS-Q-ST-70C — Space Product Assurance: Materials, Mechanical Parts and their Data[^ecssqst70]
- ECSS-Q-ST-70-01C — Cleanliness and Contamination Control[^ecssqst7001]
- NASA-STD-6016A — Standard Materials and Processes Requirements for Spacecraft[^nasastd6016]
- NASA-RP-1401 — Outgassing Data for Selecting Spacecraft Materials[^nasarpd7901]
- ISO 11357-1 — Differential Scanning Calorimetry for polymer/composite qualification[^iso11357]
