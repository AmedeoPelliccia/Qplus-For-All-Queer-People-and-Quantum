# Controlled Vocabulary and Acronym Register

**Repository:** AEROSPACEMODEL / DePutapapUE  
**Authority:** ASIT  
**Scope:** Repository-wide  
**Status:** ACTIVE  
**Constitution reference:** `AEROSPACEMODEL-model-digital-constitution.md#article-ix`  
**Machine-readable source:** `controlled_vocabulary.yaml`  
**Human-readable counterparts:** `acronyms.md`, `terms.md`

This document contains the controlled vocabulary and acronym register for the repository.

> Note: the YAML block below is rendered as code to avoid being interpreted as Markdown frontmatter.

---

## 1. Machine-Readable Controlled Vocabulary

```yaml
# Machine-readable controlled vocabulary for the AEROSPACEMODEL / DePutapapUE repository.
# Authority: ASIT
# Scope: Repository-wide
# Status: ACTIVE
# Article IX of the Model Digital Constitution (AEROSPACEMODEL-model-digital-constitution.md)
# Human-readable counterparts: acronyms.md, terms.md
#
# Schema:
#   Each top-level key is a vocabulary category.
#   Entries list every permitted value with a short definition.
#   "deprecated" flag marks values that must not be used in new content.

schema_version: "1.0.0"
last_updated: "2026-05-01"
authority: ASIT
constitution_ref: "AEROSPACEMODEL-model-digital-constitution.md#article-ix"

status_codes:
  - value: ACTIVE
    definition: "Document or artefact is in force and authoritative."
  - value: DRAFT
    aliases: ["Draft", "draft"]
    definition: "Work in progress; not yet approved or binding."
  - value: DRAFT_STAKEHOLDER_REVIEW
    aliases: ["Draft → Stakeholder Review"]
    definition: "Draft submitted for stakeholder review; not yet approved."
  - value: CONTROLLED_BASELINE
    aliases: ["controlled-baseline"]
    definition: "Approved and locked baseline; changes require a Change Request (CR)."
  - value: BALANCED_DRAFT
    aliases: ["balanced_draft"]
    definition: "Draft with competing stakeholder inputs reconciled; awaiting final approval."
  - value: SUPERSEDED
    definition: "Replaced by a newer version; retained for audit trail only."
  - value: DEPRECATED
    definition: "No longer recommended; will be removed in a future baseline."
  - value: REJECTED
    definition: "Proposed content formally rejected; recorded for audit."
  - value: ALPHA
    aliases: ["α"]
    definition: "Very early draft; experimental and subject to major change."
  - value: ARCHIVED
    definition: "Inactive and preserved for historical reference only."

root_folders:
  - name: "00_META"
    definition: "Repository-wide metadata, glossaries, and governance configuration."
  - name: "Q+ATLANTIDE"
    definition: "Master classification system and knowledge architecture, including Q+ATLANTIDE1000 Bands 000–999."
  - name: "IDEALE-ESG"
    definition: "IDEALE-ESG framework domain tree: Aerospace, Defence, Energy, Economics, Environments, Governance, Information, Logistics, Social."
  - name: "organization"
    definition: "Organizational structure: Q-Divisions, ORB-Functions, programmes, and governance entities."
  - name: "docs"
    definition: "Reference documentation, including S1000D architecture, standards, and repository-level explanatory material."
  - name: "scripts"
    definition: "Automation and tooling scripts, including CI, SICOCA, validation, and utilities."
  - name: "OPT-INS_FRAMEWORK"
    definition: "OPT-INS governance framework specifications, including GQAOA, LUT, APE-ADAPT, and related controlled artefacts."
  - name: "programs"
    definition: "Programme-specific PRDs, requirements, studies, and implementation artefacts."
  - name: "AMEDEO-ITBPFO"
    definition: "FINEX execution engine and associated API/frontend."

qatl_bands:
  - code: "000-099"
    suffix: "ATLAS"
    definition: "Aircraft Top Level Architecture Schema/System — new commercial aircraft architectures, aircraft systems, maintenance, identification, and lifecycle architecture."
  - code: "100-199"
    suffix: "STA"
    definition: "Space Technology Architecture — space systems, propulsion, missions, orbital infrastructure, and exploration architectures."
  - code: "200-299"
    suffix: "DEF"
    definition: "Defence Architecture — defence systems, protected capabilities, dual-use boundaries, mission systems, and controlled security interfaces."
  - code: "300-399"
    suffix: "DTCEC"
    definition: "Digital Twin, Cloud, Edge Computing — digital twins, IoT, AI/ML, blockchain, simulation, and distributed computation."
  - code: "400-499"
    suffix: "EPTA"
    definition: "Energy and Propulsion Technology Architecture — energy systems, propulsion, hydrogen, electric, hybrid-electric, and alternative energy architectures."
  - code: "500-599"
    suffix: "AMTA"
    definition: "Advanced Materials and Technologies for Aerospace — materials, bio, nano, composite, cryogenic, and structural technology families."
  - code: "600-699"
    suffix: "OGATA"
    definition: "Open Ground and Autonomous Technology Architecture — robotics, autonomous vehicles, ground automation, and smart infrastructure."
  - code: "700-799"
    suffix: "ACV"
    definition: "Aerial City and Vehicles — UAM, eVTOL, vertiport-compatible systems, aerial mobility, and urban aerospace integration."
  - code: "800-899"
    suffix: "CYB"
    definition: "Cybersecurity — governance, network security, cryptography, resilience, cyber-physical protection, and post-quantum security."
  - code: "900-999"
    suffix: "QCSAA"
    definition: "Quantum Computing and Sentient Agency Architecture — quantum systems, quantum-classical bridges, agency governance, and advanced intelligent systems."

ideale_esg_domains:
  - code: "A"
    name: "A-Aerospace"
    definition: "Aerospace domain."
  - code: "D"
    name: "D-Defense"
    definition: "Defence domain."
  - code: "E"
    name: "E-Energy"
    definition: "Energy domain."
  - code: "E2"
    name: "E2-Economics"
    definition: "Economics domain."
  - code: "E3"
    name: "E3-Environments"
    definition: "Environments domain."
  - code: "G"
    name: "G-Governance"
    definition: "Governance domain."
  - code: "I"
    name: "I-Information"
    definition: "Information domain."
  - code: "L"
    name: "L-Logistics"
    definition: "Logistics domain."
  - code: "S"
    name: "S-Social"
    definition: "Social domain."

ideale_esg_subdomains:
  - code: "I"
    name: "I-Infrastructures"
    definition: "Infrastructure assets and systems within an IDEALE-ESG domain."
  - code: "N"
    name: "N-Neural-Networks"
    definition: "AI and neural-network components within an IDEALE-ESG domain."
  - code: "O"
    name: "O-Organizations"
    definition: "Organizational entities within an IDEALE-ESG domain."
  - code: "P"
    name: "P-Programmes"
    definition: "Programmes and projects within an IDEALE-ESG domain."
  - code: "T"
    name: "T-Technologies"
    definition: "Technologies within an IDEALE-ESG domain."

lifecycle_phases:
  - code: LC01
    definition: "Concept Definition — define scope, need, classification, initial stakeholders, and lifecycle intent."
  - code: LC02
    definition: "Requirements Definition — define requirements, constraints, interfaces, safety needs, and applicability."
  - code: LC03
    definition: "Architecture Definition — define architecture, asset breakdown, interfaces, and system boundaries."
  - code: LC04
    definition: "Preliminary Design — establish early design assumptions, layouts, trade studies, and reference concepts."
  - code: LC05
    definition: "Detailed Design — produce detailed design, configuration data, engineering evidence, and implementation baseline."
  - code: LC06
    definition: "Verification Planning — define verification approach, test plans, inspection logic, acceptance criteria, and evidence needs."
  - code: LC07
    definition: "Construction / Implementation — build, configure, install, deploy, or implement the asset."
  - code: LC08
    definition: "Integration — integrate the asset with systems, facilities, digital platforms, operations, or programmes."
  - code: LC09
    definition: "Commissioning — confirm readiness for use through inspection, functional checks, operational acceptance, and handover."
  - code: LC10
    definition: "Certification / Approval — support regulatory, authority, customer, internal, or programme approval processes."
  - code: LC11
    definition: "Operation — use the asset in normal service, production, maintenance, testing, launch, or support operations."
  - code: LC12
    definition: "Maintenance / Support — maintain, inspect, repair, calibrate, update, or support the asset."
  - code: LC13
    definition: "Upgrade / Modification — modify, extend, retrofit, reconfigure, or improve the asset."
  - code: LC14
    definition: "Decommissioning / Retirement — retire, remove, archive, dispose, or replace the asset and its evidence records."

mandatory_inheritance_marks:
  - mark: K
    name: "Kindness"
    category: "operating duty"
    definition: "Humane, respectful, non-harmful conduct toward people, ecosystems, and machines."
  - mark: D
    name: "Determinism"
    category: "operating duty"
    definition: "Reproducible behaviour: declared inputs, pinned versions, recorded seeds, and repeatable outputs."
  - mark: L-LEG
    name: "Legality"
    category: "design principle"
    definition: "Compliance encoded as an architectural constraint from inception."
  - mark: L-LOY
    name: "Loyalty"
    category: "design principle"
    definition: "Fidelity to declared purpose, stakeholders, and charter; no hidden allegiances."
  - mark: F
    name: "Fairness"
    category: "ethical mark"
    definition: "Equal treatment, absence of unjustified bias, proportionality, and accessibility."
  - mark: J
    name: "Justice"
    category: "ethical mark"
    definition: "Due process, proportional remedy, and fair distribution of risk and reward."
  - mark: IE
    name: "Imparzialità Empatica / Empathic Impartiality"
    category: "ethical mark"
    definition: "Impartial in rule, empathic in application; synthesis of Kindness with Fairness and Justice."
  - mark: INV
    name: "Invulnerability"
    category: "security mark"
    definition: "Designed resilience: defence-in-depth, least privilege, zero-trust, and redundancy."
  - mark: AR
    name: "Activist Rights"
    category: "civic mark"
    definition: "Protection of dissent, whistleblowing, and conscientious objection without retaliation."
  - mark: WR
    name: "Workers' Rights"
    category: "labour mark"
    definition: "Full labour rights for every worker, including direct workers, contractors, and supply-chain workers."
  - mark: RA
    name: "Rights of People with Addictions"
    category: "health and dignity mark"
    definition: "Addiction treated as a health condition; full rights and dignity, with no exploitation."

authority_roles:
  - role: ASIT
    definition: "Authority for Structural and Integrity Traceability — repository traceability integrity, structural consistency, and lifecycle operating coherence."
  - role: QA_AUTHORITY
    aliases: ["QA Authority"]
    definition: "Quality assurance sign-off authority."
  - role: CERTIFICATION_AUTHORITY
    aliases: ["Certification Authority"]
    definition: "Compliance and certification sign-off authority."
  - role: OBSERVER
    definition: "Read and monitor access; no write authority."
  - role: DELINEANT
    definition: "Boundary definition and scoping authority."

governance_branches:
  - code: LEG
    name: "Legislative"
    definition: "Stakeholder Assembly — strategy, budget oversight, executive confirmation, and charter amendments."
  - code: EXE
    name: "Executive"
    definition: "Executive Committee — programme execution, operations, and resource allocation."
  - code: JUD
    name: "Judicial / Oversight"
    definition: "Independent Tribunal of Safety, Ethics and Compliance — disputes, safety halts, and whistleblower protection."
  - code: AUD
    name: "Auditorial / Control"
    definition: "Independent Audit Board — financial, operational, performance, and compliance audits."

crossing_powers:
  - code: CP-1
    name: "Education and Training / Unity"
    mode: "supporting · human-led"
    definition: "Corporate Academy and TMC — certifies competencies across all branches."
  - code: CP-2
    name: "Automation / Supervised Execution"
    mode: "supporting · supervised"
    definition: "Office of Automation and Digital Operations — governed automation under human supervision."

field_values:
  classification:
    - value: "Consortium Confidential – Approved Stakeholders Only"
      definition: "Visible only to approved consortium members."
    - value: "Internal"
      definition: "Visible to all authorized repository contributors."
    - value: "Public"
      definition: "No access restriction."

  document_type:
    - value: "governance"
      definition: "Governance charter, constitution, or policy document."
    - value: "specification"
      definition: "Technical or regulatory specification."
    - value: "readme"
      definition: "Descriptive overview or index for a folder or module."
    - value: "glossary"
      definition: "Controlled vocabulary, terms, or acronym register."
    - value: "regulatory_framework_specification"
      definition: "Machine-readable regulatory framework, for example ESSA."
    - value: "prd"
      definition: "Product Requirements Document."

  language:
    - value: "en"
      definition: "English."
    - value: "es"
      definition: "Spanish."
    - value: "it"
      definition: "Italian."
    - value: "mix"
      definition: "Mixed or multilingual document."

amendment_procedure: >
  To add, modify, or deprecate a controlled vocabulary entry:
  1. Open a Change Request (CR) per Article VII of AEROSPACEMODEL-model-digital-constitution.md.
  2. Update this file and the corresponding human-readable counterpart, acronyms.md or terms.md, in the same commit.
  3. Obtain ASIT sign-off before merging to a governed baseline branch.
  4. Record the change in CHANGELOG.md with the CR reference.
```

---

## 2. Acronyms

**Authority:** ASIT  
**Scope:** Repository-wide  
**Status:** ACTIVE  
**Source:** `AEROSPACEMODEL-model-digital-constitution.md` Article V.2 canonical inline glossary and repository content  
**Machine-readable counterpart:** `controlled_vocabulary.yaml`

This file is the authoritative register of acronyms used within this repository.  
All acronyms in folder names, status codes, and field values must be defined here.

---

| Acronym | Expansion |
|---------|-----------|
| ACV | Aerial City and Vehicles — Q+ATLANTIDE Band 700–799 |
| AMM | Aircraft Maintenance Manual |
| AMTA | Advanced Materials and Technologies for Aerospace — Q+ATLANTIDE Band 500–599 |
| APE | Aided Prompt Engineering |
| AR | Activist Rights — Civic Mark / Mandatory Inheritance |
| AS9100D | Aerospace quality management system standard |
| ASIT | Authority for Structural and Integrity Traceability |
| ATLAS | Aircraft Top Level Architecture Schema/System — Q+ATLANTIDE Band 000–099 |
| CCT | Conditions Cross-Reference Table — S1000D |
| CI | Continuous Integration |
| COI | Conflict of Interest |
| CP-1 | Crossing Power 1 — Education and Training / Unity |
| CP-2 | Crossing Power 2 — Automation / Supervised Execution |
| CR | Change Request |
| CSDB | Common Source DataBase — S1000D |
| CYB | Cybersecurity — Q+ATLANTIDE Band 800–899 |
| D | Determinism — Mandatory Inheritance |
| DEF | Defence Architecture — Q+ATLANTIDE Band 200–299 |
| DEGF | Democratic Enterprise Governance Framework |
| DO-178C | Software considerations in airborne systems — RTCA |
| DO-254 | Design assurance for airborne electronic hardware — RTCA |
| DTCEC | Digital Twin, Cloud, Edge Computing — Q+ATLANTIDE Band 300–399 |
| EAP | Employee Assistance Programme |
| EAR | Export Administration Regulations — United States |
| EASA | European Union Aviation Safety Agency |
| EPTA | Energy and Propulsion Technology Architecture — Q+ATLANTIDE Band 400–499 |
| ESG | Environmental, Social and Governance |
| ESSA | European Union Space Safety Agency — governance artefact / institutional model |
| EVM | Earned Value Management |
| F | Fairness — Ethical Mark / Mandatory Inheritance |
| FAA | Federal Aviation Administration — United States |
| GAIA-QAO | GAIA Quantum Aerospace Organisation |
| GDPR | General Data Protection Regulation — European Union |
| GSE | Ground Support Equipment |
| HR | Human Resources |
| IE | Imparzialità Empatica / Empathic Impartiality — Ethical Mark / Mandatory Inheritance |
| IDEALE | Infrastructures, Defence, Energy, Information, Aerospace, Logistics, Economics, Environments — ESG framework |
| IETP | Interactive Electronic Technical Publication |
| ILO | International Labour Organization |
| INV | Invulnerability — Security Mark / Mandatory Inheritance |
| ITAR | International Traffic in Arms Regulations — United States |
| J | Justice — Ethical Mark / Mandatory Inheritance |
| K | Kindness — Mandatory Inheritance |
| KPI | Key Performance Indicator |
| L | Legality and/or Loyalty — Design Principles / Mandatory Inheritance |
| LC01–LC14 | Canonical 14-phase product lifecycle phase model |
| LUTNDR | Libro Unico delle Tecnologie: in uso, Nuova progettazione, Disuso, Riassetti |
| MLOps | Machine Learning Operations |
| NDA | Non-Disclosure Agreement |
| OGATA | Open Ground and Autonomous Technology Architecture — Q+ATLANTIDE Band 600–699 |
| ORB | Organizational / Operational Resource Board — enterprise support function layer |
| ORB-CSR | ORB — Corporate Social Responsibility |
| ORB-FIN | ORB — Finance and Budget Control |
| ORB-GOV | ORB — Governance, Records and Decision Ledger |
| ORB-HR | ORB — Human Resources and Competence |
| ORB-LEG | ORB — Legal, Compliance and Contracts |
| ORB-MKTG | ORB — Marketing and Communications |
| ORB-OPS | ORB — Operations and Administrative Support |
| ORB-PMO | ORB — Programme Management Office |
| ORB-RISK | ORB — Risk, Audit and Assurance |
| P&L.inc | Peace-and-Love inc. — legal style name / foundation vehicle associated with the Q+ organizational stack |
| PRD | Product Requirements Document |
| QA | Quality Assurance |
| Q+ | Q+ organizational / corporate public mark |
| Q+A | Q+AEROSPACE abbreviated public mark |
| Q+AEROSPACE | Quantum + Aerospace future/full brand name |
| Q+ATLANTIDE | Quantum + Aerospace Top Level Architectures and Novel Technologies Identification and Data Ecosystem |
| Q+ATLANTIDE1000 | Controlled 000–999 identification schema of Q+ATLANTIDE |
| Q-CYBERSEC | Q-Division — Cybersecurity |
| Q-DATAGOV | Q-Division — Data Governance |
| Q-GREENTECH | Q-Division — Green Technology, Energy and Propulsion |
| Q-GROUND | Q-Division — Ground Systems and Automation |
| Q-HORIZON | Q-Division — Horizon interface, foresight and strategic positioning |
| Q-HPC | Q-Division — High-Performance Computing |
| Q-HUESCORT-SCIRES-OPEN | Horizon / SCIRES / OPEN Interface Layer |
| Q-INDUSTRY | Q-Division — Industrial Systems and Manufacturing |
| Q-MECHANICS | Q-Division — Mechanics and Mechanical Systems |
| Q-SCIRES | Q-Division — Scientific Research |
| Q-SPACE | Q-Division — Space |
| Q-STRUCTURES | Q-Division — Structures and Materials |
| QCSAA | Quantum Computing and Sentient Agency Architecture — Q+ATLANTIDE Band 900–999 |
| RA | Rights of People with Addictions — Health and Dignity Mark / Mandatory Inheritance |
| S1000D | International specification for technical publications |
| SBOM | Software Bill of Materials |
| SICOCA | Sustainable Industrial Competitive Operations — Chained Algorithms |
| SLAPP | Strategic Lawsuit Against Public Participation |
| SLA | Service Level Agreement |
| STA | Space Technology Architecture — Q+ATLANTIDE Band 100–199 |
| TMC | Training Master Class |
| UTCS | Universal Traceability and Configuration System |
| WR | Workers' Rights — Labour Mark / Mandatory Inheritance |

---

## 3. Amendment Procedure

To add, modify, or deprecate a controlled vocabulary entry:

1. Open a Change Request (CR) per Article VII of the Model Digital Constitution.
2. Update the machine-readable vocabulary and the corresponding human-readable register in the same commit.
3. Obtain ASIT sign-off before merging to a governed baseline branch.
4. Record the change in `CHANGELOG.md` with the CR reference.

---

**End of controlled vocabulary and acronym register.**
