---
document_id: QATL-ATLAS-1000-ATLAS-020-029-02-021-010-COMPRESSION
title: "ATLAS 020-029 · 02.021 — Air Conditioning and Pressurization · 021-010 Compression"
ata_chapter: "21"
ata_sns: "21-10-00"
local_section_code: "021-010"
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
# ATLAS 020-029 · 02.021 — Air Conditioning and Pressurization · 021-010 Compression

## 1. Purpose

Defines the **compression source architecture and interfaces** for the *Air Conditioning and Pressurization* subsystem (ATA 21-10-00) within the Q+ATLANTIDE programme. Covers the supply of compressed air from bleed-air off-takes or electric compressors, precooling/pre-treatment, and the interface with downstream ECS distribution (021-020).

## 2. Scope

- Covers the *Compression* section (`021-010`, ATA SNS 21-10-00) of subsection `021` *Air Conditioning and Pressurization*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **Bleed-air off-take** — engine high-pressure and low-pressure port selection, precooler heat-exchanger interface, and pressure-regulating/shut-off valve (PRSOV) control logic.
  - **Electric compression** (programme variant) — motor-driven compressor architecture, power draw limits, and thermal management interface for more-electric aircraft (MEA) configurations.
  - **Precooling** — primary heat exchanger (PHX) and secondary heat exchanger (SHX) function; ram-air duct interface; high-limit temperature switch logic.
  - **Crossbleed and isolation** — crossbleed duct, isolation valve positions, and engine-failure / ground-air-supply modes.
  - **Control interfaces** — PRSOV and flow-control valve (FCV) modulation; integration with ECS monitoring (021-080).
- Out of scope: air distribution routing (021-020), pressurisation differential control (021-030), heating packs (021-040), cooling packs (021-050).

## 3. Diagram — Compression Source Flow

Bleed or electric compression sources supply precooled air to the ECS distribution network.

```mermaid
flowchart LR
    ENG["Engine HP/LP Bleed Port<br/>or Electric Compressor"]:::source
    ENG --> PRSOV["PRSOV / FCV<br/>(pressure-regulating &<br/>shut-off valve)"]:::valve
    PRSOV --> PHX["Primary Heat Exchanger<br/>(PHX — precooler)"]:::hx
    PHX --> SHX["Secondary Heat Exchanger<br/>(SHX — ram-air cooled)"]:::hx
    SHX --> CROSS["Crossbleed Duct<br/>(isolation valve)"]:::duct
    CROSS --> DIST["Distribution Network<br/>(021-020)"]:::out
    MON["ECS Monitoring<br/>(021-080)"] -- control signals --> PRSOV
    MON -- temp/pressure feedback --> PHX

    classDef source fill:#1f3a93,stroke:#0b1d4a,color:#fff
    classDef valve fill:#2c82c9,stroke:#0b1d4a,color:#fff
    classDef hx fill:#eaf3fb,stroke:#2c82c9,color:#0b1d4a
    classDef duct fill:#f6e6ff,stroke:#7d3c98,color:#3b1f4d
    classDef out fill:#f0f9e8,stroke:#27ae60,color:#145a32
```

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `ATLAS` — Aircraft Top Level Architecture Schema/System (controlled term) |
| Master range | `000–099` |
| Code range | `020-029` |
| Section | `02` — Sistemas Core de Aeronave |
| Subsection | `021` — Air Conditioning and Pressurization |
| Local section code | `021-010` — Compression |
| ATA chapter | 21 |
| ATA SNS | 21-10-00 |
| Primary Q-Division | Q-AIR[^qdiv] |
| Support Q-Divisions | Q-MECHANICS, Q-DATAGOV, Q-GREENTECH |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `baseline`[^gov] |
| Folder path | `Q+ATLANTIDE/000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/021_Air-Conditioning-and-Pressurization/` |
| Document | `021-010-Compression.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`021-000-General.md`](./021-000-General.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md).

[^archtable]: **ATLAS §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `baseline` denotes documents under controlled change management within the Q+ATLANTIDE baseline.

[^cs25]: **EASA CS-25** — CS 25.831 and AMC covering bleed-air source requirements and precooler performance.

[^ata2200]: **ATA iSpec 2200** — Section 21-10 naming and data-module scope for compression subsystems.

### Applicable standards

- EASA CS-25[^cs25]
- ATA iSpec 2200[^ata2200]
