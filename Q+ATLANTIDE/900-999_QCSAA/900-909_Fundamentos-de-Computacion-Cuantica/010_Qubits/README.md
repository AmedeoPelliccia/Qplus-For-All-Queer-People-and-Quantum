---
document_id: QATL-ATLAS-1000-QCSAA-900-909-00-010-README
title: "QCSAA 900-909 · 00.010 — Qubits (Subsection Index)"
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
primary_q_division: Q-HORIZON
support_q_divisions: [Q-HPC, Q-DATAGOV]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: restricted
version: 1.0.0
status: active
language: en
---
# QCSAA 900-909 · Section 00 · Subsection 010 — Qubits

## 1. Purpose

Subsection-level index for *Qubits* (`010`) within QCSAA `900-909` — *Fundamentos de Computación Cuántica*. Aggregates the `00 Overview` and the detailed subsubjects (`01`–`05`) that introduce the qubit as the atomic unit of quantum computation, define its mathematical formalism, catalogue physical implementations, describe operations and measurement, characterise decoherence and noise, and bridge to fault-tolerant logical-qubit encodings — under the controlled Q+ATLANTIDE baseline[^baseline] and the IEEE quantum-computing vocabulary[^ieeep7130].

This subsection is the **foundational chapter** of the QCSAA band: every other chapter in `900-999` (gates, circuits, algorithms, QML, sensing, robotics, sentient agency) presupposes the qubit model defined here. It is therefore *upstream* of the rest of the register, rather than a peer in a horizontal partition (the structural pattern used by the ATLAS bands).

## 2. Scope

- Covers the full subsubject namespace `00`–`99` of subsection `010` *Qubits*; subsubjects `01`–`05` are populated in this baseline release, the remaining `06`–`99` slots remain available for future extension per the Overview's authorisation[^archtable].
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Pedagogical sequence followed: **definition → implementation → operation → degradation → mitigation**, the canonical structure for a quantum-computing primer.
- Acts as the cross-band reference anchor for sensing (`940-949`) and post-quantum cryptography (`880-889`, in CYB), both of which depend on qubit-level concepts but exploit them in qualitatively different ways (susceptibility vs. computational assumptions) — see §6.

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 00 | Overview | [`00_Overview.md`](./00_Overview.md) | active |
| 01 | Qubit Definition and Mathematical Formalism | [`01_Qubit-Definition-and-Mathematical-Formalism.md`](./01_Qubit-Definition-and-Mathematical-Formalism.md) | active |
| 02 | Physical Qubit Implementations | [`02_Physical-Qubit-Implementations.md`](./02_Physical-Qubit-Implementations.md) | active |
| 03 | Qubit States, Operations and Measurement | [`03_Qubit-States-Operations-and-Measurement.md`](./03_Qubit-States-Operations-and-Measurement.md) | active |
| 04 | Decoherence, Noise and Fidelity | [`04_Decoherence-Noise-and-Fidelity.md`](./04_Decoherence-Noise-and-Fidelity.md) | active |
| 05 | Logical Qubits, Encoding and Error Correction | [`05_Logical-Qubits-Encoding-and-Error-Correction.md`](./05_Logical-Qubits-Encoding-and-Error-Correction.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subject | `00` — General Information |
| Subsection | `010` — Qubits |
| Subsubject namespace | `00`–`99` (`00` + `01`–`05` populated) |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/010_Qubits/` |
| Document | `README.md` (this file) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = QCSAA`, `primary_q_division = Q-HORIZON` and `governance_class = restricted` from the parent QCSAA band; extensions added under `06`–`99` shall preserve those header fields and reuse the footnote set declared below.

## 6. Downstream and Cross-Band Dependencies

The qubit model defined in this subsection is consumed by:

- **Within `900-909`** — `020_gates/`, `030_circuits/`, `040_quantum-algorithms/`, `050_foundations/` (acyclic dependency graph: qubits → gates → circuits → algorithms → foundations/applications).
- **Within QCSAA `900-999`** — `910-919` Quantum Machine Learning & Quantum AI, `920-929` Quantum Networks & Communications, `930-939` Quantum Cybersecurity, `940-949` Quantum Sensing & Metrology (back-references qubit *susceptibility*: the same decoherence that hurts computation aids measurement), `950-959` Quantum Simulation, `960-969` Quantum Robotics, `970-979` Sentient Quantum Agency.
- **Cross-band** — CYB `880-889` Post-Quantum Cryptography depends on the *computational* assumptions about what qubits can or cannot do (PQC defends against quantum computers; the cross-band reference into `010_Qubits/` is structural, not optional).

Downstream chapters shall back-reference the specific subsubjects of this subsection rather than re-introduce the underlying concepts.

## 7. Change Log

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0.0 | 2026-05-07 | Q-HORIZON | Initial baseline: `00_Overview.md` plus subsubjects `01`–`05`. Subsection index established. |

## 8. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **QCSAA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `900-909` row (Section `00` — Fundamentos de Computación Cuántica, Primary Q-Division Q-HORIZON).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — Bands are classified as `baseline` or `restricted` per Q+ATLANTIDE §4 governance rules.

[^ieeep7130]: **IEEE P7130 — Standard for Quantum Computing Definitions** — Vocabulary baseline for the quantum computing scope of QCSAA `900-999`.

[^nistir8413]: **NIST IR 8413 — Status Report on the Third Round of the NIST Post-Quantum Cryptography Standardization Process** — Post-quantum cryptography reference for QCSAA security-bridging items.

[^etsiqsc001]: **ETSI GR QSC 001 — Quantum-Safe Cryptography (QSC); Quantum-safe algorithmic framework** — ETSI quantum-safe cryptography framework applied across QCSAA.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used for all Q+ATLANTIDE artefacts.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

### Applicable industry standards

The following standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- IEEE P7130 — Standard for Quantum Computing Definitions[^ieeep7130]
- NIST IR 8413 — Post-Quantum Cryptography Standardization, Round 3 Status Report[^nistir8413]
- ETSI GR QSC 001 — Quantum-Safe Cryptography algorithmic framework[^etsiqsc001]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
