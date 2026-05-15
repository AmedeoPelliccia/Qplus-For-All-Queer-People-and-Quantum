---
document_id: DMC-CONTENT-TEMPLATE
title: "S1000D Data Module Content Template — AMPEL360E eWTW 070-079"
programme: "AMPEL360e Wide Tube-and-Wing Family (eWTW)"
atlas_group: "070-079 Propulsión Eco-Tech e Híbrido-Eléctrica"
status: "programme-controlled / normative"
standard: "S1000D Issue 4.2"
owner: "Amedeo Pelliccia / Q+"
created: 2026-05-14
applies_to: "All DMC folders under S1000D-CSDB/DMC/"
---

# S1000D Data Module Content Template

## Purpose

This template defines the minimum mandatory XML structure for every S1000D data module stub in the AMPEL360E eWTW CSDB.  
All authors must use this template as their starting point before populating content.

## Mandatory `<dmodule>` Skeleton

```xml
<?xml version="1.0" encoding="UTF-8"?>
<dmodule xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation=
    "http://www.s1000d.org/S1000DIssue4.2/xml_schema_flat/<SCHEMA>.xsd">

  <identAndStatusSection>
    <dmAddress>
      <dmIdent>
        <dmCode
          modelIdentCode="AMPEL360E"
          systemDiffCode="EWTW"
          systemCode="<ATA>"
          subSystemCode="<SUB>"
          subSubSystemCode="<SUBSUB>"
          assyCode="<ASSY>"
          disassyCode="<DISASSY>"
          disassyCodeVariant="<VARIANT>"
          infoCode="<IC>"
          infoCodeVariant="<ICV>"
          itemLocationCode="D"/>
        <issueInfo issueNumber="001" inWork="00"/>
        <language languageIsoCode="en" countryIsoCode="US"/>
      </dmIdent>
      <dmAddressItems>
        <issueDate year="YYYY" month="MM" day="DD"/>
        <dmTitle>
          <techName><!-- System / component name --></techName>
          <infoName><!-- Info code descriptive title --></infoName>
        </dmTitle>
      </dmAddressItems>
    </dmAddress>
    <dmStatus issueType="new">
      <security securityClassification="01"/>
      <responsiblePartnerCompany enterpriseCode="AMPEL">
        <enterpriseName>AMPEL / Q+</enterpriseName>
      </responsiblePartnerCompany>
      <originator enterpriseCode="AMPEL">
        <enterpriseName>AMPEL / Q+</enterpriseName>
      </originator>
      <applic>
        <displayText>
          <simplePara>AMPEL360E eWTW All Configurations</simplePara>
        </displayText>
      </applic>
      <brexDmRef>
        <dmRef><dmRefIdent><dmCode
          modelIdentCode="AMPEL360E" systemDiffCode="EWTW"
          systemCode="<ATA>" subSystemCode="0" subSubSystemCode="0"
          assyCode="00" disassyCode="A" disassyCodeVariant="00"
          infoCode="022" infoCodeVariant="A" itemLocationCode="D"/>
        </dmRefIdent></dmRef>
      </brexDmRef>
      <qualityAssurance><unverified/></qualityAssurance>
    </dmStatus>
  </identAndStatusSection>

  <content>
    <!-- Author content here following applicable XSD schema -->
  </content>

</dmodule>
```

## Schema Selection by Info Code Category

| Info Code Range | Schema |
| --------------- | ------ |
| 040–049, 300–310, 400, 900, 940, 941 | `descript.xsd` |
| 100–109, 320, 420 | `proc.xsd` |
| 400, C20 | `fault.xsd` |
| C00, C10 | `comrep.xsd` |

## Checklist Before Submission

- [ ] `dmCode` attributes match DMRL entry
- [ ] `issueDate` set to authoring date
- [ ] `brexDmRef` points to correct BREX DM for the chapter
- [ ] Content validated against XSD schema
- [ ] Applicability cross-checked with SNS baseline
- [ ] DMRL status updated to `"authored"`
