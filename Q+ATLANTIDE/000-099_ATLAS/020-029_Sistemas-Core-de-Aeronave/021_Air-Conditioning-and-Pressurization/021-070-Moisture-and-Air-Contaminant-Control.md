---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-021-070-MOISTURE-AND-AIR-CONTAMINANT-CONTROL
title: "ATLAS 020-029 · 02.021 — Air Conditioning and Pressurization · 021-070 Moisture and Air Contaminant Control"
ata_chapter: "21"
ata_sns: "21-70-00"
local_section_code: "021-070"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "020-029"
section: "02"
section_title: "Sistemas Core de Aeronave"
subsection: "021"
subsection_title: "Air Conditioning and Pressurization"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# ATLAS 020-029 · 02.021 — Air Conditioning and Pressurization · 021-070 Moisture and Air Contaminant Control

## 1. Purpose

Defines the **moisture removal and air contaminant control architecture** for the *Air Conditioning and Pressurization* subsystem (ATA 21-70-00) within the Q+ATLANTIDE programme. Covers water separator design, humidity control, HEPA filtration, ozone converter interfaces, and cabin air quality monitoring to ensure cabin air meets airworthiness and occupational health standards.

## 2. Scope

- Covers the *Moisture and Air Contaminant Control* section (`021-070`, ATA SNS 21-70-00) of subsection `021` *Air Conditioning and Pressurization*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Water separator** — high-efficiency water separator downstream of the ACM turbine (cross-reference 021-050 Cooling); moisture extraction capacity, design limits, and drain/outlet interfaces.
  - **Humidity control** — cabin relative humidity range management; humidifier system (where fitted); fogging/condensation prevention protocols.
  - **HEPA filtration** — high-efficiency particulate air (HEPA) filter in recirculation loop; filter efficiency class (minimum HEPA H13 per EN 1822[^en1822]); replacement intervals and in-service monitoring.
  - **Ozone converter** — catalytic ozone converter on bleed-air supply path; ozone concentration limit compliance per FAR/CS 25.832[^cs25]; converter performance monitoring.
  - **Gaseous contaminant control** — activated-carbon filters for gaseous contaminants; scope of detectable species (ozone, VOCs); replacement criteria.
  - **Cabin air quality monitoring** — CO₂ and contaminant sensor integration with ECS monitoring (021-080); crew alerting on air quality degradation.
- Out of scope: primary compression and cooling (021-010, 021-050), distribution routing (021-020), pressurisation (021-030), temperature control (021-060).

## 3. Diagram — Moisture and Contaminant Control Flow

Water separation, ozone conversion, recirculation HEPA filtration, and gaseous contaminant control combine to deliver conditioned, clean cabin air.

```mermaid
flowchart TD
    ACM_OUT["ACM Turbine Output<br/>(humid / cooled air<br/>021-050 Cooling)"]:::source
    ACM_OUT --> SEP["Water Separator<br/>(high-efficiency<br/>moisture extraction · drain)"]:::filter
    SEP --> OZ["Ozone Converter<br/>(catalytic — CS 25.832<br/>performance monitoring)"]:::filter
    OZ --> FRESH["Fresh Supply Air<br/>(conditioned · low moisture)"]:::out
    FRESH --> DIST["Distribution<br/>(021-020)"]:::out
    RECIRC["Cabin Return Air<br/>(recirculation loop)"]:::source
    RECIRC --> HEPA["HEPA Filter<br/>(H13 — recirculation<br/>replacement monitoring)"]:::filter
    HEPA --> GAC["Gaseous Contaminant<br/>Filter (activated carbon<br/>VOC / odour control)"]:::filter
    GAC --> DIST
    AQM["Cabin Air Quality Monitors<br/>(CO₂ · contaminants<br/>021-080 interface)"]:::monitor
    DIST --> AQM

    classDef source fill:#1f3a93,stroke:#0b1d4a,color:#fff
    classDef filter fill:#eaf3fb,stroke:#2c82c9,color:#0b1d4a
    classDef out fill:#f0f9e8,stroke:#27ae60,color:#145a32
    classDef monitor fill:#f6e6ff,stroke:#7d3c98,color:#3b1f4d
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `021` — Air Conditioning and Pressurization |
| Local section code | `021-070` — Moisture and Air Contaminant Control |
| ATA chapter | 21 |
| ATA SNS | 21-70-00 |
| Primary Q-Division | Q-AIR[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/021_Air-Conditioning-and-Pressurization/` |
| Document | `021-070-Moisture-and-Air-Contaminant-Control.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`021-000-General.md`](./021-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **ATLAS §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^cs25]: **EASA CS-25** — CS 25.831 (Ventilation — cabin air quality), CS 25.832 (Ozone concentration limits), and CS 25.854 (Smoke penetration tests).

[^en1822]: **EN 1822 — High-Efficiency Air Filters (EPA, HEPA and ULPA)** — European standard defining HEPA filter efficiency classes and test methods; H13 is the minimum class specified for cabin recirculation applications.

[^ata2200]: **ATA iSpec 2200** — Section 21-70 naming and data-module scope for moisture and air contaminant control subsystems.

### Applicable standards

- EASA CS-25[^cs25]
- EN 1822 — High-Efficiency Air Filters[^en1822]
- ATA iSpec 2200[^ata2200]
