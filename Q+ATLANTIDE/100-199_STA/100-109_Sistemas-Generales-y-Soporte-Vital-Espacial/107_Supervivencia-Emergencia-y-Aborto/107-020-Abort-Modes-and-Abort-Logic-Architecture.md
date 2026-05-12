---
document_id: QATL-ATLAS-1000-STA-100-109-00-107-020-ABORT-MODES-AND-ABORT-LOGIC-ARCHITECTURE
title: "STA 100-109 · 107-020 — Abort-Modes-and-Abort-Logic-Architecture"
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
subsection: "107"
subsection_title: "Supervivencia, Emergencia y Aborto"
subsubject: "020"
subsubject_title: "Abort-Modes-and-Abort-Logic-Architecture"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 100-109 · 107-020 — Abort-Modes-and-Abort-Logic-Architecture

## 1. Purpose

Defines the **abort modes and abort logic architecture** for Q+ATLANTIDE missions from pad operations through on-orbit phases, specifying trigger conditions, response timelines, and software assurance requirements per NASA-STD-8739.8A[^nastd8739].

Abort modes by phase: (1) **Pad abort** (T-3600s to T+30s): LAS motor fires, separating crew module from launch vehicle in < 0.5 s after abort trigger, impulse: ≥ 60 kN·s minimum; (2) **Low-altitude abort** (T+30s to Max-Q): intact abort to launch-site vicinity, requires aerodynamic stability; (3) **High-altitude abort** (Max-Q to staging): MECO + separation + RCS orientation for capsule re-entry corridor; (4) **On-orbit abort** (orbit insertion to mission): propulsive de-orbit burn, emergency re-entry. Abort trigger logic: dual-string comparison of ≥ 3 independent sensor channels; any 2-of-3 majority vote triggers Class I abort autonomously. Software assurance: NASA-STD-8739.8A Software Safety [^nastd8739] applied to abort logic FSM.

## 2. Scope

- Covers the *Abort-Modes-and-Abort-Logic-Architecture* subsubject (`020`) of subsection `107`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All emergency/abort systems are life-safety critical per MIL-STD-882E[^milstd882] Hazard Risk Index I.

## 3. Diagram — Abort-Modes-and-Abort-Logic-Architecture

```mermaid
flowchart TB
    PAD["Pad Abort<br/>(T-3600 → T+30s)<br/>LAS motor · < 0.5s"]
    LOW_ALT["Low-Altitude Abort<br/>(T+30s → Max-Q)<br/>intact abort"]
    HIGH_ALT["High-Altitude Abort<br/>(Max-Q → staging)<br/>MECO + re-entry"]
    ORBIT["On-Orbit Abort<br/>(orbit → mission)<br/>de-orbit burn"]

    PAD --> LOW_ALT --> HIGH_ALT --> ORBIT

    LOGIC["Abort Logic FSM<br/>(2-of-3 sensor vote)"]
    LOGIC --> PAD & LOW_ALT & HIGH_ALT & ORBIT
    style LOGIC fill:#e74c3c,color:#fff
    style PAD fill:#e74c3c,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `100-109` |
| Section | `00` — Sistemas Generales y Soporte Vital Espacial |
| Subsection | `107` — Supervivencia, Emergencia y Aborto |
| Subsubject | `020` — Abort-Modes-and-Abort-Logic-Architecture |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HORIZON, Q-HPC, Q-AIR |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/100-109_Sistemas-Generales-y-Soporte-Vital-Espacial/107_Supervivencia-Emergencia-y-Aborto/` |
| Document | `107-020-Abort-Modes-and-Abort-Logic-Architecture.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`107-000-General.md`](./107-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **STA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management.

[^ecssq40]: **ECSS-Q-ST-40C — Safety** — ESA safety standards applicable to space systems including abort, emergency, and hazard management.

[^iso14620]: **ISO 14620-1:2018 — Space Systems Safety Requirements** — International safety requirements for space launch vehicles and spacecraft.

[^milstd882]: **MIL-STD-882E — System Safety** — Hazard analysis methodology (PHL, SSHA, SHA, SSHA, O&SHA) and risk acceptance criteria.

[^nastd8739]: **NASA-STD-8739.8A — Software Assurance Standard** — Software safety requirements applicable to abort and emergency management systems.

### Applicable industry standards

- ECSS-Q-ST-40C — Safety[^ecssq40]
- ISO 14620-1:2018 — Space Systems Safety Requirements[^iso14620]
- MIL-STD-882E — System Safety[^milstd882]
- NASA-STD-8739.8A — Software Assurance Standard[^nastd8739]

[^nastd3001]: **NASA-STD-3001 Vol.1 & Vol.2 — Human Integration Design Handbook**.
[^ccsds]: **CCSDS 401.0-B — Radio Frequency and Modulation Systems** — Emergency communications protocols for crewed spacecraft.
