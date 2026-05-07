---
document_id: QATL-ATLAS-1000-QCSAA-900-909-00-905-README
title: "QCSAA 900–909 · 00.905 — Quantum Complexity and Resource Theory (Subsection Index)"
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
subsection: "905"
subsection_title: "Quantum Complexity and Resource Theory"
primary_q_division: Q-HORIZON
support_q_divisions: [Q-HPC, Q-DATAGOV]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: restricted
restricted_rule: N-006
version: 1.0.0
status: active
language: en
---

# QCSAA 900–909 · Section 00 · Subsection 905 — Quantum Complexity and Resource Theory

## 1. Purpose

Subsection-level index for *Quantum Complexity and Resource Theory* (`905`) within QCSAA `900-909` — *Fundamentos de Computación Cuántica*. Covers quantum computational complexity classes and their relationships, query and circuit complexity, oracle separations, and the resource-theoretic framework that formalises quantum advantages in terms of entanglement, magic, and coherence.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It draws on the qubit formalism established in `900_Qubits/`, the gate-set taxonomy of `901_Gates/`, and the circuit model of `902_Circuits/`, and provides the complexity and resource vocabulary consumed by every QCSAA subsection that quantifies quantum advantage or estimates algorithmic resource costs.

**Restricted band (N-006[^n006]).** All documents under this subsection additionally inherit `governance_class: restricted` and must declare `evidence_package_id` and `access_control_profile`.

## 2. Scope

- Covers the full subsubject namespace `000`–`009` of subsection `905` *Quantum Complexity and Resource Theory*; subsubjects `000`–`007` are populated in this baseline release, slots `008`–`009` remain available for future extension.
- Inherits Q-Division authority and ORB support from the parent row in [`../README.md` §3](../README.md#3-subsection-index)[^archtable] and the section index in [`../../README.md`](../../README.md).
- Establishes the canonical complexity and resource vocabulary — BQP, QMA, QCMA, oracle separations, circuit lower bounds, resource theories of entanglement and magic — used by every downstream QCSAA subsection that references computational hardness or resource costs.

## 3. Subsubject Index

| 00N | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 001 | Quantum Complexity Classes BQP, QMA, QCMA | [`001_Quantum-Complexity-Classes-BQP-QMA-QCMA.md`](./001_Quantum-Complexity-Classes-BQP-QMA-QCMA.md) | active |
| 002 | Query Complexity and Oracle Separations | [`002_Query-Complexity-and-Oracle-Separations.md`](./002_Query-Complexity-and-Oracle-Separations.md) | active |
| 003 | Circuit Complexity and Lower Bounds | [`003_Circuit-Complexity-and-Lower-Bounds.md`](./003_Circuit-Complexity-and-Lower-Bounds.md) | active |
| 004 | Resource Theory Foundations | [`004_Resource-Theory-Foundations.md`](./004_Resource-Theory-Foundations.md) | active |
| 005 | Entanglement as Resource | [`005_Entanglement-as-Resource.md`](./005_Entanglement-as-Resource.md) | active |
| 006 | Magic States and Non-Stabilizer Resources | [`006_Magic-States-and-Non-Stabilizer-Resources.md`](./006_Magic-States-and-Non-Stabilizer-Resources.md) | active |
| 007 | Quantum Advantage, Classical Hardness and Verification | [`007_Quantum-Advantage-Classical-Hardness-and-Verification.md`](./007_Quantum-Advantage-Classical-Hardness-and-Verification.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subsection | `905` — Quantum Complexity and Resource Theory |
| Subsubject namespace | `000`–`009` (`000` + `001`–`007` populated; canonical `00N_*.md` scheme) |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/905_Quantum-Complexity-and-Resource-Theory/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = QCSAA`, `primary_q_division = Q-HORIZON` and `governance_class = restricted` from the parent QCSAA section. Extensions added under slots `008`–`009` shall preserve those header fields, follow the canonical `00N_*.md` naming scheme, reuse the footnote set declared below, and additionally declare `evidence_package_id` and `access_control_profile` per rule N-006[^n006]. The No-AAA Rule[^n004] applies.

## 6. Downstream and Cross-Subsection Dependencies

The complexity classes, oracle separation results, circuit lower bounds, and resource measures defined in this subsection are consumed by:

- **Within `900-909`** — `900_Qubits/` (physical and logical qubit counts drive resource estimates), `901_Gates/` (gate complexity and universality are quantified here), `902_Circuits/` (circuit depth and width bounds are derived from lower-bound results), `903_Quantum-Algorithms/` (algorithm complexity is classified in BQP/QMA/QCMA), `904_Quantum-Information-Theory/` (Shannon and von Neumann entropy connect to resource distillation rates), `906_Hamiltonian-Methods-and-Adiabatic-Computation/` (adiabatic complexity and gap hardness relate to QMA-completeness), `907_Measurement-Based-and-One-Way-Computing/` (resource state consumption is quantified using resource-theory tools).
- **Across QCSAA `900–999`** — every subsequent QCSAA section that quantifies computational hardness, verifiability, or the cost of a quantum protocol traces back to the complexity classes, oracle bounds, and resource measures established here.

## 7. Change Log

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0.0 | 2026-05-07 | Q-HORIZON | Initial baseline: `000_Overview.md` plus subsubjects `001`–`007`, using the sequential `00N_*.md` scheme under the `905_Quantum-Complexity-and-Resource-Theory/` subsection. Subsection index established. |

## 8. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Subsection Index (parent section)** — [`../README.md` §3](../README.md#3-subsection-index). Authoritative source for the `900-909` row (Section `00` — Fundamentos de Computación Cuántica, Primary Q-Division Q-HORIZON).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `restricted` denotes documents requiring additional governance, evidence packages and access controls (rule N-006[^n006]).

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n002]: **Note N-002** — Architecture bands classify technologies; Q-Divisions provide technical authority; ORB-Functions provide enterprise support. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n006]: **Note N-006 (Restricted bands)** — Quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls beyond the baseline trace record. Templates must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`. See [`organization/Q+ATLANTIDE.md` §5.3](../../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).

[^nielchung]: **Nielsen, M. A. & Chuang, I. L. (2010)** — *Quantum Computation and Quantum Information* (10th Anniversary Edition). Cambridge University Press. Canonical reference for quantum complexity, query models, and the circuit complexity of quantum algorithms.

[^arorababarak]: **Arora, S. & Barak, B. (2009)** — *Computational Complexity: A Modern Approach*. Cambridge University Press. Standard graduate reference for classical complexity classes, oracle separations, and circuit lower bounds.

[^watrous]: **Watrous, J. (2009)** — "Quantum Computational Complexity." In *Encyclopedia of Complexity and Systems Science*. Springer. Comprehensive survey of quantum complexity classes BQP, QMA, QIP, and their relationships.

[^isoiec4879]: **ISO/IEC 4879:2023** — *Quantum computing — Vocabulary*. International standard defining terms and concepts used in quantum computing, including quantum advantage (§3.18) and quantum supremacy (§3.19).
