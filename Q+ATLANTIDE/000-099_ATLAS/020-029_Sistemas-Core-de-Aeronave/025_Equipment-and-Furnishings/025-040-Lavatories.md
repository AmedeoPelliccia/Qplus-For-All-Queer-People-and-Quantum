---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-025-040-LAVATORIES
title: "ATLAS 020-029 · 02.025 · Section 025-040 — Lavatories"
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
subsection: "025"
subsection_title: "Equipment and Furnishings"
local_section_code: "025-040"
ata_sns: "25-40-00"
title_short: "Lavatories"
primary_q_division: Q-AIR
support_q_divisions: [Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# ATLAS 020-029 · 02.025 · 025-040 — Lavatories

## 1. Purpose

Define the equipment and furnishings architecture for *Lavatories* (ATA 25-40-00) within ATLAS subsection `025`. This section covers lavatory monument structures, toilet assemblies, wash basin and mirror units, waste container systems, and lavatory internal furnishing fitments.

## 2. Scope

- Covers lavatory monument structures, door assemblies, internal liners, and ceiling panels as equipment and furnishings items.
- Includes toilet seat and cover assemblies, waste container unit fitment, and drain interfaces to the water/waste system (ATA 38).
- Addresses wash basin, soap dispenser, and hand-dryer fitments, along with lavatory lighting and ventilation interfaces as furnishings items.
- Covers lavatory smoke detector mount provisions as equipment fitment — for smoke detector systems refer to ATA 26.
- Does not replace certified maintenance data for waste system chemical procedures, plumbing pressure tests, or smoke detector calibration.

**Scope boundary:** Lavatory furnishings and fitment — monuments, toilet assemblies, basins, waste containers, internal panels. Excludes water plumbing (ATA 38), electrical circuits (ATA 24), smoke detection systems (ATA 26), and accessibility compliance documentation (airworthiness directives).

**Safety boundary:** Lavatory smoke detection mounting and waste container retention under emergency landing loads are safety-relevant. Artefacts affecting smoke detector fitment, waste container locking, or door egress interfaces require compliance evidence and maintenance sign-off traceability.

## 3. System Architecture

```mermaid
graph TD
    A025_040["025-040 Lavatories"] --> LAV_MONUMENT["Lavatory Monument\nand Door Assembly"]
    A025_040 --> LAV_TOILET["Toilet Seat\nand Waste Container"]
    A025_040 --> LAV_BASIN["Wash Basin, Soap\nDispenser and Mirror"]
    A025_040 --> LAV_PANELS["Internal Liners\nand Ceiling Panels"]
    A025_040 --> LAV_DRAIN["Drain and Waste\nInterface Provisions"]

    A038["038 Water / Waste"] -->|plumbing| A025_040
    A026["026 Fire Protection"] -->|smoke detection mount| A025_040
    A024["024 Electrical Power"] -->|lighting/ventilation| A025_040
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `025` — Equipment and Furnishings |
| Local section code | `025-040` |
| ATA SNS | `25-40-00` |
| Primary Q-Division | Q-AIR |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH, Q-GROUND, Q-INDUSTRY |
| Governance class | `baseline` |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/025_Equipment-and-Furnishings/` |
| Document | `025-040-Lavatories.md` |
| Parent subsection | [`README.md`](./README.md) |
| Parent section | [`../README.md`](../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References

- ATA iSpec 2200 — Chapter 25-40, Lavatories
- Q+ATLANTIDE controlled baseline [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)
- Subsection index [`./README.md`](./README.md)
- `025-000` General [`./025-000-General.md`](./025-000-General.md)
- `025-030` Buffet, Galley and Service Equipment [`./025-030-Buffet-Galley-and-Service-Equipment.md`](./025-030-Buffet-Galley-and-Service-Equipment.md)
