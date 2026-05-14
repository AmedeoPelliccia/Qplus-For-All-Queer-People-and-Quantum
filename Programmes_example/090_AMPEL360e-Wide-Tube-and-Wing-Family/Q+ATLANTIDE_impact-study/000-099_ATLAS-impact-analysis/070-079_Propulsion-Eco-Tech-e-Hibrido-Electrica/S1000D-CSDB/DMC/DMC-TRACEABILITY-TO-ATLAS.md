---
document_id: DMC-TRACEABILITY-TO-ATLAS
title: "CSDB Traceability to ATLAS — AMPEL360E eWTW 070-079"
programme: "AMPEL360e Wide Tube-and-Wing Family (eWTW)"
atlas_group: "070-079"
status: "programme-controlled / normative"
standard: "S1000D Issue 4.2; Q+ ATLAS v2.1"
owner: "Amedeo Pelliccia / Q+"
created: 2026-05-14
applies_to: "All DMs in S1000D-CSDB/DMC/"
---

# CSDB Traceability to ATLAS — AMPEL360E eWTW 070-079

## 1. Purpose

This document maps each DMC family root to its parent ATLAS chapter and confirms the  
bidirectional traceability chain: ATLAS requirement → CSDB data module.

## 2. ATA / DMC to ATLAS Chapter Mapping

| DMC Family Root | ATA Title | ATLAS Chapter | ATLAS File |
| --------------- | --------- | ------------- | ---------- |
| `DMC-AMPEL360E-EWTW-070-xxx` | Hybrid-Electric Propulsion Architecture | ATLAS 070 | `070-000` – `070-090` |
| `DMC-AMPEL360E-EWTW-071-xxx` | Electric Motor / Generator Systems | ATLAS 071 | `071-000` – `071-090` |
| `DMC-AMPEL360E-EWTW-072-xxx` | Battery Energy Storage | ATLAS 072 | `072-000` – `072-090` |
| `DMC-AMPEL360E-EWTW-073-xxx` | Power Electronics and Conversion | ATLAS 073 | `073-000` – `073-090` |
| `DMC-AMPEL360E-EWTW-074-xxx` | Thermal Management Hybrid | ATLAS 074 | `074-000` – `074-090` |
| `DMC-AMPEL360E-EWTW-075-xxx` | Fuel Cell Integration | ATLAS 075 | `075-000` – `075-090` |
| `DMC-AMPEL360E-EWTW-076-xxx` | Hydrogen Fuel Storage Onboard | ATLAS 076 | `076-000` – `076-090` |
| `DMC-AMPEL360E-EWTW-077-xxx` | Hydrogen Distribution and Conditioning | ATLAS 077 | `077-000` – `077-090` |
| `DMC-AMPEL360E-EWTW-078-xxx` | SAF and Drop-In Compatibility | ATLAS 078 | `078-000` – `078-090` |
| `DMC-AMPEL360E-EWTW-079-xxx` | Energy Management System | ATLAS 079 | `079-000` – `079-090` |

## 3. Traceability Rules

### Rule TR-01 — Every DM traces to an ATLAS section
Every data module in this CSDB must be traceable to at least one ATLAS chapter section.  
The traceability link is recorded in the DMRL column `atlas_ref`.

### Rule TR-02 — ATLAS changes trigger DM review
When an ATLAS chapter is revised (status changes from `draft` to `active` or new revision issued),  
all linked DMs must undergo a **DM Impact Assessment** within 30 days.

### Rule TR-03 — 090 Traceability DMs are authoritative
The `-090` ATLAS files (e.g., `070-090-S1000D-CSDB-Mapping-and-Traceability.md`) are  
the authoritative cross-reference index for each chapter.

### Rule TR-04 — DMC 006-section DMs link to ATLAS -090
Each `06A_S1000D-CSDB-Mapping-and-Traceability/` folder in a DMC family root provides  
the S1000D-level view of traceability and must be kept consistent with the ATLAS `-090` file.

## 4. ATLAS Path Reference

ATLAS files for this group reside at:

```
Q+ATLANTIDE/000-099_ATLAS/070-079_Propulsion-Eco-Tech-e-Hibrido-Electrica/
```

Each ATA chapter has its own subfolder:

```
070_Propulsion-Eco-Tech-e-Hibrido-Electrica-General/
072_Battery-Energy-Storage/
073_Electric-Motor-Generator-Systems/
074_Thermal-Management-Hybrid/
075_Fuel-Cell-Integration/
076_Hydrogen-Fuel-Storage-Onboard/
077_Hydrogen-Distribution-and-Conditioning/
078_SAF-and-Drop-In-Compatibility/
079_Energy-Management-System/
```

## 5. Traceability Verification

Before CCB controlled release of any DM batch, run traceability audit:

1. Confirm every DM in the batch has a non-empty `atlas_ref` in the DMRL.
2. Confirm the referenced ATLAS file exists and its status is not `placeholder`.
3. Update the `06A` traceability DM for the affected chapter.
4. Record audit result in the CCB minutes.
