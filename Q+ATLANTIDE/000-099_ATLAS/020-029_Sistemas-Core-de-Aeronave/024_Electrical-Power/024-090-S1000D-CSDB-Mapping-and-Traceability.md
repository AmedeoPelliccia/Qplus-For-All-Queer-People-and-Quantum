---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-024-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY
title: "ATLAS 020-029 · 02.024 · Section 024-090 — S1000D CSDB Mapping and Traceability"
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
subsection: "024"
subsection_title: "Electrical Power"
local_section_code: "024-090"
ata_sns: "24-90-00"
title_short: "S1000D CSDB Mapping and Traceability"
primary_q_division: Q-MECHANICS
support_q_divisions: [Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: programme-controlled-publication-and-traceability-extension
status_note: >
  Section 024-090 is the programme-controlled publication and traceability
  extension for subsection 024. It maps all ATLAS 024 sections to S1000D DMC
  addresses and Q+ATLANTIDE URNs. Controlled by Q-MECHANICS in coordination
  with Q-DATAGOV.
language: en
---

# ATLAS 020-029 · 02.024 · 024-090 — S1000D CSDB Mapping and Traceability

## 1. Purpose

Provide the complete S1000D CSDB Data Module Code (DMC) mapping for all sections within ATLAS subsection `024` — *Electrical Power*, and define the Q+ATLANTIDE URN scheme for this subsection. This section enables bidirectional traceability between the ATLAS taxonomy and the S1000D-compliant Common Source Database (CSDB).

> **Programme-controlled publication and traceability extension.** This section is managed by Q-MECHANICS in coordination with Q-DATAGOV and requires programme publication authority before CSDB records are issued.

## 2. Scope

- Provides the full ATA SNS-to-DMC mapping table for sections `024-000` through `024-080`.
- Defines the Q+ATLANTIDE URN scheme: `urn:qatl:atlas:020-029:024:{section-code}`.
- Establishes information type codes (IMC) and applicable information sets (Info Code) for each section.
- Does not contain narrative technical content — section files `024-000` through `024-080` carry the substantive architecture content.

## 3. CSDB Mapping Table

| Section | ATA SNS | DMC (example schema) | IMC | Info Code | Q+ATLANTIDE URN |
|---|---|---|---|---|---|
| 024-000 | 24-00-00 | DMC-QATL-A-24-00-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:024:000` |
| 024-010 | 24-10-00 | DMC-QATL-A-24-10-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:024:010` |
| 024-020 | 24-20-00 | DMC-QATL-A-24-20-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:024:020` |
| 024-030 | 24-30-00 | DMC-QATL-A-24-30-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:024:030` |
| 024-040 | 24-40-00 | DMC-QATL-A-24-40-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:024:040` |
| 024-050 | 24-50-00 | DMC-QATL-A-24-50-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:024:050` |
| 024-060 | 24-60-00 | DMC-QATL-A-24-60-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:024:060` |
| 024-070 | 24-70-00 | DMC-QATL-A-24-70-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:024:070` |
| 024-080 | 24-80-00 | DMC-QATL-A-24-80-00-00A-018A-A | 018 | General (PCDE) | `urn:qatl:atlas:020-029:024:080` |

**URN scheme:** `urn:qatl:atlas:020-029:024:{section-code}`

**DMC schema note:** `DMC-QATL-A-{ATA-chapter}-{subsystem}-{subject}-{unit}-{DM-code}-{variant}-{applicability}` — schema instance codes are illustrative; final codes require CSDB configuration authority sign-off.

## 4. Traceability Architecture

```mermaid
graph TD
    CSDB["S1000D CSDB\n(Q+ATLANTIDE ATLAS-1000)"]
    URN024["URN: urn:qatl:atlas:020-029:024:{code}"]

    CSDB --> DMC000["DMC …24-00-00… (General)"]
    CSDB --> DMC010["DMC …24-10-00… (Generator Drive)"]
    CSDB --> DMC020["DMC …24-20-00… (AC Generation)"]
    CSDB --> DMC030["DMC …24-30-00… (DC Generation)"]
    CSDB --> DMC040["DMC …24-40-00… (External Power)"]
    CSDB --> DMC050["DMC …24-50-00… (AC Load Distribution)"]
    CSDB --> DMC060["DMC …24-60-00… (DC Load Distribution)"]
    CSDB --> DMC070["DMC …24-70-00… (Emergency/Standby Power)"]
    CSDB --> DMC080["DMC …24-80-00… (Monitoring/Diagnostics)"]

    URN024 -->|resolves to| CSDB
    QMECH["Q-MECHANICS\n(System Authority)"] -->|coordinates| QDATAGOV["Q-DATAGOV\n(Publication Authority)"]
    QDATAGOV -->|governs| CSDB
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `024` — Electrical Power |
| Local section code | `024-090` |
| ATA SNS | `24-90-00` |
| Status | `programme-controlled-publication-and-traceability-extension` |
| Primary Q-Division | Q-MECHANICS |
| Support Q-Divisions | Q-AIR, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| URN base | `urn:qatl:atlas:020-029:024:` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/024_Electrical-Power/` |
| Document | `024-090-S1000D-CSDB-Mapping-and-Traceability.md` |
| Parent subsection | [`README.md`](./README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References

- S1000D Issue 5.0 — Data Module Code structure and CSDB configuration management
- ATA iSpec 2200 — Chapter 24, Electrical Power
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `024-000` General [`./024-000-General.md`](./024-000-General.md)
- `022-090` S1000D CSDB Mapping (022) [`../022_Auto-Flight/022-090-S1000D-CSDB-Mapping-and-Traceability.md`](../022_Auto-Flight/022-090-S1000D-CSDB-Mapping-and-Traceability.md)
- `023-090` S1000D CSDB Mapping (023) [`../023_Communications/023-090-S1000D-CSDB-Mapping-and-Traceability.md`](../023_Communications/023-090-S1000D-CSDB-Mapping-and-Traceability.md)
