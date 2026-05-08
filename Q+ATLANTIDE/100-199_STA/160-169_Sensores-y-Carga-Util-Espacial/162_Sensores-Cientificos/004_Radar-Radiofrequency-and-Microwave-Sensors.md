---
document_id: QATL-ATLAS-1000-STA-160-169-06-162-004-RADAR-RADIOFREQUENCY-AND-MICROWAVE-SENSORS
title: "STA 160-169 · 06.162.004 — Radar, Radiofrequency and Microwave Sensors"
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
subsubject: "004"
subsubject_title: "Radar, Radiofrequency and Microwave Sensors"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-MKTG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 160-169 · Section 06 · Subsection 162 · Subsubject 004 — Radar, Radiofrequency and Microwave Sensors

## 1. Purpose

Establishes design and performance requirements for radar, radiofrequency, and microwave scientific sensors on Q+ATLANTIDE STA-band spacecraft[^baseline][^n001].

## 2. Scope

- **Sensor types** — synthetic aperture radar (SAR, L/C/X/Ka-band); radar altimeters (nadir-pointing, pulse-limited or delay-Doppler); scatterometers (ocean wind retrieval, pencil-beam or fan-beam); passive microwave radiometers (brightness temperature, 1–300 GHz); radio occultation receivers (GPS/GNSS-RO for atmospheric profiling).
- **Radar equation and link budget** — peak transmit power, antenna gain, pulse repetition frequency, bandwidth, range/azimuth resolution; noise equivalent sigma-zero (NESZ) as key figure of merit; ambiguity ratio (range/azimuth ambiguity suppression ≥25 dB).
- **Antenna design** — phased array vs. parabolic reflector vs. slotted waveguide array; polarization control (HH, VV, HV, VH) for polarimetric SAR; beam-forming network design; antenna pattern characterization and calibration.
- **Frequency coordination** — ITU-R frequency allocation for scientific Earth observation services; interference analysis with active communication payloads (→`160`); radio frequency interference (RFI) detection and mitigation for passive microwave sensors.
- **Calibration** — external calibrators (transponders, corner reflectors, distributed targets); internal calibration loop (injection path); ocean/ice reference targets for radiometers; calibration uncertainty ≤0.5 K (brightness temperature) for climate-quality passive microwave.
- **Passive microwave radiometer specifics** — total-power vs. Dicke-switched designs; noise figure and NEDT (Noise Equivalent Temperature Difference); antenna side-lobe contamination from Earth vs. cold space; spectral line vs. window channel selection.

## 3. Diagram — Radar/Microwave Sensor Architecture

```mermaid
flowchart TD
    A["Science Frequency & Resolution\nRequirement"]:::start
    B["Transmit Chain\n(active sensors only)\npower amp · waveform gen · PRF"]
    C["Antenna\nphased array · reflector\npolarization · beam forming"]
    D["Target Interaction\n(SAR/altimeter/scatterometer)\nor Thermal Emission\n(passive radiometer)"]
    E["Receive Chain\nLNA · mixer · ADC\nNESZ / NEDT budget"]
    F["SAR Processing /\nRadiometric Retrieval\nambiguity suppression · RFI mitigation"]
    G["Calibration\nexternal transponder/corner reflector\ninternal cal loop · ocean/ice targets"]
    H["Calibrated Data Product\nσ⁰ / brightness temperature / range"]:::end_node

    A --> B
    A --> C
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H

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
| Subsubject | `004` — Radar, Radiofrequency and Microwave Sensors |
| Primary Q-Division | Q-SPACE[^qdiv] |
| ORB support | ORB-PMO, ORB-MKTG |
| Governance class | `baseline`[^gov] |
| Document | `004_Radar-Radiofrequency-and-Microwave-Sensors.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

[^n001]: **Note N-001** — Q+ATLANTIDE is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

### Applicable industry standards

- ECSS-E-ST-50C — Telecommunications
- ITU-R M.1787 — Description of systems and networks in the space research service operating between 25.5–27 GHz
- CEOS Cal/Val — Committee on Earth Observation Satellites Calibration and Validation protocols
- ECSS-E-ST-10-03C — Testing
