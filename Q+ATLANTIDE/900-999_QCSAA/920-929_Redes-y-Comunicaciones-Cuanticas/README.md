---
document_id: QATL-ATLAS1000-QCSAA-920-929-02-README
title: "QCSAA 920–929 · 02 — Redes y Comunicaciones Cuánticas (Section Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../README.md
architecture_code: QCSAA
architecture_name: "Quantum Computing & Sentient Agency Architecture"
master_range: "900–999"
code_range: "920-929"
section: "02"
section_title: "Redes y Comunicaciones Cuánticas"
section_title_en: "Quantum Networks and Communications"
governance_class: restricted
restricted_rule: N-006
primary_q_division: Q-SPACE
support_q_divisions: [Q-HORIZON, Q-DATAGOV]
orb_function_support: [ORB-PMO, ORB-LEG]
version: 1.0.0
status: active
language: en
---

# QCSAA 920–929 · Section 02 — Redes y Comunicaciones Cuánticas

## 1. Purpose

Section-level index for *Redes y Comunicaciones Cuánticas* (`920-929`) within the QCSAA band. Quantum Networks and Communications: Quantum network foundations, channels, entanglement distribution, repeaters, QKD, quantum internet, satellite and free-space QComm.

This section is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. Bands classify technologies, Q-Divisions provide technical authority and ORB-Functions provide enterprise support[^n002].

**Restricted band (N-006[^n006]).** All subsections and templates under this section additionally inherit `governance_class: restricted`.

## 2. Scope

- Aggregates the subsections within the `920-929` code range listed in §3.
- Inherits Q-Division authority and ORB support from the parent row in [`../README.md` §3](../README.md#3-architecture-table)[^archtable].
- Each subsection folder contains its own `README.md` (subsection index) and may contain Overview and subsubject documents.
- All subsections under this section must declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile` per rule N-006[^n006].

## 3. Subsection Index

| Code | Title | Folder | Status |
|---:|---|---|---|
| `920` | Quantum Network Foundations | [`./920_Quantum-Network-Foundations/`](./920_Quantum-Network-Foundations/) | active |
| `921` | Quantum Channels and Capacity | [`./921_Quantum-Channels-and-Capacity/`](./921_Quantum-Channels-and-Capacity/) | active |
| `922` | Entanglement Distribution and Swapping | [`./922_Entanglement-Distribution-and-Swapping/`](./922_Entanglement-Distribution-and-Swapping/) | active |
| `923` | Quantum Repeaters and Memory | [`./923_Quantum-Repeaters-and-Memory/`](./923_Quantum-Repeaters-and-Memory/) | active |
| `924` | Quantum Key Distribution Protocols | [`./924_Quantum-Key-Distribution-Protocols/`](./924_Quantum-Key-Distribution-Protocols/) | active |
| `925` | Quantum Internet Architectures and Protocols | [`./925_Quantum-Internet-Architectures-and-Protocols/`](./925_Quantum-Internet-Architectures-and-Protocols/) | active |
| `926` | Satellite Based Quantum Communication | [`./926_Satellite-Based-Quantum-Communication/`](./926_Satellite-Based-Quantum-Communication/) | active |
| `927` | Free Space and Fiber QComm Engineering | [`./927_Free-Space-and-Fiber-QComm-Engineering/`](./927_Free-Space-and-Fiber-QComm-Engineering/) | active |
| `928` | QComm Resource Estimation and Range Bounds | [`./928_QComm-Resource-Estimation-and-Range-Bounds/`](./928_QComm-Resource-Estimation-and-Range-Bounds/) | active |
| `929` | Aerospace QComm Use Cases and Assurance Boundaries | [`./929_Aerospace-QComm-Use-Cases-and-Assurance-Boundaries/`](./929_Aerospace-QComm-Use-Cases-and-Assurance-Boundaries/) | active |

## 4. Interfaces Diagram

```mermaid
flowchart TB
    PARENT["QCSAA<br/>(`900–999` master range)"]:::parent
    SEC["Section 02 · 920-929<br/>Redes y Comunicaciones Cuánticas"]:::sec
    PARENT --> SEC

    subgraph SUBS["Subsections"]
        direction LR
        SUB_920["920 — Quantum Network Foundations"]:::sub
        SUB_921["921 — Quantum Channels and Capacity"]:::sub
        SUB_922["922 — Entanglement Distribution and Swapping"]:::sub
        SUB_923["923 — Quantum Repeaters and Memory"]:::sub
        SUB_924["924 — Quantum Key Distribution Protocols"]:::sub
        SUB_925["925 — Quantum Internet Architectures and Protocols"]:::sub
        SUB_926["926 — Satellite Based Quantum Communication"]:::sub
        SUB_927["927 — Free Space and Fiber QComm Engineering"]:::sub
        SUB_928["928 — QComm Resource Estimation and Range Bounds"]:::sub
        SUB_929["929 — Aerospace QComm Use Cases and Assurance Boundaries"]:::sub
    end
    SEC --> SUBS

    SUBS --> SUB_920
    SUBS --> SUB_921
    SUBS --> SUB_922
    SUBS --> SUB_923
    SUBS --> SUB_924
    SUBS --> SUB_925
    SUBS --> SUB_926
    SUBS --> SUB_927
    SUBS --> SUB_928
    SUBS --> SUB_929

    QPRIM["Q-SPACE<br/>(primary Q-Division)"]:::qdiv
    QSUPP["Q-HORIZON, Q-DATAGOV<br/>(support Q-Divisions)"]:::qdiv
    ORB["ORB-PMO, ORB-LEG<br/>(ORB support)"]:::orb

    SEC --> QPRIM
    SEC -.-> QSUPP
    SEC -.-> ORB

    classDef parent fill:#1f3a93,stroke:#0b1d4a,color:#fff
    classDef sec fill:#2c82c9,stroke:#0b1d4a,color:#fff
    classDef sub fill:#eaf3fb,stroke:#2c82c9,color:#0b1d4a
    classDef qdiv fill:#f6e6ff,stroke:#7d3c98,color:#3b1f4d
    classDef orb fill:#fff4dd,stroke:#b9770e,color:#5a3b00
```

*Solid arrows show parent→section→subsection ownership and primary Q-Division authority; dotted arrows show support Q-Divisions and ORB enterprise support.*

## 5. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `920-929` |
| Section | `02` — Redes y Comunicaciones Cuánticas |
| Subsections | 10 populated |
| Primary Q-Division | Q-SPACE[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/920-929_Redes-y-Comunicaciones-Cuanticas/` |
| Document | `README.md` (this file) |
| Parent architecture | [`../README.md`](../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsections under this section inherit `architecture_code = QCSAA`, `primary_q_division = Q-SPACE`, and `governance_class = restricted` from this section header. Templates declared in this section must also declare `evidence_package_id` and `access_control_profile` per rule N-006[^n006]. The No-AAA Rule[^n004] applies.

## 6. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Architecture Table (parent)** — [`../README.md` §3](../README.md#3-architecture-table). Source of authority for primary/support Q-Divisions and ORB support of this section.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `restricted` denotes documents requiring additional governance, evidence packages and access controls (rule N-006[^n006]).

[^templates]: **§5 — Templates System** — [`organization/Q+ATLANTIDE.md` §5](../../../organization/Q+ATLANTIDE.md#5-templates-system).

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../organization/Q+ATLANTIDE.md#4-notes).

[^n002]: **Note N-002** — Architecture bands classify technologies; Q-Divisions provide technical authority; ORB-Functions provide enterprise support. See [`organization/Q+ATLANTIDE.md` §4](../../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../../organization/Q+ATLANTIDE.md#4-notes).

[^n006]: **Note N-006 (Restricted bands)** — Defence-related (`200-299` DTTA), cybersecurity-related (`800-899` CYB) and quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls beyond the baseline trace record. Templates must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`. See [`organization/Q+ATLANTIDE.md` §5.3](../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).
