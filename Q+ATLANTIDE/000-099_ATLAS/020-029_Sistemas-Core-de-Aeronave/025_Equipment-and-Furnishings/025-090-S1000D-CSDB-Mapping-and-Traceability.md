---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-025-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY
title: "ATLAS 020-029 · 02.025 · Section 025-090 — S1000D CSDB Mapping and Traceability"
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
subsection: "025"
subsection_title: "Equipment and Furnishings"
local_section_code: "025-090"
ata_sns: "25-90-00"
title_short: "S1000D CSDB Mapping and Traceability"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: programme-controlled-publication-and-traceability-extension
status_note: >
  Section 025-090 is the programme-controlled publication and traceability
  extension for subsection 025. It maps all ATLAS 025 sections to S1000D DMC
  addresses and Q+ATLANTIDE URNs. Controlled by Q-AIR in coordination
  with Q-DATAGOV.
language: en
---

# ATLAS 020-029 · 02.025 · 025-090 — S1000D CSDB Mapping and Traceability

## 1. Purpose

Provide the complete S1000D CSDB Data Module Code (DMC) mapping for all sections within ATLAS subsection `025` — *Equipment and Furnishings*, and define the Q+ATLANTIDE URN scheme for this subsection. This section enables bidirectional traceability between the ATLAS taxonomy and the S1000D-compliant Common Source Database (CSDB).

> **Programme-controlled publication and traceability extension.** This section is managed by Q-AIR in coordination with Q-DATAGOV and requires programme publication authority before CSDB records are issued.

## 2. Scope

- Provides the full ATA SNS-to-DMC mapping table for sections `025-000` through `025-080`.
- Defines the Q+ATLANTIDE URN scheme: `urn:qatl:atlas:020-029:025:{section-code}`.
- Establishes information type codes (IMC) and applicable information sets (Info Code) for each section.
- Does not contain narrative technical content — section files `025-000` through `025-080` carry the substantive architecture content.

## 3. CSDB Mapping Table

| Section | ATA SNS | DMC (example schema) | IMC | Info Code | Q+ATLANTIDE URN |
|---|---|---|---|---|---|
| 025-000 | 25-00-00 | DMC-QATL-A-25-00-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:025:000` |
| 025-010 | 25-10-00 | DMC-QATL-A-25-10-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:025:010` |
| 025-020 | 25-20-00 | DMC-QATL-A-25-20-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:025:020` |
| 025-030 | 25-30-00 | DMC-QATL-A-25-30-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:025:030` |
| 025-040 | 25-40-00 | DMC-QATL-A-25-40-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:025:040` |
| 025-050 | 25-50-00 | DMC-QATL-A-25-50-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:025:050` |
| 025-060 | 25-60-00 | DMC-QATL-A-25-60-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:025:060` |
| 025-070 | 25-70-00 | DMC-QATL-A-25-70-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:025:070` |
| 025-080 | 25-80-00 | DMC-QATL-A-25-80-00-00A-018A-A | 018 | General (PCE) | `urn:qatl:atlas:020-029:025:080` |

**URN scheme:** `urn:qatl:atlas:020-029:025:{section-code}`

**DMC schema note:** `DMC-QATL-A-{ATA-chapter}-{subsystem}-{subject}-{unit}-{DM-code}-{variant}-{applicability}` — schema instance codes are illustrative; final codes require CSDB configuration authority sign-off.

## 3. Traceability Architecture

```mermaid
graph TD
    CSDB["S1000D CSDB\n(Q+ATLANTIDE ATLAS-1000)"]
    URN025["URN: urn:qatl:atlas:020-029:025:{code}"]

    CSDB --> DMC000["DMC …25-00-00… (General)"]
    CSDB --> DMC010["DMC …25-10-00… (Flight Compartment)"]
    CSDB --> DMC020["DMC …25-20-00… (Passenger Compartment)"]
    CSDB --> DMC030["DMC …25-30-00… (Buffet/Galley)"]
    CSDB --> DMC040["DMC …25-40-00… (Lavatories)"]
    CSDB --> DMC050["DMC …25-50-00… (Cargo Compartments)"]
    CSDB --> DMC060["DMC …25-60-00… (Emergency Equipment)"]
    CSDB --> DMC070["DMC …25-70-00… (Accessory Compartments)"]
    CSDB --> DMC080["DMC …25-80-00… (Monitoring/Diagnostics)"]

    URN025 -->|resolves to| CSDB
    QAIR["Q-AIR\n(System Authority)"] -->|coordinates| QDATAGOV["Q-DATAGOV\n(Publication Authority)"]
    QDATAGOV -->|governs| CSDB
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `025` — Equipment and Furnishings |
| Local section code | `025-090` |
| ATA SNS | `25-90-00` |
| Status | `programme-controlled-publication-and-traceability-extension` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| URN base | `urn:qatl:atlas:020-029:025:` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/025_Equipment-and-Furnishings/` |
| Document | `025-090-S1000D-CSDB-Mapping-and-Traceability.md` |
| Parent subsection | [`README.md`](./README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References

- S1000D Issue 5.0 — Data Module Code structure and CSDB configuration management
- ATA iSpec 2200 — Chapter 25, Equipment / Furnishings
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `025-000` General [`./025-000-General.md`](./025-000-General.md)
- `024-090` S1000D CSDB Mapping (024) [`../024_Electrical-Power/024-090-S1000D-CSDB-Mapping-and-Traceability.md`](../024_Electrical-Power/024-090-S1000D-CSDB-Mapping-and-Traceability.md)
