---
document_id: QATL-ATLAS-1000-QCSAA-900-909-00-901-000-OVERVIEW
title: "QCSAA 900-909 · 00.901.000 — gates"
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
subsubject: "000"
subsubject_title: "Overview"
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

Overview entry-point for the *gates* subsection within the `900-909` code range (Section `00` — *Fundamentos de Computación Cuántica*) of the **QCSAA** architecture band (*Quantum Computing & Sentient Agency Architecture*, master range `900–999`).

This subsubject (`00 Overview`) introduces the QCSAA 900-909.020.00 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable industry standards listed in §4.

## 2. Scope

- Covers the *gates* slice of the parent code range `900-909`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`001`–`099`) under this subsection extend this Overview with detailed data modules per S1000D[^s1000d]; the populated set in this baseline is `001`–`005`, indexed in [`README.md`](./README.md).
- **Position in the 900-909 dependency graph.** Gates are the **operations on the substrate** defined by [`../900_Qubits/`](../900_Qubits/): where `010_` defines the two-level quantum system, its Hilbert space, and its physical implementations, `020_` defines the unitary operations that act on those systems. Gates are therefore the **immediate prerequisite for [`../902_circuits/`](../902_circuits/)** (composition of gates into algorithms) and an upstream dependency for [`../903_quantum-algorithms/`](../903_quantum-algorithms/) and [`../904_foundations/`](../904_foundations/).
- **Pedagogical sequence followed in this chapter** (deliberately parallel to `900_Qubits/`): **definition → categories → composition → universality → physical realization**. The slot semantics are predictable across foundational chapters so that, once a reader has navigated `010_`, every subsequent foundational chapter is faster.
- **Boundary against `902_circuits/` (binding for contributors).** This chapter covers the **unitary operation as such** — its mathematical definition, its decomposition into a universal set, its physical realization on a given modality, its fidelity. The chapter [`../902_circuits/`](../902_circuits/) covers what happens **when gates are composed into computational sequences** — circuit depth, parallelization, measurement timing, mid-circuit measurement, classical control flow, and resource estimation at the algorithm level. Material naturally suggested by gate counts (e.g. "circuit depth as a function of T-count") belongs in `030_`, not in `020_`. This rule is restated in `004_` because that is the slot where the temptation to drift across the boundary is strongest.

## 3. Subsubject Inventory

| NN | Title | Document |
|---:|---|---|
| 00 | Overview (this file) | [`000_Overview.md`](./000_Overview.md) |
| 01 | Gate Definition and Unitary Formalism | [`001_Gate-Definition-and-Unitary-Formalism.md`](./001_Gate-Definition-and-Unitary-Formalism.md) |
| 02 | Single-Qubit Gates | [`002_Single-Qubit-Gates.md`](./002_Single-Qubit-Gates.md) |
| 03 | Multi-Qubit Gates and Entangling Operations | [`003_Multi-Qubit-Gates-and-Entangling-Operations.md`](./003_Multi-Qubit-Gates-and-Entangling-Operations.md) |
| 04 | Universal Gate Sets and Decomposition | [`004_Universal-Gate-Sets-and-Decomposition.md`](./004_Universal-Gate-Sets-and-Decomposition.md) |
| 05 | Gate Implementation, Calibration and Error Characterization | [`005_Gate-Implementation-Calibration-and-Error-Characterization.md`](./005_Gate-Implementation-Calibration-and-Error-Characterization.md) |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subject | `00` — General Information |
| Subsection | `901` — gates |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/901_gates/` |
| Document | `000_Overview.md` (this file) |
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

