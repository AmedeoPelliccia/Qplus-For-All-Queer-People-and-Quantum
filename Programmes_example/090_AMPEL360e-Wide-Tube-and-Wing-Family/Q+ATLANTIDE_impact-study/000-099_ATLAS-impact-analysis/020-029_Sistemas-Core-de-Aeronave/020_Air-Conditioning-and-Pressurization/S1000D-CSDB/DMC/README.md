---
document_id: AMPEL360e-eWTW-S1000D-DMC-ATLAS020-README
title: "DMC Register — ATLAS-020 Air Conditioning and Pressurization — eWTW CSDB"
programme: "AMPEL360e Wide Tube-and-Wing Family"
programme_code: "090"
short_code: "eWTW"
framework: "S1000D"
atlas_node: "020_Air-Conditioning-and-Pressurization"
ata_alignment: "ATA 21 — Air Conditioning"
data_module_type: "Descriptive Data Module"
content_purpose: "System Description"
schema_family: "descriptive"
information_code: "040A"
status: "draft / programme-controlled-placeholder"
classification: "open-technical-programme-study"
owner: "Amedeo Pelliccia / Q+"
primary_language: "en"
created: 2026-05-09
no_aaa_rule: true
---

# DMC Register — ATLAS-020 Air Conditioning and Pressurization  
## AMPEL360e Wide Tube-and-Wing Family (eWTW) — S1000D CSDB

## 1. Purpose

This README is the **Data Module Requirement List (DMRL)**-style register for the **ATLAS 020 — Air Conditioning and Pressurization** descriptive data modules in the eWTW CSDB. Each file in this directory is a standalone S1000D descriptive data module retrieved by its unique Data Module Code (DMC).

---

## 2. DMRL Register

```yaml
dmrl:
  programme: "AMPEL360e Wide Tube-and-Wing Family"
  system: "ATLAS 020 — Air Conditioning and Pressurization"
  ata_alignment: "ATA 21 — Air Conditioning"
  data_module_type: "descriptive"
  purpose: "system description"
  information_code: "040A (programme-controlled placeholder)"
  issue: "001-00"

  data_modules:
    - dmc: "DMC-AMPEL360E-EWTW-020-000-00A-040A-D"
      title: "Air Conditioning and Pressurization — System Description"
      atlas_section: "020-000"
      ata_sns: "21-00-00"
      file: "DMC-AMPEL360E-EWTW-020-000-00A-040A-D_System-Description.xml"
      status: "draft"

    - dmc: "DMC-AMPEL360E-EWTW-020-010-00A-040A-D"
      title: "Compression — System Description"
      atlas_section: "020-010"
      ata_sns: "21-10-00"
      file: "DMC-AMPEL360E-EWTW-020-010-00A-040A-D_Compression-System-Description.xml"
      status: "draft"

    - dmc: "DMC-AMPEL360E-EWTW-020-020-00A-040A-D"
      title: "Distribution — System Description"
      atlas_section: "020-020"
      ata_sns: "21-20-00"
      file: "DMC-AMPEL360E-EWTW-020-020-00A-040A-D_Distribution-System-Description.xml"
      status: "draft"

    - dmc: "DMC-AMPEL360E-EWTW-020-030-00A-040A-D"
      title: "Pressurization Control — System Description"
      atlas_section: "020-030"
      ata_sns: "21-30-00"
      file: "DMC-AMPEL360E-EWTW-020-030-00A-040A-D_Pressurization-Control-System-Description.xml"
      status: "draft"

    - dmc: "DMC-AMPEL360E-EWTW-020-040-00A-040A-D"
      title: "Heating — System Description"
      atlas_section: "020-040"
      ata_sns: "21-40-00"
      file: "DMC-AMPEL360E-EWTW-020-040-00A-040A-D_Heating-System-Description.xml"
      status: "draft"

    - dmc: "DMC-AMPEL360E-EWTW-020-050-00A-040A-D"
      title: "Cooling — System Description"
      atlas_section: "020-050"
      ata_sns: "21-50-00"
      file: "DMC-AMPEL360E-EWTW-020-050-00A-040A-D_Cooling-System-Description.xml"
      status: "draft"

    - dmc: "DMC-AMPEL360E-EWTW-020-060-00A-040A-D"
      title: "Temperature Control — System Description"
      atlas_section: "020-060"
      ata_sns: "21-60-00"
      file: "DMC-AMPEL360E-EWTW-020-060-00A-040A-D_Temperature-Control-System-Description.xml"
      status: "draft"

    - dmc: "DMC-AMPEL360E-EWTW-020-070-00A-040A-D"
      title: "Moisture and Air Contaminant Control — System Description"
      atlas_section: "020-070"
      ata_sns: "21-70-00"
      file: "DMC-AMPEL360E-EWTW-020-070-00A-040A-D_Moisture-and-Air-Contaminant-Control-System-Description.xml"
      status: "draft"

    - dmc: "DMC-AMPEL360E-EWTW-020-080-00A-040A-D"
      title: "ECS Monitoring, Diagnostics and Control Interfaces — Description"
      atlas_section: "020-080"
      ata_sns: "21-80-00"
      file: "DMC-AMPEL360E-EWTW-020-080-00A-040A-D_ECS-Monitoring-Diagnostics-and-Control-Interfaces-Description.xml"
      status: "programme-controlled-extension"

    - dmc: "DMC-AMPEL360E-EWTW-020-090-00A-040A-D"
      title: "S1000D / CSDB Mapping and Traceability — Description"
      atlas_section: "020-090"
      ata_sns: "21-90-00"
      file: "DMC-AMPEL360E-EWTW-020-090-00A-040A-D_S1000D-CSDB-Mapping-and-Traceability-Description.xml"
      status: "programme-controlled-publication-and-traceability-extension"
```

---

## 3. File Inventory

| File | DMC | Title | ATA SNS | Status |
|---|---|---|---|---|
| `DMC-AMPEL360E-EWTW-020-000-00A-040A-D_System-Description.xml` | 020-000 | Air Conditioning and Pressurization — System Description | 21-00-00 | draft |
| `DMC-AMPEL360E-EWTW-020-010-00A-040A-D_Compression-System-Description.xml` | 020-010 | Compression — System Description | 21-10-00 | draft |
| `DMC-AMPEL360E-EWTW-020-020-00A-040A-D_Distribution-System-Description.xml` | 020-020 | Distribution — System Description | 21-20-00 | draft |
| `DMC-AMPEL360E-EWTW-020-030-00A-040A-D_Pressurization-Control-System-Description.xml` | 020-030 | Pressurization Control — System Description | 21-30-00 | draft |
| `DMC-AMPEL360E-EWTW-020-040-00A-040A-D_Heating-System-Description.xml` | 020-040 | Heating — System Description | 21-40-00 | draft |
| `DMC-AMPEL360E-EWTW-020-050-00A-040A-D_Cooling-System-Description.xml` | 020-050 | Cooling — System Description | 21-50-00 | draft |
| `DMC-AMPEL360E-EWTW-020-060-00A-040A-D_Temperature-Control-System-Description.xml` | 020-060 | Temperature Control — System Description | 21-60-00 | draft |
| `DMC-AMPEL360E-EWTW-020-070-00A-040A-D_Moisture-and-Air-Contaminant-Control-System-Description.xml` | 020-070 | Moisture and Air Contaminant Control — System Description | 21-70-00 | draft |
| `DMC-AMPEL360E-EWTW-020-080-00A-040A-D_ECS-Monitoring-Diagnostics-and-Control-Interfaces-Description.xml` | 020-080 | ECS Monitoring, Diagnostics and Control Interfaces — Description | 21-80-00 | programme-controlled-extension |
| `DMC-AMPEL360E-EWTW-020-090-00A-040A-D_S1000D-CSDB-Mapping-and-Traceability-Description.xml` | 020-090 | S1000D / CSDB Mapping and Traceability — Description | 21-90-00 | programme-controlled-publication-and-traceability-extension |

---

## 4. DMC Structure Note

All DMCs follow the programme-controlled format:

```text
DMC-{modelIdentCode}-{systemDiffCode}-{systemCode}-{subSys}{subSubSys}-{assyCode}-{infoCode}-{itemLocationCode}
    AMPEL360E        EWTW             020           0       00          00A        040A        D
```

| Segment | Value | Meaning |
|---|---|---|
| modelIdentCode | AMPEL360E | AMPEL360 programme family |
| systemDiffCode | EWTW | eWTW variant / system difference |
| systemCode | 020 | ATLAS node 020 / ATA 21 |
| subSystemCode | 0 | Sub-system (ATA tens digit) |
| subSubSystemCode | 00–90 | Sub-sub-system (ATA units) |
| assyCode | 00A | Assembly — programme default |
| infoCode | 040A | Description — programme-controlled placeholder |
| itemLocationCode | D | Programme-controlled |

---

## 5. Governance Boundary

All data modules in this folder are **programme-controlled placeholders**. Content is subject to BREX freeze, DMRL approval and CCB release before operational use.
