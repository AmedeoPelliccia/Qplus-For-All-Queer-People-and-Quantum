---
document_id: AMPEL360-PLUS-Q10-NN-05-08-README
title: "05-08 — Predictive Maintenance Explainability and Evidence — AMPEL360-PLUS Spacecraft Q10"
programme: "AMPEL360-PLUS-Spacecraft-Q10"
section: "05 — Predictive Maintenance NN"
sub_section: "05-08 — Predictive Maintenance Explainability and Evidence"
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

# 05-08 — Predictive Maintenance Explainability and Evidence
## AMPEL360-PLUS Spacecraft Q10

---

## 1. Scope

This sub-section defines the **Explainable AI (XAI) framework, evidence generation pipeline, and human-machine interface (HMI) design** for the predictive maintenance NN system of the AMPEL360-PLUS Q10.

XAI and traceable evidence are prerequisites for certification acceptance, operator trust, and auditability of all NN-generated maintenance decisions.

> **Boundary:** Explainability artefacts support the safety case but do not replace certified engineering validation.

---

## 2. Objectives

| # | Objective | Success Metric |
|:-:|:----------|:---------------|
| 1 | Provide feature-level explanations for all safety-critical NN decisions | SHAP/counterfactual explanation generated for 100% of inspection/maintenance triggers |
| 2 | Quantify and communicate prediction uncertainty to maintenance operators | Uncertainty displayed with every NN output; operator comprehension score ≥ 80% in usability tests |
| 3 | Generate certification-grade evidence artefacts for every lifecycle gate | Evidence artefacts accepted at CDR/TRR; full audit chain from sensor to decision |

---

## 3. Key Contents

```yaml
key_contents:
  - "SHAP + Counterfactual NN for feature attribution and contrastive explanations"
  - "XAI requirements per NN module: safety-criticality-driven explainability depth"
  - "Attention mechanism visualisation for Transformer-based modules (05-05)"
  - "Uncertainty quantification communication: epistemic vs. aleatoric decomposition"
  - "Maintenance HMI design: transparency, actionability, alert hierarchy, crew/operator interface"
  - "Evidence artefact specification: explanation logs, audit trail, certification dossier format"
  - "Cross-reference to 05-09 (governance) and programme safety case"
```

---

## 4. NN Architecture Summary

| Component | Specification |
|:----------|:--------------|
| **Model Typology** | SHAP + Counterfactual NN; post-hoc explainability layer over all sub-modules |
| **Inputs** | NN model outputs, input feature vectors, uncertainty bounds from sub-modules 05-01–05-07 |
| **Outputs** | Feature importance scores, counterfactual scenarios, SHAP summary plots, evidence artefact packages |
| **Physics Constraints** | Explanations must be physically consistent; implausible SHAP attributions flagged for review |
| **Uncertainty Quantification** | Epistemic: confidence in explanation quality; aleatoric: data-driven explanation variance |
| **Edge Deployment** | Lightweight SHAP kernel approximation for onboard summary; full SHAP run on ground post-flight |

---

## 5. Integration Interfaces

| Interface | Direction | Protocol / Schema | Purpose |
|:----------|:----------|:------------------|:--------|
| Sub-modules 05-01–05-07 | Input | REST + JSON | NN outputs, input features, uncertainty bounds |
| Maintenance HMI | Output | REST + JSON + SVG | Explainability dashboards, alert displays |
| S1000D CSDB | Output | XML Data Modules | Evidence artefacts as Data Modules for certification |
| SICO.CA Audit Ledger | Output | SHA-256 hash + append-only log | Immutable registration of explanations and evidence |
| Cloud Retraining | Bidirectional | Kafka + MLflow | Explanation quality feedback to improve model transparency |

---

## 6. Validation & Verification

| Phase | Activity | Acceptance Criteria |
|:------|:---------|:-------------------|
| V1 | SHAP benchmark against held-out test set | SHAP faithfulness metric ≥ 0.85; no physically implausible attributions |
| V2 | Counterfactual plausibility review with domain experts | ≥ 90% of counterfactuals rated plausible by engineering review panel |
| V3 | HMI usability test with maintenance crew (N ≥ 10) | Operator comprehension score ≥ 80%; alert false acknowledgement rate < 1% |
| V4 | Evidence artefact certification review | Artefacts accepted by programme authority; no open findings at TRR |
| V5 | Fleet operational use | Explanation latency ≤ 2 s (onboard); ≤ 30 s (ground full SHAP) |

---

## 7. SICO.CA Compliance

| Principle | Implementation |
|:----------|:---------------|
| **Sustainable** | Transparent decisions prevent unnecessary repairs; explainability enables long-term model improvement |
| **Industrial Competitive** | Reduced certification cost through pre-formatted evidence; accelerates authority approval timelines |
| **Operations** | Real-time explanation summaries onboard; full evidence packages on ground within 30 min |
| **Chained Algorithms** | Every explanation log, SHAP run, and evidence artefact SHA-256 registered in immutable ledger |
| **No Irreversible Damage** | Conservative physical plausibility checks reject explanations that would mask safety-critical inputs |

---

## 8. Cross-References

| Document | Relationship |
|:---------|:-------------|
| `05-00` | Architecture baseline, DAL mapping, governance protocol |
| `05-06` | RUL evidence generation; lifecycle gate artefacts |
| `05-07` | Work-order audit trail and reuse decision explainability |
| `05-09` | MLOps pipeline, hash-chained audit registry, policy enforcement |

---

📜 *Sub-module aligned with Ampel Theoretical Framework v0.2.0 and SICO.CA doctrine. All model versions, datasets, and triggers are hash-chained and stored in an immutable audit ledger.*
