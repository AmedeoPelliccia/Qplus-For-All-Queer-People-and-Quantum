---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-084-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY"
register: ATLAS-1000
title: "S1000D CSDB Mapping and Traceability"
ata: "ATLAS-084 (Hybrid Architectures — Beyond Gen-2)"
sns: "084-090-00"
subsection: "084"
subsubject_code: "090"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-GREENTECH, Q-HPC, Q-INDUSTRY, Q-STRUCTURES]
status: active
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-AMPEL360E-EWTW-0084-090"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-084-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY
     ATLAS-084 (Hybrid Architectures — Beyond Gen-2) · S1000D CSDB Mapping and Traceability
     AMPEL360E eWTW — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# S1000D CSDB Mapping and Traceability

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-084 Hybrid Beyond Gen-2](https://img.shields.io/badge/ATLAS--084-Hybrid%20Beyond%20Gen--2-green)
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

ATLAS subsubject 084-090 establishes the S1000D Data Module Requirements List (DMRL), the BREX-084-v1 rule set, the ICN (Illustration Control Number) registry, the CSDB publication milestones, and the traceability matrix mapping all ten BGHA subsubject documents to their corresponding S1000D Data Modules (DMs). It is the authoritative reference for the BGHA technical publication deliverables and governs the structure of the AMPEL360E-EWTW CSDB entries under SNS 084.

---

## §2 Applicability

| Attribute | Value |
|---|---|
| Aircraft Program | AMPEL360E eWTW |
| ATA Reference | ATLAS-084 (Hybrid Architectures — Beyond Gen-2) — 084-090 S1000D/CSDB Mapping and Traceability |
| S1000D Version | Issue 5.0 |
| BREX | BREX-084-v1 |
| Total DMs in DMRL | 32 |
| DMC Pattern | `AMPEL360E-EWTW-084-{NNN}-00A-{TYPE}-EN-US` |
| Certification Basis | S1000D Issue 5.0; BREX-084-v1; EASA CS-25 Amdt 27+ (research ref.) |
| S1000D SNS | 084-090-00 |

---

## §3 Functional Description

The BGHA technical documentation suite comprises **32 S1000D Data Modules (DMs)** registered in the AMPEL360E-EWTW CSDB under the SNS 084 schema. The Data Module Code (DMC) pattern is `AMPEL360E-EWTW-084-{NNN}-00A-EN-US`, where `{NNN}` is the three-digit subsubject code (000–090) and the information code suffix identifies the DM type: `-040A` for descriptive, `-100A` for procedural (task), `-300A` for inspection, and `-520A` for removal/replacement.

The governing BREX document is `AMPEL360E-BREX-084-v1`, which enforces three domain-specific constraints applicable across all DM types under SNS 084:

**BREX-084-HV-01 — HVDC 800 V Pre-Access Rule:**
All maintenance DMs of type 100 (task), 300 (inspection), and 520 (removal/replacement) that require physical access within 500 mm of any Bus-800 component, BDCC, ATRU, BTB, or HVDC cable must include the following mandatory pre-task action as the first step:
(a) Command BGSCU to STANDBY via BGSCU-GSE-1 or cockpit BGHA PANEL; confirm Bus-800 voltage < 50 V on all segments via BGHA synoptic or GSE voltmeter.
(b) Wait ≥ 60 s (Bus-800 capacitor bleed discharge time) after STANDBY confirmation.
(c) Confirm with secondary voltmeter check on the specific component to be accessed.
The pre-access step must be rendered in the DM as a WARNING-level caution preceding all procedural steps. Warning text must state: *"HVDC 800 V BUS. Confirm BGSCU STANDBY and wait 60 s before touching any Bus-800 component. Voltages up to 800 V DC can cause fatal electrocution. Class 4 HV gloves and face shield mandatory."*

**BREX-084-QPU-01 — Quantum MPC Offline Rule:**
All DMs for BGSCU maintenance or BDCC calibration tasks must include a NOTE stating that performing the task places the BGSCU in maintenance mode, which deactivates the QAOA QPU and engages the classical rule-based fallback dispatch. The NOTE must state: *"BGSCU maintenance mode activates classical propulsion dispatch (QAOA offline). Aircraft propulsion performance is sub-optimal during maintenance mode. Complete maintenance task and restore BGSCU to OPERATIONAL mode before flight."*

**BREX-084-H2-01 — Hydrogen ATEX Zone Rule:**
All DMs for tasks in ATEX-084-H2-01 (FCSS bay) or ATEX-084-H2-02 (LH₂ manifold trench) must include: (a) mandatory O₂ check (O₂ monitor; entry prohibited if < 19.5 % v/v); (b) bay ventilation fan ON confirmation before entry; (c) H₂ SOV isolation lock-out before any connection/disconnection of H₂ feed lines; (d) a NOTE: *"Hydrogen is an odourless, colourless, highly flammable gas. Leakage may create explosive mixtures. Use non-sparking tools only. Personal H₂ detector mandatory. Evacuate immediately if H₂ alarm sounds."*

---

## §4 DMRL — Data Module Requirements List

| DM Number | DMC | Type | Title | ATLAS Source |
|---|---|---|---|---|
| DM-084-001 | AMPEL360E-EWTW-084-000-040A | Descriptive | BGHA System General Overview | 084-000 |
| DM-084-002 | AMPEL360E-EWTW-084-000-100A | Task | BGSCU System Activation Procedure | 084-000 |
| DM-084-003 | AMPEL360E-EWTW-084-000-300A | Inspection | BGSCU System Periodic BITE Inspection | 084-000 |
| DM-084-004 | AMPEL360E-EWTW-084-010-040A | Descriptive | Beyond-Gen-2 Baseline and Scope | 084-010 |
| DM-084-005 | AMPEL360E-EWTW-084-020-040A | Descriptive | Advanced Hybrid Propulsion Topology | 084-020 |
| DM-084-006 | AMPEL360E-EWTW-084-020-300A | Inspection | Bus-800 Segment BTB Functional Check | 084-020 |
| DM-084-007 | AMPEL360E-EWTW-084-030-040A | Descriptive | Multi-Source Energy Architecture | 084-030 |
| DM-084-008 | AMPEL360E-EWTW-084-030-300A | Inspection | SSBP Pack SoH Capacity Check Procedure | 084-030 |
| DM-084-009 | AMPEL360E-EWTW-084-030-300B | Inspection | SCEB ESR Measurement and Baseline Check | 084-030 |
| DM-084-010 | AMPEL360E-EWTW-084-040-040A | Descriptive | Source Coupling and Power Conditioning Interfaces | 084-040 |
| DM-084-011 | AMPEL360E-EWTW-084-040-100A | Task | BDCC-C (FCSS Boost) Calibration Procedure | 084-040 |
| DM-084-012 | AMPEL360E-EWTW-084-040-300A | Inspection | BDCC Periodic Inspection and Thermal Check | 084-040 |
| DM-084-013 | AMPEL360E-EWTW-084-040-300B | Inspection | ATRU Diode and Harmonic Inspection | 084-040 |
| DM-084-014 | AMPEL360E-EWTW-084-040-520A | Task | BDCC-A / BDCC-B LRU Removal and Replacement | 084-040 |
| DM-084-015 | AMPEL360E-EWTW-084-040-520B | Task | ATRU-1 / ATRU-2 LRU Removal and Replacement | 084-040 |
| DM-084-016 | AMPEL360E-EWTW-084-050-040A | Descriptive | BGSCU Architecture and QAOA MPC Control | 084-050 |
| DM-084-017 | AMPEL360E-EWTW-084-050-100A | Task | BGSCU Software Load Procedure | 084-050 |
| DM-084-018 | AMPEL360E-EWTW-084-050-300A | Inspection | QPU Module Calibration and Coherence Check | 084-050 |
| DM-084-019 | AMPEL360E-EWTW-084-050-520A | Task | BGSCU LRU Removal and Replacement | 084-050 |
| DM-084-020 | AMPEL360E-EWTW-084-060-040A | Descriptive | Degraded Modes, Redundancy and Reconfiguration | 084-060 |
| DM-084-021 | AMPEL360E-EWTW-084-060-100A | Task | BGHA Degraded Mode Verification — Ground Test | 084-060 |
| DM-084-022 | AMPEL360E-EWTW-084-060-300A | Inspection | BTB Position and Isolation Resistance Check | 084-060 |
| DM-084-023 | AMPEL360E-EWTW-084-070-040A | Descriptive | Airframe Integration, Thermal and Safety | 084-070 |
| DM-084-024 | AMPEL360E-EWTW-084-070-100A | Task | BGHA-TML Coolant Flush and Refill Procedure | 084-070 |
| DM-084-025 | AMPEL360E-EWTW-084-070-300A | Inspection | BGHA-TML Pump and RAHX Inspection | 084-070 |
| DM-084-026 | AMPEL360E-EWTW-084-070-300B | Inspection | Bus-800 HV Cable and Connector Inspection (HiPot) | 084-070 |
| DM-084-027 | AMPEL360E-EWTW-084-070-520A | Task | SSBP Pack Removal and Replacement | 084-070 |
| DM-084-028 | AMPEL360E-EWTW-084-070-520B | Task | FCSS Assembly Removal and Replacement | 084-070 |
| DM-084-029 | AMPEL360E-EWTW-084-080-040A | Descriptive | Monitoring, Diagnostics and Control Interfaces | 084-080 |
| DM-084-030 | AMPEL360E-EWTW-084-080-100A | Task | BGSCU BITE Full Diagnostic Run Procedure | 084-080 |
| DM-084-031 | AMPEL360E-EWTW-084-080-300A | Inspection | EPMS Interface Functional Check | 084-080 |
| DM-084-032 | AMPEL360E-EWTW-084-090-040A | Descriptive | S1000D / CSDB Mapping and Traceability | 084-090 |

---

## §5 BREX Reference Summary (BREX-084-v1)

| Rule ID | Rule Title | DM Types Affected | ATLAS Source |
|---|---|---|---|
| BREX-084-HV-01 | HVDC 800 V Pre-Access De-energisation Rule | 100, 300, 520 (HV proximity tasks) | 084-070 |
| BREX-084-QPU-01 | Quantum MPC Offline Rule | 100, 520 (BGSCU / BDCC maintenance tasks) | 084-050 |
| BREX-084-H2-01 | Hydrogen ATEX Zone Rule | 100, 300, 520 (H₂ bay / FCSS manifold tasks) | 084-040, 084-070 |

---

## §6 ICN Registry

| ICN | Content Type | Used In DM | Description |
|---|---|---|---|
| ICN-AMPEL360E-084-0001 | Diagram (SVG) | DM-084-001 | BGHA system top-level block diagram |
| ICN-AMPEL360E-084-0002 | Diagram (SVG) | DM-084-005 | BGHA power topology — full bus diagram |
| ICN-AMPEL360E-084-0003 | Diagram (SVG) | DM-084-010 | Source coupling converters — single-line diagram |
| ICN-AMPEL360E-084-0004 | Diagram (SVG) | DM-084-016 | BGSCU mode state machine diagram |
| ICN-AMPEL360E-084-0005 | Diagram (SVG) | DM-084-023 | BGHA-TML cooling loop schematic |
| ICN-AMPEL360E-084-0006 | Diagram (SVG) | DM-084-029 | BGHA cockpit synoptic MFD page layout |
| ICN-AMPEL360E-084-0007 | Warning sign (PNG) | DM-084-002, 017, 019, 026 | HVDC 800 V HV warning label (ISO 3864-2 Class B) |
| ICN-AMPEL360E-084-0008 | Warning sign (PNG) | DM-084-024, 025, 028 | H₂ flammable gas hazard label (ATEX) |
| ICN-AMPEL360E-084-0009 | Warning sign (PNG) | DM-084-002, 019 | Arc flash PPE label (Class 4 gloves required) |

---

## §7 CSDB Publication Milestones

| Milestone | Target Date | DMs Affected | Status |
|---|---|---|---|
| CSDB initial load — descriptive DMs | PDR + 3 months | DM-001, 004, 005, 007, 010, 016, 020, 023, 029, 032 | Planned |
| CSDB first load — activation task DMs | PDR + 6 months | DM-002, 011, 017 | Planned |
| CSDB load — inspection DMs | CDR − 3 months | DM-003, 006, 008, 009, 012, 013, 018, 021, 022, 025, 026, 030, 031 | Planned |
| CSDB load — removal/replacement DMs | CDR | DM-014, 015, 019, 027, 028 | Planned |
| BREX-084-v1 formal validation | CDR + 1 month | All 32 DMs | Planned |
| S1000D conformance review | Phase 2 entry | All 32 DMs | Planned |

---

## §8 Traceability to ATLAS Subsubject Documents

| ATLAS Document | Document ID | Related DM Numbers |
|---|---|---|
| 084-000 General | QATL-...-084-000-... | DM-084-001, 002, 003 |
| 084-010 Baseline and Scope | QATL-...-084-010-... | DM-084-004 |
| 084-020 Propulsion Topology | QATL-...-084-020-... | DM-084-005, 006 |
| 084-030 Multi-Source Energy | QATL-...-084-030-... | DM-084-007, 008, 009 |
| 084-040 Source Coupling | QATL-...-084-040-... | DM-084-010, 011, 012, 013, 014, 015 |
| 084-050 Control and Mode Mgmt | QATL-...-084-050-... | DM-084-016, 017, 018, 019 |
| 084-060 Degraded Modes | QATL-...-084-060-... | DM-084-020, 021, 022 |
| 084-070 Airframe / Thermal / Safety | QATL-...-084-070-... | DM-084-023, 024, 025, 026, 027, 028 |
| 084-080 Monitoring / Diagnostics | QATL-...-084-080-... | DM-084-029, 030, 031 |
| 084-090 S1000D Traceability | QATL-...-084-090-... | DM-084-032 |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-084-090-001 | BREX-084-v1 formal review and sign-off by Q-DATAGOV and airworthiness team | Q-DATAGOV | PDR |
| OI-084-090-002 | ICN-084-0004 (mode state machine) — artwork pending 084-050 CDR freeze | Q-HPC | CDR |
| OI-084-090-003 | CSDB SNS 084 namespace reservation in AMPEL360E-EWTW CSDB instance | Q-DATAGOV | PDR |
| OI-084-090-004 | DM-084-018 (QPU calibration) — 45 min outage procedure — confirm MEL impact on CSDB task DM | Q-DATAGOV | CDR |
