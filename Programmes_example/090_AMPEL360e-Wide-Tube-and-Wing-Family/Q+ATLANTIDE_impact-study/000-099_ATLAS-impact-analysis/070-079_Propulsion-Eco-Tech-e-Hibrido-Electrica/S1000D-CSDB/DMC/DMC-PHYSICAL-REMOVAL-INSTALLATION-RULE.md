---
document_id: DMC-PHYSICAL-REMOVAL-INSTALLATION-RULE
title: "Physical Removal / Installation Rule — AMPEL360E eWTW 070-079"
programme: "AMPEL360e Wide Tube-and-Wing Family (eWTW)"
atlas_group: "070-079"
status: "programme-controlled / normative"
standard: "S1000D Issue 4.2; ATA iSpec 2200"
owner: "Amedeo Pelliccia / Q+"
created: 2026-05-14
applies_to: "All removal and installation DMs in S1000D-CSDB/DMC/"
---

# Physical Removal / Installation Rule

## 1. Scope

This rule governs the authoring and approval of all data modules covering the physical removal  
and installation of line-replaceable units (LRUs) and shop-replaceable units (SRUs) within  
the AMPEL360E eWTW 070-079 propulsion and energy systems.

## 2. Mandatory Pre-Conditions

Every removal DM (`IC 520x`) must include the following `<preliminaryRqmts>` sub-elements:

- `<reqCondGroup>` — aircraft power-down state, circuit-breaker open list
- `<reqPersons>` — minimum qualified persons (e.g., `"1 × Licensed Aircraft Maintenance Engineer"`)
- `<reqTechInfoGroup>` — cross-references to applicable AMM / CMM
- `<reqSupportEquips>` — required GSE, lifting fixtures, torque tools
- `<reqSupplies>` — consumables (O-rings, locking wire, sealant types)
- `<reqSpares>` — replacement parts with Part Number and IPC reference
- `<reqSafety>` — arc-flash PPE for HVDC circuits (≥ 270 V DC), LH₂ cryogenic PPE

## 3. Mandatory Post-Conditions

Every installation DM (`IC 710x`) must include `<closeRqmts>` covering:

- Torque values and sequence for fasteners
- Leak check or pressure test (where applicable)
- Continuity / insulation test for electrical harnesses
- Functional test DM cross-reference (`IC 320A`)
- Log / maintenance record entry requirements

## 4. HVDC and Cryogenic Safety Requirements

Due to the presence of **HVDC circuits (270–800 V DC)** and **cryogenic LH₂ systems** in the  
070-079 propulsion group, the following additional requirements apply:

| System | Safety Requirement |
| ------ | ------------------ |
| HVDC ≥ 270 V (Battery, FCSS, PMSG) | Arc-flash boundary calculation per NFPA 70E; isolation confirmed by HVDC interlock before touch |
| LH₂ / cryogenic (-253 °C) | Cryo-PPE, N₂ purge verification, BOV open before line break |
| H₂ fuel (GH₂ / LH₂) | H₂ sensor reading <10% LEL before removal; ATEX zone clearance |
| High-speed rotating parts (PMSG / EP motors) | LOTO verified; rotational coast-down complete |

## 5. Info Code Normalisation

See `DMC-CORRECTION-001-Remove-Install-Normalization.md` for canonical info code assignments.  
IC `520A`/`520B` = Removal; IC `710A`/`710B` = Installation.  
All other removal/installation info codes are **not approved** without CCB waiver.

## 6. Review and Approval Gate

All removal and installation DMs must pass the following gate before controlled issue:

- [ ] Technical review by Systems Engineering (SE)
- [ ] Safety review by Safety & Airworthiness (S&A)
- [ ] BREX validation (`s1kd-brexcheck`)
- [ ] CCB approval and DMRL status update to `"approved"`
