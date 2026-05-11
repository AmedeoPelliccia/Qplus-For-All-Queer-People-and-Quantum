---
document_id: QATL-ATLAS-1000-QCSAA-910-919-01-911-README
title: "QCSAA 910–919 · 01.911 — Quantum Feature Maps and Embeddings (Subsection Index)"
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
subsection: "911"
subsection_title: "Quantum Feature Maps and Embeddings"
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

Subsection-level index for *Quantum Feature Maps and Embeddings* (`911`) within QCSAA `910-919` — *Quantum Machine Learning e IA Cuántica*. Covers the encoding of classical data into quantum state spaces: controlled definitions of feature maps and embeddings, classical-to-quantum data encoding strategies (basis, amplitude, angle), IQP and hardware-efficient circuits, kernel-induced feature spaces, expressibility and trainability tradeoffs, and aerospace data embedding constraints.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It is the foundational encoding reference for all QML subsections that consume a feature map or embedding as an input primitive — including quantum kernel methods, variational quantum classifiers, hybrid neural networks, and trainability analysis.

**Restricted band (N-006[^n006]).** All documents under this subsection additionally inherit `governance_class: restricted` and must declare `evidence_package_id` and `access_control_profile`.

## 2. Scope

- Covers the full subsubject namespace `000`–`019` of subsection `911` *Quantum Feature Maps and Embeddings*; subsubjects `000`–`010` are populated in this baseline release, slots `011`–`019` remain available for future extension.
- Inherits Q-Division authority and ORB support from the parent row in [`../README.md` §3](../README.md#3-subsection-index)[^archtable] and the section index in [`../../README.md`](../../README.md).
- Establishes the controlled vocabulary for quantum feature maps, quantum embeddings, and the full taxonomy of classical-to-quantum encoding strategies — vocabulary that every downstream QCSAA QML subsection depends on when specifying how classical data enters a quantum circuit.

## 3. Subsubject Index

| 00N | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 001 | Feature Map Controlled Definition | [`001_Feature-Map-Controlled-Definition.md`](./001_Feature-Map-Controlled-Definition.md) | active |
| 002 | Embedding Controlled Definition | [`002_Embedding-Controlled-Definition.md`](./002_Embedding-Controlled-Definition.md) | active |
| 003 | Classical to Quantum Data Encoding | [`003_Classical-to-Quantum-Data-Encoding.md`](./003_Classical-to-Quantum-Data-Encoding.md) | active |
| 004 | Basis Encoding | [`004_Basis-Encoding.md`](./004_Basis-Encoding.md) | active |
| 005 | Amplitude Encoding | [`005_Amplitude-Encoding.md`](./005_Amplitude-Encoding.md) | active |
| 006 | Angle Encoding | [`006_Angle-Encoding.md`](./006_Angle-Encoding.md) | active |
| 007 | IQP and Hardware-Efficient Feature Maps | [`007_IQP-and-Hardware-Efficient-Feature-Maps.md`](./007_IQP-and-Hardware-Efficient-Feature-Maps.md) | active |
| 008 | Kernel-Induced Feature Spaces | [`008_Kernel-Induced-Feature-Spaces.md`](./008_Kernel-Induced-Feature-Spaces.md) | active |
| 009 | Expressibility, Trainability and Noise | [`009_Expressibility-Trainability-and-Noise.md`](./009_Expressibility-Trainability-and-Noise.md) | active |
| 010 | Aerospace Data Embedding Boundaries | [`010_Aerospace-Data-Embedding-Boundaries.md`](./010_Aerospace-Data-Embedding-Boundaries.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `910-919` |
| Section | `01` — Quantum Machine Learning e IA Cuántica |
| Subsection | `911` — Quantum Feature Maps and Embeddings |
| Subsubject namespace | `000`–`019` (`000` + `001`–`010` populated; canonical `00N_*.md` scheme) |
| Primary Q-Division | Q-HPC[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/910-919_Quantum-Machine-Learning-e-IA-Cuantica/911_Quantum-Feature-Maps-and-Embeddings/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = QCSAA`, `primary_q_division = Q-HPC` and `governance_class = restricted` from the parent QCSAA section. Extensions added under slots `011`–`019` shall preserve those header fields, follow the canonical `00N_*.md` naming scheme, reuse the footnote set declared below, and additionally declare `evidence_package_id` and `access_control_profile` per rule N-006[^n006]. The No-AAA Rule[^n004] applies.

## 6. Downstream and Cross-Subsection Dependencies

The feature map and embedding vocabulary, encoding strategy taxonomy, and aerospace boundary conditions defined in this subsection are consumed by:

- **Within `910-919`** — `913_Quantum-Kernels-and-Kernel-Methods/` (quantum kernel methods use the inner product κ(x,y) = |⟨φ(x)|φ(y)⟩|² induced by the feature maps defined here); `912_Variational-Quantum-Classifiers-and-Regressors/` (VQC classifiers use angle and amplitude encoding layers as their data-input stage); `916_Hybrid-Quantum-Classical-Neural-Networks/` (hybrid architectures rely on embedding layers defined here to interface classical data pipelines with quantum circuits); `910_QML-Foundations-and-Taxonomy/` (the taxonomy overview references feature maps and embeddings as a core QML primitive).
- **Across QCSAA `900–999`** — `917_QML-Trainability-Barren-Plateaus-and-Optimization/` (trainability properties of a QML model depend critically on encoding expressibility as defined in `009_`); `918_QML-Resource-Estimation-and-Quantum-Advantage-Honesty/` (resource accounting for state preparation and encoding circuits traces back to the complexity bounds established here); `919_Aerospace-QML-Use-Cases-and-Assurance-Boundaries/` (aerospace use-case certification inherits the DO-178C and ARP4754A alignment from `010_Aerospace-Data-Embedding-Boundaries.md`).

## 7. Change Log

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0.0 | 2026-05-07 | Q+ Team/Amedeo Pelliccia + AI | Initial baseline release: `000_Overview.md` plus subsubjects `001`–`010`, using the sequential `00N_*.md` scheme under the `911_Quantum-Feature-Maps-and-Embeddings/` subsection. Subsection index established. |

## 8. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Subsection Index (parent section)** — [`../README.md` §3](../README.md#3-subsection-index). Authoritative source for the `910-919` row (Section `01` — Quantum Machine Learning e IA Cuántica, Primary Q-Division Q-HPC).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — `restricted` denotes documents requiring additional governance, evidence packages and access controls (rule N-006[^n006]).

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n002]: **Note N-002** — Architecture bands classify technologies; Q-Divisions provide technical authority; ORB-Functions provide enterprise support. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n006]: **Note N-006 (Restricted bands)** — Quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls beyond the baseline trace record. Templates must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`. See [`organization/Q+ATLANTIDE.md` §5.3](../../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).

[^havlicek]: **Havlíček, V., Córcoles, A. D., Temme, K., et al. (2019)** — "Supervised learning with quantum-enhanced feature spaces." *Nature*, 567, 209–212. Introduces quantum feature maps and kernel-based classification, demonstrating the ZZFeatureMap construction for near-term devices.

[^schuld2019]: **Schuld, M. & Killoran, N. (2019)** — "Quantum Machine Learning in Feature Hilbert Spaces." *Physical Review Letters*, 122, 040504. Formulates quantum ML as function approximation in feature Hilbert spaces, establishing the connection between quantum circuits and kernel methods.

[^schuld2021]: **Schuld, M. (2021)** — "Supervised quantum machine learning models are kernel methods." arXiv:2101.11020. Establishes the formal equivalence between quantum models and kernel methods, showing that all quantum models with a fixed embedding implicitly compute a kernel.

[^isoiec4879]: **ISO/IEC 4879:2023** — *Quantum computing — Vocabulary*. International standard defining quantum computing terms including quantum state, unitary operation, and quantum circuit.
