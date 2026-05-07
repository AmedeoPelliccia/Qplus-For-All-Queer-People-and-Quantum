---
document_id: QATL-ATLAS-1000-QCSAA-900-909-00-905-000-OVERVIEW
title: "QCSAA 900–909 · 00.905.000 — Quantum Complexity and Resource Theory"
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
subsection: "905"
subsection_title: "Quantum Complexity and Resource Theory"
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
# QCSAA 900–909 · Section 00 · Subsection 905 — Quantum Complexity and Resource Theory

## 1. Purpose

Overview entry-point for the *Quantum Complexity and Resource Theory* subsection within the `900-909` code range (Section `00` — *Fundamentos de Computación Cuántica*) of the **QCSAA** architecture band (*Quantum Computing & Sentient Agency Architecture*, master range `900–999`).

This subsubject (`000 Overview`) introduces the QCSAA 900-909.905.000 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable standards listed in §4. It establishes the canonical complexity and resource vocabulary — quantum complexity classes, oracle and circuit lower bounds, and resource-theoretic frameworks for entanglement and non-stabilizer (magic) resources — that every QCSAA subsection quantifying algorithmic hardness or resource costs depends on.

**Restricted band (N-006[^n006]).** This document inherits `governance_class: restricted` and must be accompanied by a declared `evidence_package_id` and `access_control_profile`.

## 2. Scope

- Covers the *Quantum Complexity and Resource Theory* slice of the parent code range `900-909`.
- Inherits Q-Division authority and ORB support from the parent row in [`../README.md`](../README.md)[^archtable].
- Subsequent subsubjects (`001`–`007`) under this subsection extend this Overview with detailed data modules; the populated set in this baseline is `001`–`007`, indexed in [`README.md`](./README.md).
- Concepts in scope across the subsection:
  - **Quantum Complexity Classes BQP, QMA, QCMA** (`001`) — bounded-error quantum polynomial time (BQP) as the class of efficiently decidable problems on a quantum computer; quantum Merlin-Arthur (QMA) and classical-witness variant (QCMA); class relationships and oracle separations from classical classes per Watrous[^watrous].
  - **Query Complexity and Oracle Separations** (`002`) — the quantum query model, decision-tree and adversary lower bounds, the polynomial method; Grover's quadratic speedup and the Simon/Bernstein-Vazirani separations demonstrating BQP ⊄ BPP relative to oracles.
  - **Circuit Complexity and Lower Bounds** (`003`) — quantum circuit complexity, depth-width trade-offs, the QNC hierarchy, lower bounds via rank and communication-complexity arguments, and the relationship between circuit depth and parallel quantum advantage.
  - **Resource Theory Foundations** (`004`) — the axiomatic framework of quantum resource theories: free states, free operations, monotones, and conversion rates; applied to coherence, entanglement, and thermodynamics following Winter[^winter].
  - **Entanglement as Resource** (`005`) — entanglement distillation and formation, LOCC-convertibility, Schmidt rank, entanglement entropy, and the operational role of entanglement in teleportation, dense coding, and quantum key distribution.
  - **Magic States and Non-Stabilizer Resources** (`006`) — the stabiliser/Clifford free subset, non-stabilizer (magic) measures (robustness, mana, stabilizer extent), magic-state distillation overhead, and the connection to universal fault-tolerant gate sets.
  - **Quantum Advantage, Classical Hardness and Verification** (`007`) — sampling-based quantum supremacy arguments (random circuit sampling, boson sampling), average-case hardness under polynomial-hierarchy collapse assumptions, and protocols for verifying quantum computations classically or interactively.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subsection | `905` — Quantum Complexity and Resource Theory |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/905_Quantum-Complexity-and-Resource-Theory/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Subsubject Index (parent README)** — [`README.md` §3](./README.md#3-subsubject-index). Authoritative source for the `905` row (Subsection `905` — Quantum Complexity and Resource Theory, Primary Q-Division Q-HORIZON).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `restricted` denotes documents requiring additional governance, evidence packages and access controls (rule N-006[^n006]).

[^n006]: **Note N-006 (Restricted bands)** — Quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls. Templates must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`. See [`organization/Q+ATLANTIDE.md` §5.3](../../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).

[^nielchung]: **Nielsen, M. A. & Chuang, I. L. (2010)** — *Quantum Computation and Quantum Information* (10th Anniversary Edition). Cambridge University Press. Chapters 4 and 5 cover quantum circuits and quantum algorithms; Chapter 10 introduces error correction and resource overhead.

[^arorababarak]: **Arora, S. & Barak, B. (2009)** — *Computational Complexity: A Modern Approach*. Cambridge University Press. Standard graduate reference for classical complexity classes, circuit complexity, and oracle separations underpinning quantum complexity theory.

[^watrous]: **Watrous, J. (2009)** — "Quantum Computational Complexity." In *Encyclopedia of Complexity and Systems Science*. Springer. Comprehensive survey of BQP, QMA, QIP, and their relationships to classical complexity classes.

[^winter]: **Winter, A. & Streltsov, A. (2016)** — "Operational Resource Theory of Coherence." *Physical Review Letters*, 116, 120404. Foundational paper establishing the resource-theoretic treatment of quantum coherence as a formal framework.

[^isoiec4879]: **ISO/IEC 4879:2023** — *Quantum computing — Vocabulary*. International standard defining quantum advantage (§3.18), quantum supremacy (§3.19), and related terms.

### Applicable standards

The following standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- Nielsen & Chuang (2010) — *Quantum Computation and Quantum Information*[^nielchung]
- Arora & Barak (2009) — *Computational Complexity: A Modern Approach*[^arorababarak]
- Watrous (2009) — "Quantum Computational Complexity"[^watrous]
- ISO/IEC 4879:2023 — *Quantum computing — Vocabulary*[^isoiec4879]
