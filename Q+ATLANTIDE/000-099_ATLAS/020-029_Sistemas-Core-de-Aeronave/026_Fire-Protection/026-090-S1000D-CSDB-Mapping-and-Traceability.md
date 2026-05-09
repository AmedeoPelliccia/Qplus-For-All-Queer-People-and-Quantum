---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-026-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY
title: "ATLAS 020-029 · 02.026 · Section 026-090 — S1000D CSDB Mapping and Traceability"
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
subsection: "026"
subsection_title: "Fire Protection"
local_section_code: "026-090"
ata_sns: "26-90-00"
title_short: "S1000D CSDB Mapping and Traceability"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: programme-controlled-publication-and-traceability-extension
status_note: >
  Section 026-090 is the programme-controlled publication and traceability
  extension for subsection 026. It maps all ATLAS 026 sections to S1000D DMC
  addresses and Q+ATLANTIDE URNs. Controlled by Q-AIR in coordination
  with Q-DATAGOV.
language: en
---

# ATLAS 020-029 · 02.026 · 026-090 — S1000D CSDB Mapping and Traceability

## 1. Purpose

Provide the complete S1000D CSDB Data Module Code (DMC) mapping for all sections within ATLAS subsection `026` — *Fire Protection*, and define the Q+ATLANTIDE URN scheme for this subsection. This section enables bidirectional traceability between the ATLAS taxonomy and the S1000D-compliant Common Source Database (CSDB).

> **Programme-controlled publication and traceability extension.** This section is managed by Q-AIR in coordination with Q-DATAGOV and requires programme publication authority before CSDB records are issued.

## 2. Scope

- Provides the full ATA SNS-to-DMC mapping table for sections `026-000` through `026-080`.
- Defines the Q+ATLANTIDE URN scheme: `urn:qatl:atlas:020-029:026:{section-code}`.
- Establishes information type codes (IMC) and applicable information sets (Info Code) for each section.
- Does not contain narrative technical content — section files `026-000` through `026-080` carry the substantive architecture content.

## 3. CSDB Mapping Table

| Section | ATA SNS | DMC (example schema) | IMC | Info Code | Q+ATLANTIDE URN |
|---|---|---|---|---|---|
| 026-000 | 26-00-00 | DMC-QATL-A-26-00-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:026:000` |
| 026-010 | 26-10-00 | DMC-QATL-A-26-10-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:026:010` |
| 026-020 | 26-20-00 | DMC-QATL-A-26-20-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:026:020` |
| 026-030 | 26-30-00 | DMC-QATL-A-26-30-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:026:030` |
| 026-040 | 26-40-00 | DMC-QATL-A-26-40-00-00A-018A-A | 018 | General (PCE) | `urn:qatl:atlas:020-029:026:040` |
| 026-050 | 26-50-00 | DMC-QATL-A-26-50-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:026:050` |
| 026-060 | 26-60-00 | DMC-QATL-A-26-60-00-00A-018A-A | 018 | General | `urn:qatl:atlas:020-029:026:060` |
| 026-070 | 26-70-00 | DMC-QATL-A-26-70-00-00A-018A-A | 018 | General (PCE) | `urn:qatl:atlas:020-029:026:070` |
| 026-080 | 26-80-00 | DMC-QATL-A-26-80-00-00A-018A-A | 018 | General (PCDE) | `urn:qatl:atlas:020-029:026:080` |

**URN scheme:** `urn:qatl:atlas:020-029:026:{section-code}`

**DMC schema note:** `DMC-QATL-A-{ATA-chapter}-{subsystem}-{subject}-{unit}-{DM-code}-{variant}-{applicability}` — schema instance codes are illustrative; final codes require CSDB configuration authority sign-off.

## 4. Traceability Architecture

```mermaid
graph TD
    CSDB["S1000D CSDB\n(Q+ATLANTIDE ATLAS-1000)"]
    URN026["URN: urn:qatl:atlas:020-029:026:{code}"]

    CSDB --> DMC000["DMC …26-00-00… (General)"]
    CSDB --> DMC010["DMC …26-10-00… (Fire and Smoke Detection)"]
    CSDB --> DMC020["DMC …26-20-00… (Fire Extinguishing)"]
    CSDB --> DMC030["DMC …26-30-00… (Explosion Suppression)"]
    CSDB --> DMC040["DMC …26-40-00… (Engine/APU/Nacelle — PCE)"]
    CSDB --> DMC050["DMC …26-50-00… (Cargo/Baggage Fire Protection)"]
    CSDB --> DMC060["DMC …26-60-00… (Cabin/Lavatory Fire Protection)"]
    CSDB --> DMC070["DMC …26-70-00… (H₂/Electric Propulsion — PCE)"]
    CSDB --> DMC080["DMC …26-80-00… (Monitoring/Diagnostics — PCDE)"]

    URN026 -->|resolves to| CSDB
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
| Subsection | `026` — Fire Protection |
| Local section code | `026-090` |
| ATA SNS | `26-90-00` |
| Status | `programme-controlled-publication-and-traceability-extension` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| URN base | `urn:qatl:atlas:020-029:026:` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/026_Fire-Protection/` |
| Document | `026-090-S1000D-CSDB-Mapping-and-Traceability.md` |
| Parent subsection | [`README.md`](./README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 6. References

- S1000D Issue 5.0 — Data Module Code structure and CSDB configuration management
- ATA iSpec 2200 — Chapter 26, Fire Protection
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `026-000` General [`./026-000-General.md`](./026-000-General.md)
- `024-090` S1000D CSDB Mapping (024) [`../024_Electrical-Power/024-090-S1000D-CSDB-Mapping-and-Traceability.md`](../024_Electrical-Power/024-090-S1000D-CSDB-Mapping-and-Traceability.md)
- `025-090` S1000D CSDB Mapping (025) [`../025_Equipment-and-Furnishings/025-090-S1000D-CSDB-Mapping-and-Traceability.md`](../025_Equipment-and-Furnishings/025-090-S1000D-CSDB-Mapping-and-Traceability.md)
