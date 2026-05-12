---
document_id: QATL-ATLAS-1000-STA-100-109-00-106-050-NUTRITION-PHARMACOLOGY-AND-METABOLIC-SUPPORT
title: "STA 100-109 · 106-050 — Nutrition-Pharmacology-and-Metabolic-Support"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "100-109"
section: "00"
section_title: "Sistemas Generales y Soporte Vital Espacial"
subsection: "106"
subsection_title: "Salud Tripulación y Factores Humanos"
subsubject: "050"
subsubject_title: "Nutrition-Pharmacology-and-Metabolic-Support"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 106-050 — Nutrition-Pharmacology-and-Metabolic-Support

## 1. Purpose

Defines the **nutrition, pharmacology, and metabolic support** requirements for Q+ATLANTIDE crewed missions, specifying caloric and micronutrient requirements, food system design, on-board pharmacy, and metabolic monitoring per NASA-STD-3001[^nastd3001].

Crew caloric requirements: 2000–3200 kcal/day depending on activity level; protein 0.8–1.5 g/kg/day; Ca 1000–1500 mg/day (bone loss countermeasure); Vitamin D 1000–2000 IU/day (no sunlight exposure); iron absorption monitored (elevated from haemolysis). Food system provides ≥ 3 months of shelf-stable, fully nutritional, palatable food (≥ 25 menu items per week for psychological variety). On-board pharmacy: ≥ 5-day supply of mission-critical medications (analgesics, antibiotics, antiemetics, cardiovascular, sedatives); drug stability in space radiation environment verified. Metabolic monitoring: urine/blood biomarkers for nutritional status assessment.

## 2. Scope

- Covers the *Nutrition-Pharmacology-and-Metabolic-Support* subsubject (`050`) of subsection `106`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All design decisions and monitoring thresholds traceable to NASA-STD-3001[^nastd3001] and CSDB evidence per subsection `109`.

## 3. Diagram — Nutrition-Pharmacology-and-Metabolic-Support

```mermaid
flowchart TB
    FOOD["Food System<br/>(2000–3200 kcal/day · ≥ 3 months shelf-stable)"]
    PHARMA["On-board Pharmacy<br/>(mission-critical medications)"]
    SUPPL["Nutritional Supplements<br/>(Ca · Vit D · antioxidants)"]

    FOOD & PHARMA & SUPPL --> CREW_MET["Crew Metabolic Status<br/>(biomarker monitoring)"]
    CREW_MET --> CMO["CMO / Flight Surgeon<br/>(nutritional prescription)"]
    FOOD --> VARIETY["Menu Variety<br/>(≥ 25 items/week · psychological)"]
    style CREW_MET fill:#2c82c9,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `106` — Salud Tripulación y Factores Humanos |
| Subsubject | `050` — Nutrition-Pharmacology-and-Metabolic-Support |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/106_Salud-Tripulacion-y-Factores-Humanos/` |
| Document | `106-050-Nutrition-Pharmacology-and-Metabolic-Support.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`106-000-General.md`](./106-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management.

[^nastd3001]: **NASA-STD-3001 Vol.1 & Vol.2 — Human Integration Design Handbook / Human Factors, Habitability, and Environmental Health** — Primary standard for crew health, physical performance, and medical monitoring requirements.

[^nasahf]: **NASA/SP-2010-3407 — Human Integration Design Handbook (HIDH)** — Comprehensive human factors guidance for crewed spacecraft design.

[^ecsse10]: **ECSS-E-HB-10-12A — Methods for the Calculation of Reliability** — Reliability and human factors engineering methodology applicable to crew health monitoring systems.

[^iso9241]: **ISO 9241-11:2018 — Ergonomics of Human-System Interaction** — Usability and ergonomics standards applicable to crew health monitoring interfaces.

### Applicable industry standards

- NASA-STD-3001 Vol.1 & Vol.2 — Human Integration Design Handbook[^nastd3001]
- NASA/SP-2010-3407 — Human Integration Design Handbook[^nasahf]
- ECSS-E-HB-10-12A — Methods for the Calculation of Reliability[^ecsse10]
- ISO 9241-11:2018 — Ergonomics of Human-System Interaction[^iso9241]

[^ncrp132]: **NCRP Report No. 132 — Radiation Protection Guidance for Activities in Low-Earth Orbit** — Career dose limits and SPE protection requirements for crewed space missions.

[^milstd1472]: **MIL-STD-1472G — Human Engineering** — Anthropometric, display, control, and cognitive load requirements applicable to crewed spacecraft.
