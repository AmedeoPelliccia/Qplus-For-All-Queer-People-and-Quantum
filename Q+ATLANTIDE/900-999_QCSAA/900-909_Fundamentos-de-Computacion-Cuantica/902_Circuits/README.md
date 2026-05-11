---
document_id: QATL-ATLAS1000-QCSAA-900-909-902-README
title: "QCSAA 900–909 · 902 — Circuits (Subsection Index)"
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
subsection: "902"
subsection_title: "Circuits"
primary_q_division: Q-HORIZON
support_q_divisions: [Q-HPC, Q-DATAGOV]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: restricted
restricted_rule: N-006
version: 1.0.0
status: active
language: en
---

# QCSAA 900–909 · Section 00 · Subsection 902 — Circuits

## 1. Purpose

Subsection-level index for *Circuits* (`902`) within QCSAA `900-909` — *Fundamentos de Computación Cuántica*. Covers the definition and composition of quantum circuits, structural metrics (depth, width, parallelism), measurement and classical control, circuit optimisation and transpilation for physical hardware, and noise-resilient patterns for NISQ-era practice.

This subsection is part of the **ATLAS-1000** register, a subpart of the controlled **Q+ATLANTIDE** baseline[^baseline][^n001].

**Restricted band (N-006[^n006]).** All documents under this subsection declare `governance_class: restricted`, `evidence_package_id`, and `access_control_profile`.

## 2. Scope

- Covers the full subsubject namespace `000`–`009` of subsection `902` *Circuits*; subsubjects `001`–`005` are populated in this baseline release, slots `006`–`009` remain available for future extension.
- Inherits Q-Division authority and ORB support from the parent section index in [`../README.md`](../README.md) and the parent architecture row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Establishes the controlled quantum-circuit vocabulary used across the QCSAA `900-909` band: every algorithm (`903_`), information-theory (`904_`), and complexity (`905_`) document that references a circuit model traces definitions back here.

## 3. Subsubject Index

| 00N | Title | Document | Status |
|---:|---|---|---|
| 000 | Overview | [`000_Overview.md`](./000_Overview.md) | active |
| 001 | Circuit Definition and Composition | [`001_Circuit-Definition-and-Composition.md`](./001_Circuit-Definition-and-Composition.md) | active |
| 002 | Circuit Depth, Width, and Parallelism | [`002_Circuit-Depth-Width-and-Parallelism.md`](./002_Circuit-Depth-Width-and-Parallelism.md) | active |
| 003 | Measurement, Mid-Circuit, and Classical Control | [`003_Measurement-Mid-Circuit-and-Classical-Control.md`](./003_Measurement-Mid-Circuit-and-Classical-Control.md) | active |
| 004 | Circuit Optimization, Compilation, and Transpilation | [`004_Circuit-Optimization-Compilation-and-Transpilation.md`](./004_Circuit-Optimization-Compilation-and-Transpilation.md) | active |
| 005 | Noise-Resilient Circuit Patterns and NISQ Practice | [`005_Noise-Resilient-Circuit-Patterns-and-NISQ-Practice.md`](./005_Noise-Resilient-Circuit-Patterns-and-NISQ-Practice.md) | active |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subsection | `902` — Circuits |
| Subsubject namespace | `000`–`009` (`000` + `001`–`005` populated; canonical `00N_*.md` scheme) |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/902_Circuits/` |
| Document | `README.md` (this file) |
| Parent section | [`../README.md`](../README.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. Governance

Governed by [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md)[^baseline]. All subsubjects under this subsection inherit `architecture_code = QCSAA`, `primary_q_division = Q-HORIZON`, and `governance_class = restricted` from this subsection header. Extensions added under slots `006`–`009` shall preserve those header fields, follow the canonical `00N_*.md` naming scheme, and declare `evidence_package_id` and `access_control_profile` per rule N-006[^n006]. The No-AAA Rule[^n004] applies.

## 6. Downstream and Cross-Subsection Dependencies

The circuit vocabulary defined in this subsection is consumed by:

- **Within `900-909`** — `903_Quantum-Algorithms/` (every algorithm is expressed as a parameterised circuit); `904_Quantum-Information-Theory/` (quantum channel and code constructions reference circuit diagrams); `905_Quantum-Complexity-and-Resource-Theory/` (complexity classes are defined relative to circuit families and depth bounds).
- **Across QCSAA `900–999`** — `910-919_Quantum-Machine-Learning` (variational quantum circuits); `920-929_Redes-y-Comunicaciones-Cuanticas` (quantum network protocols implemented as circuits); `930-939_Ciberseguridad-Cuantica` (quantum-cryptographic circuits and QKD implementations).

## 7. Change Log

| Version | Date | Author | Notes |
|---|---|---|---|
| 1.0.0 | 2026-05-07 | Q+ Team/Amedeo Pelliccia + AI | Initial baseline: `000_Overview.md` plus subsubjects `001`–`005`, using the sequential `00N_*.md` scheme under the `902_Circuits/` subsection. Subsection index established. |

## 8. References & Citations

[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **§3 — Architecture Table (parent)** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `900-909` row (Section `00` — Fundamentos de Computación Cuántica, Primary Q-Division Q-HORIZON).

[^qdiv]: **Q-Division authority** — [`organization/Q-Divisions/`](../../../../organization/Q-Divisions/). Technical-authority units for the Q+ATLANTIDE baseline.

[^gov]: **Governance class** — `restricted` denotes documents requiring additional governance, evidence packages and access controls (rule N-006[^n006]).

[^n001]: **Note N-001** — Q+ATLANTIDE (with its ATLAS-1000 register subpart) is a taxonomy and traceability ecosystem, not an organisation chart. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n004]: **Note N-004 (No-AAA Rule)** — "AAA" is not a valid domain, division, architecture, interface or function in this baseline. See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^n006]: **Note N-006 (Restricted bands)** — Quantum-related (`900-999` QCSAA) bands require additional governance, evidence packages and access controls beyond the baseline trace record. Templates must additionally declare `governance_class: restricted`, `evidence_package_id` and `access_control_profile`. See [`organization/Q+ATLANTIDE.md` §5.3](../../../../organization/Q+ATLANTIDE.md#53-restricted-band-templates-n-006).

### Applicable standards

The following standards are applicable to this subsection in addition to the cross-cutting Q+ATLANTIDE governance:

- IEEE Std 7130-2023 — IEEE Standard for Quantum Computing Definitions[^ieee7130]
- ISO/IEC 4879:2023 — Quantum computing — Concepts and terminology[^iso4879]
- OpenQASM 3.0 — Open Quantum Assembly Language specification[^openqasm3]

[^ieee7130]: **IEEE Std 7130-2023 — IEEE Standard for Quantum Computing Definitions** — Establishes a common vocabulary for quantum computing, including circuit, gate, qubit, and measurement terminology.

[^iso4879]: **ISO/IEC 4879:2023 — Quantum computing — Concepts and terminology** — International standard defining foundational quantum-computing concepts and terms adopted across this subsection.

[^openqasm3]: **OpenQASM 3.0 — Open Quantum Assembly Language** — Industry-standard intermediate representation for quantum circuits; reference specification for circuit syntax, mid-circuit measurement, and classical control flow.
