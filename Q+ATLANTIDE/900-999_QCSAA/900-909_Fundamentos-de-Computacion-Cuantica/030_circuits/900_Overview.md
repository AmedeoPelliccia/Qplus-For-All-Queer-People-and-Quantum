---
document_id: QATL-ATLAS-1000-QCSAA-900-909-00-030-900-OVERVIEW
title: "QCSAA 900-909 · 00.030.900 — circuits"
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
subsubject: "900"
subsubject_title: "Overview"
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

Overview entry-point for the *circuits* subsection within the `900-909` code range (Section `00` — *Fundamentos de Computación Cuántica*) of the **QCSAA** architecture band (*Quantum Computing & Sentient Agency Architecture*, master range `900–999`).

This subsubject (`900 Overview`) introduces the QCSAA 900-909.030.900 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4.

## 2. Scope

- Covers the *circuits* slice of the parent code range `900-909`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`901`–`999`) under this subsection extend this Overview with detailed data modules per S1000D[^s1000d]; the populated set in this baseline is `901`–`905`, indexed in [`README.md`](./README.md).
- **Position in the 900-909 dependency graph.** Circuits are the **synthesis** of the two preceding chapters: where [`../010_Qubits/`](../010_Qubits/) defines the substrate (the two-level quantum system, its Hilbert space, its physical implementations) and [`../901_gates/`](../901_gates/) defines the unitary operations on that substrate, `030_` defines the **computational artefacts that actually do work** by composing those operations into ordered, measured, classically-controlled sequences. Circuits are therefore the unit on which every downstream range of QCSAA operates: [`../040_quantum-algorithms/`](../040_quantum-algorithms/) consumes circuits as the realisation of an algorithm, `910-919` (Quantum Machine Learning & Quantum AI) consumes parameterised circuits as the model class, `940-949` (Quantum Sensing) consumes circuits as the measurement protocol, and `950-959` (Quantum Simulation) consumes circuits as the encoded Hamiltonian-evolution sequence.
- **Pedagogical sequence followed in this chapter** (deliberately parallel to [`../010_Qubits/`](../010_Qubits/) and [`../901_gates/`](../901_gates/)): **definition → properties → operations → engineering → practice**. The five-file slot semantics are stable across the three foundational chapters of `900-909` so that, once a reader has navigated one foundational chapter, the next two are predictable. The parallelism is not aesthetic; it is the contract that makes the foundational range navigable.
- **Boundary against `901_gates/` (binding for contributors).** Material that concerns a single unitary operation in isolation — its definition, its decomposition into a universal set, its physical realisation and calibration on a given modality, its per-gate fidelity — belongs in [`../901_gates/`](../901_gates/). Material that concerns **what happens when gates are composed** — circuit depth, parallelisation across the qubit register, measurement timing and mid-circuit measurement, classical feed-forward, optimisation/compilation/transpilation across an ISA, noise-resilient circuit patterns — belongs here in `030_`. The dividing line is restated in `901_` §2 and is binding.
- **Boundary against `040_quantum-algorithms/` (binding for contributors).** This chapter covers the **circuit as a computational artefact**: its structural properties (depth, width), its operational primitives (measurement, mid-circuit measurement, classical control), its engineering pipeline (optimisation, compilation, transpilation), and its operational regime (NISQ-era patterns, noise resilience). It does **not** cover specific algorithms (Grover, Shor, QAOA, VQE, HHL): those are realised *as* circuits but their algorithmic content — oracle structure, query complexity, ansatz semantics — is the proper subject of `040_`. Material that asks "what does this circuit *compute*" goes to `040_`; material that asks "what does this circuit *cost* and *how* is it executed" stays here.

## 3. Subsubject Inventory

| NNN | Title | Document |
|---:|---|---|
| 900 | Overview (this file) | [`900_Overview.md`](./900_Overview.md) |
| 901 | Circuit Definition and Composition | [`901_Circuit-Definition-and-Composition.md`](./901_Circuit-Definition-and-Composition.md) |
| 902 | Circuit Depth, Width and Parallelism | [`902_Circuit-Depth-Width-and-Parallelism.md`](./902_Circuit-Depth-Width-and-Parallelism.md) |
| 903 | Measurement, Mid-Circuit and Classical Control | [`903_Measurement-Mid-Circuit-and-Classical-Control.md`](./903_Measurement-Mid-Circuit-and-Classical-Control.md) |
| 904 | Circuit Optimization, Compilation and Transpilation | [`904_Circuit-Optimization-Compilation-and-Transpilation.md`](./904_Circuit-Optimization-Compilation-and-Transpilation.md) |
| 905 | Noise-Resilient Circuit Patterns and NISQ Practice | [`905_Noise-Resilient-Circuit-Patterns-and-NISQ-Practice.md`](./905_Noise-Resilient-Circuit-Patterns-and-NISQ-Practice.md) |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subject | `00` — General Information |
| Subsection | `030` — circuits |
| Subsubject | `900` — Overview |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/030_circuits/` |
| Document | `900_Overview.md` (this file) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations


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

The following ATA-family and industry standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- IEEE P7130 — Standard for Quantum Computing Definitions[^ieeep7130]
- NIST IR 8413 — Status Report on the Third Round of the NIST Post-Quantum Cryptography Standardization Process[^nistir8413]
- ETSI GR QSC 001 — Quantum-Safe Cryptography (QSC); Quantum-safe algorithmic framework[^etsiqsc001]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]

