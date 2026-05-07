---
document_id: QATL-ATLAS1000-QCSAA-900-909-00-901-README
title: "QCSAA 900-909 · 00.901 — Gates (Subsection Index)"
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
subsection: "901"
subsection_title: "Gates"
primary_q_division: Q-HORIZON
support_q_divisions: [Q-HPC, Q-DATAGOV]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: restricted
restricted_rule: N-006
version: 1.0.0
status: active
language: en
---

# QCSAA 900-909 · Section 00 · Subsection 901 — Gates

## 1. Purpose

Subsection-level index for *Gates* (`901`) within QCSAA `900-909` — *Fundamentos de Computación Cuántica* — the formal theory and physical implementation of quantum logic gates.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. **Restricted band (N-006[^n006]).** All documents under this subsection inherit `governance_class: restricted`.

## 2. Scope

- Reserves the subsubject namespace `000`–`099` of subsection `901` *Gates*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable] and the section index in [`../README.md`](../README.md).
- The Overview and detailed subsubjects (`000`–`005`) are indexed in §3 below per the parent section's authorisation.
- All documents under this subsection must declare `governance_class: restricted`, `evidence_package_id`, and `access_control_profile` per rule N-006[^n006].

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 001 | Gate Definition and Unitary Formalism | [`001_Gate-Definition-and-Unitary-Formalism.md`](./001_Gate-Definition-and-Unitary-Formalism.md) | active |
| 002 | Single-Qubit Gates | [`002_Single-Qubit-Gates.md`](./002_Single-Qubit-Gates.md) | active |
| 003 | Multi-Qubit Gates and Entangling Operations | [`003_Multi-Qubit-Gates-and-Entangling-Operations.md`](./003_Multi-Qubit-Gates-and-Entangling-Operations.md) | active |
| 004 | Universal Gate Sets and Decomposition | [`004_Universal-Gate-Sets-and-Decomposition.md`](./004_Universal-Gate-Sets-and-Decomposition.md) | active |
| 005 | Gate Implementation, Calibration and Error Characterization | [`005_Gate-Implementation-Calibration-and-Error-Characterization.md`](./005_Gate-Implementation-Calibration-and-Error-Characterization.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subsection | `901` — Gates |
| Subsubject namespace | `000`–`005` (6 subsubjects: 000–005 active) |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/901_Gates/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = QCSAA`, `primary_q_division = Q-HORIZON`, and `governance_class = restricted` from the parent QCSAA section. Extensions added under `000`–`099` shall preserve those header fields, declare `evidence_package_id` and `access_control_profile` per N-006[^n006], and reuse the footnote set declared here. The No-AAA Rule[^n004] applies.

## 5. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table). Source of authority for primary/support Q-Divisions and ORB support of this subsection.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `restricted` denotes documents requiring additional governance, evidence packages and access controls (rule N-006[^n006]).

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n006]: **Note N-006 (Restricted bands)** — Quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls beyond the baseline trace record. Templates must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`. See [`organization/Q+ATLANTIDE.md` §5.3](../../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).
