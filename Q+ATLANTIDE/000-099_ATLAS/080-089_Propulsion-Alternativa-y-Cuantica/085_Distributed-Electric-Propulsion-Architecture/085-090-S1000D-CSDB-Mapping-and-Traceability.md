---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-085-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY"
register: ATLAS-1000
title: "S1000D CSDB Mapping and Traceability"
ata: "ATLAS-085 (Distributed Electric Propulsion Architecture)"
sns: "085-090-00"
subsection: "085"
subsubject_code: "090"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-GREENTECH, Q-HPC, Q-INDUSTRY, Q-STRUCTURES]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-13"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0085-090"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-085-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY
     ATLAS-085 (Distributed Electric Propulsion Architecture) · S1000D CSDB Mapping and Traceability
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# S1000D CSDB Mapping and Traceability

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-085 DEP Architecture](https://img.shields.io/badge/ATLAS--085-DEP%20Architecture-green)
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

ATLAS subsubject 085-090 establishes the S1000D Data Module Requirements List (DMRL), the BREX-085-v1 rule set, the ICN (Illustration Control Number) registry, the CSDB publication milestones, and the traceability matrix mapping all ten DEPA subsubject documents to their corresponding S1000D Data Modules (DMs). It is the authoritative reference for the DEPA technical publication deliverables and governs the structure of the AMPEL360E-EWTW CSDB entries under SNS 085.

---

## §2 Applicability

| Attribute | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA Reference | ATLAS-085 (Distributed Electric Propulsion Architecture) — 085-090 S1000D/CSDB Mapping and Traceability |
| S1000D Version | Issue 5.0 |
| BREX | BREX-085-v1 |
| Total DMs in DMRL | 30 |
| DMC Pattern | `AMPEL360E-EWTW-085-{NNN}-00A-{TYPE}-EN-US` |
| Certification Basis | S1000D Issue 5.0; BREX-085-v1; EASA CS-25 Amdt 27+ (research ref.) |
| S1000D SNS | 085-090-00 |

---

## §3 Functional Description

The DEPA technical documentation suite comprises **30 S1000D Data Modules (DMs)** registered in the AMPEL360E-EWTW CSDB under the SNS 085 schema. The Data Module Code (DMC) pattern is `AMPEL360E-EWTW-085-{NNN}-00A-EN-US`, where `{NNN}` is the three-digit subsubject code (000–090) and the information code suffix identifies the DM type: `-040A` for descriptive, `-100A` for procedural (task), `-300A` for inspection, and `-520A` for removal/replacement.

The governing BREX document is `AMPEL360E-BREX-085-v1`, which enforces three domain-specific constraints applicable across all DM types under SNS 085:

**BREX-085-HV-01 — HVDC 800 V Pre-Access Rule:**
All maintenance DMs of type 100 (task), 300 (inspection), and 520 (removal/replacement) that require physical access within 500 mm of any BTB, SSPC, HVDC cable, or MDU must include the following mandatory pre-task action as the first step:
(a) Command DEPCU to STANDBY via DEPCU-GSE-1 or cockpit DEP PANEL; confirm DPDP bus voltage < 50 V via DEP synoptic or GSE voltmeter.
(b) Wait ≥ 60 s (MDU DC link capacitor bleed time) after STANDBY confirmation.
(c) Confirm with secondary voltmeter check on the specific component to be accessed.
The pre-access step must be rendered in the DM as a WARNING-level caution preceding all procedural steps. Warning text must state: *"HVDC 800 V BUS. Confirm DEPCU STANDBY and wait 60 s before touching any HVDC component. Voltages up to 800 V DC can cause fatal electrocution. Class 4 HV gloves and face shield mandatory."*

**BREX-085-ROT-01 — Rotating Machinery Lockout Rule:**
All DMs for tasks on any PMSM, fan rotor, fan blade, or fan shaft must include the following mandatory pre-task action:
(a) Confirm BTB for the affected propulsor is OPEN (DEPCU synoptic or BTB position indicator).
(b) Install fan rotation lockout pin (DEP-LKP-001 or equivalent) in the fan hub before any work on fan blades or shaft.
(c) A NOTE must state: *"Fan rotor can rotate freely when PMSM is de-energised. Install rotation lockout pin before approaching fan disk. Fan blade strike can cause serious injury."*

**BREX-085-VIB-01 — Vibration Monitoring Continuity Rule:**
All DMs for MDU or PMSM removal/replacement tasks must include a post-installation requirement: after BTB-close and spin-up, vibration level must be verified acceptable per DEP-BITE vibration check procedure (BITE Level 1 readout) before return to service. DMs must state the acceptance threshold: PMSM bearing RMS vibration ≤ 2.0 g (Level 1 BITE); if exceeded, remove MDU/PMSM and inspect for installation error or balance issue before further flight.

---

## §4 DMRL — Data Module Requirements List

| DM Number | DMC | Type | Title | ATLAS Source |
|---|---|---|---|---|
| DM-085-001 | AMPEL360E-EWTW-085-000-040A | Descriptive | DEP System General Overview | 085-000 |
| DM-085-002 | AMPEL360E-EWTW-085-000-100A | Task | DEPCU System Activation Procedure | 085-000 |
| DM-085-003 | AMPEL360E-EWTW-085-000-300A | Inspection | DEPCU System Periodic BITE Inspection | 085-000 |
| DM-085-004 | AMPEL360E-EWTW-085-010-040A | Descriptive | DEP Baseline and Scope | 085-010 |
| DM-085-005 | AMPEL360E-EWTW-085-020-040A | Descriptive | Distributed Propulsor Layout and Topology | 085-020 |
| DM-085-006 | AMPEL360E-EWTW-085-020-300A | Inspection | Fan Face BLI Inlet and Nacelle Structural Inspection | 085-020 |
| DM-085-007 | AMPEL360E-EWTW-085-030-040A | Descriptive | Electric Motor and Drive Allocation | 085-030 |
| DM-085-008 | AMPEL360E-EWTW-085-030-300A | Inspection | PMSM Winding Insulation Resistance Check | 085-030 |
| DM-085-009 | AMPEL360E-EWTW-085-030-300B | Inspection | MDU Gate Driver and IGBT Thermal Inspection | 085-030 |
| DM-085-010 | AMPEL360E-EWTW-085-030-520A | Task | PMSM LRU Removal and Replacement | 085-030 |
| DM-085-011 | AMPEL360E-EWTW-085-030-520B | Task | MDU LRU Removal and Replacement | 085-030 |
| DM-085-012 | AMPEL360E-EWTW-085-040-040A | Descriptive | Power Distribution and Energy Management Interfaces | 085-040 |
| DM-085-013 | AMPEL360E-EWTW-085-040-100A | Task | BTB-P1…P4 Functional Test Procedure | 085-040 |
| DM-085-014 | AMPEL360E-EWTW-085-040-300A | Inspection | HVDC 800 V Cable and Connector HiPot Inspection | 085-040 |
| DM-085-015 | AMPEL360E-EWTW-085-040-300B | Inspection | DEP-IMU Insulation Resistance Measurement | 085-040 |
| DM-085-016 | AMPEL360E-EWTW-085-040-520A | Task | SSPC-P1…P4 LRU Removal and Replacement | 085-040 |
| DM-085-017 | AMPEL360E-EWTW-085-050-040A | Descriptive | Propulsor Airframe Integration and Aero-Propulsive Coupling | 085-050 |
| DM-085-018 | AMPEL360E-EWTW-085-050-300A | Inspection | P1/P2 Nacelle Pylon and Lug Inspection | 085-050 |
| DM-085-019 | AMPEL360E-EWTW-085-050-300B | Inspection | P3/P4 Aft-Fuselage Truss Frame and Flange Inspection | 085-050 |
| DM-085-020 | AMPEL360E-EWTW-085-060-040A | Descriptive | Redundancy Fault Tolerance and Degraded Modes | 085-060 |
| DM-085-021 | AMPEL360E-EWTW-085-060-100A | Task | DEPA Degraded Mode Verification — Ground Test | 085-060 |
| DM-085-022 | AMPEL360E-EWTW-085-060-300A | Inspection | BTB Position and Isolation Resistance Check (All Propulsors) | 085-060 |
| DM-085-023 | AMPEL360E-EWTW-085-070-040A | Descriptive | Thermal EMC and Structural Integration Constraints | 085-070 |
| DM-085-024 | AMPEL360E-EWTW-085-070-100A | Task | DEP-TML Coolant Flush and Refill Procedure | 085-070 |
| DM-085-025 | AMPEL360E-EWTW-085-070-300A | Inspection | DEP-TML Pump and DEP-RAHX Inspection | 085-070 |
| DM-085-026 | AMPEL360E-EWTW-085-070-300B | Inspection | MDU Cold Plate O-Ring and Cooling Connection Inspection | 085-070 |
| DM-085-027 | AMPEL360E-EWTW-085-080-040A | Descriptive | DEP Monitoring Diagnostics and Control Interfaces | 085-080 |
| DM-085-028 | AMPEL360E-EWTW-085-080-100A | Task | DEPCU BITE Full Diagnostic Run Procedure | 085-080 |
| DM-085-029 | AMPEL360E-EWTW-085-080-300A | Inspection | DEPCU AFDX and CAN Interface Functional Check | 085-080 |
| DM-085-030 | AMPEL360E-EWTW-085-090-040A | Descriptive | S1000D / CSDB Mapping and Traceability | 085-090 |

---

## §5 BREX Reference Summary (BREX-085-v1)

| Rule ID | Rule Title | DM Types Affected | ATLAS Source |
|---|---|---|---|
| BREX-085-HV-01 | HVDC 800 V Pre-Access De-energisation Rule | 100, 300, 520 (HV proximity tasks) | 085-040, 085-070 |
| BREX-085-ROT-01 | Rotating Machinery Lockout Rule | 300, 520 (fan/PMSM tasks) | 085-020, 085-030 |
| BREX-085-VIB-01 | Vibration Monitoring Continuity Rule | 520 (MDU/PMSM R&R tasks) | 085-030, 085-070 |

---

## §6 ICN Registry

| ICN | Content Type | Used In DM | Description |
|---|---|---|---|
| ICN-AMPEL360E-085-0001 | Diagram (SVG) | DM-085-001 | DEPA system top-level block diagram |
| ICN-AMPEL360E-085-0002 | Diagram (SVG) | DM-085-005 | Four-propulsor airframe layout — planform view |
| ICN-AMPEL360E-085-0003 | Diagram (SVG) | DM-085-012 | DEP power distribution single-line diagram |
| ICN-AMPEL360E-085-0004 | Diagram (SVG) | DM-085-020 | DEPCU mode state machine diagram |
| ICN-AMPEL360E-085-0005 | Diagram (SVG) | DM-085-023 | DEP-TML cooling loop schematic |
| ICN-AMPEL360E-085-0006 | Diagram (SVG) | DM-085-027 | DEP cockpit synoptic MFD page layout |
| ICN-AMPEL360E-085-0007 | Diagram (SVG) | DM-085-017 | BLI inlet cross-section — P3/P4 D-duct |
| ICN-AMPEL360E-085-0008 | Warning sign (PNG) | DM-085-002, 013, 014, 016 | HVDC 800 V HV warning label (ISO 3864-2 Class B) |
| ICN-AMPEL360E-085-0009 | Warning sign (PNG) | DM-085-010, 011 | Rotating machinery lockout label (fan rotation hazard) |
| ICN-AMPEL360E-085-0010 | Warning sign (PNG) | DM-085-002, 011 | Arc flash PPE label (Class 4 gloves required) |

---

## §7 CSDB Publication Milestones

| Milestone | Target Date | DMs Affected | Status |
|---|---|---|---|
| CSDB initial load — descriptive DMs | PDR + 3 months | DM-001, 004, 005, 007, 012, 017, 020, 023, 027, 030 | Planned |
| CSDB first load — activation task DMs | PDR + 6 months | DM-002, 013, 021 | Planned |
| CSDB load — inspection DMs | CDR − 3 months | DM-003, 006, 008, 009, 014, 015, 018, 019, 022, 025, 026, 028, 029 | Planned |
| CSDB load — removal/replacement DMs | CDR | DM-010, 011, 016, 024 | Planned |
| BREX-085-v1 formal validation | CDR + 1 month | All 30 DMs | Planned |
| S1000D conformance review | Phase 2 entry | All 30 DMs | Planned |

---

## §8 Traceability to ATLAS Subsubject Documents

| ATLAS Document | Document ID | Related DM Numbers |
|---|---|---|
| 085-000 General | QATL-...-085-000-... | DM-085-001, 002, 003 |
| 085-010 Baseline and Scope | QATL-...-085-010-... | DM-085-004 |
| 085-020 Propulsor Layout and Topology | QATL-...-085-020-... | DM-085-005, 006 |
| 085-030 Electric Motor and Drive Allocation | QATL-...-085-030-... | DM-085-007, 008, 009, 010, 011 |
| 085-040 Power Distribution and Energy Mgmt | QATL-...-085-040-... | DM-085-012, 013, 014, 015, 016 |
| 085-050 Airframe Integration and Aero-Propulsive | QATL-...-085-050-... | DM-085-017, 018, 019 |
| 085-060 Redundancy, Fault Tolerance, Degraded Modes | QATL-...-085-060-... | DM-085-020, 021, 022 |
| 085-070 Thermal, EMC and Structural Constraints | QATL-...-085-070-... | DM-085-023, 024, 025, 026 |
| 085-080 Monitoring, Diagnostics and Control | QATL-...-085-080-... | DM-085-027, 028, 029 |
| 085-090 S1000D Traceability | QATL-...-085-090-... | DM-085-030 |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-085-090-001 | BREX-085-v1 formal review and sign-off by Q-DATAGOV and airworthiness team | Q-DATAGOV | PDR |
| OI-085-090-002 | ICN-085-0004 (mode state machine) — artwork pending DEPCU algorithm CDR freeze | Q-HPC | CDR |
| OI-085-090-003 | CSDB SNS 085 namespace reservation in AMPEL360E-EWTW CSDB instance | Q-DATAGOV | PDR |
| OI-085-090-004 | DM-085-010 (PMSM R&R) — nacelle access time study; confirm < 4 h door-to-door for C-check planning | Q-DATAGOV | CDR |
