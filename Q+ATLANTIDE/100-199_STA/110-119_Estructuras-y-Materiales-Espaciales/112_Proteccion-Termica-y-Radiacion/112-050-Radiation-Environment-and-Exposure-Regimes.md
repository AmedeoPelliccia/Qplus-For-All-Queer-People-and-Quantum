---
document_id: QATL-ATLAS-1000-STA-110-119-01-112-050-RADIATION-ENVIRONMENT-AND-EXPOSURE-REGIMES
title: "STA 110-119 · 112-050 — Radiation Environment and Exposure Regimes"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "110-119"
section: "01"
section_title: "Estructuras y Materiales Espaciales"
subsection: "112"
subsection_title: "Protección Térmica y Radiación"
subsubject: "050"
subsubject_title: "Radiation Environment and Exposure Regimes"
primary_q_division: Q-SPACE
support_q_divisions: [Q-STRUCTURES, Q-GREENTECH, Q-DATAGOV, Q-HORIZON, Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-FIN]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 110-119 · 112-050 — Radiation Environment and Exposure Regimes

## 1. Purpose

Characterises the **natural space radiation environment** for each Q+ATLANTIDE mission class, defining total ionising dose (TID), proton/electron belt fluence, GCR/SPE spectra, and single-event effect (SEE) exposure regimes used as inputs to shielding and electronics hardening design.

## 2. Scope

- Covers radiation environment characterisation within subsection `112`.
- Concepts in scope: Van Allen belt electron and proton fluence (AP-8/AE-8, AP-9/AE-9 models); GCR iron/proton spectra; solar particle event (SPE) probabilities; TID per mission lifetime; SEE LET threshold and cross-section data; ECSS-E-ST-10-04C[^ecssest1004] environment specification; orbit-dependent dose-depth curves.

## 3. Diagram — Radiation Environment Characterisation

```mermaid
flowchart TD
    MODEL["ECSS-E-ST-10-04C<br/>Environment Models<br/>(AP-9/AE-9 · CREME96 · SPENVIS)"]
    MODEL --> LEO["LEO Environment<br/>(SAA · low inclination)"]
    MODEL --> GEO["GEO Environment<br/>(outer belt · GCR dominant)"]
    MODEL --> DEEP["Deep Space / Lunar<br/>(GCR · SPE)"]
    LEO --> TID["TID (krad Si)<br/>fluence (p/cm² · e/cm²)"]
    GEO --> TID
    DEEP --> TID
    TID --> SEE["SEE LET threshold<br/>(MeV·cm²/mg)"]
    TID --> SHIELD["Shielding depth<br/>(mm Al-eq)"]
    style TID fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Subsection | `112` — Protección Térmica y Radiación |
| Subsubject | `005` — Radiation Environment and Exposure Regimes |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Governance class | `baseline`[^gov] |
| Document | `112-050-Radiation-Environment-and-Exposure-Regimes.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |

## 5. References & Citations

[^ecssest1004]: **ECSS-E-ST-10-04C — Space Environment** — European standard for natural space environment characterisation.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-10-04C — Space Environment[^ecssest1004]
- NASA-HDBK-4002A — Mitigating In-Space Charging Effects
