---
document_id: QATL-ATLAS-1000-STA-130-139-03-131-020-CELL-CHEMISTRIES-AND-STORAGE-TECHNOLOGY-FAMILIES
title: "STA 130-139 · 131-020 — Cell Chemistries and Storage Technology Families"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "130-139"
section: "03"
subsection: "131"
subsubject: "020"
subsubject_title: "Cell Chemistries and Storage Technology Families"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · 131-020 — Cell Chemistries and Storage Technology Families

## 1. Purpose

Establishes the **taxonomy of electrochemical cell chemistries and storage technology families** applicable to Q+ATLANTIDE STA-band space platforms.

## 2. Scope

- **Lithium-ion (Li-ion)** — NMC, LCO, LFP cathodes; graphite anode; specific energy 150–250 Wh/kg; dominant for LEO/GEO spacecraft; DOD limit ≤ 30% LEO, ≤ 80% GEO.
- **Lithium-polymer (Li-Po)** — similar chemistry to Li-ion; flexible pouch cell; lower specific energy but lighter packaging.
- **Nickel-Hydrogen (Ni-H₂)** — heritage GEO technology; high cycle life (>30,000 cycles); lower specific energy (50–60 Wh/kg); phased out for new designs but still in legacy systems.
- **Nickel-Cadmium (NiCd)** — legacy LEO; low specific energy; superseded by Li-ion in most applications.
- **Solid-state (emerging)** — ceramic/polymer electrolyte; improved safety; TRL 4–5 for space; no established qualification standard.
- **Selection criteria** — specific energy, cycle life, operational temperature range, radiation tolerance, TRL, and safety risk.

## 3. Diagram — Cell Chemistry Taxonomy

```mermaid
flowchart TD
    A["Storage Technology\nSelection"] --> B["Li-ion\n(NMC/LCO/LFP)\nLEO/GEO baseline"]
    A --> C["Ni-H₂\nHeritage GEO"]
    A --> D["NiCd\nLegacy LEO"]
    A --> E["Solid-State\nEmerging TRL4-5"]
    B --> F["DOD / C-rate / Temp\nConstraints (→ 004)"]
    style A fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `131` — Baterías y Almacenamiento |
| Subsubject | `002` — Cell Chemistries and Storage Technology Families |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |

## 5. References & Citations

[^ecssest2010c]: **ECSS-E-ST-20-10C — Batteries**.
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards
- ECSS-E-ST-20-10C — Batteries[^ecssest2010c]
