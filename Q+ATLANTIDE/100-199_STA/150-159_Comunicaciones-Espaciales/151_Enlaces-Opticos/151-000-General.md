---
document_id: QATL-ATLAS-1000-STA-150-159-05-151-000-GENERAL
title: "STA 150-159 · 151-000 — General"
register: ATLAS-1000
parent_baseline: Q+ATLANTIDE
parent_baseline_doc: ../../../../organization/Q+ATLANTIDE.md
parent_architecture_doc: ../../README.md
parent_section_doc: ../README.md
architecture_code: STA
architecture_name: "Space Technology Architecture"
master_range: "100–199"
code_range: "150-159"
section: "05"
section_title: "Comunicaciones Espaciales"
subsection: "151"
subsection_title: "Enlaces Ópticos"
subsubject: "000"
subsubject_title: "General"
primary_q_division: Q-SPACE
support_q_divisions: [Q-DATAGOV, Q-HPC]
orb_function_support: [ORB-PMO, ORB-LEG]
governance_class: baseline
version: 1.0.0
status: active
language: en
---

# STA 150-159 · 151-000 — General

## §1 Purpose

This document serves as the entry-point for the **Optical Links (Free-Space Optical / FSO)** subsection within the Q+ATLANTIDE Space Technology Architecture (STA), code range 150-159, section 05 — Comunicaciones Espaciales.[^baseline] It provides a navigational and contextual summary for all ten controlled subsubject documents (001–010) that together define the full FSO discipline baseline.[^archtable]

The Overview establishes the taxonomic position of optical links within the Q+ATLANTIDE register, identifies the governing Q-Division authority, and consolidates pointers to each subsubject for traceability and lifecycle governance purposes.[^qdiv][^gov]

## §2 Scope

The following ten subsubject files constitute the complete 151 — *Enlaces Ópticos* controlled baseline:

| ID | File | One-line description |
|----|------|----------------------|
| 010 | [151-010-Optical-Links-Controlled-Definition.md](./151-010-Optical-Links-Controlled-Definition.md) | Controlled Q+ATLANTIDE definition of FSO / optical link, wavelength bands, link categories, and taxonomy. |
| 020 | [151-020-Free-Space-Optical-Communication-Architecture.md](./151-020-Free-Space-Optical-Communication-Architecture.md) | Complete FSO system architecture including space and ground terminals, relay nodes, and hybrid RF/optical fallback. |
| 030 | [151-030-Laser-Terminals-Transmitters-and-Receivers.md](./151-030-Laser-Terminals-Transmitters-and-Receivers.md) | Laser terminal design parameters: laser source classes, apertures, detectors, EDFA, and polarisation. |
| 040 | [151-040-Acquisition-Pointing-and-Tracking-APT.md](./151-040-Acquisition-Pointing-and-Tracking-APT.md) | APT system definition for optical crosslinks: beacon acquisition, coarse/fine pointing, tracking bandwidth. |
| 050 | [151-050-Link-Budget-Beam-Divergence-and-Atmospheric-Losses.md](./151-050-Link-Budget-Beam-Divergence-and-Atmospheric-Losses.md) | Optical link-budget methodology: transmit power, beam divergence, geometric and atmospheric losses, fade margin. |
| 060 | [151-060-Modulation-Coding-and-Data-Rate-Classes.md](./151-060-Modulation-Coding-and-Data-Rate-Classes.md) | Optical modulation schemes (OOK, DPSK, BPSK, QPSK coherent, PPM), FEC coding, and Q+ATLANTIDE rate classes. |
| 070 | [151-070-Ground-Station-and-Optical-Network-Interfaces.md](./151-070-Ground-Station-and-Optical-Network-Interfaces.md) | OGS functional elements: telescope apertures, adaptive optics, tracking mount, modem, site diversity. |
| 080 | [151-080-Safety-Eye-Hazard-and-Regulatory-Boundaries.md](./151-080-Safety-Eye-Hazard-and-Regulatory-Boundaries.md) | Laser safety classification for space optical links: IEC 60825-1 hazard classes, MPE, exclusion zones, ITU-R coordination. |
| 090 | [151-090-Traceability-Evidence-and-Lifecycle-Governance.md](./151-090-Traceability-Evidence-and-Lifecycle-Governance.md) | Mapping of each FSO function to applicable standards: ECSS, CCSDS 141.0-B, ITU-R, IEC, NASA. |
| 100 | [`151-090-Traceability-Evidence-and-Lifecycle-Governance.md`](./151-090-Traceability-Evidence-and-Lifecycle-Governance.md) | Evidence package requirements and lifecycle review gates (PDR/CDR/ORR) for FSO subsystems. |

## §3 Footprint

| Attribute | Value |
|-----------|-------|
| Architecture | Space Technology Architecture (STA) |
| Master range | 100–199 |
| Code range | 150-159 |
| Section | 05 — Comunicaciones Espaciales |
| Subsection | 151 — Enlaces Ópticos |
| Subsubject | 000 — Overview |
| Primary Q-Division | Q-SPACE |
| Support Q-Divisions | Q-DATAGOV, Q-HPC |
| ORB support | ORB-PMO, ORB-LEG |
| Governance class | baseline |
| Folder path | `Q+ATLANTIDE/100-199_STA/150-159_Comunicaciones-Espaciales/151_Enlaces-Opticos/` |
| Document | `151-000-General.md` |
| Parent subsection | [README.md](./README.md) |
| Parent architecture | [../../README.md](../../README.md) |
| Parent baseline | [organization/Q+ATLANTIDE.md](../../../../organization/Q+ATLANTIDE.md) |

## §4 References & Citations

[^baseline]: Q+ATLANTIDE controlled baseline (v1.0.0). All documents in this subsection are governed under the Q+ATLANTIDE taxonomy and traceability ecosystem.[^n001]
[^archtable]: §3 Architecture Table (parent) — see [../../README.md](../../README.md) for the STA master architecture table.
[^qdiv]: Q-Division authority — Q-SPACE is the primary division authority for all STA 150-159 optical communications documents.
[^gov]: Governance class — baseline. Documents at this class require formal change control via ORB-PMO.
[^ecss50]: ECSS-E-ST-50C — *Space engineering: Communications* (ESA, 2008).
[^ccsds141]: CCSDS 141.0-B — *Optical Communications — Optical Link* (CCSDS, 2015).
[^iec60825]: IEC 60825-1 — *Safety of laser products — Part 1: Equipment classification and requirements* (IEC, 2014).
[^itur]: ITU-R S.1714 — *Free-space optical links on Earth* (ITU, 2005).
[^nasa4005]: NASA-STD-4005 — *LEO Spacecraft Charging Design Standard* (NASA, 2013).
[^n001]: Note N-001: Q+ATLANTIDE is a taxonomy and traceability ecosystem, not a mission or programme. All document IDs, baseline references, and governance entries are internal to the Q+ATLANTIDE register.

### Applicable industry standards

- ECSS-E-ST-50C — Space engineering: Communications (ESA, 2008)[^ecss50]
- ECSS-E-ST-10-03C — Space engineering: Testing (ESA, 2012)
- CCSDS 141.0-B — Optical Communications — Optical Link (CCSDS, 2015)[^ccsds141]
- ITU-R S.1714 — Free-space optical links on Earth (ITU, 2005)[^itur]
- IEC 60825-1 — Safety of laser products (IEC, 2014)[^iec60825]
- NASA-TM-2013-217496 — Overview of NASA's Optical Communications Program (NASA, 2013)
- NASA-STD-4005 — LEO Spacecraft Charging Design Standard (NASA, 2013)[^nasa4005]
- ETSI GS QKD 002 — Quantum Key Distribution; Use Cases (ETSI, 2010)
