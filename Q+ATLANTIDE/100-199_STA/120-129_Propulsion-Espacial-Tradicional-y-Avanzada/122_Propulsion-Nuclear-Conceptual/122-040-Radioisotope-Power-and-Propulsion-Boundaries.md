---
document_id: QATL-ATLAS-1000-STA-120-129-02-122-040-RADIOISOTOPE-POWER-AND-PROPULSION-BOUNDARIES
title: "STA 120-129 · 122-040 — Radioisotope Power and Propulsion Boundaries"
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
subsection: "122"
subsubject: "040"
subsubject_title: "Radioisotope Power and Propulsion Boundaries"
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HPC, ORB-LEG]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · 122-040 — Radioisotope Power and Propulsion Boundaries

## 1. Purpose

Defines the **conceptual boundaries for radioisotope power and propulsion systems** within the Q+ATLANTIDE STA band.

## 2. Scope

- **Conceptual-only boundary** — All content is conceptual-level; no radioisotope material specifications, handling procedures, or launch safety analysis details.
- **RTG / MMRTG power concept** — ²³⁸Pu decay heat converted to electricity via thermoelectric effect; typical: MMRTG ~110 W_e at beginning-of-mission; mission heritage: Cassini, Curiosity, Perseverance; power source for NEP subsystems.
- **ASRG / Stirling concept** — Advanced Stirling Radioisotope Generator; higher efficiency (>4× thermoelectric); reduces Pu-238 inventory requirement; development programme.
- **Propulsion application boundary** — RPS electricity drives electric thrusters (NEP); micro-RPS concepts drive µN-class thrusters; no direct radioisotope thermal propulsion in this subsection (→ `002` NTP for thermally-driven concepts).
- **Safety regulatory boundary** — Launch approval requires nuclear safety review per NASA-NSS 1676.1[^nasanss16761]; environmental impact statement; IAEA safeguards where applicable; Outer Space Treaty compliance.

## 3. Diagram — RPS Power Boundary

```mermaid
flowchart LR
    A["²³⁸Pu Fuel<br/>(conceptual boundary only)"] --> B["MMRTG/ASRG<br/>(thermoelectric/Stirling)"]
    B --> C["Spacecraft Bus Power<br/>(100W_e class)"]
    C --> D["EP Thruster<br/>(micro-NEP concept)"]
    B --> E["Safety Review<br/>(NASA-NSS 1676.1)"]
    style A fill:#7b0000,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `122` — Propulsión Nuclear Conceptual |
| Subsubject | `004` — Radioisotope Power and Propulsion Boundaries |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Safety boundary | conceptual-only |
| Document | `122-040-Radioisotope-Power-and-Propulsion-Boundaries.md` (this file) |

## 5. References & Citations

[^nasanss16761]: **NASA-NSS 1676.1 — Nuclear Safety Policy**.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- NASA-NSS 1676.1 — Nuclear Safety Policy[^nasanss16761]
- IAEA Safety Standards — Applicable series for space nuclear power sources
