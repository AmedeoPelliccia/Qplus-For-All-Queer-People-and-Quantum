---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-023-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY
title: "ATLAS 020-029 · 02.023 · Section 023-090 — S1000D CSDB Mapping and Traceability"
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
subsection: "023"
subsection_title: "Communications"
local_section_code: "023-090"
ata_sns: "23-90-00"
title_short: "S1000D CSDB Mapping and Traceability"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-AIR, Q-HPC, Q-GROUND, Q-MECHANICS, Q-SPACE]
governance_class: baseline
version: 1.0.0
status: programme-controlled-publication-and-traceability-extension
status_note: >
  Section 023-090 is the programme-controlled publication and traceability
  extension for subsection 023. It maps all ATLAS 023 sections to S1000D DMC
  addresses and Q+ATLANTIDE URNs. Controlled by Q-DATAGOV.
language: en
---

# ATLAS 020-029 · 02.023 · 023-090 — S1000D CSDB Mapping and Traceability

## 1. Purpose

Provide the complete S1000D CSDB Data Module Code (DMC) mapping for all sections within ATLAS subsection `023` — *Communications*, and define the Q+ATLANTIDE URN scheme for this subsection. This section enables bidirectional traceability between the ATLAS taxonomy and the S1000D-compliant Common Source Database (CSDB).

> **Programme-controlled publication and traceability extension.** This section is managed by Q-DATAGOV and requires programme publication authority before CSDB records are issued.

## 2. Scope

- Provides the full ATA SNS-to-DMC mapping table for sections `023-000` through `023-080`.
- Defines the Q+ATLANTIDE URN scheme: `urn:qatl:atlas:020-029:023:{section-code}`.
- Establishes information type codes (IMC) and applicable information sets (Info Code) for each section.
- Does not contain narrative technical content — section files `023-000` through `023-080` carry the substantive architecture content.

## 3. CSDB Mapping Table

| Section | ATA SNS | DMC (example schema) | IMC | Info Code | Q+ATLANTIDE URN |
|---|---|---|---|---|---|
| 023-000 | 23-00-00 | DMC-QATL-A-23-00-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:023:000` |
| 023-010 | 23-10-00 | DMC-QATL-A-23-10-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:023:010` |
| 023-020 | 23-20-00 | DMC-QATL-A-23-20-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:023:020` |
| 023-030 | 23-30-00 | DMC-QATL-A-23-30-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:023:030` |
| 023-040 | 23-40-00 | DMC-QATL-A-23-40-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:023:040` |
| 023-050 | 23-50-00 | DMC-QATL-A-23-50-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:023:050` |
| 023-060 | 23-60-00 | DMC-QATL-A-23-60-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:023:060` |
| 023-070 | 23-70-00 | DMC-QATL-A-23-70-00-00A-018A-A | 018 | General (PCE) | `urn:qatl:atlas:020-029:023:070` |
| 023-080 | 23-80-00 | DMC-QATL-A-23-80-00-00A-018A-A | 018 | General (PCDE) | `urn:qatl:atlas:020-029:023:080` |

**URN scheme:** `urn:qatl:atlas:020-029:023:{section-code}`

**DMC schema note:** `DMC-QATL-A-{ATA-chapter}-{subsystem}-{subject}-{unit}-{DM-code}-{variant}-{applicability}` — schema instance codes are illustrative; final codes require CSDB configuration authority sign-off.

## 4. Traceability Architecture

```mermaid
graph TD
    CSDB["S1000D CSDB\n(Q+ATLANTIDE ATLAS-1000)"]
    URN023["URN: urn:qatl:atlas:020-029:023:{code}"]

    CSDB --> DMC000["DMC …23-00-00… (General)"]
    CSDB --> DMC010["DMC …23-10-00… (Speech Comms)"]
    CSDB --> DMC020["DMC …23-20-00… (Data Comms)"]
    CSDB --> DMC030["DMC …23-30-00… (PA / Cabin)"]
    CSDB --> DMC040["DMC …23-40-00… (Interphone)"]
    CSDB --> DMC050["DMC …23-50-00… (Audio Integrating)"]
    CSDB --> DMC060["DMC …23-60-00… (Static / EMI)"]
    CSDB --> DMC070["DMC …23-70-00… (AV / Cabin Mon.)"]
    CSDB --> DMC080["DMC …23-80-00… (SATCOM/Datalink)"]

    URN023 -->|resolves to| CSDB
    QDATAGOV["Q-DATAGOV\n(Publication Authority)"] -->|governs| CSDB
```

## 5. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `023` — Communications |
| Local section code | `023-090` |
| ATA SNS | `23-90-00` |
| Status | `programme-controlled-publication-and-traceability-extension` |
| Primary Q-Division | Q-DATAGOV |
| Support Q-Divisions | Q-AIR, Q-HPC, Q-GROUND, Q-MECHANICS, Q-SPACE |
| Governance class | `baseline` |
| URN base | `urn:qatl:atlas:020-029:023:` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/023_Communications/` |
| Document | `023-090-S1000D-CSDB-Mapping-and-Traceability.md` |
| Parent subsection | [`README.md`](./README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 6. References

- S1000D Issue 5.0 — Data Module Code structure and CSDB configuration management
- ATA iSpec 2200 — Chapter 23, Communications
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `023-000` General [`./023-000-General.md`](./023-000-General.md)
- `021-090` S1000D CSDB Mapping (021) [`../021_Air-Conditioning-and-Pressurization/021-090-S1000D-CSDB-Mapping-and-Traceability.md`](../021_Air-Conditioning-and-Pressurization/021-090-S1000D-CSDB-Mapping-and-Traceability.md)
- `022-090` S1000D CSDB Mapping (022) [`../022_Auto-Flight/022-090-S1000D-CSDB-Mapping-and-Traceability.md`](../022_Auto-Flight/022-090-S1000D-CSDB-Mapping-and-Traceability.md)
