---
document_id: QATL-ATLAS-1000-STA-120-129-02-120-009-PERFORMANCE-METRICS-ISP-THRUST-AND-MASS-FRACTION
title: "STA 120-129 · 02.120.009 — Performance Metrics: Isp, Thrust and Mass Fraction"
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
subsubject: "009"
subsubject_title: "Performance Metrics: Isp, Thrust and Mass Fraction"
primary_q_division: Q-SPACE
support_q_divisions: [Q-GREENTECH, Q-STRUCTURES, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 120-129 · Section 02 · Subsection 120 · Subsubject 009 — Performance Metrics: Isp, Thrust and Mass Fraction

## 1. Purpose

Defines the **key chemical propulsion performance metrics** — specific impulse (Isp), thrust, thrust-to-weight ratio (T/W), propellant mass fraction (PMF), and ΔV capability — and the methodology for calculating delivered performance margins.

## 2. Scope

- Specific impulse: Isp = F / (ṁ · g₀) [s]; vacuum vs. sea-level Isp; delivered Isp efficiency η (typically 92–98%); typical ranges: N₂H₄ monoprop ≈ 220–230 s; NTO/MMH biprop ≈ 310–320 s; LOX/LH₂ ≈ 450–460 s; LOX/RP-1 ≈ 310–360 s.
- Thrust: F = ṁ · Isp · g₀; thrust range (mN RCS thrusters → MN launch vehicles); thrust-to-weight T/W = F / (m₀ · g₀).
- Propellant mass fraction: PMF = m_prop / m₀; Tsiolkovsky rocket equation: ΔV = Isp · g₀ · ln(m₀/m_f).
- Mission ΔV budget: deterministic + statistical margin; residual propellant reserve; end-of-life ΔV.

## 3. Diagram — ΔV Budget and Isp Trade

```mermaid
flowchart LR
    ISP["Propellant Isp<br/>(220 – 460 s)"]
    PMF["Propellant Mass Fraction<br/>(PMF = m_prop / m₀)"]
    ISP --> DV["ΔV = Isp · g₀ · ln(1/(1-PMF))"]
    PMF --> DV
    DV --> MARGIN["ΔV Margin<br/>(≥ 5% reserve)"]
    MARGIN --> BUDGET["Mission ΔV Budget<br/>(orbit · attitude · disposal)"]
    style DV fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `120` — Propulsión Química |
| Subsubject | `009` — Performance Metrics: Isp, Thrust and Mass Fraction |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `009_Performance-Metrics-Isp-Thrust-and-Mass-Fraction.md` (this file) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-35C — Propulsion General Requirements
