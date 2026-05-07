---
document_id: QATL-ATLAS-1000-ATLAS-090-099-09-README
title: "ATLAS 090-099 · 09 — Tipos Específicos & Expansión (Section Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "090-099"
section: "09"
section_title: "Tipos Específicos & Expansión"
section_title_en: "Type-Specific & Expansion"
primary_q_division: Q-HORIZON
support_q_divisions: [Q-AIR, Q-STRUCTURES, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-MKTG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 090-099 · Section 09 — Tipos Específicos & Expansión

## 1. Purpose

Section-level index for *Tipos Específicos & Expansión* (`090-099`) within the ATLAS band. Variantes y demostradores AMPEL360 (tube-and-wing, BWB, H₂, MRTT, eVTOL, Sky-Cleaner) y registro de identificación de tipo.

This section is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. Bands classify technologies, Q-Divisions provide technical authority and ORB-Functions provide enterprise support[^n002].

## 2. Scope

- Aggregates the subsections within the `090-099` code range listed in §3.
- Inherits Q-Division authority and ORB support from the parent row in [`../README.md` §3](../README.md#3-architecture-table)[^archtable].
- Each subsection folder contains its own `README.md` (subsection index) and may contain Overview and subsubject documents.

## 3. Subsection Index

| Code | Title | Folder | Status |
|---:|---|---|---|
| `090` | AMPEL360e Tube-and-Wing Family | [`090_AMPEL360e-Tube-and-Wing-Family/`](./090_AMPEL360e-Tube-and-Wing-Family/) | active |
| `091` | AMPEL360 BWB Q100-Q250 | [`091_AMPEL360-BWB-Q100-Q250/`](./091_AMPEL360-BWB-Q100-Q250/) | active |
| `092` | AMPEL360 BWB H₂ Demonstrator | [`092_AMPEL360-BWB-H2-Demonstrator/`](./092_AMPEL360-BWB-H2-Demonstrator/) | active |
| `093` | AMPEL360 Q300 MRTT Tanker/Transport | [`093_AMPEL360-Q300-MRTT-Tanker-Transport/`](./093_AMPEL360-Q300-MRTT-Tanker-Transport/) | active |
| `094` | AMPEL360 City eVTOL — UAM | [`094_AMPEL360-City-eVTOL-UAM/`](./094_AMPEL360-City-eVTOL-UAM/) | active |
| `095` | AMPEL360 Sky-Cleaner — Environmental | [`095_AMPEL360-Sky-Cleaner-Environmental/`](./095_AMPEL360-Sky-Cleaner-Environmental/) | active |
| `096` | Type-Specific Variant Catalog | [`096_Type-Specific-Variant-Catalog/`](./096_Type-Specific-Variant-Catalog/) | active |
| `097` | Expansion — Reserved Future Programs | [`097_Expansion-Reserved-Future-Programs/`](./097_Expansion-Reserved-Future-Programs/) | active |
| `098` | Cross-Type Common Architectures | [`098_Cross-Type-Common-Architectures/`](./098_Cross-Type-Common-Architectures/) | active |
| `099` | Type Identification and Designator Registry | [`099_Type-Identification-and-Designator-Registry/`](./099_Type-Identification-and-Designator-Registry/) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `090-099` |
| Section | `09` — Tipos Específicos & Expansión |
| Subsections | 10 populated |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-AIR, Q-STRUCTURES, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-MKTG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/090-099_Tipos-Especificos-y-Expansion/` |
| Document | `README.md` (this file) |
| Parent architecture | [`../README.md`](../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsections under this section inherit `architecture_code = ATLAS`, `primary_q_division = Q-HORIZON` and `governance_class = baseline` from this section header. Templates declared in this section must populate `architecture_band`, `architecture_code = ATLAS`, `q_division_owner` and `orb_function_support` per the Templates System[^templates]. The No-AAA Rule[^n004] applies.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Architecture Table (parent)** — [`../README.md` §3](../README.md#3-architecture-table). Source of authority for primary/support Q-Divisions and ORB support of this section.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^templates]: **§5 — Templates System** — [`organization/Q+ATLANTIDE.md` §5](../../../organization/Q+ATLANTIDE.md#5-templates-system).

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../organization/Q+ATLANTIDE.md#4-notes).

[^n002]: **Note N-002** — Architecture bands classify technologies; Q-Divisions provide technical authority; ORB-Functions provide enterprise support. See [`organization/Q+ATLANTIDE.md` §4](../../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../../organization/Q+ATLANTIDE.md#4-notes).
