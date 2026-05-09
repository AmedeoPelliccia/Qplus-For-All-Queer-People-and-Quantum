---
document_id: QATL-ATLAS-1000-STA-130-139-03-133-030-POWER-CONDITIONING-REGULATION-AND-CONVERSION
title: "STA 130-139 · 133-030 — Power Conditioning Regulation and Conversion"
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
subsection: "133"
subsubject: "030"
subsubject_title: "Power Conditioning Regulation and Conversion"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-DATAGOV, Q-HPC, Q-HORIZON, Q-INDUSTRY, Q-STRUCTURES]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 130-139 · 133-030 — Power Conditioning Regulation and Conversion

## 1. Purpose

Defines **power conditioning, point-of-load regulation, and DC/DC conversion** requirements for Q+ATLANTIDE STA-band platforms.

## 2. Scope

- **Primary DC/DC converters** — bus-to-load converters; input voltage range tracking battery SOC; output: 3.3 V / 5 V / 12 V / 15 V / 28 V regulated for subsystem loads.
- **Linear regulators** — low-noise, low-efficiency (η ≈ 60–90%); used for analogue/RF loads sensitive to switching noise.
- **Switching converters** — buck, boost, buck-boost; η ≥ 85%; switching frequency ≥ 100 kHz; filtered to MIL-STD-461G CE102/CS101.
- **Ripple and noise limits** — output ripple ≤ 1% of nominal; conducted noise per ECSS-E-ST-20C Table A-3.
- **Soft-start** — inrush current limit ≤ 3× steady-state; implemented via soft-start pin or external NTC thermistor.

## 3. Diagram — Power Conditioning, Regulation and Conversion

```mermaid
flowchart TD
    A["Power Source Input\n(→ 130 / 131 / 132)"] --> B["Power Conditioning, Regulation and Conversion\n(STA-133-003)"]
    B --> C["Load Interfaces\n(→ 121 / 100 / Payload)"]
    B --> D["Fault Isolation\n(→ 005)"]
    style A fill:#1f3a93,color:#fff
    style C fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Subsection | `133` — Distribución Eléctrica |
| Subsubject | `003` — Power Conditioning, Regulation and Conversion |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |

## 5. References & Citations

[^ecssest20]: **ECSS-E-ST-20C — Electrical and Electronic**.
[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards
- ECSS-E-ST-20C — Electrical and Electronic
