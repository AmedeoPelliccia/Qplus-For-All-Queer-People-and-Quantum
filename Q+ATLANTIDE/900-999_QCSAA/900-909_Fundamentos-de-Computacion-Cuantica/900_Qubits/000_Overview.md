---
document_id: QATL-ATLAS-1000-QCSAA-900-909-00-900-000-OVERVIEW
title: "QCSAA 900–909 · 00.900.000 — Qubits"
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
subsection: "900"
subsection_title: "Qubits"
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
# QCSAA 900–909 · Section 00 · Subsection 900 — Qubits

## 1. Purpose

Overview entry-point for the *Qubits* subsection within the `900-909` code range (Section `00` — *Fundamentos de Computación Cuántica*) of the **QCSAA** architecture band (*Quantum Computing & Sentient Agency Architecture*, master range `900–999`).

This subsubject (`000 Overview`) introduces the QCSAA 900-909.900.000 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable standards listed in §4. It establishes the controlled qubit vocabulary — mathematical state-space formalism, physical platform taxonomy, coherence and fidelity bounds, and logical-qubit encoding — that every subsequent QCSAA subsection depends on.

**Restricted band (N-006[^n006]).** This document inherits `governance_class: restricted` and must be accompanied by a declared `evidence_package_id` and `access_control_profile`.

## 2. Scope

- Covers the *Qubits* slice of the parent code range `900-909`.
- Inherits Q-Division authority and ORB support from the parent row in [`../README.md`](../README.md)[^archtable].
- Subsequent subsubjects (`001`–`005`) under this subsection extend this Overview with detailed data modules; the populated set in this baseline is `001`–`005`, indexed in [`README.md`](./README.md).
- Concepts in scope across the subsection:
  - **Qubit Definition and Mathematical Formalism** (`001`) — Hilbert-space state vectors, the Bloch sphere representation, superposition, and the Dirac (bra-ket) notation as defined in Nielsen & Chuang[^nielchung].
  - **Physical Qubit Implementations** (`002`) — superconducting transmon, trapped-ion, photonic, spin, and neutral-atom platforms, benchmarked against the DiVincenzo criteria[^divincenzo].
  - **Qubit States, Operations and Measurement** (`003`) — single-qubit and multi-qubit state evolution, unitary gate action, projective and POVM measurement, and the Born rule.
  - **Decoherence, Noise and Fidelity** (`004`) — T₁ (relaxation), T₂ (dephasing), gate fidelity, process tomography, and noise channels (bit-flip, phase-flip, depolarising, amplitude-damping).
  - **Logical Qubits, Encoding and Error Correction** (`005`) — stabiliser codes, the surface code, code distance, fault-tolerant thresholds, and the overhead relationship between physical and logical qubits per ISO/IEC 4879[^isoiec4879].

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subsection | `900` — Qubits |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/900_Qubits/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Subsubject Index (parent README)** — [`README.md` §3](./README.md#3-subsubject-index). Authoritative source for the `900` row (Subsection `900` — Qubits, Primary Q-Division Q-HORIZON).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `restricted` denotes documents requiring additional governance, evidence packages and access controls (rule N-006[^n006]).

[^n006]: **Note N-006 (Restricted bands)** — Quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls. Templates must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`. See [`organization/Q+ATLANTIDE.md` §5.3](../../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).

[^nielchung]: **Nielsen, M. A. & Chuang, I. L. (2010)** — *Quantum Computation and Quantum Information* (10th Anniversary Edition). Cambridge University Press. Canonical reference for qubit formalism, state spaces, gates, measurement, and error correction.

[^divincenzo]: **DiVincenzo, D. P. (2000)** — "The Physical Implementation of Quantum Computation." *Fortschritte der Physik*, 48(9–11), 771–783. Five criteria for a viable physical qubit platform.

[^isoiec4879]: **ISO/IEC 4879:2023** — *Quantum computing — Vocabulary*. International standard defining terms and concepts including qubit, quantum state, measurement, entanglement, and logical qubit.

### Applicable standards

The following standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- Nielsen & Chuang (2010) — *Quantum Computation and Quantum Information*[^nielchung]
- DiVincenzo (2000) — "The Physical Implementation of Quantum Computation"[^divincenzo]
- ISO/IEC 4879:2023 — *Quantum computing — Vocabulary*[^isoiec4879]
