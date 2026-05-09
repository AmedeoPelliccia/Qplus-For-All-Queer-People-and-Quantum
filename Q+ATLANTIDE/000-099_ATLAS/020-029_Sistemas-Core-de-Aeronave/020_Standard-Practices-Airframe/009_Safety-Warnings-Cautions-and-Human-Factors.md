---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-020-009-SAFETY-WARNINGS-CAUTIONS-AND-HUMAN-FACTORS
title: "ATLAS 020-029 · 02.020.009 — Safety, Warnings, Cautions and Human Factors"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "020-029"
section: "02"
section_title: "Sistemas Core de Aeronave"
subsection: "020"
subsection_title: "Standard Practices Airframe"
subsubject: "009"
subsubject_title: "Safety, Warnings, Cautions and Human Factors"
primary_q_division: Q-GROUND
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-AIR, Q-INDUSTRY, Q-MECHANICS]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# ATLAS 020-029 · Section 02 · Subsection 020 · Subsubject 009 — Safety, Warnings, Cautions and Human Factors

## 1. Purpose

Defines the **safety advisory hierarchy, WARNING/CAUTION/NOTE classification rules, hazardous-task pre-work requirements, and human-factors controls** applicable to all standard airframe maintenance tasks within the Q+ATLANTIDE programme. Establishes the controlled framework — WARN/CAU/NOTE placement discipline, lock-out/tag-out interfaces, chemical/electrical/structural hazard controls, distraction management, and check-call procedures — that protects personnel and aircraft during open-access airframe maintenance, in conformance with EASA Part 145[^part145], FAA AC 43.13[^ac4313], and EASA Human Factors guidelines[^hf].

## 2. Scope

- Covers the *Safety, Warnings, Cautions and Human Factors* subsubject (`009`) of subsection `020` *Standard Practices Airframe* within section `02` *Sistemas Core de Aeronave*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Safety advisory hierarchy** — the three-tier advisory system: WARNING (risk of personal injury or death), CAUTION (risk of equipment damage or unairworthy condition), and NOTE (important information requiring emphasis); placement rules requiring all WARNINGs and CAUTIONs to appear before the hazardous step in any procedure or data module.
  - **Hazardous-task pre-work requirements** — mandatory pre-task checks before any hazardous step: aircraft systems de-energised, pressure discharged, fuel isolated, hydraulic pressure vented, and lock-out/tag-out applied per general practices (cross-reference `002_`).
  - **Chemical hazard controls** — personal protective equipment (PPE) requirements for sealants, cleaning agents, and CICs (cross-reference `006_`, `007_`); emergency spill procedures; Safety Data Sheet (SDS) access requirements.
  - **Electrical and structural hazard controls** — shock-risk identification, bonding strap removal sequence (cross-reference `006_`), and structural-support verification before load-path interruption (cross-reference `003_`).
  - **Human-factors error management** — distraction management protocols, maintenance shift-handover procedures, PEAR model application (People, Environment, Actions, Resources), and error-capture checklists per EASA Human Factors guidelines[^hf].
  - **Check-call and independent verification** — mandatory check-call discipline for safety-critical steps (torque-critical fasteners, bonding paths, panel closure); triggers for independent inspection as opposed to self-certification.
- Out of scope: normative definitions (`001_`), general task sequencing (`002_`), zone/access management (`003_`), tool calibration (`004_`), fastener torque (`005_`), sealant and bonding (`006_`), surface treatment (`007_`), NDT protocols (`008_`), and lifecycle record formats (`010_`).

## 3. Diagram — Safety Advisory and Human Factors Control Flow

All hazardous tasks must clear pre-work safety requirements before execution; WARNING/CAUTION placement gates procedure steps; human-factors controls wrap the entire maintenance activity.

```mermaid
flowchart TD
    A["Maintenance Task Identified<br/>(work card · data module)"]:::ctrl
    A --> B["Safety Advisory Review<br/>(WARNING · CAUTION · NOTE<br/>placed before hazardous steps)"]:::safety
    B --> C["Pre-Work Requirements<br/>(de-energise · discharge · isolate<br/>lock-out / tag-out · structural support)"]:::safety
    C --> D["Human Factors Controls<br/>(distraction management · PEAR model<br/>shift-handover brief)"]:::hf
    D --> E["Task Execution<br/>(step-by-step per 002_<br/>PPE per chemical/electrical hazard)"]:::task
    E --> F["Check-Call / Independent Verify<br/>(safety-critical steps:<br/>torque · bonding · panel closure)"]:::safety
    F --> G{"All Safety<br/>Checks Passed?"}:::decision
    G -- No --> H["Stop-Work / Corrective Action<br/>(escalate to licensed certifier<br/>engineering authority if required)"]:::report
    H --> C
    G -- Yes --> I["Post-Task Safety Close-Out<br/>(lock-out removed · energy restored<br/>FOD sweep per 003_)"]:::safety
    I --> J["Record<br/>(safety sign-off · per 010_)"]:::out

    classDef ctrl fill:#1f3a93,stroke:#0b1d4a,color:#fff
    classDef safety fill:#c0392b,stroke:#7b241c,color:#fff
    classDef hf fill:#f6e6ff,stroke:#7d3c98,color:#3b1f4d
    classDef task fill:#eaf3fb,stroke:#2c82c9,color:#0b1d4a
    classDef decision fill:#fff4dd,stroke:#b9770e,color:#5a3b00
    classDef report fill:#fdebd0,stroke:#b9770e,color:#5a3b00
    classDef out fill:#f0f9e8,stroke:#27ae60,color:#145a32
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `020` — Standard Practices Airframe |
| Subsubject | `009` — Safety, Warnings, Cautions and Human Factors |
| Primary Q-Division | Q-GROUND[^qdiv] |
| Support Q-Divisions | Q-STRUCTURES, Q-DATAGOV, Q-AIR, Q-INDUSTRY, Q-MECHANICS |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/020_Standard-Practices-Airframe/` |
| Document | `009_Safety-Warnings-Cautions-and-Human-Factors.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **ATLAS §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `020-029` row.

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^part145]: **EASA Part 145 — Approved Maintenance Organisations** — Regulatory requirements for safety advisory placement, lock-out/tag-out, hazardous task controls, and independent inspection triggers in approved maintenance organisations.

[^ac4313]: **FAA AC 43.13-1B/2B — Acceptable Methods, Techniques and Practices** — Advisory circular defining WARNING/CAUTION/NOTE classification and pre-work safety requirements for airframe maintenance tasks.

[^hf]: **EASA Human Factors Guidelines for Aircraft Maintenance** — Advisory material on PEAR model application, distraction management, shift-handover protocols, and error-capture checklists in maintenance environments.

### Applicable industry standards

The following standards apply to this subsubject in addition to the cross-cutting Q+ATLANTIDE governance:

- EASA Part 145 — Approved Maintenance Organisations[^part145]
- FAA AC 43.13-1B/2B — Acceptable Methods, Techniques and Practices[^ac4313]
- EASA Human Factors Guidelines for Aircraft Maintenance[^hf]
