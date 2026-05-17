---
document_id: "QATL-ATLAS-1000-ATLAS-080-089-08-082-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY"
register: ATLAS-1000
title: "S1000D / CSDB Mapping and Traceability"
ata: "ATLAS-082 (Plasma and Ionic Propulsion Concepts)"
sns: "082-090-00"
subsection: "082"
subsubject_code: "090"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-GREENTECH, Q-HPC, Q-INDUSTRY, Q-STRUCTURES]
status: active
scope: agnostic-standard
governance_class: baseline
revision: "0.1"
date: "2026-05-12"
parent_baseline_doc: "../../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "../README.md"
s1000d_dmc: "DMC-<MODEL>-<SYSTEMDIFF>-082-090"
---

<!-- ──────────────────────────────────────────────────────────────────────────
     QATL-ATLAS-1000-ATLAS-080-089-08-082-090-S1000D-CSDB-MAPPING-AND-TRACEABILITY
     ATLAS-082 (Plasma and Ionic Propulsion Concepts) · S1000D / CSDB Mapping and Traceability
────────────────────────────────────────────────────────────────────────────── -->

# S1000D / CSDB Mapping and Traceability

![Status: DRAFT](https://img.shields.io/badge/Status-DRAFT-yellow)
![Register: ATLAS-1000](https://img.shields.io/badge/Register-ATLAS--1000-blue)
![ATA: ATLAS-082 Plasma & Ionic](https://img.shields.io/badge/ATLAS--082-Plasma%20%26%20Ionic%20Propulsion-green)
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

ATLAS subsubject 082-090 establishes the S1000D Data Module Requirements List (DMRL), BREX document reference and constraints, CSDB integration interfaces, ICN registry, and milestone plan for any programme implementing this ATLAS standard node Plasma and Ionic Propulsion Concepts (PIPC) system technical documentation. It provides the authoritative traceability table between ATLAS subsubject documents and their corresponding S1000D Data Modules (DMs) in the CSDB.

---

## §2 Applicability

| Parameter | Value |
|---|---|
| Programme | (defined in programme implementation branch) |
| ATA reference | ATLAS-082 (Plasma and Ionic Propulsion Concepts) — 082-090 S1000D / CSDB Mapping and Traceability |
| Certification basis | EASA CS-25 Amdt 27+ (research ref.); S1000D Issue 5.0; BREX-082-v1 |
| S1000D SNS | 082-090-00 |

---

## §3 Functional Description ![DRAFT]

The PIPC technical documentation suite comprises **28 S1000D Data Modules (DMs)** registered in the programme CSDB under the SNS 082 schema. The Data Module Code (DMC) pattern is `DMC-<MODEL>-<SYSTEMDIFF>-082-{NNN}-00A-EN-US`, where `{NNN}` is the three-digit subsubject code (000–090) and the information code suffix identifies the DM type: `-040A` for descriptive, `-100A` for procedural (task), `-300A` for inspection, and `-520A` for removal/replacement. The BREX governing document is `BREX-082-v1`.

**BREX-082-v1** enforces three domain-specific plasma and ionic propulsion constraints applicable across all DM types under SNS 082:

1. **High-Voltage Pre-Access Rule** — All maintenance DMs of type 100 (procedural task), 300 (inspection), and 520 (removal/replacement) that require any physical access within 300 mm of any PPPU HV output, HV cable, or thruster HV electrode must include a mandatory HV de-energisation and discharge pre-verification step as the first pre-task action: (a) PPPU BITE must confirm HV rails discharged (< 50 V on all rails) via PPPU panel indicator PROP PLASMA HV OFF; (b) time elapsed since PPPU shutdown must be ≥ 30 s (capacitor bleed discharge time). The pre-verification step must be rendered in the DM as a WARNING-level caution preceding all procedural steps. Warning text must state: "High-voltage capacitors retain charge after power-down. Confirm PROP PLASMA HV OFF indicator is illuminated and ≥ 30 s has elapsed before touching any HV cable or electrode. Voltages up to 2 000 V DC are present and are fatal."

2. **Xenon Asphyxiation Hazard Rule** — All DMs for tasks in the aft Xe storage bay or within the Xe propellant feed manifold zone (ATEX Zone 2) must include: (a) mandatory O₂ level check using calibrated O₂ monitor prior to bay entry; entry is prohibited if O₂ < 19.5 % v/v; (b) a NOTE in the DM stating: "Xenon is a non-toxic, odourless, colourless asphyxiating gas. Leakage may displace oxygen. Unexplained dizziness, shortness of breath, or loss of vision are warning signs of oxygen depletion; exit the area immediately and signal for assistance."; (c) mandatory ventilation fan on before entry; (d) Xe vessel isolation valve locked out before any connection/disconnection of Xe feed tubing.

3. **Plume Exclusion Zone Rule** — All DMs for tasks involving thruster ignition or test firing (on-aircraft) must include a mandatory plume exclusion zone clearance check as a pre-condition: no personnel, equipment, or materials within the 30° half-angle plume cone to a depth of 300 mm from each active thruster exit plane. The DM must state: "Activate PROP PLASMA PLUME ZONE CLEAR confirmation on PPPU GSE panel and visually confirm aft zone clear before enabling thruster HV. Ion beam energies up to 1 200 eV cause immediate skin and eye injury and will damage most materials within the exclusion zone."

---

## §4 DMRL — Data Module Requirements List

| DM Number | DMC | Type | Title | ATLAS Source Doc |
|---|---|---|---|---|
| DM-082-001 | DMC-<MODEL>-<SYSTEMDIFF>-082-000-040A | Descriptive | PIPC System General Overview | 082-000 |
| DM-082-002 | DMC-<MODEL>-<SYSTEMDIFF>-082-000-100A | Task | PPPU System Activation Procedure | 082-000 |
| DM-082-003 | DMC-<MODEL>-<SYSTEMDIFF>-082-000-300A | Inspection | PPPU System Periodic Inspection | 082-000 |
| DM-082-004 | DMC-<MODEL>-<SYSTEMDIFF>-082-010-040A | Descriptive | Plasma Propulsion Baseline and Mission Trade | 082-010 |
| DM-082-005 | DMC-<MODEL>-<SYSTEMDIFF>-082-020-040A | Descriptive | Ionic Propulsion Physics and Operating Principles | 082-020 |
| DM-082-006 | DMC-<MODEL>-<SYSTEMDIFF>-082-030-040A | Descriptive | Electric and Magnetic Acceleration Mechanisms | 082-030 |
| DM-082-007 | DMC-<MODEL>-<SYSTEMDIFF>-082-040-040A | Descriptive | Propellant Ionisation and Plasma Generation | 082-040 |
| DM-082-008 | DMC-<MODEL>-<SYSTEMDIFF>-082-040-100A | Task | Xenon Vessel Filling Procedure | 082-040 |
| DM-082-009 | DMC-<MODEL>-<SYSTEMDIFF>-082-040-300A | Inspection | Xe Vessel and Feed System Leak Inspection | 082-040 |
| DM-082-010 | DMC-<MODEL>-<SYSTEMDIFF>-082-040-520A | Task | XMFC Removal and Replacement | 082-040 |
| DM-082-011 | DMC-<MODEL>-<SYSTEMDIFF>-082-050-040A | Descriptive | Thruster Chamber, Grid and Electrode Interfaces | 082-050 |
| DM-082-012 | DMC-<MODEL>-<SYSTEMDIFF>-082-050-100A | Task | HET Hollow Cathode Replacement | 082-050 |
| DM-082-013 | DMC-<MODEL>-<SYSTEMDIFF>-082-050-300A | Inspection | HET Channel Erosion Borescope Inspection | 082-050 |
| DM-082-014 | DMC-<MODEL>-<SYSTEMDIFF>-082-050-300B | Inspection | GIE Accel Grid Erosion Inspection | 082-050 |
| DM-082-015 | DMC-<MODEL>-<SYSTEMDIFF>-082-050-520A | Task | HET Module Removal and Replacement | 082-050 |
| DM-082-016 | DMC-<MODEL>-<SYSTEMDIFF>-082-050-520B | Task | GIE Module Removal and Replacement | 082-050 |
| DM-082-017 | DMC-<MODEL>-<SYSTEMDIFF>-082-060-040A | Descriptive | Power Processing and High-Voltage Interfaces | 082-060 |
| DM-082-018 | DMC-<MODEL>-<SYSTEMDIFF>-082-060-100A | Task | PPPU HiPot (Insulation Resistance) Test | 082-060 |
| DM-082-019 | DMC-<MODEL>-<SYSTEMDIFF>-082-060-300A | Inspection | HV Cable and Connector Visual Inspection | 082-060 |
| DM-082-020 | DMC-<MODEL>-<SYSTEMDIFF>-082-060-520A | Task | PPPU LRU Removal and Replacement | 082-060 |
| DM-082-021 | DMC-<MODEL>-<SYSTEMDIFF>-082-070-040A | Descriptive | Thermal, EMC and Plume Interaction Constraints | 082-070 |
| DM-082-022 | DMC-<MODEL>-<SYSTEMDIFF>-082-070-300A | Inspection | Thruster Mount Thermal Shield Inspection | 082-070 |
| DM-082-023 | DMC-<MODEL>-<SYSTEMDIFF>-082-070-300B | Inspection | EMC Shielding and Bonding Continuity Check | 082-070 |
| DM-082-024 | DMC-<MODEL>-<SYSTEMDIFF>-082-080-040A | Descriptive | Monitoring, Diagnostics and Control Interfaces | 082-080 |
| DM-082-025 | DMC-<MODEL>-<SYSTEMDIFF>-082-080-100A | Task | PPPU BITE Full Diagnostic Run | 082-080 |
| DM-082-026 | DMC-<MODEL>-<SYSTEMDIFF>-082-080-300A | Inspection | Plasma Sensor Array (PSA) Functional Check | 082-080 |
| DM-082-027 | DMC-<MODEL>-<SYSTEMDIFF>-082-080-520A | Task | PSA Probe Replacement | 082-080 |
| DM-082-028 | DMC-<MODEL>-<SYSTEMDIFF>-082-090-040A | Descriptive | S1000D / CSDB Mapping and Traceability | 082-090 |

---

## §5 BREX Reference Summary (BREX-082-v1)

| Rule ID | Rule Title | DM Types Affected | ATLAS Source |
|---|---|---|---|
| BREX-082-HV-01 | HV Pre-Access De-energisation Rule | 100, 300, 520 (HV proximity tasks) | 082-060 |
| BREX-082-XE-01 | Xenon Asphyxiation Hazard Rule | 100, 300, 520 (Xe bay tasks) | 082-040 |
| BREX-082-PZ-01 | Plume Exclusion Zone Rule | 100, 300 (thruster ignition/test fire) | 082-070 |

---

## §6 ICN Registry

| ICN | Content Type | Used In | Description |
|---|---|---|---|
| ICN-082-0001 | Diagram (SVG) | DM-082-001 | PIPC system top-level block diagram |
| ICN-082-0002 | Diagram (SVG) | DM-082-006 | HET magnetic circuit cross-section |
| ICN-082-0003 | Diagram (SVG) | DM-082-006 | GIE grid assembly exploded view |
| ICN-082-0004 | Diagram (SVG) | DM-082-011 | HET installation pylon ICD sketch |
| ICN-082-0005 | Diagram (SVG) | DM-082-011 | GIE nacelle fairing installation sketch |
| ICN-082-0006 | Diagram (SVG) | DM-082-021 | Plume exclusion zone envelope drawing |
| ICN-082-0007 | Photo | DM-082-013 | HET channel borescope reference image (new channel) |
| ICN-082-0008 | Warning sign (PNG) | DM-082-008, 012, 015 | HV warning label (ISO 3864-2 Class B) |
| ICN-082-0009 | Warning sign (PNG) | DM-082-008, 009, 010 | Xe asphyxiation hazard label |

---

## §7 CSDB Publication Milestones

| Milestone | Target Date | DMs Affected | Status |
|---|---|---|---|
| CSDB initial load — descriptive DMs | PDR + 3 months | DM-001, 004, 005, 006, 007, 011, 017, 021, 024, 028 | Planned |
| CSDB first load — task DMs (Xe system) | PDR + 6 months | DM-002, 008, 010 | Planned |
| CSDB load — inspection DMs | CDR − 3 months | DM-003, 009, 013, 014, 018, 019, 022, 023, 025, 026 | Planned |
| CSDB load — removal/replacement DMs | CDR | DM-012, 015, 016, 020, 027 | Planned |
| CSDB Xe fill / LOTO DM + BREX validation | CDR + 1 month | All 28 DMs | Planned |
| Publication qualification (S1000D conformance review) | Phase 2 entry | All 28 DMs | Planned |

---

## §8 Traceability to ATLAS Subsubject Documents

| ATLAS Document | Document ID | Related DM Numbers |
|---|---|---|
| 082-000 General | QATL-...-082-000-... | DM-082-001, 002, 003 |
| 082-010 Baseline | QATL-...-082-010-... | DM-082-004 |
| 082-020 Ionic Principles | QATL-...-082-020-... | DM-082-005 |
| 082-030 E/B Mechanisms | QATL-...-082-030-... | DM-082-006 |
| 082-040 Propellant/Plasma | QATL-...-082-040-... | DM-082-007, 008, 009, 010 |
| 082-050 Chamber/Grid | QATL-...-082-050-... | DM-082-011, 012, 013, 014, 015, 016 |
| 082-060 Power Processing | QATL-...-082-060-... | DM-082-017, 018, 019, 020 |
| 082-070 Thermal/EMC/Plume | QATL-...-082-070-... | DM-082-021, 022, 023 |
| 082-080 Monitoring | QATL-...-082-080-... | DM-082-024, 025, 026, 027 |
| 082-090 S1000D Traceability | QATL-...-082-090-... | DM-082-028 |

---

## §9 Open Issues

| ID | Description | Owner | Target |
|---|---|---|---|
| OI-082-090-001 | BREX-082-v1 formal review and sign-off by Q-DATAGOV and airworthiness team | Q-DATAGOV | PDR |
| OI-082-090-002 | ICN vector artwork (SVG) for plume exclusion zone drawing (ICN-082-0006) — awaiting plume CFD | Q-STRUCTURES | CDR |
| OI-082-090-003 | CSDB SNS 082 namespace reservation in <PROGRAMME> CSDB instance | Q-DATAGOV | PDR |
