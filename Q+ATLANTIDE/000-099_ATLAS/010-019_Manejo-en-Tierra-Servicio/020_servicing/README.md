---
document_id: QATL-ATLAS-1000-ATLAS-010-019-01-020-README
title: "ATLAS 010-019 · 01.020 — servicing (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top-Level Architecture System"
master_range: "000–099"
code_range: "010-019"
section: "01"
section_title: "Manejo en Tierra & Servicio"
subject: "00"
subject_title: "General Information"
subsection: "020"
subsection_title: "servicing"
primary_q_division: Q-GROUND
support_q_divisions: [Q-MECHANICS, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# ATLAS 010-019 · Section 01 · Subsection 020 — servicing

## 1. Purpose

Subsection-level index for *servicing* (`020`) within ATLAS `010-019` — *Manejo en Tierra & Servicio*. Aggregates the `010 Overview` and the detailed subsubjects (`011`–`015`) that extend it with the canonical scope/boundary clauses, replenishment regimes (fluids/gases/energy, including LH₂/N₂ for AMPEL360), scheduled/unscheduled servicing logic, servicing-point/coupling/interface specifications and the records & traceability semantics, in conformance with the controlled Q+ATLANTIDE baseline[^baseline] and S1000D Issue 6.0[^s1000d]. Maps cleanly to **ATA 12 — Servicing**[^ata12] with infrastructure overlay to `OPT-INS_FRAMEWORK/I-INFRASTRUCTURES/ATA_12-SERVICING_INFRA/`; the H₂ overlay for couplings/hoses is consumed (read-only) from `OPT-INS_FRAMEWORK/I-INFRASTRUCTURES/ATA_IN_H2_GSE_AND_SUPPLY_CHAIN/IN-50-h2-gse-couplings-hoses-interfaces/`.

## 2. Scope

- Covers the full subsubject namespace `010`–`019` of subsection `020` *servicing*; subsubjects `011`–`015` are populated in this baseline release, the remaining `016`–`019` slots remain available for future extension per the Overview's authorisation[^archtable].
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- **Boundary with subsection `010` *Ground handling*.** Restated for navigation: [`../010_Ground-handling/014_Ground-Support-Equipment-Interfaces.md`](../010_Ground-handling/014_Ground-Support-Equipment-Interfaces.md) defines the *physical/positioning* GSE surface; [`./014_Servicing-Points-Couplings-and-Interfaces.md`](./014_Servicing-Points-Couplings-and-Interfaces.md) defines the *functional* servicing surface (what flows, at what rate, under what protocol).

## 3. Diagram

The diagram below shows how this subsection's `010 Overview` aggregates the populated subsubjects (`011`–`015`) into the *servicing* slice of ATLAS `010-019`.

```mermaid
flowchart LR
    R[(Subsection 020\nservicing)]
    OV[010 Overview] --> R
    R --> N01[011 — Scope & Servicing Boundaries]
    R --> N02[012 — Replenishment: Fluids, Gases & Energy]
    R --> N03[013 — Scheduled & Unscheduled Servicing]
    R --> N04[014 — Servicing Points, Couplings & Interfaces]
    R --> N05[015 — Servicing Records & Traceability]
```

## 4. Subsubject Index

| 01N | Title | Document | Status |
|---:|---|---|---|
| 010 | Overview | [`010_Overview.md`](./010_Overview.md) | active |
| 011 | Scope and Servicing Boundaries | [`011_Scope-and-Servicing-Boundaries.md`](./011_Scope-and-Servicing-Boundaries.md) | active |
| 012 | Replenishment: Fluids, Gases and Energy | [`012_Replenishment-Fluids-Gases-and-Energy.md`](./012_Replenishment-Fluids-Gases-and-Energy.md) | active |
| 013 | Scheduled and Unscheduled Servicing | [`013_Scheduled-and-Unscheduled-Servicing.md`](./013_Scheduled-and-Unscheduled-Servicing.md) | active |
| 014 | Servicing Points, Couplings and Interfaces | [`014_Servicing-Points-Couplings-and-Interfaces.md`](./014_Servicing-Points-Couplings-and-Interfaces.md) | active |
| 015 | Servicing Records and Traceability | [`015_Servicing-Records-and-Traceability.md`](./015_Servicing-Records-and-Traceability.md) | active |

## 5. Sibling Subsections (010-019 range)

| Code | Subsection | Document |
|---|---|---|
| `010` | Ground handling | [`../010_Ground-handling/README.md`](../010_Ground-handling/README.md) |
| `020` | servicing (this) | [`./README.md`](./README.md) |
| `030` | acceso | [`../030_acceso/010_Overview.md`](../030_acceso/010_Overview.md) |
| `040` | remolque | [`../040_remolque/README.md`](../040_remolque/README.md) |
| `050` | parking | [`../050_parking/010_Overview.md`](../050_parking/010_Overview.md) |
| `060` | GSE | [`../060_GSE/010_Overview.md`](../060_GSE/010_Overview.md) |

## 6. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top-Level Architecture System |
| Master range | `000–099` |
| Code range | `010-019` |
| Section | `01` — Manejo en Tierra & Servicio |
| Subject | `00` — General Information |
| Subsection | `020` — servicing |
| Subsubject namespace | `010`–`019` (`010` + `011`–`015` populated; canonical `01N_*.md` scheme) |
| Primary Q-Division | Q-GROUND[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-FIN |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/010-019_Manejo-en-Tierra-Servicio/020_servicing/` |
| Document | `README.md` (this file) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = ATLAS`, `primary_q_division = Q-GROUND` and `governance_class = baseline` from the parent ATLAS band; extensions added under `016`–`019` shall preserve those header fields, follow the canonical `01N_*.md` naming scheme, and reuse the footnote set declared below. Cross-subsection references with `010_Ground-handling/` shall preserve the *functional vs. physical* GSE-interface split stated in [`./010_Overview.md` §2](./010_Overview.md#2-scope) and in [`../010_Ground-handling/010_Overview.md` §2](../010_Ground-handling/010_Overview.md#2-scope). Subsubject `013` consumes the maintenance-program baseline at `LC11_MAINTENANCE/maintenance-program-baseline` (machine-readable via the document's front-matter `consumes` field) and shall not redefine it.

## 7. Change Log

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0.0 | 2026-05-06 | Q-GROUND | Initial population of subsection `020 servicing`: README + Overview enrichment (diagram, ATA cross-refs, GSE boundary clause) + subsubjects `011`–`015`. |

## 8. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **ATLAS §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `010-019` row (Section `01` — Manejo en Tierra & Servicio, Primary Q-Division Q-GROUND).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — Bands are classified as `baseline` or `restricted` per Q+ATLANTIDE §4 governance rules.

[^ata12]: **ATA Chapter 12 — Servicing** — Industry chapter covering routine servicing tasks performed during turn-around and overnight stops; canonical scope reference for ATLAS subsection `020`.

[^ata2200]: **ATA iSpec 2200 — Information Standards for Aviation Maintenance** — Industry standard for digital aircraft maintenance information; governs chapter / section / subject numbering inherited by ATLAS `000-099`.

[^ataspec100]: **ATA Spec 100 — Manufacturers' Technical Data** — Predecessor numbering scheme that established the 00–99 chapter map mirrored by ATLAS sub-ranges.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used across ATLAS technical publications.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

### Applicable industry standards

The following ATA-family and industry standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- ATA Chapter 12 — Servicing[^ata12]
- ATA iSpec 2200 — Information Standards for Aviation Maintenance[^ata2200]
- ATA Spec 100 — Manufacturers' Technical Data[^ataspec100]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
