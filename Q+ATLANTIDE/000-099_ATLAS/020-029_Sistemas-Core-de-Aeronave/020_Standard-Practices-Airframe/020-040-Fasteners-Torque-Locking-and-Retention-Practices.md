---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-020-040-FASTENERS-TORQUE-LOCKING-AND-RETENTION-PRACTICES
title: "ATLAS 020-029 · 02.020 · Section 020-040 — Fasteners, Torque, Locking and Retention Practices"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "020-029"
section: "02"
section_title: "Sistemas Core de Aeronave"
subsection: "020"
subsection_title: "Standard Practices Airframe"
local_section_code: "020-040"
ata_sns: "20-40-00"
title_short: "Fasteners, Torque, Locking and Retention Practices"
primary_q_division: Q-GROUND
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-AIR, Q-INDUSTRY, Q-MECHANICS]
governance_class: baseline
version: 1.0.0
status: deprecated
node_class: legacy-deprecated-compatibility-node
language: en
---

# ATLAS 020-029 · 02.020 · 020-040 — Fasteners, Torque, Locking and Retention Practices

> **⚠ DEPRECATED / LEGACY COMPATIBILITY NODE** — See [`README.md`](./README.md) for migration guidance.

## 1. Purpose

Define the fastener selection, torque specification, locking device, and retention practice standards within ATLAS subsection `020`, aligned to ATA SNS `20-40-00`. Establishes the controlled fastener engineering practices applicable across all airframe assembly and maintenance tasks.

## 2. Scope

- Covers fastener type selection (bolts, screws, rivets, hi-locks, cherry-max, blind fasteners) and installation standards.
- Defines torque tables, torque wrench calibration requirements, and wet-torque practices for sealed joints.
- Establishes locking device selection (castellated nuts and cotter pins, self-locking nuts, safety wire, thread-locking compounds, tab washers).
- Applies to all airframe structural fastening; does not replace aircraft structural repair manual (SRM) or AMM task-level torque tables.

## 3. System Architecture

```mermaid
graph TD
    A020_040["020-040 Fasteners, Torque,\nLocking and Retention Practices\n(ATA 20-40-00)"] --> F1["Fastener Type\nSelection Standards"]
    A020_040 --> F2["Torque Tables and\nWrench Calibration"]
    A020_040 --> F3["Wet-torque and\nSealed-joint Practices"]
    A020_040 --> F4["Locking Device\nSelection and Installation"]
    A020_040 --> F5["Fastener Inspection\nand Replacement Criteria"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Code range | `020-029` |
| Subsection | `020` — Standard Practices Airframe |
| Local section code | `020-040` |
| ATA SNS | `20-40-00` |
| Primary Q-Division | Q-GROUND |
| Governance class | `baseline` |
| Status | `deprecated` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/020_Standard-Practices-Airframe/` |
| Document | `020-040-Fasteners-Torque-Locking-and-Retention-Practices.md` |

## 5. References

- ATA iSpec 2200 — Chapter 20-40, Standard Practices Airframe — Fasteners and Torque
- Subsection index [`./README.md`](./README.md)
- General [`./020-000-General.md`](./020-000-General.md)
