---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-020-060-CLEANING-PROTECTION-AND-SURFACE-CONDITION-CONTROL
title: "ATLAS 020-029 · 02.020 · Section 020-060 — Cleaning, Protection and Surface Condition Control"
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
local_section_code: "020-060"
ata_sns: "20-60-00"
title_short: "Cleaning, Protection and Surface Condition Control"
primary_q_division: Q-GROUND
support_q_divisions: [Q-STRUCTURES, Q-DATAGOV, Q-AIR, Q-INDUSTRY, Q-MECHANICS]
governance_class: baseline
version: 1.0.0
status: deprecated
node_class: legacy-deprecated-compatibility-node
language: en
---

# ATLAS 020-029 · 02.020 · 020-060 — Cleaning, Protection and Surface Condition Control

> **⚠ DEPRECATED / LEGACY COMPATIBILITY NODE** — See [`README.md`](./README.md) for migration guidance.

## 1. Purpose

Define the cleaning procedures, surface protection schemes, and surface condition assessment standards within ATLAS subsection `020`, aligned to ATA SNS `20-60-00`. Establishes the controlled practices for maintaining airframe surface integrity across all maintenance events.

## 2. Scope

- Covers approved cleaning agent selection, application methods, and rinse-down procedures for metallic, composite, and coated surfaces.
- Defines surface protection coatings (corrosion inhibiting compounds, primers, topcoats, anodising, plating) and application controls.
- Establishes surface condition assessment criteria: paint condition grading, corrosion classification (levels I–IV), and acceptance/rejection thresholds.
- Covers pre-treatment of composite repair areas, surface cleaning prior to sealing, and FOD recovery after cleaning operations.
- Does not replace aircraft structural repair manual (SRM) corrosion repair task cards or AMM exterior cleaning procedures.

## 3. System Architecture

```mermaid
graph TD
    A020_060["020-060 Cleaning, Protection\nand Surface Condition Control\n(ATA 20-60-00)"] --> C1["Cleaning Agent Selection\nand Application Methods"]
    A020_060 --> C2["Surface Protection\nCoating Schemes"]
    A020_060 --> C3["Corrosion Classification\nand Assessment Criteria"]
    A020_060 --> C4["Composite Surface\nPre-treatment Controls"]
    A020_060 --> C5["FOD Recovery and\nClose-out Verification"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Code range | `020-029` |
| Subsection | `020` — Standard Practices Airframe |
| Local section code | `020-060` |
| ATA SNS | `20-60-00` |
| Primary Q-Division | Q-GROUND |
| Governance class | `baseline` |
| Status | `deprecated` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/020_Standard-Practices-Airframe/` |
| Document | `020-060-Cleaning-Protection-and-Surface-Condition-Control.md` |

## 5. References

- ATA iSpec 2200 — Chapter 20-60, Standard Practices Airframe — Cleaning and Protection
- Subsection index [`./README.md`](./README.md)
- General [`./020-000-General.md`](./020-000-General.md)
