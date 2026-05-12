---
document_id: AMPEL360-PLUS-Q10-NN-05-03-README
title: "05-03 — Propulsion and Thermal System Fault Prediction — AMPEL360-PLUS Spacecraft Q10"
programme: "AMPEL360-PLUS-Spacecraft-Q10"
section: "05 — Predictive Maintenance NN"
sub_section: "05-03 — Propulsion and Thermal System Fault Prediction"
version: "0.1.0"
status: "draft / programme-impact-study"
classification: "open-technical-programme-study"
owner: "Amedeo Pelliccia / Q+"
primary_language: "en"
created: 2026-05-12
related_docs:
  - "05-00: General Architecture & Governance"
  - "AMPEL-THEORETICAL-FRAMEWORK-SICOCA-GR-FLUIDS-001"
---

# 05-03 — Propulsion and Thermal System Fault Prediction
## AMPEL360-PLUS Spacecraft Q10

---

## 1. Scope

This sub-section defines the neural network architecture for **fault detection, isolation, and prognosis (FDIP)** in the main propulsion system, reaction control system (RCS), propellant feedlines, and active thermal control loops of the AMPEL360-PLUS Q10.

> **Boundary:** NN outputs are advisory; final airworthiness decisions require certified engineering validation.

---

## 2. Objectives

| # | Objective | Success Metric |
|:-:|:----------|:---------------|
| 1 | Detect incipient engine / RCS thruster faults ≥ 2 cycles before functional loss | Detection lead time ≥ 2 mission cycles; recall ≥ 92% |
| 2 | Predict propellant feed anomalies (valve, seal, line) before leak/contamination | False negative rate < 0.5%; precision ≥ 90% |
| 3 | Forecast thermal control loop degradation (radiator, pump) | MAE in coolant ΔT prediction ≤ 2 K; pump wear recall ≥ 88% |

---

## 3. Key Contents

```yaml
key_contents:
  - "1D CNN + State-Space NN for time-series engine health signatures"
  - "Main engine health model: turbopump vibration, combustion stability, nozzle erosion"
  - "RCS thruster wear, leak-before-burst, and contamination prognosis"
  - "Propellant feed system anomaly detection (valves, seals, flex lines)"
  - "Active thermal control loop NN: radiator fouling, heat pipe degradation, pump wear"
  - "Multi-signal fusion: temperature, pressure, flow rate, vibration, acoustic emission"
  - "Fault signature library and NN classifier training data requirements"
  - "Interface with 05-01 (sensor scope) and 05-07 (maintenance scheduling)"
```

---

## 4. NN Architecture Summary

| Component | Specification |
|:----------|:--------------|
| **Model Typology** | 1D CNN + State-Space NN for engine/RCS; physics-constrained GRU for thermal loops |
| **Inputs** | Turbopump speed, chamber pressure, injector ΔP, nozzle wall temp, propellant flow, coolant loop ΔT, vibration spectra |
| **Outputs** | Fault class probabilities, degradation state index, time-to-maintenance estimate, 95% prediction intervals |
| **Physics Constraints** | Rocket equation, Navier-Stokes reduced-order thermal models, valve flow coefficient laws |
| **Uncertainty Quantification** | Aleatoric: heteroscedastic Gaussian; Epistemic: 5-model deep ensemble |
| **Edge Deployment** | INT8 quantization; latency ≤ 40 ms; fallback: deterministic threshold fault detector |

---

## 5. Integration Interfaces

| Interface | Direction | Protocol / Schema | Purpose |
|:----------|:----------|:------------------|:--------|
| VHMS Router | Input | MQTT/DDS + Avro JSON | Telemetry ingestion, health state sync |
| 05-06 RUL Estimator | Output | REST/GraphQL + Parquet | Remaining life forecast, margin bands |
| 05-07 Scheduler | Output | OPC-UA + JSON Schema | Inspection triggers, work order generation |
| S1000D CSDB | Output | XML Data Modules | Maintenance task linkage, IPC references |
| Cloud Retraining | Bidirectional | Kafka + MLflow | Fleet-wide model updates, synthetic data augmentation |

---

## 6. Validation & Verification

| Phase | Activity | Acceptance Criteria |
|:------|:---------|:-------------------|
| V1 | Fault injection tests on propulsion testbed | Fault recall ≥ 90%; FAR < 2% |
| V2 | Sub-scale combustion stability simulation | Instability onset prediction within ±5% of ground truth |
| V3 | Full-scale hot-fire campaign | Cross-engine correlation r ≥ 0.87; missed detection < 1% |
| V4 | Flight campaign thermal loop validation | Coolant ΔT MAE ≤ 2 K; pump wear detection lead ≥ 3 cycles |
| V5 | Fleet generalization stress test | Robustness to ±20% input perturbation; graceful degradation |

---

## 7. SICO.CA Compliance

| Principle | Implementation |
|:----------|:---------------|
| **Sustainable** | Condition-based replacement reduces engine consumable waste by ≥ 35% vs. cycle-count maintenance |
| **Industrial Competitive** | Eliminates precautionary engine swaps; reduces turnaround engine inspection time by ≥ 20% |
| **Operations** | Real-time fault detection at 100 Hz vibration sampling; deterministic fallback within 40 ms |
| **Chained Algorithms** | All fault signatures, model versions, and inference logs SHA-256 registered in immutable ledger |
| **No Irreversible Damage** | Conservative uncertainty bounds trigger hold/abort before catastrophic failure thresholds |

---

## 8. Cross-References

| Document | Relationship |
|:---------|:-------------|
| `05-00` | Architecture baseline, DAL mapping, governance protocol |
| `05-01` | Sensor suite and telemetry ingestion for propulsion/thermal |
| `05-06` | Coupled RUL prognosis for engine life accounting |
| `05-08` | SHAP-based explainability for fault classification |
| `05-09` | MLOps pipeline, hash-chained audit registry, policy enforcement |

---

📜 *Sub-module aligned with Ampel Theoretical Framework v0.2.0 and SICO.CA doctrine. All model versions, datasets, and triggers are hash-chained and stored in an immutable audit ledger.*
