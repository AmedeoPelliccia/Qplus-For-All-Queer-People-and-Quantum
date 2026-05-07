---
document_id: QATL-ATLAS-1000-QCSAA-910-919-01-911-000-OVERVIEW
title: "QCSAA 910–919 · 01.911.000 — Quantum Feature Maps and Embeddings (Overview)"
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
subsection: "911"
subsection_title: "Quantum Feature Maps and Embeddings"
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

# QCSAA 910–919 · Section 01 · Subsection 911 — Quantum Feature Maps and Embeddings

## 1. Purpose

Overview entry-point for the *Quantum Feature Maps and Embeddings* subsection within the `910-919` code range (Section `01` — *Quantum Machine Learning e IA Cuántica*) of the **QCSAA** architecture band (*Quantum Computing & Sentient Agency Architecture*, master range `900–999`).

This subsubject (`000 Overview`) introduces the QCSAA 910-919.911.000 slice and links it to the controlled Q+ATLANTIDE baseline[^baseline] and to the applicable standards listed in §4. It establishes the controlled vocabulary for **quantum feature maps**, **quantum embeddings**, and the full taxonomy of classical-to-quantum data encoding strategies — vocabulary that every downstream QML subsection (quantum kernels, VQCs, hybrid networks, barren plateaus) depends on when specifying how classical data enters a quantum computational pipeline.

A **quantum feature map** is a parameterised unitary U(x) that lifts a classical input vector x ∈ ℝⁿ into a quantum state |φ(x)⟩ = U(x)|0⟩ living in a high-dimensional Hilbert space ℋ[^havlicek]. A **quantum embedding** is the complete specification — encoding circuit plus Hilbert space — that maps an entire classical dataset into a quantum state space amenable to learning[^lloyd2020]. The choice of embedding determines which kernel function is implicitly computed by a quantum model[^schuld2021], making the design of feature maps and embeddings one of the most consequential decisions in quantum machine learning.

**Restricted band (N-006[^n006]).** This document inherits `governance_class: restricted` and must be accompanied by a declared `evidence_package_id` and `access_control_profile`.

## 2. Scope

- Covers the *Quantum Feature Maps and Embeddings* slice of the parent code range `910-919`.
- Inherits Q-Division authority and ORB support from the parent row in [`README.md`](./README.md)[^archtable].
- Subsequent subsubjects (`001`–`010`) under this subsection extend this Overview with detailed data modules; the populated set in this baseline is `001`–`010`, indexed in [`README.md`](./README.md).
- Concepts in scope across the subsection:
  - **Feature Map Controlled Definition** (`001`) — the formal definition φ(x) = U(x)|0⟩⟨0|U(x)†, the induced kernel κ(x,y) = |⟨φ(x)|φ(y)⟩|², and the distinction from classical kernel methods[^havlicek][^schuld2019].
  - **Embedding Controlled Definition** (`002`) — distinction between embedding (circuit + Hilbert space + readout) and feature map (purely the encoding unitary), data re-uploading, inductive bias, and the representational power theorem[^lloyd2020].
  - **Classical to Quantum Data Encoding** (`003`) — full taxonomy of encoding strategies (basis, amplitude, angle, IQP/product, data-reuploading) with circuit-depth and qubit-count tradeoffs[^schuld2019].
  - **Basis Encoding** (`004`) — mapping binary strings b ∈ {0,1}ⁿ to computational basis states |b⟩ via selective X gates; QRAM model; O(n) qubit and depth requirements.
  - **Amplitude Encoding** (`005`) — exponential compression mapping normalised vectors x ∈ ℝ^(2ⁿ) to |ψ⟩ = Σᵢ xᵢ|i⟩ in n qubits; state preparation circuit depth tradeoffs and QRAM-assisted approaches.
  - **Angle Encoding** (`006`) — product states ⊗ᵢ R(xᵢ)|0⟩ via single-qubit rotation gates Rx/Ry/Rz; O(1) circuit depth per layer; limited expressibility and data re-uploading extensions.
  - **IQP and Hardware-Efficient Feature Maps** (`007`) — IQP diagonal circuits (Havlíček et al. ZZFeatureMap), hardware-native decompositions, depth–expressibility tradeoffs, and the classical-simulation hardness claim[^havlicek].
  - **Kernel-Induced Feature Spaces** (`008`) — quantum kernel κ(x,y) estimation via SWAP test or destructive SWAP; positive-semidefiniteness; kernel SVM training; geometric difference metric for quantum advantage[^schuld2021].
  - **Expressibility, Trainability and Noise** (`009`) — the tension between expressibility (Sim et al. frame potential distance), trainability (barren plateaus), and noise-induced fidelity degradation; mitigation strategies.
  - **Aerospace Data Embedding Boundaries** (`010`) — sensor dimensionality constraints, real-time latency budgets, NISQ depth limits, DO-178C / ARP4754A alignment, and the no-certification boundary for safety-critical QML inference.

## 3. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `910-919` |
| Section | `01` — Quantum Machine Learning e IA Cuántica |
| Subsection | `911` — Quantum Feature Maps and Embeddings |
| Subsubject | `000` — Overview |
| Primary Q-Division | Q-HPC[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/910-919_Quantum-Machine-Learning-e-IA-Cuantica/911_Quantum-Feature-Maps-and-Embeddings/` |
| Document | `000_Overview.md` (this file) |
| Parent subsection | [`README.md`](./README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 4. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Subsubject Index (parent README)** — [`README.md` §3](./README.md#3-subsubject-index). Authoritative source for the `911` subsection row (Primary Q-Division Q-HPC).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `restricted` denotes documents requiring additional governance, evidence packages and access controls (rule N-006[^n006]).

[^n006]: **Note N-006 (Restricted bands)** — Quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls. Templates must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`. See [`organization/Q+ATLANTIDE.md` §5.3](../../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).

[^havlicek]: **Havlíček, V., Córcoles, A. D., Temme, K., et al. (2019)** — "Supervised learning with quantum-enhanced feature spaces." *Nature*, 567, 209–212. Introduces quantum feature maps and kernel-based classification, demonstrating the ZZFeatureMap construction for near-term devices.

[^schuld2019]: **Schuld, M. & Killoran, N. (2019)** — "Quantum Machine Learning in Feature Hilbert Spaces." *Physical Review Letters*, 122, 040504. Formulates quantum ML as function approximation in feature Hilbert spaces, establishing the connection between quantum circuits and kernel methods.

[^schuld2021]: **Schuld, M. (2021)** — "Supervised quantum machine learning models are kernel methods." arXiv:2101.11020. Establishes the formal equivalence between quantum models and kernel methods.

[^lloyd2020]: **Lloyd, S., Schuld, M., Ijaz, A., Izaac, J., & Killoran, N. (2020)** — "Quantum embeddings for machine learning." arXiv:2001.03622. Defines quantum embeddings and their role in separating data classes in Hilbert space through metric learning.

[^isoiec4879]: **ISO/IEC 4879:2023** — *Quantum computing — Vocabulary*. International standard defining quantum computing terms including quantum state, unitary operation, and quantum circuit.

### Applicable standards

The following standards apply to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- Havlíček et al. (2019) — "Supervised learning with quantum-enhanced feature spaces"[^havlicek]
- Schuld & Killoran (2019) — "Quantum Machine Learning in Feature Hilbert Spaces"[^schuld2019]
- Schuld (2021) — "Supervised quantum machine learning models are kernel methods"[^schuld2021]
- Lloyd et al. (2020) — "Quantum embeddings for machine learning"[^lloyd2020]
- ISO/IEC 4879:2023 — *Quantum computing — Vocabulary*[^isoiec4879]
