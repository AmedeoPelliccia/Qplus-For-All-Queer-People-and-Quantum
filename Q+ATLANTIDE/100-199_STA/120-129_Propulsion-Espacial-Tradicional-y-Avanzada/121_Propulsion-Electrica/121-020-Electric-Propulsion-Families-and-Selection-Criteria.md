---
document_id: QATL-ATLAS-1000-STA-120-129-02-121-020-ELECTRIC-PROPULSION-FAMILIES-AND-SELECTION-CRITERIA
title: "STA 120-129 · 121-020 — Electric Propulsion Families and Selection Criteria"
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
subsection: "121"
subsubject: "020"
subsubject_title: "Electric Propulsion Families and Selection Criteria"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-HPC, Q-DATAGOV, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · 121-020 — Electric Propulsion Families and Selection Criteria

## 1. Purpose

Defines the **taxonomy of electric propulsion families** and establishes the selection criteria framework for Q+ATLANTIDE STA-band platforms.

## 2. Scope

- **Electrothermal family** — Resistojets (P < 1 kW, Isp 150–300 s), arcjets (P 0.5–30 kW, Isp 500–1 800 s), microwave electrothermal. Selected for low-delta-V attitude maintenance and drag compensation.
- **Electrostatic family** — Gridded ion engines (Isp 2 000–10 000 s, thrust 0.1–250 mN), Hall-effect thrusters (Isp 1 500–3 500 s, thrust 5 mN–1 N). Selected for orbit raising, GEO station-keeping, and interplanetary missions.
- **Electromagnetic family** — Magnetoplasmadynamic (MPD) thrusters (Isp 1 000–8 000 s, thrust up to 200 N applied), pulsed plasma thrusters (PPT, micro-Newton to milli-Newton range). Selected for high-power future missions and precision attitude control.
- **Selection criteria** — Mission ΔV budget, power availability (solar or RTG), propellant mass fraction, Isp target, thruster lifetime, qualification status, plume compatibility.

## 3. Diagram — Electric Propulsion Family Taxonomy

```mermaid
flowchart TD
    A["Electric Propulsion Families (002)"]
    A --> B["Electrothermal<br/>(resistojet · arcjet)"]
    A --> C["Electrostatic<br/>(ion · Hall HET)"]
    A --> D["Electromagnetic<br/>(MPD · PPT)"]
    B --> E["003 — Electrothermal Detail"]
    C --> F["004 — Ion & Hall Detail"]
    D --> G["005 — MPD & PPT Detail"]
    style A fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `121` — Propulsión Eléctrica |
| Subsubject | `002` — EP Families and Selection Criteria |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `121-020-Electric-Propulsion-Families-and-Selection-Criteria.md` (this file) |

## 5. References & Citations

[^ecssest35]: **ECSS-E-ST-35C — Propulsion General Requirements**.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-35C — Propulsion General Requirements[^ecssest35]
