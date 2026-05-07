---
document_id: QATL-ATLAS-1000-ATLAS-000-009-00-001-README
title: "ATLAS 000-009 · 00.001 — Configuración (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "000-009"
section: "00"
section_title: "Información General y Servicio"
subsection: "001"
subsection_title: "Configuración"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-GROUND, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.1.0
status: active
language: en
---

# ATLAS 000-009 · Section 00 · Subsection 001 — Configuración

## 1. Purpose

Subsection-level index for *Configuración* (`001`) within ATLAS `000-009` — *Información General y Servicio*. This subsection controls the **content and lifecycle of the aircraft's top-level configuration state** — what the aircraft *is* at any given point in time, how that state is baselined, how individual aircraft are differentiated by effectivity, how modifications are tracked, how variants are catalogued, and how change is governed.

*ATLAS describes the aircraft as an integrated system at the top level; this Subject controls how that integrated state evolves over time.*

Boundary: `000_Identificacion/README.md` defines the **identifier** side of configuration (label, code, namespace) at the current index level; `001_Configuracion/` defines the **configuration itself** (content, control, change). This separation is intrinsic to ATLAS as a Schema, not an implementation detail.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

## 2. Scope

- Populates the subsubject namespace `000`–`005` of subsection `001` *Configuración*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- Top-level scope only: baselines, effectivity, modification status, variants and CCB procedures described here refer to the aircraft as a complete system. Subsystem-level equivalents live in their respective Code ranges (`020-029`, `040-049`, `050-059`, `070-079`, etc.) and aggregate upward via the digital thread.

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 001 | Configuration Baseline | [`001_Configuration-Baseline.md`](./001_Configuration-Baseline.md) | active |
| 002 | Effectivity and Applicability | [`002_Effectivity-and-Applicability.md`](./002_Effectivity-and-Applicability.md) | active |
| 003 | Modification Status | [`003_Modification-Status.md`](./003_Modification-Status.md) | active |
| 004 | Variant and Option Catalog | [`004_Variant-and-Option-Catalog.md`](./004_Variant-and-Option-Catalog.md) | active |
| 005 | Configuration Control and Change Management | [`005_Configuration-Control-and-Change-Management.md`](./005_Configuration-Control-and-Change-Management.md) | active |

## 4. Sibling-Subject Pointers

| Sibling Subsection | Relationship |
|---|---|
| [`000_Identificacion/`](../000_Identificacion/) | **Boundary**: `003_Configuration-Identification.md` there holds the *identifier* of configuration; this Subject holds the configuration *content and control*. |
| [`002_Documentacion-General/`](../002_Documentacion-General/) | Configuration baselines are referenced in general documentation structures managed there. |
| [`003_Operaciones-Basicas/`](../003_Operaciones-Basicas/) | Operational procedures reference effectivity codes defined in `002_Effectivity-and-Applicability.md`. |

## 5. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `000-009` |
| Section | `00` — Información General y Servicio |
| Subsection | `001` — Configuración |
| Subsubject namespace | `000`–`005` (active) |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-GROUND, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/000-009_Informacion-General-y-Servicio/001_Configuracion/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-DATAGOV` and `governance_class = baseline` from the parent ATLAS section. Extensions added under `006`–`99` shall preserve those header fields and reuse the footnote set declared here.

## 6. Change Log

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2025-01-01 | Initial reservation; subsection placeholder. |
| 1.1.0 | 2026-05-07 | Populated subsubjects 000–005; activated subsection. |

## 7. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
