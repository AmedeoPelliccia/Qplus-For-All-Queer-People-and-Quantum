---
document_id: QATL-ATLAS-1000-ATLAS-040-049-04-040-030-AVIONICS-NETWORKS-AND-DATA-BUSES
title: "ATLAS 040-049 · 04.040.030 — Avionics Networks and Data Buses"
register: "ATLAS-1000"
register_link: "../../../README.md"
parent_baseline: "Q+ATLANTIDE"
parent_baseline_doc: "../../../../organization/Q+ATLANTIDE.md"
parent_architecture_doc: "../../../README.md"
parent_section_doc: "../../README.md"
parent_subsection_doc: "./README.md"
architecture_code: "ATLAS"
architecture_name: "Aircraft Top Level Architecture Schema/System"
architecture_link: "../../../README.md"
master_range: "000–099"
master_range_title: "New Commercial Aircraft Architectures"
master_range_link: "../../../README.md"
code_range: "040-049"
code_range_title: "Aviónica, Información & APU"
code_range_link: "../../README.md"
section: "04"
section_title: "Aviónica, Información & APU"
section_link: "../../README.md"
subsection: "040"
subsection_title: "Multisystem"
subsection_link: "./README.md"
subsubject: "030"
subsubject_title: "Avionics Networks and Data Buses"
subsubject_file: "040-030-Avionics-Networks-and-Data-Buses.md"
subsubject_link: "./040-030-Avionics-Networks-and-Data-Buses.md"
primary_q_division: "Q-DATAGOV"
primary_q_division_link: "../../../../organization/Q-Divisions/Q-DATAGOV.md"
support_q_divisions:
  - name: "Q-AIR"
    link: "../../../../organization/Q-Divisions/Q-AIR.md"
  - name: "Q-SPACE"
    link: "../../../../organization/Q-Divisions/Q-SPACE.md"
  - name: "Q-HPC"
    link: "../../../../organization/Q-Divisions/Q-HPC.md"
orb_function_support:
  - name: "ORB-PMO"
    link: "../../../../organization/ORB-Functions/ORB-PMO.md"
  - name: "ORB-LEG"
    link: "../../../../organization/ORB-Functions/ORB-LEG.md"
governance_class: "baseline"
governance_class_link: "#ref-gov"
version: "1.0.0"
status: "active"
language: "en"
s1000d_applicability: "S1000D-CSDB-compatible"
s1000d_reference_link: "#ref-s1000d"
ata_reference: "ATA iSpec 2200"
ata_reference_link: "#ref-ata-ispec-2200"
created: "2026-05-09"
updated: "2026-05-09"
review_status: "to-be-reviewed-by-system-expert"
---

# ATLAS 040-049 · Section 04 · Subsection 040 · 030 — Avionics Networks and Data Buses

## 0. Hyperlink Policy

All linkable content in this file shall be expressed as Markdown links where a stable target exists.
Use relative links for repository-internal content; anchor links for headings, diagrams, glossary terms, citations, references, and footprint entries.
Use `TBD` as placeholder where no stable target yet exists.
Parent context: [040-000 Multisystem General](./040-000-Multisystem-General.md) | IMA: [040-010](./040-010-Integrated-Modular-Avionics-IMA.md).

---

## 1. Purpose

This document defines the avionics network and data bus architecture for the AMPEL360E aircraft. It covers AFDX (ARINC 664 Part 7) virtual link architecture, bandwidth allocation groups (BAG), end-system configuration, legacy buses (ARINC 429, MIL-STD-1553), network redundancy schemes, switch topology, traffic shaping, and bandwidth allocation. It is the primary reference for network architects, avionics integration engineers, and certification authorities.

---

## 2. Applicability

| Attribute | Value |
|-----------|-------|
| Aircraft Model | AMPEL360E (all variants) |
| ATA Reference | [ATA iSpec 2200](#ref-ata-ispec-2200) — Chapter 040 |
| Primary Network Standard | [ARINC 664 Part 7](#ref-arinc-664) (AFDX) |
| Legacy Bus Standards | [ARINC 429](#ref-arinc-429), [MIL-STD-1553B](#ref-1553) |
| Development Assurance | [DO-178C](#ref-do-178c), [DO-254](#ref-do-254) |
| Applicability Code | All S/N unless superseded by service bulletin |

---

## 3. System / Function Overview

The AMPEL360E avionics network uses a dual-redundant AFDX fabric (Network A and Network B) composed of AFDX switches interconnecting IMA Cabinets, avionics LRUs, displays, and maintenance terminals. Virtual Links (VLs) provide deterministic, unidirectional, latency-bounded data paths between end-systems. Legacy ARINC 429 buses serve sensors and actuators not yet migrated to AFDX. MIL-STD-1553B serves specific military-grade subsystems. All networks are fully redundant; end-systems select active network based on reception.

---

## 4. Scope

### 4.1 Included

- AFDX dual-redundant switch topology (Network A / Network B)
- Virtual Link (VL) configuration: BAG, max frame size, latency budget
- AFDX end-system architecture and traffic shaping
- ARINC 429 channel allocation and word definitions
- MIL-STD-1553B bus controller / remote terminal allocation
- Network health monitoring and fault isolation
- Bandwidth allocation and load analysis

### 4.2 Excluded

- Physical wiring and harness routing (see wiring design documents)
- Application-layer data content (each system chapter)
- Time synchronisation over AFDX (see [040-060](./040-060-Time-Synchronization-and-Data-Integrity.md))

---

## 5. Architecture Description

**AFDX Fabric**: Two fully independent AFDX networks (A and B), each comprising a star topology with a core switch (AFDX-SW-A, AFDX-SW-B) and edge ports for up to 100 end-systems. End-systems implement ARINC 664 Part 7 traffic shaping (leaky bucket per VL) to guarantee maximum frame inter-arrival time equal to BAG. Dual-end-system redundancy management selects data from the network with the best integrity status.

**Virtual Links**: Each VL is unidirectional, from one source end-system to one or more destination end-systems. VL parameters (BAG, payload size, latency budget) are defined in the Network Definition File (NDF) and enforced by the switch.

**Legacy Buses**: ARINC 429 high-speed (100 kbps) and low-speed (12.5 kbps) channels connect to CPIOM I/O termination cards. MIL-STD-1553B bus controllers reside on dedicated I/O modules.

---

## 6. Functional Breakdown

| Function ID | Function Name | Description | Allocated To | DAL |
|-------------|---------------|-------------|-------------|-----|
| F-001 | VL Traffic Shaping | Leaky-bucket enforcement of BAG per VL at source end-system | AFDX End-System | A |
| F-002 | Switch Filtering & Policing | VL integrity check and frame forwarding per NDF | AFDX Switch | A |
| F-003 | Redundancy Management | Selection of valid frame from Network A or B at destination | AFDX End-System | A |
| F-004 | ARINC 429 Transmit/Receive | Serial data encoding and decoding per ARINC 429 | CPIOM I/O | B |
| F-005 | MIL-STD-1553B BC/RT | Bus controller and remote terminal protocol management | 1553 I/O Module | B |
| F-006 | Network Health Monitoring | VL integrity counters, error rate monitoring, switch port status | AFDX Switch + CMC | B |
| F-007 | NDF Configuration | Load and apply Network Definition File defining all VL parameters | Ground loader / ARINC 615A | B |

---

## 7. Mermaid — System Context Diagram

```mermaid
graph TB
    subgraph NetworkFabric["AFDX Dual Network Fabric"]
        SW_A["AFDX Switch A\n(Network A)"]
        SW_B["AFDX Switch B\n(Network B)"]
    end
    IMA_L["IMA Cabinet L\nEnd-System"]
    IMA_R["IMA Cabinet R\nEnd-System"]
    EFIS["EFIS Display\nEnd-System"]
    CMC["CMC\nEnd-System"]
    AMT["Avionics Maint.\nTerminal"]
    SENSOR["Sensors via\nARINC 429 / 1553"]

    IMA_L --> SW_A & SW_B --> IMA_R & EFIS & CMC & AMT
    SENSOR --> IMA_L & IMA_R
```

---

## 8. Mermaid — Internal Functional Architecture

```mermaid
graph LR
    subgraph EndSys["AFDX End-System"]
        TX["TX Traffic Shaper\n(Leaky Bucket per VL)"]
        RX_A["RX Network A"]
        RX_B["RX Network B"]
        RM["Redundancy Manager\n(select A or B)"]
        APP["Application\n(APEX Port)"]
    end
    subgraph Switch["AFDX Switch"]
        FP["Filtering &\nPolicing"]
        FWD["Frame\nForwarding"]
        MON["Health Monitor\nCounters"]
    end

    APP --> TX --> Switch
    Switch --> RX_A & RX_B --> RM --> APP
    FP --> FWD --> MON
```

---

## 9. Mermaid — Lifecycle Traceability

```mermaid
graph LR
    LC02["LC02\nRequirements"]
    LC03["LC03\nDesign"]
    LC05["LC05\nImplementation"]
    LC06["LC06\nVerification"]
    LC10["LC10\nCertification"]
    LC11["LC11\nOperation"]
    LC12["LC12\nDisposal"]
    CSDB["CSDB\nData Modules"]
    DMRL["DMRL"]
    Evidence["Network\nVerification Evidence"]

    LC02 --> LC03 --> LC05 --> LC06 --> LC10 --> LC11 --> LC12
    LC02 --> DMRL --> CSDB
    LC06 --> Evidence --> LC10
    LC11 --> CSDB
```

---

## 10. Interfaces

| Interface ID | From | To | Protocol / Standard | Direction | Notes |
|-------------|------|----|---------------------|-----------|-------|
| IF-030-01 | IMA End-System | AFDX Switch | ARINC 664 Part 7 / 100BASE-TX | Bidirectional | Primary data fabric |
| IF-030-02 | AFDX Switch A | AFDX Switch B | Cross-link (optional) | Bidirectional | TBD — inter-switch redundancy |
| IF-030-03 | CPIOM I/O | Sensors/Actuators | ARINC 429 | Bidirectional | Per channel allocation |
| IF-030-04 | 1553 I/O Module | Subsystems | MIL-STD-1553B | Bidirectional | BC or RT per allocation |
| IF-030-05 | AFDX Switch | CMC | ARINC 664 / SNMP-like | Output | Network health telemetry |
| IF-030-06 | Ground Loader | End-System NDF | ARINC 615A / Ethernet | Input | NDF configuration load |

---

## 11. Operating Modes

| Mode | Description | Trigger | System Response |
|------|-------------|---------|-----------------|
| Normal | Both Network A and B active; redundancy management operating | Nominal | All VLs active; data from preferred network |
| Degraded | One network failed; single network operation | Switch or cable fault detected | Redundancy manager selects surviving network; alert to CMC |
| Maintenance | Network in diagnostic mode; NDF reload active | AMT command | VL scheduling suspended; network accessible for loading |
| Failure/Safe State | Both networks inoperative for critical VL | Double-network failure | Affected hosted applications enter safe state; crew CAS alert |

---

## 12. Monitoring and Diagnostics

- AFDX switch maintains per-VL integrity counters (received frames, discarded frames, integrity violations).
- End-system reports per-VL redundancy management status to IMA HM.
- Switch port status (link up/down, error rate) forwarded to [CMC](./040-080-Multisystem-Monitoring-Diagnostics-and-Control-Interfaces.md) via management VL.
- ARINC 429 parity error and word rate counters maintained by CPIOM BITE.
- 1553 bus error counters maintained by BC module; available via AMT.

---

## 13. Maintenance Concept

| Task | Interval | Access | Tooling |
|------|----------|--------|---------|
| AFDX switch health review | Power-up | CMC / AMT | None |
| AFDX switch LRU swap | On condition | E/E Bay | Standard avionics tools |
| NDF reload | On demand / post-modification | AMT / Ground loader | ARINC 615A loader |
| ARINC 429 wire continuity | Per maintenance cycle | Wiring inspection | Multimeter |
| VL bandwidth audit | Post modification | Engineering analysis | Network analysis tool |

---

## 14. S1000D / CSDB Mapping

| Document Type | Data Module Code (DMC) | Info Code | Title |
|---------------|----------------------|-----------|-------|
| System Description | DMC-AMPEL360E-EWTW-040-030-00A-040A-A | 040 | Avionics Network Description |
| Maintenance Procedures | DMC-AMPEL360E-EWTW-040-030-00A-300A-A | 300 | AFDX Fault Isolation |
| BITE/Test | DMC-AMPEL360E-EWTW-040-030-00A-400A-A | 400 | Network BITE Procedures |
| Wiring Data | DMC-AMPEL360E-EWTW-040-030-00A-520A-A | 520 | Network Wiring and Connector Data |
| IPD | DMC-AMPEL360E-EWTW-040-030-00A-941A-A | 941 | Network LRU Illustrated Parts |
| Software Desc | DMC-AMPEL360E-EWTW-040-030-00A-720A-A | 720 | NDF and Switch Configuration |

### Recommended Data Module Set

| Info Code | Publication | Applicability |
|-----------|-------------|---------------|
| 040 | AMM — System Description | All variants |
| 300 | FIM — Fault Isolation | All variants |
| 400 | TSM — BITE Procedures | All variants |
| 520 | AMM — Wiring Data | All variants |
| 720 | SRM — NDF Description | All variants |
| 941 | IPD — Parts Data | All variants |

---

## 15. Footprints

### 15.1 Physical

| Item | Dimension (mm) | Mass (kg) | Location |
|------|---------------|-----------|----------|
| AFDX Switch A | 300 × 150 × 40 | 2.5 | E/E Bay — Centre |
| AFDX Switch B | 300 × 150 × 40 | 2.5 | E/E Bay — Centre |
| AFDX cable harness | — | 8.0 (est.) | Aircraft-wide routing |

### 15.2 Electrical / Data

| Interface | Standard | Bandwidth / Power |
|-----------|----------|-------------------|
| AFDX | ARINC 664 Part 7 / 100BASE-TX | 100 Mbps per port |
| ARINC 429 HS | ARINC 429 | 100 kbps |
| MIL-STD-1553B | MIL-STD-1553B | 1 Mbps |
| Switch power | 28 VDC | 30 W per switch |

### 15.3 Maintenance

| Task | Man-Hours | Skill Level | Access |
|------|-----------|-------------|--------|
| Switch swap | 0.5 | Avionics tech | E/E Bay |
| NDF reload | 0.5 | Avionics tech | AMT |
| Cable inspection | 2.0 | Avionics tech | Multiple zones |

### 15.4 Data

| Data Item | Volume | Storage | Retention |
|-----------|--------|---------|-----------|
| NDF (Network Definition File) | 5 MB | Protected NVM | Until updated |
| VL integrity counters log | 64 MB | Switch NVM / CSDB | 500 FH rolling |
| ARINC 429 error log | 16 MB | CPIOM NVM | 500 FH rolling |

---

## 16. Safety and Certification Considerations

- Dual-network AFDX topology provides single-failure tolerance for all critical VLs.
- VL traffic shaping enforced at source ensures no single application can monopolise bandwidth.
- Latency budget analysis required per VL; worst-case end-to-end latency must satisfy hosted application requirements.
- Switch certification per [DO-178C](#ref-do-178c) (firmware) and [DO-254](#ref-do-254) (hardware) required.
- ARINC 664 Part 7 compliance verification required at system integration level.
- Network redundancy independence analysis must demonstrate A and B networks are physically and electrically separated.

---

## 17. Verification and Validation

| V&V ID | Requirement | Method | Success Criteria | Status |
|--------|-------------|--------|-----------------|--------|
| VV-030-01 | VL maximum latency | Network simulation + bench test | Worst-case latency within budget | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| VV-030-02 | VL traffic shaping | Bench test — overload injection | No VL exceeds BAG period | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| VV-030-03 | Network A/B independence | Physical inspection + test | No shared single-point failure | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| VV-030-04 | Redundancy manager selection | Fault injection | Correct network selected within 1 frame | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| VV-030-05 | NDF load and activation | Integration test | All VLs active post-load | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |

---

## 18. Glossary

| Term/Acronym | Definition | Link |
|-------------|-----------|------|
| <a id="glossary-afdx"></a>AFDX | Avionics Full-Duplex Switched Ethernet — ARINC 664 Part 7 deterministic network | [§3](#3-system--function-overview) |
| <a id="glossary-vl"></a>VL | Virtual Link — unidirectional, bandwidth-bounded communication path in AFDX | [§5](#5-architecture-description) |
| <a id="glossary-bag"></a>BAG | Bandwidth Allocation Gap — minimum interval between AFDX frames on a VL | [§6](#6-functional-breakdown) |
| <a id="glossary-ndf"></a>NDF | Network Definition File — configuration file defining all VL parameters | [§5](#5-architecture-description) |
| <a id="glossary-es"></a>ES | End-System — AFDX network interface implementing ARINC 664 Part 7 | [§5](#5-architecture-description) |
| <a id="glossary-a429"></a>ARINC 429 | ARINC 429 — unidirectional serial avionics data bus standard | [§5](#5-architecture-description) |
| <a id="glossary-1553"></a>MIL-STD-1553B | Military standard 1 Mbps avionics bus with BC/RT/MT architecture | [§5](#5-architecture-description) |
| <a id="glossary-bc"></a>BC | Bus Controller — MIL-STD-1553B master node | [§6](#6-functional-breakdown) |
| <a id="glossary-rt"></a>RT | Remote Terminal — MIL-STD-1553B slave node | [§6](#6-functional-breakdown) |
| <a id="glossary-rm"></a>RM | Redundancy Management — selection logic choosing valid data from Network A or B | [§6](#6-functional-breakdown) |
| <a id="glossary-snmp"></a>SNMP | Simple Network Management Protocol — used for switch health monitoring | [§12](#12-monitoring-and-diagnostics) |
| <a id="glossary-dal"></a>DAL | Design Assurance Level — rigor level per DO-178C/DO-254 | [§16](#16-safety-and-certification-considerations) |

---

## 19. Citations

| Ref | Citation | Use | Link |
|-----|---------|-----|------|
| <a id="ref-arinc-664"></a>ARINC 664 | ARINC 664 Part 7 — Aircraft Data Network, Avionics Full Duplex Switched Ethernet | AFDX network standard | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| <a id="ref-arinc-429"></a>ARINC 429 | ARINC 429 — Mark 33 Digital Information Transfer System | Legacy bus standard | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| <a id="ref-1553"></a>MIL-STD-1553B | MIL-STD-1553B — Aircraft Internal Time Division Command/Response Multiplex Data Bus | Military bus standard | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| <a id="ref-do-178c"></a>DO-178C | RTCA DO-178C | Software assurance | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| <a id="ref-do-254"></a>DO-254 | RTCA DO-254 | Hardware assurance | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| <a id="ref-gov"></a>GOV | Q+ATLANTIDE Governance Framework | Document governance | [Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |
| <a id="ref-s1000d"></a>S1000D | S1000D Issue 5.0 | CSDB mapping | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| <a id="ref-ata-ispec-2200"></a>ATA iSpec 2200 | ATA iSpec 2200 | ATA chapter alignment | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |

---

## 20. References

| Ref | Document | Identifier | Revision | Status | Link |
|-----|---------|-----------|---------|--------|------|
| REF-030-01 | Multisystem General | QATL-ATLAS-1000-ATLAS-040-049-04-040-000 | 1.0.0 | Active | [040-000](./040-000-Multisystem-General.md) |
| REF-030-02 | IMA Platform | QATL-ATLAS-1000-ATLAS-040-049-04-040-010 | 1.0.0 | Active | [040-010](./040-010-Integrated-Modular-Avionics-IMA.md) |
| REF-030-03 | ARINC 664 Part 7 | ARINC 664-7 | Current | Normative | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| REF-030-04 | ARINC 429 | ARINC 429 | Current | Normative | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| REF-030-05 | MIL-STD-1553B | MIL-STD-1553B | Current | Normative | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |

---

## 21. Open Issues

| ID | Issue | Owner | Status | Link |
|----|-------|-------|--------|------|
| OI-030-01 | AFDX switch vendor selection pending procurement | Q-AIR | Open | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| OI-030-02 | VL latency budget analysis for FCS critical VLs to be completed | Q-DATAGOV | Open | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
| OI-030-03 | MIL-STD-1553B usage to be confirmed for non-military variant | Q-AIR | Open | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |

---

## 22. Change Log

| Version | Date | Author | Change | Link |
|---------|------|--------|--------|------|
| 1.0.0 | 2026-05-09 | Q+ Team/Amedeo Pelliccia + AI | Initial creation with full 22-section template | <img src="https://img.shields.io/badge/TBD-red" alt="TBD"> |
