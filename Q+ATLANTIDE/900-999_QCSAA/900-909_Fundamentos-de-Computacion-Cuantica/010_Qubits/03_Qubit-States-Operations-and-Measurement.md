---
document_id: QATL-ATLAS-1000-QCSAA-900-909-00-010-03-QUBIT-STATES-OPERATIONS-AND-MEASUREMENT
title: "QCSAA 900-909 · 00.010.03 — Qubit States, Operations and Measurement"
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
subject: "00"
subject_title: "General Information"
subsection: "010"
subsection_title: "Qubits"
subsubject: "03"
subsubject_title: "Qubit States, Operations and Measurement"
primary_q_division: Q-HORIZON
support_q_divisions: [Q-HPC, Q-DATAGOV]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: restricted
version: 1.0.0
status: active
language: en
---
# QCSAA 900-909 · Section 00 · Subsection 010 · Subsubject 03 — Qubit States, Operations and Measurement

## 1. Purpose

Defines the **operational layer** on top of the qubit formalism established in `01_`: state preparation, the canonical single- and two-qubit gates, the entangled states they produce (Bell states), and the measurement model. The objects defined here — gates and measurements — are the primitives consumed by `020_gates/`, `030_circuits/` and `040_quantum-algorithms/` downstream.

## 2. Scope

- Covers the *Qubit States, Operations and Measurement* subsubject (`03`) of subsection `010` *Qubits* within section `00` *Fundamentos de Computación Cuántica*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **State preparation** — initialisation into a known reference state (commonly $|0\rangle$); reset protocols (passive thermal, active feedback).
  - **Single-qubit gates** — Pauli operators $X$, $Y$, $Z$; Hadamard $H$; phase gates $S$, $T$; arbitrary rotations $R_x(\theta)$, $R_y(\theta)$, $R_z(\theta)$.
  - **Two-qubit gates** — controlled-NOT (CNOT), controlled-Z (CZ), iSWAP; equivalence classes under local unitaries.
  - **Entanglement** — the four Bell states $|\Phi^\pm\rangle$, $|\Psi^\pm\rangle$ as the canonical maximally entangled basis on two qubits; entanglement as a non-classical resource for downstream algorithms.
  - **Measurement** — projective measurement in the computational basis ($Z$-basis); rotation of basis to enable $X$- and $Y$-basis measurement; **weak / generalised (POVM) measurement** as a generalisation that returns less-than-full collapse and is foundational for feedback-driven protocols and quantum sensing.
- Out of scope: implementation-level pulse shaping (`02_`), gate-error characterisation (`04_`), error-correcting code construction (`05_`).

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subject | `00` — General Information |
| Subsection | `010` — Qubits |
| Subsubject | `03` — Qubit States, Operations and Measurement |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/010_Qubits/` |
| Document | `03_Qubit-States-Operations-and-Measurement.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`00_Overview.md`](./00_Overview.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **QCSAA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `900-909` row (Section `00` — Fundamentos de Computación Cuántica, Primary Q-Division Q-HORIZON).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — Bands are classified as `baseline` or `restricted` per Q+ATLANTIDE §4 governance rules.

[^ieeep7130]: **IEEE P7130 — Standard for Quantum Computing Definitions** — Vocabulary baseline for the quantum computing scope of QCSAA `900-999`.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used for all Q+ATLANTIDE artefacts.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

### Applicable industry standards

The following standards apply to this subsubject in addition to the cross-cutting Q+ATLANTIDE governance:

- IEEE P7130 — Standard for Quantum Computing Definitions[^ieeep7130]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
