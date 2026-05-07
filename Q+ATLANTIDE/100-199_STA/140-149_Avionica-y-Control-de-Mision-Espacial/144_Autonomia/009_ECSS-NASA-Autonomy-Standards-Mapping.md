---
document_id: QATL-ATLAS-1000-STA-140-149-04-144-009-ECSS-NASA-AUTONOMY-STANDARDS-MAPPING
title: "STA 140-149 · 04.144.009 — ECSS-NASA Autonomy Standards Mapping"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "140-149"
section: "04"
section_title: "Aviónica y Control de Misión Espacial"
subsection: "144"
subsection_title: "Autonomía"
subsubject: "009"
subsubject_title: "ECSS-NASA Autonomy Standards Mapping"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 140-149 · Section 04 · Subsection 144 · Subsubject 009 — ECSS-NASA Autonomy Standards Mapping

## 1. Purpose

Maps the applicable **ECSS and NASA standards** to the spacecraft autonomy functional areas within STA `144`, establishing the normative standards hierarchy for Q+ATLANTIDE STA-band autonomous spacecraft systems.

## 2. Scope

- **ECSS standards applicable to autonomy** — ECSS-E-ST-40C (Software Engineering): primary standard for autonomous software development lifecycle, criticality classification, and V&V requirements; ECSS-E-ST-70-41C (Fault Detection, Isolation and Recovery): FDIR architecture and autonomy interaction requirements; ECSS-E-ST-10-02C (Verification): general verification methodology applicable to autonomy V&V evidence gates; ECSS-E-ST-70C (Ground Systems and Operations): human-in-the-loop and ground override interface requirements; ECSS-Q-ST-80C (Software Product Assurance): autonomy software product assurance and configuration control requirements.
- **NASA standards applicable to autonomy** — NASA-STD-8739.8 (Software Assurance Standard): software assurance requirements for mission-critical autonomous functions; NASA-NPR-7120.5 (Space Systems Development): autonomy requirements within the system development lifecycle; NASA-STD-3001 (Human Integration Design Requirements): crew authority and override interfaces for crewed mission autonomous functions; NASA-HDBK-7120.6 (Lessons Learned): autonomy lessons-learned capture and heritage assessment.
- **Emerging AI/ML standards references** — ISO/IEC 42001 (AI Management System): organisational governance framework for AI systems; DO-178C (adapted): software assurance methodology adapted for AI/ML qualification in space applications; EASA AI Roadmap: aviation AI assurance methodology adapted as reference for space AI/ML autonomy admission.
- **Standards applicability matrix** — mapping of each standards requirement to applicable STA `144` subsubject; identification of deviations and waivers; standards version control and update monitoring; tailoring rationale documented for any standards clause not fully applicable.
- **Standards evolution monitoring** — autonomy and AI/ML standards are actively developing; Q+ATLANTIDE baseline shall monitor ECSS and NASA standards updates in autonomy and AI/ML domains; baseline update process triggered on issuance of new autonomy-relevant standards.

## 3. Diagram — Autonomy Standards Hierarchy

```mermaid
flowchart TD
    A["ECSS-E-ST-40C<br/>Software Engineering"] --> B["001 — Controlled Definition"]
    A --> C["003 — Decision Logic"]
    A --> D["008 — V&V / HIL"]
    E["ECSS-E-ST-70-41C<br/>FDIR"] --> F["004 — FDIR Autonomy"]
    G["ECSS-E-ST-70C<br/>Ground Operations"] --> H["006 — HITL & Override"]
    I["NASA-STD-8739.8"] --> J["005 — AI/ML Admission"]
    I --> D
    K["ISO/IEC 42001 · DO-178C adapted"] --> J
    style A fill:#1f3a93,color:#fff
    style E fill:#1f3a93,color:#fff
    style G fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `140-149` |
| Section | `04` — Aviónica y Control de Misión Espacial |
| Subsection | `144` — Autonomía |
| Subsubject | `009` — ECSS-NASA Autonomy Standards Mapping |
| Primary Q-Division | Q-SPACE[^qdiv] |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Document | `009_ECSS-NASA-Autonomy-Standards-Mapping.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |

## 5. References & Citations

[^ecssest40c]: **ECSS-E-ST-40C — Software Engineering** — Primary autonomous software development standard.

[^ecssest7041c]: **ECSS-E-ST-70-41C — Space FDIR** — FDIR architecture and autonomy interaction.

[^ecssest70c]: **ECSS-E-ST-70C — Ground Systems and Operations** — HITL and ground override requirements.

[^nasastd87398]: **NASA-STD-8739.8 — Software Assurance Standard** — NASA autonomy software assurance.

[^isoiec42001]: **ISO/IEC 42001 — AI Management System** — AI governance framework reference.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-40C — Software Engineering[^ecssest40c]
- ECSS-E-ST-70-41C — Space FDIR[^ecssest7041c]
- ECSS-E-ST-70C — Ground Systems and Operations[^ecssest70c]
- NASA-STD-8739.8 — Software Assurance Standard[^nasastd87398]
- ISO/IEC 42001 — AI Management System[^isoiec42001]
