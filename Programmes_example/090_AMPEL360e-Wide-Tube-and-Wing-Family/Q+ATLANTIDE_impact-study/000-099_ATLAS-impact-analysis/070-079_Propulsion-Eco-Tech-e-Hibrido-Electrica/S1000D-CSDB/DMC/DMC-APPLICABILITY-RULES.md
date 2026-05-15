---
document_id: DMC-APPLICABILITY-RULES
title: "Applicability Rules — AMPEL360E eWTW CSDB"
programme: "AMPEL360e Wide Tube-and-Wing Family (eWTW)"
atlas_group: "070-079"
status: "programme-controlled / normative"
standard: "S1000D Issue 4.2 §7"
owner: "Amedeo Pelliccia / Q+"
created: 2026-05-14
applies_to: "All DMs in S1000D-CSDB/DMC/"
---

# Applicability Rules — AMPEL360E eWTW CSDB

## 1. Applicability Model

Applicability is managed at DM level using the S1000D `<applic>` / `<evaluate>` mechanism.

### Programme Baseline Configurations

| Config Code | Description |
| ----------- | ----------- |
| `EWTW-A` | Standard hybrid-electric (battery + gas turbine) |
| `EWTW-B` | Hydrogen fuel-cell variant (PEMFC + battery buffer) |
| `EWTW-C` | Full-electric development prototype (battery only) |
| `EWTW-ALL` | Common to all configurations (default for scaffold stubs) |

## 2. DM Applicability Coding

### All-configurations default (scaffold stubs)

```xml
<applic>
  <displayText>
    <simplePara>AMPEL360E eWTW All Configurations</simplePara>
  </displayText>
</applic>
```

### Configuration-specific

```xml
<applic>
  <evaluate andOr="or">
    <assert applicPropertyIdent="config" applicPropertyType="prodattr"
            applicPropertyValues="EWTW-A EWTW-B"/>
  </evaluate>
</applic>
```

## 3. Applicability Property Registry

| Property Ident | Type | Values | Description |
| -------------- | ---- | ------ | ----------- |
| `config` | `prodattr` | `EWTW-A`, `EWTW-B`, `EWTW-C` | Aircraft configuration |
| `propulsion` | `prodattr` | `HYB`, `FC`, `EL` | Propulsion type |
| `cert_basis` | `condition` | `CS-25`, `SC-VTOL` | Certification basis |
| `dal` | `condition` | `A`, `B`, `C`, `D` | DO-178C/DO-254 DAL |

## 4. Rules

1. All scaffold stubs MUST carry `EWTW-ALL` applicability until content authoring confirms configuration scope.
2. Configuration-specific DMs MUST be registered in the DMRL with the applicability property values.
3. Applicability annotations must be validated by the BREX rule `BREX-APPLIC-01` before controlled release.
4. Any DM applicable to only one configuration must be reviewed by the CCB for potential commonisation.
