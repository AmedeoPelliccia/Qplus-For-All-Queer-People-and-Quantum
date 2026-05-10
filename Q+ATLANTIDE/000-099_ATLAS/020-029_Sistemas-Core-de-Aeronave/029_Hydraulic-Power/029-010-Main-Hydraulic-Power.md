---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-029-010-MAIN-HYDRAULIC-POWER
title: "ATLAS 020-029 · 02.029 · Section 029-010 — Main Hydraulic Power"
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
subsection: "029"
subsection_title: "Hydraulic Power"
local_section_code: "029-010"
ata_sns: "29-10-00"
title_short: "Main Hydraulic Power"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.029 · 029-010 — Main Hydraulic Power

## 1. Purpose

Define the architecture boundary for *Main Hydraulic Power* (ATA 29-10-00) within ATLAS subsection `029`. This section covers engine-driven hydraulic pump systems, main hydraulic circuit generation, system pressure regulation, and the primary hydraulic power architecture serving flight control actuators and primary aircraft systems.

## 2. Scope

- Aligned to ATA SNS `29-10-00 Main Hydraulic Power`.
- Covers engine-driven hydraulic pumps (EDPs), main hydraulic system pressure limits, variable-displacement pump control, main reservoir circuits, hydraulic pressure switches and relief valves, and primary circuit suction and return lines.
- Does not cover auxiliary hydraulic power sources (see `029-020`), distribution routing (see `029-040`), or pump diagnostics beyond the main generation boundary (see `029-080`).

## 3. System Architecture

```mermaid
graph TD
    A029_010["029-010 Main Hydraulic Power\n(ATA 29-10-00)"]

    A029_010 --> EDP1["Engine 1 EDP\n(Variable-displacement)"]
    A029_010 --> EDP2["Engine 2 EDP\n(Variable-displacement)"]
    A029_010 --> Reservoir["Main Hydraulic Reservoir\n(Pressurised)"]
    A029_010 --> PressReg["Pressure Regulation\n& Relief Valves"]

    ENG1["Engine 1"] -->|mechanical drive| EDP1
    ENG2["Engine 2"] -->|mechanical drive| EDP2
    EDP1 -->|hydraulic supply| A029_010
    EDP2 -->|hydraulic supply| A029_010
    A029_010 -->|main system pressure| A029_040["029-040 Distribution"]
    A029_010 -->|status data| A029_030["029-030 Indicating"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `029` — Hydraulic Power |
| Local section code | `029-010` |
| ATA SNS | `29-10-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/029_Hydraulic-Power/` |
| Document | `029-010-Main-Hydraulic-Power.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 29-10, Main Hydraulic Power
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `029-000` General [`./029-000-General.md`](./029-000-General.md)
- `029-020` Auxiliary Hydraulic Power [`./029-020-Auxiliary-Hydraulic-Power.md`](./029-020-Auxiliary-Hydraulic-Power.md)
