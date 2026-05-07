---
document_id: QATL-ATLAS-1000-QCSAA-900-909-00-900-README
title: "QCSAA 900–909 · 00.900 — Qubits (Subsection Index)"
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
subsection: "900"
subsection_title: "Qubits"
primary_q_division: Q-HORIZON
support_q_divisions: [Q-HPC, Q-DATAGOV]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: restricted
restricted_rule: N-006
version: 1.0.0
status: active
language: en
---

# QCSAA 900–909 · Section 00 · Subsection 900 — Qubits

## 1. Purpose

Subsection-level index for *Qubits* (`900`) within QCSAA `900-909` — *Fundamentos de Computación Cuántica*. Covers the qubit as the fundamental unit of quantum information: its mathematical formalism, physical implementations, state-space operations and measurement, decoherence and noise mechanisms, and the encoding of logical qubits for error correction.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is the foundational reference for all subsequent QCSAA subsections (gates, circuits, algorithms, information theory) that build on the qubit abstraction.

**Restricted band (N-006[^n006]).** All documents under this subsection additionally inherit `governance_class: restricted` and must declare `evidence_package_id` and `access_control_profile`.

## 2. Scope

- Covers the full subsubject namespace `000`–`009` of subsection `900` *Qubits*; subsubjects `001`–`005` are populated in this baseline release, slots `006`–`009` remain available for future extension.
- Inherits Q-Division authority and ORB support from the parent row in [`../README.md` §3](../README.md#3-subsection-index)[^archtable] and the section index in [`../../README.md`](../../README.md).
- Establishes the canonical qubit vocabulary — state vectors, Bloch sphere, physical platforms, decoherence, and logical encoding — used by every downstream QCSAA subsection that references qubit primitives.

## 3. Subsubject Index

| 00N | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 001 | Qubit Definition and Mathematical Formalism | [`001_Qubit-Definition-and-Mathematical-Formalism.md`](./001_Qubit-Definition-and-Mathematical-Formalism.md) | active |
| 002 | Physical Qubit Implementations | [`002_Physical-Qubit-Implementations.md`](./002_Physical-Qubit-Implementations.md) | active |
| 003 | Qubit States, Operations and Measurement | [`003_Qubit-States-Operations-and-Measurement.md`](./003_Qubit-States-Operations-and-Measurement.md) | active |
| 004 | Decoherence, Noise and Fidelity | [`004_Decoherence-Noise-and-Fidelity.md`](./004_Decoherence-Noise-and-Fidelity.md) | active |
| 005 | Logical Qubits, Encoding and Error Correction | [`005_Logical-Qubits-Encoding-and-Error-Correction.md`](./005_Logical-Qubits-Encoding-and-Error-Correction.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subsection | `900` — Qubits |
| Subsubject namespace | `000`–`009` (`000` + `001`–`005` populated; canonical `00N_*.md` scheme) |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/900_Qubits/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = QCSAA`, `primary_q_division = Q-HORIZON` and `governance_class = restricted` from the parent QCSAA section. Extensions added under slots `006`–`009` shall preserve those header fields, follow the canonical `00N_*.md` naming scheme, reuse the footnote set declared below, and additionally declare `evidence_package_id` and `access_control_profile` per rule N-006[^n006]. The No-AAA Rule[^n004] applies.

## 6. Downstream and Cross-Subsection Dependencies

The qubit vocabulary and fidelity metrics defined in this subsection are consumed by:

- **Within `900-909`** — `901_Gates/` (gate operations act on qubit state spaces), `902_Circuits/` (circuits are composed sequences of gates applied to qubit registers), `903_Quantum-Algorithms/` (algorithms specify qubit initialisation, gate sequences and measurement schedules), `904_Quantum-Information-Theory/` (entropy and channel capacity are defined over qubit density matrices), `905_Quantum-Complexity-and-Resource-Theory/` (resource counts expressed in qubit and gate units), `906_Hamiltonian-Methods-and-Adiabatic-Computation/` (adiabatic evolution of qubit Hamiltonians).
- **Across QCSAA `900–999`** — every subsequent QCSAA section that references a qubit register, coherence time, or error rate traces back to the definitions, fidelity bounds and physical-platform constraints established here.

## 7. Change Log

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0.0 | 2026-05-07 | Q-HORIZON | Initial baseline: `000_Overview.md` plus subsubjects `001`–`005`, using the sequential `00N_*.md` scheme under the `900_Qubits/` subsection. Subsection index established. |

## 8. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Subsection Index (parent section)** — [`../README.md` §3](../README.md#3-subsection-index). Authoritative source for the `900-909` row (Section `00` — Fundamentos de Computación Cuántica, Primary Q-Division Q-HORIZON).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `restricted` denotes documents requiring additional governance, evidence packages and access controls (rule N-006[^n006]).

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n002]: **Note N-002** — Architecture bands classify technologies; Q-Divisions provide technical authority; ORB-Functions provide enterprise support. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n006]: **Note N-006 (Restricted bands)** — Quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls beyond the baseline trace record. Templates must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`. See [`organization/Q+ATLANTIDE.md` §5.3](../../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).

[^nielchung]: **Nielsen, M. A. & Chuang, I. L. (2010)** — *Quantum Computation and Quantum Information* (10th Anniversary Edition). Cambridge University Press. The canonical graduate reference for qubit formalism, quantum gates, circuits, and error correction.

[^divincenzo]: **DiVincenzo, D. P. (2000)** — "The Physical Implementation of Quantum Computation." *Fortschritte der Physik*, 48(9–11), 771–783. Establishes the five DiVincenzo criteria for a viable qubit physical platform.

[^isoiec4879]: **ISO/IEC 4879:2023** — *Quantum computing — Vocabulary*. International standard defining terms and concepts used in quantum computing, including qubit, quantum state, measurement and entanglement.
