---
document_id: QATL-ATLAS-1000-STA-120-129-02-120-002-PROPELLANT-FAMILIES-AND-SELECTION-CRITERIA
title: "STA 120-129 · 02.120.002 — Propellant Families and Selection Criteria"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "120-129"
section: "02"
section_title: "Propulsión Espacial Tradicional y Avanzada"
subsection: "120"
subsection_title: "Propulsión Química"
subsubject: "002"
subsubject_title: "Propellant Families and Selection Criteria"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · Section 02 · Subsection 120 · Subsubject 002 — Propellant Families and Selection Criteria

## 1. Purpose

Defines the **taxonomy of chemical propellant families** — bipropellant, monopropellant, solid, and hybrid — and the mission-level selection criteria (Isp, storability, toxicity, temperature range, heritage).

## 2. Scope

- Propellant families: MON/MMH, NTO/UDMH (hypergolic bipropellant); LOX/LH₂, LOX/RP-1, LOX/LCH₄ (cryogenic bipropellant); hydrazine, AF-M315E, LMP-103S (monopropellant); HTPB/AP/Al (composite solid); hybrid (N₂O/HTPB).
- Selection criteria: delivered Isp; storability (pressure vs. cryogenic); toxicity class (REACH/GHS); mission impulse budget; heritage and TRL; compatibility with feed system materials (→ `007`).

## 3. Diagram — Propellant Family Taxonomy

```mermaid
flowchart TD
    CHEM["Chemical Propellant Families"]
    CHEM --> BPROP["Bipropellant<br/>(MON/MMH · NTO/UDMH · LOX/LH₂ · LOX/RP-1 · LOX/CH₄)"]
    CHEM --> MONO["Monopropellant<br/>(N₂H₄ · AF-M315E · LMP-103S)"]
    CHEM --> SOLID["Solid<br/>(HTPB/AP/Al composite)"]
    CHEM --> HYBRID["Hybrid<br/>(N₂O + HTPB)"]
    BPROP --> ISP["High Isp (300–460 s)"]
    MONO --> ISP2["Moderate Isp (220–260 s)"]
    SOLID --> ISP3["Moderate Isp (250–280 s)"]
    style CHEM fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `120` — Propulsión Química |
| Subsubject | `002` — Propellant Families and Selection Criteria |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `002_Propellant-Families-and-Selection-Criteria.md` (this file) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-35C — Propulsion General Requirements
- NASA-STD-8719.15 — Safety Standard for Explosives, Propellants and Pyrotechnics
