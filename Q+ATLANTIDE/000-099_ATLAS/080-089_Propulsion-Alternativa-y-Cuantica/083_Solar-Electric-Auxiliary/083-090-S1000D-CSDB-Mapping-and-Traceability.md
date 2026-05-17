---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-083-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY"
register: ATLAS-1000
title: "S1000D / CSDB Mapping and Traceability"
ata: "ATLAS-083 (Solar-Electric Auxiliary)"
sns: "083-090-00"
subsection: "083"
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
s1000d_dmc: "DMC-<PROGRAMME>-<VARIANT>-0083-090"
standard_scope: agnostic
programme_specific: false
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-083-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY
     ATLAS-083 (Solar-Electric Auxiliary) · S1000D / CSDB Mapping and Traceability
     programme-defined aircraft type — ATLAS Register 1000
────────────────────────────────────────────────────────────────────────────── -->

# S1000D / CSDB Mapping and Traceability

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-083 Solar-Electric](https://img.shields.io/badge/ATLAS--083-Solar--Electric%20Auxiliary-green)
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

This document defines the agnostic ATLAS standard-level architecture context for `S1000D / CSDB Mapping and Traceability`.

It describes the controlled scope, functions, interfaces, safety considerations, lifecycle traceability, and S1000D/CSDB mapping logic that programme implementations shall instantiate when this node is applicable.

This document is not a programme design baseline. Programme-specific capacities, locations, part numbers, effectivity, operating limits, maintenance references, and data module codes shall be defined only inside the applicable programme implementation branch.

## §2 Applicability

| Applicability Level | Rule |
|---|---|
| Standard taxonomy | Applies to the ATLAS node `083` |
| Programme implementation | Conditional; determined by programme architecture, trade studies, certification basis, and applicability model |
| Product configuration | Defined in the programme-specific configuration baseline |
| Effectivity | Defined in the programme CSDB / applicability layer |
| Non-applicability | Must be explicitly stated in the programme impact-study branch when excluded |

## §3 Functional Description ![DRAFT]

The SEA technical documentation suite comprises **30 S1000D Data Modules (DMs)** registered in the [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT] CSDB under the SNS 083 schema. The Data Module Code (DMC) pattern is `[PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-{NNN}-00A-EN-US`, where `{NNN}` is the three-digit subsubject code (000–090) and the information code suffix identifies the DM type: `-040A` for descriptive, `-100A` for procedural (task), `-300A` for inspection, and `-520A` for removal/replacement. The BREX governing document is `[PROGRAMME-AIRCRAFT]-BREX-083-v1`.

**BREX-083-v1** enforces three domain-specific solar-electric auxiliary constraints applicable across all DM types under SNS 083:

1. **PV Panel Safe De-energisation Rule** — All maintenance DMs of type 100 (procedural task), 300 (inspection), and 520 (removal/replacement) that require any physical access within 300 mm of any PV string connector, MPPT input terminal, junction box, or DC link busbar must include a mandatory PV array isolation pre-check as the first pre-task action: (a) SEACU BITE must confirm PV string current = 0 A (SEACU SOLAR ARRAY ISOLATED indicator illuminated); (b) opaque cover blanket must be installed over all PV panels in the work zone before any connector handling. Warning text must state: "Photovoltaic panels generate voltage in any light conditions including hangar lighting. Open-circuit voltage up to 600 V DC is present without panel blanket. Install approved opaque blanket and confirm SEACU SOLAR ARRAY ISOLATED before touching any PV connector or terminal. Electrical shock causes serious injury or death."

2. **SCAP Pre-Access Discharge Rule** — All DMs for tasks within 150 mm of SCAP bank terminals, bus bars, or the bidirectional DC/DC converter output must verify SCAP voltage < 50 V (SEACU SCAP DISCHARGED indicator illuminated on SEACU front panel), with ≥ 60 s elapsed after SEACU shutdown to allow bleeder resistor to discharge the capacitor bank. Warning text must state: "Supercapacitor bank retains up to 700 V DC after power-down. Bleeder resistor requires ≥ 60 s to discharge below 50 V. Confirm SEACU SCAP DISCHARGED indicator illuminated and ≥ 60 s elapsed from SEACU power-off before touching any SCAP terminal or bus bar. Voltages above 50 V are potentially fatal."

3. **BLI Fan Exclusion Zone Rule** — All DMs for tasks involving on-aircraft propulsor run-up, motor functional test, or inverter enable must include a mandatory exclusion zone clearance check as a pre-condition: 2 m radius from each propulsor intake and exhaust clear of all personnel, tools, and loose objects. SEACU GSE panel software command BLI FAN ZONE CLEAR must be activated (operator confirms zone clear) before SEACU enables motor inverter gate signals. DM must state: "BLI fan propulsor operates at up to 15 000 RPM. Loose objects ingested into intake cause fan damage and may be ejected from exhaust at high velocity. Ensure 2 m exclusion zone around intake and exhaust is clear before enabling propulsor. Activate BLI FAN ZONE CLEAR on SEACU GSE panel."

---

## §4 DMRL — Data Module Requirements List

| DM Number | DMC | Type | Title | ATLAS Source Doc |
|---|---|---|---|---|
| DM-083-001 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-000-040A | Descriptive | SEA System General Overview | 083-000 |
| DM-083-002 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-000-100A | Task | SEACU System Activation Procedure | 083-000 |
| DM-083-003 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-000-300A | Inspection | SEACU System Periodic Inspection | 083-000 |
| DM-083-004 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-010-040A | Descriptive | SEA Baseline and Mission Trade Study | 083-010 |
| DM-083-005 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-020-040A | Descriptive | Solar Array Integration and MPPT Architecture | 083-020 |
| DM-083-006 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-020-300A | Inspection | PV Panel Visual and EL Imaging Inspection | 083-020 |
| DM-083-007 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-020-300B | Inspection | PV String Open-Circuit Voltage and Current Check | 083-020 |
| DM-083-008 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-020-520A | Task | PV Panel Removal and Replacement | 083-020 |
| DM-083-009 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-030-040A | Descriptive | Energy Storage and Buffering System Description | 083-030 |
| DM-083-010 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-030-100A | Task | SCAP Bank Discharge Procedure (LOTO) | 083-030 |
| DM-083-011 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-030-300A | Inspection | SCAP Bank Capacitance and ESR Check | 083-030 |
| DM-083-012 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-030-300B | Inspection | Li-Ion Battery Auxiliary Subset Inspection | 083-030 |
| DM-083-013 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-030-520A | Task | SCAP Bank Module Removal and Replacement | 083-030 |
| DM-083-014 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-040-040A | Descriptive | Power Conditioning and Distribution Architecture | 083-040 |
| DM-083-015 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-040-100A | Task | SEACU MPPT Converter Functional Test | 083-040 |
| DM-083-016 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-040-300A | Inspection | DC Cable and Connector Visual Inspection | 083-040 |
| DM-083-017 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-040-300B | Inspection | Insulation Resistance (HiPot) Test — DC Link | 083-040 |
| DM-083-018 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-040-520A | Task | MPPT Converter Module Removal and Replacement | 083-040 |
| DM-083-019 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-040-520B | Task | SiC Inverter LRU Removal and Replacement | 083-040 |
| DM-083-020 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-050-040A | Descriptive | Auxiliary Electric Propulsor Concepts | 083-050 |
| DM-083-021 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-050-100A | Task | BLI Propulsor Ground Run-Up Functional Test | 083-050 |
| DM-083-022 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-050-300A | Inspection | BLI Fan Blade and Duct Visual Inspection | 083-050 |
| DM-083-023 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-050-520A | Task | BLI Propulsor Motor / Fan Removal and Replacement | 083-050 |
| DM-083-024 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-060-040A | Descriptive | Emergency and Degraded Mode Operation | 083-060 |
| DM-083-025 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-070-040A | Descriptive | Airframe Integration and Structural Constraints | 083-070 |
| DM-083-026 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-070-300A | Inspection | PV Laminate Bond Line Inspection (Tap Test) | 083-070 |
| DM-083-027 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-080-040A | Descriptive | SEA Monitoring, Diagnostics and Control | 083-080 |
| DM-083-028 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-080-100A | Task | SEACU BITE Full Diagnostic Run (IBIT) | 083-080 |
| DM-083-029 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-080-300A | Inspection | SEACU BITE Functional Check (CBIT Verification) | 083-080 |
| DM-083-030 | [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT]-083-090-040A | Descriptive | S1000D / CSDB Mapping and Traceability | 083-090 |

---

## §5 BREX Reference Summary (BREX-083-v1)

| Rule ID | Rule Title | DM Types Affected | ATLAS Source |
|---|---|---|---|
| BREX-083-PV-01 | PV Panel Safe De-energisation Rule | 100, 300, 520 (PV proximity tasks) | 083-020 |
| BREX-083-SC-01 | SCAP Pre-Access Discharge Rule | 100, 300, 520 (SCAP proximity tasks) | 083-030 |
| BREX-083-BF-01 | BLI Fan Exclusion Zone Rule | 100, 300 (propulsor run-up/test) | 083-050 |

---

## §6 ICN Registry

| ICN | Content Type | Used In | Description |
|---|---|---|---|
| ICN-[PROGRAMME-AIRCRAFT]-083-0001 | Diagram (SVG) | DM-083-001 | SEA system top-level block diagram |
| ICN-[PROGRAMME-AIRCRAFT]-083-0002 | Diagram (SVG) | DM-083-005 | PV array zone layout and MPPT channel map |
| ICN-[PROGRAMME-AIRCRAFT]-083-0003 | Diagram (SVG) | DM-083-005 | PV panel laminate cross-section |
| ICN-[PROGRAMME-AIRCRAFT]-083-0004 | Diagram (SVG) | DM-083-009 | SCAP bank configuration and module layout |
| ICN-[PROGRAMME-AIRCRAFT]-083-0005 | Diagram (SVG) | DM-083-014 | SEACU internal power conditioning schematic |
| ICN-[PROGRAMME-AIRCRAFT]-083-0006 | Diagram (SVG) | DM-083-020 | BLI duct and motor installation cross-section |
| ICN-[PROGRAMME-AIRCRAFT]-083-0007 | Diagram (SVG) | DM-083-025 | SEA structural weight and zone layout |
| ICN-[PROGRAMME-AIRCRAFT]-083-0008 | Warning sign (PNG) | DM-083-008, 010, 013 | PV panel high-voltage hazard label (ISO 3864-2) |
| ICN-[PROGRAMME-AIRCRAFT]-083-0009 | Warning sign (PNG) | DM-083-010, 013 | SCAP high-voltage retained charge label |
| ICN-[PROGRAMME-AIRCRAFT]-083-0010 | Warning sign (PNG) | DM-083-021, 022, 023 | BLI fan exclusion zone label with 2 m radius |

---

## §7 CSDB Publication Milestones

| Milestone | Target Date | DMs Affected | Status |
|---|---|---|---|
| CSDB initial load — descriptive DMs | PDR + 3 months | DM-001, 004, 005, 009, 014, 020, 024, 025, 027, 030 | Planned |
| CSDB first load — task DMs (LOTO / discharge) | PDR + 6 months | DM-002, 010, 015, 021 | Planned |
| CSDB load — inspection DMs | CDR − 3 months | DM-003, 006, 007, 011, 012, 016, 017, 022, 026, 028, 029 | Planned |
| CSDB load — removal/replacement DMs | CDR | DM-008, 013, 018, 019, 023 | Planned |
| BREX-083-v1 validation and CSDB conformance review | CDR + 1 month | All 30 DMs | Planned |
| Publication qualification (S1000D Issue 5.0 conformance) | Phase 2 entry | All 30 DMs | Planned |

---

## §8 Traceability to ATLAS Subsubject Documents

| ATLAS Document | Document ID | Related DM Numbers |
|---|---|---|
| 083-000 General | QATL-...-083-000-... | DM-083-001, 002, 003 |
| 083-010 Baseline | QATL-...-083-010-... | DM-083-004 |
| 083-020 Solar Array | QATL-...-083-020-... | DM-083-005, 006, 007, 008 |
| 083-030 Energy Storage | QATL-...-083-030-... | DM-083-009, 010, 011, 012, 013 |
| 083-040 Power Conditioning | QATL-...-083-040-... | DM-083-014, 015, 016, 017, 018, 019 |
| 083-050 Propulsor Concepts | QATL-...-083-050-... | DM-083-020, 021, 022, 023 |
| 083-060 Emergency Modes | QATL-...-083-060-... | DM-083-024 |
| 083-070 Airframe Integration | QATL-...-083-070-... | DM-083-025, 026 |
| 083-080 Monitoring | QATL-...-083-080-... | DM-083-027, 028, 029 |
| 083-090 S1000D Traceability | QATL-...-083-090-... | DM-083-030 |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-083-090-001 | BREX-083-v1 formal review and sign-off by Q-DATAGOV and airworthiness team | Q-DATAGOV | PDR |
| OI-083-090-002 | ICN vector artwork (SVG) for BLI duct cross-section (ICN-083-0006) — awaiting structural design freeze | Q-STRUCTURES | CDR |
| OI-083-090-003 | CSDB SNS 083 namespace reservation in [PROGRAMME-AIRCRAFT]-[PROGRAMME-VARIANT] CSDB instance | Q-DATAGOV | PDR |
| OI-083-090-004 | DM-083-021 (BLI Ground Run-Up) — BREX-083-BF-01 rule verification in CSDB authoring tool | Q-DATAGOV | CDR |
