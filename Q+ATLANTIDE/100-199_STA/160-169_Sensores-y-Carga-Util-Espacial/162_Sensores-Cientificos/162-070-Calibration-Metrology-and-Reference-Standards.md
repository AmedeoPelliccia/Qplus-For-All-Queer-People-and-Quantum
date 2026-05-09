---
document_id: QATL-ATLAS-1000-STA-160-169-06-162-070-CALIBRATION-METROLOGY-AND-REFERENCE-STANDARDS
title: "STA 160-169 · 162-070 — Calibration Metrology and Reference Standards"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "160-169"
section: "06"
section_title: "Sensores y Carga Útil Espacial"
subsection: "162"
subsection_title: "Sensores Científicos"
subsubject: "070"
subsubject_title: "Calibration Metrology and Reference Standards"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-MKTG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 160-169 · 162-070 — Calibration Metrology and Reference Standards

## 1. Purpose

Establishes calibration hierarchy, metrology traceability, and reference standard requirements for scientific sensors within Q+ATLANTIDE STA 162[^baseline][^n001].

## 2. Scope

- **SI traceability chain** — measurement traceability from spacecraft science data to SI fundamental units; traceability chain: SI base unit → national metrology institute (NMI) primary standard → working reference standard → instrument under calibration; each link documented with calibration certificate, expanded uncertainty U (k=2), and validity period.
- **Uncertainty budget (GUM method)** — per BIPM JCGM 100:2008; Type A (random, from repeated measurements) and Type B (systematic, from calibration certificates, datasheet, models) contributions; combined standard uncertainty uc by quadrature combination; expanded uncertainty U = k·uc (k=2 for 95% confidence); separate uncertainty budget for each calibration state (pre-launch, in-orbit, degraded).
- **Pre-launch calibration reference** — ISO/IEC 17025 accredited calibration facility for primary reference instruments; spectral calibration using NIST-traceable spectral irradiance standards; radiometric calibration using black-body or integrating sphere of known temperature and emissivity.
- **In-orbit calibration strategies** — internal calibration sources (stability monitored against pre-launch baseline); celestial reference targets (solar irradiance for solar sensors, stellar standard candles for photometric sensors, CMB for microwave radiometers); vicarious calibration using Earth surface reference sites (PICS: pseudo-invariant calibration sites).
- **CEOS Cal/Val framework** — alignment with CEOS Working Group on Calibration and Validation (WGCV) protocols; inter-comparison with other spacecraft sensors in GEO/CEOS frameworks; data product quality monitoring post-launch through operational Cal/Val campaign.
- **Degradation monitoring and recalibration** — scheduled in-orbit calibration period (e.g., monthly, annually); calibration parameter trending; recalibration triggers (>2σ drift from baseline); calibration update procedure and version control.

## 3. Diagram — Calibration Chain: SI to Science Data

```mermaid
flowchart TD
    A["SI Reference\nbase units: m · kg · s · K · cd · A · mol"]:::start
    B["NMI Primary Standard\nNIST · PTB · NPL · BIPM\nISO/IEC 17025 accredited"]
    C["Calibration Facility\naccredited lab · black-body · int. sphere\nspectral irradiance standards"]
    D["Ground Calibration\npre-launch TVAC\nType A + Type B uncertainty budget"]
    E["In-Orbit Internal Calibration\nlamp · diffuser · injection path\nstability vs. pre-launch baseline"]
    F["Celestial Reference Targets\nsolar irradiance · stellar candles\nCMB · PICS vicarious sites"]
    G["Calibrated Data Product\nL1b · U = k·uc (k=2) per pixel\nCEOS WGCV inter-comparison"]:::end_node

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    E --> G
    F --> G

    classDef start fill:#1f3a93,color:#fff
    classDef end_node fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `160-169` |
| Section | `06` — Sensores y Carga Útil Espacial |
| Subsection | `162` — Sensores Científicos |
| Subsubject | `007` — Calibration, Metrology and Reference Standards |
| Primary Q-Division | Q-SPACE[^qdiv] |
| ORB support | ORB-PMO, ORB-MKTG |
| Governance class | `baseline`[^gov] |
| Document | `162-070-Calibration-Metrology-and-Reference-Standards.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`162-000-General.md`](./162-000-General.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

[^n001]: **Note N-001** — Q+ATLANTIDE is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

### Applicable industry standards

- BIPM JCGM 100:2008 — Guide to the Expression of Uncertainty in Measurement (GUM)
- ISO/IEC 17025 — General requirements for the competence of testing and calibration laboratories
- CEOS WGCV — Working Group on Calibration and Validation protocols
- ECSS-E-ST-10-03C — Testing
