---
document_id: QATL-ATLAS-1000-STA-140-149-04-141-007-RADIATION-HARDENING-AND-SINGLE-EVENT-EFFECTS
title: "STA 140-149 · 04.141.007 — Radiation Hardening and Single Event Effects"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "140-149"
section: "04"
section_title: "Aviónica y Control de Misión Espacial"
subsection: "141"
subsection_title: "Aviónica Espacial"
subsubject: "007"
subsubject_title: "Radiation Hardening and Single Event Effects"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 140-149 · Section 04 · Subsection 141 · Subsubject 007 — Radiation Hardening and Single Event Effects

## 1. Purpose

Defines the **radiation hardening approach, Total Ionising Dose (TID) budget, and Single Event Effect (SEE) mitigation strategy** for avionics components on Q+ATLANTIDE STA-band spacecraft.

## 2. Scope

- **Total Ionising Dose (TID) budget** — TID environment calculation per mission orbit and duration (proton and electron contribution, including solar proton events); shielding analysis (aluminium equivalent); component TID qualification level requirements; TID margin policy (safety factor ≥ 2 on component qualification level vs. mission dose).
- **SEE types and mitigation** — Single Event Upset (SEU): bit flip in memory or registers, mitigated by EDAC and memory scrubbing; Single Event Functional Interrupt (SEFI): device enters anomalous state, mitigated by watchdog and power cycling; Single Event Transient (SET): glitch propagation in combinatorial logic, mitigated by filtering and triple-redundant voting; Single Event Latch-up (SEL): destructive current surge, mitigated by current limiters and SEL-immune process selection.
- **Radiation-hardened vs COTS-with-mitigation** — radiation-hardened (RH) or radiation-tolerant (RT) components for critical data paths (processor, FPGA logic); COTS-with-mitigation approach for non-critical functions with adequate SEE analysis and system-level mitigation; trade-off criteria: TID level, SEE rate, availability, power, and cost.
- **Radiation analysis evidence** — component radiation test data (proton, heavy ion) per ECSS-Q-ST-60-15C[^ecssqst6015c] or equivalent; SEE rate calculation (CREME96 or similar tool); FMEA for radiation-induced failures; radiation test plan for custom ASICs.
- **Shielding strategy** — spot shielding for radiation-sensitive components; box-level shielding optimization; mass budget impact; verification by Monte Carlo transport simulation.

## 3. Diagram — Radiation Effect Mitigation Strategy

```mermaid
flowchart TD
    A["Radiation Environment<br/>(TID · proton · heavy ion)"]
    A --> B["TID Analysis<br/>(shielding + margin × 2)"]
    A --> C["SEE Rate Analysis<br/>(CREME96 / Petrov)"]
    B --> D["Component Selection<br/>(RH / RT / COTS+mitigation)"]
    C --> E["SEE Mitigation<br/>(EDAC · watchdog · current limiter)"]
    D --> F["Avionics Design<br/>(qualified components)"]
    E --> F
    F --> G["Radiation Test Evidence<br/>(ECSS-Q-ST-60-15C)"]
    style A fill:#8b0000,color:#fff
    style F fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `140-149` |
| Section | `04` — Aviónica y Control de Misión Espacial |
| Subsection | `141` — Aviónica Espacial |
| Subsubject | `007` — Radiation Hardening and Single Event Effects |
| Primary Q-Division | Q-SPACE[^qdiv] |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Document | `007_Radiation-Hardening-and-Single-Event-Effects.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |

## 5. References & Citations

[^ecssqst6015c]: **ECSS-Q-ST-60-15C — Radiation Hardness Assurance** — Component radiation testing and qualification standard.

[^jedecjesd57]: **JEDEC JESD57 — Test Procedures for the Measurement of Single-Event Effects** — Standard test procedures for SEE characterisation.

[^milstd883]: **MIL-STD-883 — Test Method Standard for Microcircuits** — Qualification test methods including radiation tests.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-Q-ST-60-15C — Radiation Hardness Assurance[^ecssqst6015c]
- JEDEC JESD57 — Test Procedures for the Measurement of Single-Event Effects[^jedecjesd57]
- MIL-STD-883 — Test Method Standard for Microcircuits[^milstd883]
