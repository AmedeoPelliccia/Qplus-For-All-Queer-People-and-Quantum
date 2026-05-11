---
document_id: QATL-ATLAS1000-QCSAA-910-919-01-912-README
title: "QCSAA 910–919 · 01.912 — Variational Quantum Classifiers and Regressors (Subsection Index)"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: QCSAA
architecture_name: "Quantum Computing & Sentient Agency Architecture"
master_range: "900–999"
code_range: "910-919"
section: "01"
section_title: "Quantum Machine Learning e IA Cuántica"
section_title_en: "Quantum Machine Learning and Quantum AI"
subsection: "912"
subsection_title: "Variational Quantum Classifiers and Regressors"
primary_q_division: Q-HPC
support_q_divisions: [Q-HORIZON, Q-DATAGOV]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: restricted
restricted_rule: N-006
evidence_package_id: EP-QCSAA-912-001
access_control_profile: ACP-QCSAA-RESTRICTED
version: 1.0.0
status: active
language: en
---

# QCSAA 910–919 · Section 01 · Subsection 912 — Variational Quantum Classifiers and Regressors

## 1. Purpose

Subsection-level index for *Variational Quantum Classifiers and Regressors* (`912`) within QCSAA `910-919` — *Quantum Machine Learning e IA Cuántica*. Covers the controlled vocabulary and technical standards for variational QML models: parameterized quantum circuits, classification and regression architectures, loss functions and cost landscapes, optimizers and training loops, gradient estimation via the parameter-shift rule, trainability constraints (barren plateaus and noise), benchmarking against classical baselines, and aerospace assurance boundaries.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. Restricted-band governance applies per rule N-006[^n006].

## 2. Scope

- Covers the full subsubject namespace `000`–`010` of subsection `912` *Variational Quantum Classifiers and Regressors*; all eleven subsubjects are populated in this baseline release.
- Inherits Q-Division authority and ORB support from the parent row in [`../README.md` §3](../README.md#3-subsection-index)[^archtable] and the section index in [`../../README.md`](../../README.md).
- Provides the canonical reference for variational QML classifier and regressor models applicable across the QCSAA `910-919` band and the broader Q+ATLANTIDE baseline; downstream QCSAA subsections (`913_Quantum-Kernels`, `916_Hybrid-Quantum-Classical-Neural-Networks`, `917_QML-Trainability`) and cross-cutting aerospace subsystems reference the vocabulary and training-loop definitions established here.
- All subsubjects under this subsection must declare `governance_class: restricted`, `evidence_package_id`, and `access_control_profile` per rule N-006[^n006].

## 3. Subsubject Index

| 00N | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 001 | Variational QML Controlled Definition | [`001_Variational-QML-Controlled-Definition.md`](./001_Variational-QML-Controlled-Definition.md) | active |
| 002 | Parameterized Quantum Circuits | [`002_Parameterized-Quantum-Circuits.md`](./002_Parameterized-Quantum-Circuits.md) | active |
| 003 | Variational Quantum Classifiers | [`003_Variational-Quantum-Classifiers.md`](./003_Variational-Quantum-Classifiers.md) | active |
| 004 | Variational Quantum Regressors | [`004_Variational-Quantum-Regressors.md`](./004_Variational-Quantum-Regressors.md) | active |
| 005 | Loss Functions and Cost Landscapes | [`005_Loss-Functions-and-Cost-Landscapes.md`](./005_Loss-Functions-and-Cost-Landscapes.md) | active |
| 006 | Optimizers and Training Loops | [`006_Optimizers-and-Training-Loops.md`](./006_Optimizers-and-Training-Loops.md) | active |
| 007 | Gradient Estimation and Parameter Shift | [`007_Gradient-Estimation-and-Parameter-Shift.md`](./007_Gradient-Estimation-and-Parameter-Shift.md) | active |
| 008 | Trainability, Barren Plateaus, and Noise | [`008_Trainability-Barren-Plateaus-and-Noise.md`](./008_Trainability-Barren-Plateaus-and-Noise.md) | active |
| 009 | Benchmarking, Classical Baselines, and Validation | [`009_Benchmarking-Classical-Baselines-and-Validation.md`](./009_Benchmarking-Classical-Baselines-and-Validation.md) | active |
| 010 | Aerospace Assurance and Use-Case Boundaries | [`010_Aerospace-Assurance-and-Use-Case-Boundaries.md`](./010_Aerospace-Assurance-and-Use-Case-Boundaries.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `910-919` |
| Section | `01` — Quantum Machine Learning e IA Cuántica |
| Subsection | `912` — Variational Quantum Classifiers and Regressors |
| Subsubject namespace | `000`–`010` (11 subsubjects populated; canonical `00N_*.md` scheme) |
| Primary Q-Division | Q-HPC[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Evidence package | `EP-QCSAA-912-001` |
| Access control profile | `ACP-QCSAA-RESTRICTED` |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/910-919_Quantum-Machine-Learning-e-IA-Cuantica/912_Variational-Quantum-Classifiers-and-Regressors/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = QCSAA`, `primary_q_division = Q-HPC`, and `governance_class = restricted` from this subsection header. Extensions added under future subsubject slots shall preserve those header fields, follow the canonical `00N_*.md` naming scheme, and reuse the footnote set declared below. Per rule N-006[^n006] every document must additionally declare `evidence_package_id` and `access_control_profile`. The No-AAA Rule[^n004] applies.

## 6. Downstream and Cross-Subsection Dependencies

The variational QML vocabulary, circuit structures, and training-loop definitions established in this subsection are consumed by:

- **Within `910-919`** — `910_QML-Foundations-and-Taxonomy/` (variational models as a primary QML paradigm); `911_Quantum-Feature-Maps-and-Embeddings/` (data-encoding layers used as input to variational classifiers); `913_Quantum-Kernels-and-Kernel-Methods/` (kernel alignment and quantum kernel classifiers share parameterized-circuit substrates); `916_Hybrid-Quantum-Classical-Neural-Networks/` (hybrid architectures embed variational layers); `917_QML-Trainability-Barren-Plateaus-and-Optimization/` (trainability analysis extends subsubject `008`); `918_QML-Resource-Estimation-and-Quantum-Advantage-Honesty/` (resource overheads for variational training loops).
- **Across QCSAA `900-999`** — `900-909_Fundamentos/903_Quantum-Algorithms/004_Variational-Quantum-Algorithms` (foundational variational algorithm framework); `902_Circuits/` (parameterized circuit primitives); `919_Aerospace-QML-Use-Cases-and-Assurance-Boundaries/` (deployment of variational classifiers in aerospace scenarios).
- **Across ATLAS `000-099`** — airborne health-monitoring and fault-classification subsystems that adopt variational-classifier outputs trace assurance-boundary requirements back to subsubject `010`.

## 7. Change Log

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0.0 | 2026-05-07 | Q+ Team/Amedeo Pelliccia + AI | Initial baseline: `000_Overview.md` plus subsubjects `001`–`010`, using the sequential `00N_*.md` scheme under the `912_Variational-Quantum-Classifiers-and-Regressors/` subsection. Subsection index established. |

## 8. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Subsection Index (parent)** — [`../README.md` §3](../README.md#3-subsection-index). Authoritative source for the `910-919` subsection listing and Q-Division authority.

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `restricted` denotes documents requiring additional governance, evidence packages and access controls (rule N-006[^n006]).

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n006]: **Note N-006 (Restricted bands)** — Quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls. Templates must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`. See [`organization/Q+ATLANTIDE.md` §5.3](../../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).

[^ieee7130]: **IEEE Std 7130-2023 — IEEE Standard for Quantum Computing Definitions** — Establishes a common vocabulary for quantum computing terms including parameterized circuits and variational algorithms used throughout this subsection.

[^iso4879]: **ISO/IEC 4879:2023 — Quantum computing — Terminology and vocabulary** — International standard defining foundational quantum-computing concepts and terms adopted across this subsection.

[^easa2023]: **EASA AI Roadmap 2.0 (2023)** — EASA framework for assurance of AI/ML-based systems in aviation; applicable to variational-classifier outputs consumed by airborne subsystems.

### Applicable standards

The following standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- IEEE Std 7130-2023 — IEEE Standard for Quantum Computing Definitions[^ieee7130]
- ISO/IEC 4879:2023 — Quantum computing — Terminology and vocabulary[^iso4879]
- EASA AI Roadmap 2.0 (2023)[^easa2023]
