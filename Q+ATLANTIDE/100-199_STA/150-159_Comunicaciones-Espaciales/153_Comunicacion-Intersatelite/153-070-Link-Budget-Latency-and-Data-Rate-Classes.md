---
document_id: QATL-ATLAS-1000-STA-150-159-05-153-070-LINK-BUDGET-LATENCY-AND-DATA-RATE-CLASSES
title: "STA 150-159 · 153-070 — Link Budget Latency and Data Rate Classes"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "150-159"
section: "05"
section_title: "Comunicaciones Espaciales"
subsection: "153"
subsection_title: "Comunicación Intersatélite"
subsubject: "070"
subsubject_title: "Link Budget Latency and Data Rate Classes"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 150-159 · 153-070 — Link Budget Latency and Data Rate Classes

## §1 Purpose

This document defines the ISL link-budget methodology and data-rate taxonomy used throughout Q+ATLANTIDE STA subsection 153, providing a controlled framework for ISL performance analysis.[^baseline] It decomposes the end-to-end latency budget into propagation and processing contributors and establishes the four Q+ATLANTIDE ISL rate classes (Class I–IV).[^archtable] The methodology defined here is the normative reference for evidence-package content (→ 010) and is informed by the physical-layer parameters (→ 003) and APT losses (→ 004).[^qdiv]

## §2 Scope

**In scope:**

- ISL link-budget chain: transmit EIRP (dBW), free-space path loss (FSPL = 20·log(4πd/λ) dB), pointing loss (derived from APT residual, → 004), atmospheric loss (negligible in vacuum), receiver sensitivity (dBW), and received Eb/N0 margin.
- Latency budget decomposition: one-way propagation delay (d/c ms), on-board processing latency (framing, encoding, switching), and queueing delay per routing hop.
- Q+ATLANTIDE ISL data-rate class taxonomy: Class I (< 1 Mbps, TM/TC), Class II (1–100 Mbps, housekeeping data), Class III (100 Mbps–10 Gbps, payload data relay), Class IV (> 10 Gbps, high-throughput optical).
- Link margin requirements per class: minimum Eb/N0 margin (dB) vs. modulation order and coding rate.

**Out of scope:** Physical-layer technology selection (→ 003), routing algorithm design (→ 005), security overhead impact on throughput (→ 008).

## §3 Diagram

```mermaid
flowchart LR
    A[ISL Transmitter] -->|EIRP dBW| B[Free-Space Path Loss\nFSPL = 20·log 4πd/λ dB]
    B -->|Received power| C[Pointing Loss\nfrom APT residual]
    C -->|Adjusted Rx power| D[Receiver\nSensitivity dBW]
    D -->|Eb/N0 margin| E{Margin ≥ Threshold?}
    E -- Yes --> F[Link Closed]
    E -- No --> G[Link Margin Violation\nAdjust EIRP or coding]

    F --> H[Latency Budget]
    H --> H1[Propagation delay\nd/c ms]
    H --> H2[Processing latency\nframing + encoding + switching]
    H --> H3[Queueing delay\nper routing hop]

    H --> I[ISL Rate Class]
    I --> I1[Class I < 1 Mbps\nTM / TC commands]
    I --> I2[Class II 1–100 Mbps\nHousekeeping data]
    I --> I3[Class III 100 Mbps–10 Gbps\nPayload relay]
    I --> I4[Class IV > 10 Gbps\nHigh-throughput optical]
```

## §4 Footprint

| Field | Value |
|-------|-------|
| Architecture | Space Technology Architecture (STA) |
| Master range | 100–199 |
| Code range | 150-159 |
| Section | 05 — Comunicaciones Espaciales |
| Subsection | 153 — Comunicación Intersatélite |
| Subsubject | 007 — Link Budget, Latency, and Data-Rate Classes |
| Primary Q-Division | Q-SPACE |
| Support Q-Divisions | Q-DATAGOV, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | baseline |
| Folder path | `Q+ATLANTIDE/100-199_STA/150-159_Comunicaciones-Espaciales/153_Comunicacion-Intersatelite/` |
| Document | `153-070-Link-Budget-Latency-and-Data-Rate-Classes.md` |
| Parent subsection | [README.md](./README.md) · [`153-000-General.md`](./153-000-General.md) |
| Parent architecture | [../../README.md](../../README.md) |
| Parent baseline | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

## §5 References & Citations

[^baseline]: Q+ATLANTIDE controlled baseline (v1.0.0)
[^archtable]: §3 Architecture Table (parent)
[^qdiv]: Q-Division authority
[^gov]: Governance class — baseline
[^ecss50]: ECSS-E-ST-50C — Space engineering: Communications
[^ccsds401]: CCSDS 401.0-B — Radio Frequency and Modulation Systems
[^ccsds141]: CCSDS 141.0-B — Optical Communications
[^ccsds131]: CCSDS 131.0-B — TM Synchronization and Channel Coding
[^itur]: ITU-R F.1491 — Inter-satellite link characteristics
[^nasa4005]: NASA-STD-4005 — LEO Spacecraft Charging Design Standard
[^n001]: Note N-001 (Q+ATLANTIDE is a taxonomy/traceability ecosystem)

### Applicable industry standards

| Standard | Title | Relevance |
|----------|-------|-----------|
| CCSDS 401.0-B | Radio Frequency and Modulation Systems | RF-ISL EIRP and modulation parameters |
| CCSDS 141.0-B | Optical Communications | Optical-ISL link budget parameters |
| CCSDS 131.0-B | TM Synchronization and Channel Coding | Coding gain in link-budget margin |
| ITU-R F.1491 | Inter-satellite link characteristics | ISL FSPL and frequency allocation |
| ECSS-E-ST-50C | Space engineering: Communications | ISL link-budget methodology framework |
