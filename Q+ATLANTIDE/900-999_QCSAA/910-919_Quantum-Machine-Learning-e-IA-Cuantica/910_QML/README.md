---
document_id: QATL-ATLAS-1000-QCSAA-910-919-01-010-README
title: "QCSAA 910-919 · 01.010 — QML (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
architecture_code: QCSAA
architecture_name: "Quantum Computing & Sentient Agency Architecture"
master_range: "900–999"
code_range: "910-919"
section: "01"
section_title: "Quantum Machine Learning e IA Cuántica"
subject: "00"
subject_title: "General Information"
subsection: "010"
subsection_title: "QML"
primary_q_division: Q-HPC
support_q_divisions: [Q-HORIZON, Q-DATAGOV]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: restricted
version: 1.0.0
status: active
language: en
---
# QCSAA 910-919 · Section 01 · Subsection 010 — QML

## 1. Purpose

Subsection-level index for *Quantum Machine Learning* (`010` QML) within QCSAA `910-919` — *Quantum Machine Learning e IA Cuántica*. Aggregates the `000 Overview` and the detailed subsubjects (`001`–`008`) that define what QML is and isn't, how classical data is encoded into quantum states, how kernels and variational circuits are built and trained, how noise and barren plateaus constrain trainability, how QML models are verified and benchmarked, and where they enter aerospace assurance boundaries — under the controlled Q+ATLANTIDE baseline[^baseline] and the IEEE quantum-computing vocabulary[^ieeep7130].

This subsection is the **applied-learning chapter** of the QCSAA band: it presupposes the qubit, gate, circuit and algorithm primitives defined in `900-909` *Fundamentos de Computación Cuántica*, and supplies the modelling and trainability vocabulary consumed by the rest of `910-919` (hybrid AI, optimisation-learning) as well as by sentient-agency rows further downstream in the band.

## 2. Scope

- Covers the full subsubject namespace `000`–`009` of subsection `010` *QML*; subsubjects `001`–`008` are populated in this baseline release, the `009` slot remains available for future extension per the Overview's authorisation[^archtable].
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Pedagogical sequence followed: **definition → encoding → kernels → variational circuits → hybrid training → trainability obstructions → verification → aerospace use & assurance**, the canonical structure for an applied QML primer aimed at safety-relevant programmes.
- Acts as the upstream reference anchor for `020_hybrid-quantum-classical-AI/` and `030_optimization-learning/` within the same code range, both of which depend on the encoding, kernel and variational vocabulary defined here.

## 3. Subsubject Index

| 00N | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 001 | QML Definition and Taxonomy | [`001_QML-Definition-and-Taxonomy.md`](./001_QML-Definition-and-Taxonomy.md) | active |
| 002 | Data Encoding and Feature Maps | [`002_Data-Encoding-and-Feature-Maps.md`](./002_Data-Encoding-and-Feature-Maps.md) | active |
| 003 | Quantum Kernels and Similarity Models | [`003_Quantum-Kernels-and-Similarity-Models.md`](./003_Quantum-Kernels-and-Similarity-Models.md) | active |
| 004 | Variational QML and Parameterized Circuits | [`004_Variational-QML-and-Parameterized-Circuits.md`](./004_Variational-QML-and-Parameterized-Circuits.md) | active |
| 005 | Hybrid Quantum-Classical Training Loops | [`005_Hybrid-Quantum-Classical-Training-Loops.md`](./005_Hybrid-Quantum-Classical-Training-Loops.md) | active |
| 006 | Noise, Barren Plateaus and Trainability | [`006_Noise-Barren-Plateaus-and-Trainability.md`](./006_Noise-Barren-Plateaus-and-Trainability.md) | active |
| 007 | QML Verification and Benchmarking | [`007_QML-Verification-and-Benchmarking.md`](./007_QML-Verification-and-Benchmarking.md) | active |
| 008 | Aerospace Use Cases and Assurance Boundaries | [`008_Aerospace-Use-Cases-and-Assurance-Boundaries.md`](./008_Aerospace-Use-Cases-and-Assurance-Boundaries.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `910-919` |
| Section | `01` — Quantum Machine Learning e IA Cuántica |
| Subject | `00` — General Information |
| Subsection | `010` — QML |
| Subsubject namespace | `000`–`009` (`000` + `001`–`008` populated; canonical `00N_*.md` scheme) |
| Primary Q-Division | Q-HPC[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/910-919_Quantum-Machine-Learning-e-IA-Cuantica/910_QML/` |
| Document | `README.md` (this file) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = QCSAA`, `primary_q_division = Q-HPC` and `governance_class = restricted` from the parent QCSAA band; extensions added under the remaining `009` slot shall preserve those header fields, follow the canonical `00N_*.md` naming scheme, and reuse the footnote set declared below. Any subsubject that proposes the use of QML output inside a certified aerospace function must back-reference `008_Aerospace-Use-Cases-and-Assurance-Boundaries.md` and shall not relax the assurance boundary defined there without going through the Q+ATLANTIDE change-control process.

## 6. Downstream and Cross-Band Dependencies

The QML model defined in this subsection is consumed by:

- **Within `910-919`** — `020_hybrid-quantum-classical-AI/` (uses the hybrid-loop and variational vocabulary of `004_`–`005_`) and `030_optimization-learning/` (uses the kernel and trainability vocabulary of `003_` and `006_`).
- **Within QCSAA `900-999`** — `950-959` Quantum Simulation (shared variational ansatz family with VQE), `960-969` Quantum Robotics (QML for perception/control under the `008_` assurance boundary), `970-979` Sentient Quantum Agency (uses `001_` taxonomy to classify learning components of agents), `980-989` Governance and Ethics (uses `007_`–`008_` as the auditable-evidence baseline for QML claims).
- **Cross-band** — ATLAS aerospace bands consume `008_` whenever a QML component is proposed inside a certifiable function; the subsubject draws the assurance boundary that the rest of the register must respect.

Downstream chapters shall back-reference the specific subsubjects of this subsection rather than re-introduce the underlying concepts.

## 7. Change Log

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0.0 | 2026-05-07 | Q-HPC | Initial baseline: `000_Overview.md` plus subsubjects `001`–`008`, using the sequential `00N_*.md` scheme under the `910_QML/` subsection. Subsection index established. |

## 8. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **QCSAA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `910-919` row (Section `01` — Quantum Machine Learning e IA Cuántica, Primary Q-Division Q-HPC).

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
