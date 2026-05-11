---
document_id: QATL-ATLAS-1000-STA-140-149-04-142-060-SAFE-MODE-CONTINGENCY-AND-AUTONOMOUS-RECOVERY-SOFTWARE
title: "STA 140-149 · 142-060 — Safe Mode Contingency and Autonomous Recovery Software"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "140-149"
section: "04"
section_title: "Aviónica y Control de Misión Espacial"
subsection: "142"
subsection_title: "Software de Vuelo"
subsubject: "060"
subsubject_title: "Safe Mode Contingency and Autonomous Recovery Software"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC, Q-HORIZON, Q-AIR, Q-GREENTECH, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---
# STA 140-149 · 142-060 — Safe Mode Contingency and Autonomous Recovery Software

## 1. Purpose

Defines the **flight software components for safe-mode entry, contingency mode management, and autonomous recovery sequences** that ensure spacecraft survival without ground intervention on Q+ATLANTIDE STA-band spacecraft.

## 2. Scope

- **Safe-mode transition sequences** — software-controlled safe-mode entry: save current state to non-volatile memory, disable non-essential functions, transition GNC to safe mode (→ `140` subsubject 006), reduce OBC load to minimum; safe-mode entry trigger sources: FDIR escalation (→ `005`), hardware watchdog expiry, ground-commanded entry.
- **Autonomous onboard emergency management** — autonomous power management (load shedding sequence for under-voltage); autonomous thermal management (heater activation/deactivation); onboard time-out logic for ground contact loss (enter contingency after N consecutive missed contact windows); recovery from anomalous software state via boot sequence with NVRAM configuration.
- **Contingency mode logic** — defined contingency modes for specific fault classes (GNC sensor failure contingency, power contingency, thermal contingency, communication contingency); contingency mode state machine; parameter tables configuring contingency mode behaviour; ground-commanded exit from contingency.
- **Ground-command-free recovery procedures** — fully autonomous recovery sequences executable without ground intervention; required coverage: recovery from any single-point failure within defined recovery time objective (RTO); ground command authority to override or inhibit autonomous recovery.
- **Non-volatile memory management** — boot configuration stored in EEPROM/Flash (bootloader parameters, safe-mode configuration, recovery script pointers); integrity checking (CRC) on boot data; multiple boot attempts with degraded configuration fallback.
- **Safe-mode to normal mode re-entry criteria** — all FDIR inhibits cleared, power positive, navigation converged, thermal within limits, ground-acknowledged recovery; re-entry inhibit counter management.

## 3. Diagram — Safe-Mode Entry and Autonomous Recovery Flow

```mermaid
flowchart TD
    A["Normal / Mission Mode"] -->|"FDIR escalation / watchdog / cmd"| B["Safe-Mode Entry Sequence<br/>(save state · disable non-essential · load shed)"]
    B --> C["GNC Safe Mode (140.006)<br/>(Sun-pointing · min power)"]
    C --> D["Autonomous Monitoring<br/>(power · thermal · ground contact)"]
    D -->|"ground contact restored"| E["Ground Assessment"]
    E -->|"recovery approved"| F["Re-Entry Criteria Check"]
    F -->|"all criteria met"| A
    D -->|"no contact · timeout"| G["Contingency Mode<br/>(autonomous recovery script)"]
    G --> C
    style B fill:#8b0000,color:#fff
    style C fill:#1f3a93,color:#fff
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `STA` — Space Technology Architecture |
| Master range | `100–199` |
| Code range | `140-149` |
| Section | `04` — Aviónica y Control de Misión Espacial |
| Subsection | `142` — Software de Vuelo |
| Subsubject | `006` — Safe-Mode, Contingency and Autonomous Recovery Software |
| Primary Q-Division | Q-SPACE[^qdiv] |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Document | `142-060-Safe-Mode-Contingency-and-Autonomous-Recovery-Software.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`142-000-General.md`](./142-000-General.md) |

## 5. References & Citations

[^ecssest7011c]: **ECSS-E-ST-70-11C — Space Segment Operability** — Safe-mode and contingency software requirements.

[^ecssest40c]: **ECSS-E-ST-40C — Software Engineering** — Safe-mode software implementation requirements.

[^qdiv]: **Q-Division authority** — See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline`.

### Applicable industry standards

- ECSS-E-ST-70-11C — Space Segment Operability[^ecssest7011c]
- ECSS-E-ST-40C — Software Engineering[^ecssest40c]
