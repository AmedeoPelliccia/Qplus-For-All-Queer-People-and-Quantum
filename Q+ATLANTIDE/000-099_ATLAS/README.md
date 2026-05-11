---
document_id: QATL-ATLAS1000-ATLAS-README
title: "000–099 ATLAS — Aircraft Top Level Architecture Schema/System"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../organization/Q+ATLANTIDE.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
architecture_term:
  controlled_term: true
  expansion: "Aircraft Top Level Architecture Schema/System"
  domain: "Q+ATLANTIDE / Q+ATLANTIDE1000"
  master_range: "000-099"
  meaning: >
    Controlled architecture layer for aircraft top-level classification,
    identification, system mapping, technical documentation alignment,
    and lifecycle-governed aerospace configuration structure.
  usage_note:
    Schema: "Use when referring to taxonomy, data model, classification, or repository structure."
    System: "Use when referring to operational architecture, governance, interfaces, and lifecycle control."
master_range: "000–099"
subrange_count: 10
governance_class: baseline
structural_interface_rule: N-005
primary_q_divisions: [Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-HORIZON, Q-MECHANICS, Q-STRUCTURES]
orb_function_support: [ORB-FIN, ORB-LEG, ORB-MKTG, ORB-PMO]
version: 1.0.0
status: active
language: en
---

# 000–099 ATLAS — Aircraft Top Level Architecture Schema/System

## 1. Purpose

Aircraft top-level architecture band covering identification, ground handling, core aircraft systems, mechanical protection, avionics & APU, primary structures, traditional and alternative propulsion, and aircraft-type expansion.

This folder is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. Bands classify technologies, Q-Divisions provide technical authority, and ORB-Functions provide enterprise support[^n002].

## 2. Glossary of Terms & Acronyms

| Term / Acronym | Expansion | Meaning in this band |
|---|---|---|
| ATLAS | Aircraft Top Level Architecture **Schema/System** (controlled term) | Aircraft architecture band `000-099`. *Schema* — taxonomy, data model, classification, or repository structure; *System* — operational architecture, governance, interfaces, and lifecycle control. |
| APU | Auxiliary Power Unit | Onboard auxiliary power generator. |
| BWB | Blended Wing Body | Aircraft configuration family. |
| CMS | Central Maintenance System | Onboard maintenance computing function. |
| ECS | Environmental Control System | Cabin air conditioning and pressurisation. |
| GSE | Ground Support Equipment | Ground operations and maintenance support. |
| HVDC | High Voltage Direct Current | Electrical distribution and propulsion systems. |
| IMA | Integrated Modular Avionics | Aircraft avionics architecture. |
| LH₂ | Liquid Hydrogen | Cryogenic hydrogen fuel / energy carrier. |
| WTW | Wide Tube and Wing | Aircraft configuration family. |
| Q+ATLANTIDE | Controlled baseline for the `000-999` architecture-band taxonomy. | Parent baseline of this register. |
| ATLAS-1000 | Umbrella register of the 10 architectures inside Q+ATLANTIDE. | Subpart of Q+ATLANTIDE; not a numeric band. |
| Q-Division | Technical authority unit (e.g. Q-AIR, Q-DATAGOV, Q-HPC). | Owns architecture decisions inside a band (rule N-002). |
| ORB | Organizational Resource Backbone — enterprise support functions. | Provides enterprise-side support to bands (rule N-002). |
| CSDB | Common Source DataBase | S1000D technical-publication data environment. |
| LC | Lifecycle phase / acceptance gate | Used across SSOT/LC01–LC14. |

Cross-reference the full Q+ATLANTIDE acronym set at [`organization/Q+ATLANTIDE.md` §2](../../organization/Q+ATLANTIDE.md#2-acronyms)[^glossary].

## 3. Architecture Table

Sub-ranges within this band, sourced from the Q+ATLANTIDE controlled baseline[^baseline] §3 *Consolidated Architecture Table*[^table].

| Code range | Section | Section title | Subject | Subject title | Primary focus | Primary Q-Division | Support Q-Divisions | ORB support |
|---:|---:|---|---:|---|---|---|---|---|
| 000–009 | 00 | Información General y Servicio | 00 | General Information | Identificación, configuración, documentación general, operaciones básicas | Q-DATAGOV | Q-GROUND, Q-AIR | ORB-PMO, ORB-LEG |
| 010–019 | 01 | Manejo en Tierra & Servicio | 00 | General Information | Ground handling, servicing, acceso, remolque, parking, GSE | Q-GROUND | Q-MECHANICS, Q-INDUSTRY | ORB-PMO, ORB-FIN |
| 020–029 | 02 | Sistemas Core de Aeronave | 00 | General Information | Aviónica base, eléctrica, hidráulica, ECS, fuel, flight control | Q-AIR | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH | ORB-PMO, ORB-LEG |
| 030–039 | 03 | Protección & Sistemas Mecánicos | 00 | General Information | Ice/rain protection, fire protection, tren, actuadores | Q-MECHANICS | Q-AIR, Q-STRUCTURES | ORB-PMO, ORB-LEG |
| 040–049 | 04 | Aviónica, Información & APU | 00 | General Information | IMA, redes de datos, CMS, APU, onboard information systems | Q-DATAGOV | Q-AIR, Q-SPACE, Q-HPC | ORB-PMO, ORB-LEG |
| 050–059 | 05 | Estructuras | 00 | General Information | Compartimentos de carga, prácticas estándar estructurales, puertas, fuselaje, nacelles y pilones, estabilizadores, ventanas y alas | Q-STRUCTURES | Q-AIR, Q-INDUSTRY, Q-HPC | ORB-PMO, ORB-FIN, ORB-LEG |
| 060–069 | 06 | Propulsión Tradicional | 00 | General Information | Turbofan, nacelles, thrust reversers, engine installation, fire zones | Q-GREENTECH | Q-MECHANICS, Q-AIR, Q-INDUSTRY | ORB-PMO, ORB-FIN |
| 070–079 | 07 | Propulsión Eco-Tech e Híbrido-Eléctrica | 00 | General Information | Hybrid-electric propulsion, thermal management, power conversion, battery-assisted propulsion | Q-GREENTECH | Q-HPC, Q-MECHANICS, Q-AIR, Q-INDUSTRY | ORB-PMO, ORB-FIN, ORB-CSR |
| 080–089 | 08 | Propulsión Alternativa & Cuántica | 00 | General Information | LH₂, fuel cells, HVDC, superconductores, Q-sensing | Q-GREENTECH | Q-HORIZON, Q-HPC, Q-STRUCTURES | ORB-PMO, ORB-LEG, ORB-FIN |
| 090–099 | 09 | Tipos Específicos & Expansión | 00 | General Information | Variantes BWB/WTW, demostradores, clases especiales de aeronaves | Q-HORIZON | Q-AIR, Q-STRUCTURES, Q-GREENTECH | ORB-PMO, ORB-MKTG |

## 4. Interfaces Diagram

```mermaid
flowchart TB
    BASELINE["Q+ATLANTIDE baseline<br/>(controlled `000-999` taxonomy)"]:::baseline
    ATLAS["ATLAS-1000 register<br/>master range `000–099`"]:::register
    BASELINE --> ATLAS

    subgraph SECTIONS["ATLAS sections (10 sub-ranges)"]
        direction LR
        S00["00 · 000-009<br/>Información General y Servicio"]:::sec
        S01["01 · 010-019<br/>Manejo en Tierra & Servicio"]:::sec
        S02["02 · 020-029<br/>Sistemas Core de Aeronave"]:::sec
        S03["03 · 030-039<br/>Protección & Sist. Mecánicos"]:::sec
        S04["04 · 040-049<br/>Aviónica, Información & APU"]:::sec
        S05["05 · 050-059<br/>Estructuras"]:::sec
        S06["06 · 060-069<br/>Propulsión Tradicional"]:::sec
        S07["07 · 070-079<br/>Propulsión Eco-Tech & Híbrido-Eléctrica"]:::sec
        S08["08 · 080-089<br/>Propulsión Alternativa & Cuántica"]:::sec
        S09["09 · 090-099<br/>Tipos Específicos & Expansión"]:::sec
    end
    ATLAS --> SECTIONS

    subgraph QDIV["Q-Divisions — technical authority (rule N-002)"]
        direction LR
        QAIR[Q-AIR]:::qdiv
        QDATA[Q-DATAGOV]:::qdiv
        QGND[Q-GROUND]:::qdiv
        QMECH[Q-MECHANICS]:::qdiv
        QSTR[Q-STRUCTURES]:::qdiv
        QGT[Q-GREENTECH]:::qdiv
        QHOR[Q-HORIZON]:::qdiv
    end

    subgraph ORB["ORB-Functions — enterprise support (rule N-002)"]
        direction LR
        OPMO[ORB-PMO]:::orb
        OFIN[ORB-FIN]:::orb
        OLEG[ORB-LEG]:::orb
        OMKTG[ORB-MKTG]:::orb
        OCSR[ORB-CSR]:::orb
    end

    %% Primary Q-Division ownership per section
    S00 --> QDATA
    S01 --> QGND
    S02 --> QAIR
    S03 --> QMECH
    S04 --> QDATA
    S05 --> QSTR
    S06 --> QGT
    S07 --> QGT
    S08 --> QGT
    S09 --> QHOR

    %% ORB enterprise support (every section is PMO-supported)
    SECTIONS -.-> ORB

    %% Notable cross-section interfaces (rule N-005, structural & energy)
    S05 -. "structural interfaces<br/>(rule N-005)" .- S02
    S05 -. structural .- S06
    S05 -. structural .- S07
    S05 -. structural .- S09
    S02 -. "ATA 28 ↔ LH₂" .- S07
    S07 -. "H₂ / fuel cell" .- S08
    S04 -. "AI/ML hooks" .- S08

    classDef baseline fill:#1f3a93,stroke:#0b1d4a,color:#fff,stroke-width:2px
    classDef register fill:#2c82c9,stroke:#0b1d4a,color:#fff
    classDef sec fill:#eaf3fb,stroke:#2c82c9,color:#0b1d4a
    classDef qdiv fill:#f6e6ff,stroke:#7d3c98,color:#3b1f4d
    classDef orb fill:#fff4dd,stroke:#b9770e,color:#5a3b00
```

*Solid arrows denote primary Q-Division ownership (rule N-002); dotted arrows denote notable cross-section technical interfaces (e.g. structural interfaces from §05 per rule N-005, fuel/energy continuity from ATA 28 to H₂ storage in §07–§08, and AI/ML hooks from §04 to §08).*

## 5. Footprint

| Metric | Value |
|---|---|
| Master range | `000–099` |
| Sub-ranges | 10 |
| Architecture code | `ATLAS` |
| Governance class | `baseline` |
| Restricted band | No |
| Primary Q-Divisions | Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-HORIZON, Q-MECHANICS, Q-STRUCTURES |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/` |
| Documents | `README.md` (this file) + 10 section `README.md` indexes (one per `0X0-0X9` sub-range) |
| Subsections | 86 populated under the 10 section indexes |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md) |
| Register subpart | ATLAS-1000 |
| Structural-interface rule | Sub-range `050–059` covers structural elements of the aircraft (rule N-005[^n005]). |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md)[^baseline]. Templates declared in this band must populate `architecture_band`, `architecture_code = ATLAS`, `q_division_owner` and `orb_function_support` per the Templates System[^templates]. The No-AAA Rule[^n004] applies.

## 6. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^table]: **§3 — Consolidated Architecture Table** — [`organization/Q+ATLANTIDE.md` §3](../../organization/Q+ATLANTIDE.md#3-consolidated-architecture-table).

[^glossary]: **§2 — Acronyms** — [`organization/Q+ATLANTIDE.md` §2](../../organization/Q+ATLANTIDE.md#2-acronyms).

[^templates]: **§5 — Templates System** — [`organization/Q+ATLANTIDE.md` §5](../../organization/Q+ATLANTIDE.md#5-templates-system). Mandatory template header fields, naming rules and lifecycle integration.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n002]: **Note N-002** — Architecture bands classify technologies; Q-Divisions provide technical authority; ORB-Functions provide enterprise support. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n003]: **Note N-003** — The `000-999` range is controlled; `ATLAS-1000` is the umbrella name, not an additional numeric band. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n005]: **Note N-005** — `ATLAS 050–059` covers structural elements (Estructuras). See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^repo]: **Repository root README** — [`README.md`](../../README.md). Top-level entry point referencing the Q+ATLANTIDE baseline and the ATLAS-1000 register subpart.
