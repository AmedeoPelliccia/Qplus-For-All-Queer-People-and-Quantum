---
document_id: QATL-ATLAS1000-CYB-870-879-07-README
title: "CYB 870-879 · 07 — Ciberseguridad ICS-OT (Section Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../README.md
architecture_code: CYB
architecture_name: "Cybersecurity Architecture"
master_range: "800–899"
code_range: "870-879"
section: "07"
section_title: "Ciberseguridad ICS-OT"
section_title_en: "ICS-OT Cybersecurity"
primary_q_division: Q-DATAGOV
support_q_divisions: [Q-HPC, Q-INDUSTRY]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: restricted
restricted_rule: N-006
evidence_package_id: PENDING
access_control_profile: QATL-ACP-CYB-RESTRICTED
version: 1.0.0
status: active
language: en
---

# CYB 870-879 · Section 07 — Ciberseguridad ICS-OT

## 1. Purpose

Section-level index for *Ciberseguridad ICS-OT* (`870-879`) within the CYB band. ICS/OT asset inventory, SCADA/PLC/DCS security, OT segmentation, OT monitoring, patch management, remote access, safety-instrumented systems.

This section is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. Bands classify technologies, Q-Divisions provide technical authority and ORB-Functions provide enterprise support[^n002].

**Restricted band (N-006[^n006]).** Documents in this section must declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`.

**Non-offensive boundary.** This section provides cybersecurity architecture, defensive controls, risk governance and assurance evidence only. It does not contain exploit instructions, offensive procedures, credential theft methods, evasion techniques, malware implementation, persistence logic or misuse-enabling operational detail.

## 2. Scope

- Aggregates the subjects within the `870-879` code range listed in §3.
- Inherits Q-Division authority and ORB support from the parent row in [`../README.md` §3](../README.md#3-architecture-table)[^archtable].
- Each subject folder contains its own documents. Subject codes use absolute numbering (`870`–`879`).

## 3. Subject Index

| Code | Title | Folder | Status |
|---:|---|---|---|
| `870` | Arquitectura General de Ciberseguridad ICS OT | [`./870_Arquitectura-General-de-Ciberseguridad-ICS-OT/`](./870_Arquitectura-General-de-Ciberseguridad-ICS-OT/) | reserved |
| `871` | ICS OT Asset Inventory y Network Zoning | [`./871_ICS-OT-Asset-Inventory-y-Network-Zoning/`](./871_ICS-OT-Asset-Inventory-y-Network-Zoning/) | reserved |
| `872` | SCADA PLC DCS y Control System Security | [`./872_SCADA-PLC-DCS-y-Control-System-Security/`](./872_SCADA-PLC-DCS-y-Control-System-Security/) | reserved |
| `873` | OT Segmentation Conduits y Zones | [`./873_OT-Segmentation-Conduits-y-Zones/`](./873_OT-Segmentation-Conduits-y-Zones/) | reserved |
| `874` | OT Monitoring Anomaly Detection y Safety Telemetry | [`./874_OT-Monitoring-Anomaly-Detection-y-Safety-Telemetry/`](./874_OT-Monitoring-Anomaly-Detection-y-Safety-Telemetry/) | reserved |
| `875` | Patch Vulnerability y Change Management OT | [`./875_Patch-Vulnerability-y-Change-Management-OT/`](./875_Patch-Vulnerability-y-Change-Management-OT/) | reserved |
| `876` | Remote Access Vendor Access y Maintenance Control | [`./876_Remote-Access-Vendor-Access-y-Maintenance-Control/`](./876_Remote-Access-Vendor-Access-y-Maintenance-Control/) | reserved |
| `877` | Safety Instrumented Systems y Cyber Safety Interface | [`./877_Safety-Instrumented-Systems-y-Cyber-Safety-Interface/`](./877_Safety-Instrumented-Systems-y-Cyber-Safety-Interface/) | reserved |
| `878` | Evidencia Trazabilidad y Gobernanza ICS OT | [`./878_Evidencia-Trazabilidad-y-Gobernanza-ICS-OT/`](./878_Evidencia-Trazabilidad-y-Gobernanza-ICS-OT/) | reserved |
| `879` | Safety Critical Operational Boundaries y Stop Authority | [`./879_Safety-Critical-Operational-Boundaries-y-Stop-Authority/`](./879_Safety-Critical-Operational-Boundaries-y-Stop-Authority/) | reserved |

## 4. Interfaces Diagram

```mermaid
flowchart TB
    PARENT["CYB<br/>(`800–899` master range)"]:::parent
    SEC["Section 07 · 870-879<br/>Ciberseguridad ICS-OT"]:::sec
    PARENT --> SEC

    subgraph SUBS["Subjects"]
        direction LR
        SUB_870["870 — Arquitectura General de Ciberseguridad ICS OT"]:::sub
        SUB_871["871 — ICS OT Asset Inventory y Network Zoning"]:::sub
        SUB_872["872 — SCADA PLC DCS y Control System Security"]:::sub
        SUB_873["873 — OT Segmentation Conduits y Zones"]:::sub
        SUB_874["874 — OT Monitoring Anomaly Detection y Safety Telemetry"]:::sub
        SUB_875["875 — Patch Vulnerability y Change Management OT"]:::sub
        SUB_876["876 — Remote Access Vendor Access y Maintenance Control"]:::sub
        SUB_877["877 — Safety Instrumented Systems y Cyber Safety Interface"]:::sub
        SUB_878["878 — Evidencia Trazabilidad y Gobernanza ICS OT"]:::sub
        SUB_879["879 — Safety Critical Operational Boundaries y Stop Authority"]:::sub
    end
    SEC --> SUBS

    SUBS --> SUB_870
    SUBS --> SUB_871
    SUBS --> SUB_872
    SUBS --> SUB_873
    SUBS --> SUB_874
    SUBS --> SUB_875
    SUBS --> SUB_876
    SUBS --> SUB_877
    SUBS --> SUB_878
    SUBS --> SUB_879

    QPRIM["Q-DATAGOV<br/>(primary Q-Division)"]:::qdiv
    QSUPP["Q-HPC, Q-INDUSTRY<br/>(support Q-Divisions)"]:::qdiv
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

*Solid arrows show parent→section→subject ownership and primary Q-Division authority; dotted arrows show support Q-Divisions and ORB enterprise support.*

## 5. Footprint

| Metric | Value |
|---|---|
| Architecture | `CYB` — Cybersecurity Architecture |
| Master range | `800–899` |
| Code range | `870-879` |
| Section | `07` — Ciberseguridad ICS-OT |
| Subjects | 10 reserved |
| Primary Q-Division | Q-DATAGOV[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-INDUSTRY |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/800-899_CYB/870-879_Ciberseguridad-ICS-OT/` |
| Document | `README.md` (this file) |
| Parent architecture | [`../README.md`](../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../organization/Q+ATLANTIDE.md)[^baseline]. All subjects under this section inherit `architecture_code = CYB`, `primary_q_division = Q-DATAGOV`, `governance_class = restricted`, and must additionally declare `evidence_package_id` and `access_control_profile` per N-006[^n006]. The No-AAA Rule[^n004] applies.

## 6. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../organization/Q+ATLANTIDE.md).

[^archtable]: **§3 — Architecture Table (parent)** — [`../README.md` §3](../README.md#3-architecture-table).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../organization/Q-Divisions/).

[^gov]: **Governance class** — `restricted` per N-006 for CYB band documents.

[^templates]: **§5 — Templates System** — [`organization/Q+ATLANTIDE.md` §5](../../../organization/Q+ATLANTIDE.md#5-templates-system).

[^n001]: **Note N-001** — Q+ATLANTIDE is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../organization/Q+ATLANTIDE.md#4-notes).

[^n002]: **Note N-002** — Architecture bands classify technologies; Q-Divisions provide technical authority; ORB-Functions provide enterprise support. See [`organization/Q+ATLANTIDE.md` §4](../../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../../organization/Q+ATLANTIDE.md#4-notes).

[^n006]: **Note N-006 (Restricted bands)** — Defence-related (`200-299` DTTA), cybersecurity-related (`800-899` CYB) and quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls beyond the baseline trace record. Templates must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`. See [`organization/Q+ATLANTIDE.md` §5.3](../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).
