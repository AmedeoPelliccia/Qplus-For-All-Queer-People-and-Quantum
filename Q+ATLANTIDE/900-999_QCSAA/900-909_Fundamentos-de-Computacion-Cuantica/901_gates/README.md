---
document_id: QATL-ATLAS-1000-QCSAA-900-909-00-901-README
title: "QCSAA 900-909 · 00.901 — gates (Subsection Index)"
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
subsection: "901"
subsection_title: "gates"
primary_q_division: Q-HORIZON
support_q_divisions: [Q-HPC, Q-DATAGOV]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: restricted
version: 1.0.0
status: active
language: en
---
# QCSAA 900-909 · Section 00 · Subsection 901 — gates

## 1. Purpose

Subsection-level index for *gates* (`901`) within QCSAA `900-909` — *Fundamentos de Computación Cuántica*. Aggregates the `00 Overview` and the detailed subsubjects (`001`–`005`) that introduce the **quantum gate** as a unitary operator on the qubit Hilbert space, catalogue single- and multi-qubit gate families, formalise universality and decomposition, and document per-modality physical implementation, calibration, and error characterisation — under the controlled Q+ATLANTIDE baseline[^baseline] and the IEEE quantum-computing vocabulary[^ieeep7130].

This subsection is the **second foundational chapter** of the QCSAA band and the **direct downstream consumer** of [`../900_Qubits/`](../900_Qubits/): where qubits define the substrate, gates define the operations on that substrate. It is the **immediate prerequisite** for [`../902_circuits/`](../902_circuits/), which composes gates into algorithms.

The chapter is organised in the same five-file structure as [`../900_Qubits/`](../900_Qubits/) — **definition → categories → composition → universality → physical realization** — deliberately. The parallelism is not aesthetic; it is pedagogical: once readers have learned the slot semantics of one foundational chapter, every subsequent foundational chapter in `900-909` is faster to navigate.

## 2. Scope

- Covers the full subsubject namespace `000`–`099` of subsection `901` *gates*; subsubjects `001`–`005` are populated in this baseline release, the remaining `006`–`099` slots remain available for future extension per the Overview's authorisation[^archtable].
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Pedagogical sequence followed: **definition → categories → composition → universality → physical realization**, mirroring [`../900_Qubits/`](../900_Qubits/).
- **Boundary against [`../902_circuits/`](../902_circuits/)** (binding for contributors). This chapter covers the **unitary operation as such** — its mathematical definition, its decomposition into a universal set, its physical realization on a given modality, its fidelity. The next chapter covers what happens **when gates are composed into algorithms** — depth, parallelisation, measurement timing, mid-circuit measurement, classical control flow. The rule is restated in `000_Overview.md` §2 and re-binding-ly in `004_` §3.

## 3. Subsubject Index

| NN | Title | Document | Status |
|---:|---|---|---|
| 00 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 01 | Gate Definition and Unitary Formalism | [`001_Gate-Definition-and-Unitary-Formalism.md`](./001_Gate-Definition-and-Unitary-Formalism.md) | active |
| 02 | Single-Qubit Gates | [`002_Single-Qubit-Gates.md`](./002_Single-Qubit-Gates.md) | active |
| 03 | Multi-Qubit Gates and Entangling Operations | [`003_Multi-Qubit-Gates-and-Entangling-Operations.md`](./003_Multi-Qubit-Gates-and-Entangling-Operations.md) | active |
| 04 | Universal Gate Sets and Decomposition | [`004_Universal-Gate-Sets-and-Decomposition.md`](./004_Universal-Gate-Sets-and-Decomposition.md) | active |
| 05 | Gate Implementation, Calibration and Error Characterization | [`005_Gate-Implementation-Calibration-and-Error-Characterization.md`](./005_Gate-Implementation-Calibration-and-Error-Characterization.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subject | `00` — General Information |
| Subsection | `901` — gates |
| Subsubject namespace | `000`–`099` (`000` + `001`–`005` populated) |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/901_gates/` |
| Document | `README.md` (this file) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = QCSAA`, `primary_q_division = Q-HORIZON` and `governance_class = restricted` from the parent QCSAA band; extensions added under `006`–`099` shall preserve those header fields and reuse the footnote set declared below.

## 6. Upstream, Downstream and Cross-Band Dependencies

- **Upstream (within `900-909`)** — [`../900_Qubits/`](../900_Qubits/). Every gate in this chapter acts on the Hilbert space defined in `900_Qubits/001_`; every per-modality fidelity and gate-time number in `005_` is bounded by the $T_1, T_2$ characterisation in `900_Qubits/004_`; every reference to overhead in `004_` compounds with the physical-to-logical ratio in `900_Qubits/005_`.
- **Downstream (within `900-909`)** — [`../902_circuits/`](../902_circuits/), [`../903_quantum-algorithms/`](../903_quantum-algorithms/), [`../904_foundations/`](../904_foundations/). The chapter boundary against `902_circuits/` is stated explicitly in `000_Overview.md` §2 and `004_` §3.
- **Within QCSAA `900-999`** — `910-919` Quantum Machine Learning & Quantum AI (variational circuits depend on the entangling-gate family of `003_`), `920-929` Quantum Networks & Communications (entanglement distribution depends on the Bell/EPR preparation of `003_`), `930-939` Quantum Cybersecurity, `950-959` Quantum Simulation, `960-969` Quantum Robotics, `970-979` Sentient Quantum Agency.
- **Cross-band** — CYB `880-889` Post-Quantum Cryptography back-references the universality and overhead arguments of `004_` to size the threat model.

Downstream chapters shall back-reference the specific subsubjects of this subsection rather than re-introduce the underlying gate concepts.

## 7. Change Log

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0.0 | 2026-05-07 | Q-HORIZON | Initial baseline: `000_Overview.md` plus subsubjects `001`–`005`. Subsection index established; chapter parallel to `900_Qubits/` (definition → categories → composition → universality → physical realization). |

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
