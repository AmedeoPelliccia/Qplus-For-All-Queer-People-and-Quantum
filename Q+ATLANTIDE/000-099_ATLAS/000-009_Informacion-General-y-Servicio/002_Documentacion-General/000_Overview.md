---
document_id: QATL-ATLAS-1000-ATLAS-000-009-00-002-000-OVERVIEW
title: "ATLAS 000-009 · 00.002.000 — Documentación General (Overview)"
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
subsection: "002"
subsection_title: "Documentación General"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-GROUND, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 000-009 · 00.002.000 — Documentación General: Overview

## 1. Purpose

Overview entry-point for *Documentación General* (`002`) — the third Subject of the first Code range (`000-009`) of the ATLAS master range (`000–099`).

Doctrinal statement: *ATLAS describes the aircraft as an integrated system at the top level; this Subject defines how that description is published in a controlled manner.*

The publication layer represented by this subsection materialises the content that ATLAS classifies and governs. Without it, architecture decisions remain internal artefacts. With it, those decisions become controlled, auditable, and deliverable technical publications consumed by operators, regulators, and maintainers worldwide.

This subsubject (`000 Overview`) introduces the `002_Documentacion-General` slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4.

## 2. Scope

### 2.1 What this Subject covers

- The **publication set**: the canonical list of technical manuals produced by the programme and their mapping to ATLAS Code ranges and Subjects (→ `001`).
- The **S1000D CSDB infrastructure**: the Common Source DataBase architecture, Data Module Code format, BREX rules, and information-reuse repositories (→ `002`).
- The **Publication Module (PM) assembly**: how Data Modules are assembled into PMs and delivered as commercial manuals (→ `003`).
- The **revision and distribution control**: issue numbering, revision policy, release authority, and regulatory distribution (→ `004`).
- The **language and localization policy**: Simplified Technical English (STE) as authoritative language, translation governance, and the authority hierarchy in case of discrepancy (→ `005`).

### 2.2 Boundary rule

> **This Subject defines the structure of publication; the content published lives in the CSDB referenced from each Code range respectively.**

Each Code range (`020-029`, `040-049`, `060-069`, …) produces its own Data Modules within the CSDB structure defined here. Those DMs are *registered* against the schema defined in `002_S1000D-CSDB-and-Data-Modules.md`; they are **not** stored in this subsection folder.

### 2.3 What is outside scope

- Aircraft system-level descriptions: governed by the respective Code range subjects (`020-029`, `040-049`, etc.).
- Configuration management of the aircraft baseline: governed by `001_Configuracion/` (sibling Subject).
- Aircraft identification, registration, and digital identifiers: governed by `000_Identificacion/` (sibling Subject).
- Operational procedures: governed by `003_Operaciones-Basicas/` (sibling Subject).

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `000-009` |
| Section | `00` — Información General y Servicio |
| Subsection | `002` — Documentación General |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-GROUND, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/000-009_Informacion-General-y-Servicio/002_Documentacion-General/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection index | [`README.md`](./README.md) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `000-009` row (Section `00` — Información General y Servicio, Primary Q-Division Q-DATAGOV).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/). Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^ata2200]: **ATA iSpec 2200 — Information Standards for Aviation Maintenance** — Industry information standard governing structure and exchange of aircraft maintenance data; adopted by this programme as secondary normative reference.

[^ataspec100]: **ATA Spec 100 — Manufacturers' Technical Data** — Legacy ATA specification for manufacturers' technical data, predecessor to iSpec 2200; remains normative for legacy publication formats.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Adopted version for the Q+ATLANTIDE / Q+ programme CSDB. See `002_S1000D-CSDB-and-Data-Modules.md` for version decision rationale.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

[^sub000]: **`000_Identificacion/`** — [`../000_Identificacion/`](../000_Identificacion/). Aircraft and programme identifiers; DMC prefix and ICN namespace authority.

[^sub001]: **`001_Configuracion/`** — [`../001_Configuracion/`](../001_Configuracion/). Configuration baseline and effectivity data consumed by PM applicability filtering.

[^sub003]: **`003_Operaciones-Basicas/`** — [`../003_Operaciones-Basicas/`](../003_Operaciones-Basicas/). Basic operational procedures; DMs assembled and published under the rules defined in this subsection.

### Applicable industry standards

The following standards apply to this subsection:

- ATA iSpec 2200 — Information Standards for Aviation Maintenance[^ata2200]
- ATA Spec 100 — Manufacturers' Technical Data[^ataspec100]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
