---
document_id: DMC-NAMING-CONVENTION
title: "DM Naming Convention — AMPEL360E eWTW 070-079 CSDB"
programme: "AMPEL360e Wide Tube-and-Wing Family (eWTW)"
atlas_group: "070-079"
status: "programme-controlled / normative"
standard: "S1000D Issue 4.2 §3.8.1"
owner: "Amedeo Pelliccia / Q+"
created: 2026-05-14
applies_to: "All DMC folders and XML files in S1000D-CSDB/DMC/"
---

# DM Naming Convention — AMPEL360E eWTW 070-079

## 1. DMC String Format

```
DMC-<modelIdentCode>-<systemDiffCode>-<systemCode>-<subSystemCode><subSubSystemCode>-<assyCode>-<disassyCode><disassyCodeVariant>-<infoCode><infoCodeVariant>-<itemLocationCode>
```

| Field | Length | Value (this CSDB) | Description |
| ----- | ------ | ----------------- | ----------- |
| `modelIdentCode` | 2–14 | `AMPEL360E` | Model identifier |
| `systemDiffCode` | 1–4 | `EWTW` | System differentiator |
| `systemCode` | 3 | `070`–`079` | ATA chapter |
| `subSystemCode` | 1 | `0` | Sub-system (use `0` unless sub-divided) |
| `subSubSystemCode` | 1 | `0` | Sub-sub-system |
| `assyCode` | 2 | `00`–`09` | Assembly (section variant, e.g. `00`=general) |
| `disassyCode` | 2 | `00`–`99` | Disassembly code |
| `disassyCodeVariant` | 1 | `A`–`Z` | Variant letter |
| `infoCode` | 3 | per baseline | Info code |
| `infoCodeVariant` | 1 | `A`–`Z` | Variant |
| `itemLocationCode` | 1 | `D` | Document location (`D`=document) |

## 2. File Naming

XML stub files follow the DMC string with an underscore-separated human-readable suffix:

```
DMC-AMPEL360E-EWTW-<systemCode>-000-<assyCode>-<IC><ICV>-D_<Short-Title>.xml
```

**Examples:**
```
DMC-AMPEL360E-EWTW-070-000-00A-040A-D_System-Description.xml
DMC-AMPEL360E-EWTW-070-000-00A-100A-D_Operation.xml
DMC-AMPEL360E-EWTW-072-000-00A-520A-D_Battery-Module-Removal.xml
```

## 3. Folder Naming

Each DMC family root folder is named after the DMC string prefix (without info code):

```
DMC-<modelIdentCode>-<systemDiffCode>-<systemCode>-<subCode>/
```

**Examples:**
```
DMC-AMPEL360E-EWTW-070-000/
DMC-AMPEL360E-EWTW-072-060/
```

Sub-folders within a DMC family root are named by disassembly code + topic:

```
<assyCode><disassyCodeVariant>_<Topic-Title>/
```

**Example:**
```
00A_Hybrid-Electric-Architecture-Overview/
01A_Propulsion-Architecture-and-Energy-Flow/
```

Info-code sub-folders within a section follow:

```
<infoCode>_<category>/
```

**Example:**
```
040_descriptive/
100_operation/
400_fault-reports-and-isolation-procedures/
```

## 4. README Files

Every folder level must contain a `README.md` that:
- Lists the DMC string(s) covered
- Provides an info-code breakdown table
- States the current `status` of content

## 5. Reserved Characters

The following characters must **not** appear in any file or folder name:
`/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`, `#`, `&`, `%`
