---
document_id: QATL-ATLAS-1000-ATLAS-070-079-07-README
title: "ATLAS 070-079 · 07 — Propulsión Eco-Tech e Híbrido-Eléctrica (Section Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "070-079"
section: "07"
section_title: "Propulsión Eco-Tech e Híbrido-Eléctrica"
section_title_en: "Eco-Tech & Hybrid-Electric Propulsion"
primary_q_division: Q-GREENTECH
support_q_divisions: [Q-HPC, Q-MECHANICS, Q-AIR, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-CSR]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 070-079 · Section 07 — Propulsión Eco-Tech e Híbrido-Eléctrica

## 1. Purpose

Section-level index for *Propulsión Eco-Tech e Híbrido-Eléctrica* (`070-079`) within the ATLAS band. Arquitectura híbrido-eléctrica, motores y drives eléctricos, almacenamiento, distribución MV/HV, gestión térmica, fuel cells, hidrógeno, SAF y EMS.

This section is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. Bands classify technologies, Q-Divisions provide technical authority and ORB-Functions provide enterprise support[^n002].

## 2. Scope

- Aggregates the subsections within the `070-079` code range listed in §3.
- Inherits Q-Division authority and ORB support from the parent row in [`../README.md` §3](../README.md#3-architecture-table)[^archtable].
- Each subsection folder contains its own `README.md` (subsection index) and may contain Overview and subsubject documents.

## 3. Subsection Index

| Code | Title | Folder | Status |
|---:|---|---|---|
| `070` | Hybrid-Electric Architecture Overview | [`070_Hybrid-Electric-Architecture-Overview/`](./070_Hybrid-Electric-Architecture-Overview/) | active |
| `071` | Electric Motor and Drive Systems | [`071_Electric-Motor-and-Drive-Systems/`](./071_Electric-Motor-and-Drive-Systems/) | active |
| `072` | Battery Energy Storage | [`072_Battery-Energy-Storage/`](./072_Battery-Energy-Storage/) | active |
| `073` | Power Distribution — MV/HV | [`073_Power-Distribution-MV-HV/`](./073_Power-Distribution-MV-HV/) | active |
| `074` | Thermal Management — Hybrid | [`074_Thermal-Management-Hybrid/`](./074_Thermal-Management-Hybrid/) | active |
| `075` | Fuel Cell Integration | [`075_Fuel-Cell-Integration/`](./075_Fuel-Cell-Integration/) | active |
| `076` | Hydrogen Fuel Storage — Onboard | [`076_Hydrogen-Fuel-Storage-Onboard/`](./076_Hydrogen-Fuel-Storage-Onboard/) | active |
| `077` | Hydrogen Distribution and Conditioning | [`077_Hydrogen-Distribution-and-Conditioning/`](./077_Hydrogen-Distribution-and-Conditioning/) | active |
| `078` | SAF and Drop-In Compatibility | [`078_SAF-and-Drop-In-Compatibility/`](./078_SAF-and-Drop-In-Compatibility/) | active |
| `079` | Energy Management System | [`079_Energy-Management-System/`](./079_Energy-Management-System/) | active |

## 4. Interfaces Diagram

```mermaid
flowchart TB
    PARENT["ATLAS-1000<br/>(`000–099` master range)"]:::parent
    SEC["Section 07 · 070-079<br/>Propulsión Eco-Tech e Híbrido-Eléctrica"]:::sec
    PARENT --> SEC

    subgraph SUBS["Subsections"]
        direction LR
        SUB_070["070 — Hybrid-Electric Architecture Overview"]:::sub
        SUB_071["071 — Electric Motor & Drive Systems"]:::sub
        SUB_072["072 — Battery Energy Storage"]:::sub
        SUB_073["073 — Power Distribution MV/HV"]:::sub
        SUB_074["074 — Thermal Management — Hybrid"]:::sub
        SUB_075["075 — Fuel Cell Integration"]:::sub
        SUB_076["076 — Hydrogen Fuel Storage — Onboard"]:::sub
        SUB_077["077 — Hydrogen Distribution & Conditioning"]:::sub
        SUB_078["078 — SAF & Drop-In Compatibility"]:::sub
        SUB_079["079 — Energy Management System"]:::sub
    end
    SEC --> SUBS

    QPRIM["Q-GREENTECH<br/>(primary Q-Division)"]:::qdiv
    QSUPP["Q-HPC, Q-MECHANICS, Q-AIR, Q-INDUSTRY<br/>(support Q-Divisions)"]:::qdiv
    ORB["ORB-PMO, ORB-FIN, ORB-CSR<br/>(ORB support)"]:::orb

    SEC --> QPRIM
    SEC -.-> QSUPP
    SEC -.-> ORB

    SUBS --> SUB_070
    SUBS --> SUB_071
    SUBS --> SUB_072
    SUBS --> SUB_073
    SUBS --> SUB_074
    SUBS --> SUB_075
    SUBS --> SUB_076
    SUBS --> SUB_077
    SUBS --> SUB_078
    SUBS --> SUB_079
    EXT_S02["§02 · Fuel & Energy Storage (027)"]:::ext
    EXT_S08["§08 · Quantum Sensing (080)"]:::ext
    SUB_076 -. "ATA 28 LH₂ cross-ref" .- EXT_S02
    SUB_079 -. "EMS telemetry" .- EXT_S08

    classDef parent fill:#1f3a93,stroke:#0b1d4a,color:#fff
    classDef sec fill:#2c82c9,stroke:#0b1d4a,color:#fff
    classDef sub fill:#eaf3fb,stroke:#2c82c9,color:#0b1d4a
    classDef qdiv fill:#f6e6ff,stroke:#7d3c98,color:#3b1f4d
    classDef orb fill:#fff4dd,stroke:#b9770e,color:#5a3b00
    classDef ext fill:#fdebd0,stroke:#b9770e,color:#5a3b00,stroke-dasharray:3 3
```

*Solid arrows show parent→section→subsection ownership and primary Q-Division authority; dotted arrows show support Q-Divisions, ORB enterprise support, and notable cross-section interfaces.*

## 5. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `070-079` |
| Section | `07` — Propulsión Eco-Tech e Híbrido-Eléctrica |
| Subsections | 10 populated |
| Primary Q-Division | Q-GREENTECH[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-MECHANICS, Q-AIR, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN, ORB-CSR |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/070-079_Propulsion-Eco-Tech-e-Hibrido-Electrica/` |
| Document | `README.md` (this file) |
| Parent architecture | [`../README.md`](../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsections under this section inherit `architecture_code = ATLAS`, `primary_q_division = Q-GREENTECH` and `governance_class = baseline` from this section header. Templates declared in this section must populate `architecture_band`, `architecture_code = ATLAS`, `q_division_owner` and `orb_function_support` per the Templates System[^templates]. The No-AAA Rule[^n004] applies.

## 6. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Architecture Table (parent)** — [`../README.md` §3](../README.md#3-architecture-table). Source of authority for primary/support Q-Divisions and ORB support of this section.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^templates]: **§5 — Templates System** — [`organization/Q+ATLANTIDE.md` §5](../../../organization/Q+ATLANTIDE.md#5-templates-system).

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../organization/Q+ATLANTIDE.md#4-notes).

[^n002]: **Note N-002** — Architecture bands classify technologies; Q-Divisions provide technical authority; ORB-Functions provide enterprise support. See [`organization/Q+ATLANTIDE.md` §4](../../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../../organization/Q+ATLANTIDE.md#4-notes).
