---
document_id: QATL-ATLAS-1000-QCSAA-910-919-01-910-README
title: "QCSAA 910–919 · 01.910 — QML Foundations and Taxonomy (Subsection Index)"
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
subsection: "910"
subsection_title: "QML Foundations and Taxonomy"
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

Subsection-level index for *QML Foundations and Taxonomy* (`910`) within QCSAA `910-919` — *Quantum Machine Learning e IA Cuántica*. Establishes the controlled vocabulary, taxonomy, and boundary conditions of Quantum Machine Learning (QML): its definition, a four-quadrant model taxonomy, the classical–quantum boundary, the quantum-data vs. classical-data distinction, data-encoding and feature-map strategies, model families, hybrid architectures, trainability constraints, benchmarking discipline, and aerospace assurance boundaries.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001]. It constitutes the mandatory terminological and taxonomic entry-point that all downstream QML subsections (`911`–`919`) and any aerospace QML application must reference.

**Restricted band (N-006[^n006]).** All documents under this subsection additionally inherit `governance_class: restricted` and must declare `evidence_package_id` and `access_control_profile`.

## 2. Scope

- Covers the full subsubject namespace `000`–`010` of subsection `910` *QML Foundations and Taxonomy*; all eleven slots (`000`–`010`) are populated in this baseline release.
- Inherits Q-Division authority and ORB support from the parent row in [`../README.md` §3](../README.md#3-subsection-index)[^archtable] and the section index in [`../../README.md`](../../README.md).
- Establishes the canonical QML vocabulary — controlled definition, taxonomy quadrants, data types, feature maps, model families, and claim-discipline rules — used by every downstream QCSAA `910-919` subsection and by aerospace system-assurance documents that interface with QML components.

## 3. Subsubject Index

| 00N | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 001 | QML Controlled Definition | [`001_QML-Controlled-Definition.md`](./001_QML-Controlled-Definition.md) | active |
| 002 | QML Taxonomy | [`002_QML-Taxonomy.md`](./002_QML-Taxonomy.md) | active |
| 003 | Classical ML vs QML Boundary | [`003_Classical-ML-vs-QML-Boundary.md`](./003_Classical-ML-vs-QML-Boundary.md) | active |
| 004 | Quantum Data vs Classical Data | [`004_Quantum-Data-vs-Classical-Data.md`](./004_Quantum-Data-vs-Classical-Data.md) | active |
| 005 | Feature Maps and Data Encoding | [`005_Feature-Maps-and-Data-Encoding.md`](./005_Feature-Maps-and-Data-Encoding.md) | active |
| 006 | QML Model Families | [`006_QML-Model-Families.md`](./006_QML-Model-Families.md) | active |
| 007 | Hybrid Quantum-Classical Architecture | [`007_Hybrid-Quantum-Classical-Architecture.md`](./007_Hybrid-Quantum-Classical-Architecture.md) | active |
| 008 | Trainability, Noise and Barren Plateaus | [`008_Trainability-Noise-and-Barren-Plateaus.md`](./008_Trainability-Noise-and-Barren-Plateaus.md) | active |
| 009 | Benchmarking and Claim Discipline | [`009_Benchmarking-and-Claim-Discipline.md`](./009_Benchmarking-and-Claim-Discipline.md) | active |
| 010 | Aerospace Assurance Boundaries | [`010_Aerospace-Assurance-Boundaries.md`](./010_Aerospace-Assurance-Boundaries.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `910-919` |
| Section | `01` — Quantum Machine Learning e IA Cuántica |
| Subsection | `910` — QML Foundations and Taxonomy |
| Subsubject namespace | `000`–`010` (all 11 slots populated; canonical `00N_*.md` scheme) |
| Primary Q-Division | Q-HPC[^qdiv] |
| Support Q-Divisions | Q-HORIZON, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/910-919_Quantum-Machine-Learning-e-IA-Cuantica/910_QML-Foundations-and-Taxonomy/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = QCSAA`, `primary_q_division = Q-HPC` and `governance_class = restricted` from the parent QCSAA section. Extensions added under future slots shall preserve those header fields, follow the canonical `00N_*.md` naming scheme, reuse the footnote set declared below, and additionally declare `evidence_package_id` and `access_control_profile` per rule N-006[^n006]. The No-AAA Rule[^n004] applies.

## 6. Downstream and Cross-Subsection Dependencies

The QML vocabulary, taxonomy, and claim-discipline rules defined in this subsection are consumed by:

- **Within `910-919`** — `911_Quantum-Feature-Maps-and-Embeddings/` (implements the encoding strategies catalogued in `005`), `912_Variational-Quantum-Classifiers-and-Regressors/` (instantiates model families from `006`), `913_Quantum-Kernels-and-Kernel-Methods/` (applies quantum feature-space theory from `005` and `006`), `914_Quantum-Generative-Models/` (extends model taxonomy from `006`), `915_Quantum-Reinforcement-Learning/` (applies hybrid architecture patterns from `007`), `916_Hybrid-Quantum-Classical-Neural-Networks/` (realises the hybrid architectures of `007`), `917_QML-Trainability-Barren-Plateaus-and-Optimization/` (expands the trainability and barren-plateau treatment of `008`), `918_QML-Resource-Estimation-and-Quantum-Advantage-Honesty/` (applies the benchmarking and claim-discipline rules of `009`), `919_Aerospace-QML-Use-Cases-and-Assurance-Boundaries/` (operationalises the aerospace assurance framework of `010`).
- **Across QCSAA `900–999`** — any subsection referencing a quantum learning model, a variational circuit, or a quantum-advantage claim traces its definitional authority back to this subsection.

## 7. Change Log

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0.0 | 2026-05-07 | Q-HPC | Initial baseline: `000_Overview.md` plus subsubjects `001`–`010`, using the sequential `00N_*.md` scheme under the `910_QML-Foundations-and-Taxonomy/` subsection. Subsection index established. |

## 8. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Subsection Index (parent section)** — [`../README.md` §3](../README.md#3-subsection-index). Authoritative source for the `910-919` row (Section `01` — Quantum Machine Learning e IA Cuántica, Primary Q-Division Q-HPC).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `restricted` denotes documents requiring additional governance, evidence packages and access controls (rule N-006[^n006]).

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organization chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n002]: **Note N-002** — Architecture bands classify technologies; Q-Divisions provide technical authority; ORB-Functions provide enterprise support. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n006]: **Note N-006 (Restricted bands)** — Quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls beyond the baseline trace record. Templates must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`. See [`organization/Q+ATLANTIDE.md` §5.3](../../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).

[^biamonte]: **Biamonte, J. et al. (2017)** — "Quantum machine learning." *Nature*, 549, 195–202. Foundational survey introducing the four-quadrant CC/CQ/QC/QQ taxonomy of quantum–classical learning models.

[^schuld2021]: **Schuld, M. & Petruccione, F. (2021)** — *Machine Learning with Quantum Computers*. Springer. Systematic treatment of QML algorithms, feature maps, variational circuits, and quantum kernels.

[^cerezo2021]: **Cerezo, M. et al. (2021)** — "Variational quantum algorithms." *Nature Reviews Physics*, 3, 625–644. Comprehensive review of VQAs including trainability, barren plateaus, and near-term applicability.

[^mcclean2018]: **McClean, J. R. et al. (2018)** — "Barren plateaus in quantum neural network training landscapes." *Nature Communications*, 9, 4812. Identifies the exponential gradient vanishing phenomenon in random quantum circuits.

[^isoiec4879]: **ISO/IEC 4879:2023** — *Quantum computing — Vocabulary*. International standard defining terms and concepts used in quantum computing, providing the normative vocabulary base for QML definitions.
