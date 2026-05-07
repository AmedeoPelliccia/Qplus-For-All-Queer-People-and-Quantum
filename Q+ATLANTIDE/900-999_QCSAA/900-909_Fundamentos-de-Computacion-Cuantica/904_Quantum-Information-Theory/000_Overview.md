---
document_id: QATL-ATLAS1000-QCSAA-900-909-00-904-000-OVERVIEW
title: "QCSAA 900-909 · 00.904.000 — Quantum Information Theory Overview"
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
subsection: "904"
subsection_title: "Quantum Information Theory"
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

# QCSAA 900-909 · Section 00 · Subsection 904 — Quantum Information Theory

## 1. Purpose

Overview entry-point for the *Quantum Information Theory* subsection within the `900-909` code range (Section `00` — *Fundamentos de Computación Cuántica*) of the **QCSAA** architecture band (*Quantum Computing & Sentient Agency Architecture*, master range `900–999`).

This subsubject (`000 Overview`) introduces the QCSAA 900-909.904.000 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable standards and foundational texts listed in §4. Quantum Information Theory provides the mathematical substrate for the entire QCSAA subsection `904`: it formalises how information is encoded, transmitted, stored, and processed using quantum-mechanical systems, and establishes the fundamental limits and boundaries that govern all quantum computational and communicational tasks within the Q+ATLANTIDE programme.

The eight subsubjects (`000`–`007`) indexed in [`README.md`](./README.md) collectively cover:

- **Quantum States, Density Operators and Mixed States** (`001`) — the representational layer: state vectors, density matrices, pure and mixed states, Bloch sphere, partial trace[^nc2000][^preskill].
- **Quantum Entropy and Information Measures** (`002`) — the quantification layer: von Neumann entropy, quantum relative entropy, mutual information, conditional entropy, Rényi and smooth entropies[^nc2000][^wilde].
- **Quantum Channels and Operations** (`003`) — the transformation layer: CPTP maps, Kraus operators, Stinespring dilation, standard noise channels[^wilde][^watrous].
- **Entanglement Theory and Measures** (`004`) — the correlation layer: separability, Bell and GHZ states, entanglement witnesses, PPT criterion, entanglement measures and monogamy[^nc2000][^wilde].
- **Quantum Coding and Compression** (`005`) — the compression and error-correction layer: Schumacher compression, QECCs, stabiliser and CSS codes, threshold theorem[^nc2000][^wilde].
- **Quantum Channel Capacity and Communication Limits** (`006`) — the capacity layer: classical capacity (HSW/Holevo), quantum capacity (LSD/coherent information), entanglement-assisted and private capacities[^wilde][^watrous].
- **No-Go Theorems and Information-Theoretic Boundaries** (`007`) — the fundamental limits layer: no-cloning, no-deleting, no-broadcasting, no-hiding, Holevo bound, data-processing inequality[^nc2000][^preskill].

## 2. Scope

- Covers the *Quantum Information Theory* slice of the parent code range `900-909`.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- All artefacts in this subsection fall under governance class `restricted` per Note N-006[^n006][^gov].
- Subsequent subsubjects (`001`–`007`) under this subsection extend this Overview with detailed data modules; the full populated set is `001`–`007`, indexed in [`README.md`](./README.md).
- Concepts in scope span the theoretical foundations of quantum information science as formalised in the canonical literature[^nc2000][^wilde][^watrous][^preskill] and the controlled vocabulary of ISO/IEC 4879:2023[^iso4879].
- Out of scope: quantum algorithm design (subsection `905`), quantum hardware and qubit technologies (subsection `901`), quantum error correction implementation (subsection `906`), and quantum cryptography protocols (subsection `907`).

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture (controlled term) |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subsection | `904` — Quantum Information Theory |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/904_Quantum-Information-Theory/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `900-909` row.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `restricted` denotes documents requiring additional governance, evidence packages and access controls (rule N-006[^n006]).

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n002]: **Note N-002** — Architecture bands classify technologies; Q-Divisions provide technical authority; ORB-Functions provide enterprise support. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n006]: **Note N-006 (Restricted bands)** — Quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls. See [`organization/Q+ATLANTIDE.md` §5.3](../../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).

[^nc2000]: **Nielsen, M.A. & Chuang, I.L. — "Quantum Computation and Quantum Information"** (Cambridge University Press, 2000). Canonical reference for quantum states, channels, entropy, entanglement, and information-theoretic bounds.

[^wilde]: **Wilde, M.M. — "Quantum Information Theory"** (2nd ed., Cambridge University Press, 2017). Comprehensive treatment of quantum entropy, channel capacities, and coding theorems.

[^preskill]: **Preskill, J. — "Lecture Notes for Physics 219: Quantum Information and Computation"** (Caltech, 2018). Covers density operators, quantum channels, entanglement measures, and no-go theorems.

[^iso4879]: **ISO/IEC 4879:2023 — Quantum computing — Vocabulary** — Controlled terminology standard for quantum computing concepts used across Q+ATLANTIDE QCSAA artefacts.

[^watrous]: **Watrous, J. — "The Theory of Quantum Information"** (Cambridge University Press, 2018). Formal treatment of quantum states, measurements, channels, and information-theoretic quantities.

### Applicable industry standards

The following standards and foundational texts apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- ISO/IEC 4879:2023 — Quantum computing — Vocabulary[^iso4879]
- Nielsen & Chuang — Quantum Computation and Quantum Information (Cambridge, 2000)[^nc2000]
- Wilde — Quantum Information Theory, 2nd ed. (Cambridge, 2017)[^wilde]
- Watrous — The Theory of Quantum Information (Cambridge, 2018)[^watrous]
- Preskill — Lecture Notes for Physics 219 (Caltech, 2018)[^preskill]
