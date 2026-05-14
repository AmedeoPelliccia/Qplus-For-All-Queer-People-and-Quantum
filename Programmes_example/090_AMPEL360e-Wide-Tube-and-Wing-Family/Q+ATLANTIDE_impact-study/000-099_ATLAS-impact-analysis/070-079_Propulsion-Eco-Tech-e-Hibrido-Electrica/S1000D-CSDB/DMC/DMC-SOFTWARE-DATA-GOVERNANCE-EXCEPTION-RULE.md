---
document_id: DMC-SOFTWARE-DATA-GOVERNANCE-EXCEPTION-RULE
title: "Software Data Governance Exception Rule — AMPEL360E eWTW 070-079"
programme: "AMPEL360e Wide Tube-and-Wing Family (eWTW)"
atlas_group: "070-079"
status: "programme-controlled / normative"
standard: "S1000D Issue 4.2; DO-178C; DO-254; ARP4754A"
owner: "Amedeo Pelliccia / Q+"
created: 2026-05-14
applies_to: "Computer system DMs (IC C00, C10, C20) in S1000D-CSDB/DMC/"
---

# Software Data Governance Exception Rule

## 1. Purpose

S1000D `<comrep>` data modules (info codes C00, C10, C20) for the AMPEL360E eWTW describe  
embedded software and firmware. These DMs are subject to both S1000D editorial governance  
and DO-178C / DO-254 software lifecycle governance.

This rule defines the exceptions and additional approval gates that apply.

## 2. Classification of Software DMs

| IC | Content | DO-178C Assurance Level | Additional Gate |
| -- | ------- | ----------------------- | --------------- |
| C00 | Computer System Description | DAL per system host | SE + SW review |
| C10 | Software / Firmware Description | DAL per system host | SE + SW + SQA review |
| C20 | Computer System Fault Isolation | DAL per system host | SE + Safety review |

### DAL Assignments for 070-079 Systems

| System | Software DAL |
| ------ | ------------ |
| Hybrid Propulsion Control Unit (HPCU) | DAL B |
| Battery Management System (BMS) | DAL B |
| Fuel Cell Control Unit (FCCU) | DAL B |
| Thermal Management Controller (TMC) | DAL B |
| Energy Management Control Unit (EMCU) | DAL B |
| AI Propulsion Optimisation Core (AIOCU) | DAL B |
| Hydrogen Safety Control & Monitoring Unit (HSCMU) | DAL B |
| Quantum Sensing Processing Unit (QSPU) | DAL B |

## 3. Exception Conditions

The following exceptions to standard S1000D DM processing apply to software DMs:

### Exception SW-001 — Source Code References
Software DMs (IC C10) may include references to version-controlled source code repositories  
using `<externalPubRef>`. These references are **not** subject to CSDB DM traceability rules  
but must cite an approved software configuration item (CI) identifier.

### Exception SW-002 — Classification Marking
Software DMs covering DAL A or B systems must carry a `<security>` classification annotation  
indicating the applicable export control regime (e.g., EAR99 / ECCN 7E994).

### Exception SW-003 — Quantum Algorithm Content
DMs describing quantum-optimised algorithms (e.g., QAOA, VQE, QML) integrated into the  
propulsion control chain are classified as **dual-use research content** and require additional  
review by the Q+ Quantum Technology Board before CCB controlled release.

## 4. Approval Gate for Software DMs

- [ ] DO-178C / DO-254 Software Quality Assurance (SQA) review
- [ ] Software Configuration Management (SCM) registration
- [ ] BREX validation (`s1kd-brexcheck`, IC C00/C10/C20)
- [ ] CCB approval with DAL justification record
- [ ] DMRL status update to `"approved"` with SW CI identifier

## 5. Prohibited Content

The following content is **prohibited** in S1000D software DMs:

- Source code listings (use external repository reference instead)
- Cryptographic key material
- Red-team / penetration-test findings
- Unredacted vulnerability disclosure details
