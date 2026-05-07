---
document_id: QATL-ATLAS-1000-QCSAA-900-909-00-030-README
title: "QCSAA 900-909 · 00.030 — circuits (Subsection Index)"
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
subsection: "030"
subsection_title: "circuits"
primary_q_division: Q-HORIZON
support_q_divisions: [Q-HPC, Q-DATAGOV]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: restricted
version: 1.0.0
status: active
language: en
---
# QCSAA 900-909 · Section 00 · Subsection 030 — circuits

## 1. Purpose

Subsection-level index for *circuits* (`030`) within QCSAA `900-909` — *Fundamentos de Computación Cuántica*. Aggregates the `900 Overview` and the detailed subsubjects (`901`–`905`) that introduce the **quantum circuit** as the directed, measured, classically-controlled composition of unitary gates over a qubit register; formalise its structural resource metrics (depth, width, parallelism); document measurement, mid-circuit measurement and classical feed-forward; describe the optimisation/compilation/transpilation pipeline that maps a logical circuit to a hardware ISA; and record the noise-resilient circuit patterns appropriate to NISQ-era execution — under the controlled Q+ATLANTIDE baseline[^baseline] and the IEEE quantum-computing vocabulary[^ieeep7130].

This subsection is the **third foundational chapter** of the QCSAA band and the **synthesis** of [`../900_Qubits/`](../900_Qubits/) and [`../020_gates/`](../020_gates/): where qubits define the substrate and gates define the operations, circuits define the **computational artefacts** that downstream ranges actually consume. It is the **immediate prerequisite** for [`../040_quantum-algorithms/`](../040_quantum-algorithms/) and an upstream dependency for `910-919` (QML), `940-949` (sensing) and `950-959` (simulation), all of which operate on circuits — not on gates or qubits in isolation.

The chapter is organised in the same five-file structure as [`../900_Qubits/`](../900_Qubits/) and [`../020_gates/`](../020_gates/) — **definition → properties → operations → engineering → practice** — deliberately. The semantic slots are stable across the foundational range: once readers have learned the slot semantics of one foundational chapter, every subsequent foundational chapter in `900-909` is faster to navigate. The parallelism is the contract.

## 2. Scope

- Covers the full subsubject namespace `900`–`999` of subsection `030` *circuits*; subsubjects `901`–`905` are populated in this baseline release, the remaining `906`–`999` slots remain available for future extension per the Overview's authorisation[^archtable].
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Pedagogical sequence followed: **definition → properties → operations → engineering → practice**, mirroring [`../900_Qubits/`](../900_Qubits/) and [`../020_gates/`](../020_gates/).
- **Boundary against [`../020_gates/`](../020_gates/)** (binding for contributors). `020_` covers the **single unitary operation** — its definition, its decomposition into a universal set, its physical realisation and per-gate fidelity. This chapter covers what happens **when those operations are composed into circuits**: depth, parallelism, measurement timing, mid-circuit measurement, classical control flow, and the engineering pipeline that emits hardware-executable instructions. The rule is restated in `900_Overview.md` §2 and re-bindingly in `901_` §2.
- **Boundary against [`../040_quantum-algorithms/`](../040_quantum-algorithms/)** (binding for contributors). This chapter covers the circuit as a **structural and operational artefact** — its cost, its execution semantics, its compilation. It does **not** cover what specific algorithms (Grover, Shor, QAOA, VQE, HHL) compute — that is the proper subject of `040_`. Material that asks "what does this circuit *compute*" goes to `040_`; material that asks "what does this circuit *cost* and *how* is it executed" stays here. The rule is restated in `900_Overview.md` §2 and in `904_` §2 because that is the slot where the temptation to drift into algorithm-specific arguments is strongest.

## 3. Subsubject Index

| NNN | Title | Document | Status |
|---:|---|---|---|
| 900 | Overview | [`900_Overview.md`](./900_Overview.md) | active |
| 901 | Circuit Definition and Composition | [`901_Circuit-Definition-and-Composition.md`](./901_Circuit-Definition-and-Composition.md) | active |
| 902 | Circuit Depth, Width and Parallelism | [`902_Circuit-Depth-Width-and-Parallelism.md`](./902_Circuit-Depth-Width-and-Parallelism.md) | active |
| 903 | Measurement, Mid-Circuit and Classical Control | [`903_Measurement-Mid-Circuit-and-Classical-Control.md`](./903_Measurement-Mid-Circuit-and-Classical-Control.md) | active |
| 904 | Circuit Optimization, Compilation and Transpilation | [`904_Circuit-Optimization-Compilation-and-Transpilation.md`](./904_Circuit-Optimization-Compilation-and-Transpilation.md) | active |
| 905 | Noise-Resilient Circuit Patterns and NISQ Practice | [`905_Noise-Resilient-Circuit-Patterns-and-NISQ-Practice.md`](./905_Noise-Resilient-Circuit-Patterns-and-NISQ-Practice.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subject | `00` — General Information |
| Subsection | `030` — circuits |
| Subsubject namespace | `900`–`999` (`900` + `901`–`905` populated) |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/030_circuits/` |
| Document | `README.md` (this file) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = QCSAA`, `primary_q_division = Q-HORIZON` and `governance_class = restricted` from the parent QCSAA band; extensions added under `906`–`999` shall preserve those header fields and reuse the footnote set declared below.

## 6. Upstream, Downstream and Cross-Band Dependencies

- **Upstream (within `900-909`)** — [`../900_Qubits/`](../900_Qubits/) and [`../020_gates/`](../020_gates/). Every circuit in this chapter operates on the Hilbert space defined in `900_Qubits/001_` and is composed of the unitary operations defined in `020_gates/01_`–`020_gates/04_`; every circuit-depth and noise-budget argument in `902_` and `905_` is bounded by the per-gate times and fidelities of [`../020_gates/05_Gate-Implementation-Calibration-and-Error-Characterization.md`](../020_gates/05_Gate-Implementation-Calibration-and-Error-Characterization.md) and the $T_1, T_2$ values of [`../900_Qubits/004_Decoherence-Noise-and-Fidelity.md`](../900_Qubits/004_Decoherence-Noise-and-Fidelity.md).
- **Downstream (within `900-909`)** — [`../040_quantum-algorithms/`](../040_quantum-algorithms/), [`../904_foundations/`](../904_foundations/). The chapter boundary against `040_quantum-algorithms/` is stated explicitly in `900_Overview.md` §2 and re-bindingly in `904_` §2.
- **Within QCSAA `900-999`** — `910-919` Quantum Machine Learning & Quantum AI (parameterised / variational circuits depend on the depth, width and ansatz patterns of `902_` and `905_`), `920-929` Quantum Networks & Communications (entanglement-distribution protocols are circuits with classical communication, depending on `903_`), `930-939` Quantum Cybersecurity, `940-949` Quantum Sensing (sensing protocols are measurement circuits, depending on `903_`), `950-959` Quantum Simulation (Hamiltonian-evolution circuits depend on Trotter-step depth analysis from `902_` and `904_`), `960-969` Quantum Robotics, `970-979` Sentient Quantum Agency.
- **Cross-band** — CYB `880-889` Post-Quantum Cryptography back-references the resource estimates produced by the depth/width analysis of `902_` and the compilation pipeline of `904_` to size the threat model.

Downstream chapters shall back-reference the specific subsubjects of this subsection rather than re-introduce the underlying circuit concepts.

## 7. Change Log

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0.0 | 2026-05-07 | Q-HORIZON | Initial baseline: `900_Overview.md` plus subsubjects `901`–`905`. Subsection index established; chapter parallel to `900_Qubits/` and `020_gates/` (definition → properties → operations → engineering → practice). |

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
