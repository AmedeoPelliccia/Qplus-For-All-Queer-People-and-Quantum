---
document_id: AMPEL360e-eWTW-S1000D-SNS-ATLAS020-README
title: "SNS — ATLAS-020 Air Conditioning and Pressurization — eWTW CSDB"
programme: "AMPEL360e Wide Tube-and-Wing Family"
short_code: "eWTW"
framework: "S1000D"
atlas_node: "020_Air-Conditioning-and-Pressurization"
ata_alignment: "ATA 21 — Air Conditioning"
folder_role: "Standard Numbering System (SNS) node for ATLAS-020"
status: "draft / programme-controlled-placeholder"
classification: "open-technical-programme-study"
owner: "Amedeo Pelliccia / Q+"
primary_language: "en"
created: 2026-05-09
no_aaa_rule: true
---

# SNS — ATLAS-020 Air Conditioning and Pressurization  
## AMPEL360e Wide Tube-and-Wing Family (eWTW) CSDB

## 1. Purpose

This folder defines the **Standard Numbering System (SNS)** node for **ATLAS 020 — Air Conditioning and Pressurization** within the eWTW CSDB. The SNS controls how system codes map to data module codes, ensuring consistent retrieval, applicability and reuse.

---

## 2. SNS / ATLAS / ATA Alignment

```yaml
sns_alignment:
  programme: "AMPEL360e Wide Tube-and-Wing Family"
  short_code: "eWTW"
  atlas_node: "020"
  atlas_title: "Air Conditioning and Pressurization"
  ata_chapter: "ATA 21 — Air Conditioning"
  s1000d_systemCode: "020"

  subsystem_mapping:
    - atlas_section: "020-000"
      ata_sns: "21-00-00"
      title: "General — Air Conditioning and Pressurization"
      subSystemCode: "0"
      subSubSystemCode: "00"

    - atlas_section: "020-010"
      ata_sns: "21-10-00"
      title: "Compression"
      subSystemCode: "0"
      subSubSystemCode: "10"

    - atlas_section: "020-020"
      ata_sns: "21-20-00"
      title: "Distribution"
      subSystemCode: "0"
      subSubSystemCode: "20"

    - atlas_section: "020-030"
      ata_sns: "21-30-00"
      title: "Pressurization Control"
      subSystemCode: "0"
      subSubSystemCode: "30"

    - atlas_section: "020-040"
      ata_sns: "21-40-00"
      title: "Heating"
      subSystemCode: "0"
      subSubSystemCode: "40"

    - atlas_section: "020-050"
      ata_sns: "21-50-00"
      title: "Cooling"
      subSystemCode: "0"
      subSubSystemCode: "50"

    - atlas_section: "020-060"
      ata_sns: "21-60-00"
      title: "Temperature Control"
      subSystemCode: "0"
      subSubSystemCode: "60"

    - atlas_section: "020-070"
      ata_sns: "21-70-00"
      title: "Moisture and Air Contaminant Control"
      subSystemCode: "0"
      subSubSystemCode: "70"

    - atlas_section: "020-080"
      ata_sns: "21-80-00"
      title: "ECS Monitoring, Diagnostics and Control Interfaces"
      subSystemCode: "0"
      subSubSystemCode: "80"
      status_note: "programme-controlled-extension"

    - atlas_section: "020-090"
      ata_sns: "21-90-00"
      title: "S1000D / CSDB Mapping and Traceability"
      subSystemCode: "0"
      subSubSystemCode: "90"
      status_note: "programme-controlled-publication-and-traceability-extension"
```

---

## 3. SNS Governance Note

The mapping above is a programme-controlled draft. The ATLAS node numbering (020-xxx) is aligned to ATA chapter 21 for the eWTW programme. Deviations from standard ATA 21 numbering in the 080 and 090 sections are programme-controlled extensions and must be formally registered in the BREX before production issue.

---

## 4. Q-Division Ownership

```yaml
q_division_ownership:
  primary: "Q-AIR"
  support:
    - "Q-DATAGOV (SNS governance, BREX, CSDB)"
    - "Q-MECHANICS (ECS mechanical interfaces)"
    - "Q-GREENTECH (thermal management, energy coupling)"
    - "Q-GROUND (maintenance, ground servicing)"
```
