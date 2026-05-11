---
document_id: QATL-ATLAS-1000-STA-100-109-00-102-010-ECLSS-CONTROLLED-DEFINITION
title: "STA 100-109 · 102-010 — ECLSS Controlled Definition"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "100-109"
section: "00"
section_title: "Sistemas Generales y Soporte Vital Espacial"
subsection: "102"
subsection_title: "Soporte Vital ECLSS"
subsubject: "010"
subsubject_title: "ECLSS Controlled Definition"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 100-109 · 102-010 — ECLSS Controlled Definition

## 1. Purpose

Establishes the **normative definition and controlled acronym** for the Environmental Control and Life Support System (ECLSS) within the Q+ATLANTIDE STA band, defining the applicability limits, key terms, and regulatory references per ECSS-E-ST-34C[^ecsse34] and NASA/JSC-65591[^nasajsc].

## 2. Scope

- Covers the *ECLSS Controlled Definition* subsubject (`001`) of subsection `102`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Controlled acronym** — ECLSS = *Environmental Control and Life Support System*; the unique STA `102` designation for the life-support function.
  - **System scope** — ECLSS encompasses atmospheric management, water recovery, waste management, and thermal/humidity control functions; it does not cover propulsion, power, or structural systems.
  - **Applicability** — crewed missions (ISS-class LEO, Gateway cis-lunar, lunar surface, interplanetary transit) under STA authority.
  - **Controlled vocabulary** — *atmosphere revitalization*, *pressure control*, *water recovery system (WRS)*, *urine processor assembly (UPA)*, *trace contaminant control (TCC)*, *condensate collection*, *sabatier reaction*.
  - **Relationship to Habitabilidad** — ECLSS is the supply function; Habitabilidad (`101`) is the demand function; interfaces declared in `101.008`.
  - **Safety classification** — ECLSS is classified life-support critical; all subsystems require redundancy, FDIR, and explicit assurance per ECSS-Q-ST-40C.

## 3. Diagram — ECLSS Controlled Definition Framework

```mermaid
flowchart TD
    A["ECSS-E-ST-34C · NASA/JSC-65591<br/>Regulatory Anchors"]
    A --> B["ECLSS Controlled Definition<br/>(001 — this document)"]
    B --> C["System Scope<br/>(atm · water · waste · thermal)"]
    B --> D["Controlled Vocabulary<br/>(WRS · UPA · CDRA · TCC)"]
    C --> E["002 — Atm Generation"]
    C --> F["006 — Water Recovery"]
    C --> G["007 — Waste Management"]
    D --> H["101.008 — Habitabilidad Interface"]
    style B fill:#2c82c9,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `102` — Soporte Vital ECLSS |
| Subsubject | `001` — ECLSS Controlled Definition |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/102_Soporte-Vital-ECLSS/` |
| Document | `102-010-ECLSS-Controlled-Definition.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`102-000-General.md`](./102-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `100-109` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ecsse34]: **ECSS-E-ST-34C Rev.1 — Space Engineering: Environmental Control and Life Support** — European standard for ECLSS design, subsystem interfaces, and test criteria.

[^nasajsc]: **NASA/JSC-65591 — ECLSS Design and Performance Requirements** — NASA design specification for ISS-class ECLSS subsystems, used as the baseline engineering reference.

[^nastd3001v2]: **NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health** — Atmosphere and water quality requirements that ECLSS must satisfy.

[^iso14644]: **ISO 14644-1:2015 — Cleanrooms and Associated Controlled Environments** — Applied to atmosphere quality monitoring and contamination control requirements.

[^nasacp]: **NASA/CP-2008-214304 — ECLSS Development and Testing** — ECLSS hardware development and qualification test reference covering all subsystems.

### Applicable industry standards

- ECSS-E-ST-34C Rev.1 — Space Engineering: Environmental Control and Life Support[^ecsse34]
- NASA/JSC-65591 — ECLSS Design and Performance Requirements[^nasajsc]
- NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health[^nastd3001v2]
- ISO 14644-1:2015 — Cleanrooms and Associated Controlled Environments[^iso14644]
- NASA/CP-2008-214304 — ECLSS Development and Testing[^nasacp]
