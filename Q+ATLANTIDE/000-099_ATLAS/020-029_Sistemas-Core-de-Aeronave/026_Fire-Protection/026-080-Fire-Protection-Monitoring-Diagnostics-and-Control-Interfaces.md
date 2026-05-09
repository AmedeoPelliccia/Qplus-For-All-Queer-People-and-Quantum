---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-026-080-FIRE-PROTECTION-MONITORING-DIAGNOSTICS-AND-CONTROL-INTERFACES
title: "ATLAS 020-029 · 02.026 · Section 026-080 — Fire Protection Monitoring, Diagnostics and Control Interfaces"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
parent_subsection_doc: ./README.md
architecture_code: ATLAS
architecture_name: "Aircraft Top Level Architecture Schema/System"
master_range: "000–099"
code_range: "020-029"
section: "02"
section_title: "Sistemas Core de Aeronave"
subsection: "026"
subsection_title: "Fire Protection"
local_section_code: "026-080"
ata_sns: "26-80-00"
title_short: "Fire Protection Monitoring, Diagnostics and Control Interfaces"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: programme-controlled-diagnostics-extension
status_note: >
  Section 026-080 is a programme-controlled diagnostics extension covering
  fire protection system health monitoring, BITE diagnostics, and CMS control
  interfaces beyond the baseline ATA 26 scope. Activation requires programme
  authority and is controlled by Q-AIR.
language: en
---

# ATLAS 020-029 · 02.026 · 026-080 — Fire Protection Monitoring, Diagnostics and Control Interfaces

## 1. Purpose

Define the architecture boundary for *Fire Protection Monitoring, Diagnostics and Control Interfaces* (ATA 26-80-00) within ATLAS subsection `026`. This section covers fire protection system health monitoring, BITE for detection loops and extinguishing squib circuits, centralised fault isolation logic, ARINC data bus interfaces for fire system status, and the Central Maintenance System (CMS) health data output.

> **Programme-controlled diagnostics extension.** This section covers monitoring, health management, and advanced diagnostics interfaces activated under programme authority. Architecture boundary and Q-Division assignments require formal programme review before population of detailed design data modules.

## 2. Scope

- Aligned to ATA SNS `26-80-00 Fire Protection Monitoring and Diagnostics` (programme-controlled diagnostics extension of baseline ATA 26 scope).
- Covers fire loop BITE (loop continuity, open/short circuit detection), extinguishing squib BITE (squib resistance monitoring, discharge circuit integrity), bottle pressure monitoring, smoke detector response time and sensitivity validation, centralised fire system status bus (ARINC 429/664), fault isolation logic, CMS health data interface, and maintenance control panel.
- Does not cover core detection hardware (see `026-010`), extinguishing bottles (see `026-020`), or zone-specific protection architecture.

## 3. System Architecture

```mermaid
graph TD
    A026_080["026-080 Fire Protection Monitoring,\nDiagnostics and Control Interfaces\n(ATA 26-80-00 — PCDE)"]

    A026_080 --> LoopBITE["Detection Loop\nBITE (Continuity / Resistance)"]
    A026_080 --> SquibBITE["Squib Circuit\nBITE (Discharge Integrity)"]
    A026_080 --> BottleMonitor["Extinguishing Bottle\nPressure Monitoring"]
    A026_080 --> FaultIso["Fault Isolation\nLogic"]
    A026_080 --> StatusBus["Fire System Status Bus\n(ARINC 429 / 664)"]

    A026_010["026-010 Fire Detection"] -->|detector status| A026_080
    A026_020["026-020 Fire Extinguishing"] -->|bottle/squib status| A026_080
    A026_080 -->|health data| CMS["041 Central Maintenance System"]
    A026_080 -->|maintenance data| MaintPanel["Maintenance\nControl Panel"]
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `026` — Fire Protection |
| Local section code | `026-080` |
| ATA SNS | `26-80-00` |
| Status | `programme-controlled-diagnostics-extension` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/026_Fire-Protection/` |
| Document | `026-080-Fire-Protection-Monitoring-Diagnostics-and-Control-Interfaces.md` |
| Parent subsection | [`README.md`](./README.md) |

## 5. References

- ATA iSpec 2200 — Chapter 26-80, Fire Protection Monitoring
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `026-010` Fire and Smoke Detection [`./026-010-Fire-and-Smoke-Detection.md`](./026-010-Fire-and-Smoke-Detection.md)
- `026-020` Fire Extinguishing [`./026-020-Fire-Extinguishing.md`](./026-020-Fire-Extinguishing.md)
- ATA 41 — Central Maintenance System (CMS)
