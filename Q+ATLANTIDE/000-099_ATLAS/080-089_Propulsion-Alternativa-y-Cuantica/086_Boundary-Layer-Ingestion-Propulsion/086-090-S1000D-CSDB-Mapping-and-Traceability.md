---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-086-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY"
register: ATLAS-1000
title: "S1000D CSDB Mapping and Traceability"
ata: "ATLAS-086 (Boundary Layer Ingestion Propulsion)"
sns: "086-090-00"
subsection: "086"
subsubject_code: "090"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-GREENTECH, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0086-090"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-086-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY
     ATLAS-086 (Boundary Layer Ingestion Propulsion) · S1000D CSDB Mapping and Traceability
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# S1000D CSDB Mapping and Traceability

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-086 BLI Propulsion](https://img.shields.io/badge/ATLAS--086-BLI%20Propulsion-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-DATAGOV](https://img.shields.io/badge/Q--Division-Q--DATAGOV-blue)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden. Every linked document must exist in the Q+ATLANTIDE repository
> before the link is activated. Broken links are treated as open issues and must be resolved
> before the document is promoted from `DRAFT` to `APPROVED`.

---

## §1 Purpose

ATLAS subsubject 086-090 establishes the S1000D Data Module Requirements List (DMRL), the BREX-086-v1 rule set, the ICN (Illustration Control Number) registry, the CSDB publication milestones, and the traceability matrix mapping all ten BLI Propulsion subsubject documents to their corresponding S1000D Data Modules (DMs). It is the authoritative reference for the BLI Propulsion technical publication deliverables and governs the structure of the AMPEL360E-EWTW CSDB entries under SNS 086.

---

## §2 Applicability

| Attribute | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA Reference | ATLAS-086 (Boundary Layer Ingestion Propulsion) — 086-090 S1000D/CSDB Mapping and Traceability |
| S1000D Version | Issue 5.0 |
| BREX | BREX-086-v1 |
| Total DMs in DMRL | 30 |
| DMC Pattern | `AMPEL360E-EWTW-086-{NNN}-00A-{TYPE}-EN-US` |
| Certification Basis | S1000D Issue 5.0; BREX-086-v1; EASA CS-25 Amdt 27+ (research ref.) |
| S1000D SNS | 086-090-00 |

---

## §3 Functional Description

The BLI Propulsion technical documentation suite comprises **30 S1000D Data Modules (DMs)** registered in the AMPEL360E-EWTW CSDB under the SNS 086 schema. The Data Module Code (DMC) pattern is `AMPEL360E-EWTW-086-{NNN}-00A-EN-US`, where `{NNN}` is the three-digit subsubject code (000–090) and the information code suffix identifies the DM type: `-040A` for descriptive, `-100A` for procedural (task), `-300A` for inspection, and `-520A` for removal/replacement.

The governing BREX document is `AMPEL360E-BREX-086-v1`, which enforces three domain-specific constraints applicable across all DM types under SNS 086:

**BREX-086-HV-01 — HVDC 270 V Pre-Access Rule:**
All maintenance DMs of type 100 (task), 300 (inspection), and 520 (removal/replacement) that require physical access within 500 mm of MCU-086-1, MCU-086-2, or their HVDC 270 V feed cables must include the following mandatory pre-task action as the first step:
(a) Command BLICU to STANDBY via BLICU-GSE-1 or cockpit BLI panel; confirm MCU-086 DC link voltage < 50 V on GSE voltmeter.
(b) Wait ≥ 60 s (DC-link capacitor bleed discharge time) after STANDBY confirmation.
(c) Confirm with secondary voltmeter check on the specific component to be accessed.
The pre-access step must be rendered in the DM as a WARNING-level caution preceding all procedural steps. Warning text must state: *"HVDC 270 V BUS. Confirm BLICU STANDBY and wait 60 s before touching MCU-086 or HVDC cables. Voltages up to 270 V DC can cause fatal electrocution. Class 2 HV gloves and face shield mandatory."*

**BREX-086-FAN-01 — Rotating Fan Lock-Out Rule:**
All DMs for tasks within 300 mm of the BLI fan rotor or inlet throat must include a mandatory pre-task action:
(a) Confirm fan speed = 0 RPM on BLICU display or GSE.
(b) Install fan lock pin TL-086-002 (visible red flag).
(c) Confirm BLICU in STANDBY mode (MCU-086 de-energised).
Warning text must state: *"ROTATING FAN HAZARD. Install fan lock pin TL-086-002 before entering inlet or approaching fan rotor within 300 mm. Confirm RPM = 0 before entry. Failure to secure fan can result in serious injury or death."*

**BREX-086-CFD-01 — Distortion Tool Note Rule:**
All descriptive DMs for inlet aerodynamic content (SNS 086-020 and 086-050) must include a NOTE: *"Distortion indices (DC60, ΔPRT) reported in this document are CFD predictions validated by wind tunnel test programme. See ATLAS-086-010 for TRL status. Values will be updated at CDR following rig test completion."*

---

## §4 DMRL — Data Module Requirements List

| DM Number | DMC | Type | Title | ATLAS Source |
|---|---|---|---|---|
| DM-086-001 | AMPEL360E-EWTW-086-000-040A | Descriptive | BLI System General Overview | 086-000 |
| DM-086-002 | AMPEL360E-EWTW-086-000-100A | Task | BLICU System Activation Procedure | 086-000 |
| DM-086-003 | AMPEL360E-EWTW-086-000-300A | Inspection | BLICU System Periodic BITE Inspection | 086-000 |
| DM-086-004 | AMPEL360E-EWTW-086-010-040A | Descriptive | BLI Baseline, Scope and Technology Readiness | 086-010 |
| DM-086-005 | AMPEL360E-EWTW-086-020-040A | Descriptive | Boundary Layer Capture and Inlet Architecture | 086-020 |
| DM-086-006 | AMPEL360E-EWTW-086-020-300A | Inspection | S-Duct Inlet Visual and NDT Inspection | 086-020 |
| DM-086-007 | AMPEL360E-EWTW-086-020-300B | Inspection | Bypass Door Functional Check and Actuator Inspection | 086-020 |
| DM-086-008 | AMPEL360E-EWTW-086-020-520A | Task | S-Duct Inlet Assembly Removal and Replacement | 086-020 |
| DM-086-009 | AMPEL360E-EWTW-086-030-040A | Descriptive | Fan-Propulsor Design and Distortion Tolerance | 086-030 |
| DM-086-010 | AMPEL360E-EWTW-086-030-300A | Inspection | Fan Blade Visual Inspection and Leading-Edge Assessment | 086-030 |
| DM-086-011 | AMPEL360E-EWTW-086-030-300B | Inspection | Fan Balance Check and Re-Balance Procedure | 086-030 |
| DM-086-012 | AMPEL360E-EWTW-086-030-300C | Inspection | Fan Tip Clearance Measurement | 086-030 |
| DM-086-013 | AMPEL360E-EWTW-086-030-520A | Task | BLI Propulsor Fan Stage Removal and Replacement | 086-030 |
| DM-086-014 | AMPEL360E-EWTW-086-040-040A | Descriptive | Aero-Propulsive Coupling and Airframe Integration | 086-040 |
| DM-086-015 | AMPEL360E-EWTW-086-040-300A | Inspection | BLI Hardpoint Fastener Torque Check | 086-040 |
| DM-086-016 | AMPEL360E-EWTW-086-040-300B | Inspection | Vibration Isolation Mount Compression-Set Inspection | 086-040 |
| DM-086-017 | AMPEL360E-EWTW-086-050-040A | Descriptive | BLICU Architecture and BLI Control Logic | 086-050 |
| DM-086-018 | AMPEL360E-EWTW-086-050-100A | Task | BLICU Software Load Procedure | 086-050 |
| DM-086-019 | AMPEL360E-EWTW-086-050-520A | Task | BLICU LRU Removal and Replacement | 086-050 |
| DM-086-020 | AMPEL360E-EWTW-086-060-040A | Descriptive | Noise, Vibration and Aeroelastic Constraints | 086-060 |
| DM-086-021 | AMPEL360E-EWTW-086-060-300A | Inspection | Aft Fuselage Vibration Level Verification | 086-060 |
| DM-086-022 | AMPEL360E-EWTW-086-070-040A | Descriptive | Thermal, Structural and Maintenance Integration | 086-070 |
| DM-086-023 | AMPEL360E-EWTW-086-070-100A | Task | BLITM Coolant Flush and Refill Procedure | 086-070 |
| DM-086-024 | AMPEL360E-EWTW-086-070-300A | Inspection | BLITM Pump and Coolant Sample Inspection | 086-070 |
| DM-086-025 | AMPEL360E-EWTW-086-070-300B | Inspection | PMSM Winding Resistance and Insulation Check | 086-070 |
| DM-086-026 | AMPEL360E-EWTW-086-070-520A | Task | PMSM Motor Stator Removal and Replacement | 086-070 |
| DM-086-027 | AMPEL360E-EWTW-086-070-520B | Task | MCU-086 LRU Removal and Replacement | 086-070 |
| DM-086-028 | AMPEL360E-EWTW-086-080-040A | Descriptive | BLI Monitoring, Diagnostics and Control Interfaces | 086-080 |
| DM-086-029 | AMPEL360E-EWTW-086-080-100A | Task | BLICU BITE Full Diagnostic Run and GSE Download | 086-080 |
| DM-086-030 | AMPEL360E-EWTW-086-090-040A | Descriptive | S1000D / CSDB Mapping and Traceability | 086-090 |

---

## §5 BREX Reference Summary (BREX-086-v1)

| Rule ID | Rule Title | DM Types Affected | ATLAS Source |
|---|---|---|---|
| BREX-086-HV-01 | HVDC 270 V Pre-Access De-energisation Rule | 100, 300, 520 (MCU/HV proximity tasks) | 086-070 |
| BREX-086-FAN-01 | Rotating Fan Lock-Out Rule | 100, 300, 520 (fan rotor / inlet proximity tasks) | 086-030, 086-070 |
| BREX-086-CFD-01 | Distortion Tool Note Rule | 040 (descriptive DMs for inlet aero content) | 086-020, 086-050 |

---

## §6 ICN Registry

| ICN | Content Type | Used In DM | Description |
|---|---|---|---|
| ICN-AMPEL360E-086-0001 | Diagram (SVG) | DM-086-001 | BLI system top-level block diagram |
| ICN-AMPEL360E-086-0002 | Diagram (SVG) | DM-086-005 | S-duct inlet geometry cross-section |
| ICN-AMPEL360E-086-0003 | Diagram (SVG) | DM-086-009 | Fan stage aerodynamic design — blade profile |
| ICN-AMPEL360E-086-0004 | Diagram (SVG) | DM-086-014 | Aero-propulsive coupling — thrust–drag diagram |
| ICN-AMPEL360E-086-0005 | Diagram (SVG) | DM-086-017 | BLICU mode state machine diagram |
| ICN-AMPEL360E-086-0006 | Diagram (SVG) | DM-086-022 | BLITM cooling loop schematic |
| ICN-AMPEL360E-086-0007 | Diagram (SVG) | DM-086-028 | BLI cockpit synoptic MFD page layout |
| ICN-AMPEL360E-086-0008 | Warning sign (PNG) | DM-086-002, 018, 019, 023, 025, 026, 027 | HVDC 270 V HV warning label (ISO 3864-2) |
| ICN-AMPEL360E-086-0009 | Warning sign (PNG) | DM-086-010, 011, 012, 013 | Rotating fan hazard warning label |

---

## §7 CSDB Publication Milestones

| Milestone | Target Date | DMs Affected | Status |
|---|---|---|---|
| CSDB initial load — descriptive DMs | PDR + 3 months | DM-001, 004, 005, 009, 014, 017, 020, 022, 028, 030 | Planned |
| CSDB first load — activation task DMs | PDR + 6 months | DM-002, 018, 023, 029 | Planned |
| CSDB load — inspection DMs | CDR − 3 months | DM-003, 006, 007, 010, 011, 012, 015, 016, 021, 024, 025 | Planned |
| CSDB load — removal/replacement DMs | CDR | DM-008, 013, 019, 026, 027 | Planned |
| BREX-086-v1 formal validation | CDR + 1 month | All 30 DMs | Planned |
| S1000D conformance review | Phase 2 entry | All 30 DMs | Planned |

---

## §8 Traceability to ATLAS Subsubject Documents

| ATLAS Document | Document ID | Related DM Numbers |
|---|---|---|
| 086-000 General | QATL-...-086-000-... | DM-086-001, 002, 003 |
| 086-010 Baseline and Scope | QATL-...-086-010-... | DM-086-004 |
| 086-020 Inlet Architecture | QATL-...-086-020-... | DM-086-005, 006, 007, 008 |
| 086-030 Fan-Propulsor | QATL-...-086-030-... | DM-086-009, 010, 011, 012, 013 |
| 086-040 Aero-Propulsive Coupling | QATL-...-086-040-... | DM-086-014, 015, 016 |
| 086-050 Distortion Control Logic | QATL-...-086-050-... | DM-086-017, 018, 019 |
| 086-060 Noise/Vibration/Aeroelastic | QATL-...-086-060-... | DM-086-020, 021 |
| 086-070 Thermal / Structural / Maint. | QATL-...-086-070-... | DM-086-022, 023, 024, 025, 026, 027 |
| 086-080 Monitoring / Diagnostics | QATL-...-086-080-... | DM-086-028, 029 |
| 086-090 S1000D Traceability | QATL-...-086-090-... | DM-086-030 |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-086-090-001 | BREX-086-v1 formal review and sign-off by Q-DATAGOV and airworthiness team | Q-DATAGOV | PDR |
| OI-086-090-002 | ICN-086-0002 (S-duct cross-section) — artwork pending inlet CDR freeze | Q-HORIZON | CDR |
| OI-086-090-003 | CSDB SNS 086 namespace reservation in AMPEL360E-EWTW CSDB instance | Q-DATAGOV | PDR |
| OI-086-090-004 | DM-086-011 (fan balance) — confirm ground spin balance rig procedure with maintenance engineering | Q-INDUSTRY | CDR |
