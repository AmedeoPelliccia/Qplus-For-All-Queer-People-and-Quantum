---
document_id: DMC-BREX-RULES
title: "BREX Rules Summary — AMPEL360E eWTW 070-079 CSDB"
programme: "AMPEL360e Wide Tube-and-Wing Family (eWTW)"
atlas_group: "070-079"
status: "programme-controlled / normative"
standard: "S1000D Issue 4.2 §3.9"
owner: "Amedeo Pelliccia / Q+"
created: 2026-05-14
applies_to: "All DMs in S1000D-CSDB/DMC/"
---

# BREX Rules Summary — AMPEL360E eWTW 070-079

## 1. BREX DM References by Chapter

| ATA Chapter | BREX DM Reference | Status |
| ----------- | ----------------- | ------ |
| 070 (Hybrid Propulsion Architecture) | `DMC-AMPEL360E-EWTW-070-000-00A-022A-D` | scaffold |
| 072 (Battery Energy Storage) | `BREX-072-v1` | active |
| 073 (Electric Motor / Generator) | `BREX-073-v1` | active |
| 074 (Thermal Management) | `BREX-074-v1` | active |
| 075 (Fuel Cell Integration) | `BREX-075-v1` | active |
| 076 (Hydrogen Fuel Storage) | `BREX-076-v1` | active |
| 077 (Hydrogen Distribution) | `BREX-077-v1` | active |
| 078 (SAF Compatibility) | `BREX-078-v1` | active |
| 079 (Energy Management System) | `BREX-079-v1` | active |

## 2. Key BREX Constraints

### BREX-APPLIC-01
All DMs must include a valid `<applic>` element. Bare scaffold stubs default to `EWTW-ALL`.

### BREX-DMCODE-01
`dmCode` attributes must match exactly one DMRL entry. No orphaned DMs permitted in controlled release.

### BREX-IC-01
`infoCode` must be drawn from the `DMC-INFOCODE-BASELINE.md` registry. Non-baseline info codes require CCB approval.

### BREX-LANG-01
`languageIsoCode="en"` and `countryIsoCode="US"` are mandatory for all primary DMs.  
Translation DMs (countryIsoCode ≠ "US") must reference the source DM via `<derivativeClassification>`.

### BREX-SCHEMA-01
Each DM must declare the correct XSD schema URL in `xsi:noNamespaceSchemaLocation`.  
Valid bases: `descript.xsd`, `proc.xsd`, `fault.xsd`, `comrep.xsd`, `ipd.xsd`, `proced.xsd`.

### BREX-SAFETY-01
DMs with safety-critical content (DAL A/B systems) must include `<warningRef>` pointing to the applicable warning DM before controlled release.

## 3. BREX Validation Tool

All DMs must be validated using `s1kd-brexcheck` against the chapter BREX DM before submission to CCB.

```bash
s1kd-brexcheck -b DMC-AMPEL360E-EWTW-070-000-00A-022A-D.xml \
               DMC-AMPEL360E-EWTW-070-000-<section>-<ic>-D.xml
```
