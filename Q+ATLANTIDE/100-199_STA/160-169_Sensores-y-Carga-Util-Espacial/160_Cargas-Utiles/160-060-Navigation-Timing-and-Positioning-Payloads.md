---
document_id: QATL-ATLAS-1000-STA-160-169-06-160-060-NAVIGATION-TIMING-AND-POSITIONING-PAYLOADS
title: "STA 160-169 · 160-060 — Navigation Timing and Positioning Payloads"
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
subsection: "160"
subsection_title: "Cargas Útiles"
subsubject: "060"
subsubject_title: "Navigation Timing and Positioning Payloads"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-MKTG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 160-169 · 160-060 — Navigation Timing and Positioning Payloads

## 1. Purpose

Establishes design and performance requirements for navigation, timing, and positioning payloads on Q+ATLANTIDE STA-band spacecraft, covering GNSS signal generation, atomic frequency standards, timing accuracy budgets, signal integrity, and inter-satellite link timing.

## 2. Scope

- **GNSS signal generation payloads** — L-band signal-in-space (SIS) requirements covering frequency channels (L1/L2/L5 for GPS, E1/E5/E6 for Galileo equivalents), signal modulation (BPSK, CBOC, AltBOC), minimum received power floor, and pseudo-random noise (PRN) code assignment; signal generation chain shall comply with applicable GPS/Galileo SIS ICDs.
- **Atomic frequency standards** — Rubidium atomic frequency standard (RAFS), Caesium beam frequency standard, and Hydrogen maser options evaluated against stability requirements (Allan deviation at τ = 1 s, 100 s, 1 day); clock ensemble management and monitoring shall be declared in the payload timing architecture document.
- **Timing accuracy budget allocation** — end-to-end User Range Error (URE) and Signal-In-Space Range Error (SISRE) budgets shall be allocated across clock stability, orbit determination errors, signal generation errors, and inter-satellite link timing uncertainties; total SISRE shall meet service performance commitments.
- **Signal integrity and authenticity** — Navigation Message Authentication (NMA) and signal authentication provisions shall be declared where required by service design; anti-spoofing, anti-jamming margin, and interference environment analysis shall be produced as evidence artefacts.
- **Inter-satellite link timing** — cross-link ranging and time-transfer accuracy for constellations with inter-satellite links (ISL) shall be declared; ISL data latency and synchronisation protocol shall be consistent with CCSDS 131.0-B timing recommendations.
- **User receiver performance models** — user position, velocity, and time (PVT) accuracy models linking SISRE to dilution of precision (DOP) geometry shall be included; minimum constellation availability (PDOP ≤ 6, ≥ 4 visible satellites) shall be verified via simulation.

## 3. Diagram — Navigation Payload Timing Chain

```mermaid
flowchart TD
    A["Atomic Frequency Standard\n(RAFS / Cs / H-Maser)"]:::first
    A --> B["Clock Ensemble Management\n(Allan Deviation Monitoring)"]
    B --> C["Navigation Message Generation\n(Ephemeris · Clock Corrections · NMA)"]
    C --> D["Signal Generation\n(PRN Code · Modulation · Frequency)"]
    D --> E["Power Amplifier\n(L-Band EIRP Budget)"]
    E --> F["Transmit Antenna\n→ User Segment PVT"]:::last

    classDef first fill:#1f3a93,color:#fff
    classDef last fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `160-169` |
| Section | `06` — Sensores y Carga Útil Espacial |
| Subsection | `160` — Cargas Útiles |
| Subsubject | `006` — Navigation, Timing and Positioning Payloads |
| Primary Q-Division | Q-SPACE[^qdiv] |
| ORB support | ORB-PMO, ORB-MKTG |
| Governance class | `baseline`[^gov] |
| Document | `160-060-Navigation-Timing-and-Positioning-Payloads.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`160-000-General.md`](./160-000-General.md) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

| Standard | Title | Applicability |
|---|---|---|
| ECSS-E-ST-50C | Space engineering — Communications | Signal generation and communication link requirements |
| CCSDS 131.0-B | TM Synchronization and Channel Coding | Timing synchronisation and inter-satellite link protocols |
| GPS SIS ICD (IS-GPS-200) | GPS Interface Specification — Signal-in-Space | GPS L1/L2/L5 signal requirements |
| Galileo OS SIS ICD | Galileo Open Service Signal-in-Space ICD | Galileo E1/E5/E6 signal requirements |
| ITU-R M.1787 | Description of systems and networks in the radionavigation-satellite service | Frequency coordination for navigation payloads |
