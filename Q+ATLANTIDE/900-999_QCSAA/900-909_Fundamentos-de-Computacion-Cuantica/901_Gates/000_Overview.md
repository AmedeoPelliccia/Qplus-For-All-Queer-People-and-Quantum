---
document_id: QATL-ATLAS1000-QCSAA-900-909-00-901-000-OVERVIEW
title: "QCSAA 900-909 · 00.901.000 — Gates"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: QCSAA
architecture_name: "Quantum Computing & Sentient Agency Architecture"
master_range: "900–999"
code_range: "900-909"
section: "00"
section_title: "Fundamentos de Computación Cuántica"
subsection: "901"
subsection_title: "Gates"
subsubject: "000"
subsubject_title: "Overview"
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

Overview entry-point for the *Gates* subsection within the `900-909` code range (Section `00` — *Fundamentos de Computación Cuántica*) of the **QCSAA** architecture band (*Quantum Computing & Sentient Agency Architecture*, master range `900–999`).

This subsubject (`000 Overview`) introduces the QCSAA 900-909.901.000 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable standards listed in §4. It establishes the formal framework — unitary formalism, single-qubit and multi-qubit gates, universal gate sets, and physical implementation — that governs all quantum-gate theory and engineering within the Q+ATLANTIDE programme.

**Restricted band (N-006[^n006]).** This document inherits `governance_class: restricted` from the parent QCSAA section.

## 2. Scope

- Covers the *Gates* slice of the parent code range `900-909`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`001`–`005`) under this subsection extend this Overview with detailed data modules; the populated set in this baseline is `001`–`005`, indexed in [`README.md`](./README.md).
- Concepts in scope across the subsection:
  - **Gate Definition and Unitary Formalism** (`001`) — mathematical foundation: unitary operators, matrix representations, Dirac notation, and the operator algebra that defines quantum gates[^nielsen_chuang].
  - **Single-Qubit Gates** (`002`) — Pauli gates (X, Y, Z), Hadamard (H), phase gates (S, T), and arbitrary single-qubit rotations; their matrix forms and Bloch-sphere action[^nielsen_chuang].
  - **Multi-Qubit Gates and Entangling Operations** (`003`) — controlled gates (CNOT, CZ, controlled-U), SWAP variants, and the Toffoli gate; entanglement generation and Bell-state preparation[^nielsen_chuang].
  - **Universal Gate Sets and Decomposition** (`004`) — universality theorems, the Clifford+T set, Solovay-Kitaev decomposition, and compilation to native hardware gate sets[^openqasm3].
  - **Gate Implementation, Calibration and Error Characterization** (`005`) — physical realizations across qubit modalities, pulse-level calibration, gate fidelity metrics, randomized benchmarking, and process tomography[^ieee_p7131].

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subsection | `901` — Gates |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/901_Gates/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **QCSAA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `900-909` row (Section `00` — Fundamentos de Computación Cuántica, Primary Q-Division Q-HORIZON).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `restricted` denotes documents requiring additional governance, evidence packages and access controls (rule N-006).

[^n006]: **Note N-006 (Restricted bands)** — Quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls. See [`organization/Q+ATLANTIDE.md` §5.3](../../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).

[^nielsen_chuang]: **Nielsen, M. A. & Chuang, I. L. — *Quantum Computation and Quantum Information* (10th anniversary ed., Cambridge University Press, 2010)** — Standard reference for quantum gate formalism, unitary operators, and circuit model. ISBN 978-1-107-00217-3.

[^openqasm3]: **Cross, A. W. et al. — *OpenQASM 3: A Broader and Deeper Quantum Assembly Language* (ACM TQCA 2022)** — Open specification for quantum assembly and gate-level circuit description. [arXiv:2104.14722](https://arxiv.org/abs/2104.14722).

[^ieee_p7131]: **IEEE P7131 — Standard for Quantum Computing Performance Metrics and Benchmarking** — Defines gate fidelity, process tomography protocols, and performance metrics for quantum hardware evaluation.

[^iso4879]: **ISO/IEC 4879:2023 — Information technology — Quantum computing — Vocabulary** — International standard vocabulary for quantum computing terms including gate, qubit, unitary, and entanglement.

### Applicable standards

The following standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- Nielsen & Chuang — *Quantum Computation and Quantum Information* (Cambridge, 2010)[^nielsen_chuang]
- OpenQASM 3.0 — Open Quantum Assembly Language specification[^openqasm3]
- IEEE P7131 — Quantum Computing Performance Metrics and Benchmarking[^ieee_p7131]
- ISO/IEC 4879:2023 — Quantum computing — Vocabulary[^iso4879]
