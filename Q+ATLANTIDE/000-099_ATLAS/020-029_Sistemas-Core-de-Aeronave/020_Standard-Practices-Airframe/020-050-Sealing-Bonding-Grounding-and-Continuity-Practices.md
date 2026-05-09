---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-020-050-SEALING-BONDING-GROUNDING-AND-CONTINUITY-PRACTICES
title: "ATLAS 020-029 · 02.020 · Section 020-050 — Sealing, Bonding, Grounding and Continuity Practices"
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
local_section_code: "020-050"
ata_sns: "20-50-00"
title_short: "Sealing, Bonding, Grounding and Continuity Practices"
primary_q_division: Q-GROUND
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-AIR, Q-INDUSTRY, Q-MECHANICS]
governance_class: baseline
version: 1.0.0
status: deprecated
node_class: legacy-deprecated-compatibility-node
language: en
---

# ATLAS 020-029 · 02.020 · 020-050 — Sealing, Bonding, Grounding and Continuity Practices

> **⚠ DEPRECATED / LEGACY COMPATIBILITY NODE** — See [`README.md`](./README.md) for migration guidance.

## 1. Purpose

Define the sealing compound application, structural bonding, electrical bonding, grounding, and electrical continuity verification standards within ATLAS subsection `020`, aligned to ATA SNS `20-50-00`. Establishes the controlled practices applicable across all airframe sealing, adhesive bonding, and electrical grounding tasks.

## 2. Scope

- Covers sealant application methods (faying-surface sealing, fillet sealing, injection sealing) and cure-time controls.
- Defines structural adhesive bonding surface preparation, application, and proof-load acceptance criteria.
- Establishes electrical bonding jumper installation, resistance acceptance limits (≤ 2.5 mΩ typical), and continuity test procedures.
- Covers lightning protection zone bonding, static discharge paths, and HIRF protection continuity.
- Applies across all airframe zones; does not replace aircraft structural repair manual (SRM), AMM task cards, or electrical wiring interconnect system (EWIS) manuals.

## 3. System Architecture

```mermaid
graph TD
    A020_050["020-050 Sealing, Bonding,\nGrounding and Continuity Practices\n(ATA 20-50-00)"] --> S1["Sealant Application\nMethods and Controls"]
    A020_050 --> S2["Structural Adhesive\nBonding Practices"]
    A020_050 --> S3["Electrical Bonding\nJumper Installation"]
    A020_050 --> S4["Continuity Test\nProcedures and Limits"]
    A020_050 --> S5["Lightning Protection\nand HIRF Bonding"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Code range | `020-029` |
| Subsection | `020` — Standard Practices Airframe |
| Local section code | `020-050` |
| ATA SNS | `20-50-00` |
| Primary Q-Division | Q-GROUND |
| Governance class | `baseline` |
| Status | `deprecated` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/020_Standard-Practices-Airframe/` |
| Document | `020-050-Sealing-Bonding-Grounding-and-Continuity-Practices.md` |

## 5. References

- ATA iSpec 2200 — Chapter 20-50, Standard Practices Airframe — Sealing and Bonding
- Subsection index [`./README.md`](./README.md)
- General [`./020-000-General.md`](./020-000-General.md)
