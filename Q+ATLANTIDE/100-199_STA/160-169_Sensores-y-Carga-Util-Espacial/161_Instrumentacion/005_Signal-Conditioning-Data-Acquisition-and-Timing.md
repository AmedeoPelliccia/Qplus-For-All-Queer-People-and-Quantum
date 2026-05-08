---
document_id: QATL-ATLAS-1000-STA-160-169-06-161-005-SIGNAL-CONDITIONING-DATA-ACQUISITION-AND-TIMING
title: "STA 160-169 · 06.161.005 — Signal Conditioning, Data Acquisition and Timing"
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
subsection: "161"
subsection_title: "Instrumentación"
subsubject: "005"
subsubject_title: "Signal Conditioning, Data Acquisition and Timing"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-MKTG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 160-169 · Section 06 · Subsection 161 · Subsubject 005 — Signal Conditioning, Data Acquisition and Timing

## 1. Purpose

Establishes requirements for signal conditioning, data acquisition, and timing within Q+ATLANTIDE STA-band spacecraft instrumentation systems. Covers the electronic path from detector output to time-tagged, packetized telemetry including EMC and on-board data processing.

## 2. Scope

- **Signal conditioning** — amplification stages (gain, bandwidth, impedance matching), filtering (low-pass, band-pass, notch filters for EMI rejection), isolation (opto-couplers, differential signaling), signal multiplexing; noise figure budget allocation.
- **Data acquisition architecture** — instrument data processing unit (IDPU) or payload data handling unit (PDHU); acquisition modes (continuous, burst, event-triggered, programmatic); data volume estimation and on-board storage allocation.
- **Timing and synchronization** — time-tagging of science measurements; synchronization with spacecraft on-board time (OBT) per CCSDS time code formats; time transfer accuracy requirements (instrument-level to millisecond or better; for atomic standards to nanosecond level); latency budget from physical event to packetized telemetry.
- **Digital interface to platform** — data formatting in CCSDS space packets; SpaceWire or MIL-STD-1553 transport; data rate allocation, prioritization, and flow control; housekeeping versus science data channel separation.
- **On-board data processing** — lossless compression (Rice/CCSDS 121.0-B), lossy compression (CCSDS 122.0-B for imagery), on-board data reduction (averaging, thresholding, event selection); processing budget (MIPS, memory) per instrument.
- **EMC and cross-coupling** — conducted and radiated emission limits per ECSS-E-ST-20C; susceptibility requirements; instrument power supply filtering; grounding and bonding design.

## 3. Diagram — Data Acquisition and Timing Flow

```mermaid
flowchart TD
    A["Instrument Detector\n(analog output)"]:::entry
    A --> B["Signal Conditioning\n(gain · filter · isolation · MUX)\nnoise figure budget"]
    B --> C["IDPU / PDHU\n(instrument data processing unit)"]
    C --> D["Timing & Synchronization\n(OBT time-tag · CCSDS time code\nlatency budget)"]
    D --> E["On-Board Data Processing\nCCSDS 121.0-B lossless\nCCSDS 122.0-B lossy\naveraging / thresholding"]
    E --> F["Data Bus Interface\n(SpaceWire ≤400 Mbit/s /\nMIL-STD-1553B 1 Mbit/s /\nRS-422)"]
    F --> G["CCSDS Space Packet\nTelemetry Stream\n(science + housekeeping separated)"]:::exit
    H["EMC Compliance\nECSS-E-ST-20C\nconducted/radiated limits"] -.->|governs| B

    classDef entry fill:#1f3a93,color:#fff
    classDef exit fill:#0f7a0f,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `160-169` |
| Section | `06` — Sensores y Carga Útil Espacial |
| Subsection | `161` — Instrumentación |
| Subsubject | `005` — Signal Conditioning, Data Acquisition and Timing |
| Primary Q-Division | Q-SPACE[^qdiv] |
| ORB support | ORB-PMO, ORB-MKTG |
| Governance class | `baseline`[^gov] |
| Document | `005_Signal-Conditioning-Data-Acquisition-and-Timing.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`000_Overview.md`](./000_Overview.md) |

## 5. References & Citations

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).
[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

| Standard | Title | Applicability |
|---|---|---|
| ECSS-E-ST-20C | Space Engineering: Electrical and Electronic | EMC, grounding, bonding, and signal conditioning requirements |
| ECSS-E-ST-50C | Space Engineering: Communications | Data interface and protocol requirements |
| CCSDS 121.0-B | Lossless Data Compression | Lossless on-board compression standard |
| CCSDS 122.0-B | Image Data Compression | Lossy on-board image compression standard |
