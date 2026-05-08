---
document_id: QATL-ATLAS1000-CYB-README
title: "800–899 CYB — Cybersecurity Architecture"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../organization/Q+ATLANTIDE.md
architecture_code: CYB
architecture_name: "Cybersecurity Architecture"
master_range: "800–899"
subrange_count: 10
governance_class: restricted
restricted_rule: N-006
evidence_package_id: PENDING
access_control_profile: QATL-ACP-CYB-RESTRICTED
primary_q_divisions: [Q-DATAGOV, Q-HPC]
orb_function_support: [ORB-LEG, ORB-PMO, ORB-FIN, ORB-HR]
version: 1.0.0
status: active
language: en
---

# 800–899 CYB — Cybersecurity Architecture

## 1. Purpose

Cybersecurity architecture band covering governance and risk management, network and communications security, data and storage security, identity and access management, application and software security, operational cybersecurity, cloud and edge security, ICS-OT cybersecurity, post-quantum cryptography and quantum security, and threat intelligence and cyber resilience.

This folder is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. Bands classify technologies, Q-Divisions provide technical authority, and ORB-Functions provide enterprise support[^n002].

## 2. Glossary of Terms & Acronyms

| Term / Acronym | Expansion | Meaning in this band |
|---|---|---|
| CYB | Cybersecurity Architecture | Cybersecurity architecture band `800-899` (restricted). |
| IAM | Identity and Access Management | Identity lifecycle, authentication, authorisation and access governance. |
| MFA | Multi-Factor Authentication | Authentication requiring two or more verification factors. |
| PAM | Privileged Access Management | Controls for elevated/privileged account lifecycle and usage. |
| SOC | Security Operations Center | Centralised function for monitoring, detection and incident response. |
| SIEM | Security Information and Event Management | Platform aggregating security telemetry for correlation and alerting. |
| SOAR | Security Orchestration, Automation and Response | Workflow automation and orchestration for security operations. |
| RBAC | Role-Based Access Control | Access control model based on roles assigned to subjects. |
| ABAC | Attribute-Based Access Control | Access control model based on attributes of subjects, objects and environment. |
| CSPM | Cloud Security Posture Management | Continuous assessment of cloud configuration against security baselines. |
| CWPP | Cloud Workload Protection Platform | Runtime protection for cloud workloads and containers. |
| ICS | Industrial Control System | Systems controlling industrial processes (SCADA, DCS, PLC). |
| OT | Operational Technology | Hardware and software operating physical systems and processes. |
| SCADA | Supervisory Control and Data Acquisition | Distributed monitoring and control system for industrial processes. |
| PLC | Programmable Logic Controller | Industrial digital computer for automation of electromechanical processes. |
| DCS | Distributed Control System | Control system for large industrial processes using distributed controllers. |
| PQC | Post-Quantum Cryptography | Cryptographic algorithms resistant to quantum-computer attacks. |
| QKD | Quantum Key Distribution | Quantum-physics-based secure key exchange protocol. |
| SBOM | Software Bill of Materials | Formal record of software components and their dependencies. |
| DLP | Data Loss Prevention | Controls preventing unauthorised exfiltration of sensitive data. |
| GDPR | General Data Protection Regulation | EU data protection and privacy regulation. |
| DPIA | Data Protection Impact Assessment | Risk assessment required under GDPR for high-risk processing. |
| TLS | Transport Layer Security | Cryptographic protocol for secure communications over networks. |
| VPN | Virtual Private Network | Encrypted tunnel for secure network communications. |
| SSO | Single Sign-On | Authentication scheme allowing one credential for multiple systems. |
| PKI | Public Key Infrastructure | Framework for managing digital certificates and public-key encryption. |
| IOC | Indicator of Compromise | Forensic artefact indicating a potential security breach. |
| TTP | Tactics, Techniques and Procedures | Behaviour patterns of threat actors used for threat intelligence. |
| Q+ATLANTIDE | Controlled baseline for the `000-999` architecture-band taxonomy. | Parent baseline of this register. |
| ATLAS-1000 | Umbrella register of the 10 architectures inside Q+ATLANTIDE. | Subpart of Q+ATLANTIDE; not a numeric band. |
| Q-Division | Technical authority unit (e.g. Q-DATAGOV, Q-HPC). | Owns architecture decisions inside a band (rule N-002). |
| ORB | Organizational Resource Backbone — enterprise support functions. | Provides enterprise-side support to bands (rule N-002). |
| CSDB | Common Source DataBase | S1000D technical-publication data environment. |
| LC | Lifecycle phase / acceptance gate | Used across SSOT/LC01–LC14. |

Cross-reference the full Q+ATLANTIDE acronym set at [`organization/Q+ATLANTIDE.md` §2](../../organization/Q+ATLANTIDE.md#2-acronyms)[^glossary].

## 3. Architecture Table

Sub-ranges within this band, sourced from the Q+ATLANTIDE controlled baseline[^baseline] §3 *Consolidated Architecture Table*[^table].

| Code range | Section | Section title | Subject | Subject title | Primary focus | Primary Q-Division | Support Q-Divisions | ORB support |
|---:|---:|---|---:|---|---|---|---|---|
| 800–809 | 00 | Gobernanza y Gestión de Riesgos de Ciberseguridad | 00 | General Information | Governance framework, risk management, policies, compliance, supply chain risk, audit | Q-DATAGOV | Q-HPC, Q-HORIZON | ORB-LEG, ORB-PMO |
| 810–819 | 01 | Seguridad de Redes y Comunicaciones | 00 | General Information | Network architecture, segmentation, zero trust, VPN/TLS, wireless, SATCOM, monitoring, firewalls, DDoS | Q-DATAGOV | Q-HPC, Q-HORIZON | ORB-PMO, ORB-LEG |
| 820–829 | 02 | Seguridad de Datos y Almacenamiento | 00 | General Information | Data classification, encryption at rest, DLP, backup, database security, data lineage, privacy/GDPR | Q-DATAGOV | Q-HPC, Q-HORIZON | ORB-LEG, ORB-PMO |
| 830–839 | 03 | Gestión de Identidades y Acceso | 00 | General Information | IAM, identity lifecycle, MFA, RBAC/ABAC, PAM, federation/SSO, machine identity, access review | Q-DATAGOV | Q-HPC, Q-HORIZON | ORB-PMO, ORB-LEG |
| 840–849 | 04 | Seguridad de Aplicaciones y Software | 00 | General Information | Secure SDLC, threat modeling, SAST/DAST, API security, SBOM, secrets management, vulnerability governance | Q-DATAGOV | Q-HPC, Q-HORIZON | ORB-PMO, ORB-LEG |
| 850–859 | 05 | Ciberseguridad Operacional | 00 | General Information | SOC, SIEM/SOAR, incident response, detection engineering, forensics, playbooks, BCM, cyber resilience | Q-DATAGOV | Q-HPC, Q-HORIZON | ORB-PMO, ORB-LEG |
| 860–869 | 06 | Seguridad Cloud y Edge | 00 | General Information | CSPM, CWPP, containers/Kubernetes, serverless, edge security, cloud IAM, multi-cloud, sovereignty | Q-DATAGOV | Q-HPC, Q-HORIZON | ORB-PMO, ORB-LEG |
| 870–879 | 07 | Ciberseguridad ICS-OT | 00 | General Information | ICS/OT asset inventory, SCADA/PLC/DCS security, OT segmentation, OT monitoring, patch, SIS | Q-DATAGOV | Q-HPC, Q-INDUSTRY | ORB-PMO, ORB-LEG |
| 880–889 | 08 | Criptografía Post-Cuántica y Seguridad Cuántica | 00 | General Information | PQC algorithms, crypto inventory, quantum risk, key management/PKI, crypto agility, QKD boundaries | Q-DATAGOV | Q-HPC, Q-HORIZON | ORB-LEG, ORB-PMO |
| 890–899 | 09 | Inteligencia de Amenazas y Ciber-resiliencia | 00 | General Information | Threat intelligence lifecycle, IOC/TTP, attack surface, risk prioritization, red/blue/purple, exercises | Q-DATAGOV | Q-HPC, Q-HORIZON | ORB-PMO, ORB-LEG |

## 4. Footprint

| Metric | Value |
|---|---|
| Master range | `800–899` |
| Sub-ranges | 10 |
| Architecture code | `CYB` |
| Governance class | `restricted` |
| Restricted band | Yes (rule N-006[^n006]) |
| Primary Q-Divisions | Q-DATAGOV, Q-HPC |
| Folder path | `Q+ATLANTIDE/800-899_CYB/` |
| Documents | `README.md` (this file) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md) |
| Register subpart | ATLAS-1000 |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md)[^baseline]. Templates declared in this band must populate `architecture_band`, `architecture_code = CYB`, `q_division_owner` and `orb_function_support` per the Templates System[^templates]. The No-AAA Rule[^n004] applies.

**Restricted band (N-006[^n006]).** Templates inside this band must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`.

**Non-offensive boundary.** CYB nodes define cybersecurity architecture, defensive controls, risk governance, assurance evidence, monitoring, resilience, privacy, compliance and cryptographic transition. The taxonomy shall not include exploit instructions, offensive procedures, credential theft, evasion methods, unauthorized access workflows, malware implementation, persistence logic or misuse-enabling operational detail.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^table]: **§3 — Consolidated Architecture Table** — [`organization/Q+ATLANTIDE.md` §3](../../organization/Q+ATLANTIDE.md#3-consolidated-architecture-table).

[^glossary]: **§2 — Acronyms** — [`organization/Q+ATLANTIDE.md` §2](../../organization/Q+ATLANTIDE.md#2-acronyms).

[^templates]: **§5 — Templates System** — [`organization/Q+ATLANTIDE.md` §5](../../organization/Q+ATLANTIDE.md#5-templates-system). Mandatory template header fields, naming rules and lifecycle integration.

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n002]: **Note N-002** — Architecture bands classify technologies; Q-Divisions provide technical authority; ORB-Functions provide enterprise support. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n003]: **Note N-003** — The `000-999` range is controlled; `ATLAS-1000` is the umbrella name, not an additional numeric band. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../organization/Q+ATLANTIDE.md#4-notes).

[^n006]: **Note N-006 (Restricted bands)** — Defence-related (`200-299` DTTA), cybersecurity-related (`800-899` CYB) and quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls beyond the baseline trace record. Templates must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`. See [`organization/Q+ATLANTIDE.md` §5.3](../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).

[^repo]: **Repository root README** — [`README.md`](../../README.md). Top-level entry point referencing the Q+ATLANTIDE baseline and the ATLAS-1000 register subpart.
