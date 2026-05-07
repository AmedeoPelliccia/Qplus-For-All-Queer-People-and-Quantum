---
document_id: QATL-ATLAS1000-QCSAA-900-909-00-904-README
title: "QCSAA 900-909 · 00.904 — Quantum Information Theory (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: QCSAA
architecture_name: "Quantum Computing & Sentient Agency Architecture"
master_range: "900–999"
code_range: "900-909"
section: "00"
section_title: "Fundamentos de Computación Cuántica"
subsection: "904"
subsection_title: "Quantum Information Theory"
primary_q_division: Q-HORIZON
support_q_divisions: [Q-HPC, Q-DATAGOV]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: restricted
restricted_rule: N-006
version: 1.0.0
status: active
language: en
---

# QCSAA 900-909 · Section 00 · Subsection 904 — Quantum Information Theory

## 1. Purpose

Subsection-level index for *Quantum Information Theory* (`904`) within QCSAA `900-909` — *Fundamentos de Computación Cuántica* — covering the mathematical and information-theoretic foundations of quantum computing and quantum communication.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It establishes the theoretical bedrock upon which all higher-level QCSAA artefacts depend: quantum states, entropy measures, quantum channels, entanglement, coding, capacity limits, and fundamental no-go theorems.

## 2. Scope

- Reserves the subsubject namespace `000`–`007` of subsection `904` *Quantum Information Theory*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- The Overview and detailed subsubjects (`000`–`007`) are indexed in §3 below per the parent section's authorisation.
- Governance class `restricted` applies to all artefacts in this subsection per Note N-006[^n006][^gov].

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 001 | Quantum States, Density Operators and Mixed States | [`001_Quantum-States-Density-Operators-and-Mixed-States.md`](./001_Quantum-States-Density-Operators-and-Mixed-States.md) | active |
| 002 | Quantum Entropy and Information Measures | [`002_Quantum-Entropy-and-Information-Measures.md`](./002_Quantum-Entropy-and-Information-Measures.md) | active |
| 003 | Quantum Channels and Operations | [`003_Quantum-Channels-and-Operations.md`](./003_Quantum-Channels-and-Operations.md) | active |
| 004 | Entanglement Theory and Measures | [`004_Entanglement-Theory-and-Measures.md`](./004_Entanglement-Theory-and-Measures.md) | active |
| 005 | Quantum Coding and Compression | [`005_Quantum-Coding-and-Compression.md`](./005_Quantum-Coding-and-Compression.md) | active |
| 006 | Quantum Channel Capacity and Communication Limits | [`006_Quantum-Channel-Capacity-and-Communication-Limits.md`](./006_Quantum-Channel-Capacity-and-Communication-Limits.md) | active |
| 007 | No-Go Theorems and Information-Theoretic Boundaries | [`007_No-Go-Theorems-and-Information-Theoretic-Boundaries.md`](./007_No-Go-Theorems-and-Information-Theoretic-Boundaries.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture (controlled term) |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subsection | `904` — Quantum Information Theory |
| Subsubject namespace | `000`–`007` (8 subsubjects: 000–007 active) |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/904_Quantum-Information-Theory/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = QCSAA`, `primary_q_division = Q-HORIZON` and `governance_class = restricted` from the parent QCSAA section. Restricted-band rules (N-006[^n006]) require additional governance, evidence packages and access controls for all artefacts in the `900-999` band. Extensions added under `000`–`007` shall preserve those header fields and reuse the footnote set declared here. The "AAA" domain is not valid within this baseline[^n004].

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `900-909` row.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `restricted` denotes documents requiring additional governance, evidence packages and access controls (rule N-006[^n006]).

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n002]: **Note N-002** — Architecture bands classify technologies; Q-Divisions provide technical authority; ORB-Functions provide enterprise support. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n006]: **Note N-006 (Restricted bands)** — Quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls. See [`organization/Q+ATLANTIDE.md` §5.3](../../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).
