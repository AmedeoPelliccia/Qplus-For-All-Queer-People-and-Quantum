---
document_id: QATL-ATLAS-1000-STA-100-109-00-108-020-CREW-DISPLAY-AND-CONTROL-ARCHITECTURE
title: "STA 100-109 · 108-020 — Crew-Display-and-Control-Architecture"
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
subsubject: "020"
subsubject_title: "Crew-Display-and-Control-Architecture"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 108-020 — Crew-Display-and-Control-Architecture

## 1. Purpose

Defines the **crew display and control architecture** for Q+ATLANTIDE spacecraft, specifying multi-function display (MFD) layout, control panel design, alert/warning system hierarchy, and display redundancy per MIL-STD-1472G[^milstd1472].

Display architecture: primary flight displays (3 independent MFDs minimum per workstation) showing: flight parameters, GNC status, ECLSS status, power status, comms status, and active alarms. Alert hierarchy: Level 1 — Master Warning (red, audio tone, immediate crew action); Level 2 — Master Caution (yellow, audio tone, crew acknowledgement); Level 3 — Advisory (white, silent, crew awareness). Display legibility: minimum 0.3 m, maximum 3.0 m; character height ≥ 16 arcminutes at nominal viewing distance. Control panel: force limits 4.5–22 N for guarded switches; minimum switch separation 19 mm for gloved operation. All critical switches guarded (safety-wire or flip-cover) to prevent inadvertent activation.

## 2. Scope

- Covers the *Crew-Display-and-Control-Architecture* subsubject (`020`) of subsection `108`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All HMI designs require human factors evaluation per MIL-STD-1472G[^milstd1472] and NASA-STD-3001 Vol.2[^nastd3001v2].

## 3. Diagram — Crew-Display-and-Control-Architecture

```mermaid
flowchart TB
    subgraph DISPLAY_ARCH["Display Architecture (per workstation)"]
        MFD1["MFD 1 — Flight/GNC"]
        MFD2["MFD 2 — ECLSS/Power"]
        MFD3["MFD 3 — Comms/Alarms"]
    end
    CWS["Caution & Warning System"]
    CWS --> L1["Level 1 Master Warning<br/>(red · audio · immediate)"]
    CWS --> L2["Level 2 Master Caution<br/>(yellow · audio)"]
    CWS --> L3["Level 3 Advisory<br/>(white · silent)"]
    style L1 fill:#e74c3c,color:#fff
    style L2 fill:#f39c12,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `108` — Interfaces de Operación Tripulación y Tierra |
| Subsubject | `020` — Crew-Display-and-Control-Architecture |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/108_Interfaces-de-Operacion-Tripulacion-y-Tierra/` |
| Document | `108-020-Crew-Display-and-Control-Architecture.md` (this file) |
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
