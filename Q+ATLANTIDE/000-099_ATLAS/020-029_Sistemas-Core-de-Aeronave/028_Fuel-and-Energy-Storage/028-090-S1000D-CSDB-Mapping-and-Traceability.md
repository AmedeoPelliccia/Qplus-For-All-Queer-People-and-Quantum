---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-028-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY
title: "ATLAS 020-029 · 02.028 · Section 028-090 — S1000D CSDB Mapping and Traceability"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "020-029"
section: "02"
section_title: "Sistemas Core de Aeronave"
subsection: "028"
subsection_title: "Fuel and Energy Storage"
local_section_code: "028-090"
ata_sns: "28-90-00"
title_short: "S1000D CSDB Mapping and Traceability"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: programme-controlled-publication-and-traceability-extension
status_note: >
  Section 028-090 is the programme-controlled publication and traceability
  extension for subsection 028. It maps all ATLAS 028 sections to S1000D DMC
  addresses and Q+ATLANTIDE URNs. Controlled by Q-AIR in coordination
  with Q-DATAGOV.
language: en
---

# ATLAS 020-029 · 02.028 · 028-090 — S1000D CSDB Mapping and Traceability

## 1. Purpose

Provide the complete S1000D CSDB Data Module Code (DMC) mapping for all sections within ATLAS subsection `028` — *Fuel and Energy Storage*, and define the Q+ATLANTIDE URN scheme for this subsection. This section enables bidirectional traceability between the ATLAS taxonomy and the S1000D-compliant Common Source Database (CSDB).

> **Programme-controlled publication and traceability extension.** This section is managed by Q-AIR in coordination with Q-DATAGOV and requires programme publication authority before CSDB records are issued.

## 2. Scope

- Provides the full ATA SNS-to-DMC mapping table for sections `028-000` through `028-080`.
- Defines the Q+ATLANTIDE URN scheme: `urn:qatl:atlas:020-029:028:{section-code}`.
- Establishes information type codes (IMC) and applicable information sets (Info Code) for each section.
- Does not contain narrative technical content — section files `028-000` through `028-080` carry the substantive architecture content.

## 3. CSDB Mapping Table

| Section | ATA SNS | DMC (example schema) | IMC | Info Code | Q+ATLANTIDE URN |
|---|---|---|---|---|---|
| 028-000 | 28-00-00 | DMC-QATL-A-28-00-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:028:000` |
| 028-010 | 28-10-00 | DMC-QATL-A-28-10-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:028:010` |
| 028-020 | 28-20-00 | DMC-QATL-A-28-20-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:028:020` |
| 028-030 | 28-30-00 | DMC-QATL-A-28-30-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:028:030` |
| 028-040 | 28-40-00 | DMC-QATL-A-28-40-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:028:040` |
| 028-050 | 28-50-00 | DMC-QATL-A-28-50-00-00A-018A-A | 018 | General (PCE-H2) | `urn:qatl:atlas:020-029:028:050` |
| 028-060 | 28-60-00 | DMC-QATL-A-28-60-00-00A-018A-A | 018 | General (PCE) | `urn:qatl:atlas:020-029:028:060` |
| 028-070 | 28-70-00 | DMC-QATL-A-28-70-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:028:070` |
| 028-080 | 28-80-00 | DMC-QATL-A-28-80-00-00A-018A-A | 018 | General (PCDE) | `urn:qatl:atlas:020-029:028:080` |

**URN scheme:** `urn:qatl:atlas:020-029:028:{section-code}`

**DMC schema note:** `DMC-QATL-A-{ATA-chapter}-{subsystem}-{subject}-{unit}-{DM-code}-{variant}-{applicability}` — schema instance codes are illustrative; final codes require CSDB configuration authority sign-off.

## 4. Traceability Architecture

```mermaid
graph TD
    CSDB["S1000D CSDB\n(Q+ATLANTIDE ATLAS-1000)"]
    URN028["URN: urn:qatl:atlas:020-029:028:{code}"]

    CSDB --> DMC000["DMC …28-00-00… (General)"]
    CSDB --> DMC010["DMC …28-10-00… (Storage)"]
    CSDB --> DMC020["DMC …28-20-00… (Distribution)"]
    CSDB --> DMC030["DMC …28-30-00… (Dump/Jettison/Transfer)"]
    CSDB --> DMC040["DMC …28-40-00… (Indicating)"]
    CSDB --> DMC050["DMC …28-50-00… (LH₂ Cryogenic Storage — PCE-H2)"]
    CSDB --> DMC060["DMC …28-60-00… (Fuel Cell Feed — PCE)"]
    CSDB --> DMC070["DMC …28-70-00… (Venting/Purge/Leak Detection)"]
    CSDB --> DMC080["DMC …28-80-00… (Monitoring/Diagnostics — PCDE)"]

    URN028 -->|resolves to| CSDB
    QAIR["Q-AIR\n(System Authority)"] -->|coordinates| QDATAGOV["Q-DATAGOV\n(Publication Authority)"]
    QDATAGOV -->|governs| CSDB
```

## 5. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `028` — Fuel and Energy Storage |
| Local section code | `028-090` |
| ATA SNS | `28-90-00` |
| Status | `programme-controlled-publication-and-traceability-extension` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| URN base | `urn:qatl:atlas:020-029:028:` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/028_Fuel-and-Energy-Storage/` |
| Document | `028-090-S1000D-CSDB-Mapping-and-Traceability.md` |
| Parent subsection | [`README.md`](./README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 6. References

- S1000D Issue 5.0 — Data Module Code structure and CSDB configuration management
- ATA iSpec 2200 — Chapter 28, Fuel
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `028-000` General [`./028-000-General.md`](./028-000-General.md)
- `027-090` S1000D CSDB Mapping (027) [`../027_Flight-Controls/027-090-S1000D-CSDB-Mapping-and-Traceability.md`](../027_Flight-Controls/027-090-S1000D-CSDB-Mapping-and-Traceability.md)
- `026-090` S1000D CSDB Mapping (026) [`../026_Fire-Protection/026-090-S1000D-CSDB-Mapping-and-Traceability.md`](../026_Fire-Protection/026-090-S1000D-CSDB-Mapping-and-Traceability.md)
