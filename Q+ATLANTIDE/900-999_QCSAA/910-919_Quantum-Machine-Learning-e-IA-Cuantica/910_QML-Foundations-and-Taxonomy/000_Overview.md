---
document_id: QATL-ATLAS-1000-QCSAA-910-919-01-910-000-OVERVIEW
title: "QCSAA 910–919 · 01.910.000 — QML Foundations and Taxonomy"
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
subsection: "910"
subsection_title: "QML Foundations and Taxonomy"
subsubject: "000"
subsubject_title: "Overview"
primary_q_division: Q-HPC
support_q_divisions: [Q-HORIZON, Q-DATAGOV]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: restricted
restricted_rule: N-006
version: 1.0.0
status: active
language: en
---

# QCSAA 910–919 · Section 01 · Subsection 910 — QML Foundations and Taxonomy

## 1. Purpose

Overview entry-point for the *QML Foundations and Taxonomy* subsection within the `910-919` code range (Section `01` — *Quantum Machine Learning e IA Cuántica*) of the **QCSAA** architecture band (*Quantum Computing & Sentient Agency Architecture*, master range `900–999`).

This subsubject (`000 Overview`) introduces the QCSAA 910-919.910.000 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable standards listed in §4. It establishes the controlled QML vocabulary and taxonomy framework — definition, model quadrants, data types, encoding strategies, model families, hybrid architectures, trainability limits, benchmarking discipline, and aerospace assurance boundaries — that every subsequent QCSAA `910-919` subsection depends on.

**Restricted band (N-006[^n006]).** This document inherits `governance_class: restricted` and must be accompanied by a declared `evidence_package_id` and `access_control_profile`.

## 2. Scope

- Covers the *QML Foundations and Taxonomy* slice of the parent code range `910-919`.
- Inherits Q-Division authority and ORB support from the parent row in [`../README.md`](../README.md)[^archtable].
- All subsubjects (`001`–`010`) under this subsection extend this Overview with detailed data modules; the full set is indexed in [`README.md`](./README.md).
- Concepts in scope across the subsection:
  - **QML Controlled Definition** (`001`) — a hardware-anchored definition of QML that excludes loosely quantum-inspired classical algorithms, establishes the scope of genuine quantum advantage, and prevents premature claims.
  - **QML Taxonomy** (`002`) — the four-quadrant CC/CQ/QC/QQ taxonomy from Biamonte et al.[^biamonte] classifying algorithms by whether the data processing and the learning model are classical (C) or quantum (Q).
  - **Classical ML vs QML Boundary** (`003`) — empirical and theoretical criteria for determining when a QML approach is appropriate over a classical baseline, including complexity-theoretic conditions and practical NISQ constraints.
  - **Quantum Data vs Classical Data** (`004`) — distinction between natively quantum data (from quantum sensors, quantum processes, or quantum simulations) and classical data encoded into quantum states, with implications for advantage claims.
  - **Feature Maps and Data Encoding** (`005`) — data-loading strategies for quantum processors: basis encoding, amplitude encoding, angle encoding, IQP circuits, and their respective depth, fidelity, and expressibility trade-offs.
  - **QML Model Families** (`006`) — taxonomy of concrete QML model types: variational quantum classifiers/regressors (VQC), quantum kernel methods (QKM), quantum neural networks (QNN), quantum generative adversarial networks (QGAN), and quantum reinforcement learning (QRL).
  - **Hybrid Quantum-Classical Architecture** (`007`) — the variational quantum eigensolver (VQE) / quantum approximate optimisation algorithm (QAOA) hybrid loop, parameter-shift rule for gradient estimation, classical optimiser interface, and shot-budget management.
  - **Trainability, Noise and Barren Plateaus** (`008`) — the barren-plateau phenomenon in random quantum circuits[^mcclean2018], noise-induced concentration, localised cost functions as mitigations, and hardware-efficient ansatz design constraints.
  - **Benchmarking and Claim Discipline** (`009`) — controlled rules for comparing QML models against classical baselines, reporting quantum advantage honestly, selecting representative datasets, and avoiding benchmark gaming.
  - **Aerospace Assurance Boundaries** (`010`) — EASA AI Roadmap alignment, DO-178C/DO-254 interface requirements, TRL gating for QML components, and the DAL/assurance level framework applied to quantum-augmented functions.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `910-919` |
| Section | `01` — Quantum Machine Learning e IA Cuántica |
| Subsection | `910` — QML Foundations and Taxonomy |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-HPC[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/910-919_Quantum-Machine-Learning-e-IA-Cuantica/910_QML-Foundations-and-Taxonomy/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Subsubject Index (parent README)** — [`README.md` §3](./README.md#3-subsubject-index). Authoritative source for the `910` subsection row (Subsection `910` — QML Foundations and Taxonomy, Primary Q-Division Q-HPC).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `restricted` denotes documents requiring additional governance, evidence packages and access controls (rule N-006[^n006]).

[^n006]: **Note N-006 (Restricted bands)** — Quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls. Templates must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`. See [`organization/Q+ATLANTIDE.md` §5.3](../../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).

[^biamonte]: **Biamonte, J. et al. (2017)** — "Quantum machine learning." *Nature*, 549, 195–202. Introduces the CC/CQ/QC/QQ quadrant taxonomy and surveys near-term quantum ML prospects.

[^schuld2021]: **Schuld, M. & Petruccione, F. (2021)** — *Machine Learning with Quantum Computers*. Springer. Systematic treatment of QML algorithms, feature maps, variational circuits, and quantum kernels.

[^cerezo2021]: **Cerezo, M. et al. (2021)** — "Variational quantum algorithms." *Nature Reviews Physics*, 3, 625–644. Comprehensive review of variational quantum algorithms covering trainability, barren plateaus, and NISQ applicability.

[^mcclean2018]: **McClean, J. R. et al. (2018)** — "Barren plateaus in quantum neural network training landscapes." *Nature Communications*, 9, 4812. Identifies exponential gradient vanishing in random quantum circuits.

[^isoiec4879]: **ISO/IEC 4879:2023** — *Quantum computing — Vocabulary*. International standard defining terms and concepts used in quantum computing.

### Applicable standards

The following standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- Biamonte et al. (2017) — "Quantum machine learning"[^biamonte]
- Schuld & Petruccione (2021) — *Machine Learning with Quantum Computers*[^schuld2021]
- Cerezo et al. (2021) — "Variational quantum algorithms"[^cerezo2021]
- McClean et al. (2018) — "Barren plateaus in quantum neural network training landscapes"[^mcclean2018]
- ISO/IEC 4879:2023 — *Quantum computing — Vocabulary*[^isoiec4879]
