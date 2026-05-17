---
document_id: "QATL-ATLAS-1000-ATLAS-000-009-00-007-050-CENTRE-OF-GRAVITY-CALCULATION-GENERAL"
title: "ATLAS 000-009 · 00.007.050 — Centre of Gravity Calculation General"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../../README.md
parent_section_doc: ../../README.md
parent_subsection_doc: ./README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "000-009"
section: "00"
section_title: "Información General y Servicio"
subsection: "007"
subsection_title: "Leveling and Weighing General"
subsubject: "050"
subsubject_title: "Centre of Gravity Calculation General"
subsubject_file: "007-050-Centre-of-Gravity-Calculation-General.md"
subsubject_link: "./007-050-Centre-of-Gravity-Calculation-General.md"
primary_q_division: Q-GROUND
support_q_divisions: [Q-DATAGOV, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
s1000d_applicability: "S1000D-CSDB-compatible"
ata_reference: "ATA 08"
programme: "[PROGRAMME-AIRCRAFT] programme-defined aircraft configuration Family"
short_code: "[PROGRAMME-VARIANT]"
created: "2026-05-11"
updated: "2026-05-11"
review_status: "to-be-reviewed-by-system-expert"
standard_scope: agnostic
programme_specific: false
---

![DRAFT](https://img.shields.io/badge/DRAFT-yellow)
![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)

# ATLAS 000-009 · Section 00 · Subsection 007 · 050 — Centre of Gravity Calculation General

## 0. Hyperlink Policy

All hyperlinks within this document use **relative paths** from the current file location. Cross-subsection links navigate to sibling files within `./` (same folder), to the subsection index at [`./README.md`](./README.md), and to parent indexes at `../`, `../../`, and `../../../`. Absolute URLs are used only for external standards references.

---

## 1. Purpose

Documents the centre of gravity (CG) calculation methodology for the programme-defined aircraft type. Covers the reference datum location, CG calculation from load cell readings, CG limits (forward and aft), and the relationship between the measured CG and the operational CG envelope used in load and balance calculations.

This document is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline. It applies to the [[PROGRAMME-AIRCRAFT] programme-defined aircraft configuration Family](../../../../[PROGRAMME-PATH]/090_[PROGRAMME-AIRCRAFT]-Wide-Tube-and-Wing-Family/) programme, **[PROGRAMME-VARIANT]** configuration.

---

## 2. Applicability

| Applicability Item | Value | Status |
|---|---|---|
| Programme | [PROGRAMME-AIRCRAFT] programme-defined aircraft configuration Family | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| Short code | [PROGRAMME-VARIANT] | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| Architecture register | Q+ATLANTIDE | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| ATLAS band | 000-099_ATLAS | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| ATA reference | ATA 08 | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| S1000D SNS | 007-050-00 | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| S1000D compatibility | S1000D-CSDB-compatible | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |

---

## 3. System / Function Overview

The **Centre of Gravity Calculation General** node defines the C-of-G reference geometry, calculation methodology, and applicable limits for the programme-defined aircraft type. The C-of-G reference datum is located at FS 0 (the nose reference plane); the MAC (Mean Aerodynamic Chord) reference is 6.2 m, with MAC leading edge at FS 620.0. The [PROGRAMME-VARIANT] C-of-G envelope (from the Aircraft Flight Manual, AFM Chapter 6) is: forward limit 17% MAC (FS 725.4); aft limit 38% MAC (FS 855.6); lateral limit ±0.12 m from BL 0.

The [PROGRAMME-VARIANT]-specific complication is that the HVDC battery pack (lower centre fuselage, FS 680–FS 800) is a major fixed mass at a known station, but the battery SoC varies in flight (cells discharge, reducing mass). This introduces a small dynamic C-of-G shift during flight: ΔFS_CG ≈ 0.06 m forward per full discharge cycle (conservative bound per structural loads analysis Q-LOADS-001). This shift is pre-computed in the [PROGRAMME-VARIANT] Mass and Balance system (MMBS) and accounted for in the certified AFM C-of-G envelope. The MMBS (DO-178C DAL B) ingests live BMS SoC and passenger/cargo loading data to compute in-flight C-of-G predictions displayed to the crew on the EFB mass-and-balance page.

---

## 4. Scope

### 4.1 Included

This document includes:

- controlled definition of the centre of gravity calculation general scope;
- architecture boundaries and interface definitions;
- programme-defined aircraft type-specific implementation notes;
- S1000D/CSDB mapping requirements;
- lifecycle evidence requirements.

### 4.2 Excluded

This document excludes:

- supplier-proprietary internal design data;
- final certification compliance statements;
- detailed maintenance procedures (pending DMRL assignment);
- final illustrated parts data (pending CSDB release).

---

## 5. Architecture Description ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)

The **Centre of Gravity Calculation General** architecture is organized around controlled interfaces, deterministic function allocation, and maintainable component boundaries within the 000-009 General Information and Service section of the programme-defined aircraft type programme.

---

## 6. Functional Breakdown ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)

| Ref | Function | Description | Primary Interface | Status |
|---:|---|---|---|---|
| F-001 | Core Function | Primary controlled function for centre of gravity calculation general. | [Interfaces](#10-interfaces) | ![TBD](https://img.shields.io/badge/TBD-red) |
| F-002 | Support Function | Supporting controlled function. | [Interfaces](#10-interfaces) | ![TBD](https://img.shields.io/badge/TBD-red) |
| F-003 | Monitoring | Captures status, faults, and maintenance data. | [CMS / BITE](#12-monitoring-and-diagnostics) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| F-004 | Traceability | Links architecture, requirements, and S1000D content. | [CSDB / DMRL](#14-s1000d--csdb-mapping) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |

---

## 7. Mermaid — System Context Diagram

```mermaid
flowchart LR
    A[Aircraft-Level Function] --> B[Centre of Gravity Calculation General]
    B --> C[Power / Data Interface]
    B --> D[Ground Interface]
    B --> E[Maintenance Interface]
    E --> F[CMS / BITE]
    F --> G[S1000D / CSDB Evidence]
```

*Diagram 1 — System context for Centre of Gravity Calculation General.*

---

## 8. Mermaid — Internal Functional Architecture

```mermaid
flowchart TB
    SYS[Centre of Gravity Calculation General] --> F1[Core Function]
    SYS --> F2[Support Function]
    SYS --> CTRL[Control Logic]
    SYS --> MON[Monitoring and Diagnostics]
    MON --> CMS[CMS / BITE]
    CTRL --> IMA[IMA / Controller Interface]
```

*Diagram 2 — Internal functional architecture for Centre of Gravity Calculation General.*

---

## 9. Mermaid — Lifecycle Traceability

```mermaid
flowchart LR
    LC02[LC02 Requirements] --> LC03[LC03 Architecture]
    LC03 --> LC05[LC05 Detailed Design]
    LC05 --> LC06[LC06 Verification Planning]
    LC06 --> LC10[LC10 Certification]
    LC10 --> LC11[LC11 Operation]
    LC11 --> LC12[LC12 Maintenance]
    LC03 --> CSDB[S1000D / CSDB]
    LC05 --> DMRL[DMRL]
    LC06 --> EVID[Evidence Records]
```

*Diagram 3 — Lifecycle traceability.*

---

## 10. Interfaces ![TBD](https://img.shields.io/badge/TBD-red)

| Interface Type | Connected System | Description | Status |
|---|---|---|---|
| Electrical power | HVDC Bus / GPU | Power supply interface | ![TBD](https://img.shields.io/badge/TBD-red) |
| Data / control | IMA / CMS / AMT | Command and monitoring interface | ![TBD](https://img.shields.io/badge/TBD-red) |
| Mechanical | Structure / GSE | Mounting and access interface | ![TBD](https://img.shields.io/badge/TBD-red) |
| Maintenance | CSDB / IETP | Technician-facing access and procedure boundary | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |

---

## 11. Operating Modes ![DRAFT](https://img.shields.io/badge/DRAFT-yellow)

| Mode | Description | Entry Condition | Exit Condition | Status |
|---|---|---|---|---|
| Normal | System operates within nominal limits. | Aircraft powered and system enabled. | Shutdown or fault. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| Degraded | Reduced function or redundancy. | Fault detected. | Recovery or maintenance action. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| Maintenance | Configured for inspection or servicing. | Authorized maintenance action. | Operational check complete. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| Failure / Safe State | Protective state to prevent unsafe operation. | Fault threshold exceeded. | Reset or repair. | ![TBD](https://img.shields.io/badge/TBD-red) |

---

## 12. Monitoring and Diagnostics ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)

The system shall provide sufficient monitoring to support safe operation, maintenance troubleshooting, and lifecycle evidence capture. Diagnostic data shall be mapped to the relevant S1000D/CSDB fault isolation and maintenance data modules.

---

## 13. Maintenance Concept ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)

The maintenance concept shall support modular inspection, fault isolation, removal, installation, and return-to-service verification. Maintenance procedures shall remain provisional until validated against the applicable DMRL, BREX, and task validation records.

---

## 14. S1000D / CSDB Mapping ![TBD](https://img.shields.io/badge/TBD-red)

| S1000D Element | Controlled Value | Status |
|---|---|---|
| Model ident code | `[PROGRAMME-AIRCRAFT]` | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| System diff code | `[PROGRAMME-VARIANT]` | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| System code | `007` | ![TBD](https://img.shields.io/badge/TBD-red) |
| Sub-system code | `050` | ![TBD](https://img.shields.io/badge/TBD-red) |
| DMC prefix | `DMC-<PROGRAMME>-<VARIANT>-007-050` | ![TBD](https://img.shields.io/badge/TBD-red) |
| Info codes | `040 / 300 / 400 / 520 / 720 / 941` | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |

---

## 15. Footprints ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)

### 15.1 Physical Footprint

| Footprint Item | Description | Status |
|---|---|---|
| Installation zone | TBD | ![TBD](https://img.shields.io/badge/TBD-red) |
| Access panels | TBD | ![TBD](https://img.shields.io/badge/TBD-red) |

### 15.2 Data Footprint

| Footprint Item | Description | Status |
|---|---|---|
| Configuration records | Part number, serial number, effectivity | ![TBD](https://img.shields.io/badge/TBD-red) |
| Evidence records | Test, inspection, compliance records | ![TBD](https://img.shields.io/badge/TBD-red) |
| CSDB records | DMCs, ICNs, BREX, applicability | ![TBD](https://img.shields.io/badge/TBD-red) |

---

## 16. Safety and Certification Considerations ![TBD](https://img.shields.io/badge/TBD-red)

Final safety classification shall remain **TBD** until reviewed against the applicable FHA, PSSA, SSA, and certification basis (EASA CS-25 Amendment 27+).

---

## 17. Verification and Validation ![DRAFT](https://img.shields.io/badge/DRAFT-yellow)

| Verification Method | Description | Evidence | Status |
|---|---|---|---|
| Analysis | Engineering calculation or safety analysis. | Analysis report | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| Inspection | Physical or visual verification. | Inspection record | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| Test | Functional or integration test. | Test report | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |

---

## 18. Glossary of Terms and Acronyms

| Term | Meaning | Status |
|---|---|---|
| [PROGRAMME-AIRCRAFT] | Electrified aircraft programme family. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| ATLAS | Aircraft Top Level Architecture Schema/System. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| BITE | Built-In Test Equipment. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| CSDB | Common Source DataBase (S1000D). | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| DMC | Data Module Code. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| DMRL | Data Module Requirement List. | ![TBD](https://img.shields.io/badge/TBD-red) |
| [PROGRAMME-VARIANT] | Electric programme-defined aircraft configuration. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| HVDC | High-Voltage Direct Current. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| IMA | Integrated Modular Avionics. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| S1000D | International specification for technical publications. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |

---

## 19. Open Issues

| ID | Description | Owner | Status |
|---|---|---|---|
| OI-007-050-001 | Content requires review by system expert. | Q-GROUND | open |
| OI-007-050-002 | S1000D DMC mapping to be validated against DMRL. | Q-DATAGOV | open |

---

## 20. References

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).
[^ata2200]: **ATA iSpec 2200** — Information Standards for Aviation Maintenance.
[^s1000d]: **S1000D Issue 6.0** — International specification for technical publications.
[^as9100d]: **AS9100D** — Quality Management Systems — Aviation, Space and Defense Organizations.
[^cs25]: **EASA CS-25** — Certification Specifications for Large Aeroplanes (Amendment 27+).

---

## 21. Change Log

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0.0 | 2026-05-11 | Q+ Team / Amedeo Pelliccia + AI | Initial baseline from template.md. Content scaffold — pending system expert review. |
