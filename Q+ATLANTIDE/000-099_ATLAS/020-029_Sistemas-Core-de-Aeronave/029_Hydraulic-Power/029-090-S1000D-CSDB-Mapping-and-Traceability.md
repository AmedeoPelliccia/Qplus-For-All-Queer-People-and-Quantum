---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-029-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY
title: "ATLAS 020-029 · 02.029 · Section 029-090 — S1000D CSDB Mapping and Traceability"
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
subsection: "029"
subsection_title: "Hydraulic Power"
local_section_code: "029-090"
ata_sns: "29-90-00"
title_short: "S1000D CSDB Mapping and Traceability"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: programme-controlled-publication-and-traceability-extension
status_note: >
  Section 029-090 is the programme-controlled publication and traceability
  extension for subsection 029. It maps all ATLAS 029 sections to S1000D DMC
  addresses and Q+ATLANTIDE URNs. Controlled by Q-AIR in coordination
  with Q-DATAGOV.
language: en
---

# ATLAS 020-029 · 02.029 · 029-090 — S1000D CSDB Mapping and Traceability

## 1. Purpose

Provide the complete S1000D CSDB Data Module Code (DMC) mapping for all sections within ATLAS subsection `029` — *Hydraulic Power*, and define the Q+ATLANTIDE URN scheme for this subsection. This section enables bidirectional traceability between the ATLAS taxonomy and the S1000D-compliant Common Source Database (CSDB).

> **Programme-controlled publication and traceability extension.** This section is managed by Q-AIR in coordination with Q-DATAGOV and requires programme publication authority before CSDB records are issued.

## 2. Scope

- Provides the full ATA SNS-to-DMC mapping table for sections `029-000` through `029-080`.
- Defines the Q+ATLANTIDE URN scheme: `urn:qatl:atlas:020-029:029:{section-code}`.
- Establishes information type codes (IMC) and applicable information sets (Info Code) for each section.
- Does not contain narrative technical content — section files `029-000` through `029-080` carry the substantive architecture content.

## 3. CSDB Mapping Table

| Section | ATA SNS | DMC (example schema) | IMC | Info Code | Q+ATLANTIDE URN |
|---|---|---|---|---|---|
| 029-000 | 29-00-00 | DMC-QATL-A-29-00-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:029:000` |
| 029-010 | 29-10-00 | DMC-QATL-A-29-10-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:029:010` |
| 029-020 | 29-20-00 | DMC-QATL-A-29-20-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:029:020` |
| 029-030 | 29-30-00 | DMC-QATL-A-29-30-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:029:030` |
| 029-040 | 29-40-00 | DMC-QATL-A-29-40-00-00A-018A-A | 018 | General (PCE-dist) | `urn:qatl:atlas:020-029:029:040` |
| 029-050 | 29-50-00 | DMC-QATL-A-29-50-00-00A-018A-A | 018 | General (PCE-pumps) | `urn:qatl:atlas:020-029:029:050` |
| 029-060 | 29-60-00 | DMC-QATL-A-29-60-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:029:060` |
| 029-070 | 29-70-00 | DMC-QATL-A-29-70-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:029:070` |
| 029-080 | 29-80-00 | DMC-QATL-A-29-80-00-00A-018A-A | 018 | General (PCDE) | `urn:qatl:atlas:020-029:029:080` |

**URN scheme:** `urn:qatl:atlas:020-029:029:{section-code}`

**DMC schema note:** `DMC-QATL-A-{ATA-chapter}-{subsystem}-{subject}-{unit}-{DM-code}-{variant}-{applicability}` — schema instance codes are illustrative; final codes require CSDB configuration authority sign-off.

## 4. Traceability Architecture

```mermaid
graph TD
    CSDB["S1000D CSDB\n(Q+ATLANTIDE ATLAS-1000)"]
    URN029["URN: urn:qatl:atlas:020-029:029:{code}"]

    CSDB --> DMC000["DMC …29-00-00… (General)"]
    CSDB --> DMC010["DMC …29-10-00… (Main Hydraulic Power)"]
    CSDB --> DMC020["DMC …29-20-00… (Auxiliary Hydraulic Power)"]
    CSDB --> DMC030["DMC …29-30-00… (Indicating)"]
    CSDB --> DMC040["DMC …29-40-00… (Distribution, Reservoirs & Lines — PCE-dist)"]
    CSDB --> DMC050["DMC …29-50-00… (Pumps, Accumulators & Pressure Control — PCE-pumps)"]
    CSDB --> DMC060["DMC …29-60-00… (Fluids, Filters & Servicing)"]
    CSDB --> DMC070["DMC …29-70-00… (Isolation, Leak Detection & Safety)"]
    CSDB --> DMC080["DMC …29-80-00… (Monitoring/Diagnostics — PCDE)"]

    URN029 -->|resolves to| CSDB
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
| Subsection | `029` — Hydraulic Power |
| Local section code | `029-090` |
| ATA SNS | `29-90-00` |
| Status | `programme-controlled-publication-and-traceability-extension` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| URN base | `urn:qatl:atlas:020-029:029:` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/029_Hydraulic-Power/` |
| Document | `029-090-S1000D-CSDB-Mapping-and-Traceability.md` |
| Parent subsection | [`README.md`](./README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 6. References

- S1000D Issue 5.0 — Data Module Code structure and CSDB configuration management
- ATA iSpec 2200 — Chapter 29, Hydraulic Power
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `029-000` General [`./029-000-General.md`](./029-000-General.md)
- `028-090` S1000D CSDB Mapping (028) [`../028_Fuel-and-Energy-Storage/028-090-S1000D-CSDB-Mapping-and-Traceability.md`](../028_Fuel-and-Energy-Storage/028-090-S1000D-CSDB-Mapping-and-Traceability.md)
- `027-090` S1000D CSDB Mapping (027) [`../027_Flight-Controls/027-090-S1000D-CSDB-Mapping-and-Traceability.md`](../027_Flight-Controls/027-090-S1000D-CSDB-Mapping-and-Traceability.md)
