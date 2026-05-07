---
document_id: QATL-ATLAS-1000-STA-110-119-01-111-008-QUALIFICATION-TESTING-AND-MATERIAL-ALLOWABLES
title: "STA 110-119 · 01.111.008 — Qualification Testing and Material Allowables"
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
subsubject: "008"
subsubject_title: "Qualification Testing and Material Allowables"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 110-119 · Section 01 · Subsection 111 · Subsubject 008 — Qualification Testing and Material Allowables

## 1. Purpose

Defines the **material qualification test programme, allowables derivation methodology, and materials database management** for Q+ATLANTIDE STA-band materials — establishing the evidence basis for all structural and mechanical material applications, per ECSS-Q-ST-70C[^ecssqst70] and NASA-STD-6016A[^nasastd6016].

## 2. Scope

- Covers the *Qualification Testing and Material Allowables* subsubject (`008`) of subsection `111`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Material qualification programme** — qualification test plan (QTP) scope: coupon-level static testing, fatigue, fracture toughness, outgassing, radiation exposure, thermal cycling; witness sample retention; DRD documentation format.
  - **Statistical basis** — A-basis (99th percentile at 95% confidence, ≥ 100 samples) for primary structure; B-basis (90th percentile at 95% confidence, ≥ 30 samples) for secondary structure; S-basis (specification minimum) for standard off-the-shelf materials with heritage per MMPDS-19.
  - **Environmental conditioning** — humidity soak, thermal extremes, vacuum conditioning prior to mechanical testing to simulate in-orbit material state; ASTM D5229 (moisture), ASTM D3039 (CFRP tension), ASTM D7137 (CFRP compression after impact).
  - **Material allowables database** — Q+ATLANTIDE STA-band controlled database of A-/B-basis mechanical properties vs. temperature; version-controlled; change authority: Q-STRUCTURES sign-off; linked to structural analysis tools used by `110`.
  - **Batch conformance testing** — flight production batch verification tests: incoming inspection (hardness, conductivity, CMM for dimensions), reduced mechanical test matrix per ECSS-Q-ST-70C[^ecssqst70] Annex F.
  - **Non-conformance** — NCR (non-conformance report) protocol for out-of-specification material; accept-as-is waiver requires engineering justification + Q-STRUCTURES authority sign-off.

## 3. Diagram — Material Qualification and Allowables Flow

```mermaid
flowchart TB
    MATPROP["Material Properties<br/>(vendor datasheet)"]
    MATPROP --> QTP["Qualification Test Plan<br/>(coupon · fatigue · fracture)"]
    QTP --> ENV["Environmental Conditioning<br/>(humidity · thermal · vacuum)"]
    ENV --> TEST["Mechanical Testing<br/>(ASTM D3039 · D7137 · …)"]
    TEST --> STAT["Statistical Analysis<br/>(A-basis / B-basis per MMPDS-19)"]
    STAT --> DB["Material Allowables Database<br/>(Q+ATLANTIDE STA-band)"]
    DB --> STRUCT["110 Structural Analysis<br/>(margin calculations)"]
    DB --> BATCH["Batch Conformance<br/>(incoming inspection)"]

    style DB fill:#1f3a93,color:#fff
    style STAT fill:#2c82c9,color:#fff
```

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `110-119` |
| Section | `01` — Estructuras y Materiales Espaciales |
| Subsection | `111` — Materiales Espaciales |
| Subsubject | `008` — Qualification Testing and Material Allowables |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/110-119_Estructuras-y-Materiales-Espaciales/111_Materiales-Espaciales/` |
| Document | `008_Qualification-Testing-and-Material-Allowables.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

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
