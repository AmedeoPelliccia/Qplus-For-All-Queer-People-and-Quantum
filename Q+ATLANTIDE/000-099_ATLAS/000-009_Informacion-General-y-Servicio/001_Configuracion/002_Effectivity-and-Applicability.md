---
document_id: QATL-ATLAS-1000-ATLAS-000-009-00-001-002-EFFECTIVITY-AND-APPLICABILITY
title: "ATLAS 000-009 · 00.001.002 — Effectivity and Applicability"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "000-009"
section: "00"
section_title: "Información General y Servicio"
subsection: "001"
subsection_title: "Configuración"
subsubject: "002"
subsubject_title: "Effectivity and Applicability"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-GROUND, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 000-009 · 00.001.002 — Effectivity and Applicability

## 1. Purpose

Defines the **effectivity and applicability framework** for ATLAS top-level configuration. This is the mechanism by which the ATLAS schema top-level filters which subsystems from which Master ranges apply to which individual aircraft.

*Effectivity is where ATLAS stops being a static schema and becomes a dynamic system.* Without effectivity defined here, downstream Code ranges (`020-029`, `040-049`, `070-079`, etc.) cannot correctly filter their contents by individual aircraft; contributors would reinvent applicability logic locally, producing inconsistent filtering behaviour across publications.

This subsubject is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

### 2.1 Doctrinal Role

Effectivity is the controlled attribute set that maps an abstract configuration (as described in the ATLAS schema) to a specific aircraft individual (identified by MSN) or a set of aircraft (identified by a range, modification status, or operator condition). The mapping is authoritative; all downstream CSDB publications shall resolve applicability by reference to this document, not by local reinvention.

### 2.2 S1000D Applicability Tables

The AMPEL360 CSDB shall implement the following S1000D applicability constructs[^s1000d]:

#### Applicability Cross-Reference Table (ACT)

The ACT maps property identifiers to their controlled values. AMPEL360 top-level ACT properties:

| `applicPropertyIdent` | Type | Description | Example Values |
|---|---|---|---|
| `product` | string | Aircraft product family | `AMPEL360` |
| `variant` | string | Variant designator (see `004_Variant-and-Option-Catalog.md`) | `BWB-Q100`, `BWB-Q250`, `BWB-e`, `Q300-MRTT`, `City`, `SkyCleaner`, `BWB-H2` |
| `msn` | string / range | Manufacturer Serial Number | `0001`, `0001-0050`, `0051-` |
| `modStatus` | string | Modification status code | `PRE-SB-001`, `POST-SB-001`, `STD` |
| `operator` | string | Operator ICAO code | `IBE`, `AAL`, `* (any)` |
| `environment` | string | Operational environment | `CIVIL`, `MILITARY`, `DEMO` |
| `lutState` | string | Logical unit test state | `RELEASE`, `DEV` |
| `lcPhase` | string | Lifecycle phase | `PRODUCTION`, `DELIVERY`, `MAINTENANCE`, `RETIREMENT` |
| `optAxis` | string | Option axis (cabin, mission kit) | `PAX-180`, `MRTT-BASIC`, `FREIGHTER` |

#### Product Cross-Reference Table (PCT)

The PCT maps each MSN (or MSN range) to its variant, initial modification status, operator and option axis. The PCT is the source of truth for "which physical aircraft maps to which configuration at delivery". PCT is maintained in PLM and exported to CSDB at each baseline release.

| MSN Range | Variant | Initial `modStatus` | Operator | `optAxis` |
|---|---|---|---|---|
| 0001–0010 | `BWB-Q100` | `STD` | `*` | `PAX-180` |
| 0011–0020 | `BWB-Q250` | `STD` | `*` | `PAX-280` |
| 0021–0025 | `BWB-H2` | `DEMO` | `*` | `DEMO-H2` |
| *(subsequent blocks defined at each baseline release)* | | | | |

#### Conditions Cross-Reference Table (CCT)

The CCT defines compound applicability conditions combining ACT properties using `AND`/`OR`/`NOT` logic. CCT conditions are used in CSDB data modules to apply conditional filtering:

| Condition ID | Expression | Meaning |
|---|---|---|
| `COND-CIVIL-PAX` | `product=AMPEL360 AND environment=CIVIL AND optAxis=PAX-*` | All civil passenger configurations |
| `COND-MRTT` | `variant=Q300-MRTT AND environment=MILITARY` | MRTT variant in military environment |
| `COND-POST-SB-001` | `modStatus=POST-SB-001` | Any aircraft embodying SB-001 |
| `COND-DEMO` | `environment=DEMO` | Demonstrator aircraft only |

### 2.3 Effectivity Code Mapping (ATA → S1000D)

For backwards compatibility with ATA iSpec 2200[^ata2200] tools used by operators:

| ATA Effectivity Concept | S1000D Equivalent | Notes |
|---|---|---|
| Effectivity code (e.g. `EFF-001`) | ACT `applicPropertyIdent` + value set | CSDB maps ATA codes to ACT property expressions |
| Aircraft model applicability | `variant` property in ACT | AMPEL360 variant designators are controlled in `004_Variant-and-Option-Catalog.md` |
| MSN range (e.g. `001-050`) | `msn` property range in PCT | Inclusive ranges in PCT |
| Modification effectivity | `modStatus` property in ACT | Pre/post-SB status tracked in `003_Modification-Status.md` |
| Fleet-wide effectivity | `operator=*` in CCT | Wildcard match in CCT expression |

### 2.4 Resolution: Publication Time vs. Operation Time

Applicability can be resolved at two points:

| Resolution Point | Definition | AMPEL360 Practice |
|---|---|---|
| **Publication time** | Filtering applied when CSDB data modules are assembled into a publication (AMM, CMM, etc.) | Used for aircraft-specific paper/PDF publications; resolved against PCT snapshot |
| **Operation time** | Filtering applied at runtime by an Interactive Electronic Technical Publication (IETP) system using live aircraft data | Used for digital IETP delivery; IETP queries `lcPhase` and `modStatus` from aircraft digital twin (`300-399_DTCEC/`) |

AMPEL360 shall support both modes. The authoritative effectivity data source is the PCT (publication time) or the digital twin configuration state (operation time). Both must remain synchronised; the synchronisation procedure is defined in `005_Configuration-Control-and-Change-Management.md`.

### 2.5 Governance Rule

The ACT, PCT and CCT defined in this document are the **single authoritative source** for applicability across all AMPEL360 CSDB publications. Downstream Code ranges (`020-029`, `040-049`, `050-059`, `070-079`, `080-089`) shall reference this document and shall not define independent applicability schemas. If a downstream range requires additional properties, a change request shall be submitted to Q-DATAGOV to extend the ACT here.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `000-009` |
| Section | `00` — Información General y Servicio |
| Subsection | `001` — Configuración |
| Subsubject | `002` — Effectivity and Applicability |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-GROUND, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/000-009_Informacion-General-y-Servicio/001_Configuracion/` |
| Document | `002_Effectivity-and-Applicability.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Cross-ref: S1000D CSDB | `OPT-INS_FRAMEWORK/I-INFRASTRUCTURES/.../CSDB/APPLICABILITY/` |
| Cross-ref: variant list | [`004_Variant-and-Option-Catalog.md`](./004_Variant-and-Option-Catalog.md) |
| Cross-ref: modification status | [`003_Modification-Status.md`](./003_Modification-Status.md) |
| Cross-ref: digital twin | `Q+ATLANTIDE/300-399_DTCEC/` |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ata2200]: **ATA iSpec 2200** — Airlines Electronic Engineering Committee (AEEC) specification for aircraft information management; defines effectivity codes and publication structures.

[^ataspec100]: **ATA Spec 100** — Historical ATA chapter numbering standard; predecessor to iSpec 2200.

[^s1000d]: **S1000D** — International specification for technical publications; Issue 5.0+. Defines CSDB architecture, ACT (Applicability Cross-reference Table), PCT (Product Cross-reference Table), CCT (Conditions Cross-reference Table) and applicability expression language.

[^as9100d]: **AS9100D** — Quality management system standard for the aviation, space and defence industry.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
