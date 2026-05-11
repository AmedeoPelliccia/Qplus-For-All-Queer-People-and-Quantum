#!/usr/bin/env python3
"""Create all subsubject folders and files for ATLAS 052_Doors."""

import os

BASE = (
    "/home/runner/work/Qplus-For-All-Queer-People-and-Quantum/"
    "Qplus-For-All-Queer-People-and-Quantum/"
    "Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/052_Doors"
)

# ---------------------------------------------------------------------------
# Subsubject definitions
# Each entry: (folder_name, nnn, subsubject_title, [(slug, title), ...])
# ---------------------------------------------------------------------------
SUBSUBJECTS = [
    (
        "052-000-Doors-General",
        "000",
        "Doors — General",
        [
            ("052-000-Doors-General-Overview",
             "Doors General Overview"),
            ("052-000-Door-System-Scope-and-Boundaries",
             "Door System Scope and Boundaries"),
            ("052-000-Door-Types-and-Classification",
             "Door Types and Classification"),
            ("052-000-Door-Zones-and-Access-References",
             "Door Zones and Access References"),
            ("052-000-Door-Structural-and-System-Interfaces",
             "Door Structural and System Interfaces"),
            ("052-000-Door-Safety-and-Operational-Principles",
             "Door Safety and Operational Principles"),
            ("052-000-Door-Maintenance-Concept-General",
             "Door Maintenance Concept — General"),
            ("052-000-Door-Inspection-and-Repair-General",
             "Door Inspection and Repair — General"),
            ("052-000-Doors-Applicability-and-Effectivity",
             "Doors Applicability and Effectivity"),
            ("052-000-S1000D-CSDB-Mapping-and-Traceability",
             "S1000D CSDB Mapping and Traceability"),
        ],
    ),
    (
        "052-010-Passenger-and-Service-Doors",
        "010",
        "Passenger and Service Doors",
        [
            ("052-010-Passenger-and-Service-Doors-Overview",
             "Passenger and Service Doors Overview"),
            ("052-010-Passenger-Door-Architecture",
             "Passenger Door Architecture"),
            ("052-010-Service-Door-Architecture",
             "Service Door Architecture"),
            ("052-010-Door-Plug-Frame-and-Surround-Structure",
             "Door Plug, Frame and Surround Structure"),
            ("052-010-Door-Hinge-Arm-and-Support-Fittings",
             "Door Hinge Arm and Support Fittings"),
            ("052-010-Door-Latching-Locking-and-Handle-Mechanisms",
             "Door Latching, Locking and Handle Mechanisms"),
            ("052-010-Door-Sealing-Pressurization-and-Drainage",
             "Door Sealing, Pressurization and Drainage"),
            ("052-010-Door-Operation-Assist-and-Damping-Devices",
             "Door Operation Assist and Damping Devices"),
            ("052-010-Passenger-Service-Door-Inspection-and-Maintenance",
             "Passenger / Service Door Inspection and Maintenance"),
            ("052-010-S1000D-CSDB-Mapping-and-Traceability",
             "S1000D CSDB Mapping and Traceability"),
        ],
    ),
    (
        "052-020-Cargo-Doors",
        "020",
        "Cargo Doors",
        [
            ("052-020-Cargo-Doors-Overview",
             "Cargo Doors Overview"),
            ("052-020-Forward-Cargo-Door",
             "Forward Cargo Door"),
            ("052-020-Aft-Cargo-Door",
             "Aft Cargo Door"),
            ("052-020-Bulk-Cargo-and-Service-Access-Doors",
             "Bulk Cargo and Service Access Doors"),
            ("052-020-Cargo-Door-Structure-and-Cutout-Reinforcement",
             "Cargo Door Structure and Cutout Reinforcement"),
            ("052-020-Cargo-Door-Latching-and-Locking-Systems",
             "Cargo Door Latching and Locking Systems"),
            ("052-020-Cargo-Door-Sealing-and-Pressurization",
             "Cargo Door Sealing and Pressurization"),
            ("052-020-Cargo-Door-Actuation-and-Assist-Systems",
             "Cargo Door Actuation and Assist Systems"),
            ("052-020-Cargo-Door-Inspection-and-Maintenance",
             "Cargo Door Inspection and Maintenance"),
            ("052-020-S1000D-CSDB-Mapping-and-Traceability",
             "S1000D CSDB Mapping and Traceability"),
        ],
    ),
    (
        "052-030-Emergency-Exit-Doors",
        "030",
        "Emergency Exit Doors",
        [
            ("052-030-Emergency-Exit-Doors-Overview",
             "Emergency Exit Doors Overview"),
            ("052-030-Type-I-and-Type-II-Emergency-Exits",
             "Type I and Type II Emergency Exits"),
            ("052-030-Type-III-and-Type-IV-Emergency-Exits",
             "Type III and Type IV Emergency Exits"),
            ("052-030-Exit-Door-Structural-Architecture",
             "Exit Door Structural Architecture"),
            ("052-030-Exit-Door-Activation-and-Release-Mechanisms",
             "Exit Door Activation and Release Mechanisms"),
            ("052-030-Evacuation-Slide-and-Raft-Interfaces",
             "Evacuation Slide and Raft Interfaces"),
            ("052-030-Exit-Door-Sealing-and-Environmental-Protection",
             "Exit Door Sealing and Environmental Protection"),
            ("052-030-Exit-Door-Warning-and-Annunciation",
             "Exit Door Warning and Annunciation"),
            ("052-030-Emergency-Exit-Inspection-and-Maintenance",
             "Emergency Exit Inspection and Maintenance"),
            ("052-030-S1000D-CSDB-Mapping-and-Traceability",
             "S1000D CSDB Mapping and Traceability"),
        ],
    ),
    (
        "052-040-Service-and-Access-Doors",
        "040",
        "Service and Access Doors",
        [
            ("052-040-Service-and-Access-Doors-Overview",
             "Service and Access Doors Overview"),
            ("052-040-Avionics-Bay-Access-Doors",
             "Avionics Bay Access Doors"),
            ("052-040-Fuel-Access-Panels-and-Doors",
             "Fuel Access Panels and Doors"),
            ("052-040-APU-Access-Doors",
             "APU Access Doors"),
            ("052-040-Landing-Gear-Bay-Access-Doors",
             "Landing Gear Bay Access Doors"),
            ("052-040-Hydraulic-and-Fluid-Access-Panels",
             "Hydraulic and Fluid Access Panels"),
            ("052-040-Electrical-and-EWIS-Access-Panels",
             "Electrical and EWIS Access Panels"),
            ("052-040-Access-Door-Sealing-and-Retention",
             "Access Door Sealing and Retention"),
            ("052-040-Service-Access-Inspection-and-Maintenance",
             "Service Access Inspection and Maintenance"),
            ("052-040-S1000D-CSDB-Mapping-and-Traceability",
             "S1000D CSDB Mapping and Traceability"),
        ],
    ),
    (
        "052-050-Door-Structural-Architecture",
        "050",
        "Door Structural Architecture",
        [
            ("052-050-Door-Structural-Architecture-Overview",
             "Door Structural Architecture Overview"),
            ("052-050-Door-Frame-and-Cutout-Structural-Load-Paths",
             "Door Frame and Cutout Structural Load Paths"),
            ("052-050-Door-Skin-and-Panel-Structural-Design",
             "Door Skin and Panel Structural Design"),
            ("052-050-Hinge-Arms-Fittings-and-Attachments",
             "Hinge Arms, Fittings and Attachments"),
            ("052-050-Sill-Beam-Header-and-Jamb-Structures",
             "Sill Beam, Header and Jamb Structures"),
            ("052-050-Door-Surround-Reinforcement-and-Doubler-Design",
             "Door Surround Reinforcement and Doubler Design"),
            ("052-050-Pressurization-and-Structural-Load-Distribution",
             "Pressurization and Structural Load Distribution"),
            ("052-050-Door-Structure-Fatigue-and-Damage-Tolerance",
             "Door Structure Fatigue and Damage Tolerance"),
            ("052-050-Door-Structure-Repair-and-Allowable-Damage",
             "Door Structure Repair and Allowable Damage"),
            ("052-050-S1000D-CSDB-Mapping-and-Traceability",
             "S1000D CSDB Mapping and Traceability"),
        ],
    ),
    (
        "052-060-Door-Sealing-and-Weatherproofing",
        "060",
        "Door Sealing and Weatherproofing",
        [
            ("052-060-Door-Sealing-and-Weatherproofing-Overview",
             "Door Sealing and Weatherproofing Overview"),
            ("052-060-Pressurization-Seal-Architecture",
             "Pressurization Seal Architecture"),
            ("052-060-Weatherstrip-and-Secondary-Sealing",
             "Weatherstrip and Secondary Sealing"),
            ("052-060-Drainage-and-Moisture-Control",
             "Drainage and Moisture Control"),
            ("052-060-Seal-Installation-and-Replacement-Practices",
             "Seal Installation and Replacement Practices"),
            ("052-060-Seal-Material-Specifications-and-Approvals",
             "Seal Material Specifications and Approvals"),
            ("052-060-Acoustic-and-Thermal-Sealing",
             "Acoustic and Thermal Sealing"),
            ("052-060-Seal-Inspection-and-Acceptance-Criteria",
             "Seal Inspection and Acceptance Criteria"),
            ("052-060-Sealing-System-Troubleshooting",
             "Sealing System Troubleshooting"),
            ("052-060-S1000D-CSDB-Mapping-and-Traceability",
             "S1000D CSDB Mapping and Traceability"),
        ],
    ),
    (
        "052-070-Door-Warning-and-Indication-Systems",
        "070",
        "Door Warning and Indication Systems",
        [
            ("052-070-Door-Warning-and-Indication-Systems-Overview",
             "Door Warning and Indication Systems Overview"),
            ("052-070-Door-Open-and-Closed-Sensing",
             "Door Open and Closed Sensing"),
            ("052-070-Door-Lock-and-Latch-Position-Indication",
             "Door Lock and Latch Position Indication"),
            ("052-070-Cockpit-Door-Warning-Annunciation",
             "Cockpit Door Warning Annunciation"),
            ("052-070-Cabin-Door-Arming-and-Disarming-Logic",
             "Cabin Door Arming and Disarming Logic"),
            ("052-070-Door-Warning-System-Architecture-and-Wiring",
             "Door Warning System Architecture and Wiring"),
            ("052-070-Emergency-Exit-Indication-and-Signage",
             "Emergency Exit Indication and Signage"),
            ("052-070-Door-Warning-BITE-and-Diagnostics",
             "Door Warning BITE and Diagnostics"),
            ("052-070-Door-Warning-System-Inspection-and-Maintenance",
             "Door Warning System Inspection and Maintenance"),
            ("052-070-S1000D-CSDB-Mapping-and-Traceability",
             "S1000D CSDB Mapping and Traceability"),
        ],
    ),
    (
        "052-080-Door-Actuation-and-Assist-Systems",
        "080",
        "Door Actuation and Assist Systems",
        [
            ("052-080-Door-Actuation-and-Assist-Systems-Overview",
             "Door Actuation and Assist Systems Overview"),
            ("052-080-Door-Dampers-and-Check-Devices",
             "Door Dampers and Check Devices"),
            ("052-080-Power-Assist-and-Powered-Door-Actuation",
             "Power Assist and Powered Door Actuation"),
            ("052-080-Door-Opening-Force-and-Ergonomics",
             "Door Opening Force and Ergonomics"),
            ("052-080-Door-Gust-Lock-and-Hold-Open-Devices",
             "Door Gust Lock and Hold-Open Devices"),
            ("052-080-Cargo-Door-Hydraulic-or-Electric-Actuation",
             "Cargo Door Hydraulic or Electric Actuation"),
            ("052-080-Door-Drive-and-Gear-Mechanisms",
             "Door Drive and Gear Mechanisms"),
            ("052-080-Actuation-System-Failure-Modes-and-Safety",
             "Actuation System Failure Modes and Safety"),
            ("052-080-Door-Actuation-Inspection-and-Maintenance",
             "Door Actuation Inspection and Maintenance"),
            ("052-080-S1000D-CSDB-Mapping-and-Traceability",
             "S1000D CSDB Mapping and Traceability"),
        ],
    ),
    (
        "052-090-S1000D-CSDB-Mapping-and-Traceability",
        "090",
        "S1000D CSDB Mapping and Traceability",
        [
            ("052-090-S1000D-CSDB-Mapping-and-Traceability-Overview",
             "S1000D CSDB Mapping and Traceability Overview"),
            ("052-090-ATA-SNS-to-ATLAS-Doors-Mapping",
             "ATA SNS to ATLAS Doors Mapping"),
            ("052-090-DMC-Naming-Rules-and-Data-Module-Structure",
             "DMC Naming Rules and Data Module Structure"),
            ("052-090-BREX-Business-Rules-and-Validation-Logic",
             "BREX Business Rules and Validation Logic"),
            ("052-090-DMRL-Planning-and-Data-Module-Register",
             "DMRL Planning and Data Module Register"),
            ("052-090-Applicability-Effectivity-and-Configuration-Control",
             "Applicability, Effectivity and Configuration Control"),
            ("052-090-ICN-Illustration-and-Media-Traceability",
             "ICN Illustration and Media Traceability"),
            ("052-090-Procedure-Fault-Isolation-and-IPD-Cross-References",
             "Procedure, Fault Isolation and IPD Cross-References"),
            ("052-090-Evidence-Ledger-and-Change-Control-Traceability",
             "Evidence Ledger and Change Control Traceability"),
            ("052-090-Repository-Path-and-GitHub-Traceability",
             "Repository Path and GitHub Traceability"),
        ],
    ),
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def upper_slug(filename_no_ext: str) -> str:
    return filename_no_ext.upper()


def doc_id(nnn: str, slug: str) -> str:
    return f"QATL-ATLAS-1000-ATLAS-050-059-05-052-{nnn}-{upper_slug(slug)}"


def topic_md(folder: str, nnn: str, sub_title: str, slug: str, title: str) -> str:
    did = doc_id(nnn, slug)
    short = title.split("—")[-1].strip() if "—" in title else title
    topic_keyword = title  # used in prose sections

    return f"""---
document_id: "{did}"
title: "ATLAS 050-059 · 05.052.{nnn} — {title}"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../../../README.md
parent_section_doc: ../../../README.md
parent_subsection_doc: ../../README.md
parent_subsubject_doc: ./README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "050-059"
section: "05"
section_title: "Estructuras"
subsection: "052"
subsection_title: "Doors"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
subsubject: "{nnn}"
subsubject_title: "{sub_title}"
---
# ATLAS 050-059 · 05.052.{nnn} — {title}

> 05.052.{nnn} | {sub_title}

## 1. Purpose

This document defines **{title}** within the 052.{nnn} subsubject of the Q+ATLANTIDE ATLAS 050-059 Estructuras / 052 Doors section. It establishes the technical scope, key parameters, and programme governance applicable to this topic.

## 2. Scope

### 2.1 Context

This document addresses **{topic_keyword}** as part of the 052.{nnn} subsubject within the Q+ATLANTIDE ATLAS 050-059 Estructuras section. It defines the technical boundaries, key parameters, and interfaces relevant to this topic across all Q+ programme configurations.

The scope encompasses design, analysis, and documentation activities applicable to door systems where {topic_keyword.lower()} considerations are relevant. Applicability is governed by the effectivity codes defined in the programme CSDB.

Compliance and traceability to CS-25, ARP4754A, and programme-level requirements are maintained through the ATLAS governance process.

### 2.2 Scope Diagram

```mermaid
graph TD
    A["052.{nnn} {sub_title}"] --> B["{title}"]
    B --> C[Requirements]
    B --> D[Analysis / Design]
    B --> E[Verification]
    B --> F[Documentation]
    C --> G[Compliance Matrix]
    D --> H[Models / Reports]
    E --> I[Test Evidence]
    F --> J[CSDB / ATLAS]
```

## 3. Footprint

| Attribute | Value |
|-----------|-------|
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/052_Doors/{folder}/` |
| Document ID prefix | `QATL-ATLAS-1000-ATLAS-050-059-05-052-{nnn}` |
| Subsection | 052 — Doors |
| Subsubject | {nnn} — {sub_title} |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |

## 4. References

| Ref | Document | Applicability |
|-----|----------|---------------|
| [1] | CS-25 Subpart C — Structure | All variants |
| [2] | ARP4754A — Development of Civil Aircraft Systems | All |
| [3] | Q+ATLANTIDE ATLAS 050-059 README | Section governance |
| [4] | S1000D Issue 5.0 — Data Module structure | CSDB delivery |
"""


def readme_md(folder: str, nnn: str, sub_title: str, topics: list) -> str:
    did = f"QATL-ATLAS-1000-ATLAS-050-059-05-052-{nnn}-INDEX"
    rows = "\n".join(
        f"| [{slug}.md](./{slug}.md) | {doc_id(nnn, slug)} | {title} | DRAFT |"
        for slug, title in topics
    )

    return f"""---
document_id: "{did}"
title: "ATLAS 050-059 · 05.052.{nnn} — {sub_title}"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../../../README.md
parent_section_doc: ../../../README.md
parent_subsection_doc: ../../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "050-059"
section: "05"
section_title: "Estructuras"
subsection: "052"
subsection_title: "Doors"
primary_q_division: Q-STRUCTURES
support_q_divisions: [Q-AIR, Q-INDUSTRY, Q-HPC]
orb_function_support: [ORB-PMO, ORB-FIN, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: draft
language: en
subsubject: "{nnn}"
subsubject_title: "{sub_title}"
---
# ATLAS 050-059 · 05.052.{nnn} — {sub_title}

> Subsubject Index

## 1. Purpose

This index covers **05.052.{nnn} — {sub_title}** within the ATLAS 050-059 Estructuras / 052 Doors section of the Q+ATLANTIDE baseline. It lists all topic documents, their document identifiers, and current status.

## 2. Document Index

| File | Document ID | Topic | Status |
|------|-------------|-------|--------|
{rows}

## 3. Footprint

| Attribute | Value |
|-----------|-------|
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/050-059_Estructuras/052_Doors/{folder}/` |
| Files | 11 (README + 10 topic documents) |
| Status | ![DRAFT](https://img.shields.io/badge/status-DRAFT-yellow) |
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

created = 0

for folder, nnn, sub_title, topics in SUBSUBJECTS:
    folder_path = os.path.join(BASE, folder)
    os.makedirs(folder_path, exist_ok=True)

    # README
    readme_path = os.path.join(folder_path, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_md(folder, nnn, sub_title, topics))
    created += 1

    # Topic files
    for slug, title in topics:
        topic_path = os.path.join(folder_path, f"{slug}.md")
        with open(topic_path, "w", encoding="utf-8") as f:
            f.write(topic_md(folder, nnn, sub_title, slug, title))
        created += 1

print(f"Done — {created} files created across {len(SUBSUBJECTS)} subsubject folders.")
