---
document_id: QATL-ATLAS1000-QCSAA-900-909-00-907-000-OVERVIEW
title: "QCSAA 900-909 · 00.907.000 — Measurement-Based and One-Way Computing"
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
subsection: "907"
subsection_title: "Measurement-Based and One-Way Computing"
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

# QCSAA 900-909 · Section 00 · Subsection 907 — Measurement-Based and One-Way Computing

## 1. Purpose

Overview entry-point for the *Measurement-Based and One-Way Computing* subsection within the `900-909` code range (Section `00` — *Fundamentos de Computación Cuántica*) of the **QCSAA** architecture band (*Quantum Computing & Sentient Agency Architecture*, master range `900–999`).

This subsubject (`000 Overview`) introduces the QCSAA 900-909.907.000 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable standards listed in §4. It establishes the foundational framework — cluster and graph states, adaptive single-qubit measurements, measurement patterns and flow conditions, equivalence with the circuit model, physical realizations, fault-tolerance, and aerospace hardware applicability — that governs all measurement-based quantum computation (MBQC) theory and engineering within the Q+ATLANTIDE programme.

**Restricted band (N-006[^n006]).** This document inherits `governance_class: restricted` from the parent QCSAA section.

## 2. Scope

- Covers the *Measurement-Based and One-Way Computing* slice of the parent code range `900-909`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Subsequent subsubjects (`001`–`007`) under this subsection extend this Overview with detailed data modules; the populated set in this baseline is `001`–`007`, indexed in [`README.md`](./README.md).
- Concepts in scope across the subsection:
  - **Cluster States and Graph States** (`001`) — graph state formalism, stabilizer generators, cluster states as universal resource states for MBQC[^raussendorf_briegel][^briegel_mbqc].
  - **One-Way Computation Model** (`002`) — the Raussendorf-Briegel one-way quantum computer: adaptive single-qubit measurements, classical feed-forward, byproduct operators, and the separation of quantum and classical resources[^raussendorf_briegel].
  - **Measurement Patterns and Flow Conditions** (`003`) — measurement calculus, open graph states, determinism conditions, flow and generalised flow (gflow), causal flow, and their algorithmic verification[^danos_kashefi][^browne_flow].
  - **Equivalence with Circuit Model** (`004`) — formal simulation of unitary circuits by MBQC patterns, universality proof, teleportation-based gate constructions, and depth-complexity trade-offs[^nielsen_cluster][^gross_eisert].
  - **Photonic and Continuous-Variable Realizations** (`005`) — linear optical MBQC (KLM and Browne-Rudolph schemes), continuous-variable cluster states, GKP encoding, and dual-rail photonic implementations[^browne_rudolph][^menicucci_cv].
  - **Fault-Tolerance in Measurement-Based Computing** (`006`) — topological fault-tolerance on 3-D cluster states (Raussendorf-Harrington-Goyal), surface-code MBQC, percolation thresholds, and loss-tolerant schemes[^raussendorf_topological].
  - **Aerospace Applicability and Hardware Realizations** (`007`) — photonic MBQC for space-borne and airborne platforms, cryogenic and room-temperature hardware trade-offs, satellite quantum links, and Q+ATLANTIDE programme applicability[^esa_qci].

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subsection | `907` — Measurement-Based and One-Way Computing |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/907_Measurement-Based-and-One-Way-Computing/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **QCSAA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `900-909` row (Section `00` — Fundamentos de Computación Cuántica, Primary Q-Division Q-HORIZON).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `restricted` denotes documents requiring additional governance, evidence packages and access controls (rule N-006).

[^n006]: **Note N-006 (Restricted bands)** — Quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls. See [`organization/Q+ATLANTIDE.md` §5.3](../../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).

[^raussendorf_briegel]: **Raussendorf, R. & Briegel, H. J. — "A One-Way Quantum Computer" (*Physical Review Letters* 86(22), 2001, pp. 5188–5191)** — Foundational paper introducing cluster states and the one-way quantum computer model. [DOI:10.1103/PhysRevLett.86.5188](https://doi.org/10.1103/PhysRevLett.86.5188).

[^briegel_mbqc]: **Briegel, H. J., Browne, D. E., Dür, W., Raussendorf, R. & Van den Nest, M. — "Measurement-based quantum computation" (*Nature Physics* 5, 2009, pp. 19–26)** — Comprehensive review of MBQC: resource states, measurement patterns, and computational power. [DOI:10.1038/nphys1157](https://doi.org/10.1038/nphys1157).

[^danos_kashefi]: **Danos, V. & Kashefi, E. — "Determinism in the one-way model" (*Physical Review A* 74, 052310, 2006)** — Defines the measurement calculus and the flow condition for deterministic MBQC. [DOI:10.1103/PhysRevA.74.052310](https://doi.org/10.1103/PhysRevA.74.052310).

[^browne_flow]: **Browne, D. E., Kashefi, E., Mhalla, M. & Perdrix, S. — "Generalized Flow and Determinism in Measurement-Based Quantum Computation" (*New Journal of Physics* 9, 250, 2007)** — Generalised flow (gflow) condition extending determinism to a wider class of measurement patterns. [DOI:10.1088/1367-2630/9/8/250](https://doi.org/10.1088/1367-2630/9/8/250).

[^nielsen_cluster]: **Nielsen, M. A. — "Cluster-state quantum computation" (*Reports on Mathematical Physics* 57(1), 2006, pp. 147–161)** — Circuit-model equivalence, universality, and teleportation-based constructions for MBQC. [DOI:10.1016/S0034-4877(06)80014-5](https://doi.org/10.1016/S0034-4877(06)80014-5).

[^gross_eisert]: **Gross, D. & Eisert, J. — "Novel schemes for measurement-based quantum computation" (*Physical Review Letters* 98, 220503, 2007)** — Extends MBQC universality beyond cluster states; resource-state classification. [DOI:10.1103/PhysRevLett.98.220503](https://doi.org/10.1103/PhysRevLett.98.220503).

[^browne_rudolph]: **Browne, D. E. & Rudolph, T. — "Resource-Efficient Linear Optical Quantum Computation" (*Physical Review Letters* 95, 010501, 2005)** — Fusion-based photonic scheme for building cluster states with linear optics. [DOI:10.1103/PhysRevLett.95.010501](https://doi.org/10.1103/PhysRevLett.95.010501).

[^menicucci_cv]: **Menicucci, N. C. et al. — "Universal Quantum Computation with Continuous-Variable Cluster States" (*Physical Review Letters* 97, 110501, 2006)** — CV cluster states and Gaussian measurement operations for universal MBQC. [DOI:10.1103/PhysRevLett.97.110501](https://doi.org/10.1103/PhysRevLett.97.110501).

[^raussendorf_topological]: **Raussendorf, R., Harrington, J. & Goyal, K. — "Topological fault-tolerance in cluster state quantum computation" (*New Journal of Physics* 9, 199, 2007)** — 3-D cluster state topological code achieving fault-tolerance with high threshold. [DOI:10.1088/1367-2630/9/6/199](https://doi.org/10.1088/1367-2630/9/6/199).

[^esa_qci]: **ESA — Quantum Computing and Communication for Space (QCI4Space programme, 2022–)** — European Space Agency strategic initiative addressing space-borne quantum hardware, satellite quantum links, and aerospace quantum computing applicability.

[^iso4879]: **ISO/IEC 4879:2023 — Information technology — Quantum computing — Vocabulary** — International standard vocabulary for quantum computing terms including cluster state, graph state, measurement-based computation, and entanglement.

### Applicable standards

The following standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- Raussendorf & Briegel — *A One-Way Quantum Computer* (PRL, 2001)[^raussendorf_briegel]
- Briegel et al. — *Measurement-based quantum computation* (Nature Physics, 2009)[^briegel_mbqc]
- Danos & Kashefi — *Determinism in the one-way model* (PRA, 2006)[^danos_kashefi]
- Nielsen — *Cluster-state quantum computation* (Reports on Mathematical Physics, 2006)[^nielsen_cluster]
- ISO/IEC 4879:2023 — Quantum computing — Vocabulary[^iso4879]
