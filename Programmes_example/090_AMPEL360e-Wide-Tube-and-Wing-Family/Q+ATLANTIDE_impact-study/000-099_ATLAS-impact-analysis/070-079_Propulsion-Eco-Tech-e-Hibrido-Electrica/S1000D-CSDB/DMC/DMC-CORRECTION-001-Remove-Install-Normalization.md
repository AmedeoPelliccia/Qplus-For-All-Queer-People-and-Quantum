---
document_id: DMC-CORRECTION-001-Remove-Install-Normalization
title: "Correction Notice 001 — Removal/Installation Info-Code Normalization"
correction_ref: "CORR-EWTW-070-001"
programme: "AMPEL360E eWTW 070-079"
status: "approved / normative"
standard: "S1000D Issue 4.2"
owner: "Amedeo Pelliccia / Q+"
effective_date: 2026-05-14
applies_to: "All DMC folders — removal and installation data modules"
---

# Correction 001 — Removal/Installation Info-Code Normalization

## Summary

Early scaffold iterations used inconsistent info codes for component removal and installation procedures.  
This correction establishes the canonical mapping and requires all affected stubs to be updated before first controlled release.

## Canonical Info-Code Mapping

| Procedure Type | Correct Info Code | XSD Schema | Previous (incorrect) |
| -------------- | ----------------- | ---------- | --------------------- |
| Component Removal | `520A` | `proc.xsd` | `510A`, `530A` (mixed) |
| Component Installation | `710A` | `proc.xsd` | `720A`, `700A` (mixed) |
| Removal with Caution | `520B` | `proc.xsd` | `520A` (no variant) |
| Installation with Caution | `710B` | `proc.xsd` | `710A` (no variant) |

## Affected DMC Families

All DMC folders in `S1000D-CSDB/DMC/` that contain removal or installation procedure stubs:

- `DMC-AMPEL360E-EWTW-072-xxx` (Battery Energy Storage)
- `DMC-AMPEL360E-EWTW-073-xxx` (Electric Motor / Generator)
- `DMC-AMPEL360E-EWTW-074-xxx` (Thermal Management)
- `DMC-AMPEL360E-EWTW-075-xxx` (Fuel Cell Integration)
- `DMC-AMPEL360E-EWTW-076-xxx` (Hydrogen Fuel Storage)
- `DMC-AMPEL360E-EWTW-077-xxx` (Hydrogen Distribution)
- `DMC-AMPEL360E-EWTW-078-xxx` (SAF Compatibility)
- `DMC-AMPEL360E-EWTW-079-xxx` (Energy Management)

## Action Required

For each affected stub before CCB-controlled release:

1. Verify `infoCode` attribute in `<dmCode>` matches canonical table above.
2. Update filename to reflect corrected info code.
3. Update DMRL entry accordingly.
4. Record correction in `DMC-CORRECTION-001` change log below.

## Change Log

| Date | DM Reference | Old IC | New IC | Author |
| ---- | ------------ | ------- | ------- | ------ |
| 2026-05-14 | (scaffold) | (mixed) | normalized per table | Amedeo Pelliccia |
