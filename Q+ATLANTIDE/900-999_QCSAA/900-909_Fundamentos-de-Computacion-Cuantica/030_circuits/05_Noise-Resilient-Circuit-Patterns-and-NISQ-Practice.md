---
document_id: QATL-ATLAS-1000-QCSAA-900-909-00-030-05-NOISE-RESILIENT-CIRCUIT-PATTERNS-AND-NISQ-PRACTICE
title: "QCSAA 900-909 · 00.030.05 — Noise-Resilient Circuit Patterns and NISQ Practice"
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
subject: "00"
subject_title: "General Information"
subsection: "030"
subsection_title: "circuits"
subsubject: "05"
subsubject_title: "Noise-Resilient Circuit Patterns and NISQ Practice"
primary_q_division: Q-HORIZON
support_q_divisions: [Q-HPC, Q-DATAGOV]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: restricted
version: 1.0.0
status: active
language: en
---
# QCSAA 900-909 · Section 00 · Subsection 030 · Subsubject 05 — Noise-Resilient Circuit Patterns and NISQ Practice

## 1. Purpose

Records the **circuit-level patterns** that allow useful work to be extracted from Noisy Intermediate-Scale Quantum (NISQ) hardware — devices with no active error correction and limited qubit counts — by exploiting circuit structure to suppress, mitigate, or post-process the noise budgeted in `02_`. This subsubject is the operational complement to the engineering pipeline of `04_`: where `04_` minimises depth and gate count, `05_` records the *patterns* that, at any given depth and gate count, extract the most signal from a noisy execution. It is also the slot where the chapter declares the binding boundary against the fault-tolerant regime owned by [`../010_Qubits/05_Logical-Qubits-Encoding-and-Error-Correction.md`](../010_Qubits/05_Logical-Qubits-Encoding-and-Error-Correction.md).

## 2. Scope

- Covers the *Noise-Resilient Circuit Patterns and NISQ Practice* subsubject (`05`) of subsection `030` *circuits* within section `00` *Fundamentos de Computación Cuántica*.
- Inherits Q-Division authority and ORB support from the parent row in [`../../README.md` §3](../../README.md#3-architecture-table)[^archtable].
- Concepts in scope:
  - **The NISQ regime, defined operationally.** A circuit is in the NISQ regime when its two-qubit depth $\times$ two-qubit gate time is comparable to (not negligibly less than) $\min(T_1, T_2)$ — the inequality of `02_` is **not** comfortably satisfied, but the circuit still produces signal above the noise floor when shots and mitigation are budgeted accordingly. The NISQ regime is bounded above by the depth at which mitigation can no longer recover the signal, and below by the depth at which fault tolerance starts to be cheaper.
  - **Variational circuits (parameterised circuits).** Shallow circuits with classically-tunable rotation parameters whose output expectation values are optimised by a classical outer loop. Standard ansatz families: hardware-efficient ansatz (HEA), unitary coupled-cluster (UCC), QAOA mixer/cost-layer alternation. Variational circuits are the dominant NISQ pattern because they trade circuit depth for outer-loop iterations, and because the classical optimiser can absorb a class of coherent errors as a parameter shift.
  - **Dynamical decoupling (DD).** Insertion of pulse sequences (X, XY-4, XY-8, CPMG, ...) into idle windows to refocus low-frequency dephasing. DD is a circuit-level pattern (it inserts gates into the circuit) and is the simplest, broadly applicable noise-suppression technique on every modality with a non-trivial $T_2/T_2^*$ gap.
  - **Echoing / refocusing patterns.** $XX$, $YY$, or composite-pulse refocusing wrapped around a slow operation to cancel coherent miscalibration to first order. Closely related to DD; the distinction is that echoes cancel a *specific* coherent error, while DD broadly suppresses dephasing.
  - **Randomised compiling / Pauli twirling.** Randomisation of the gate set used to implement a logical operation across many shots, converting a coherent error channel into an effective stochastic Pauli channel that is easier to mitigate and that no longer accumulates ballistically with depth.
  - **Zero-noise extrapolation (ZNE).** Run the circuit at deliberately scaled noise levels (e.g. by gate-folding or pulse-stretching), measure the observable at each level, and extrapolate to the zero-noise limit. ZNE is purely classical post-processing applied to a family of noisy executions — it does not change the gate count of any individual run, only the number of runs.
  - **Probabilistic error cancellation (PEC).** Express the inverse of a characterised noise channel as a quasi-probability distribution over implementable operations; sample from this distribution and combine the outcomes. Higher overhead than ZNE; sharper bias correction.
  - **Measurement / readout-error mitigation.** Calibrate a readout confusion matrix and invert it (or use Bayesian mitigation, or M3 / nearest-neighbour techniques) to correct measurement statistics. Always applicable; cheap; the standard first step.
  - **Symmetry verification and post-selection.** When the algorithm guarantees a conserved quantity (parity, particle number, magnetisation), discard shots that violate the symmetry. Trades shot count for fidelity; particularly effective in chemistry circuits.
  - **Uncomputation.** A circuit-design pattern: every ancilla used to compute an intermediate value should be **uncomputed** (the inverse subcircuit applied) before being released, otherwise the ancilla remains entangled with the result and degrades it. Uncomputation depends on the reversibility of `01_` §2.
  - **Noise-aware circuit design.** Choose ansatz topology to match the device's connectivity graph (avoid SWAPs); place high-fidelity gates on the critical path; place idle qubits on the highest-$T_2$ wires; align measurement to the end of the longest-$T_1$ qubits. These are circuit-design rules of thumb that *consume* the per-qubit calibration data of [`../010_Qubits/04_`](../010_Qubits/04_Decoherence-Noise-and-Fidelity.md) and [`../020_gates/05_`](../020_gates/05_Gate-Implementation-Calibration-and-Error-Characterization.md).
- **Boundary against [`../010_Qubits/05_Logical-Qubits-Encoding-and-Error-Correction.md`](../010_Qubits/05_Logical-Qubits-Encoding-and-Error-Correction.md) (binding for contributors).** Mitigation patterns recorded in this subsubject **do not correct errors** — they suppress, twirl, extrapolate, or post-select around them; they do not protect a quantum state below threshold. Active **quantum error correction** (encoded logical qubits, syndrome extraction, decoder, magic-state distillation) belongs in [`../010_Qubits/05_`](../010_Qubits/05_Logical-Qubits-Encoding-and-Error-Correction.md). The crossover from NISQ mitigation to fault tolerance happens when the depth required by the algorithm exceeds the depth recoverable by mitigation at acceptable shot overhead, and the per-T-gate cost of magic-state distillation becomes the dominant resource — the program shall not blur this boundary in compliance arguments.
- Out of scope: the gate catalogue (`../020_gates/`), the abstract circuit (`01_`), the depth/width metrics being budgeted (`02_`), the dynamic-circuit primitives consumed by these patterns (`03_`), the compilation pipeline that emits the executable patterns (`04_`), and active quantum error correction (`../010_Qubits/05_`).

## 3. NISQ Pattern Selection Matrix

The matrix below records, **per noise-mitigation pattern**, the noise class it targets, the overhead it pays (extra gates per shot vs. extra shots), and the indicative depth budget within which it remains useful. It is intended as a contributor-facing decision aid: any aerospace-integration argument that depends on NISQ execution shall cite the pattern selected, the overhead category accepted, and the depth budget assumed. This is the `030_circuits/` analogue of the per-modality matrix in [`../020_gates/05_`](../020_gates/05_Gate-Implementation-Calibration-and-Error-Characterization.md) §3.

| Pattern | Noise class targeted | Overhead category | Indicative depth budget | Notes |
|---|---|---|---|---|
| **Readout-error mitigation** | Measurement / classical readout | None on circuit; small classical post-processing | Any depth | Always-on baseline; near-zero cost |
| **Dynamical decoupling (DD)** | Low-frequency dephasing during idle windows | Extra gates per shot (modest) | Shallow → mid; bounded by $T_2$ | Modality-agnostic; standard first hardware step |
| **Echoing / refocusing** | Coherent miscalibration on a specific operation | Extra gates per shot (modest) | Shallow → mid | Targeted at a known coherent error |
| **Randomised compiling / Pauli twirling** | Coherent → stochastic conversion | Extra shots × extra gates per shot | Shallow → mid | Gate-set randomisation; reduces depth-ballistic accumulation |
| **Zero-noise extrapolation (ZNE)** | Generic depolarising-like noise | Extra shots (multiple noise levels) | Shallow → mid | Pure classical post-processing; needs noise scalability |
| **Probabilistic error cancellation (PEC)** | Characterised stochastic noise channel | Extra shots (potentially exponential) | Shallow only | Higher overhead; sharper bias correction |
| **Symmetry verification / post-selection** | Algorithm-violating errors | Reduced effective shot count | Shallow → mid | Requires a conserved quantity in the algorithm |
| **Uncomputation of ancillas** | Residual entanglement / leakage of intermediate state | Extra gates per shot (≈ 2× the ancilla subcircuit) | Any depth | Circuit-design discipline; not optional for ancilla use |
| **Noise-aware ansatz / placement** | Heterogeneous per-qubit / per-pair fidelities | Compile-time only | Any depth | Consumes calibration data; relies on `04_` |
| **Variational circuits (HEA, UCC, QAOA)** | Bounded coherent miscalibration absorbed by classical optimiser | Outer-loop iterations | Shallow only | Trades depth for outer-loop iteration count |

## 4. Footprint

| Metric | Value |
|---|---|
| Architecture | `QCSAA` — Quantum Computing & Sentient Agency Architecture |
| Master range | `900–999` |
| Code range | `900-909` |
| Section | `00` — Fundamentos de Computación Cuántica |
| Subject | `00` — General Information |
| Subsection | `030` — circuits |
| Subsubject | `05` — Noise-Resilient Circuit Patterns and NISQ Practice |
| Primary Q-Division | Q-HORIZON[^qdiv] |
| Support Q-Divisions | Q-HPC, Q-DATAGOV |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | `restricted`[^gov] |
| Folder path | `Q+ATLANTIDE/900-999_QCSAA/900-909_Fundamentos-de-Computacion-Cuantica/030_circuits/` |
| Document | `05_Noise-Resilient-Circuit-Patterns-and-NISQ-Practice.md` (this file) |
| Parent subsection | [`README.md`](./README.md) · [`00_Overview.md`](./00_Overview.md) |
| Parent architecture | [`../../README.md`](../../README.md) |
| Parent baseline | [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md) |

## 5. References & Citations


[^baseline]: **Q+ATLANTIDE controlled baseline (v1.0.0)** — [`organization/Q+ATLANTIDE.md`](../../../../organization/Q+ATLANTIDE.md). Defines the controlled `000-999` architecture-band taxonomy and the ATLAS-1000 register subpart.

[^archtable]: **QCSAA §3 Architecture Table** — [`../../README.md` §3](../../README.md#3-architecture-table). Authoritative source for the `900-909` row (Section `00` — Fundamentos de Computación Cuántica, Primary Q-Division Q-HORIZON).

[^qdiv]: **Q-Division authority** — Q-Divisions provide technical authority over an architecture row (Q+ATLANTIDE Note N-002). See [`organization/Q+ATLANTIDE.md` §4](../../../../organization/Q+ATLANTIDE.md#4-notes).

[^gov]: **Governance class** — Bands are classified as `baseline` or `restricted` per Q+ATLANTIDE §4 governance rules.

[^ieeep7130]: **IEEE P7130 — Standard for Quantum Computing Definitions** — Vocabulary baseline for the quantum computing scope of QCSAA `900-999`.

[^s1000d]: **S1000D Issue 6.0 — International specification for technical publications** — Common Source DataBase (CSDB) and Data Module Code (DMC) specification used for all Q+ATLANTIDE artefacts.

[^as9100d]: **AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations** — Quality-management baseline for all Q+ATLANTIDE deliverables.

### Applicable industry standards

The following standards apply to this subsubject in addition to the cross-cutting Q+ATLANTIDE governance:

- IEEE P7130 — Standard for Quantum Computing Definitions[^ieeep7130]
- S1000D Issue 6.0 — International specification for technical publications[^s1000d]
- AS9100D — Quality Management Systems — Aviation, Space and Defense Organizations[^as9100d]
