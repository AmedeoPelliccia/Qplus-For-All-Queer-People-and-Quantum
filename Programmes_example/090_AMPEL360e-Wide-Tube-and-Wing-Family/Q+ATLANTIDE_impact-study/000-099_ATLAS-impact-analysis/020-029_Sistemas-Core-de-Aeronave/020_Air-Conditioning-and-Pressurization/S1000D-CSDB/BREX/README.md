---
document_id: AMPEL360e-eWTW-S1000D-CSDB-BREX-README
title: "BREX — Business Rules EXchange — AMPEL360e eWTW CSDB"
programme: "AMPEL360e Wide Tube-and-Wing Family"
short_code: "eWTW"
framework: "S1000D"
folder_role: "Business Rules EXchange (BREX) placeholder"
status: "pending — BREX freeze required before production release"
classification: "open-technical-programme-study"
owner: "Amedeo Pelliccia / Q+"
primary_language: "en"
created: 2026-05-09
no_aaa_rule: true
---

# BREX — Business Rules EXchange  
## AMPEL360e Wide Tube-and-Wing Family (eWTW) CSDB

## 1. Purpose

This folder will contain the **Business Rules EXchange (BREX)** data modules for the eWTW programme CSDB. BREX documents define the authoring constraints, allowed elements, SNS rules, information code policies and schema restrictions that govern all data modules in this CSDB.

---

## 2. BREX Role in S1000D

A BREX data module is a special S1000D data module (infoCode 022) that:

- Specifies which XML elements and attributes are permitted or forbidden
- Controls the allowed Standard Numbering System (SNS) structure
- Defines allowed information code values and their variants
- Establishes applicability, security classification and issue control rules
- Is referenced by every data module in the CSDB via `brexDmRef`

All data modules in this CSDB include a forward reference to the programme BREX:

```xml
<brexDmRef>
  <dmRef>
    <dmRefIdent>
      <dmCode modelIdentCode="AMPEL360E"
              systemDiffCode="EWTW"
              systemCode="000"
              subSystemCode="0"
              subSubSystemCode="00"
              assyCode="00A"
              disassyCode="00"
              disassyCodeVariant="A"
              infoCode="022"
              infoCodeVariant="A"
              itemLocationCode="D"/>
    </dmRefIdent>
  </dmRef>
</brexDmRef>
```

---

## 3. Pending Actions

```yaml
brex_pending_actions:
  - action: "Define SNS hierarchy for ATLAS-EWTW system codes"
    responsible: "Q-DATAGOV"
    status: "pending"

  - action: "Freeze information code policy — especially 040A programme extension"
    responsible: "Q-DATAGOV + programme CCB"
    status: "pending"

  - action: "Author BREX data module DMC-AMPEL360E-EWTW-000-000-00A-022A-D"
    responsible: "Q-DATAGOV"
    status: "pending"

  - action: "Validate all CSDB data modules against frozen BREX"
    responsible: "Q-DATAGOV + Q-AIR"
    status: "pending — awaiting BREX freeze"
```

---

## 4. Information Code Policy Note

The provisional information code **040A** used in the current descriptive data modules is a programme-controlled placeholder:

```yaml
information_code_policy:
  proposed_info_code: "040A"
  meaning: "programme-controlled descriptive system description placeholder"
  note: >
    Final infoCode must be frozen by project BREX / SNS / DMRL rules.
    Standard S1000D infoCode 040 = Description (content purpose aligned).
    The 'A' variant is reserved pending BREX CCB approval.
```

---

## 5. Governance Boundary

This folder is a **placeholder**. No BREX data module has been authored or approved. Content in this CSDB must not be used in production publications until a BREX data module has been authored, reviewed and formally issued by the programme Configuration Control Board.
