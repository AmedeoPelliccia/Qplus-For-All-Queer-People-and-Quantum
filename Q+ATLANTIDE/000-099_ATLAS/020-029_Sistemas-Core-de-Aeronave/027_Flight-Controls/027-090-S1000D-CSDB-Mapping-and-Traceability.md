---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-027-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY
title: "ATLAS 020-029 · 02.027 · Section 027-090 — S1000D CSDB Mapping and Traceability"
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
subsection: "027"
subsection_title: "Flight Controls"
local_section_code: "027-090"
ata_sns: "27-90-00"
title_short: "S1000D CSDB Mapping and Traceability"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: programme-controlled-publication-and-traceability-extension
status_note: >
  Section 027-090 is the programme-controlled publication and traceability
  extension for subsection 027. It maps all ATLAS 027 sections to S1000D DMC
  addresses and Q+ATLANTIDE URNs. Controlled by Q-AIR in coordination
  with Q-DATAGOV.
language: en
---

# ATLAS 020-029 · 02.027 · 027-090 — S1000D CSDB Mapping and Traceability

## 1. Purpose

Provide the complete S1000D CSDB Data Module Code (DMC) mapping for all sections within ATLAS subsection `027` — *Flight Controls*, and define the Q+ATLANTIDE URN scheme for this subsection. This section enables bidirectional traceability between the ATLAS taxonomy and the S1000D-compliant Common Source Database (CSDB).

> **Programme-controlled publication and traceability extension.** This section is managed by Q-AIR in coordination with Q-DATAGOV and requires programme publication authority before CSDB records are issued.

## 2. Scope

- Provides the full ATA SNS-to-DMC mapping table for sections `027-000` through `027-080`.
- Defines the Q+ATLANTIDE URN scheme: `urn:qatl:atlas:020-029:027:{section-code}`.
- Establishes information type codes (IMC) and applicable information sets (Info Code) for each section.
- Does not contain narrative technical content — section files `027-000` through `027-080` carry the substantive architecture content.

## 3. CSDB Mapping Table

| Section | ATA SNS | DMC (example schema) | IMC | Info Code | Q+ATLANTIDE URN |
|---|---|---|---|---|---|
| 027-000 | 27-00-00 | DMC-QATL-A-27-00-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:027:000` |
| 027-010 | 27-10-00 | DMC-QATL-A-27-10-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:027:010` |
| 027-020 | 27-20-00 | DMC-QATL-A-27-20-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:027:020` |
| 027-030 | 27-30-00 | DMC-QATL-A-27-30-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:027:030` |
| 027-040 | 27-40-00 | DMC-QATL-A-27-40-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:027:040` |
| 027-050 | 27-50-00 | DMC-QATL-A-27-50-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:027:050` |
| 027-060 | 27-60-00 | DMC-QATL-A-27-60-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:027:060` |
| 027-070 | 27-70-00 | DMC-QATL-A-27-70-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:027:070` |
| 027-080 | 27-80-00 | DMC-QATL-A-27-80-00-00A-018A-A | 018 | General (PCDE) | `urn:qatl:atlas:020-029:027:080` |

**URN scheme:** `urn:qatl:atlas:020-029:027:{section-code}`

**DMC schema note:** `DMC-QATL-A-{ATA-chapter}-{subsystem}-{subject}-{unit}-{DM-code}-{variant}-{applicability}` — schema instance codes are illustrative; final codes require CSDB configuration authority sign-off.

## 4. Traceability Architecture

```mermaid
graph TD
    CSDB["S1000D CSDB\n(Q+ATLANTIDE ATLAS-1000)"]
    URN027["URN: urn:qatl:atlas:020-029:027:{code}"]

    CSDB --> DMC000["DMC …27-00-00… (General)"]
    CSDB --> DMC010["DMC …27-10-00… (Aileron/Elevon/Roll Control)"]
    CSDB --> DMC020["DMC …27-20-00… (Rudder/Yaw Control)"]
    CSDB --> DMC030["DMC …27-30-00… (Elevator/Pitch Control)"]
    CSDB --> DMC040["DMC …27-40-00… (Stabilizer/Pitch Trim)"]
    CSDB --> DMC050["DMC …27-50-00… (Flaps/High Lift)"]
    CSDB --> DMC060["DMC …27-60-00… (Spoilers/Speedbrakes)"]
    CSDB --> DMC070["DMC …27-70-00… (Actuation/Feel/Gust Lock)"]
    CSDB --> DMC080["DMC …27-80-00… (FBW Monitoring/Diagnostics — PCDE)"]

    URN027 -->|resolves to| CSDB
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
| Subsection | `027` — Flight Controls |
| Local section code | `027-090` |
| ATA SNS | `27-90-00` |
| Status | `programme-controlled-publication-and-traceability-extension` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-HPC, Q-INDUSTRY |
| Governance class | `baseline` |
| URN base | `urn:qatl:atlas:020-029:027:` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/027_Flight-Controls/` |
| Document | `027-090-S1000D-CSDB-Mapping-and-Traceability.md` |
| Parent subsection | [`README.md`](./README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 6. References

- S1000D Issue 5.0 — Data Module Code structure and CSDB configuration management
- ATA iSpec 2200 — Chapter 27, Flight Controls
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `027-000` General [`./027-000-General.md`](./027-000-General.md)
- `026-090` S1000D CSDB Mapping (026) [`../026_Fire-Protection/026-090-S1000D-CSDB-Mapping-and-Traceability.md`](../026_Fire-Protection/026-090-S1000D-CSDB-Mapping-and-Traceability.md)
- `028-090` S1000D CSDB Mapping (028) [`../028_Fuel-and-Energy-Storage/028-090-S1000D-CSDB-Mapping-and-Traceability.md`](../028_Fuel-and-Energy-Storage/028-090-S1000D-CSDB-Mapping-and-Traceability.md)
