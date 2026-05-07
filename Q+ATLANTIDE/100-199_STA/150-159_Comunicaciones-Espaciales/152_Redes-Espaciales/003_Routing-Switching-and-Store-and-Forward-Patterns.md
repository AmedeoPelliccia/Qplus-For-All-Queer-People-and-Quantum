---
document_id: QATL-ATLAS-1000-STA-150-159-05-152-003-ROUTING-SWITCHING-AND-STORE-AND-FORWARD-PATTERNS
title: "STA 150-159 · 05.152.003 — Routing, Switching, and Store-and-Forward Patterns"
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
subsection: "152"
subsection_title: "Redes Espaciales"
subsubject: "003"
subsubject_title: "Routing, Switching, and Store-and-Forward Patterns"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 150-159 · 05.152.003 — Routing, Switching, and Store-and-Forward Patterns

## §1 Purpose

This document defines the routing and switching strategies applicable to Q+ATLANTIDE space networks, covering both real-time IP-based and disruption-tolerant forwarding paradigms.[^baseline] It establishes authoritative terminology for IP routing over satellite (IPoS), MPLS over satellite, virtual circuit switching, store-and-forward relay, and contact graph routing (CGR), enabling consistent design and implementation decisions across missions.[^archtable] The document also prescribes priority-based forwarding rules to enforce traffic class guarantees.[^n001]

## §2 Scope

**In scope:**

- IP routing over satellite (IPoS): adaptation of IPv4/IPv6 routing protocols (OSPF, BGP, RIP) for high-latency asymmetric satellite links[^ccsds702]
- MPLS over satellite: label-switched paths, traffic engineering, and fast reroute over space segments
- Virtual circuit switching: ATM-legacy and connection-oriented forwarding for deterministic latency applications
- Store-and-forward relay patterns: node-based message buffering, scheduled contact exploitation, and epidemic routing variants
- Contact graph routing (CGR): deterministic contact schedule computation, route selection based on predicted link availability, and Dijkstra/Yen algorithm adaptation for DTN[^ccsds720]
- Priority-based forwarding: strict priority queuing, weighted fair queuing, and preemption policies per traffic class

**Out of scope:** Physical-layer modulation and coding schemes (subsection 151), DTN bundle-layer custody transfer (subsubject 004), and QoS DSCP marking policies (subsubject 007).

## §3 Diagram

```mermaid
flowchart TD
    PKT["Incoming Packet / Bundle"]
    Q1{"Real-time\nIP path\navailable?"}
    IP["IPoS Routing\n(OSPF/BGP/RIP adapted)"]
    Q2{"MPLS LSP\nprovisioned?"}
    MPLS["MPLS Forwarding\n(label switched)"]
    Q3{"Virtual circuit\nestablished?"}
    VC["Virtual Circuit\nSwitching"]
    Q4{"Contact window\nopen?"}
    SAF["Store-and-Forward\n(buffer at node)"]
    CGR["CGR Schedule\nLookup"]
    FWD["Forward to\nnext hop"]

    PKT --> Q1
    Q1 -- Yes --> IP --> FWD
    Q1 -- No --> Q2
    Q2 -- Yes --> MPLS --> FWD
    Q2 -- No --> Q3
    Q3 -- Yes --> VC --> FWD
    Q3 -- No --> Q4
    Q4 -- Yes --> CGR --> FWD
    Q4 -- No --> SAF --> CGR

    style PKT fill:#d0e8ff,stroke:#336699
    style FWD fill:#d0f0d0,stroke:#336633
    style SAF fill:#ffd0d0,stroke:#993333
    style CGR fill:#fff0c0,stroke:#996600
```

## §4 Footprint

| Attribute | Value |
|---|---|
| Architecture | Space Technology Architecture (STA) |
| Master range | 100–199 |
| Code range | 150-159 |
| Section | 05 — Comunicaciones Espaciales |
| Subsection | 152 — Redes Espaciales |
| Subsubject | 003 — Routing, Switching, and Store-and-Forward Patterns |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-DATAGOV, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | baseline[^gov] |
| Folder path | `Q+ATLANTIDE/100-199_STA/150-159_Comunicaciones-Espaciales/152_Redes-Espaciales/` |
| Document | `003_Routing-Switching-and-Store-and-Forward-Patterns.md` |
| Parent subsection | [README.md](./README.md) · [000_Overview.md](./000_Overview.md) |
| Parent architecture | [../../README.md](../../README.md) |
| Parent baseline | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

## §5 References & Citations

[^baseline]: Q+ATLANTIDE controlled baseline (v1.0.0)
[^archtable]: §3 Architecture Table (parent)
[^qdiv]: Q-Division authority
[^gov]: Governance class — baseline
[^n001]: Note N-001 (Q+ATLANTIDE is a taxonomy/traceability ecosystem)

### Applicable industry standards

| Standard | Title |
|---|---|
| CCSDS 702.1-B | IP over CCSDS Space Links[^ccsds702] |
| CCSDS 720.1-G | Delay-Tolerant Networking Architecture[^ccsds720] |
| RFC 5050 | Bundle Protocol Specification[^rfc5050] |
| RFC 5326 | Licklider Transmission Protocol (LTP)[^rfc5326] |
| ECSS-E-ST-50C | Space engineering: Communications[^ecss50] |
| ITU-R S.1003 | Environmental protection of the geostationary-satellite orbit[^itur] |

[^ecss50]: ECSS-E-ST-50C — Space engineering: Communications
[^ccsds720]: CCSDS 720.1-G — Delay-Tolerant Networking Architecture
[^ccsds702]: CCSDS 702.1-B — IP over CCSDS Space Links
[^rfc5050]: RFC 5050 — Bundle Protocol Specification
[^rfc5326]: RFC 5326 — Licklider Transmission Protocol (LTP)
[^itur]: ITU-R S.1003 — Environmental protection of the geostationary-satellite orbit
