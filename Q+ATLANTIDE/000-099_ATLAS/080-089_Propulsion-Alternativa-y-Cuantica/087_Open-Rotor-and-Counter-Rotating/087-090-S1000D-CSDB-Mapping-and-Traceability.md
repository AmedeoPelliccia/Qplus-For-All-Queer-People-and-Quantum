---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-087-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY"
register: ATLAS-1000
title: "S1000D CSDB Mapping and Traceability"
ata: "ATLAS-087 (Open Rotor and Counter-Rotating)"
sns: "087-090-00"
subsection: "087"
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
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0087-090"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-087-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY
     ATLAS-087 (Open Rotor and Counter-Rotating) · S1000D CSDB Mapping and Traceability
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# S1000D CSDB Mapping and Traceability

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-087 Open Rotor](https://img.shields.io/badge/ATLAS--087-Open%20Rotor%20%26%20Counter--Rotating-green)
![Governance: baseline](https://img.shields.io/badge/Governance-baseline-lightgrey)
![Q-Division: Q-DATAGOV](https://img.shields.io/badge/Q--Division-Q--DATAGOV-blue)

---

## §0 Hyperlink Policy

> All hyperlinks in this document are **relative** (five directory levels: `../../../../../`).
> Absolute URLs are forbidden.

---

## §1 Purpose

This document defines the agnostic ATLAS standard-level architecture context for `S1000D CSDB Mapping and Traceability`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.

## §2 Applicability

| Applicability Level | Rule |
|---|---|
| Standard taxonomy | Applies to the ATLAS node `087` |
| Programme implementation | Conditional; determined by programme architecture, trade studies, certification basis, and applicability model |
| Product configuration | Defined in the programme-specific configuration baseline |
| Effectivity | Defined in the programme CSDB / applicability layer |
| Non-applicability | Must be explicitly stated in the programme impact-study branch when excluded |

## §3 Functional Description

The ORCR technical documentation suite comprises **30 S1000D Data Modules (DMs)** registered in the [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT] CSDB under the SNS 087 schema. The Data Module Code (DMC) pattern is `[PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-{NNN}-00A-EN-US`, where `{NNN}` is the three-digit subsubject code (000–090) and the information code suffix identifies the DM type: `-040A` for descriptive, `-100A` for procedural (task), `-300A` for inspection, and `-520A` for removal/replacement.

The governing BREX document is `[PROGRAMME-AIRCRAFT]-BREX-087-v1`, which enforces three domain-specific constraints applicable across all DM types under SNS 087:

**BREX-087-ROT-01 — Rotating Equipment Lock-Out Rule:**
All maintenance DMs of type 100 (task), 300 (inspection), and 520 (removal/replacement) that require physical access within the blade-tip sweep zone must include as the first mandatory step the ORCR LOTO procedure ORCR-LOTO-087:
(a) Confirm N1 < 100 rpm on both FR and AR before entering sweep zone.
(b) Insert blade-pitch lock pins (MEI 087-LOCK-001) on both FR and AR hubs.
(c) De-energise ORSCU hydraulic supply and discharge pitch accumulator to < 50 psi.
(d) Apply LOTO tags to ORSCU circuit breakers Ch A and Ch B.
The mandatory step must be rendered as a WARNING-level caution: *"ROTATING MACHINERY. Do NOT enter blade-tip sweep zone unless ORCR LOTO-087 is fully applied and confirmed. Rotating blades can cause fatal injury. Minimum safe distance from rotating blades: 2.5 m."*

**BREX-087-OVS-01 — Over-Speed Shutdown Inhibit Rule:**
All DMs for ORSCU software load or hardware replacement tasks must include a NOTE stating that the task places the ORSCU over-speed shutdown system in INHIBIT mode. The NOTE must state: *"ORSCU over-speed shutdown is INHIBITED during this maintenance task. Engine run is prohibited while ORSCU is in MAINTENANCE mode. Restore ORSCU to OPERATIONAL mode and confirm over-speed shutdown is ACTIVE before engine start."*

**BREX-087-FOD-01 — FOD Sweep Pre-Task Rule:**
All DMs for tasks that require opening of nacelle cowls or removal of pylon fairing panels must include a mandatory close-out FOD sweep step as the final procedural step before cowl/panel refitting: (a) Inspect all work areas and tool inventory; (b) confirm no loose articles, tools, or consumables remain in or near the blade sweep zone; (c) confirm FOD-87-CHECKLIST is signed by two independent inspectors before cowl closure.

---

## §4 DMRL — Data Module Requirements List

| DM Number | DMC | Type | Title | ATLAS Source |
|---|---|---|---|---|
| DM-087-001 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-000-040A | Descriptive | ORCR System General Overview | 087-000 |
| DM-087-002 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-000-100A | Task | ORSCU System Activation and Ground Check Procedure | 087-000 |
| DM-087-003 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-000-300A | Inspection | ORSCU System Periodic BITE Inspection | 087-000 |
| DM-087-004 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-010-040A | Descriptive | Open Rotor Baseline and Scope | 087-010 |
| DM-087-005 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-020-040A | Descriptive | Counter-Rotating Propulsor Architecture | 087-020 |
| DM-087-006 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-020-300A | Inspection | DPGB Gear Train Functional Check | 087-020 |
| DM-087-007 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-030-040A | Descriptive | Rotor Blade Design and Aeroacoustics | 087-030 |
| DM-087-008 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-030-300A | Inspection | FR Blade Visual and Erosion Inspection | 087-030 |
| DM-087-009 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-030-300B | Inspection | AR Blade NDI (Tap Test and Ultrasound) Inspection | 087-030 |
| DM-087-010 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-030-520A | Task | FR Blade LRU Removal and Replacement | 087-030 |
| DM-087-011 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-030-520B | Task | AR Blade LRU Removal and Replacement | 087-030 |
| DM-087-012 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-040-040A | Descriptive | Gearbox Drive and Torque-Transfer Interfaces | 087-040 |
| DM-087-013 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-040-100A | Task | DPGB Oil Level Check and Top-Up Procedure | 087-040 |
| DM-087-014 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-040-100B | Task | DPGB Oil Filter Replacement Procedure | 087-040 |
| DM-087-015 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-040-300A | Inspection | DPGB Chip Detector Inspection | 087-040 |
| DM-087-016 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-040-520A | Task | DPGB Assembly Removal and Replacement | 087-040 |
| DM-087-017 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-050-040A | Descriptive | Propulsor Airframe Integration and Clearance Zones | 087-050 |
| DM-087-018 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-050-300A | Inspection | BOCS Structural Inspection (Visual + Thermography) | 087-050 |
| DM-087-019 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-060-040A | Descriptive | Noise, Vibration and Cabin Comfort Constraints | 087-060 |
| DM-087-020 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-060-100A | Task | ANC System Ground Test and Verification Procedure | 087-060 |
| DM-087-021 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-060-300A | Inspection | Tuned Vibration Absorber (TVA) Inspection and Retuning | 087-060 |
| DM-087-022 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-070-040A | Descriptive | Safety, Containment and Blade-Off Risk Management | 087-070 |
| DM-087-023 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-070-100A | Task | ORCR LOTO Procedure (ORCR-LOTO-087) | 087-070 |
| DM-087-024 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-070-300A | Inspection | BOCS Post-Event Inspection (After Bird Strike or Hard Landing) | 087-070 |
| DM-087-025 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-070-520A | Task | BOCS Panel Removal and Replacement | 087-070 |
| DM-087-026 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-080-040A | Descriptive | ORCR Monitoring, Diagnostics and Control Interfaces | 087-080 |
| DM-087-027 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-080-100A | Task | ORSCU Software Load Procedure | 087-080 |
| DM-087-028 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-080-300A | Inspection | ORSCU BITE Full Diagnostic Run | 087-080 |
| DM-087-029 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-080-520A | Task | ORSCU LRU Removal and Replacement | 087-080 |
| DM-087-030 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-087-090-040A | Descriptive | S1000D / CSDB Mapping and Traceability | 087-090 |

---

## §5 BREX Reference Summary (BREX-087-v1)

| Rule ID | Rule Title | DM Types Affected | ATLAS Source |
|---|---|---|---|
| BREX-087-ROT-01 | Rotating Equipment Lock-Out Rule | 100, 300, 520 (blade sweep zone tasks) | 087-070 |
| BREX-087-OVS-01 | Over-Speed Shutdown Inhibit Rule | 100, 520 (ORSCU maintenance tasks) | 087-080 |
| BREX-087-FOD-01 | FOD Sweep Pre-Task Rule | 100, 300, 520 (cowl/fairing open tasks) | 087-050 |

---

## §6 ICN Registry

| ICN | Content Type | Used In DM | Description |
|---|---|---|---|
| ICN-[PROGRAMME-AIRCRAFT]-087-0001 | Diagram (SVG) | DM-087-001 | ORCR system top-level block diagram |
| ICN-[PROGRAMME-AIRCRAFT]-087-0002 | Diagram (SVG) | DM-087-005 | Counter-rotating propulsor topology — FR/AR/DPGB |
| ICN-[PROGRAMME-AIRCRAFT]-087-0003 | Diagram (SVG) | DM-087-007 | FR and AR blade planform geometry (scimitar) |
| ICN-[PROGRAMME-AIRCRAFT]-087-0004 | Diagram (SVG) | DM-087-012 | DPGB oil system schematic |
| ICN-[PROGRAMME-AIRCRAFT]-087-0005 | Diagram (SVG) | DM-087-017 | Pylon station clearance zone drawing |
| ICN-[PROGRAMME-AIRCRAFT]-087-0006 | Diagram (SVG) | DM-087-022 | BOCS arc coverage and blade-off trajectory zones |
| ICN-[PROGRAMME-AIRCRAFT]-087-0007 | Diagram (SVG) | DM-087-026 | ORSCU AFDX network topology |
| ICN-[PROGRAMME-AIRCRAFT]-087-0008 | Warning sign (PNG) | DM-087-002, 010, 011, 023, 029 | Rotating machinery hazard label (ISO 11684) |
| ICN-[PROGRAMME-AIRCRAFT]-087-0009 | Warning sign (PNG) | DM-087-013, 014, 015, 016 | DPGB hot surfaces / oil hazard label |

---

## §7 CSDB Publication Milestones

| Milestone | Target Date | DMs Affected | Status |
|---|---|---|---|
| CSDB initial load — descriptive DMs | PDR + 3 months | DM-001, 004, 005, 007, 012, 017, 019, 022, 026, 030 | Planned |
| CSDB first load — activation task DMs | PDR + 6 months | DM-002, 013, 020, 023, 027 | Planned |
| CSDB load — inspection DMs | CDR − 3 months | DM-003, 006, 008, 009, 015, 018, 021, 024, 028 | Planned |
| CSDB load — removal/replacement DMs | CDR | DM-010, 011, 014, 016, 025, 029 | Planned |
| BREX-087-v1 formal validation | CDR + 1 month | All 30 DMs | Planned |
| S1000D conformance review | Phase 2 entry | All 30 DMs | Planned |

---

## §8 Traceability to ATLAS Subsubject Documents

| ATLAS Document | Document ID | Related DM Numbers |
|---|---|---|
| 087-000 General | QATL-...-087-000-... | DM-087-001, 002, 003 |
| 087-010 Baseline and Scope | QATL-...-087-010-... | DM-087-004 |
| 087-020 Counter-Rotating Architecture | QATL-...-087-020-... | DM-087-005, 006 |
| 087-030 Blade Design and Aeroacoustics | QATL-...-087-030-... | DM-087-007, 008, 009, 010, 011 |
| 087-040 Gearbox and Torque Interfaces | QATL-...-087-040-... | DM-087-012, 013, 014, 015, 016 |
| 087-050 Airframe Integration and Clearances | QATL-...-087-050-... | DM-087-017, 018 |
| 087-060 Noise, Vibration and Cabin Comfort | QATL-...-087-060-... | DM-087-019, 020, 021 |
| 087-070 Safety, Containment and Blade-Off | QATL-...-087-070-... | DM-087-022, 023, 024, 025 |
| 087-080 Monitoring, Diagnostics and Control | QATL-...-087-080-... | DM-087-026, 027, 028, 029 |
| 087-090 S1000D Traceability | QATL-...-087-090-... | DM-087-030 |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-087-090-001 | BREX-087-v1 formal review and sign-off by Q-DATAGOV and airworthiness team | Q-DATAGOV | PDR |
| OI-087-090-002 | ICN-087-0006 (blade-off trajectory zones) — artwork pending 087-070 CDR freeze | Q-STRUCTURES | CDR |
| OI-087-090-003 | CSDB SNS 087 namespace reservation in [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT] CSDB instance | Q-DATAGOV | PDR |
| OI-087-090-004 | DM-087-016 (DPGB removal) — off-wing procedure (120 h depot) — confirm MEL DDPB dispatch condition | Q-DATAGOV | CDR |
