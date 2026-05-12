---
document_id: QATL-ATLAS-1000-STA-100-109-00-108-060-VOICE-VIDEO-AND-DATA-COMMUNICATIONS
title: "STA 100-109 · 108-060 — Voice-Video-and-Data-Communications"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "100-109"
section: "00"
section_title: "Sistemas Generales y Soporte Vital Espacial"
subsection: "108"
subsection_title: "Interfaces de Operación Tripulación y Tierra"
subsubject: "060"
subsubject_title: "Voice-Video-and-Data-Communications"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 108-060 — Voice-Video-and-Data-Communications

## 1. Purpose

Defines the **voice, video, and data communications** architecture for Q+ATLANTIDE missions, specifying crew-to-ground voice links, video conferencing, science data transfer, and private communications per CCSDS standards[^ccsds].

Voice communications: full-duplex audio links between crew and MCC (primary via S-band, secondary via UHF/VHF); intra-vehicle intercom (IVC) for crew-to-crew communication; audio quality: intelligibility score ≥ 90 % per MIL-STD-1472G[^milstd1472] under worst-case background noise. Video communications: high-definition (≥ 720p) video conferencing at ≥ 10 fps; crew-family private video link via encrypted channel, separate from mission data; mission payload/science video at up to 4K for science value. Data communications: science data downlink; software/procedure uplink; telemetry continuity. Private crew communications: encrypted end-to-end, not routed through mission operations monitoring, compliant with crew privacy policy (subsubject 106-080).

## 2. Scope

- Covers the *Voice-Video-and-Data-Communications* subsubject (`060`) of subsection `108`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All HMI designs require human factors evaluation per MIL-STD-1472G[^milstd1472] and NASA-STD-3001 Vol.2[^nastd3001v2].

## 3. Diagram — Voice-Video-and-Data-Communications

```mermaid
flowchart LR
    VOICE["Voice Communications<br/>(S-band primary · UHF/VHF secondary)"]
    VIDEO["Video Communications<br/>(≥ 720p · 10 fps)"]
    DATA["Data Transfer<br/>(science · software · TM)"]
    PRIVATE["Private Crew Comms<br/>(encrypted · E2E · family)"]

    VOICE & VIDEO & DATA & PRIVATE --> COMMS_BUS["Integrated Comms Bus<br/>(CCSDS compliant)"]
    COMMS_BUS --> MCC_LINK["MCC Link<br/>(primary + backup paths)"]
    style PRIVATE fill:#2c82c9,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `108` — Interfaces de Operación Tripulación y Tierra |
| Subsubject | `060` — Voice-Video-and-Data-Communications |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/108_Interfaces-de-Operacion-Tripulacion-y-Tierra/` |
| Document | `108-060-Voice-Video-and-Data-Communications.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`108-000-General.md`](./108-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management.

[^ecsse1011]: **ECSS-E-ST-10-11C — Spacecraft Environment Interaction** — Applied here for operations interface monitoring standards.

[^nastd3001v2]: **NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health** — Display, control, and HMI design requirements for crewed spacecraft operations.

[^milstd1472]: **MIL-STD-1472G — Human Engineering** — Anthropometric, display, control-force, and cognitive load requirements.

[^ccsds]: **CCSDS 401.0-B — Radio Frequency and Modulation Systems; CCSDS 131.0-B — TM Synchronization and Channel Coding** — Uplink/downlink communications standards.

### Applicable industry standards

- ECSS-E-ST-10-11C — Spacecraft Environment Interaction[^ecsse1011]
- NASA-STD-3001 Vol.2 — Human Factors, Habitability, and Environmental Health[^nastd3001v2]
- MIL-STD-1472G — Human Engineering[^milstd1472]
- CCSDS — Radio Frequency and Modulation Systems[^ccsds]
