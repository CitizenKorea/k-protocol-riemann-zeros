# Part IV: Theory-Driven Inverse Design of 2D High-Tc Superconducting Parents

[![ORCID](https://img.shields.io/badge/ORCID-0009--0004--3627--6997-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0004-3627-6997)
[![Zenodo Master DOI](https://img.shields.io/badge/Zenodo_Master_DOI-10.5281%2Fzenodo.22763956-blue?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.22763956)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white&style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Research_Preprint-blue?style=flat-square)

> **"Translating Prime Field Theory Decoupling into Solid-State Crystal Architectures"**  
> An autonomous inverse-design discovery engine enforcing 5-body planar $C_4$ coordination and steric apical gauge isolation, screening 61 parent compounds with first-principles electronic structure validation.

---

## Overview

This directory contains the manuscript, autonomous screening pipeline, and master structural database for **Part IV** of the unified K-Protocol framework.

Here, the analytical 5-body field theory (EFT) truncation proven in Part III ($k \le 5$, residue $R_{\ge 6} < 2.3 \times 10^{-7}$) is mapped directly to real-space crystal lattices. By enforcing a 5-body $C_4$ planar coordination ($1 \times \text{transition metal} + 4 \times \text{in-plane ligands}$) and steric apical gauge isolation ($c/a \ge 3.60$, $r_Y/r_X \ge 1.25$), the framework suppresses cross-plane hopping ($t_z \to 0$). The autonomous miner independently rediscovers the landmark high-Tc cuprate parent $Sr_2CuO_2Cl_2$ as a blind positive control, while discovering 60 additional stoichiometric candidates spanning $3d^9$ hole-type and $3d^1$ electron-type configurations.

* **Unified Master DOI:** [10.5281/zenodo.22763956](https://doi.org/10.5281/zenodo.22763956)
* **Parent Repository:** [k-protocol-riemann-zeros](https://github.com/CitizenKorea/k-protocol-riemann-zeros)

---

## Core Principles & Design Rules

### 1. Solid-State Realization of 5-Body Truncation
* Translates the mathematical 5-body cutoff into a physical $MX_4$ square plaquette where one transition metal $M$ couples strongly to four in-plane anions $X$ within a $D_{4h}$ local crystal field.
* Enforces single-orbital active manifolds ($d_{x^2-y^2}$ for $3d^9$ hole systems; $d_{xy}$ for $3d^1$ electron systems) by widening the planar-apical crystal field splitting.

### 2. Steric Apical Gauge Isolation ($t_z \to 0$)
* **Ionic Radius Ratio:** Enforces $r_Y / r_X \ge 1.25$, where the apical anion $Y$ (e.g., $Cl^-, Br^-, I^-$) possesses a substantially larger ionic radius than the in-plane anion $X$ (e.g., $O^{2-}, F^-$), physically displacing interlayer blocks.
* **Tetragonal Elongation:** Requires an axial lattice ratio $c/a \ge 3.60$, driving interlayer electronic decoupling and eliminating three-dimensional parasitic dispersion.

### 3. Blind Positive Control: Autonomous Rediscovery of $Sr_2CuO_2Cl_2$
* Operating strictly on combinatorial valence balance and steric criteria without empirical curve-fitting, the pipeline autonomously isolates $Sr_2CuO_2Cl_2$ ($c/a \approx 3.97$, $r_{Cl}/r_O \approx 1.29$) as a top-tier candidate, validating the predictive accuracy of the geometric criteria against known experimental high-Tc parent systems.

### 4. First-Principles Electronic Verification (Hurdle 1)
* Density Functional Theory (DFT) calculations using Quantum ESPRESSO demonstrate quasi-ideal 2D electronic isolation across the screened candidates:
  $$\Delta E_z \equiv \max_{k_x, k_y} \vert{}\epsilon(k_x, k_y, k_z = \pi) - \epsilon(k_x, k_y, k_z = 0)\vert{} < 0.015\text{ eV}$$
* Confirms that apical halogen substitution enforces rigorous two-dimensional electronic confinement along the critical conduction plane.

---

## Directory Structure

```text
04/
├── K_Protocol_2D_Superconducting_Parents_Inverse_Design.pdf   # Complete Part IV materials science manuscript
├── 01_k_protocol_miner.py                                     # Autonomous 2D materials screener & Quantum ESPRESSO generator
├── k_protocol_master_db.json                                  # Master structural database containing all 61 screened candidates
└── README.md                                                  # Directory documentation
```

---

## Execution & Workflow

The materials screening engine searches combinatorial stoichiometric spaces and generates fully parameterized Quantum ESPRESSO self-consistent field (SCF) input decks:

### Running Full Materials Screening
```bash
python 01_k_protocol_miner.py --database k_protocol_master_db.json
```

### Generating Quantum ESPRESSO DFT Input Files
```bash
python 01_k_protocol_miner.py --database k_protocol_master_db.json --generate-qe
```

---

## Candidate Database Overview (`k_protocol_master_db.json`)

The database indexes 61 stoichiometric candidate parent compounds categorized into:
* **Hole-type ($3d^9$, $Cu^{2+} / Ni^{1+}$):** e.g., $Sr_2CuO_2Cl_2$, $Ba_2CuO_2Cl_2$, $LaSrNiO_2Cl_2$, $Ca_2CuO_2Br_2$
* **Electron-type ($3d^1$, $V^{4+} / Ti^{3+}$):** e.g., $Cs_2VO_2I_2$, $Rb_2VO_2Br_2$, $K_2TiO_2F_2$

Each JSON record contains fractional coordinates, relaxed cell parameters ($a, b, c$), tolerance factors, and automated Monkhorst-Pack k-point meshes for downstream ab initio runs.

---

## Citation

```bibtex
@misc{k_protocol_master_suite_2026,
  author       = {{A Citizen of the Republic of Korea}},
  title        = {{K-Protocol Unified Research Suite: From Analytic Number Theory to 2D High-Tc Superconducting Inverse Design (Parts I--IV)}},
  howpublished = {Zenodo},
  year         = {2026},
  doi          = {10.5281/zenodo.22763956},
  url          = {[https://doi.org/10.5281/zenodo.22763956](https://doi.org/10.5281/zenodo.22763956)}
}
```
