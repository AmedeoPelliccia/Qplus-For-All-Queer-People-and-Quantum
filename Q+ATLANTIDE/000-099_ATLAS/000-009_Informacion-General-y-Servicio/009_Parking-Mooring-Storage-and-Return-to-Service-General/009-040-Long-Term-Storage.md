---
document_id: "QATL-ATLAS-1000-ATLAS-000-009-00-009-040-LONG-TERM-STORAGE"
title: "ATLAS 000-009 · 00.009.040 — Long-Term Storage"
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
subsection: "009"
subsection_title: "Parking, Mooring, Storage and Return to Service General"
subsubject: "040"
subsubject_title: "Long-Term Storage"
subsubject_file: "009-040-Long-Term-Storage.md"
subsubject_link: "./009-040-Long-Term-Storage.md"
primary_q_division: Q-GROUND
support_q_divisions: [Q-DATAGOV, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
s1000d_applicability: "S1000D-CSDB-compatible"
ata_reference: "ATA 10"
programme: "AMPEL360e Wide Tube-and-Wing Family"
short_code: "eWTW"
created: "2026-05-11"
updated: "2026-05-11"
review_status: "to-be-reviewed-by-system-expert"
---

![DRAFT](https://img.shields.io/badge/DRAFT-yellow)
![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)

# ATLAS 000-009 · Section 00 · Subsection 009 · 040 — Long-Term Storage

## 0. Hyperlink Policy

All hyperlinks within this document use **relative paths** from the current file location. Cross-subsection links navigate to sibling files within `./` (same folder), to the subsection index at [`./README.md`](./README.md), and to parent indexes at `../`, `../../`, and `../../../`. Absolute URLs are used only for external standards references.

---

## 1. Purpose

Documents the long-term storage procedures (30 days to 24 months) for the AMPEL360E eWTW. Covers the controlled aircraft preservation configuration, HVDC battery hibernation mode, engine long-term preservation (corrosion inhibitor, desiccant), hydraulic system (TBD) preservation, and the full preservation/depreservation task list with intervals.

This document is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline. It applies to the [AMPEL360e Wide Tube-and-Wing Family](../../../../Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family/) programme, **eWTW** configuration.

---

## 2. Applicability

| Applicability Item | Value | Status |
|---|---|---|
| Programme | AMPEL360e Wide Tube-and-Wing Family | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| Short code | eWTW | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| Architecture register | Q+ATLANTIDE | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| ATLAS band | 000-099_ATLAS | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| ATA reference | ATA 10 | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| S1000D SNS | 009-040-00 | ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange) |
| S1000D compatibility | S1000D-CSDB-compatible | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |

---

## 3. System / Function Overview

The **Long-Term Storage** node covers the architecture, interfaces, operational logic, maintenance boundaries, and traceability requirements associated with this topic.

For the AMPEL360E eWTW configuration, this topic shall be treated as part of a full-electric, bleed-less, medium-range, approximately 100-passenger aircraft architecture. Where conventional aircraft assumptions rely on engine bleed, hydraulic supply, pneumatic supply, or legacy equipment, the AMPEL360E implementation shall be explicitly reviewed for electric, distributed, or digitally controlled alternatives.

---

## 4. Scope

### 4.1 Included

This document includes:

- controlled definition of the long-term storage scope;
- architecture boundaries and interface definitions;
- AMPEL360E eWTW-specific implementation notes;
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

The **Long-Term Storage** architecture is organized around controlled interfaces, deterministic function allocation, and maintainable component boundaries within the 000-009 General Information and Service section of the AMPEL360E eWTW programme.

---

## 6. Functional Breakdown ![To Be Completed](https://img.shields.io/badge/To_Be_Completed-orange)

| Ref | Function | Description | Primary Interface | Status |
|---:|---|---|---|---|
| F-001 | Core Function | Primary controlled function for long-term storage. | [Interfaces](#10-interfaces) | ![TBD](https://img.shields.io/badge/TBD-red) |
| F-002 | Support Function | Supporting controlled function. | [Interfaces](#10-interfaces) | ![TBD](https://img.shields.io/badge/TBD-red) |
| F-003 | Monitoring | Captures status, faults, and maintenance data. | [CMS / BITE](#12-monitoring-and-diagnostics) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| F-004 | Traceability | Links architecture, requirements, and S1000D content. | [CSDB / DMRL](#14-s1000d--csdb-mapping) | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |

---

## 7. Mermaid — System Context Diagram

```mermaid
flowchart LR
    A[Aircraft-Level Function] --> B[Long-Term Storage]
    B --> C[Power / Data Interface]
    B --> D[Ground Interface]
    B --> E[Maintenance Interface]
    E --> F[CMS / BITE]
    F --> G[S1000D / CSDB Evidence]
```

*Diagram 1 — System context for Long-Term Storage.*

---

## 8. Mermaid — Internal Functional Architecture

```mermaid
flowchart TB
    SYS[Long-Term Storage] --> F1[Core Function]
    SYS --> F2[Support Function]
    SYS --> CTRL[Control Logic]
    SYS --> MON[Monitoring and Diagnostics]
    MON --> CMS[CMS / BITE]
    CTRL --> IMA[IMA / Controller Interface]
```

*Diagram 2 — Internal functional architecture for Long-Term Storage.*

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
| Model ident code | `AMPEL360E` | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| System diff code | `EWTW` | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| System code | `009` | ![TBD](https://img.shields.io/badge/TBD-red) |
| Sub-system code | `040` | ![TBD](https://img.shields.io/badge/TBD-red) |
| DMC prefix | `DMC-AMPEL360E-EWTW-009-040` | ![TBD](https://img.shields.io/badge/TBD-red) |
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
| AMPEL360E | Electrified aircraft programme family. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| ATLAS | Aircraft Top Level Architecture Schema/System. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| BITE | Built-In Test Equipment. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| CSDB | Common Source DataBase (S1000D). | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| DMC | Data Module Code. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| DMRL | Data Module Requirement List. | ![TBD](https://img.shields.io/badge/TBD-red) |
| eWTW | Electric Wide Tube-and-Wing. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| HVDC | High-Voltage Direct Current. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| IMA | Integrated Modular Avionics. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |
| S1000D | International specification for technical publications. | ![DRAFT](https://img.shields.io/badge/DRAFT-yellow) |

---

## 19. Open Issues

| ID | Description | Owner | Status |
|---|---|---|---|
| OI-009-040-001 | Content requires review by system expert. | Q-GROUND | open |
| OI-009-040-002 | S1000D DMC mapping to be validated against DMRL. | Q-DATAGOV | open |

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
